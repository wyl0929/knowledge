#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-28 00:24:13
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-28 00:24:17
#FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/src/visualize.py
#Description  :

#!/usr/bin/env python3
"""
visualize.py — publication-grade figures for Γ-μ random walk simulation.

Plan reference: docs/plan.md §4.6

Figures:
  1. main_error_vs_M      — RMS error vs M, 6 kernel×method lines (log-log)
  2. scaling_law           — log-log + fit line + α, R² annotation
  3. gamma_heatmap         — |Γ| heatmap (small M=64)
  4. mu_heatmap            — μ values heatmap (small M=64)
  5. kernel_profiles       — Jackson vs Lorentz kernel curves
  6. comprehensive_summary — 4-panel summary figure
  7. lorentz_lambda        — α vs λ (from P4 data)
  8. ranking_bar           — horizontal bar chart of convergence ranking
"""

import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Style settings
plt.rcParams.update({
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'legend.fontsize': 8,
    'figure.dpi': 150,
    'savefig.dpi': 150,
    'savefig.bbox': 'tight',
})

# Color scheme
COLORS = {
    'clean': '#e41a1c',
    'jackson': '#377eb8',
    'lorentz': '#4daf4a',
}
LINE_STYLES = {
    'sequential': '-',
    'kahan': '--',
}
MARKERS = {
    'clean': 'o',
    'jackson': 's',
    'lorentz': '^',
}

OUTPUT_DIR = 'output/figures'
DATA_DIR = 'output/data'


def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


# ===========================================================================
# Figure 1: Main error vs M (6 lines)
# ===========================================================================

def plot_error_vs_M(df=None):
    """RMS error vs M for all kernel×method combinations."""
    if df is None:
        df = pd.read_csv(os.path.join(DATA_DIR, 'scan_results.csv'))

    ensure_output_dir()
    fig, ax = plt.subplots(figsize=(7, 5))

    for kernel in ['clean', 'jackson', 'lorentz']:
        for method in ['sequential', 'kahan']:
            mask = (df['mu_kernel'] == kernel) & (df['method'] == method)
            subset = df[mask]
            M_groups = subset.groupby('M')['abs_err'].apply(
                lambda x: np.sqrt(np.mean(np.square(x.astype(float)))))
            M_vals = np.array(list(M_groups.index), dtype=float)
            rms_vals = np.array(list(M_groups.values), dtype=float)

            valid = (rms_vals > 0) & (~np.isnan(rms_vals))
            M_v = M_vals[valid]
            rms_v = rms_vals[valid]

            label = f"{kernel}+{method}"
            color = COLORS[kernel]
            ls = LINE_STYLES[method]
            marker = MARKERS[kernel]

            ax.loglog(M_v, rms_v, color=color, linestyle=ls, marker=marker,
                      markersize=4, linewidth=1.2, label=label, alpha=0.85)

    # Reference line: ∝ M²
    M_ref = np.array([64, 8192])
    rms_ref = 1e-21 * M_ref ** 2
    ax.loglog(M_ref, rms_ref, 'k:', linewidth=0.8, alpha=0.4, label=r'$\propto M^2$')

    ax.set_xlabel('M (Chebyshev order)')
    ax.set_ylabel('RMS absolute error')
    ax.set_title('Γ-μ Random Walk: RMS Error vs M')
    ax.legend(ncol=2, fontsize=7, framealpha=0.8)
    ax.grid(True, alpha=0.3, which='both')

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, 'main_error_vs_M.png'))
    plt.close(fig)
    print("  ✓ main_error_vs_M.png")


# ===========================================================================
# Figure 2: Scaling law fit
# ===========================================================================

