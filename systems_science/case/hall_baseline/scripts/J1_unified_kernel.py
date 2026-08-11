#!/usr/bin/env python3
"""
J1_unified_kernel.py — Phase J1: 统一 Jackson 核截断验证

从 mu_raw_M4096_m64.h5 (raw μ, 无 Jackson 核) 出发，
截断到 M' ∈ {2048, 2560, 3072, 3584, 4096}，
对比两种核处理方式:
  - standard: 各 M' 使用自己的 g^(M') Jackson 核
  - unified:  所有 M' 统一使用 g^(4096) Jackson 核 (截断到 M')

数学优化: 利用 γ_{ij} = cos(iθ)*fn_j + cos(jθ)*fm_i 的秩-2 结构，
sum_gm 用 2 次 BLAS gemv 代替 M×M γ 矩阵构建:
  A = Re(μ @ fn),  B = Re(μ^T @ fm)
  sum_gm = cos_nt · (A + B)

用法: python test/J1_unified_kernel.py
输出: test/J1_unified_kernel_S_vs_M.png, test/J1_unified_kernel_report.txt
"""

import sys
import os
import numpy as np
import h5py
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import time

# ─── 配置 ─────────────────────────────────────────────────────────────────
H5_PATH = "runs/0624/mu_raw_M4096_m64.h5"
OUT_DIR = "test"
os.makedirs(OUT_DIR, exist_ok=True)

# 物理参数 (来自 configs/sigma/hall_m64_M4096_save_mu.yaml + 自动检测)
RESCALE = 17.0         # auto-detected bandwidth ≈ 17 eV (rescale=-1)
RESCALE_CENTER = 0.0   # eV
TEMPERATURE = 10.0     # K
BETA = 1.0 / (8.617333262145e-5 * TEMPERATURE)  # eV⁻¹, ≈ 1160.45
NUM_THETA = 2048       # θ 积分点数
ENERGIES = [-1.5, 0.0, 1.5]  # eV — 对 S(M) 分析, E_F=0 最关键

# M 扫描范围
M_TARGETS = [2048, 2560, 3072, 3584, 4096]
M_FULL = 4096

plt.rcParams.update({"font.size": 11, "axes.titlesize": 13, "axes.labelsize": 12})


# ─── 工具函数 ─────────────────────────────────────────────────────────────

def load_mu_raw(h5_path: str) -> np.ndarray:
    """加载 raw μ 矩阵 (无 Jackson 核), 重组为 complex128, C-contiguous."""
    print(f"Loading {h5_path}...")
    t0 = time.time()
    with h5py.File(h5_path, "r") as f:
        raw = f["mu_raw"][:]  # shape (M, 2*M) float64
    mu = raw[:, 0::2] + 1j * raw[:, 1::2]
    mu = np.ascontiguousarray(mu)
    M = mu.shape[0]
    print(f"  shape={mu.shape}, dtype={mu.dtype}, "
          f"|mu| range=[{np.abs(mu).min():.2e}, {np.abs(mu).max():.2e}], "
          f"memory={mu.nbytes/1e6:.1f}MB, elapsed={time.time()-t0:.1f}s")
    return mu


def jackson_kernel(M: int) -> np.ndarray:
    """Jackson kernel g_n (n=0..M-1), 含 Kronecker delta 修正 g_0 *= 0.5."""
    n = np.arange(M, dtype=np.float64)
    alpha = np.pi / (M + 1)
    g = ((M - n + 1) * np.cos(alpha * n) + np.sin(alpha * n) / np.tan(alpha)) / (M + 1)
    g[0] *= 0.5
    return g


def apply_kernel(mu_raw: np.ndarray, g_row: np.ndarray, g_col: np.ndarray = None) -> np.ndarray:
    """mu_kern[m,n] = g_row[m] * g_col[n] * mu_raw[m,n]."""
    if g_col is None:
        g_col = g_row
    return mu_raw * g_row[:, None] * g_col[None, :]


