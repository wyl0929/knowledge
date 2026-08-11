#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-23 20:12:36
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-23 20:12:38
#FilePath     : /MG/test/analyze_mM_grid.py
#Description  :

#coding=utf-8
"""
analyze_mM_grid.py — m×M 网格测试汇总分析

Read all Hall conductivity data from runs/0623/, extract baseline shift S,
produce summary tables and figures.

Usage:
    python test/analyze_mM_grid.py [RUNS_DIR]

    RUNS_DIR defaults to runs/0623

Output:
    - Terminal: full S_edge data table + scaling analysis
    - runs/0623/mM_grid_summary.png (optional)
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import glob

# ── Configuration ──
RUNS_DIR = sys.argv[1] if len(sys.argv) > 1 else "runs/0623"
PLOT = "--plot" in sys.argv


def extract_S(filepath, E_range=(-1.5, -1.4)):
    """Extract baseline shift S as mean sigma_xy in reference energy window."""
    try:
        data = np.loadtxt(filepath)
    except Exception:
        return None
    eng, sigma = data[:, 0], data[:, 1]
    mask = ~np.isnan(sigma)
    eng, sigma = eng[mask], sigma[mask]
    if len(sigma) == 0:
        return None
    mask_win = (eng >= E_range[0]) & (eng <= E_range[1])
    sigma_win = sigma[mask_win]
    if len(sigma_win) == 0:
        return None
    return float(np.mean(sigma_win))


def parse_filename(basename):
    """Extract m, M, source from filename like hall_AB_d0.000_m256_M1024_load_B100.0.txt"""
    parts = basename.replace(".txt", "").split("_")
    m_val = None
    M_val = None
    source = "unknown"
    for p in parts:
        if p.startswith("m") and p[1:].isdigit():
            m_val = int(p[1:])
        if p.startswith("M") and p[1:].isdigit():
            M_val = int(p[1:])
    if "load" in parts:
        source = "load"
    elif "cluster" in parts:
        source = "cluster"
    elif "local" in parts:
        source = "local"
    elif "save" in parts:
        source = "save"
    return m_val, M_val, source


# ── Collect data ──
all_files = sorted(glob.glob(os.path.join(RUNS_DIR, "hall_*.txt")))
results = {}  # {m: {M: S_edge}}

for f in all_files:
    m_val, M_val, source = parse_filename(os.path.basename(f))
    if m_val is None or M_val is None:
        continue
    S = extract_S(f)
    if S is None:
        continue
    if m_val not in results:
        results[m_val] = {}
    # Prefer cluster over local, local over load for m=512 duplicates
    if M_val in results[m_val]:
        old_source = results[m_val][M_val][1]
        priority = {"cluster": 3, "local": 2, "load": 1, "save": 0}
        if priority.get(source, 0) <= priority.get(old_source, 0):
            continue
    results[m_val][M_val] = (S, source)

# ── Summary Table ──
print("=" * 80)
print("m×M Grid — Baseline Shift S_edge (σ_xy at E≈-1.5 eV, units e²/h)")
print("=" * 80)

m_list = sorted(results.keys())
M_all = sorted(set(M for m in m_list for M in results[m]))

# Header
header = f"{'M':>6s}"
for m in m_list:
    header += f"  {'m='+str(m):>12s}"
print(header)
print("-" * (6 + 14 * len(m_list)))

for M in M_all:
    row = f"{M:6d}"
    for m in m_list:
        if M in results[m]:
            row += f"  {results[m][M][0]:12.4f}"
        else:
            row += f"  {'—':>12s}"
    print(row)

print("=" * 80)

# ── Scaling Analysis ──
print("\n## Low-M Scaling (M ≤ 1024): S/M, S/M², S/M³")
print(f"{'m':>6s} {'M':>6s} {'|S|':>12s} {'|S|/M':>12s} {'|S|/M²':>12s} {'|S|/M³':>12s}")
print("-" * 60)
for m in m_list:
    for M in sorted(results[m]):
        if M <= 1024:
            S = abs(results[m][M][0])
            print(f"{m:6d} {M:6d} {S:12.4f} {S/M:12.6f} {S/M**2:12.8f} {S/M**3:12.10f}")

print("\n## High-M Local Growth Exponent α = d ln|S| / d ln M")
print(f"{'m':>6s} {'M1→M2':>12s} {'|S1|':>10s} {'|S2|':>10s} {'α':>8s}")
print("-" * 50)
for m in m_list:
    Ms = sorted(results[m])
    for i in range(len(Ms) - 1):
        M1, M2 = Ms[i], Ms[i + 1]
        if M2 >= 2048:
            S1, S2 = abs(results[m][M1][0]), abs(results[m][M2][0])
            alpha = np.log(S2 / S1) / np.log(M2 / M1)
            print(f"{m:6d} {M1:4d}→{M2:<4d} {S1:10.3f} {S2:10.3f} {alpha:8.3f}")

# ── Cross-m Comparison ──
print("\n## Cross-m Ratio at Fixed M")
print(f"{'M':>6s}  {'S_512/S_256':>14s}  {'S_1024/S_256':>15s}  {'S_1024/S_512':>15s}")
print("-" * 58)
for M in M_all:
    vals = {}
    for m in m_list:
        if M in results[m]:
            vals[m] = abs(results[m][M][0])
    if len(vals) >= 2:
        r1 = f"{vals.get(512,0)/vals.get(256,1):.3f}" if (256 in vals and 512 in vals) else "—"
        r2 = f"{vals.get(1024,0)/vals.get(256,1):.3f}" if (256 in vals and 1024 in vals) else "—"
        r3 = f"{vals.get(1024,0)/vals.get(512,1):.3f}" if (512 in vals and 1024 in vals) else "—"
        print(f"{M:6d}  {r1:>14s}  {r2:>15s}  {r3:>15s}")

# ── H_η Falsification ──
print("\n## H_η Falsification Evidence")
N_orb_factor = 8  # rough: 8*m²
tests = [
    ("m=1024, M=1024 → η=8192", 1024, 1024, "S should be large", abs(results.get(1024, {}).get(1024, (0,))[0])),
    ("m=256, M=3072 → η=171", 256, 3072, "S should be ≈0", abs(results.get(256, {}).get(3072, (0,))[0])),
    ("m=512, M=2048 → η=1024", 512, 2048, "ref for comparison", abs(results.get(512, {}).get(2048, (0,))[0])),
    ("m=1024, M=4096 → η=2048", 1024, 4096, "S should be ~2× m512/M2048", abs(results.get(1024, {}).get(4096, (0,))[0])),
]
print(f"{'Test':<35s} {'Prediction':<25s} {'|S|':>10s}  Verdict")
print("-" * 85)
for label, m, M, pred, val in tests:
    verdict = "✓ consistent" if val < 50 else "✗ FALSIFIED"
    print(f"{label:<35s} {pred:<25s} {val:10.3f}  {verdict}")

# ── Optional Plot ──
if PLOT:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left: S vs M
    ax = axes[0]
    colors = {256: "#1f77b4", 512: "#ff7f0e", 1024: "#2ca02c"}
    for m in m_list:
        Ms = sorted(results[m])
        Ss = [abs(results[m][M][0]) for M in Ms]
        ax.loglog(Ms, Ss, "o-", color=colors.get(m, "gray"),
                  ms=6, lw=1.5, label=f"m={m}")
    ax.axvline(x=2560, color="red", ls="--", lw=1, alpha=0.5, label="$M_c \\approx 2560$")
    ax.set_xlabel("M (dckb_num_kernel)")
    ax.set_ylabel("|S| ($e^2/h$)")
    ax.set_title("Baseline Shift vs M")
    ax.legend()
    ax.grid(alpha=0.2)

    # Right: Local α vs M
    ax = axes[1]
    for m in m_list:
        Ms = sorted(results[m])
        alphas = []
        M_mid = []
        for i in range(len(Ms) - 1):
            M1, M2 = Ms[i], Ms[i + 1]
            S1, S2 = abs(results[m][M1][0]), abs(results[m][M2][0])
            a = np.log(S2 / S1) / np.log(M2 / M1)
            alphas.append(a)
            M_mid.append(np.sqrt(M1 * M2))
        ax.semilogx(M_mid, alphas, "o-", color=colors.get(m, "gray"),
                    ms=5, lw=1.2, label=f"m={m}")
    ax.axhline(y=2.0, color="gray", ls=":", lw=1, alpha=0.5, label="$\\alpha=2$ (M²)")
    ax.axhline(y=1.0, color="gray", ls="-.", lw=1, alpha=0.3, label="$\\alpha=1$ (linear)")
    ax.set_xlabel("M (geometric mean)")
    ax.set_ylabel("Local α = d ln|S| / d ln M")
    ax.set_title("Local Growth Exponent")
    ax.legend()
    ax.grid(alpha=0.2)

    fig.tight_layout()
    outpath = os.path.join(RUNS_DIR, "mM_grid_summary.png")
    fig.savefig(outpath, dpi=200)
    print(f"\nSaved summary figure to: {outpath}")