def plot_scaling_law(df=None):
    """Log-log plot with scaling law fit for each kernel+method."""
    if df is None:
        df = pd.read_csv(os.path.join(DATA_DIR, 'scan_results.csv'))

    ensure_output_dir()
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    axes = axes.flatten()

    kernels = ['clean', 'jackson', 'lorentz']
    methods = ['sequential', 'kahan']

    for idx, (kernel, method) in enumerate(
        [(k, m) for k in kernels for m in methods]):
        ax = axes[idx]

        mask = (df['mu_kernel'] == kernel) & (df['method'] == method)
        subset = df[mask]
        M_groups = subset.groupby('M')['abs_err'].apply(
            lambda x: np.sqrt(np.mean(np.square(x.astype(float)))))
        M_vals = np.array(list(M_groups.index), dtype=float)
        rms_vals = np.array(list(M_groups.values), dtype=float)

        valid = (rms_vals > 0) & (~np.isnan(rms_vals))
        M_v = M_vals[valid]
        rms_v = rms_vals[valid]

        ax.loglog(M_v, rms_v, 'o', color=COLORS[kernel], markersize=4, alpha=0.7)

        if len(M_v) >= 4:
            x = np.log10(M_v)
            y = np.log10(rms_v)
            coeffs = np.polyfit(x, y, 1)
            alpha, beta = coeffs[0], coeffs[1]
            y_pred = alpha * x + beta
            ss_res = np.sum((y - y_pred) ** 2)
            ss_tot = np.sum((y - np.mean(y)) ** 2)
            R2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0

            M_fit = np.logspace(np.log10(M_v[0]), np.log10(M_v[-1]), 100)
            rms_fit = 10 ** (alpha * np.log10(M_fit) + beta)
            ax.loglog(M_fit, rms_fit, '--', color='gray', linewidth=0.8, alpha=0.6)
            ax.text(0.05, 0.95, f'α={alpha:.3f}\nR²={R2:.4f}',
                    transform=ax.transAxes, fontsize=7, verticalalignment='top',
                    bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        ax.set_title(f'{kernel} + {method}', fontsize=9)
        ax.grid(True, alpha=0.3, which='both')
        ax.set_xlabel('M')
        ax.set_ylabel('RMS error')

    fig.suptitle('Scaling Law Fits: RMS ∝ M^α', fontsize=12)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, 'scaling_law.png'))
    plt.close(fig)
    print("  ✓ scaling_law.png")


# ===========================================================================
# Figure 3: Gamma heatmap
# ===========================================================================

def plot_gamma_heatmap(M=64, theta=np.pi/4):
    """|Gamma| heatmap for small M."""
    from gamma_matrix import gamma_matrix_full

    ensure_output_dir()
    gamma = gamma_matrix_full(M, theta)
    gamma_abs = np.abs(gamma)

    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(gamma_abs, cmap='inferno', aspect='auto', origin='lower',
                   extent=[0, M-1, 0, M-1])
    plt.colorbar(im, ax=ax, label='|Γ_mn|')
    ax.set_xlabel('n')
    ax.set_ylabel('m')
    ax.set_title(f'|Γ| Heatmap (M={M}, θ=π/4)')

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, 'gamma_heatmap.png'))
    plt.close(fig)
    print("  ✓ gamma_heatmap.png")


# ===========================================================================
# Figure 4: Mu heatmap
# ===========================================================================

def plot_mu_heatmap(M=64):
    """μ values heatmap for small M (clean kernel)."""
    from mu_matrix import mu_raw_clean

    ensure_output_dir()
    mu = mu_raw_clean(M, E0=0.0)

    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(mu, cmap='RdBu_r', aspect='auto', origin='lower',
                   vmin=-1, vmax=1, extent=[0, M-1, 0, M-1])
    plt.colorbar(im, ax=ax, label='μ_mn')
    ax.set_xlabel('n')
    ax.set_ylabel('m')
    ax.set_title(f'μ (clean) Heatmap (M={M}, E₀=0)')

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, 'mu_heatmap.png'))
    plt.close(fig)
    print("  ✓ mu_heatmap.png")


# ===========================================================================
# Figure 5: Kernel profiles
# ===========================================================================

