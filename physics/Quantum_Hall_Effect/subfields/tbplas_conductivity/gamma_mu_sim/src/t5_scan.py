#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-28 00:18:04
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-28 00:18:06
#FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/src/t5_scan.py
#Description  :

#!/usr/bin/env python3
"""
T5: Kernel Model Comparison — Lorentz λ scan + 3-kernel convergence ranking.

Plan reference: docs/plan.md §8.3

Steps:
  P1–P3: Analyze existing T4 data for 3-kernel convergence ranking
  P4: Lorentz λ scan (λ=2,3,4,6,8), M=64→4096, sequential, 5 trials
"""

import sys, os, time, math, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import numpy as np
import pandas as pd

from gamma_matrix import gamma_matrix_full
from mu_matrix import mu_matrix_generate

# ===========================================================================
# Fast summation (same as t4_scan.py)
# ===========================================================================

def sum_sequential_fast(gamma: np.ndarray, mu: np.ndarray) -> float:
    prod = np.real(gamma).ravel() * mu.ravel()
    total = 0.0
    for v in prod:
        total += v
    return float(total)


def compute_S_ref(gamma: np.ndarray, mu_true: np.ndarray) -> float:
    prod = np.real(gamma).ravel() * mu_true.ravel()
    return math.fsum(prod.tolist())


# ===========================================================================
# P1–P3: Analyze T4 data for 3-kernel ranking
# ===========================================================================

def analyze_t4_data():
    """Extract convergence metrics from T4 scan_results.csv."""
    df = pd.read_csv('output/data/scan_results.csv')

    print("=" * 70)
    print("P1–P3: Three-Kernel Convergence Analysis (from T4 data)")
    print("=" * 70)

    results = {}
    for kernel in ['clean', 'jackson', 'lorentz']:
        mask = (df['mu_kernel'] == kernel) & (df['method'] == 'sequential')
        subset = df[mask]

        # RMS per M
        M_groups = subset.groupby('M')['abs_err'].apply(
            lambda x: np.sqrt(np.mean(np.square(x.astype(float)))))
        M_vals = np.array(list(M_groups.index), dtype=float)
        rms_vals = np.array(list(M_groups.values), dtype=float)

        valid = (rms_vals > 0) & (~np.isnan(rms_vals)) & (M_vals <= 4096)
        M_v = M_vals[valid]
        rms_v = rms_vals[valid]

        # Scaling fit
        if len(M_v) >= 4:
            x = np.log10(M_v)
            y = np.log10(rms_v)
            coeffs = np.polyfit(x, y, 1)
            alpha, beta = coeffs[0], coeffs[1]
            y_pred = alpha * x + beta
            ss_res = np.sum((y - y_pred) ** 2)
            ss_tot = np.sum((y - np.mean(y)) ** 2)
            R2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
        else:
            alpha, beta, R2 = np.nan, np.nan, np.nan

        # RMS at key M values
        rms_at_M = {}
        for target_M in [1024, 2048, 4096]:
            idx = np.argmin(np.abs(M_v - target_M))
            rms_at_M[f"M{target_M}"] = float(rms_v[idx])

        results[kernel] = {
            'alpha': float(alpha), 'beta': float(beta), 'R2': float(R2),
            'rms_M1024': rms_at_M['M1024'],
            'rms_M2048': rms_at_M['M2048'],
            'rms_M4096': rms_at_M['M4096'],
        }

        print(f"\n  [{kernel}]")
        print(f"    α = {alpha:.4f}, β = {beta:.4f}, R² = {R2:.6f}")
        print(f"    RMS(M=1024) = {rms_at_M['M1024']:.3e}")
        print(f"    RMS(M=2048) = {rms_at_M['M2048']:.3e}")
        print(f"    RMS(M=4096) = {rms_at_M['M4096']:.3e}")

    # Ranking by RMS at M=4096
    ranking = sorted(results.items(), key=lambda x: x[1]['rms_M4096'])
    print(f"\n  Convergence ranking (by RMS at M=4096, low→high):")
    for rank, (kernel, info) in enumerate(ranking, 1):
        print(f"    {rank}. {kernel}: RMS={info['rms_M4096']:.3e}")

    # Also check Kahan
    print(f"\n  --- Kahan vs Sequential comparison at M=4096 ---")
    for kernel in ['clean', 'jackson', 'lorentz']:
        for method in ['sequential', 'kahan']:
            mask = (df['mu_kernel'] == kernel) & (df['method'] == method) & (df['M'] == 4096)
            subset = df[mask]
            if len(subset) > 0:
                rms = np.sqrt(np.mean(np.square(subset['abs_err'].astype(float))))
                print(f"    {kernel:8s} + {method:10s}: RMS={rms:.3e}")

    return results, ranking


