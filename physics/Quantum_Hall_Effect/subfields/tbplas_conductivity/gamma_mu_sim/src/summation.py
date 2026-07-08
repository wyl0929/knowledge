#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-27 23:11:30
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-27 23:11:35
#FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/src/summation.py
#Description  :

"""
summation.py — double summation engines.

S = Σ_{m=0}^{M-1} Σ_{n=0}^{M-1} Re[Γ_{mn} · μ_{mn}]

Two methods:
  - sequential: standard double-loop accumulation
  - kahan:      Kahan compensated summation

Plan reference: docs/plan.md §4.3
"""

import numpy as np


def sum_sequential(gamma: np.ndarray, mu: np.ndarray) -> float:
    """Standard sequential double summation.

    Parameters
    ----------
    gamma : np.ndarray
        (M, M) complex Γ matrix.
    mu : np.ndarray
        (M, M) real μ matrix.

    Returns
    -------
    float
        Σ Re[Γ_{mn}·μ_{mn}]
    """
    M = gamma.shape[0]
    total = 0.0
    for m in range(M):
        for n in range(M):
            total += (gamma[m, n].real * mu[m, n])
    return total


def sum_kahan(gamma: np.ndarray, mu: np.ndarray) -> float:
    """Kahan compensated double summation.

    Maintains a running compensation term to recover low-order bits
    lost in floating-point accumulation.

    Parameters
    ----------
    gamma : np.ndarray
        (M, M) complex Γ matrix.
    mu : np.ndarray
        (M, M) real μ matrix.

    Returns
    -------
    float
        Σ Re[Γ_{mn}·μ_{mn}]
    """
    M = gamma.shape[0]
    total = 0.0
    compensation = 0.0
    for m in range(M):
        for n in range(M):
            term = gamma[m, n].real * mu[m, n]
            y = term - compensation
            t = total + y
            compensation = (t - total) - y
            total = t
    return total


def sum_dispatch(gamma: np.ndarray, mu: np.ndarray, method: str) -> float:
    """Dispatch to the appropriate summation method.

    Parameters
    ----------
    gamma : np.ndarray
        (M, M) complex Γ matrix.
    mu : np.ndarray
        (M, M) real μ matrix.
    method : str
        "sequential" or "kahan".

    Returns
    -------
    float
    """
    if method == "sequential":
        return sum_sequential(gamma, mu)
    elif method == "kahan":
        return sum_kahan(gamma, mu)
    else:
        raise ValueError(f"Unknown summation method: '{method}'. "
                         f"Use 'sequential' or 'kahan'.")


# --- self-test ---
if __name__ == "__main__":
    M = 32

    # Generate small test matrices
    from gamma_matrix import gamma_matrix_full
    from mu_matrix import mu_matrix_generate
    theta = np.pi / 4
    gamma = gamma_matrix_full(M, theta)
    mu_true, _ = mu_matrix_generate(M, kernel="clean", E0=0.0, seed=42)

    s_seq = sum_sequential(gamma, mu_true)
    s_kahan = sum_kahan(gamma, mu_true)

    print(f"sequential = {s_seq:.15e}")
    print(f"kahan      = {s_kahan:.15e}")
    diff = abs(s_seq - s_kahan)
    print(f"|diff|     = {diff:.1e}")

    # They should agree to high precision at M=32
    # (absolute difference may be up to ~√N·ε ≈ √1024·2.2e-16 ≈ 7e-15)
    assert diff < 5e-14, f"Sequential vs Kahan differ by {diff}"

    # Test dispatch
    s_d = sum_dispatch(gamma, mu_true, "sequential")
    assert s_d == s_seq

    print("summation.py: all self-tests passed.")