def plot_kernel_profiles(M=256):
    """Jackson vs Lorentz kernel function curves."""
    from mu_matrix import jackson_kernel_vector, lorentz_kernel_vector

    ensure_output_dir()
    n = np.arange(M)

    jackson_kv = jackson_kernel_vector(M)
    lorentz_kv_4 = lorentz_kernel_vector(M, lam=4.0)
    lorentz_kv_2 = lorentz_kernel_vector(M, lam=2.0)
    lorentz_kv_6 = lorentz_kernel_vector(M, lam=6.0)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(n/M, jackson_kv, label='Jackson', color=COLORS['jackson'], linewidth=1.5)
    ax.plot(n/M, lorentz_kv_2, label='Lorentz λ=2', color='#ff7f00', linewidth=1.2, linestyle='--')
    ax.plot(n/M, lorentz_kv_4, label='Lorentz λ=4', color=COLORS['lorentz'], linewidth=1.5)
    ax.plot(n/M, lorentz_kv_6, label='Lorentz λ=6', color='#984ea3', linewidth=1.2, linestyle='--')

    ax.set_xlabel('n / M')
    ax.set_ylabel('Kernel weight g_n')
    ax.set_title(f'Kernel Damping Profiles (M={M})')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.05)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, 'kernel_profiles.png'))
    plt.close(fig)
    print("  ✓ kernel_profiles.png")


# ===========================================================================
# Figure 6: Alpha vs Lambda (from P4)
# ===========================================================================

def plot_alpha_vs_lambda():
    """α vs λ from Lorentz λ scan."""
    ensure_output_dir()

    # Read P4 data or analyze from scan
    p4_path = os.path.join(DATA_DIR, 'P4_lorentz_lambda_scan.csv')
    if not os.path.exists(p4_path):
        print("  ⚠ P4_lorentz_lambda_scan.csv not found, skipping alpha_vs_lambda")
        return

    df = pd.read_csv(p4_path)

    lambda_vals = sorted(df['lambda'].unique())
    alphas = []
    rms_4096 = []

    for lam in lambda_vals:
        subset = df[df['lambda'] == lam]
        M_groups = subset.groupby('M')['abs_err'].apply(
            lambda x: np.sqrt(np.mean(np.square(x.astype(float)))))
        M_vals = np.array(list(M_groups.index), dtype=float)
        rms_vals = np.array(list(M_groups.values), dtype=float)

        valid = (rms_vals > 0) & (~np.isnan(rms_vals))
        M_v = M_vals[valid]
        rms_v = rms_vals[valid]

        if len(M_v) >= 4:
            x = np.log10(M_v)
            y = np.log10(rms_v)
            coeffs = np.polyfit(x, y, 1)
            alphas.append(coeffs[0])
        else:
            alphas.append(np.nan)

        idx_4096 = np.argmin(np.abs(M_v - 4096))
        rms_4096.append(float(rms_v[idx_4096]))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.plot(lambda_vals, alphas, 'o-', color='#377eb8', markersize=6, linewidth=1.5)
    ax1.axhline(y=2.0, color='gray', linestyle=':', alpha=0.5, label='α=2 (random walk)')
    ax1.axhline(y=0.1, color='red', linestyle='--', alpha=0.4, label='α=0.1 (goal)')
    ax1.set_xlabel('Lorentz λ')
    ax1.set_ylabel('Scaling exponent α')
    ax1.set_title('α vs λ (Lorentz kernel)')
    ax1.legend(fontsize=7)
    ax1.grid(True, alpha=0.3)

    ax2.plot(lambda_vals, rms_4096, 's-', color='#e41a1c', markersize=6, linewidth=1.5)
    ax2.set_xlabel('Lorentz λ')
    ax2.set_ylabel('RMS at M=4096')
    ax2.set_title('RMS(4096) vs λ')
    ax2.set_yscale('log')
    ax2.grid(True, alpha=0.3)

    fig.suptitle('Lorentz λ Scan: No Convergence Improvement', fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, 'P4_alpha_vs_lambda.png'))
    plt.close(fig)
    print("  ✓ P4_alpha_vs_lambda.png")


# ===========================================================================
# Figure 7: Comprehensive ranking bar chart
# ===========================================================================

