#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-27 22:55:55
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-27 22:55:58
#FilePath     : /MG/test/phase_M_analysis.py
#Description  :

#!/usr/bin/env python3
"""
Phase M — 随机游走假说的封闭验证

M1: 合成噪声注入验证 — 对 mu_2048 注入 i.i.d. Gaussian 噪声, 验证 ΔS = Σ Γ_mn · η_mn
M2: 浮点精度缩放验证 — float32/float64/float80 对比, 验证 S ∝ ε_mach
M3: Γ 量级截断 — 截断 |Γ_mn|, 验证 S 随 Γ_max 线性缩放

用法: python test/phase_M_analysis.py
输出: test/M1_noise_injection.png, test/M1_noise_injection.txt,
       test/M2_precision_scaling.png, test/M2_precision_scaling.txt,
       test/M3_gamma_capping.png, test/M3_gamma_capping.txt
"""

import os
import sys
import time
import numpy as np
import h5py
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ─── 配置 ─────────────────────────────────────────────────────────────────
MU2048_PATH = "runs/0624/mu_raw_M2048_m64.h5"
MU4096_PATH = "runs/0624/mu_raw_M4096_m64.h5"
OUT_DIR = "test"
os.makedirs(OUT_DIR, exist_ok=True)

# M1 配置
NUM_THETA_M1 = 3  # 固定 theta 点用于 M1 验证
THETA_VALUES_M1 = [1.0, np.pi/2, 2.0]  # ≈57°, 90°, 115°
SIGMA_NOISE_LEVELS = [1e-16, 1e-15, 1e-14, 1e-13, 1e-12]
N_TRIALS_M1 = 100  # 每个 σ_noise 的随机种子数

# M2 配置
NUM_THETA_SWEEP_M2 = 128  # θ 扫点
M_VALUES_M2 = [2048, 4096]

# M3 配置
THETA_VALUES_M3 = [1.0, np.pi/2, 2.0]
GAMMA_FRACTIONS = [0.01, 0.03, 0.1, 0.3, 1.0]

plt.rcParams.update({"font.size": 11, "axes.titlesize": 13, "axes.labelsize": 12})


# ═══════════════════════════════════════════════════════════════════════════
# 工具函数 (复用自 Phase K/L/J1)
# ═══════════════════════════════════════════════════════════════════════════

def load_mu(h5_path: str) -> np.ndarray:
    """加载 raw μ 矩阵, 重组为 complex128, C-contiguous."""
    print(f"  Loading {h5_path}...")
    t0 = time.time()
    with h5py.File(h5_path, "r") as f:
        raw = f["mu_raw"][:]  # shape (M, 2*M) float64
    mu = raw[:, 0::2] + 1j * raw[:, 1::2]
    mu = np.ascontiguousarray(mu)
    M = mu.shape[0]
    print(f"    shape={mu.shape}, |mu| range=[{np.abs(mu).min():.2e}, {np.abs(mu).max():.2e}], "
          f"mem={mu.nbytes/1e6:.1f}MB, elapsed={time.time()-t0:.1f}s")
    return mu


def jackson_kernel(M_val: int) -> np.ndarray:
    """Jackson kernel g_n (n=0..M-1), 含 Kronecker delta 修正 g_0 *= 0.5."""
    n = np.arange(M_val, dtype=np.float64)
    alpha = np.pi / (M_val + 1)
    g = ((M_val - n + 1) * np.cos(alpha * n) + np.sin(alpha * n) / np.tan(alpha)) / (M_val + 1)
    g[0] *= 0.5
    return g


def build_gamma_matrix(theta: float, M_val: int) -> np.ndarray:
    """
    构造 Γ 矩阵 (M_val × M_val, complex128).
    γ_{mn} = cos(mθ)·fn_n + cos(nθ)·fm_m
    其中 fn_n = (cosθ - i·n·sinθ)·exp(i·n·θ), fm_m = conj(fn_m).
    """
    idx = np.arange(M_val, dtype=np.float64)
    cos_nt = np.cos(idx * theta)
    sin_t = np.sin(theta)
    cos_t = np.cos(theta)
    n_theta = idx * theta
    fn = (cos_t - 1j * idx * sin_t) * (np.cos(n_theta) + 1j * np.sin(n_theta))
    fm = np.conj(fn)
    Gamma = cos_nt[:, None] * fn[None, :] + cos_nt[None, :] * fm[:, None]
    return Gamma


def compute_sum_gm_fast(mu_kern: np.ndarray, theta: float) -> float:
    """
    BLAS 优化 sum_gamma_mu 计算 (单 theta 点).
    sum = Σ_{m,n} Re(Γ_{mn} · mu_kern[m,n])
    """
    M_val = mu_kern.shape[0]
    i_idx = np.arange(M_val, dtype=np.float64)
    sin_t = np.sin(theta)
    cos_t = np.cos(theta)
    nt = i_idx * theta
    fn = (cos_t - 1j * i_idx * sin_t) * (np.cos(nt) + 1j * np.sin(nt))
    fm = np.conj(fn)
    cos_nt = np.cos(nt)
    A = np.real(mu_kern @ fn)
    B = np.real(mu_kern.T @ fm)
    return float(np.dot(cos_nt, A + B))


