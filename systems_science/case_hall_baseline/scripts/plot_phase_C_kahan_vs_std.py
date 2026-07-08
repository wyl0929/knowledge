#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-25 05:58:04
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-25 05:58:06
#FilePath     : /MG/test/plot_phase_C_kahan_vs_std.py
#Description  :

#!/usr/bin/env python3
"""
plot_phase_C_kahan_vs_std.py — Phase C Kahan vs Standard σ_xy 偏移对比

横轴 M, 纵轴 σ_xy(EF=0), 双曲线: Standard (load-/save-mode) vs Kahan

数据来源:
  Standard: runs/0624/hall_AB_d0.000_m64_M*_{save,load}_B100.0.txt (Phase A)
  Kahan:    Phase C 汇总表 (docs/sigma/task_vbl_trace.md §Phase C 总结)

用法: python test/plot_phase_C_kahan_vs_std.py
输出: test/kahan_vs_standard.png
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

# ─── 硬编码数据 ─────────────────────────────────────────────────────────────
# Standard (非 Kahan, Phase A)
#   save-mode: 直接从集群 save 输出读取 (EF=0)
#   load-mode: 从 M=4096 μ 截断后 load 输出读取
M_std_save     = np.array([2048,            4096])
sig_std_save   = np.array([-5.9411,         1060.1406])

M_std_load     = np.array([2048,   2560,    3072,    3584])
sig_std_load   = np.array([5.5753, 10.1167, 150.850, 950.4108])

# Kahan (Phase C 汇总表, 集群 Kahan 编译版重算)
M_kahan        = np.array([2048,   2560,  3072,   3584,   4096])
sig_kahan      = np.array([10.1,   10.1,  150.9,  950.4,  2945.2])

# ─── 绘图 ──────────────────────────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(10, 6))

# Kahan curve
ax.plot(M_kahan, sig_kahan, "s-", color="#d73027", lw=2, ms=8,
        label="Kahan (Phase C, cluster recompute)")

# Standard load-mode (截断 μ)
ax.plot(M_std_load, sig_std_load, "o--", color="#4575b4", lw=1.5, ms=7,
        label="Standard load-mode (Phase A6, truncated μ)")

# Standard save-mode (标记点)
ax.scatter(M_std_save, sig_std_save, marker="D", s=80, color="#fc8d59",
           zorder=5, edgecolors="black", linewidth=0.5,
           label="Standard save-mode (Phase A, fresh compute)")

# 标注数值
for m, s in zip(M_std_save, sig_std_save):
    ax.annotate(f"{s:.1f}", (m, s), textcoords="offset points",
                xytext=(10, -12), fontsize=8, color="#fc8d59")
for m, s in zip(M_kahan, sig_kahan):
    ax.annotate(f"{s:.1f}", (m, s), textcoords="offset points",
                xytext=(10, 10), fontsize=8, color="#d73027")

# 零参考线
ax.axhline(y=0, color="gray", lw=0.8, ls="--", alpha=0.5)

# 标签
ax.set_xlabel("M (Chebyshev kernel size)", fontsize=13)
ax.set_ylabel(r"$\sigma_{xy}(E_F=0)$ (e$^2$/h)", fontsize=13)
ax.set_title("Phase C — Kahan vs Standard: σ_xy offset vs M (m=64, B=100T, AB monolayer)",
             fontsize=13)
ax.legend(fontsize=10, loc="upper left")
ax.grid(alpha=0.3)

# 注释
note = ("Standard load-mode: truncated mu from M=4096 (Phase A6).\n"
        "Standard save-mode: fresh compute at given M (Phase A).\n"
        "Kahan: fresh compute with -DTBPLAS_KAHAN_SUM (Phase C).\n"
        "WARNING: load-mode ~= Kahan for M>=2560; see discussion.")
ax.text(0.98, 0.02, note, transform=ax.transAxes, fontsize=8,
        verticalalignment="bottom", horizontalalignment="right",
        bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.9))

fig.tight_layout()
outpath = "test/kahan_vs_standard.png"
fig.savefig(outpath, dpi=150)
plt.close(fig)
print(f"Saved: {outpath}")

# ─── 打印数据表 ─────────────────────────────────────────────────────────────
print("\n数据汇总:")
print(f"{'M':>6}  {'Std(save)':>11}  {'Std(load)':>11}  {'Kahan':>11}")
print("-" * 45)
for m in sorted(set(M_std_save) | set(M_std_load) | set(M_kahan)):
    ss = sig_std_save[M_std_save == m][0] if m in M_std_save else float("nan")
    sl = sig_std_load[M_std_load == m][0] if m in M_std_load else float("nan")
    sk = sig_kahan[M_kahan == m][0] if m in M_kahan else float("nan")
    print(f"{m:6d}  {ss:11.4f}  {sl:11.4f}  {sk:11.4f}")
