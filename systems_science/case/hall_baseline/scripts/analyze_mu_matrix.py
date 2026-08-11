#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-24 15:12:48
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-24 15:12:50
#FilePath     : /MG/test/analyze_mu_matrix.py
#Description  :

#!/usr/bin/env python3
"""
analyze_mu_matrix.py — μ 矩阵离线分析 (VBL Phase A: A3–A5)

功能:
  A3 — Hermiticity 检验
  A4 — μ 矩阵量级热图
  A5 — 逐行/列统计

用法:
  python test/analyze_mu_matrix.py
"""

import h5py
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

# ─── 配置 ─────────────────────────────────────────────────────────────────
RUNS_DIR = "runs/0624"
FILES = {
    "M2048": os.path.join(RUNS_DIR, "mu_raw_M2048_m64.h5"),
    "M4096": os.path.join(RUNS_DIR, "mu_raw_M4096_m64.h5"),
}
OUT_DIR = "test"
os.makedirs(OUT_DIR, exist_ok=True)


# ─── 工具函数 ─────────────────────────────────────────────────────────────

def load_mu(path):
    """加载 mu_raw (M, 2M) interleaved → 转换为 (M, M) complex"""
    with h5py.File(path, "r") as f:
        raw = f["mu_raw"][:]
        meta = f["metadata"][:]
    M = raw.shape[0]
    # interleaved to complex
    mu = raw[:, 0::2] + 1j * raw[:, 1::2]
    print(f"  Loaded: shape={raw.shape} → ({M},{M}) complex, metadata={meta[:].tolist()}")
    return mu


# ═══════════════════════════════════════════════════════════════════════════
# A3 — Hermiticity 检验
# ═══════════════════════════════════════════════════════════════════════════

def check_hermiticity(mu):
    """返回 |mu_{mn} - mu_{nm}^*| 的统计"""
    diff = np.abs(mu - mu.conj().T)
    stats = {
        "max": diff.max(),
        "mean": diff.mean(),
        "median": np.median(diff),
        "p99": np.percentile(diff, 99),
        "bad_frac": (diff > 1e-10).mean(),
    }
    return stats


def run_a3():
    """A3 — Hermiticity 检验"""
    print("=" * 60)
    print("A3 — μ 矩阵 Hermiticity 检验")
    print("=" * 60)

    report_lines = ["# μ 矩阵 Hermiticity 检验报告\n"]
    report_lines.append(f"| Label | max | mean | median | p99 | bad_frac (>1e-10) |")
    report_lines.append(f"|-------|-----|------|--------|-----|-------------------|")

    results = {}
    for label, path in FILES.items():
        print(f"\n[{label}]")
        mu = load_mu(path)
        stats = check_hermiticity(mu)
        results[label] = stats
        line = (f"| {label} | {stats['max']:.2e} | {stats['mean']:.2e} | "
                f"{stats['median']:.2e} | {stats['p99']:.2e} | {stats['bad_frac']:.2%} |")
        report_lines.append(line)
        print(f"  max={stats['max']:.2e}  mean={stats['mean']:.2e}  "
              f"median={stats['median']:.2e}  p99={stats['p99']:.2e}  "
              f"bad_frac={stats['bad_frac']:.2%}")

    # 对比判定
    ratio = results["M4096"]["mean"] / results["M2048"]["mean"]
    verdict = "正常 (同级)" if ratio < 10 else f"异常 (M4096/M2048={ratio:.1f}×)"
    report_lines.append(f"\n**判定**: M4096/M2048 mean 比 = {ratio:.1f}× → {verdict}")
    if ratio >= 10:
        report_lines.append("→ 建议跳转 Phase D (μ 矩阵已受污染)")
    else:
        report_lines.append("→ μ 内积构建精度正常，建议继续 Phase B")

    report_path = os.path.join(OUT_DIR, "mu_hermiticity_report.txt")
    with open(report_path, "w") as f:
        f.write("\n".join(report_lines) + "\n")
    print(f"\n报告已写入: {report_path}")
    return results


# ═══════════════════════════════════════════════════════════════════════════
# A4 — μ 矩阵量级热图
# ═══════════════════════════════════════════════════════════════════════════

def plot_mu_heatmap(mu, title, outpath):
    """绘制 log10|mu_mn| 2D 热图"""
    log_mu = np.log10(np.maximum(np.abs(mu), 1e-20))
    plt.figure(figsize=(8, 7))
    plt.imshow(log_mu, aspect="auto", cmap="viridis",
               extent=[0, mu.shape[1], mu.shape[0], 0])
    plt.colorbar(label=r"$\log_{10}|\mu_{mn}|$")
    plt.xlabel("n")
    plt.ylabel("m")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()
    print(f"  热图已保存: {outpath}")