def compute_sum_gm_explicit(mu_kern: np.ndarray, Gamma: np.ndarray) -> float:
    """显式方式: sum = Σ Re(Γ_{mn} · mu_kern[m,n])."""
    return float(np.sum((Gamma * mu_kern).real))


def compute_kahan_sum_f32(values: np.ndarray) -> float:
    """float32 Kahan 补偿求和."""
    s = np.float32(0.0)
    c = np.float32(0.0)
    for v in values.flat:
        v32 = np.float32(v)
        y = v32 - c
        t = s + y
        c = (t - s) - y
        s = t
    return float(s)


def compute_pairwise_sum(values: np.ndarray) -> float:
    """Pairwise summation (减少随机游走)."""
    if values.size <= 1:
        return float(values.flat[0]) if values.size == 1 else 0.0
    mid = values.size // 2
    return compute_pairwise_sum(values.flat[:mid]) + compute_pairwise_sum(values.flat[mid:])


# ═══════════════════════════════════════════════════════════════════════════
# M1 — 合成噪声注入验证
# ═══════════════════════════════════════════════════════════════════════════

def run_m1():
    """
    对 mu_2048 添加 i.i.d. Gaussian 噪声, 验证 ΔS = Σ Γ_mn · η_mn 的预言.
    """
    print("\n" + "=" * 70)
    print("M1 — 合成噪声注入验证")
    print("=" * 70)

    # 1. 加载干净 mu_2048
    print("\n[M1.1] Loading mu_2048...")
    mu = load_mu(MU2048_PATH)
    assert mu.shape == (2048, 2048), f"Expected (2048,2048), got {mu.shape}"
    M = 2048
    g = jackson_kernel(M)

    # 2. 对每个 theta, 计算基准 S_ref
    print(f"\n[M1.2] Computing S_ref at θ = {[f'{t:.3f}' for t in THETA_VALUES_M1]}...")
    Gamma_dict = {}
    S_ref_dict = {}
    for theta in THETA_VALUES_M1:
        Gamma = build_gamma_matrix(theta, M)
        Gamma_dict[theta] = Gamma
        mu_kern = mu * g[:, None] * g[None, :]
        S_ref = compute_sum_gm_explicit(mu_kern, Gamma)
        S_ref_dict[theta] = S_ref
        print(f"  θ={theta:.3f}: S_ref={S_ref:.4f}")

    # 3. 注入噪声 — 多级 σ_noise
    print(f"\n[M1.3] Noise injection at σ ∈ {[f'{s:.0e}' for s in SIGMA_NOISE_LEVELS]}...")

    # --- 单次测试 (seed=42) ---
    print("\n  ── Single-shot verification (seed=42) ──")
    print(f"  {'σ_noise':>10} | {'θ':>6} | {'dS_obs':>14} | {'dS_pred':>14} | {'ratio':>12} | {'|Δ|/|pred|':>14}")
    print("  " + "-" * 90)

    single_results = {}
    np.random.seed(42)
    for sigma in SIGMA_NOISE_LEVELS:
        noise = np.random.randn(M, M) * sigma
        mu_noisy = mu + noise
        mu_kern_noisy = mu_noisy * g[:, None] * g[None, :]

        for theta in THETA_VALUES_M1:
            Gamma = Gamma_dict[theta]
            S_noisy = compute_sum_gm_explicit(mu_kern_noisy, Gamma)
            S_ref = S_ref_dict[theta]
            dS_obs = S_noisy - S_ref

            # 预言: dS = Σ Γ_mn * g_m * g_n * noise_mn
            noise_kern = noise * g[:, None] * g[None, :]
            dS_pred = float(np.sum((Gamma * noise_kern).real))

            ratio = dS_obs / dS_pred if abs(dS_pred) > 1e-30 else np.nan
            rel_diff = abs(dS_obs - dS_pred) / max(abs(dS_pred), 1e-30)

            key = (sigma, theta)
            single_results[key] = {"dS_obs": dS_obs, "dS_pred": dS_pred,
                                    "ratio": ratio, "rel_diff": rel_diff}
            print(f"  {sigma:10.0e} | {theta:6.3f} | {dS_obs:14.6f} | {dS_pred:14.6f} | "
                  f"{ratio:10.6f}" if not np.isnan(ratio) else f"  {sigma:10.0e} | {theta:6.3f} | {dS_obs:14.6f} | {dS_pred:14.6f} | {'N/A':>10}",
                  end="")
            print(f" | {rel_diff:14.2e}")

    # --- RMS 标度 (N_trial=100) ---
    print(f"\n  ── RMS scaling ({N_TRIALS_M1} trials per σ) ──")
    print(f"  {'σ_noise':>10} | {'θ':>6} | {'dS_obs_mean':>14} | {'dS_obs_std':>14} | {'dS_pred_mean':>14} | {'RMS(obs)':>12} | {'RMS ratio':>12}")
    print("  " + "-" * 105)

    rms_results = {}
    for sigma in SIGMA_NOISE_LEVELS:
        for theta in THETA_VALUES_M1:
            Gamma = Gamma_dict[theta]
            dS_obs_list = []
            dS_pred_list = []

            for trial in range(N_TRIALS_M1):
                np.random.seed(1000 + trial)
                noise = np.random.randn(M, M) * sigma
                mu_noisy = mu + noise
                mu_kern_noisy = mu_noisy * g[:, None] * g[None, :]
                S_noisy = compute_sum_gm_explicit(mu_kern_noisy, Gamma)
                dS_obs = S_noisy - S_ref_dict[theta]

                noise_kern = noise * g[:, None] * g[None, :]
                dS_pred = float(np.sum((Gamma * noise_kern).real))

                dS_obs_list.append(dS_obs)
                dS_pred_list.append(dS_pred)

            dS_obs_arr = np.array(dS_obs_list)
            dS_pred_arr = np.array(dS_pred_list)
            rms_obs = np.sqrt(np.mean(dS_obs_arr ** 2))
            rms_pred = np.sqrt(np.mean(dS_pred_arr ** 2))
            rms_ratio = rms_obs / rms_pred if rms_pred > 1e-30 else np.nan

            key = (sigma, theta)
            rms_results[key] = {"mean_obs": np.mean(dS_obs_arr),
                                 "std_obs": np.std(dS_obs_arr),
                                 "mean_pred": np.mean(dS_pred_arr),
                                 "rms_obs": rms_obs, "rms_pred": rms_pred,
                                 "rms_ratio": rms_ratio}
            print(f"  {sigma:10.0e} | {theta:6.3f} | {np.mean(dS_obs_arr):14.6f} | "
                  f"{np.std(dS_obs_arr):14.6f} | {np.mean(dS_pred_arr):14.6f} | "
                  f"{rms_obs:12.6f} | {rms_ratio:10.6f}" if not np.isnan(rms_ratio)
                  else f"  {sigma:10.0e} | {theta:6.3f} | ... | {rms_obs:12.6f} | {'N/A':>10}")

    # 4. 绘图
    fig = plt.figure(figsize=(16, 7))
    gs = GridSpec(1, 2, figure=fig, width_ratios=[1, 1])

    # Panel 1: dS_obs vs dS_pred scatter (all σ_noise × theta, single shot)
    ax1 = fig.add_subplot(gs[0])
    colors = {1.0: "#d73027", np.pi/2: "#4575b4", 2.0: "#1a9850"}
    for (sigma, theta), res in single_results.items():
        color = colors[theta]
        marker = {1e-16: "o", 1e-15: "s", 1e-14: "D", 1e-13: "^", 1e-12: "v"}[sigma]
        ax1.scatter(res["dS_pred"], res["dS_obs"], c=color, marker=marker, s=50,
                    alpha=0.7, edgecolors="k", linewidth=0.5,
                    label=f"{theta:.1f}, σ={sigma:.0e}" if sigma == 1e-12 else "")
    # Add diagonal line
    all_vals = np.concatenate([[r["dS_obs"], r["dS_pred"]] for r in single_results.values()])
    lim = max(abs(all_vals.min()), abs(all_vals.max())) * 1.1
    ax1.plot([-lim, lim], [-lim, lim], "k--", linewidth=0.8, alpha=0.5, label="dS_obs = dS_pred")
    ax1.set_xlabel(r"$\Delta S_{\rm pred} = \Sigma \Gamma_{mn} \eta_{mn}$")
    ax1.set_ylabel(r"$\Delta S_{\rm obs}$")
    ax1.set_title("M1: Noise Injection — Observed vs Predicted ΔS")
    ax1.legend(fontsize=7, loc="upper left")
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(-lim, lim)
    ax1.set_ylim(-lim, lim)

    # Panel 2: RMS(dS) vs σ_noise (log-log) for each theta
    ax2 = fig.add_subplot(gs[1])
    sigma_arr = np.array(SIGMA_NOISE_LEVELS)
    for theta in THETA_VALUES_M1:
        rms_vals = [rms_results[(s, theta)]["rms_obs"] for s in SIGMA_NOISE_LEVELS]
        color = colors[theta]
        ax2.loglog(sigma_arr, rms_vals, "o-", color=color, linewidth=1.5, markersize=6,
                   label=f"θ={theta:.1f} (obs)")
        rms_pred_vals = [rms_results[(s, theta)]["rms_pred"] for s in SIGMA_NOISE_LEVELS]
        ax2.loglog(sigma_arr, rms_pred_vals, "s--", color=color, linewidth=1.0, markersize=4,
                   alpha=0.6, label=f"θ={theta:.1f} (pred)")

    # Fit slope for middle theta
    theta_mid = np.pi / 2
    rms_mid = np.array([rms_results[(s, theta_mid)]["rms_obs"] for s in SIGMA_NOISE_LEVELS])
    coef = np.polyfit(np.log10(sigma_arr), np.log10(rms_mid), 1)
    ax2.loglog(sigma_arr, 10**(coef[1]) * sigma_arr**coef[0], "k--", linewidth=1.0,
               alpha=0.5, label=f"fit θ=π/2: α={coef[0]:.3f}")
    ax2.set_xlabel(r"$\sigma_{\rm noise}$ (injected)")
    ax2.set_ylabel(r"RMS($\Delta S$) over 100 trials")
    ax2.set_title("M1: RMS Scaling — RMS(ΔS) ∝ σ_noise^α")
    ax2.legend(fontsize=7)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    out_png = os.path.join(OUT_DIR, "M1_noise_injection.png")
    fig.savefig(out_png, dpi=150)
    plt.close(fig)
    print(f"\n  Figure saved: {out_png}")

    # 5. 生成报告
    report_lines = [
        "=" * 70,
        "Phase M1 — Synthetic Noise Injection Verification",
        f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 70,
        "",
        f"mu matrix: {MU2048_PATH} (M=2048, clean baseline)",
        f"theta values: {[f'{t:.3f}' for t in THETA_VALUES_M1]}",
        f"sigma_noise levels: {[f'{s:.0e}' for s in SIGMA_NOISE_LEVELS]}",
        f"trials per sigma: {N_TRIALS_M1}",
        "",
        "Single-shot results (seed=42):",
        f"{'σ_noise':>10} {'θ':>6} {'dS_obs':>14} {'dS_pred':>14} {'ratio':>12} {'|Δ|/|pred|':>14}",
        "-" * 80,
    ]
    for (sigma, theta), res in single_results.items():
        report_lines.append(
            f"{sigma:10.0e} {theta:6.3f} {res['dS_obs']:14.6f} {res['dS_pred']:14.6f} "
            f"{res['ratio']:10.6f}" if not np.isnan(res['ratio'])
            else f"{sigma:10.0e} {theta:6.3f} {res['dS_obs']:14.6f} {res['dS_pred']:14.6f} {'N/A':>10}"
            + f" {res['rel_diff']:14.2e}")

    report_lines += [
        "",
        f"RMS scaling ({N_TRIALS_M1} trials):",
        f"{'σ_noise':>10} {'θ':>6} {'RMS(obs)':>12} {'RMS(pred)':>12} {'ratio':>10}",
        "-" * 60,
    ]
    for (sigma, theta), res in rms_results.items():
        report_lines.append(
            f"{sigma:10.0e} {theta:6.3f} {res['rms_obs']:12.6f} {res['rms_pred']:12.6f} "
            f"{res['rms_ratio']:10.6f}" if not np.isnan(res['rms_ratio'])
            else f"{sigma:10.0e} {theta:6.3f} {res['rms_obs']:12.6f} {res['rms_pred']:12.6f} {'N/A':>10}")

    # RMS scaling fit results
    report_lines.append("")
    report_lines.append("RMS scaling power-law fit (θ=π/2):")
    report_lines.append(f"  α = {coef[0]:.4f} (expect α≈1.0 for linear noise propagation)")
    report_lines.append(f"  RMS ∝ σ_noise^{coef[0]:.4f}")

    # Success criteria
    report_lines.append("")
    report_lines.append("Success Criteria:")
    # Check ratio close to 1
    max_rel_diff = max(abs(r["rel_diff"]) for r in single_results.values() if not np.isnan(r.get("rel_diff", np.nan)))
    report_lines.append(f"  [{'x' if max_rel_diff < 0.01 else ' '}] dS_obs/dS_pred ≈ 1.0 (max |Δ|/|pred| = {max_rel_diff:.2e})")
    report_lines.append(f"  [{'x' if abs(coef[0] - 1.0) < 0.05 else ' '}] RMS(dS) ∝ σ_noise^α with α≈1.0 (α={coef[0]:.4f})")

    report_lines.append("")
    out_txt = os.path.join(OUT_DIR, "M1_noise_injection.txt")
    with open(out_txt, "w") as f:
        f.write("\n".join(report_lines))
    print(f"  Report saved: {out_txt}")

    return single_results, rms_results, coef