# ===========================================================================
# P4: Lorentz λ scan
# ===========================================================================

def run_lorentz_lambda_scan():
    """Scan Lorentz λ parameter."""
    print("\n" + "=" * 70)
    print("P4: Lorentz λ Scan")
    print("=" * 70)

    theta = np.pi / 4
    M_list = [64, 128, 256, 384, 512, 768, 1024, 2048, 3072, 4096]
    lambda_list = [2.0, 3.0, 4.0, 6.0, 8.0]
    n_trials = 5
    noise_level = 2.2e-16

    rows = []
    total = len(M_list) * len(lambda_list) * n_trials
    count = 0
    t_start = time.time()

    for M in M_list:
        print(f"\n  M={M} ...", end=" ", flush=True)
        t_m = time.time()

        # Generate Γ once per M (deterministic)
        gamma = gamma_matrix_full(M, theta)

        for lam in lambda_list:
            for trial in range(n_trials):
                count += 1
                seed = trial * 10000 + M * 10 + int(lam * 10)
                mu_true, mu_noisy = mu_matrix_generate(
                    M, kernel='lorentz', E0=0.0, lorentz_lambda=lam,
                    noise_level=noise_level, seed=seed)

                S_ref = compute_S_ref(gamma, mu_true)
                S_approx = sum_sequential_fast(gamma, mu_noisy)
                abs_err = abs(S_approx - S_ref)
                rel_err = abs_err / max(abs(S_ref), 1e-300)

                rows.append({
                    'M': M,
                    'lambda': lam,
                    'trial': trial,
                    'S_approx': S_approx,
                    'S_ref': S_ref,
                    'abs_err': abs_err,
                    'rel_err': rel_err,
                    'N_terms': M * M,
                })

        dt = time.time() - t_m
        progress = count / total * 100
        print(f"done ({dt:.1f}s, {progress:.0f}%)", flush=True)

    df = pd.DataFrame(rows)
    df.to_csv('output/data/P4_lorentz_lambda_scan.csv', index=False)

    dt_total = time.time() - t_start
    print(f"\n  Total: {len(df)} rows, {dt_total:.1f}s")
    print(f"  Saved to output/data/P4_lorentz_lambda_scan.csv")

    return df


# ===========================================================================
# Analyze λ scan results
# ===========================================================================

def analyze_lambda_scan(df):
    """Compute α(λ) for each λ value."""
    print("\n" + "=" * 70)
    print("P4 Analysis: α vs λ")
    print("=" * 70)

    lambda_results = {}
    for lam in sorted(df['lambda'].unique()):
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
            alpha, beta = coeffs[0], coeffs[1]
            y_pred = alpha * x + beta
            ss_res = np.sum((y - y_pred) ** 2)
            ss_tot = np.sum((y - np.mean(y)) ** 2)
            R2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
        else:
            alpha, beta, R2 = np.nan, np.nan, np.nan

        lambda_results[lam] = {'alpha': float(alpha), 'beta': float(beta), 'R2': float(R2)}

        # RMS at M=4096
        idx_4096 = np.argmin(np.abs(M_v - 4096))
        rms_4096 = float(rms_v[idx_4096])
        lambda_results[lam]['rms_M4096'] = rms_4096

        print(f"  λ={lam:.1f}: α={alpha:.4f}, R²={R2:.6f}, RMS(M=4096)={rms_4096:.3e}")

    # Check if α(λ) decreases with λ
    if len(lambda_results) >= 2:
        lams = sorted(lambda_results.keys())
        alphas = [lambda_results[l]['alpha'] for l in lams]
        print(f"\n  α(λ) trend: {'monotonically decreasing ✓' if all(alphas[i] > alphas[i+1] for i in range(len(alphas)-1)) else 'NOT monotonic'}")

    # Sweet-spot λ where α < 0.1
    sweet_spot = None
    for lam in sorted(lambda_results.keys()):
        if lambda_results[lam]['alpha'] < 0.1:
            sweet_spot = lam
            break
    if sweet_spot:
        print(f"  Sweet-spot λ (α<0.1): λ ≥ {sweet_spot:.1f}")
    else:
        print(f"  Sweet-spot λ: none found in scanned range (all α ≥ 0.1)")

    return lambda_results


# ===========================================================================
# Comprehensive ranking
# ===========================================================================

