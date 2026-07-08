#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-27 23:13:35
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-27 23:13:40
#FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/src/main.py
#Description  :

"""
main.py — M-scan pipeline entry point.

Plan reference: docs/plan.md §3.2, §4.5
"""

import os
import sys
import json
import signal
import argparse
import numpy as np
import pandas as pd

# Local imports (from same package)
from config import default_config, M_scan_grid
from gamma_matrix import gamma_matrix_full
from mu_matrix import mu_matrix_generate
from summation import sum_dispatch
from reference import sum_exact_mpmath
from analysis import fit_scaling_law, rms_error, convergence_diagnostic


# ---------------------------------------------------------------------------
# Single measurement
# ---------------------------------------------------------------------------

def run_single(gamma: np.ndarray, mu_noisy: np.ndarray,
               method: str, S_ref: float) -> dict:
    """Perform a single summation measurement.

    Parameters
    ----------
    gamma : np.ndarray
        (M, M) Γ matrix.
    mu_noisy : np.ndarray
        (M, M) noisy μ matrix.
    method : str
        "sequential" or "kahan".
    S_ref : float
        Ground-truth reference value.

    Returns
    -------
    dict
        {S_approx, abs_err, rel_err}
    """
    S_approx = sum_dispatch(gamma, mu_noisy, method)
    abs_err = abs(S_approx - S_ref)
    rel_err = abs_err / max(abs(S_ref), 1e-300)
    return {"S_approx": S_approx, "abs_err": abs_err, "rel_err": rel_err}


# ---------------------------------------------------------------------------
# M scan
# ---------------------------------------------------------------------------