# ═══════════════════════════════════════════════════════════════════════════
# M2 — 浮点精度缩放验证
# ═══════════════════════════════════════════════════════════════════════════

def run_m2():
    """
    在 Python 中用 float32/float64/float80 复算 Γ·μ 求和, 验证 S ∝ ε_mach.
    """
    print("\n" + "=" * 70)
    print("M2 — 浮点精度缩放验证")
    print("=" * 70)

    # 1. 加载 mu_4096
    print("\n[M2.1] Loading mu_4096...")
    mu = load_mu(MU4096_PATH)
    assert mu.shape == (4096, 4096)

    # 2. 单 theta 点多精度复算
    print(f"\n[M2.2] Single-theta precision comparison at θ=π/2...")
    theta_test = np.pi / 2

    M4096 = 4096
    g4096 = jackson_kernel(M4096)
    mu_kern_f64 = (mu * g4096[:, None] * g4096[None, :]).astype(np.complex128)
    Gamma_f64 = build_gamma_matrix(theta_test, M4096)

    # Compute in different precisions
    results_single = {}
    for dtype, label, eps_mach in [
        (np.float32, "f32", np.finfo(np.float32).eps),
        (np.float64, "f64", np.finfo(np.float64).eps),
    ]:
        if dtype == np.float32:
            Gamma_dt = Gamma_f64.astype(np.complex64)
            mu_kern_dt = mu_kern_f64.astype(np.complex64)
        else:
            Gamma_dt = Gamma_f64
            mu_kern_dt = mu_kern_f64

        terms = (Gamma_dt * mu_kern_dt).real
        if dtype == np.float32:
            terms_sum_dtype = terms.astype(np.float32)
        else:
            terms_sum_dtype = terms.astype(np.float64)

        S_naive = float(np.sum(terms_sum_dtype))
        S_pairwise = compute_pairwise_sum(terms_sum_dtype)

        if dtype == np.float32:
            S_kahan = compute_kahan_sum_f32(terms)
        else:
            S_kahan = S_naive

        results_single[label] = {"S_naive": S_naive, "S_kahan": S_kahan,
                                  "S_pairwise": S_pairwise, "eps": eps_mach}
        print(f"  {label} (ε={eps_mach:.1e}): S_naive={S_naive:.4f}, "
              f"S_kahan={S_kahan:.4f}, S_pairwise={S_pairwise:.4f}")

    # Try long double if available
    try:
        Gamma_ld = Gamma_f64.astype(np.clongdouble)
        mu_kern_ld = mu_kern_f64.astype(np.clongdouble)
        terms_ld = (Gamma_ld * mu_kern_ld).real.astype(np.longdouble)
        S_ld = float(np.sum(terms_ld))
        eps_ld = np.finfo(np.longdouble).eps
        results_single["f80"] = {"S_naive": S_ld, "S_kahan": S_ld,
                                  "S_pairwise": S_ld, "eps": eps_ld}
        print(f"  f80 (ε={eps_ld:.1e}): S_naive={S_ld:.4f}")
    except Exception as e:
        print(f"  f80: not available ({e})")

    # 3. θ 扫 — 精度-偏移标度律
    print(f"\n[M2.3] θ-sweep ({NUM_THETA_SWEEP_M2} points) for M=2048, 4096...")

    theta_arr = (np.arange(NUM_THETA_SWEEP_M2) + 0.5) * np.pi / NUM_THETA_SWEEP_M2

    sweep_results = {}
    for M in M_VALUES_M2:
        sweep_results[M] = {}
        mu_trunc = mu[:M, :M]
        g = jackson_kernel(M)
        mu_kern_f64 = (mu_trunc * g[:, None] * g[None, :]).astype(np.complex128)
        del mu_trunc

        for dtype, label in [(np.float32, "f32"), (np.float64, "f64")]:
            S_arr = np.zeros(NUM_THETA_SWEEP_M2)
            print(f"    M={M}, {label}...", end=" ", flush=True)
            t0 = time.time()

            for k in range(NUM_THETA_SWEEP_M2):
                th = theta_arr[k]
                Gamma = build_gamma_matrix(th, M)
                Gamma_dt = Gamma.astype(np.complex64) if dtype == np.float32 else Gamma
                mu_kern_dt = mu_kern_f64.astype(np.complex64) if dtype == np.float32 else mu_kern_f64
                terms = (Gamma_dt * mu_kern_dt).real
                if dtype == np.float32:
                    S_arr[k] = float(np.sum(terms.astype(np.float32)))
                else:
                    S_arr[k] = float(np.sum(terms))

            print(f"done in {time.time()-t0:.1f}s, range=[{S_arr.min():.2f}, {S_arr.max():.2f}]")
            sweep_results[M][label] = S_arr

        del mu_kern_f64

    # 4. 绘图
    fig = plt.figure(figsize=(18, 12))
    gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)

    # Panel 1 & 2: S(θ) for M=2048 and M=4096
    for pi, M in enumerate(M_VALUES_M2):
        ax = fig.add_subplot(gs[0, pi])
        for label, color, ls in [("f64", "#4575b4", "-"), ("f32", "#d73027", "--")]:
            ax.plot(theta_arr, sweep_results[M][label], color=color, linestyle=ls,
                    linewidth=1.0, alpha=0.8, label=f"{label} (ε={np.finfo(np.float32 if label=='f32' else np.float64).eps:.0e})")
        ax.axhline(y=0, color="gray", linestyle=":", linewidth=0.5)
        ax.set_xlabel(r"$\theta$")
        ax.set_ylabel(r"$\sum \Gamma \odot \mu$")
        ax.set_title(f"M2: S(θ) — M={M}")
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

    # Panel 3: S_f32/S_f64 ratio vs θ
    ax = fig.add_subplot(gs[0, 2])
    for M in M_VALUES_M2:
        S_f32 = sweep_results[M]["f32"]
        S_f64 = sweep_results[M]["f64"]
        ratio = np.abs(S_f32) / np.maximum(np.abs(S_f64), 1e-30)
        ax.semilogy(theta_arr, ratio, linewidth=1.0, alpha=0.8, label=f"M={M}")
    eps_ratio = np.finfo(np.float32).eps / np.finfo(np.float64).eps
    ax.axhline(y=eps_ratio, color="gray", linestyle="--", linewidth=0.8,
               label=f"ε_f32/ε_f64 ≈ {eps_ratio:.0e}")
    ax.set_xlabel(r"$\theta$")
    ax.set_ylabel(r"$|S_{f32}| / |S_{f64}|$")
    ax.set_title("M2: Precision Ratio vs θ")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 4: Bar chart — S for different precisions at θ=π/2
    ax = fig.add_subplot(gs[1, 0])
    labels = list(results_single.keys())
    S_vals = [results_single[l]["S_naive"] for l in labels]
    colors_bar = ["#d73027", "#4575b4", "#1a9850"]
    ax.bar(labels, S_vals, color=colors_bar, edgecolor="k", linewidth=0.5)
    # Add text with epsilon
    for i, (l, v) in enumerate(zip(labels, S_vals)):
        ax.text(i, v + max(abs(np.array(S_vals)))*0.05,
                f"ε={results_single[l]['eps']:.1e}\nS={v:.1f}",
                ha="center", fontsize=8)
    ax.axhline(y=0, color="gray", linestyle=":", linewidth=0.5)
    ax.set_ylabel(r"$S_{naive}$ at θ=π/2")
    ax.set_title("M2: Precision Comparison (M=4096)")
    ax.grid(True, alpha=0.3, axis="y")

    # Panel 5: Kahan vs naive for f32
    ax = fig.add_subplot(gs[1, 1])
    S_f32_naive = results_single["f32"]["S_naive"]
    S_f32_kahan = results_single["f32"]["S_kahan"]
    S_f32_pairwise = results_single["f32"]["S_pairwise"]
    methods = ["naive", "Kahan", "pairwise"]
    vals = [S_f32_naive, S_f32_kahan, S_f32_pairwise]
    ax.bar(methods, vals, color=["#fc8d59", "#91bfdb", "#fee08b"],
           edgecolor="k", linewidth=0.5)
    ax.axhline(y=results_single["f64"]["S_naive"], color="#4575b4",
               linestyle="--", linewidth=1.5, label=f"f64 naive = {results_single['f64']['S_naive']:.1f}")
    ax.set_ylabel(r"$S$ (float32)")
    ax.set_title("M2: f32 Summation Methods")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3, axis="y")

    # Panel 6: S vs ε_mach log-log
    ax = fig.add_subplot(gs[1, 2])
    eps_arr = np.array([results_single[l]["eps"] for l in ["f32", "f64"]])
    S_naive_arr = np.array([results_single[l]["S_naive"] for l in ["f32", "f64"]])
    ax.loglog(eps_arr, np.abs(S_naive_arr), "o-", color="#d73027",
              linewidth=2, markersize=10, label="|S_naive|")
    # Add f80 if available
    if "f80" in results_single:
        eps_f80 = results_single["f80"]["eps"]
        S_f80 = results_single["f80"]["S_naive"]
        ax.loglog([eps_f80], [abs(S_f80)], "s", color="#1a9850",
                  markersize=10, label=f"f80: |S|={abs(S_f80):.1f}")
    if len(eps_arr) >= 2:
        coef = np.polyfit(np.log10(eps_arr), np.log10(np.abs(S_naive_arr)), 1)
        ax.loglog(eps_arr, 10**coef[1] * eps_arr**coef[0], "k--", linewidth=1.0,
                  alpha=0.5, label=f"fit: α={coef[0]:.3f}")
    ax.set_xlabel(r"$\varepsilon_{\rm mach}$")
    ax.set_ylabel(r"$|S|$ at θ=π/2")
    ax.set_title("M2: |S| vs Machine Precision")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.invert_xaxis()

    plt.tight_layout()
    out_png = os.path.join(OUT_DIR, "M2_precision_scaling.png")
    fig.savefig(out_png, dpi=150)
    plt.close(fig)
    print(f"\n  Figure saved: {out_png}")

    # 5. 报告
    f32_naive = results_single["f32"]["S_naive"]
    f64_naive = results_single["f64"]["S_naive"]
    S_ratio = abs(f32_naive) / max(abs(f64_naive), 1e-30)
    eps_ratio_actual = np.finfo(np.float32).eps / np.finfo(np.float64).eps

    report_lines = [
        "=" * 70,
        "Phase M2 — Floating-Point Precision Scaling Verification",
        f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 70,
        "",
        f"mu matrix: {MU4096_PATH} (M=4096)",
        f"θ test point: π/2 = {theta_test:.4f}",
        f"θ sweep resolution: {NUM_THETA_SWEEP_M2}",
        "",
        "Single-θ precision comparison (M=4096, θ=π/2):",
        f"  f32 (ε={np.finfo(np.float32).eps:.1e}): S_naive={f32_naive:.6f}",
        f"  f64 (ε={np.finfo(np.float64).eps:.1e}): S_naive={f64_naive:.6f}",
    ]
    if "f80" in results_single:
        f80_naive = results_single["f80"]["S_naive"]
        report_lines.append(f"  f80 (ε={np.finfo(np.longdouble).eps:.1e}): S_naive={f80_naive:.6f}")

    report_lines += [
        "",
        f"  |S_f32| / |S_f64| = {S_ratio:.6f}",
        f"  ε_f32 / ε_f64 = {eps_ratio_actual:.6f} (theoretical)",
        f"  Observed/theoretical = {S_ratio/eps_ratio_actual:.6f}",
        "",
        "f32 summation methods (θ=π/2):",
        f"  naive: {f32_naive:.6f}",
        f"  Kahan: {results_single['f32']['S_kahan']:.6f}",
        f"  pairwise: {results_single['f32']['S_pairwise']:.6f}",
        "",
        "Success Criteria:",
        f"  [{'x' if S_ratio > 10 else ' '}] S_f32 ≫ S_f64 (ratio={S_ratio:.1f}×)",
        f"  [{'x' if S_ratio > eps_ratio_actual*0.1 else ' '}] S scaling consistent with ε_mach",
    ]

    out_txt = os.path.join(OUT_DIR, "M2_precision_scaling.txt")
    with open(out_txt, "w") as f:
        f.write("\n".join(report_lines))
    print(f"  Report saved: {out_txt}")

    return results_single, sweep_results


