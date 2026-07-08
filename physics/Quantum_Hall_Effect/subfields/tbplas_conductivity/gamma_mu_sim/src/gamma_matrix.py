#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-27 23:11:19
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-27 23:11:25
#FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/src/gamma_matrix.py
#Description  :

"""
gamma_matrix.py — analytic Γ matrix generation.

Γ_{mn}(θ) = cos(mθ)·(cosθ - i·n·sinθ)·e^{i·nθ}
           + cos(nθ)·(cosθ + i·m·sinθ)·e^{-i·mθ}

Reference: tbplas kubo_bastin.h:131-167 (C++ implementation)
Plan reference: docs/plan.md §4.1
"""

import numpy as np


def gamma_element(m: int, n: int, theta: float) -> complex:
    """Compute a single Γ_{mn}(θ) element.

    Parameters
    ----------
    m, n : int
        Chebyshev indices, 0 ≤ m, n < M.
    theta : float
        Angle in radians, 0 < θ < π.

    Returns
    -------
    complex
    """
    sin_t = np.sin(theta)
    cos_t = np.cos(theta)
    cos_m = np.cos(m * theta)
    cos_n = np.cos(n * theta)
    exp_in = complex(np.cos(n * theta), np.sin(n * theta))
    exp_im = complex(np.cos(m * theta), -np.sin(m * theta))  # e^{-i m θ}
    term1 = cos_m * (cos_t - 1j * n * sin_t) * exp_in
    term2 = cos_n * (cos_t + 1j * m * sin_t) * exp_im
    return complex(term1 + term2)


def gamma_matrix_full(M: int, theta: float, dtype: str = 'complex128') -> np.ndarray:
    """Generate full M×M Γ matrix for a single θ.

    Parameters
    ----------
    M : int
        Number of Chebyshev moments (kernel order).
    theta : float
        Angle in radians, 0 < θ < π.
    dtype : str
        NumPy dtype string, 'complex128' or 'complex64'.

    Returns
    -------
    np.ndarray
        Complex matrix of shape (M, M).
    """
    if theta <= 0 or theta >= np.pi:
        raise ValueError(f"theta={theta} is outside (0, π); singularities at endpoints.")

    sin_t = np.sin(theta)
    cos_t = np.cos(theta)
    n = np.arange(M, dtype=np.float64)
    cos_nt = np.cos(n * theta)

    # fn[n] = (cosθ - i·n·sinθ) · e^{i·n·θ}
    fn = (cos_t - 1j * n * sin_t) * (cos_nt + 1j * np.sin(n * theta))
    fm = np.conj(fn)  # fm[m] = (cosθ + i·m·sinθ) · e^{-i·m·θ}

    # gmn(i,j) = cos_nt[i]*fn[j] + cos_nt[j]*fm[i]
    gamma = np.add.outer(cos_nt, fn)  # shape (M, M), but we need specific structure
    # Actually: gamma[i,j] = cos_nt[i] * fn[j] + cos_nt[j] * fm[i]
    gamma = cos_nt[:, np.newaxis] * fn[np.newaxis, :] + cos_nt[np.newaxis, :] * fm[:, np.newaxis]

    return gamma.astype(dtype, copy=False)


def gamma_matrix_theta_grid(M: int, n_theta: int) -> np.ndarray:
    """Generate Γ matrices on a uniform θ ∈ (0, π) grid.

    θ_k = π·(k+1) / (n_θ+1)  for k = 0, …, n_θ-1
    (endpoints 0, π are excluded to avoid singularities.)

    Parameters
    ----------
    M : int
        Number of Chebyshev moments.
    n_theta : int
        Number of θ points.

    Returns
    -------
    np.ndarray
        Complex array of shape (n_theta, M, M).
    """
    theta_vals = np.pi * np.arange(1, n_theta + 1, dtype=np.float64) / (n_theta + 1)
    gamma_grid = np.empty((n_theta, M, M), dtype='complex128')
    for k, theta in enumerate(theta_vals):
        gamma_grid[k] = gamma_matrix_full(M, theta)
    return gamma_grid


# --- self-test ---
if __name__ == "__main__":
    # Smoke test: small M
    M = 32
    theta = np.pi / 4
    gamma = gamma_matrix_full(M, theta)
    assert gamma.shape == (M, M)
    assert gamma.dtype in (np.complex128, np.complex64)

    # Check a few elements against scalar computation
    for m_test in [0, M-1]:
        for n_test in [0, M-1]:
            expected = gamma_element(m_test, n_test, theta)
            actual = gamma[m_test, n_test]
            assert abs(actual - expected) < 1e-14, \
                f"m={m_test}, n={n_test}: {actual} vs {expected}"

    # Quantity check: max|Γ| ≈ M
    max_val = np.max(np.abs(gamma))
    print(f"M={M}, θ=π/4, max|Γ| = {max_val:.2f} (expected ~{M})")
    assert 0.5 * M < max_val < 2.5 * M, f"max|Γ|={max_val} not ~M={M}"

    # θ grid test
    gamma_grid = gamma_matrix_theta_grid(M, 5)
    assert gamma_grid.shape == (5, M, M)

    print("gamma_matrix.py: all self-tests passed.")
