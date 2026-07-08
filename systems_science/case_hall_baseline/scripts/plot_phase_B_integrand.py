#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-25 07:12:04
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-25 07:12:06
#FilePath     : /MG/test/plot_phase_B_integrand.py
#Description  :

#!/usr/bin/env python3
"""
plot_phase_B_integrand.py — Phase B θ 积分被积函数 S_M(θ)/sin³θ vs θ

S_M(θ) = Σ_{m,n=0}^{M-1} Γ_{mn}(θ) · μ_{mn}
被积函数 = S_M(θ) / sin³θ

数据源: runs/0624/vbl_sum_M*.log (Phase B VBL_SUM 输出)
两幅图: 对数坐标 + 普通坐标, 各 M 曲线叠加

用法: python test/plot_phase_B_integrand.py
输出: test/integrand_vs_theta_log.png / test/integrand_vs_theta_lin.png
"""

import re
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ─── Parse ──────────────────────────────────────────────────────────────────
M_list = [2048, 2560, 3072, 3584, 4096]
data = {}  # M -> (theta, mean_sum, std_sum)

for M in M_list:
    fpath = f"runs/0624/vbl_sum_M{M}.log"
    all_theta = []
    all_sum = []
    with open(fpath) as f:
        for line in f:
            line = line.strip()
            if not line.startswith(f"M={M}"):
                continue
            # M=4096 rs=1 0.00076699:2.46845e-15 0.00230097:2.01906e-15 ...
            parts = line.split()
            theta_vals = []
            sum_vals = []
            for token in parts[2:]:  # skip "M=..." and "rs=..."
                if ":" not in token:
                    continue
                t_str, s_str = token.split(":", 1)
                theta_vals.append(float(t_str))
                sum_vals.append(float(s_str))
            all_theta.append(np.array(theta_vals))
            all_sum.append(np.array(sum_vals))

    theta = all_theta[0]  # all ranks share same theta grid
    sum_stack = np.array(all_sum)  # (n_ranks, n_theta)
    mean_sum = sum_stack.mean(axis=0)
    std_sum = sum_stack.std(axis=0)
    data[M] = (theta, mean_sum, std_sum)
    print(f"  M={M}: {len(theta)} theta points, "
          f"sum range=[{mean_sum.min():.2e}, {mean_sum.max():.2e}], "
          f"n_ranks={len(all_sum)}")

# ─── Compute integrand ──────────────────────────────────────────────────────
for M in M_list:
    theta, mean_sum, _ = data[M]
    sin_th = np.sin(theta)
    # Avoid division by zero at theta=0, pi
    sin_th = np.maximum(sin_th, 1e-15)
    integrand = mean_sum / (sin_th ** 3)
    data[M] = (theta, mean_sum, integrand)

# ─── Plot ───────────────────────────────────────────────────────────────────
cmap = plt.cm.tab10

# ── Figure 1: Log scale ──
fig1, axes1 = plt.subplots(1, 2, figsize=(16, 6))

for idx, M in enumerate(M_list):
    theta, mean_sum, integrand = data[M]
    color = cmap(idx)
    # Left: signed |integrand|
    abs_integrand = np.abs(integrand)
    axes1[0].semilogy(theta, abs_integrand, "-", color=color, label=f"M={M}", lw=1.0, alpha=0.8)

    # Right: zoom θ ∈ [π/4, 3π/4]
    mask = (theta >= np.pi / 4) & (theta <= 3 * np.pi / 4)
    axes1[1].semilogy(theta[mask], abs_integrand[mask], "-", color=color, label=f"M={M}", lw=1.2)

axes1[0].set_xlabel(r"$\theta$"); axes1[0].set_ylabel(r"$|S_M(\theta)/\sin^3\theta|$ (log)")
axes1[0].set_title("Integrand magnitude vs θ — Full range [0, π]")
axes1[0].legend(fontsize=8, ncol=2); axes1[0].grid(alpha=0.3, which="both")

axes1[1].set_xlabel(r"$\theta$"); axes1[1].set_ylabel(r"$|S_M(\theta)/\sin^3\theta|$ (log)")
axes1[1].set_title("Integrand magnitude — Zoom [π/4, 3π/4]")
axes1[1].legend(fontsize=8, ncol=2); axes1[1].grid(alpha=0.3, which="both")