def compute_sum_gamma_mu_fast(mu_kern: np.ndarray, num_theta: int = NUM_THETA) -> tuple:
    """
    优化版 sum_gamma_mu 计算.

    利用 gamma_{ij} = cos(iθ)*fn_j + cos(jθ)*fm_i 的秩-2 结构:
      sum_gm = Re(Sigma_{i,j} gamma_{ij} * mu_{ij})
             = cos_nt . Re(mu @ fn + mu^T @ fm)
    每 theta 点仅需 2 次 BLAS gemv (O(M^2)) 而非构建 MxM gamma 矩阵.

    Returns:
      theta_array: shape (num_theta,)
      sum_gamma_mu: shape (num_theta,)
    """
    M = mu_kern.shape[0]
    theta_array = (np.arange(num_theta) + 0.5) * np.pi / num_theta
    sum_gm = np.zeros(num_theta, dtype=np.float64)
    i_idx = np.arange(M, dtype=np.float64)

    print(f"  Computing sum_gamma_mu (BLAS gemv) for M={M}, {num_theta} theta...")
    t0 = time.time()

    for k in range(num_theta):
        th = theta_array[k]
        sin_t = np.sin(th)
        cos_t = np.cos(th)

        nt = i_idx * th
        fn = (cos_t - 1j * i_idx * sin_t) * (np.cos(nt) + 1j * np.sin(nt))
        fm = np.conj(fn)
        cos_nt = np.cos(nt)

        A = np.real(mu_kern @ fn)       # shape (M,), BLAS ZGEMV
        B = np.real(mu_kern.T @ fm)     # shape (M,), BLAS ZGEMV

        sum_gm[k] = np.dot(cos_nt, A + B)

        if (k + 1) % 512 == 0:
            elapsed = time.time() - t0
            eta = elapsed / (k + 1) * (num_theta - k - 1)
            print(f"    theta[{k+1}/{num_theta}] elapsed={elapsed:.1f}s eta={eta:.1f}s")

    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.1f}s ({elapsed/num_theta*1000:.1f}ms/theta), "
          f"sum_gm range=[{sum_gm.min():.4f}, {sum_gm.max():.4f}]")
    return theta_array, sum_gm


def theta_integral(theta_array: np.ndarray, sum_gm: np.ndarray,
                   energies: list, rescale: float, beta: float) -> np.ndarray:
    """
    theta 积分: sigma(E) = Sigma_k sum_gm[k] * f(E, cos(theta_k)) * Delta_theta / sin^3(theta_k)
    不含外部 prefactor.
    """
    num_theta = len(theta_array)
    dtheta = np.pi / num_theta
    sigma = np.zeros(len(energies))

    sin_theta = np.sin(theta_array)
    cos_theta = np.cos(theta_array)
    div = sin_theta ** 3

    for ie, E in enumerate(energies):
        efermi_re = (E - RESCALE_CENTER) / rescale
        fd = 1.0 / (1.0 + np.exp(beta * (cos_theta - efermi_re)))
        integrand = sum_gm * fd * dtheta / div
        sigma[ie] = np.sum(integrand)

    return sigma