def plot_ranking_bar():
    """Horizontal bar chart of convergence ranking."""
    ranking_path = os.path.join(DATA_DIR, 'kernel_ranking.json')
    if not os.path.exists(ranking_path):
        # Build from scratch
        build_ranking_from_data()

    with open(ranking_path) as f:
        ranking = json.load(f)

    entries = ranking.get('entries', [])
    if not entries:
        print("  ⚠ No ranking entries, skipping ranking_bar")
        return

    ensure_output_dir()

    labels = [f"{e['kernel']}+{e['method']}" for e in entries]
    rms_vals = [e['rms_4096'] for e in entries]
    colors = [COLORS.get(e['kernel'].split('(')[0], '#999999') for e in entries]

    fig, ax = plt.subplots(figsize=(8, 5))
    y_pos = range(len(labels))
    bars = ax.barh(y_pos, rms_vals, color=colors, edgecolor='white', height=0.6)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel('RMS error at M=4096')
    ax.set_title('Convergence Ranking (lower = better)')
    ax.set_xscale('log')
    ax.grid(True, alpha=0.3, axis='x')

    # Annotate values
    for i, (bar, val) in enumerate(zip(bars, rms_vals)):
        ax.text(val * 1.05, bar.get_y() + bar.get_height()/2,
                f'{val:.2e}', va='center', fontsize=6)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, 'P_comprehensive_ranking.png'))
    plt.close(fig)
    print("  ✓ P_comprehensive_ranking.png")


def build_ranking_from_data():
    """Build ranking.json from available data if not already present."""
    entries = []

    # From T4 scan_results.csv
    df_path = os.path.join(DATA_DIR, 'scan_results.csv')
    if os.path.exists(df_path):
        df = pd.read_csv(df_path)
        for kernel in ['clean', 'jackson', 'lorentz']:
            for method in ['sequential', 'kahan']:
                mask = (df['mu_kernel'] == kernel) & (df['method'] == method) & (df['M'] == 4096)
                subset = df[mask]
                if len(subset) > 0:
                    rms = float(np.sqrt(np.mean(
                        np.square(subset['abs_err'].astype(float)))))
                    entries.append({
                        'kernel': kernel, 'method': method,
                        'rms_4096': rms, 'source': 'T4'
                    })

    # From P4 lorentz lambda scan
    p4_path = os.path.join(DATA_DIR, 'P4_lorentz_lambda_scan.csv')
    if os.path.exists(p4_path):
        df = pd.read_csv(p4_path)
        for lam in sorted(df['lambda'].unique()):
            mask = (df['lambda'] == lam) & (df['M'] == 4096)
            subset = df[mask]
            if len(subset) > 0:
                rms = float(np.sqrt(np.mean(
                    np.square(subset['abs_err'].astype(float)))))
                entries.append({
                    'kernel': f'lorentz(λ={lam:.0f})', 'method': 'sequential',
                    'rms_4096': rms, 'source': 'P4'
                })

    entries.sort(key=lambda x: x['rms_4096'])
    ranking_data = {
        'entries': entries,
        'best': entries[0] if entries else None,
    }
    with open(os.path.join(DATA_DIR, 'kernel_ranking.json'), 'w') as f:
        json.dump(ranking_data, f, indent=2)
    return ranking_data


# ===========================================================================
# Figure 8: Comprehensive 4-panel summary
# ===========================================================================

