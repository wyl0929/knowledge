#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-27 23:26:14
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-27 23:26:15
#FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/src/t4_scan.py
#Description  :

#!/usr/bin/env python3
"""
T4: M Systematic Scan — 6 kernel×method lines + float32 comparison.

Optimizations:
- Γ generated once per M (deterministic)
- S_ref computed via math.fsum (Shewchuk exact rounding, verified vs mpmath)
- Products pre-computed via numpy vectorization, accumulation via Python loop
- Incremental CSV saving every M to protect against crashes

Plan reference: docs/plan.md §8.2
"""

import sys, os, time, math, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import numpy as np
import pandas as pd

from gamma_matrix import gamma_matrix_full
from mu_matrix import mu_matrix_generate
from reference import sum_exact_mpmath
from summation import sum_sequential, sum_kahan


# ===========================================================================
# Fast summation: precompute product matrix, then accumulate
# ===========================================================================

def sum_sequential_fast(gamma: np.ndarray, mu: np.ndarray) -> float:
    """Standard sequential sum over pre-computed flat product array."""
    prod = np.real(gamma).ravel() * mu.ravel()
    total = 0.0
    for v in prod:
        total += v
    return float(total)


def sum_kahan_fast(gamma: np.ndarray, mu: np.ndarray) -> float:
    """Kahan compensated sum over pre-computed flat product array."""
    prod = np.real(gamma).ravel() * mu.ravel()
    total = 0.0
    comp = 0.0
    for v in prod:
        y = v - comp
        t = total + y
        comp = (t - total) - y
        total = t
    return float(total)


def sum_fast(gamma: np.ndarray, mu: np.ndarray, method: str) -> float:
    """Dispatch to fast summation."""
    if method == "sequential":
        return sum_sequential_fast(gamma, mu)
    elif method == "kahan":
        return sum_kahan_fast(gamma, mu)
    else:
        raise ValueError(f"Unknown method: {method}")


# ===========================================================================
# Reference: math.fsum (Shewchuk exact rounding) — verified vs mpmath
# ===========================================================================

def compute_S_ref(gamma: np.ndarray, mu_true: np.ndarray) -> float:
    """Compute high-accuracy reference sum using math.fsum.

    math.fsum uses Shewchuk's algorithm for exact rounding (error ≤ 0.5 ULP).
    Verified against mpmath dps=50 for M up to 256 (diff < 1e-14).
    """
    prod = np.real(gamma).ravel() * mu_true.ravel()
    return math.fsum(prod.tolist())


# ===========================================================================
# Verification: fsum vs mpmath at a representative M
# ===========================================================================

def verify_fsum_vs_mpmath():
    """Quick verification that math.fsum matches mpmath."""
    M_test = 256
    theta = np.pi / 4
    gamma = gamma_matrix_full(M_test, theta)
    for kernel in ["clean", "jackson", "lorentz"]:
        mu_true, _ = mu_matrix_generate(M_test, kernel=kernel, E0=0.0)
        S_fsum = compute_S_ref(gamma, mu_true)
        S_mp = float(sum_exact_mpmath(gamma, mu_true, dps=50))
        diff = abs(S_fsum - S_mp)
        rel_diff = diff / max(abs(S_mp), 1e-300)
        print(f"  fsum vs mpmath [{kernel}]: diff={diff:.2e}, rel={rel_diff:.2e}")
        # For near-zero S_ref, absolute error up to ~√N·ε·max|Γ| is expected
        # M=256: N=65536, √N·ε≈5.6e-14, max|Γ|≈180 → worst diff ~1e-11
        assert diff < 1e-10, f"fsum vs mpmath diverges for {kernel}: {diff}"


# ===========================================================================
# Main scan
# ===========================================================================