# ─── 主分析 ───────────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("Phase J1 - Unified Jackson Kernel Truncation Verification")
    print("=" * 70)

    # 1. 加载 raw mu (M=4096)
    mu_full = load_mu_raw(H5_PATH)
    assert mu_full.shape == (M_FULL, M_FULL), \
        f"Expected ({M_FULL},{M_FULL}), got {mu_full.shape}"

    # 2. 预计算 g^(4096) (unified kernel)
    g4096 = jackson_kernel(M_FULL)
    print(f"\ng^(4096): g[0]={g4096[0]:.6f}, g[1]={g4096[1]:.6f}, "
          f"g[2047]={g4096[2047]:.6f}, g[4095]={g4096[4095]:.6f}")

    # 检查不同 M 核的差异
    print("\nJackson kernel g_n comparison at n=1000:")
    for M in [2048, 2560, 3072, 3584, 4096]:
        g = jackson_kernel(M)
        print(f"  g^({M})[1000] = {g[1000]:.8f}")
    ratio_n1000 = g4096[1000] / jackson_kernel(2048)[1000]
    print(f"  Ratio g^(4096)/g^(2048) at n=1000: {ratio_n1000:.6f}")

    # 3. 对每个 M_target 做 standard 和 unified 两种核处理
    results = {}
    theta_arr = None

    for M in M_TARGETS:
        print(f"\n{'─'*60}")
        print(f"M_target = {M}")
        print(f"{'─'*60}")

        mu_trunc = np.ascontiguousarray(mu_full[:M, :M])

        # --- Standard kernel ---
        print(f"  [Standard] g^({M})...")
        t0 = time.time()
        g_own = jackson_kernel(M)
        mu_kern_std = apply_kernel(mu_trunc, g_own)
        theta_arr, sum_gm_std = compute_sum_gamma_mu_fast(mu_kern_std)
        sig_std = theta_integral(theta_arr, sum_gm_std, ENERGIES, RESCALE, BETA)
        del mu_kern_std
        print(f"  [Standard] wall={time.time()-t0:.1f}s")

        # --- Unified kernel ---
        print(f"  [Unified] truncated g^(4096)...")
        t0 = time.time()
        g_unified = g4096[:M].copy()
        mu_kern_uni = apply_kernel(mu_trunc, g_unified)
        _, sum_gm_uni = compute_sum_gamma_mu_fast(mu_kern_uni)
        sig_uni = theta_integral(theta_arr, sum_gm_uni, ENERGIES, RESCALE, BETA)
        del mu_kern_uni
        print(f"  [Unified] wall={time.time()-t0:.1f}s")

        results[M] = {
            "sig_std": sig_std,
            "sig_uni": sig_uni,
            "sum_gm_std": sum_gm_std,
            "sum_gm_uni": sum_gm_uni,
        }

        print(f"  sigma_std(E_F=0) = {sig_std[1]:.6f}")
        print(f"  sigma_uni(E_F=0) = {sig_uni[1]:.6f}")
        print(f"  Delta = {sig_uni[1] - sig_std[1]:.6f}")

        del mu_trunc

    # 4. 绘图
    M_arr = np.array(M_TARGETS)
    S_std = np.array([results[M]["sig_std"][1] for M in M_TARGETS])
    S_uni = np.array([results[M]["sig_uni"][1] for M in M_TARGETS])

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Panel 1: S(M) comparison
    ax = axes[0]
    ax.plot(M_arr, S_std, "o-", color="#d73027", label="Standard (own g$^{(M)}$)",
            linewidth=2, markersize=8)
    ax.plot(M_arr, S_uni, "s--", color="#4575b4", label="Unified (g$^{(4096)}$ truncated)",
            linewidth=2, markersize=8)
    ax.axhline(y=0, color="gray", linestyle=":", linewidth=1)
    ax.set_xlabel("M (Chebyshev kernel size)")
    ax.set_ylabel(r"$\sigma_{xy}(E_F=0)$ [a.u., no prefactor]")
    ax.set_title("J1: S(M) - Standard vs Unified Jackson Kernel")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 2: sum(theta) curves for largest M
    ax = axes[1]
    M_last = M_TARGETS[-1]
    ax.plot(theta_arr, results[M_last]["sum_gm_std"], "-", color="#d73027",
            label=f"Standard g^({M_last})", linewidth=1.0, alpha=0.8)
    ax.plot(theta_arr, results[M_last]["sum_gm_uni"], "--", color="#4575b4",
            label=f"Unified g^(4096) truncated to {M_last}", linewidth=1.0, alpha=0.8)
    ax.set_xlabel(r"$\theta$")
    ax.set_ylabel(r"$\sum \Gamma \odot \mu$")
    ax.set_title(f"J1: sum(theta) comparison at M={M_last}")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    out_png = os.path.join(OUT_DIR, "J1_unified_kernel_S_vs_M.png")
    fig.savefig(out_png, dpi=150)
    plt.close(fig)
    print(f"\nFigure saved: {out_png}")

    # 5. 生成报告
    S_range_std = np.ptp(S_std)
    S_range_uni = np.ptp(S_uni)
    S_abs_uni = np.max(np.abs(S_uni))

    from numpy.polynomial.polynomial import polyfit
    coef_std = polyfit(M_arr, S_std, 1)
    coef_uni = polyfit(M_arr, S_uni, 1)
    slope_std = coef_std[1] * 4096
    slope_uni = coef_uni[1] * 4096

    report_lines = [
        "=" * 70,
        "Phase J1 - Unified Jackson Kernel Truncation Verification",
        f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 70,
        "",
        "Parameters:",
        f"  rescale = {RESCALE} eV (auto-detected)",
        f"  rescale_center = {RESCALE_CENTER} eV",
        f"  temperature = {TEMPERATURE} K (beta = {BETA:.2f} eV^-1)",
        f"  num_theta = {NUM_THETA}",
        f"  M_full = {M_FULL}",
        f"  M_targets = {M_TARGETS}",
        "",
        "Jackson kernel comparison at n=1000:",
    ]
    for M in [2048, 2560, 3072, 3584, 4096]:
        g = jackson_kernel(M)
        report_lines.append(f"  g^({M})[1000] = {g[1000]:.8f}")
    report_lines.append(f"  Ratio g^(4096)/g^(2048) at n=1000: {ratio_n1000:.6f}")

    report_lines += [
        "",
        "Results - sigma_xy(E_F=0) [a.u., no external prefactor]:",
        f"{'M':>6} | {'Standard':>14} {'Unified':>14} {'Delta(uni-std)':>15}",
        "-" * 55,
    ]
    for M in M_TARGETS:
        r = results[M]
        delta = r["sig_uni"][1] - r["sig_std"][1]
        report_lines.append(
            f"{M:>6} | {r['sig_std'][1]:>14.6f} {r['sig_uni'][1]:>14.6f} "
            f"{delta:>15.6f}"
        )

    report_lines += [
        "",
        "S(M) trend analysis:",
        f"  S_std range (max-min) = {S_range_std:.4f}",
        f"  S_uni range (max-min) = {S_range_uni:.4f}",
        f"  S_std linear slope (per 4096 M) = {slope_std:.4f}",
        f"  S_uni linear slope (per 4096 M) = {slope_uni:.4f}",
        f"  |S_uni| max = {S_abs_uni:.4f}",
        "",
        "S(M) individual values:",
    ]
    for i, M in enumerate(M_TARGETS):
        report_lines.append(f"  M={M:>4}: std={S_std[i]:>12.6f}  uni={S_uni[i]:>12.6f}")

    report_lines += [
        "",
        "-" * 70,
        "Judgment:",
    ]

    if S_range_uni < 0.2 * S_range_std and S_abs_uni < 100.0:
        report_lines.append(
            "  [OK] H_J CONFIRMED: Unified kernel makes S(M) essentially flat "
            f"(range={S_range_uni:.2f} << std range={S_range_std:.2f})."
        )
        report_lines.append(
            "     Jackson kernel M-dependence IS the root cause of baseline shift."
        )
        report_lines.append("     -> Proceed to J2 (Lorentz kernel C++ implementation).")
    elif S_range_uni < 0.5 * S_range_std:
        report_lines.append(
            f"  [WARN] H_J PARTIALLY SUPPORTED: Unified kernel reduces S(M) variation "
            f"(range={S_range_uni:.2f} vs std={S_range_std:.2f}) but not fully flat."
        )
        report_lines.append(
            "     Jackson kernel M-dependence is a significant factor, "
            "but there may be additional root causes."
        )
    else:
        report_lines.append(
            f"  [FAIL] H_J EXCLUDED: Unified kernel does NOT flatten S(M) "
            f"(range={S_range_uni:.2f} ~ std range={S_range_std:.2f})."
        )
        report_lines.append(
            "     Jackson kernel M-dependence is NOT the root cause of baseline shift."
        )

    report_lines += [
        "",
        "=" * 70,
    ]

    report_text = "\n".join(report_lines)
    print("\n" + report_text)

    out_txt = os.path.join(OUT_DIR, "J1_unified_kernel_report.txt")
    with open(out_txt, "w") as f:
        f.write(report_text + "\n")
    print(f"\nReport saved: {out_txt}")

    return results, S_std, S_uni


if __name__ == "__main__":
    main()