def comprehensive_ranking(t4_results, lambda_results):
    """Build comprehensive kernel × method ranking table."""
    print("\n" + "=" * 70)
    print("Comprehensive Ranking (by RMS at M=4096)")
    print("=" * 70)

    # Build ranking entries
    entries = []

    # From T4: clean/jackson/lorentz × sequential/kahan
    for kernel, info in t4_results.items():
        entries.append({
            'kernel': kernel, 'method': 'sequential',
            'alpha': info['alpha'], 'rms_4096': info['rms_M4096'],
            'source': 'T4'
        })
        # Kahan data from original scaling_fit.json
        # We'll approximate from the same data

    # From P4: lorentz × various λ
    for lam, info in lambda_results.items():
        entries.append({
            'kernel': f'lorentz(λ={lam:.0f})', 'method': 'sequential',
            'alpha': info['alpha'], 'rms_4096': info.get('rms_M4096', np.nan),
            'source': 'P4'
        })

    # Also compute Kahan entries from T4 scan_results.csv
    df = pd.read_csv('output/data/scan_results.csv')
    for kernel in ['clean', 'jackson', 'lorentz']:
        mask = (df['mu_kernel'] == kernel) & (df['method'] == 'kahan') & (df['M'] == 4096)
        subset = df[mask]
        if len(subset) > 0:
            rms = np.sqrt(np.mean(np.square(subset['abs_err'].astype(float))))
            # Get alpha from scaling_fit.json
            with open('output/data/scaling_fit.json') as f:
                sf = json.load(f)
            key = f"{kernel}_kahan"
            alpha_k = sf.get(key, {}).get('alpha', np.nan)
            entries.append({
                'kernel': kernel, 'method': 'kahan',
                'alpha': alpha_k, 'rms_4096': rms,
                'source': 'T4'
            })

    # Sort by RMS at M=4096
    entries.sort(key=lambda x: x['rms_4096'] if not np.isnan(x['rms_4096']) else float('inf'))

    print(f"\n  {'Rank':<5} {'Kernel':<20} {'Method':<12} {'α':<8} {'RMS(M=4096)':<14} {'Source'}")
    print(f"  {'-'*65}")
    for i, e in enumerate(entries, 1):
        rms_str = f"{e['rms_4096']:.3e}" if not np.isnan(e['rms_4096']) else "N/A"
        print(f"  {i:<5} {e['kernel']:<20} {e['method']:<12} {e['alpha']:<8.4f} {rms_str:<14} {e['source']}")

    # Save ranking
    ranking_data = {
        'entries': entries,
        'best': entries[0] if entries else None,
        'recommendation': (
            f"Best: {entries[0]['kernel']}+{entries[0]['method']} "
            f"(RMS={entries[0]['rms_4096']:.3e} at M=4096)"
            if entries else "N/A"
        ),
    }
    with open('output/data/kernel_ranking.json', 'w') as f:
        json.dump(ranking_data, f, indent=2, default=str)
    print(f"\n  Ranking saved to output/data/kernel_ranking.json")

    return ranking_data


# ===========================================================================
# Main
# ===========================================================================

def main():
    os.makedirs('output/data', exist_ok=True)

    # P1–P3: Analyze existing T4 data
    t4_results, ranking = analyze_t4_data()

    # P4: Lorentz λ scan
    df_lambda = run_lorentz_lambda_scan()
    lambda_results = analyze_lambda_scan(df_lambda)

    # Comprehensive ranking
    comp_ranking = comprehensive_ranking(t4_results, lambda_results)

    # Final verdict
    print("\n" + "=" * 70)
    print("T5 VERDICT")
    print("=" * 70)

    # P3 check: Lorentz λ=4: RMS(M=8192) < RMS(M=4096)?
    df_t4 = pd.read_csv('output/data/scan_results.csv')
    lorentz_seq_4096 = df_t4[(df_t4['mu_kernel']=='lorentz') & (df_t4['method']=='sequential') & (df_t4['M']==4096)]
    lorentz_seq_8192 = df_t4[(df_t4['mu_kernel']=='lorentz') & (df_t4['method']=='sequential') & (df_t4['M']==8192)]
    if len(lorentz_seq_4096) > 0 and len(lorentz_seq_8192) > 0:
        rms_4096 = np.sqrt(np.mean(np.square(lorentz_seq_4096['abs_err'].astype(float))))
        rms_8192 = np.sqrt(np.mean(np.square(lorentz_seq_8192['abs_err'].astype(float))))
        print(f"  P3: Lorentz λ=4 RMS(M=8192)={rms_8192:.3e} vs RMS(M=4096)={rms_4096:.3e}")
        if rms_8192 < rms_4096:
            print(f"  P3: ✓ RMS decreases with M (convergent)")
        else:
            print(f"  P3: ✗ RMS increases with M (divergent — random walk dominates)")

    print(f"\n  Best kernel+method: {comp_ranking.get('recommendation', 'N/A')}")
    print(f"  Lorentz+Kahan ranking: see ranking table above")


if __name__ == '__main__':
    main()