def plot_comprehensive_summary():
    """4-panel comprehensive summary figure."""
    ensure_output_dir()
    fig, axes = plt.subplots(2, 2, figsize=(11, 9))

    # Panel 1: Error vs M (from T4)
    ax = axes[0, 0]
    df_path = os.path.join(DATA_DIR, 'scan_results.csv')
    if os.path.exists(df_path):
        df = pd.read_csv(df_path)
        for kernel in ['clean', 'jackson', 'lorentz']:
            mask = (df['mu_kernel'] == kernel) & (df['method'] == 'sequential')
            subset = df[mask]
            M_groups = subset.groupby('M')['abs_err'].apply(
                lambda x: np.sqrt(np.mean(np.square(x.astype(float)))))
            M_vals = np.array(list(M_groups.index), dtype=float)
            rms_vals = np.array(list(M_groups.values), dtype=float)
            valid = (rms_vals > 0) & (~np.isnan(rms_vals))
            ax.loglog(M_vals[valid], rms_vals[valid],
                      color=COLORS[kernel], marker=MARKERS[kernel],
                      markersize=4, linewidth=1.2, label=kernel, alpha=0.85)
        ax.set_xlabel('M')
        ax.set_ylabel('RMS error')
        ax.set_title('(a) Error vs M (sequential)')
        ax.legend(fontsize=7)
        ax.grid(True, alpha=0.3, which='both')

    # Panel 2: Kernel profiles
    ax = axes[0, 1]
    from mu_matrix import jackson_kernel_vector, lorentz_kernel_vector
    M_kern = 256
    n = np.arange(M_kern)
    ax.plot(n/M_kern, jackson_kernel_vector(M_kern), label='Jackson', color=COLORS['jackson'])
    ax.plot(n/M_kern, lorentz_kernel_vector(M_kern, 4.0), label='Lorentz λ=4', color=COLORS['lorentz'])
    ax.set_xlabel('n / M')
    ax.set_ylabel('g_n')
    ax.set_title('(b) Kernel Damping Profiles')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 3: Alpha vs Lambda (if P4 data exists)
    ax = axes[1, 0]
    p4_path = os.path.join(DATA_DIR, 'P4_lorentz_lambda_scan.csv')
    if os.path.exists(p4_path):
        df_p4 = pd.read_csv(p4_path)
        lambda_vals = sorted(df_p4['lambda'].unique())
        alphas = []
        for lam in lambda_vals:
            sub = df_p4[df_p4['lambda'] == lam]
            Mg = sub.groupby('M')['abs_err'].apply(
                lambda x: np.sqrt(np.mean(np.square(x.astype(float)))))
            Mv = np.array(list(Mg.index), dtype=float)
            rv = np.array(list(Mg.values), dtype=float)
            v = (rv > 0) & (~np.isnan(rv))
            if sum(v) >= 4:
                c = np.polyfit(np.log10(Mv[v]), np.log10(rv[v]), 1)
                alphas.append(c[0])
            else:
                alphas.append(np.nan)
        ax.plot(lambda_vals, alphas, 'o-', color='#377eb8', markersize=6)
        ax.axhline(y=2.0, color='gray', linestyle=':', alpha=0.5)
        ax.set_xlabel('Lorentz λ')
        ax.set_ylabel('α')
        ax.set_title('(c) α vs λ (Lorentz)')
        ax.grid(True, alpha=0.3)
    else:
        ax.text(0.5, 0.5, 'P4 data not available', transform=ax.transAxes,
                ha='center', va='center', fontsize=10)
        ax.set_title('(c) α vs λ')

    # Panel 4: Ranking
    ax = axes[1, 1]
    ranking_path = os.path.join(DATA_DIR, 'kernel_ranking.json')
    if not os.path.exists(ranking_path):
        build_ranking_from_data()
    if os.path.exists(ranking_path):
        with open(ranking_path) as f:
            ranking = json.load(f)
        entries = ranking.get('entries', [])
        # Top 8
        entries = entries[:8]
        labels = [f"{e['kernel']}+{e['method']}" for e in entries]
        rms_vals = [e['rms_4096'] for e in entries]
        colors_bar = [COLORS.get(e['kernel'].split('(')[0], '#999999') for e in entries]
        y_pos = range(len(labels))
        ax.barh(y_pos, rms_vals, color=colors_bar, edgecolor='white', height=0.6)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels, fontsize=6)
        ax.invert_yaxis()
        ax.set_xlabel('RMS at M=4096')
        ax.set_title('(d) Convergence Ranking')
        ax.set_xscale('log')
        ax.grid(True, alpha=0.3, axis='x')
    else:
        ax.text(0.5, 0.5, 'Ranking data not available', transform=ax.transAxes,
                ha='center', va='center')

    fig.suptitle('Γ-μ Random Walk Simulation: Comprehensive Summary', fontsize=13, fontweight='bold')
    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, 'comprehensive_summary.png'))
    plt.close(fig)
    print("  ✓ comprehensive_summary.png")


# ===========================================================================
# Main
# ===========================================================================

def main():
    """Generate all figures."""
    print("Generating figures...")
    ensure_output_dir()

    # Read common data
    df_path = os.path.join(DATA_DIR, 'scan_results.csv')
    df = pd.read_csv(df_path) if os.path.exists(df_path) else None

    if df is None:
        print("ERROR: scan_results.csv not found. Run T4 first.")
        return

    plot_error_vs_M(df)
    plot_scaling_law(df)
    plot_gamma_heatmap(M=64)
    plot_mu_heatmap(M=64)
    plot_kernel_profiles(M=256)
    plot_alpha_vs_lambda()
    plot_ranking_bar()
    plot_comprehensive_summary()

    print(f"\nAll figures saved to {OUTPUT_DIR}/")


if __name__ == '__main__':
    main()