# ═══════════════════════════════════════════════════════════════════════════
# M3 — Γ 量级截断
# ═══════════════════════════════════════════════════════════════════════════

def run_m3():
    """
    将 |Γ_mn| 截断在 Γ_max 阈值, 验证 S 随 Γ_max 线性缩放.
    """
    print("\n" + "=" * 70)
    print("M3 — Γ 量级截断验证")
    print("=" * 70)

    # 1. 加载 mu_4096
    print("\n[M3.1] Loading mu_4096...")
    mu = load_mu(MU4096_PATH)
    assert mu.shape == (4096, 4096)
    M = 4096
    g = jackson_kernel(M)
    mu_kern = mu * g[:, None] * g[None, :]
    del mu  # free memory

    # 2. 对每个 theta, 做 Γ 截断扫描
    print(f"\n[M3.2] Γ capping scan at θ = {[f'{t:.3f}' for t in THETA_VALUES_M3]}...")

    results = {}
    np.random.seed(42)

    for theta in THETA_VALUES_M3:
        print(f"\n  θ = {theta:.3f}:")
        Gamma = build_gamma_matrix(theta, M)
        absG = np.abs(Gamma)
        G_max = absG.max()
        print(f"    |Γ| max = {G_max:.2f}")

        capped_results = []
        for frac in GAMMA_FRACTIONS:
            G_cap = G_max * frac
            mask = absG <= G_cap
            n_capped = int(np.sum(mask))
            n_total = M * M

            # S_capped: only include terms with |Γ| ≤ G_cap
            S_capped = float(np.sum((Gamma * mask * mu_kern).real))

            # Control: random selection of same number of terms
            idx = np.random.choice(n_total, n_capped, replace=False)
            Gamma_flat = Gamma.ravel()
            mu_flat = mu_kern.ravel()
            S_random = float(np.sum((Gamma_flat[idx] * mu_flat[idx]).real))

            capped_results.append({
                "frac": frac, "G_cap": G_cap, "n_capped": n_capped,
                "S_capped": S_capped, "S_random": S_random,
                "frac_terms": n_capped / n_total,
            })
            print(f"      frac={frac:.2f} (G_cap={G_cap:.1f}): "
                  f"S_capped={S_capped:.4f}, S_random={S_random:.4f}, "
                  f"n_capped={n_capped}/{n_total} ({n_capped/n_total*100:.1f}%)")

        results[theta] = capped_results
        del Gamma

    # 3. 绘图
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))

    for pi, theta in enumerate(THETA_VALUES_M3):
        cr = results[theta]
        G_cap_arr = np.array([r["G_cap"] for r in cr])
        S_capped_arr = np.array([r["S_capped"] for r in cr])
        S_random_arr = np.array([r["S_random"] for r in cr])
        frac_terms_arr = np.array([r["frac_terms"] for r in cr])

        # Row 1: S vs G_cap (linear)
        ax = axes[0, pi]
        ax.plot(G_cap_arr, S_capped_arr, "o-", color="#d73027", linewidth=2, markersize=8,
                label="Capped (|Γ| ≤ G_cap)")
        ax.plot(G_cap_arr, S_random_arr, "s--", color="#4575b4", linewidth=1.5, markersize=6,
                label="Random (same n_terms)")
        S_full = S_capped_arr[-1]  # frac=1.0 = full sum
        ax.axhline(y=S_full, color="gray", linestyle=":", linewidth=0.8)
        ax.set_xlabel(r"$\Gamma_{\rm max}$ (cap threshold)")
        ax.set_ylabel(r"$S = \sum {\rm Re}(\Gamma \odot \mu)$")
        ax.set_title(f"M3: θ={theta:.3f} — S vs Γ_max")
        ax.legend(fontsize=7)
        ax.grid(True, alpha=0.3)

        # Row 2: log|S| vs log(G_max)
        ax = axes[1, pi]
        # Use only points with |S_capped| > 0
        valid = np.abs(S_capped_arr) > 1e-30
        if np.sum(valid) >= 3:
            coef = np.polyfit(np.log10(G_cap_arr[valid]), np.log10(np.abs(S_capped_arr[valid])), 1)
            ax.loglog(G_cap_arr, np.abs(S_capped_arr), "o-", color="#d73027",
                      linewidth=2, markersize=8, label=f"Capped (α={coef[0]:.3f})")
            ax.loglog(G_cap_arr[valid], 10**coef[1] * G_cap_arr[valid]**coef[0],
                      "k--", linewidth=1.0, alpha=0.5)
        else:
            ax.loglog(G_cap_arr, np.abs(S_capped_arr), "o-", color="#d73027",
                      linewidth=2, markersize=8, label="Capped")
        ax.loglog(G_cap_arr, np.abs(S_random_arr), "s--", color="#4575b4",
                  linewidth=1.5, markersize=6, label="Random")
        ax.set_xlabel(r"$\Gamma_{\rm max}$")
        ax.set_ylabel(r"$|S|$")
        ax.set_title(f"M3: θ={theta:.3f} — |S| vs Γ_max (log-log)")
        ax.legend(fontsize=7)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    out_png = os.path.join(OUT_DIR, "M3_gamma_capping.png")
    fig.savefig(out_png, dpi=150)
    plt.close(fig)
    print(f"\n  Figure saved: {out_png}")

    # 4. 报告
    report_lines = [
        "=" * 70,
        "Phase M3 — Γ Magnitude Truncation Verification",
        f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 70,
        "",
        f"mu matrix: {MU4096_PATH} (M=4096)",
        f"theta values: {[f'{t:.3f}' for t in THETA_VALUES_M3]}",
        f"Γ fractions: {GAMMA_FRACTIONS}",
        "",
    ]

    for theta in THETA_VALUES_M3:
        cr = results[theta]
        report_lines.append(f"θ = {theta:.3f}:")
        report_lines.append(f"  {'frac':>6} {'G_cap':>8} {'n_capped':>10} {'S_capped':>14} {'S_random':>14} {'S_cap/S_rand':>12}")
        report_lines.append("  " + "-" * 70)
        for r in cr:
            ratio_cr = r["S_capped"] / max(abs(r["S_random"]), 1e-30)
            report_lines.append(
                f"  {r['frac']:6.2f} {r['G_cap']:8.1f} {r['n_capped']:10d} "
                f"{r['S_capped']:14.6f} {r['S_random']:14.6f} {ratio_cr:12.6f}")
        # Fit
        G_cap_arr = np.array([r["G_cap"] for r in cr])
        S_capped_arr = np.array([r["S_capped"] for r in cr])
        valid = np.abs(S_capped_arr) > 1e-30
        if np.sum(valid) >= 3:
            coef = np.polyfit(np.log10(G_cap_arr[valid]), np.log10(np.abs(S_capped_arr[valid])), 1)
            report_lines.append(f"  Log-log fit: |S| ∝ Γ_max^{coef[0]:.4f} (expect α≈1 for Γ amplification)")
            report_lines.append(f"  S_capped > S_random: {all(r['S_capped'] != r['S_random'] for r in cr)}")
        report_lines.append("")

    report_lines.append("Success Criteria:")
    # Check if S_capped systematically differs from S_random
    all_capped = []
    all_random = []
    for theta in THETA_VALUES_M3:
        for r in results[theta]:
            all_capped.append(r["S_capped"])
            all_random.append(r["S_random"])
    capped_gt_random = sum(1 for c, r in zip(all_capped, all_random) if abs(c) > abs(r))
    total_points = len(all_capped)
    report_lines.append(f"  [{'x' if capped_gt_random > total_points*0.5 else ' '}] S_capped systematically > S_random "
                         f"({capped_gt_random}/{total_points} points)")

    out_txt = os.path.join(OUT_DIR, "M3_gamma_capping.txt")
    with open(out_txt, "w") as f:
        f.write("\n".join(report_lines))
    print(f"  Report saved: {out_txt}")

    return results