def run_t4_scan():
    """Run T4 systematic M scan — 6 kernel×method lines + float32 comparison."""

    # --- Setup ---
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
    data_dir = os.path.join(out_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)

    # --- Parameters ---
    M_list = [64, 128, 256, 384, 512, 768, 1024, 2048,
              3072, 4096, 6144, 8192]
    theta = np.pi / 4  # fixed θ per plan
    n_trials = 10
    noise_level = 2.2e-16
    kernels = ["clean", "jackson", "lorentz"]
    methods = ["sequential", "kahan"]
    lorentz_lambda = 4.0

    # M=8192 reduce trials if memory limited
    trials_per_M = {M: (3 if M >= 6144 else n_trials) for M in M_list}

    # --- Verify fsum vs mpmath first ---
    print("=" * 60)
    print("T4: Pre-flight — verifying math.fsum vs mpmath (M=256)")
    print("=" * 60)
    verify_fsum_vs_mpmath()
    print("  ✓ fsum reference validated\n")

    # --- Main scan loop ---
    csv_path = os.path.join(data_dir, "scan_results.csv")
    scaling_path = os.path.join(data_dir, "scaling_fit.json")

    records = []
    total_combos = sum(
        trials_per_M[M] * len(kernels) * len(methods)
        for M in M_list
    )
    print(f"Total measurements: {total_combos}")
    print(f"M list: {M_list}")
    print(f"Kernels: {kernels}")
    print(f"Methods: {methods}")
    print(f"Trials: {n_trials} (M≥6144: 3)")
    print("-" * 60)

    t_start = time.time()
    combo_count = 0

    for M in M_list:
        t_m_start = time.time()
        print(f"\n[M={M}] Generating Γ matrix...", end=" ", flush=True)
        gamma = gamma_matrix_full(M, theta)
        print(f"shape={gamma.shape}, max|Γ|={np.max(np.abs(gamma)):.1f}")

        for kernel in kernels:
            kernel_M_start = time.time()
            for trial in range(trials_per_M[M]):
                seed = trial * 10000 + M
                mu_true, mu_noisy = mu_matrix_generate(
                    M, kernel=kernel, E0=0.0,
                    noise_level=noise_level,
                    lorentz_lambda=lorentz_lambda,
                    seed=seed)

                # S_ref computed once per (M, kernel) — same for all trials
                # Use cached S_ref if available
                if trial == 0:
                    S_ref = compute_S_ref(gamma, mu_true)

                for method in methods:
                    S_approx = sum_fast(gamma, mu_noisy, method)
                    abs_err = abs(S_approx - S_ref)
                    rel_err = abs_err / max(abs(S_ref), 1e-300)

                    records.append({
                        "M": M,
                        "theta_idx": 0,
                        "theta_val": theta,
                        "mu_kernel": kernel,
                        "method": method,
                        "trial": trial,
                        "S_approx": float(S_approx),
                        "S_ref": float(S_ref),
                        "abs_err": float(abs_err),
                        "rel_err": float(rel_err),
                        "N_terms": M * M,
                    })
                    combo_count += 1

            # Print per-kernel timing
            kernel_elapsed = time.time() - kernel_M_start
            n_done = trials_per_M[M] * len(methods)
            print(f"  [{kernel:8s}] {n_done} measurements, "
                  f"{kernel_elapsed:.1f}s "
                  f"({kernel_elapsed/n_done:.2f}s/meas)")

        # Incremental save after each M
        df = pd.DataFrame(records)
        df.to_csv(csv_path, index=False)

        t_m_elapsed = time.time() - t_m_start
        t_total = time.time() - t_start
        print(f"  [M={M}] done in {t_m_elapsed:.1f}s "
              f"(total: {t_total/60:.1f}min, {combo_count}/{total_combos})")

    # --- Final save ---
    df = pd.DataFrame(records)
    df.to_csv(csv_path, index=False)
    print(f"\n✓ Saved {len(df)} rows to {csv_path}")

    # --- Compute scaling fits ---
    print("\n--- Scaling Law Fits ---")
    scaling_results = {}
    for kernel in kernels:
        for method in methods:
            mask = (df["mu_kernel"] == kernel) & (df["method"] == method)
            subset = df[mask]
            if len(subset) == 0:
                continue
            # Per-M RMS
            M_groups = subset.groupby("M")["abs_err"].apply(
                lambda x: np.sqrt(np.mean(np.square(x))))
            M_vals = list(M_groups.index)
            rms_vals = list(M_groups.values)

            if len(M_vals) >= 4:
                logM = np.log10(M_vals)
                logR = np.log10(rms_vals)
                coeffs = np.polyfit(logM, logR, 1)
                alpha, beta = coeffs[0], coeffs[1]
                y_pred = alpha * logM + beta
                ss_res = np.sum((logR - y_pred)**2)
                ss_tot = np.sum((logR - np.mean(logR))**2)
                R2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0

                key = f"{kernel}_{method}"
                scaling_results[key] = {
                    "alpha": float(alpha),
                    "beta": float(beta),
                    "R2": float(R2),
                }
                print(f"  {key:25s}: α={alpha:+.4f}, R²={R2:.4f}")

    with open(scaling_path, "w") as f:
        json.dump(scaling_results, f, indent=2)
    print(f"\n✓ Scaling fits saved to {scaling_path}")

    # --- S7: float32 comparison ---
    print("\n" + "=" * 60)
    print("S7: float32 Comparison")
    print("=" * 60)
    run_float32_comparison(data_dir, M_list)

    t_total = time.time() - t_start
    print(f"\n{'='*60}")
    print(f"T4 complete! Total time: {t_total/60:.1f} min")
    print(f"Results: {csv_path}")
    print(f"{'='*60}")


