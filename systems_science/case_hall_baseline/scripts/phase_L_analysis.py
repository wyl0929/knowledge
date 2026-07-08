#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-25 08:37:23
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-25 08:37:24
#FilePath     : /MG/test/phase_L_analysis.py
#Description  :

#!/usr/bin/env python3
"""
Phase L — 高阶项符号结构: 随机噪声 vs 系统性偏置

L1: μ 矩阵行/列符号一致性检验 (raw μ, 无核)
L2: 新区 Γ·μ 项的正负对消率 (含 Jackson 核)
L3: 单行贡献剖面: 哪一行打破了对消?

用法: python test/phase_L_analysis.py
输出: test/L1_mu_sign_structure.png, test/L1_mu_sign_structure.txt,
       test/L2_cancellation_rate.png, test/L2_cancellation_rate.txt,
       test/L3_row_profile.png
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
MU4096_PATH = "runs/0624/mu_raw_M4096_m64.h5"
OUT_DIR = "test"
NUM_THETA_SWEEP = 256   # L2 θ sweep resolution
M = 4096
SPLIT = 2048
os.makedirs(OUT_DIR, exist_ok=True)

plt.rcParams.update({"font.size": 11, "axes.titlesize": 13, "axes.labelsize": 12})


# ═══════════════════════════════════════════════════════════════════════════
# 工具函数
# ═══════════════════════════════════════════════════════════════════════════

def load_mu(h5_path: str) -> np.ndarray:
    """加载 raw μ 矩阵, 重组为 complex128, C-contiguous."""
    print(f"  Loading {h5_path}...")
    t0 = time.time()
    with h5py.File(h5_path, "r") as f:
        raw = f["mu_raw"][:]  # shape (M, 2*M) float64
    mu = raw[:, 0::2] + 1j * raw[:, 1::2]
    mu = np.ascontiguousarray(mu)
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


def apply_kernel(mu_raw: np.ndarray, g: np.ndarray) -> np.ndarray:
    """mu_kern[m,n] = g[m] * g[n] * mu_raw[m,n]."""
    return mu_raw * g[:, None] * g[None, :]


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
    # γ_{mn} = cos(mθ)·fn_n + cos(nθ)·fm_m
    Gamma = cos_nt[:, None] * fn[None, :] + cos_nt[None, :] * fm[:, None]
    return Gamma


def compute_terms_fast(mu_kern: np.ndarray, cos_nt: np.ndarray,
                       fn: np.ndarray, fm: np.ndarray) -> np.ndarray:
    """
    快速计算 terms[m,n] = Re(Γ_{mn} · μ_kern[m,n])  (M×M, float64).
    避免显式构造 Γ:
      terms = cos(mθ)·Re(fn_n·μ_kern[m,n]) + cos(nθ)·Re(fm_m·μ_kern[m,n])
    """
    # T1[m,n] = fn_n * mu_kern[m,n]  (broadcast fn along columns)
    # T2[m,n] = fm_m * mu_kern[m,n]  (broadcast fm along rows)
    T1 = mu_kern * fn[None, :]       # fn broadcast to each row
    T2 = mu_kern * fm[:, None]       # fm broadcast to each column
    terms = cos_nt[:, None] * T1.real + cos_nt[None, :] * T2.real
    return terms


def cancellation_rate(terms: np.ndarray, mask: np.ndarray) -> dict:
    """
    计算对消率 R = |net| / (|pos| + |neg|).
    返回 {pos, neg, net, R}.
    """
    t = terms[mask]
    pos = float(np.sum(t[t > 0]))
    neg = float(np.sum(t[t < 0]))
    net = pos + neg
    denom = pos + abs(neg)
    R = abs(net) / max(denom, 1e-30)
    return {"pos": pos, "neg": neg, "net": net, "R": R, "n_terms": len(t)}


# ═══════════════════════════════════════════════════════════════════════════
# L1 — μ 矩阵行/列符号一致性检验
# ═══════════════════════════════════════════════════════════════════════════

def run_l1(mu: np.ndarray):
    """
    对 raw μ (无核加权)，统计每行/每列的正负符号分布，
    检验是否有系统性符号偏置。
    """
    print("\n" + "=" * 70)
    print("L1 — μ 矩阵行/列符号一致性检验")
    print("=" * 70)

    mu_real = mu.real  # (4096, 4096)

    # 1. 行符号统计
    print("\n[L1.1] Row/column sign statistics...")
    pos_frac_row = np.sum(mu_real > 0, axis=1) / M  # (4096,)
    pos_frac_col = np.sum(mu_real > 0, axis=0) / M  # (4096,)

    print(f"  Row pos_frac: mean={pos_frac_row.mean():.4f}, std={pos_frac_row.std():.4f}, "
          f"min={pos_frac_row.min():.4f}, max={pos_frac_row.max():.4f}")
    print(f"  Col pos_frac: mean={pos_frac_col.mean():.4f}, std={pos_frac_col.std():.4f}, "
          f"min={pos_frac_col.min():.4f}, max={pos_frac_col.max():.4f}")

    # 2. 高 n 区段分析
    print("\n[L1.2] Block-wise pos_frac (512-row blocks):")
    block_size = 512
    n_blocks = M // block_size
    block_fracs = []
    for b in range(n_blocks):
        r0, r1 = b * block_size, (b + 1) * block_size
        frac = np.sum(mu_real[r0:r1, :] > 0) / (block_size * M)
        block_fracs.append(frac)
        flag = " ⚠️" if abs(frac - 0.5) > 0.02 else ""
        print(f"  block [{r0:4d},{r1:4d}): pos_frac={frac:.4f}{flag}")

    # 3. 全矩阵直方图
    print("\n[L1.3] Full matrix histogram...")
    # 采样以避免内存问题（直方图用 1M 随机采样足够）
    n_sample = min(10_000_000, M * M)
    idx_flat = np.random.default_rng(42).choice(M * M, size=n_sample, replace=False)
    sample_vals = mu_real.ravel()[idx_flat]

    # 4. 绘图
    fig = plt.figure(figsize=(18, 12))
    gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.3)

    # Panel A: 行 pos_frac vs m
    ax = fig.add_subplot(gs[0, :2])
    ax.plot(pos_frac_row, ".", markersize=0.8, color="#4575b4", alpha=0.7)
    ax.axhline(y=0.5, color="gray", linestyle="--", linewidth=0.8, label="0.5 (zero-mean)")
    ax.axhline(y=0.48, color="silver", linestyle=":", linewidth=0.5)
    ax.axhline(y=0.52, color="silver", linestyle=":", linewidth=0.5)
    ax.set_xlabel("Row index m")
    ax.set_ylabel("Positive fraction in row")
    ax.set_title(f"L1: Row pos_frac vs m  (mean={pos_frac_row.mean():.4f}, std={pos_frac_row.std():.4f})")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel B: 列 pos_frac vs n
    ax = fig.add_subplot(gs[0, 2])
    ax.plot(pos_frac_col, ".", markersize=0.8, color="#d73027", alpha=0.7)
    ax.axhline(y=0.5, color="gray", linestyle="--", linewidth=0.8)
    ax.axhline(y=0.48, color="silver", linestyle=":", linewidth=0.5)
    ax.axhline(y=0.52, color="silver", linestyle=":", linewidth=0.5)
    ax.set_xlabel("Column index n")
    ax.set_ylabel("Positive fraction in col")
    ax.set_title(f"L1: Col pos_frac vs n  (mean={pos_frac_col.mean():.4f})")
    ax.grid(True, alpha=0.3)

    # Panel C: 分块柱状图
    ax = fig.add_subplot(gs[1, :2])
    x = np.arange(n_blocks)
    colors = ["#fc8d59" if abs(f - 0.5) > 0.02 else "#91bfdb" for f in block_fracs]
    ax.bar(x, block_fracs, color=colors, edgecolor="white", linewidth=0.5)
    ax.axhline(y=0.5, color="gray", linestyle="--", linewidth=0.8)
    ax.axhline(y=0.48, color="silver", linestyle=":", linewidth=0.5)
    ax.axhline(y=0.52, color="silver", linestyle=":", linewidth=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels([f"[{b*512},{min((b+1)*512,4096)})" for b in range(n_blocks)],
                       rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("Positive fraction")
    ax.set_title(f"L1: Block-wise pos_frac  (n_blocks={n_blocks}, block_size={block_size})")
    ax.grid(True, alpha=0.3, axis="y")

    # Panel D: 全矩阵直方图
    ax = fig.add_subplot(gs[1, 2])
    p1, p99 = np.percentile(sample_vals, [1, 99])
    clip_range = max(abs(p1), abs(p99)) * 1.2
    ax.hist(np.clip(sample_vals, -clip_range, clip_range), bins=200,
            color="#5e4fa2", alpha=0.7, edgecolor="none", density=True)
    ax.axvline(x=0, color="gray", linestyle="--", linewidth=0.8)
    ax.set_xlabel("Re(μ_mn)")
    ax.set_ylabel("Density")
    ax.set_title(f"L1: Re(μ) histogram\n(sample={n_sample}, clip=±{clip_range:.2e})")

    # Panel E: 高 m 区 pos_frac 放大 (m > 3072)
    ax = fig.add_subplot(gs[2, :2])
    m_start = 3072
    ax.plot(range(m_start, M), pos_frac_row[m_start:], ".", markersize=1.5,
            color="#d73027", alpha=0.8)
    ax.axhline(y=0.5, color="gray", linestyle="--", linewidth=0.8)
    ax.axhline(y=0.48, color="silver", linestyle=":", linewidth=0.5)
    ax.axhline(y=0.52, color="silver", linestyle=":", linewidth=0.5)
    ax.set_xlabel("Row index m")
    ax.set_ylabel("Positive fraction")
    ax.set_title(f"L1: Row pos_frac zoom (m ∈ [{m_start},{M}))  "
                 f"mean={pos_frac_row[m_start:].mean():.4f}")
    ax.grid(True, alpha=0.3)

    # Panel F: pos_frac 的分布直方图
    ax = fig.add_subplot(gs[2, 2])
    ax.hist(pos_frac_row, bins=100, color="#4575b4", alpha=0.7, edgecolor="none",
            label=f"row (std={pos_frac_row.std():.4f})")
    ax.hist(pos_frac_col, bins=100, color="#d73027", alpha=0.5, edgecolor="none",
            label=f"col (std={pos_frac_col.std():.4f})")
    ax.axvline(x=0.5, color="gray", linestyle="--", linewidth=0.8)
    ax.set_xlabel("Positive fraction")
    ax.set_ylabel("Count")
    ax.set_title("L1: Distribution of pos_frac")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3, axis="y")

    out_png = os.path.join(OUT_DIR, "L1_mu_sign_structure.png")
    fig.savefig(out_png, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {out_png}")

    # 5. 写入文本报告
    out_txt = os.path.join(OUT_DIR, "L1_mu_sign_structure.txt")
    with open(out_txt, "w") as f:
        f.write(f"Phase L1 — μ Matrix Sign Structure Analysis\n")
        f.write(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"{'='*70}\n\n")
        f.write(f"Matrix: M=4096, shape={mu.shape}, dtype={mu.dtype}\n")
        f.write(f"Source: {MU4096_PATH}\n\n")
        f.write(f"Row pos_frac:  mean={pos_frac_row.mean():.6f}, std={pos_frac_row.std():.6f}, "
                f"min={pos_frac_row.min():.6f}, max={pos_frac_row.max():.6f}\n")
        f.write(f"Col pos_frac:  mean={pos_frac_col.mean():.6f}, std={pos_frac_col.std():.6f}, "
                f"min={pos_frac_col.min():.6f}, max={pos_frac_col.max():.6f}\n\n")
        f.write(f"Block-wise (block_size={block_size}):\n")
        for b, frac in enumerate(block_fracs):
            flag = " ⚠️ DEVIATION > 0.02" if abs(frac - 0.5) > 0.02 else ""
            f.write(f"  [{b*block_size:4d},{(b+1)*block_size:4d}): {frac:.6f}{flag}\n")
        f.write(f"\nHigh-m region (m >= 3072): mean={pos_frac_row[3072:].mean():.6f}, "
                f"std={pos_frac_row[3072:].std():.6f}\n")

        # Verdict
        global_dev = abs(pos_frac_row.mean() - 0.5)
        high_dev = abs(pos_frac_row[3072:].mean() - 0.5)
        max_block_dev = max(abs(f - 0.5) for f in block_fracs)
        f.write(f"\n--- Verdict ---\n")
        if global_dev < 0.02 and high_dev < 0.02 and max_block_dev < 0.02:
            f.write("✅ PASS: No systematic sign bias detected.\n")
            f.write("   μ matrix signs are consistent with zero-mean random distribution.\n")
            f.write("   Krylov direction drift hypothesis is NOT supported.\n")
        else:
            f.write("⚠️  WARNING: Systematic sign bias detected.\n")
            if global_dev >= 0.02:
                f.write(f"   Global pos_frac deviates from 0.5 by {global_dev:.4f}\n")
            if high_dev >= 0.02:
                f.write(f"   High-m pos_frac deviates from 0.5 by {high_dev:.4f}\n")
            if max_block_dev >= 0.02:
                f.write(f"   Max block deviation: {max_block_dev:.4f}\n")

    print(f"  Saved: {out_txt}")

    return {
        "pos_frac_row": pos_frac_row,
        "pos_frac_col": pos_frac_col,
        "block_fracs": block_fracs,
        "global_dev": abs(pos_frac_row.mean() - 0.5),
        "high_m_dev": abs(pos_frac_row[3072:].mean() - 0.5),
    }


# ═══════════════════════════════════════════════════════════════════════════
# L2 — 新区 Γ·μ 项的正负对消率
# ═══════════════════════════════════════════════════════════════════════════

def run_l2(mu: np.ndarray):
    """
    对新区 (max(m,n)>=SPLIT)，分别累加正项和负项，
    计算对消率 R = |net| / (|pos| + |neg|).
    """
    print("\n" + "=" * 70)
    print("L2 — 新区 Γ·μ 项的正负对消率")
    print("=" * 70)

    # 1. 应用 Jackson 核
    print("\n[L2.1] Applying Jackson kernel...")
    g4096 = jackson_kernel(M)
    mu_kern = apply_kernel(mu, g4096)
    print(f"  mu_kern: |mu_kern| range=[{np.abs(mu_kern).min():.2e}, {np.abs(mu_kern).max():.2e}]")

    # 2. 构造区域 mask
    # Old region: m < SPLIT and n < SPLIT
    # New region: max(m,n) >= SPLIT
    mask_old = np.zeros((M, M), dtype=bool)
    mask_old[:SPLIT, :SPLIT] = True
    mask_new = ~mask_old

    n_old = np.sum(mask_old)
    n_new = np.sum(mask_new)
    print(f"  Old region (m,n<{SPLIT}): {n_old} elements ({n_old/(M*M)*100:.1f}%)")
    print(f"  New region (max≥{SPLIT}): {n_new} elements ({n_new/(M*M)*100:.1f}%)")

    # 3. 对 3 个选定 θ 做逐点对比
    test_thetas = [1.0, np.pi / 2, 2.0]
    print(f"\n[L2.2] Point analysis at θ = {[f'{t:.3f}' for t in test_thetas]}:")
    print(f"{'θ':>8} | {'Region':>6} | {'Σ+':>14} | {'Σ−':>14} | {'net':>14} | {'R':>8} | {'n_terms':>10}")
    print("-" * 85)

    point_results = []
    for theta in test_thetas:
        t0 = time.time()
        # Compute terms efficiently
        idx = np.arange(M, dtype=np.float64)
        cos_nt = np.cos(idx * theta)
        sin_t = np.sin(theta)
        cos_t = np.cos(theta)
        n_theta = idx * theta
        fn = (cos_t - 1j * idx * sin_t) * (np.cos(n_theta) + 1j * np.sin(n_theta))
        fm = np.conj(fn)

        terms = compute_terms_fast(mu_kern, cos_nt, fn, fm)

        for label, mask in [("old", mask_old), ("new", mask_new)]:
            r = cancellation_rate(terms, mask)
            point_results.append((theta, label, r))
            print(f"  {theta:6.3f} | {label:>6} | {r['pos']:14.2f} | {r['neg']:14.2f} | "
                  f"{r['net']:14.2f} | {r['R']:.4f} | {r['n_terms']:>10}")
        print(f"    (elapsed {time.time()-t0:.1f}s)")

    # 4. 扫 θ ∈ [0,π], 绘制 R(θ) 曲线
    print(f"\n[L2.3] Sweeping θ ∈ [0,π] ({NUM_THETA_SWEEP} points)...")
    theta_arr = (np.arange(NUM_THETA_SWEEP) + 0.5) * np.pi / NUM_THETA_SWEEP
    R_old_arr = np.zeros(NUM_THETA_SWEEP)
    R_new_arr = np.zeros(NUM_THETA_SWEEP)
    net_old_arr = np.zeros(NUM_THETA_SWEEP)
    net_new_arr = np.zeros(NUM_THETA_SWEEP)

    t0 = time.time()
    for k in range(NUM_THETA_SWEEP):
        theta = theta_arr[k]
        idx_arr = np.arange(M, dtype=np.float64)
        cos_nt = np.cos(idx_arr * theta)
        sin_t = np.sin(theta)
        cos_t = np.cos(theta)
        n_theta = idx_arr * theta
        fn = (cos_t - 1j * idx_arr * sin_t) * (np.cos(n_theta) + 1j * np.sin(n_theta))
        fm = np.conj(fn)

        terms = compute_terms_fast(mu_kern, cos_nt, fn, fm)

        r_old = cancellation_rate(terms, mask_old)
        r_new = cancellation_rate(terms, mask_new)
        R_old_arr[k] = r_old["R"]
        R_new_arr[k] = r_new["R"]
        net_old_arr[k] = r_old["net"]
        net_new_arr[k] = r_new["net"]

        if (k + 1) % 64 == 0:
            elapsed = time.time() - t0
            eta = elapsed / (k + 1) * (NUM_THETA_SWEEP - k - 1)
            print(f"    θ[{k+1}/{NUM_THETA_SWEEP}] elapsed={elapsed:.1f}s eta={eta:.1f}s "
                  f"R_old={R_old_arr[k]:.4f} R_new={R_new_arr[k]:.4f}")

    print(f"  Sweep done in {time.time()-t0:.1f}s")

    # 5. 绘图
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # Panel A: R_old(θ) vs R_new(θ)
    ax = axes[0, 0]
    ax.plot(theta_arr, R_old_arr, "-", color="#4575b4", linewidth=1.2,
            label=f"Old (m,n<{SPLIT})")
    ax.plot(theta_arr, R_new_arr, "-", color="#d73027", linewidth=1.2,
            label=f"New (max≥{SPLIT})")
    ax.axhline(y=0.01, color="gray", linestyle=":", linewidth=0.5, label="R=0.01")
    ax.set_xlabel(r"$\theta$")
    ax.set_ylabel("Cancellation rate R")
    ax.set_title(f"L2: Cancellation Rate R(θ)  "
                 f"(old: mean R={R_old_arr.mean():.4f}, new: mean R={R_new_arr.mean():.4f})")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-0.05, 1.05)

    # Panel B: net contribution vs θ
    ax = axes[0, 1]
    ax.plot(theta_arr, net_old_arr, "-", color="#4575b4", linewidth=1.0,
            label=f"Old net")
    ax.plot(theta_arr, net_new_arr, "-", color="#d73027", linewidth=1.0,
            label=f"New net")
    ax.axhline(y=0, color="gray", linestyle=":", linewidth=0.5)
    ax.set_xlabel(r"$\theta$")
    ax.set_ylabel("Net contribution")
    ax.set_title("L2: Net contribution vs θ")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel C: R_old vs R_new scatter
    ax = axes[1, 0]
    ax.scatter(R_old_arr, R_new_arr, c=theta_arr, cmap="viridis", s=5, alpha=0.6)
    ax.plot([0, 1], [0, 1], "k--", linewidth=0.5, alpha=0.3)
    ax.set_xlabel("R_old")
    ax.set_ylabel("R_new")
    ax.set_title("L2: R_old vs R_new (colored by θ)")
    cbar = plt.colorbar(ax.collections[0], ax=ax, label=r"$\theta$")
    ax.grid(True, alpha=0.3)

    # Panel D: R_new / R_old ratio vs θ
    ax = axes[1, 1]
    ratio = np.where(R_old_arr > 1e-6, R_new_arr / R_old_arr, np.nan)
    ax.plot(theta_arr, ratio, "-", color="#fc8d59", linewidth=1.0)
    ax.axhline(y=1.0, color="gray", linestyle="--", linewidth=0.8)
    ax.set_xlabel(r"$\theta$")
    ax.set_ylabel("R_new / R_old")
    ax.set_title(f"L2: Cancellation rate ratio  "
                 f"(mean={np.nanmean(ratio):.3f})")
    ax.grid(True, alpha=0.3)

    out_png = os.path.join(OUT_DIR, "L2_cancellation_rate.png")
    fig.savefig(out_png, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {out_png}")

    # 6. 文本报告
    out_txt = os.path.join(OUT_DIR, "L2_cancellation_rate.txt")
    with open(out_txt, "w") as f:
        f.write(f"Phase L2 — Γ·μ Cancellation Rate Analysis\n")
        f.write(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"{'='*70}\n\n")
        f.write(f"Matrix: M={M}, split={SPLIT}\n")
        f.write(f"Jackson kernel: M={M}\n")
        f.write(f"Old region: m,n < {SPLIT}  ({n_old} elements)\n")
        f.write(f"New region: max(m,n) >= {SPLIT}  ({n_new} elements)\n\n")

        f.write(f"Point comparisons:\n")
        f.write(f"{'θ':>8} | {'Region':>6} | {'Σ+':>14} | {'Σ−':>14} | "
                f"{'net':>14} | {'R':>8}\n")
        f.write("-" * 72 + "\n")
        for theta, label, r in point_results:
            f.write(f"  {theta:6.3f} | {label:>6} | {r['pos']:14.2f} | {r['neg']:14.2f} | "
                    f"{r['net']:14.2f} | {r['R']:.4f}\n")

        f.write(f"\nSweep summary ({NUM_THETA_SWEEP} θ points):\n")
        f.write(f"  R_old: mean={R_old_arr.mean():.6f}, std={R_old_arr.std():.6f}, "
                f"min={R_old_arr.min():.6f}, max={R_old_arr.max():.6f}\n")
        f.write(f"  R_new: mean={R_new_arr.mean():.6f}, std={R_new_arr.std():.6f}, "
                f"min={R_new_arr.min():.6f}, max={R_new_arr.max():.6f}\n")
        f.write(f"  R_new/R_old: mean={np.nanmean(ratio):.6f}, median={np.nanmedian(ratio):.6f}\n")

        # Verdict
        mean_R_new = R_new_arr.mean()
        f.write(f"\n--- Verdict ---\n")
        if mean_R_new < 0.01:
            f.write("✅ PASS: New-region cancellation rate R ≈ 0.\n")
            f.write("   Oscillation cancellation is effective. Baseline shift from other sources.\n")
        elif mean_R_new < 0.1:
            f.write("⚠️  MODERATE: R_new = {mean_R_new:.4f} is small but non-zero.\n")
            f.write("   Partial cancellation — some net bias exists.\n")
        else:
            f.write("❌ FAIL: R_new = {mean_R_new:.4f} >> 0.\n")
            f.write("   Oscillation cancellation is NOT effective in new region.\n")
            f.write("   Systematic bias confirmed → direction drift hypothesis supported.\n")

    print(f"  Saved: {out_txt}")

    return {
        "R_old": R_old_arr,
        "R_new": R_new_arr,
        "theta_arr": theta_arr,
        "point_results": point_results,
    }


# ═══════════════════════════════════════════════════════════════════════════
# L3 — 单行贡献剖面: 哪一行打破了对消？
# ═══════════════════════════════════════════════════════════════════════════

def run_l3(mu: np.ndarray):
    """
    对固定 θ，绘制 Σ_n Γ_{mn} μ_{mn} 随 m 的累积和曲线，
    定位净贡献来自哪些 m 行。
    """
    print("\n" + "=" * 70)
    print("L3 — 单行贡献剖面: 哪一行打破了对消?")
    print("=" * 70)

    # 1. 应用 Jackson 核
    print("\n[L3.1] Applying Jackson kernel...")
    g4096 = jackson_kernel(M)
    mu_kern = apply_kernel(mu, g4096)

    # 2. 对 3 个 θ 分别分析
    test_thetas = [1.0, np.pi / 2, 2.0]
    fig, axes = plt.subplots(3, 3, figsize=(20, 16))

    all_top_rows = {}  # theta -> list of (row_idx, row_sum)
    row_sums_all = {}  # theta -> row_sums array

    for ti, theta in enumerate(test_thetas):
        print(f"\n[L3.2] θ = {theta:.3f} ({theta*180/np.pi:.1f}°)")
        t0 = time.time()

        # Build Gamma matrix and compute row sums
        idx = np.arange(M, dtype=np.float64)
        cos_nt = np.cos(idx * theta)
        sin_t = np.sin(theta)
        cos_t = np.cos(theta)
        n_theta = idx * theta
        fn = (cos_t - 1j * idx * sin_t) * (np.cos(n_theta) + 1j * np.sin(n_theta))
        fm = np.conj(fn)

        terms = compute_terms_fast(mu_kern, cos_nt, fn, fm)  # (M, M) float64

        # Row sums: Σ_n terms[m,n]
        row_sums = np.sum(terms, axis=1)  # (M,)
        cumsum = np.cumsum(row_sums)       # (M,)

        row_sums_all[theta] = row_sums

        # 总 sum
        total = float(np.sum(terms))
        print(f"  Total sum = {total:.4f}")

        # Old vs new region contributions
        mask_old = np.zeros((M, M), dtype=bool)
        mask_old[:SPLIT, :SPLIT] = True
        mask_new = ~mask_old
        old_contrib = float(np.sum(terms[mask_old]))
        new_contrib = float(np.sum(terms[mask_new]))
        print(f"  Old region sum = {old_contrib:.4f} ({old_contrib/max(abs(total),1e-30)*100:.1f}%)")
        print(f"  New region sum = {new_contrib:.4f} ({new_contrib/max(abs(total),1e-30)*100:.1f}%)")

        # Top 10 rows by |row_sum|
        top_idx = np.argsort(np.abs(row_sums))[::-1][:10]
        print(f"  Top 10 rows by |row_sum|:")
        print(f"  {'m':>6} | {'row_sum':>14} | {'sign':>6} | {'cumsum_before':>14}")
        top_rows = []
        for rank, mi in enumerate(top_idx):
            sign = "+" if row_sums[mi] > 0 else "-"
            cumsum_before = cumsum[mi - 1] if mi > 0 else 0.0
            print(f"  {mi:>6} | {row_sums[mi]:14.4f} | {sign:>6} | {cumsum_before:14.4f}")
            top_rows.append((mi, row_sums[mi], sign))
        all_top_rows[theta] = top_rows

        # Panel A: row_sums vs m
        ax = axes[ti, 0]
        ax.plot(row_sums, ".", markersize=0.8, color="#4575b4", alpha=0.7)
        ax.axhline(y=0, color="gray", linestyle=":", linewidth=0.5)
        # Mark top 5 rows
        for mi, val, _ in top_rows[:5]:
            ax.plot(mi, val, "o", markersize=6, markerfacecolor="none",
                    markeredgecolor="#d73027", markeredgewidth=1.5)
        ax.axvline(x=SPLIT, color="orange", linestyle="--", linewidth=0.8,
                   label=f"split={SPLIT}")
        ax.set_xlabel("Row index m")
        ax.set_ylabel("Row sum")
        ax.set_title(f"θ={theta:.3f}: Row sums Σ_n Γ·μ")
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

        # Panel B: cumsum vs m
        ax = axes[ti, 1]
        ax.plot(cumsum, "-", color="#fc8d59", linewidth=1.2)
        ax.axhline(y=0, color="gray", linestyle=":", linewidth=0.5)
        ax.axvline(x=SPLIT, color="orange", linestyle="--", linewidth=0.8,
                   label=f"split={SPLIT}")
        ax.set_xlabel("Row index m")
        ax.set_ylabel("Cumulative sum")
        ax.set_title(f"θ={theta:.3f}: Cumulative row sum")
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

        # Panel C: high-m zoom (m > 3072)
        ax = axes[ti, 2]
        m_start = 3072
        ax.plot(range(m_start, M), row_sums[m_start:], ".", markersize=1.5,
                color="#d73027", alpha=0.8)
        ax.axhline(y=0, color="gray", linestyle=":", linewidth=0.5)
        # Mark sign of each point
        pos_mask = row_sums[m_start:] > 0
        neg_mask = row_sums[m_start:] < 0
        n_pos = np.sum(pos_mask)
        n_neg = np.sum(neg_mask)
        ax.set_xlabel("Row index m")
        ax.set_ylabel("Row sum")
        ax.set_title(f"θ={theta:.3f}: High-m zoom (n_pos={n_pos}, n_neg={n_neg})")
        ax.grid(True, alpha=0.3)

        print(f"  elapsed={time.time()-t0:.1f}s")

    # 跨 θ 一致性分析: top rows
    print(f"\n[L3.3] Cross-θ consistency of top rows:")
    all_top_m = set()
    for theta in test_thetas:
        all_top_m.update(mi for mi, _, _ in all_top_rows[theta])
    print(f"  Unique m in any top-10: {sorted(all_top_m)}")
    # Check if any row appears in top-10 for all 3 thetas
    common = set(mi for mi, _, _ in all_top_rows[test_thetas[0]])
    for theta in test_thetas[1:]:
        common &= set(mi for mi, _, _ in all_top_rows[theta])
    if common:
        print(f"  ⚠️  Rows in TOP-10 for ALL θ: {sorted(common)} — systematic bias!")
    else:
        print(f"  No row appears in top-10 for all θ — isolated spikes.")

    # Check sign consistency for rows that appear in multiple thetas
    print(f"\n  Sign consistency check:")
    for m_val in sorted(all_top_m):
        signs = []
        for theta in test_thetas:
            rs = row_sums_all[theta]
            signs.append("+" if rs[m_val] > 0 else "-")
        if len(set(signs)) == 1:
            print(f"    m={m_val:>4}: {', '.join(signs)} — CONSISTENT sign ⚠️")
        else:
            print(f"    m={m_val:>4}: {', '.join(signs)} — oscillating")

    # Add text summary to figure
    fig.text(0.02, 0.01,
             f"Cross-θ common top rows: {sorted(common) if common else 'none'} | "
             f"Old region contribution: see above",
             fontsize=9, color="gray", fontfamily="monospace")

    out_png = os.path.join(OUT_DIR, "L3_row_profile.png")
    fig.savefig(out_png, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"\n  Saved: {out_png}")

    return {
        "all_top_rows": all_top_rows,
        "row_sums_all": row_sums_all,
        "common_rows": common,
    }


# ═══════════════════════════════════════════════════════════════════════════
# 主入口
# ═══════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("Phase L — 高阶项符号结构: 随机噪声 vs 系统性偏置")
    print(f"Start: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    # 加载数据 (一次性)
    print("\n>>> Loading data...")
    mu = load_mu(MU4096_PATH)
    assert mu.shape == (M, M), f"Expected ({M},{M}), got {mu.shape}"

    # L1: 符号一致性 (无核)
    l1_results = run_l1(mu)

    # L2: 对消率 (含核)
    l2_results = run_l2(mu)

    # L3: 行贡献剖面 (含核)
    l3_results = run_l3(mu)

    # ─── 综合判别 ───
    print("\n" + "=" * 70)
    print("Phase L — 综合判别")
    print("=" * 70)
    print(f"""
    L1: μ 符号偏置?
      global_dev = {l1_results['global_dev']:.4f}
      high_m_dev = {l1_results['high_m_dev']:.4f}
      → {'⚠️ BIAS' if l1_results['global_dev'] > 0.02 or l1_results['high_m_dev'] > 0.02 else '✅ NO BIAS'}

    L2: 新区对消率?
      mean R_new = {l2_results['R_new'].mean():.4f}
      mean R_old = {l2_results['R_old'].mean():.4f}
      → {'⚠️ NET BIAS' if l2_results['R_new'].mean() > 0.1 else '⚠️ MODERATE' if l2_results['R_new'].mean() > 0.01 else '✅ EFFECTIVE CANCELLATION'}

    L3: 跨θ一致异常行?
      common_rows = {sorted(l3_results['common_rows']) if l3_results['common_rows'] else 'none'}
      → {'⚠️ SYSTEMATIC ROWS' if l3_results['common_rows'] else '✅ NO SYSTEMATIC ROWS'}
    """)

    print("Phase L complete. All outputs in test/")
    print(f"End: {time.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
