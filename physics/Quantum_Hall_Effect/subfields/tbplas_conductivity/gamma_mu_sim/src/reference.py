#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-27 23:11:36
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-27 23:11:39
#FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/src/reference.py
#Description  :

"""
reference.py — mpmath high-precision ground truth.

Plan reference: docs/plan.md §4.4
"""

import numpy as np

# mpmath is optional at import time; we import it lazily in functions.
# This avoids blocking module import if mpmath isn't installed.


def _ensure_mpmath():
    """Lazy-import mpmath."""
    try:
        import mpmath as mp
        return mp
    except ImportError:
        raise ImportError("mpmath is required for reference.py. "
                          "Install with: pip install mpmath")


def gamma_element_mpmath(m: int, n: int, theta, dps: int = 50):
    """mpmath high-precision Γ_{mn}(θ).

    Parameters
    ----------
    m, n : int
        Chebyshev indices.
    theta : float
        Angle in radians.
    dps : int
        Decimal places precision.

    Returns
    -------
    mp.mpc
    """
    mp = _ensure_mpmath()
    mp.mp.dps = dps
    sin_t = mp.sin(theta)
    cos_t = mp.cos(theta)
    cos_m = mp.cos(m * theta)
    cos_n = mp.cos(n * theta)
    exp_in = mp.e ** (1j * n * theta)
    exp_im = mp.e ** (-1j * m * theta)
    term1 = cos_m * (cos_t - 1j * n * sin_t) * exp_in
    term2 = cos_n * (cos_t + 1j * m * sin_t) * exp_im
    return term1 + term2


def sum_exact_mpmath(gamma_np: np.ndarray, mu_np: np.ndarray,
                     dps: int = 50) -> 'mp.mpf':
    """High-precision double summation using mpmath.

    Converts numpy Γ and μ arrays to mpmath types and computes the sum
    with dps decimal places.

    Parameters
    ----------
    gamma_np : np.ndarray
        (M, M) complex128 Γ matrix.
    mu_np : np.ndarray
        (M, M) float64 μ matrix.
    dps : int
        Decimal places precision.

    Returns
    -------
    mp.mpf
        High-precision sum.
    """
    mp = _ensure_mpmath()
    mp.mp.dps = dps
    M = gamma_np.shape[0]
    total = mp.mpf('0')
    for m in range(M):
        for n in range(M):
            g = mp.mpc(gamma_np[m, n])
            mu_val = mp.mpf(float(mu_np[m, n]))
            total += mp.re(g * mu_val)
    return total


# --- self-test ---
if __name__ == "__main__":
    M = 32
    theta = np.pi / 4

    from gamma_matrix import gamma_matrix_full, gamma_element
    from mu_matrix import mu_matrix_generate

    gamma = gamma_matrix_full(M, theta)
    mu_true, _ = mu_matrix_generate(M, kernel="clean", E0=0.0)

    # mpmath reference
    S_ref = sum_exact_mpmath(gamma, mu_true, dps=50)
    S_ref_f = float(S_ref)

    # numpy sequential for comparison
    from summation import sum_sequential
    S_seq = sum_sequential(gamma, mu_true)

    print(f"mpmath (dps=50)  = {S_ref_f:.15e}")
    print(f"sequential       = {S_seq:.15e}")
    diff = abs(S_seq - S_ref_f)
    print(f"|diff|           = {diff:.1e}")

    # For M=32, they should agree to ~1e-14 or better
    assert diff < 1e-13, f"mpmath vs sequential differ by {diff}"

    # Test gamma_element_mpmath vs numpy
    g_mp = gamma_element_mpmath(10, 15, theta, dps=30)
    g_np = gamma_element(10, 15, theta)
    assert abs(float(g_mp.real) - g_np.real) < 1e-14
    assert abs(float(g_mp.imag) - g_np.imag) < 1e-14

    print("reference.py: all self-tests passed.")