fig1.suptitle(r"Phase B — $\frac{1}{\sin^3\theta}\sum\Gamma_{\mu}$ vs θ (log scale, m=64, B=100T)",
             fontsize=14, y=1.01)
fig1.tight_layout()
out1 = "test/integrand_vs_theta_log.png"
fig1.savefig(out1, dpi=150)
plt.close(fig1)
print(f"\nSaved: {out1}")

# ── Figure 2: Linear scale ──
fig2, axes2 = plt.subplots(1, 2, figsize=(16, 6))

for idx, M in enumerate(M_list):
    theta, mean_sum, integrand = data[M]
    color = cmap(idx)

    # Left: full range
    axes2[0].plot(theta, integrand, "-", color=color, label=f"M={M}", lw=0.6, alpha=0.8)

    # Right: zoom central region
    mask = (theta >= 1.0) & (theta <= np.pi - 1.0)  # ~57° to ~123°
    axes2[1].plot(theta[mask], integrand[mask], "-", color=color, label=f"M={M}", lw=1.0)

axes2[0].set_xlabel(r"$\theta$"); axes2[0].set_ylabel(r"$S_M(\theta)/\sin^3\theta$")
axes2[0].set_title("Integrand vs θ — Full range [0, π] (linear)")
axes2[0].legend(fontsize=8, ncol=2); axes2[0].grid(alpha=0.3)

axes2[1].set_xlabel(r"$\theta$"); axes2[1].set_ylabel(r"$S_M(\theta)/\sin^3\theta$")
axes2[1].set_title("Integrand vs θ — Zoom [1.0, π−1.0] (linear)")
axes2[1].legend(fontsize=8, ncol=2); axes2[1].grid(alpha=0.3)

fig2.suptitle(r"Phase B — $\frac{1}{\sin^3\theta}\sum\Gamma_{\mu}$ vs θ (linear, m=64, B=100T)",
             fontsize=14, y=1.01)
fig2.tight_layout()
out2 = "test/integrand_vs_theta_lin.png"
fig2.savefig(out2, dpi=150)
plt.close(fig2)
print(f"Saved: {out2}")

# ── Figure 3: Scatter + lines, y ∈ [10^2, 10^5], with integral annotation ──
# Load sigma_xy(EF=0) for each M from save/load data
sigma_xy = {}
for M in M_list:
    fpath_save = f"runs/0624/hall_AB_d0.000_m64_M{M}_save_B100.0.txt"
    fpath_load = f"runs/0624/hall_AB_d0.000_m64_M{M}_load_B100.0.txt"
    if os.path.exists(fpath_save):
        d = np.loadtxt(fpath_save)
        idx0 = np.argmin(np.abs(d[:, 0]))
        sigma_xy[M] = (d[idx0, 1], "save")
    elif os.path.exists(fpath_load):
        d = np.loadtxt(fpath_load)
        idx0 = np.argmin(np.abs(d[:, 0]))
        sigma_xy[M] = (d[idx0, 1], "load")
    else:
        sigma_xy[M] = (np.nan, "?")

# ── Figure 3: Scatter, M=2048/3072/4096 only, distinct markers ──
M_scatter = [2048, 3072, 4096]
markers = ["o", "s", "D"]  # circle, square, diamond
colors_scatter = ["#2166ac", "#f4a582", "#b2182b"]

fig3, ax3 = plt.subplots(figsize=(12, 8))

for idx, M in enumerate(M_scatter):
    theta, _, integrand = data[M]
    s, src = sigma_xy[M]
    step = max(1, len(theta) // 150)
    t_sub = theta[::step]
    ig_sub = np.abs(integrand[::step])
    ax3.semilogy(t_sub, ig_sub, marker=markers[idx], color=colors_scatter[idx],
                 linestyle="none", ms=3.5, alpha=0.7,
                 label=f"M={M}  ({markers[idx]})  |  {s:.0f} e^2/h")

ax3.set_xlabel(r"$\theta$", fontsize=13)
ax3.set_ylabel(r"$|S_M(\theta)/\sin^3\theta|$", fontsize=13)
ax3.set_title(r"Integrand magnitude $|S_M/\sin^3\theta|$ vs $\theta$ (m=64, B=100T)",
             fontsize=14)
ax3.set_ylim(1e2, 1e5)
ax3.legend(fontsize=10, loc="upper center", markerscale=2)
ax3.grid(alpha=0.3, which="both")

text_lines = [r"$\sigma_{xy}(E_F=0)$:"]
for M in M_scatter:
    s, src = sigma_xy[M]
    text_lines.append(f"  M={M}: {s:.1f} e^2/h ({src})")
ax3.text(0.02, 0.98, "\n".join(text_lines), transform=ax3.transAxes,
         fontsize=9, verticalalignment="top", fontfamily="monospace",
         bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.9))