def run_a4():
    """A4 — μ 矩阵量级热图"""
    print("\n" + "=" * 60)
    print("A4 — μ 矩阵量级热图")
    print("=" * 60)

    fig, axes = plt.subplots(1, 2, figsize=(16, 7))

    for idx, (label, path) in enumerate(FILES.items()):
        print(f"\n[{label}]")
        mu = load_mu(path)
        log_mu = np.log10(np.maximum(np.abs(mu), 1e-20))
        im = axes[idx].imshow(log_mu, aspect="auto", cmap="viridis",
                              extent=[0, mu.shape[1], mu.shape[0], 0])
        axes[idx].set_title(f"{label}  μ 矩阵量级热图")
        axes[idx].set_xlabel("n")
        axes[idx].set_ylabel("m")
        fig.colorbar(im, ax=axes[idx], label=r"$\log_{10}|\mu_{mn}|$")

        # 单独保存
        single_path = os.path.join(OUT_DIR, f"mu_heatmap_{label}.png")
        plt.figure(figsize=(8, 7))
        plt.imshow(log_mu, aspect="auto", cmap="viridis",
                   extent=[0, mu.shape[1], mu.shape[0], 0])
        plt.colorbar(label=r"$\log_{10}|\mu_{mn}|$")
        plt.xlabel("n")
        plt.ylabel("m")
        plt.title(f"{label}  μ 矩阵量级热图")
        plt.tight_layout()
        plt.savefig(single_path, dpi=150)
        plt.close()
        print(f"  热图已保存: {single_path}")

    plt.tight_layout()
    combined_path = os.path.join(OUT_DIR, "mu_heatmap_comparison.png")
    fig.savefig(combined_path, dpi=150)
    plt.close()
    print(f"\n  对比图已保存: {combined_path}")


# ═══════════════════════════════════════════════════════════════════════════
# A5 — μ 矩阵逐行/列统计
# ═══════════════════════════════════════════════════════════════════════════

def extract_diag_stats(mu):
    """返回逐行 norm, mean, std"""
    row_norms = np.linalg.norm(mu, axis=1)
    row_means = np.mean(np.abs(mu), axis=1)
    row_stds = np.std(np.abs(mu), axis=1)
    return row_norms, row_means, row_stds


def run_a5():
    """A5 — μ 矩阵逐行/列统计"""
    print("\n" + "=" * 60)
    print("A5 — μ 矩阵逐行/列统计")
    print("=" * 60)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    stats_data = {}
    for label, path in FILES.items():
        print(f"\n[{label}]")
        mu = load_mu(path)
        row_norms, row_means, row_stds = extract_diag_stats(mu)
        stats_data[label] = {
            "row_norms": row_norms,
            "row_means": row_means,
            "row_stds": row_stds,
        }

        # 保存统计到 txt
        stat_path = os.path.join(OUT_DIR, f"mu_stats_{label}.txt")
        header = f"# {label} 逐行统计\n# m  row_norm  row_mean  row_std\n"
        np.savetxt(stat_path, np.column_stack([
            np.arange(len(row_norms)), row_norms, row_means, row_stds
        ]), fmt="%d  %.6e  %.6e  %.6e", header=header)
        print(f"  统计已保存: {stat_path}")

    # 双对数绘制 row_norm vs m
    for label, data in stats_data.items():
        m_idx = np.arange(len(data["row_norms"]))
        axes[0].loglog(m_idx, data["row_norms"], label=label, linewidth=1.5)
        axes[1].semilogy(m_idx, data["row_means"], label=label, linewidth=1.5)

    axes[0].set_xlabel("m (Chebyshev 阶数)")
    axes[0].set_ylabel(r"$\|\mu_{m*}\|$ (行 norm)")
    axes[0].set_title("行 norm vs m (双对数)")
    axes[0].legend()
    axes[0].grid(True, which="both", alpha=0.3)

    axes[1].set_xlabel("m (Chebyshev 阶数)")
    axes[1].set_ylabel(r"均值 $|\mu_{mn}|$")
    axes[1].set_title("行均值 vs m (半对数)")
    axes[1].legend()
    axes[1].grid(True, which="both", alpha=0.3)

    plt.tight_layout()
    comp_path = os.path.join(OUT_DIR, "mu_row_norm_comparison.png")
    fig.savefig(comp_path, dpi=150)
    plt.close()
    print(f"\n  对比图已保存: {comp_path}")

    # 分析: 检查 M=4096 在高 m 区是否偏离 M=2048 外推
    norms_2048 = stats_data["M2048"]["row_norms"]
    norms_4096 = stats_data["M4096"]["row_norms"]
    overlap_end = min(len(norms_2048), 2000)
    if len(norms_4096) > overlap_end:
        # 重叠区域一致性
        ratio_overlap = norms_4096[:overlap_end] / norms_2048[:overlap_end]
        mean_ratio = np.mean(ratio_overlap)
        std_ratio = np.std(ratio_overlap)
        print(f"\n  重叠区域 (m<{overlap_end}) 比值: mean={mean_ratio:.4f}, std={std_ratio:.4f}")

        # 高阶区 (m>2048) 趋势检查
        high_start = 2048
        high_norms = norms_4096[high_start:]
        # 用 M=2048 的最后 200 点外推
        extrap_base = norms_2048[-200:]
        extrap_trend = np.polyfit(np.arange(len(extrap_base)), np.log(extrap_base), 1)
        extrap_at_high = np.exp(extrap_trend[1]) * np.exp(extrap_trend[0] * (
            np.arange(high_start, len(norms_4096)) - (len(norms_2048) - 200)))
        deviation = high_norms / extrap_at_high
        max_dev = deviation.max()
        print(f"  高阶区 (m>{high_start}) 偏离外推: max={max_dev:.2f}×")
        if max_dev > 2:
            print(f"  ⚠️ 高 m 区行 norm 偏离外推趋势 > 2× → 可疑")
        else:
            print(f"  ✅ 高 m 区行 norm 在外推范围内")

    return stats_data


# ═══════════════════════════════════════════════════════════════════════════
# 主入口
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("VBL Phase A — μ 矩阵离线分析")
    print("=" * 60)

    results_a3 = run_a3()
    run_a4()
    run_a5()

    print("\n" + "=" * 60)
    print("所有分析完成!")
    print("=" * 60)