def run_M_scan(cfg: dict) -> pd.DataFrame:
    """Run full M scan according to configuration.

    Parameters
    ----------
    cfg : dict
        Configuration dictionary (from default_config() or overridden).

    Returns
    -------
    pd.DataFrame
        scan_results with columns:
        M, theta_idx, theta_val, mu_kernel, method, trial,
        S_approx, S_ref, abs_err, rel_err, N_terms
    """
    M_list = cfg["M_list"]
    theta_vals = [t * np.pi for t in cfg["theta_grid"]]
    n_trials = cfg["n_trials"]
    noise_level = cfg["noise_level"]
    methods = cfg["summation_methods"]
    mu_kernel = cfg["mu_kernel"]
    lorentz_lambda = cfg["lorentz_lambda"]
    mu_E0 = cfg["mu_E0"]
    mpmath_dps = cfg["mpmath_dps"]

    records = []
    total_steps = len(M_list) * len(theta_vals) * n_trials * len(methods)
    step = 0

    # Try to import tqdm for progress bar
    try:
        from tqdm import tqdm
        pbar = tqdm(total=total_steps, desc="M-scan")
        use_tqdm = True
    except ImportError:
        use_tqdm = False
        pbar = None

    _interrupted = False

    def _sigint_handler(signum, frame):
        nonlocal _interrupted
        _interrupted = True
        print("\n[Interrupted] Saving collected data...")

    old_handler = signal.signal(signal.SIGINT, _sigint_handler)

    try:
        for M in M_list:
            for ti, theta in enumerate(theta_vals):
                # Generate Γ once per (M, θ) — deterministic
                gamma = gamma_matrix_full(M, theta)

                trials_done = 0
                for trial in range(n_trials):
                    if _interrupted:
                        break

                    # Generate μ with fresh noise seed per trial
                    seed = trial * 10000 + ti * 1000 + M
                    mu_true, mu_noisy = mu_matrix_generate(
                        M, kernel=mu_kernel, E0=mu_E0,
                        noise_level=noise_level,
                        lorentz_lambda=lorentz_lambda,
                        seed=seed)

                    # Compute mpmath reference once per (M, θ) trial
                    # (mpmath reference uses mu_true, not mu_noisy, since
                    #  we want to measure noise accumulation, not noise in μ)
                    S_ref = float(sum_exact_mpmath(gamma, mu_true, dps=mpmath_dps))

                    for method in methods:
                        result = run_single(gamma, mu_noisy, method, S_ref)
                        records.append({
                            "M": M,
                            "theta_idx": ti,
                            "theta_val": theta,
                            "mu_kernel": mu_kernel,
                            "method": method,
                            "trial": trial,
                            "S_approx": result["S_approx"],
                            "S_ref": S_ref,
                            "abs_err": result["abs_err"],
                            "rel_err": result["rel_err"],
                            "N_terms": M * M,
                        })
                        step += 1
                        if use_tqdm:
                            pbar.update(1)
                        else:
                            if step % max(1, total_steps // 20) == 0:
                                print(f"  [{step}/{total_steps}] M={M}, θ={theta:.3f}, "
                                      f"trial={trial}, method={method}")

                    trials_done += 1

                if _interrupted:
                    break
            if _interrupted:
                break
    finally:
        signal.signal(signal.SIGINT, old_handler)
        if use_tqdm and pbar:
            pbar.close()

    df = pd.DataFrame(records)
    return df


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Γ-μ random walk simulation — M-scan pipeline")
    parser.add_argument("--config", type=str, default=None,
                        help="JSON file to override default config")
    parser.add_argument("--M-list", type=str, default=None,
                        help="Comma-separated M list, e.g. '64,128,256'")
    parser.add_argument("--mu-kernel", type=str, default=None,
                        choices=["clean", "jackson", "lorentz"],
                        help="μ kernel model")
    parser.add_argument("--methods", type=str, default=None,
                        help="Comma-separated summation methods, e.g. 'sequential,kahan'")
    parser.add_argument("--n-trials", type=int, default=None,
                        help="Number of trials per (M,θ)")
    parser.add_argument("--theta-grid", type=str, default=None,
                        help="Comma-separated θ values in units of π")
    parser.add_argument("--output", type=str, default=None,
                        help="Output CSV path (default: output/data/scan_results.csv)")
    parser.add_argument("--noise-level", type=float, default=None,
                        help="Noise level ε")
    parser.add_argument("--mpmath-dps", type=int, default=None,
                        help="mpmath decimal places")
    parser.add_argument("--lorentz-lambda", type=float, default=None,
                        help="Lorentz kernel λ")
    parser.add_argument("--mu-E0", type=float, default=None,
                        help="Energy E0 in Chebyshev domain")
    parser.add_argument("--small", action="store_true",
                        help="Use small M grid (16-256) for smoke test")
    parser.add_argument("--tiny", action="store_true",
                        help="Use tiny M grid (16-64) for quick test")
    args = parser.parse_args()

    # Load config
    cfg = default_config()

    if args.config:
        with open(args.config, "r") as f:
            override = json.load(f)
        cfg.update(override)

    # CLI overrides
    if args.M_list is not None:
        cfg["M_list"] = [int(x) for x in args.M_list.split(",")]
    elif args.small:
        cfg["M_list"] = M_scan_grid("small")
    elif args.tiny:
        cfg["M_list"] = M_scan_grid("tiny")

    if args.mu_kernel is not None:
        cfg["mu_kernel"] = args.mu_kernel
    if args.methods is not None:
        cfg["summation_methods"] = [x.strip() for x in args.methods.split(",")]
    if args.n_trials is not None:
        cfg["n_trials"] = args.n_trials
    if args.theta_grid is not None:
        cfg["theta_grid"] = [float(x) for x in args.theta_grid.split(",")]
    if args.noise_level is not None:
        cfg["noise_level"] = args.noise_level
    if args.mpmath_dps is not None:
        cfg["mpmath_dps"] = args.mpmath_dps
    if args.lorentz_lambda is not None:
        cfg["lorentz_lambda"] = args.lorentz_lambda
    if args.mu_E0 is not None:
        cfg["mu_E0"] = args.mu_E0

    output_path = args.output or os.path.join(cfg["output_dir"], "data", "scan_results.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print("=" * 60)
    print("Γ-μ Random Walk Simulation — M-Scan Pipeline")
    print("=" * 60)
    print(f"M list:     {cfg['M_list']}")
    print(f"θ grid:     {[f'{t:.2f}π' for t in cfg['theta_grid']]}")
    print(f"μ kernel:   {cfg['mu_kernel']}")
    print(f"Methods:    {cfg['summation_methods']}")
    print(f"Trials:     {cfg['n_trials']}")
    print(f"Noise ε:    {cfg['noise_level']:.1e}")
    print(f"mpmath dps: {cfg['mpmath_dps']}")
    if cfg['mu_kernel'] == 'lorentz':
        print(f"Lorentz λ:  {cfg['lorentz_lambda']}")
    print(f"Output:     {output_path}")
    print("-" * 60)

    df = run_M_scan(cfg)

    if len(df) == 0:
        print("No data collected.")
        return

    # Save
    df.to_csv(output_path, index=False)
    print(f"\nSaved {len(df)} rows to {output_path}")

    # Print summary
    print("\n--- Summary ---")
    for method in cfg["summation_methods"]:
        mask = df["method"] == method
        if mask.any():
            subset = df[mask]
            # Per-M RMS
            M_groups = subset.groupby("M")["abs_err"].apply(rms_error)
            print(f"\n  {method}:")
            for M_val, rms_val in M_groups.items():
                print(f"    M={M_val:5d}: RMS={rms_val:.2e}")

            # Scaling fit
            if len(M_groups) >= 4:
                α, β, R2 = fit_scaling_law(
                    list(M_groups.index), list(M_groups.values))
                print(f"    Scaling: α={α:.3f}, R²={R2:.4f}")

    print("\nDone.")


if __name__ == "__main__":
    main()