fig3.tight_layout()
out3 = "test/integrand_vs_theta_scatter.png"
fig3.savefig(out3, dpi=150)
plt.close(fig3)
print(f"Saved: {out3}")

# ── Figure 4: Bare sum S_M(θ) = Σ Γμ, scatter, M=2048/3072/4096 ──
fig4, ax4 = plt.subplots(figsize=(12, 8))

for idx, M in enumerate(M_scatter):
    theta, mean_sum, _ = data[M]
    s, src = sigma_xy[M]
    step = max(1, len(theta) // 150)
    t_sub = theta[::step]
    sum_sub = np.abs(mean_sum[::step])
    ax4.plot(t_sub, sum_sub, marker=markers[idx], color=colors_scatter[idx],
             linestyle="none", ms=3.5, alpha=0.7,
             label=f"M={M}  ({markers[idx]})  |  {s:.0f} e^2/h")

ax4.set_xlabel(r"$\theta$", fontsize=13)
ax4.set_ylabel(r"$|S_M(\theta)| = |\sum_{m,n}\Gamma_{mn}(\theta)\,\mu_{mn}|$", fontsize=13)
ax4.set_title(r"Bare sum $|S_M(\theta)|$ vs $\theta$  —  before $1/\sin^3\theta$ weight (linear, m=64, B=100T)",
             fontsize=14)
ax4.legend(fontsize=10, loc="upper center", markerscale=2)
ax4.grid(alpha=0.3, which="both")

# ── Quantitative shift analysis in θ ∈ [0.5, 2.6] ──
mask_shift = (theta >= 0.5) & (theta <= 2.6)
ref_sum = np.abs(data[2048][1][mask_shift])  # |S_2048|
shift_text = [r"Mean |S_M| / |S_2048| in $\theta\in[0.5,2.6]$:"]
for M in [3072, 4096]:
    cur_sum = np.abs(data[M][1][mask_shift])
    ratio = cur_sum / np.maximum(ref_sum, 1e-30)
    mean_ratio = np.mean(ratio)
    median_ratio = np.median(ratio)
    # Also compute per-point excess
    excess = cur_sum - ref_sum
    mean_excess = np.mean(excess)
    shift_text.append(f"  M={M}: mean ratio={mean_ratio:.2f}×, median={median_ratio:.2f}×")
    shift_text.append(f"          mean |Δ| = {mean_excess:.1e}")
    print(f"M={M} vs M=2048 in θ∈[0.5,2.6]: "
          f"mean_ratio={mean_ratio:.2f}×, median_ratio={median_ratio:.2f}×, "
          f"mean_excess={mean_excess:.2e}")

ax4.text(0.02, 0.98, "\n".join(shift_text), transform=ax4.transAxes,
         fontsize=9, verticalalignment="top", fontfamily="monospace",
         bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.9))

# Shade the analysis region
ax4.axvspan(0.5, 2.6, alpha=0.07, color="gray")
ax4.annotate(r"$\theta\in[0.5,2.6]$", xy=(1.55, 1e2), fontsize=9,
             ha="center", color="gray")

fig4.tight_layout()
out4 = "test/sum_vs_theta_scatter.png"
fig4.savefig(out4, dpi=150)
plt.close(fig4)
print(f"Saved: {out4}")

# ── Print σ_xy values ──
print("\nσ_xy(EF=0) for annotation:")
for M in M_list:
    s, src = sigma_xy[M]
    print(f"  M={M}: {s:.1f} e²/h ({src})")

# ── Print key values at θ=π/2 ──
print("\nIntegrand at θ=π/2 (midpoint):")
for M in M_list:
    theta, _, integrand = data[M]
    idx_mid = np.argmin(np.abs(theta - np.pi / 2))
    print(f"  M={M}: θ={theta[idx_mid]:.4f}, S={data[M][1][idx_mid]:.4e}, "
          f"S/sin³={integrand[idx_mid]:.4f}")