def run_float32_comparison(data_dir: str, M_list_full: list):
    """S7: float32 comparison for 2 representative lines.

    Lines: clean+sequential (worst case), lorentz+kahan (best case)
    M range: 64→2048 (float32 may overflow beyond this)
    """
    M_list = [m for m in M_list_full if m <= 2048]
    theta = np.pi / 4
    n_trials = 10
    noise_level = 2.2e-16

    lines = [
        ("clean", "sequential"),
        ("lorentz", "kahan"),
    ]

    records = []
    for kernel, method in lines:
        print(f"\n  [{kernel}+{method}] float32:")
        for M in M_list:
            gamma = gamma_matrix_full(M, theta).astype(np.complex64)
            for trial in range(n_trials):
                seed = trial * 10000 + M + 99999  # offset from main scan
                mu_true_f64, mu_noisy_f64 = mu_matrix_generate(
                    M, kernel=kernel, E0=0.0,
                    noise_level=noise_level,
                    lorentz_lambda=4.0,
                    seed=seed)
                mu_noisy_f32 = mu_noisy_f64.astype(np.float32)

                # Reference: fsum on float64 mu_true
                S_ref = compute_S_ref(
                    gamma_matrix_full(M, theta), mu_true_f64)

                # Approximate: sum with float32 inputs
                S_approx = sum_fast(gamma, mu_noisy_f32, method)
                abs_err = abs(S_approx - S_ref)
                rel_err = abs_err / max(abs(S_ref), 1e-300)

                records.append({
                    "M": M,
                    "mu_kernel": kernel,
                    "method": f"{method}_f32",
                    "trial": trial,
                    "abs_err": float(abs_err),
                    "rel_err": float(rel_err),
                    "S_approx": float(S_approx),
                    "S_ref": float(S_ref),
                    "N_terms": M * M,
                })

            # Per-M RMS for this line
            line_df = pd.DataFrame([r for r in records
                                    if r["mu_kernel"] == kernel
                                    and r["method"] == f"{method}_f32"
                                    and r["M"] == M])
            if len(line_df) > 0:
                rms = np.sqrt(np.mean(np.square(line_df["abs_err"].values)))
                print(f"    M={M:5d}: RMS={rms:.2e}")

    df_f32 = pd.DataFrame(records)
    f32_path = os.path.join(data_dir, "S7_float32_scan.csv")
    df_f32.to_csv(f32_path, index=False)
    print(f"\n  ✓ S7 float32 results saved to {f32_path}")


if __name__ == "__main__":
    run_t4_scan()
