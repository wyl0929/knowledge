#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-25 05:31:30
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-25 05:31:33
#FilePath     : /MG/test/plot_phase_D_blocks.py
#Description  :

#!/usr/bin/env python3
"""
plot_phase_D_blocks.py — Phase D 分块贡献热图重绘

从 vbl_block_M4096.log (C++ VBL_BLOCK 诊断输出) 读取 Re(gamma·mu) 块贡献,
使用线性着色 (非对数), 含多 M 截断视图。

用法: python test/plot_phase_D_blocks.py
输出: data/sigma/phase_D_block_decomp/block_contrib_*.png
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os, re, sys

# ─── 配置 ─────────────────────────────────────────────────────────────────
VBL_LOG = "runs/0624/vbl_block_M4096.log"
OUT_DIR = "data/sigma/phase_D_block_decomp"
BLOCK_SIZE = 256
M_FULL = 4096
M_TRUNC = [2048, 2560, 3072, 3584, 4096]  # 多 M 截断视图

os.makedirs(OUT_DIR, exist_ok=True)
plt.rcParams.update({"font.size": 11, "axes.titlesize": 13, "axes.labelsize": 12})


# ─── 解析 vbl_block 日志 ──────────────────────────────────────────────────

def parse_vbl_block(log_path: str) -> np.ndarray:
    """解析 VBL_BLOCK 日志, 返回 (nb, nb) 块矩阵, 元素为 Re(gamma*mu) 块和."""
    nb = M_FULL // BLOCK_SIZE  # 16
    block_mat = np.zeros((nb, nb))
    seen = set()

    with open(log_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # 格式: ib=0 jb=0 sum=-0.00219075
            parts = line.split()
            if len(parts) != 3:
                continue
            try:
                ib = int(parts[0].split("=")[1])
                jb = int(parts[1].split("=")[1])
                s = float(parts[2].split("=")[1])
            except (IndexError, ValueError):
                continue

            key = (ib // BLOCK_SIZE, jb // BLOCK_SIZE)
            if key not in seen:
                seen.add(key)
                block_mat[key] = s
            # 重复条目 (多 MPI rank) 值相同, 跳过

    print(f"  Parsed {len(seen)} unique blocks (expected {nb*nb})")
    return block_mat


def truncate_block_mat(full_mat: np.ndarray, M_target: int) -> np.ndarray:
    """从 M_FULL 块矩阵截断到 M_target."""
    nb_target = M_target // BLOCK_SIZE
    return full_mat[:nb_target, :nb_target].copy()


# ─── 绘图函数 ─────────────────────────────────────────────────────────────

def plot_single_M(block_mat: np.ndarray, M: int, outpath: str):
    """单 M 分块贡献热图 — 三面板: signed / abs / diagonal profile."""
    nb = block_mat.shape[0]
    fig, axes = plt.subplots(1, 3, figsize=(22, 6))

    # ── Panel 1: Signed Re(Γ·μ) ──
    vmax = max(abs(block_mat.min()), abs(block_mat.max()))
    im1 = axes[0].imshow(block_mat, cmap="RdBu_r", aspect="auto",
                         origin="upper", vmin=-vmax, vmax=vmax)
    axes[0].set_title(f"M={M} — Re(Γ·μ) signed")
    axes[0].set_xlabel("jb block index"); axes[0].set_ylabel("ib block index")
    cbar1 = plt.colorbar(im1, ax=axes[0], shrink=0.82)
    cbar1.set_label("Re(Γ·μ) block sum")

    # 标注零线参考
    for i in range(nb):
        axes[0].axhline(y=i + 0.5, color="gray", lw=0.3, alpha=0.4)
        axes[0].axvline(x=i + 0.5, color="gray", lw=0.3, alpha=0.4)

    # ── Panel 2: |Re(Γ·μ)| magnitude ──
    abs_mat = np.abs(block_mat)
    im2 = axes[1].imshow(abs_mat, cmap="inferno", aspect="auto", origin="upper")
    axes[1].set_title(f"M={M} — |Re(Γ·μ)| magnitude")
    axes[1].set_xlabel("jb block index"); axes[1].set_ylabel("ib block index")
    cbar2 = plt.colorbar(im2, ax=axes[1], shrink=0.82)
    cbar2.set_label("|Re(Γ·μ)| block sum")

    for i in range(nb):
        axes[1].axhline(y=i + 0.5, color="gray", lw=0.3, alpha=0.4)
        axes[1].axvline(x=i + 0.5, color="gray", lw=0.3, alpha=0.4)

    # ── Panel 3: Diagonal profile ──
    diag = np.array([block_mat[i, i] for i in range(nb)])
    abs_diag = np.abs(diag)
    m_indices = np.arange(nb) * BLOCK_SIZE

    axes[2].bar(m_indices, diag, width=BLOCK_SIZE * 0.8,
                color=["#d73027" if v < 0 else "#4575b4" for v in diag],
                edgecolor="black", linewidth=0.3, alpha=0.85)
    axes[2].axhline(y=0, color="black", lw=0.8)
    axes[2].set_xlabel("m (= n) Chebyshev index"); axes[2].set_ylabel("Re(Γ·μ) diagonal block sum")
    axes[2].set_title(f"M={M} — Diagonal block contributions")
    axes[2].grid(axis="y", alpha=0.3)

    # 统计标注
    total = block_mat.sum()
    low_nb = nb // 2  # 低阶 = 前一半块
    low_contrib = block_mat[:low_nb, :low_nb].sum()
    high_contrib = block_mat[low_nb:, low_nb:].sum()
    total_abs = np.abs(block_mat).sum()  # L1 norm as reference
    if total_abs < 1e-15:
        total_abs = 1.0
    info_text = (f"Total sum = {total:.4f}\n"
                 f"L1 norm = {total_abs:.4f}\n"
                 f"Low-order (m,n<{low_nb*BLOCK_SIZE}): {low_contrib:.4f} "
                 f"({low_contrib/total_abs*100:.1f}% of L1)\n"
                 f"High-order (m,n≥{low_nb*BLOCK_SIZE}): {high_contrib:.4f} "
                 f"({high_contrib/total_abs*100:.1f}% of L1)")
    axes[2].text(0.98, 0.97, info_text, transform=axes[2].transAxes,
                 fontsize=9, verticalalignment="top", horizontalalignment="right",
                 bbox=dict(boxstyle="round", facecolor="white", alpha=0.85))

    fig.tight_layout()
    fig.savefig(outpath, dpi=150)
    plt.close(fig)
    print(f"  Saved: {outpath}")
    print(f"    Total={total:.4f}, L1={total_abs:.4f}, "
          f"Low={low_contrib:.4f} ({low_contrib/total_abs*100:.1f}% L1), "
          f"High={high_contrib:.4f} ({high_contrib/total_abs*100:.1f}% L1)")


def plot_multi_M(block_mats: dict, outpath: str):
    """多 M 值 signed Re(Γ·μ) 对比面板."""
    M_list = sorted(block_mats.keys())
    n_M = len(M_list)
    ncols = min(3, n_M)
    nrows = (n_M + ncols - 1) // ncols

    fig, axes = plt.subplots(nrows, ncols, figsize=(6 * ncols, 5.5 * nrows),
                             squeeze=False)

    # 全局 vmax (用 M=4096 的对称范围)
    full_mat = block_mats[M_FULL]
    global_vmax = max(abs(full_mat.min()), abs(full_mat.max()))

    for idx, M in enumerate(M_list):
        row, col = idx // ncols, idx % ncols
        ax = axes[row][col]
        mat = block_mats[M]
        nb = mat.shape[0]

        im = ax.imshow(mat, cmap="RdBu_r", aspect="auto",
                       origin="upper", vmin=-global_vmax, vmax=global_vmax)
        ax.set_title(f"M={M} ({nb}×{nb} blocks)")
        ax.set_xlabel("jb block"); ax.set_ylabel("ib block")

        # 网格线
        for i in range(nb):
            ax.axhline(y=i + 0.5, color="gray", lw=0.2, alpha=0.3)
            ax.axvline(x=i + 0.5, color="gray", lw=0.2, alpha=0.3)

        # 统计
        total = mat.sum()
        half = nb // 2
        l1 = np.abs(mat).sum()
        if l1 < 1e-15:
            l1 = 1.0
        low_pct = mat[:half, :half].sum() / l1 * 100
        ax.text(0.02, 0.98, f"Σ={total:.3f}\nlow={low_pct:.0f}%",
                transform=ax.transAxes, fontsize=8, verticalalignment="top",
                bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

    # 隐藏空白子图
    for idx in range(n_M, nrows * ncols):
        row, col = idx // ncols, idx % ncols
        axes[row][col].set_visible(False)

    # 公共 colorbar
    cbar = fig.colorbar(im, ax=axes.ravel().tolist(), shrink=0.8, pad=0.02)
    cbar.set_label("Re(Γ·μ) block sum")

    fig.suptitle("Phase D — Block Contributions Re(Γ·μ) vs M (linear scale, truncated from M=4096)",
                 fontsize=14, y=1.01)
    fig.tight_layout()
    fig.savefig(outpath, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {outpath}")


def plot_M_vs_contrib(block_mats: dict, outpath: str):
    """综合 M vs 块贡献 — L1 标度 + 低阶/高阶占比 + 对角线剖面叠加."""
    M_list = sorted(block_mats.keys())
    cmap_M = plt.cm.viridis

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # ── 数据准备 ──
    l1_vals, total_vals = [], []
    low_fracs, high_fracs = [], []
    diag_profiles = {}  # M → normalized diagonal

    for M in M_list:
        mat = block_mats[M]
        nb = mat.shape[0]
        half = nb // 2

        l1 = np.abs(mat).sum()
        total = mat.sum()
        l1_vals.append(l1)
        total_vals.append(total)

        low_abs = np.abs(mat[:half, :half]).sum()
        high_abs = np.abs(mat[half:, half:]).sum()
        low_fracs.append(low_abs / l1 * 100 if l1 > 0 else 0)
        high_fracs.append(high_abs / l1 * 100 if l1 > 0 else 0)

        # 对角线剖面 (按块归一化到 [0,1])
        diag = np.array([mat[i, i] for i in range(nb)])
        diag_profiles[M] = diag

    # ── Panel 1: L1 norm vs M ──
    ax = axes[0, 0]
    colors = [cmap_M(i / (len(M_list) - 1)) for i in range(len(M_list))]
    ax.bar(range(len(M_list)), l1_vals, color=colors, edgecolor="black", linewidth=0.5)
    ax.set_xticks(range(len(M_list)))
    ax.set_xticklabels([str(m) for m in M_list])
    ax.set_xlabel("M (Chebyshev kernel size)")
    ax.set_ylabel("L1 norm = Σ|Re(Γ·μ)| per block")
    ax.set_title("Total |Re(Γ·μ)| content vs M")
    ax.grid(axis="y", alpha=0.3)
    # 数值标注
    for i, v in enumerate(l1_vals):
        ax.text(i, v + 0.002, f"{v:.3f}", ha="center", fontsize=8)

    # ── Panel 2: Low/High fraction vs M ──
    ax = axes[0, 1]
    x = np.arange(len(M_list))
    w = 0.35
    ax.bar(x - w/2, low_fracs, w, label="Low-order (m,n < M/2)", color="#4575b4",
           edgecolor="black", linewidth=0.3)
    ax.bar(x + w/2, high_fracs, w, label="High-order (m,n ≥ M/2)", color="#d73027",
           edgecolor="black", linewidth=0.3)
    ax.set_xticks(x)
    ax.set_xticklabels([str(m) for m in M_list])
    ax.set_xlabel("M (Chebyshev kernel size)")
    ax.set_ylabel("Fraction of L1 norm (%)")
    ax.set_title("Low-order vs High-order contribution fraction")
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.3)
    for i in range(len(M_list)):
        ax.text(i - w/2, low_fracs[i] + 0.5, f"{low_fracs[i]:.1f}%",
                ha="center", fontsize=7)
        ax.text(i + w/2, high_fracs[i] + 0.5, f"{high_fracs[i]:.1f}%",
                ha="center", fontsize=7)

    # ── Panel 3: Diagonal profile overlay (absolute m index) ──
    ax = axes[1, 0]
    for idx, M in enumerate(M_list):
        diag = diag_profiles[M]
        nb = len(diag)
        m_idx = np.arange(nb) * BLOCK_SIZE + BLOCK_SIZE / 2  # block中心
        color = cmap_M(idx / (len(M_list) - 1))
        ax.plot(m_idx, diag, "o-", color=color, label=f"M={M}", lw=1.2, ms=5)

    ax.axhline(y=0, color="black", lw=0.6, ls="--")
    ax.set_xlabel("m = n (Chebyshev index)")
    ax.set_ylabel("Re(Γ·μ) diagonal block sum")
    ax.set_title("Diagonal block Re(Γ·μ) vs Chebyshev index")
    ax.legend(fontsize=8, ncol=2)
    ax.grid(alpha=0.3)

    # ── Panel 4: Diagonal profile (normalized to [0,1] in block index) ──
    ax = axes[1, 1]
    for idx, M in enumerate(M_list):
        diag = diag_profiles[M]
        nb = len(diag)
        x_norm = np.linspace(0, 1, nb)
        color = cmap_M(idx / (len(M_list) - 1))
        ax.plot(x_norm, diag, "o-", color=color, label=f"M={M}", lw=1.2, ms=5)

    ax.axhline(y=0, color="black", lw=0.6, ls="--")
    ax.set_xlabel("Normalized Chebyshev index (m / M)")
    ax.set_ylabel("Re(Γ·μ) diagonal block sum")
    ax.set_title("Diagonal profile (normalized Chebyshev index)")
    ax.legend(fontsize=8, ncol=2)
    ax.grid(alpha=0.3)

    fig.suptitle("Phase D — M vs Block Contribution Summary (truncated from M=4096, Jackson M=4096 kernel)",
                 fontsize=14, y=1.01)
    fig.tight_layout()
    fig.savefig(outpath, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {outpath}")
    print(f"  L1: {dict(zip(M_list, [f'{v:.4f}' for v in l1_vals]))}")
    print(f"  Low%: {dict(zip(M_list, [f'{v:.1f}' for v in low_fracs]))}")
    print(f"  High%: {dict(zip(M_list, [f'{v:.1f}' for v in high_fracs]))}")


# ─── 主入口 ───────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("Phase D — Block Contribution Heatmaps (Linear Re(Γ·μ))")
    print("=" * 60)

    # 1. 解析 M=4096 权威数据
    print("\n[1] Parsing vbl_block_M4096.log...")
    if not os.path.exists(VBL_LOG):
        print(f"  ERROR: {VBL_LOG} not found!")
        sys.exit(1)
    full_mat = parse_vbl_block(VBL_LOG)
    print(f"  Block matrix shape: {full_mat.shape}")
    print(f"  Value range: [{full_mat.min():.6f}, {full_mat.max():.6f}]")

    # 2. M=4096 三面板详图
    print("\n[2] Plotting M=4096 detailed view...")
    plot_single_M(full_mat, M_FULL,
                  os.path.join(OUT_DIR, "block_contrib_M4096_linear.png"))

    # 3. 多 M 截断对比
    print("\n[3] Plotting multi-M truncated comparison...")
    block_mats = {}
    for M in M_TRUNC:
        mat = truncate_block_mat(full_mat, M)
        block_mats[M] = mat
        print(f"  M={M}: {mat.shape[0]}×{mat.shape[0]} blocks, "
              f"Σ={mat.sum():.4f}, range=[{mat.min():.4f}, {mat.max():.4f}]")

    plot_multi_M(block_mats,
                 os.path.join(OUT_DIR, "block_contrib_all_M_linear.png"))

    # 4. M vs 块贡献综合图
    print("\n[4] Plotting M vs block contribution summary...")
    plot_M_vs_contrib(block_mats,
                      os.path.join(OUT_DIR, "block_contrib_M_vs_summary.png"))

    print("\n[Done] All figures saved to", OUT_DIR)
    print("  - block_contrib_M4096_linear.png   (M=4096, 3-panel detailed)")
    print("  - block_contrib_all_M_linear.png    (M=2048-4096, multi-M comparison)")
    print("  - block_contrib_M_vs_summary.png    (M vs contribution summary)")


if __name__ == "__main__":
    main()