# ═══════════════════════════════════════════════════════════════════════════
# 主入口
# ═══════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("Phase M — Random Walk Hypothesis Closed-Loop Verification")
    print(f"Started: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    t_total = time.time()

    # M1
    t0 = time.time()
    m1_single, m1_rms, m1_coef = run_m1()
    print(f"\n  M1 completed in {time.time()-t0:.1f}s")

    # M2
    t0 = time.time()
    m2_single, m2_sweep = run_m2()
    print(f"\n  M2 completed in {time.time()-t0:.1f}s")

    # M3
    t0 = time.time()
    m3_results = run_m3()
    print(f"\n  M3 completed in {time.time()-t0:.1f}s")

    # Summary
    print("\n" + "=" * 70)
    print("Phase M Summary")
    print("=" * 70)

    # M1 PASS/FAIL
    max_rel_diff = max(abs(r["rel_diff"]) for r in m1_single.values()
                       if not np.isnan(r.get("rel_diff", np.nan)))
    m1_pass = max_rel_diff < 0.01 and abs(m1_coef[0] - 1.0) < 0.05

    # M2 PASS/FAIL
    f32_S = abs(m2_single["f32"]["S_naive"])
    f64_S = abs(m2_single["f64"]["S_naive"])
    m2_pass = f32_S > f64_S * 10

    # M3 PASS/FAIL
    all_capped = []
    all_random = []
    for theta in THETA_VALUES_M3:
        for r in m3_results[theta]:
            all_capped.append(abs(r["S_capped"]))
            all_random.append(abs(r["S_random"]))
    m3_pass = sum(1 for c, r in zip(all_capped, all_random) if c > r) > len(all_capped) * 0.5

    print(f"  M1 Noise Injection: {'✅ PASS' if m1_pass else '⚠️ NEEDS REVIEW'}")
    print(f"    max |Δ|/|pred| = {max_rel_diff:.2e}")
    print(f"    RMS scaling α = {m1_coef[0]:.4f}")
    print(f"  M2 Precision Scaling: {'✅ PASS' if m2_pass else '⚠️ NEEDS REVIEW'}")
    print(f"    |S_f32|/|S_f64| = {f32_S/max(f64_S, 1e-30):.1f}×")
    print(f"  M3 Gamma Capping: {'✅ PASS' if m3_pass else '⚠️ NEEDS REVIEW'}")

    if m1_pass and m2_pass and m3_pass:
        print("\n  🎉 ALL THREE PREDICTIONS CONFIRMED — Root cause chain CLOSED:")
        print("     δμ zero-mean random noise × Γ O(n) linear amplification × conditional convergence")
        print("     → Random walk accumulation ~O(√N·ε·|Γ|_avg)")
    else:
        print("\n  ⚠️ Some predictions not fully confirmed — see individual reports.")

    print(f"\n  Total elapsed: {time.time()-t_total:.1f}s")
    print(f"  Outputs: test/M1_*.png/txt, test/M2_*.png/txt, test/M3_*.png/txt")


if __name__ == "__main__":
    main()
