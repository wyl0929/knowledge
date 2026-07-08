#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-27 23:11:25
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-27 23:11:31
#FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/src/mu_matrix.py
#Description  :

"""
mu_matrix.py — Chebyshev moment μ matrix generation.

Three kernel models:
  - clean:    g_n ≡ 1 (no damping)
  - jackson:  Jackson kernel (tbplas default)
  - lorentz:  Lorentz kernel (λ-controlled exponential damping)

μ_{mn} = g_m · g_n · T_m(E0)·T_n(E0)  +  δμ_{mn}
where δμ ~ N(0, ε) is floating-point noise.

Reference: tbplas kpm.cpp:8-17 (Jackson kernel), kubo_bastin.h:262-268 (μ assembly)
Plan reference: docs/plan.md §4.2
"""

import numpy as np
from scipy.special import eval_chebyt


# ---------------------------------------------------------------------------
# Raw Chebyshev moments
# ---------------------------------------------------------------------------

def mu_raw_clean(M: int, E0: float = 0.0, seed: int = None) -> np.ndarray:
    """Generate raw Chebyshev moments: μ_{mn} = T_m(E0)·T_n(E0).

    For E0=0 (the standard case), uses the analytic form:
        T_n(0) = cos(n·π/2)
    which is stable for arbitrarily high n (unlike scipy's eval_chebyt
    which produces NaN for n ≥ 2466 due to recurrence instability).

    Parameters
    ----------
    M : int
        Number of Chebyshev moments.
    E0 : float
        Energy in Chebyshev domain [-1, 1].
    seed : int, optional
        RNG seed (unused, kept for interface consistency).

    Returns
    -------
    np.ndarray
        (M, M) float64 matrix.
    """
    if not -1.0 <= E0 <= 1.0:
        raise ValueError(f"E0={E0} outside Chebyshev domain [-1, 1].")
    n = np.arange(M, dtype=np.float64)

    # Use analytic form for E0=0 (stable for arbitrarily high n)
    if abs(E0) < 1e-15:
        Tn = np.cos(n * np.pi / 2.0)
    else:
        # For general E0, scipy's eval_chebyt may produce NaN for n ≥ 2466
        Tn = eval_chebyt(n, E0)
        if np.any(np.isnan(Tn)):
            raise RuntimeError(
                f"eval_chebyt produced NaN for n≥2466 at E0={E0}. "
                f"Use E0=0 (analytic form) for M≥2466, or implement "
                f"a stable recurrence for general E0.")

    mu = np.outer(Tn, Tn)
    return mu


# ---------------------------------------------------------------------------
# Kernel functions
# ---------------------------------------------------------------------------

def jackson_kernel(n: int, M: int) -> float:
    """Jackson kernel g_n^{(M)}.

    g_0 = 1.0
    g_n = ((M-n+1)·cos(π·n/(M+1)) + cot(π/(M+1))·sin(π·n/(M+1))) / (M+1)

    Reference: tbplas kpm.cpp:8-17

    Parameters
    ----------
    n : int
        Index, 0 ≤ n < M.
    M : int
        Kernel order (number of Chebyshev moments).

    Returns
    -------
    float
    """
    if n == 0:
        return 1.0
    denom = float(M + 1)
    theta = np.pi / denom
    cot = np.cos(theta) / np.sin(theta)
    return ((denom - n) * np.cos(theta * n) + cot * np.sin(theta * n)) / denom


def jackson_kernel_vector(M: int) -> np.ndarray:
    """Vectorized Jackson kernel for all n=0,…,M-1."""
    kernel = np.ones(M, dtype=np.float64)
    if M <= 1:
        return kernel
    denom = float(M + 1)
    theta = np.pi / denom
    cot = np.cos(theta) / np.sin(theta)
    n = np.arange(1, M, dtype=np.float64)
    kernel[1:] = ((denom - n) * np.cos(theta * n) + cot * np.sin(theta * n)) / denom
    return kernel


def lorentz_kernel(n: int, M: int, lam: float = 4.0) -> float:
    """Lorentz kernel: g_n(λ) = sinh(λ·(1 - n/M)) / sinh(λ).

    Reference: García 2015, PRL 114, 116602; Weisse 2006 RMP.

    Parameters
    ----------
    n : int
        Index, 0 ≤ n < M.
    M : int
        Kernel order.
    lam : float
        Broadening parameter λ > 0.

    Returns
    -------
    float
    """
    if n == 0:
        return 1.0
    if lam <= 0:
        raise ValueError(f"lam={lam} must be > 0.")
    return np.sinh(lam * (1.0 - n / M)) / np.sinh(lam)


def lorentz_kernel_vector(M: int, lam: float = 4.0) -> np.ndarray:
    """Vectorized Lorentz kernel for all n=0,…,M-1."""
    if lam <= 0:
        raise ValueError(f"lam={lam} must be > 0.")
    n = np.arange(M, dtype=np.float64)
    return np.sinh(lam * (1.0 - n / M)) / np.sinh(lam)


# ---------------------------------------------------------------------------
# Kernel application
# ---------------------------------------------------------------------------

def apply_kernel(mu_raw: np.ndarray,
                 kernel_m: np.ndarray,
                 kernel_n: np.ndarray) -> np.ndarray:
    """Apply kernel weighting: μ_{mn} = g_m · g_n · μ_{mn}^{raw}.

    Parameters
    ----------
    mu_raw : np.ndarray
        (M, M) raw Chebyshev moments.
    kernel_m, kernel_n : np.ndarray
        Kernel vectors of length M.

    Returns
    -------
    np.ndarray
        (M, M) kernel-weighted μ matrix.
    """
    weights = np.outer(kernel_m, kernel_n)
    return mu_raw * weights


# ---------------------------------------------------------------------------
# Noise layer
# ---------------------------------------------------------------------------

def mu_noise_layer(mu_true: np.ndarray,
                   eps: float = 2.2e-16,
                   seed: int = None) -> np.ndarray:
    """Add zero-mean Gaussian noise δμ ~ N(0, ε) to μ_true.

    Parameters
    ----------
    mu_true : np.ndarray
        (M, M) noise-free μ matrix.
    eps : float
        Standard deviation of the noise.
    seed : int, optional
        RNG seed for reproducibility.

    Returns
    -------
    np.ndarray
        mu_noisy = mu_true + δμ.
    """
    rng = np.random.RandomState(seed)
    noise = rng.normal(loc=0.0, scale=eps, size=mu_true.shape)
    return mu_true + noise


# ---------------------------------------------------------------------------
# Unified interface
# ---------------------------------------------------------------------------

def mu_matrix_generate(M: int, kernel: str = "clean",
                       E0: float = 0.0,
                       noise_level: float = 2.2e-16,
                       lorentz_lambda: float = 4.0,
                       seed: int = None) -> tuple:
    """Unified μ matrix generation.

    Parameters
    ----------
    M : int
        Number of Chebyshev moments.
    kernel : str
        "clean" | "jackson" | "lorentz"
    E0 : float
        Energy in Chebyshev domain [-1, 1].
    noise_level : float
        ε for δμ ~ N(0, ε).
    lorentz_lambda : float
        λ for Lorentz kernel (ignored otherwise).
    seed : int, optional
        RNG seed.

    Returns
    -------
    (mu_true, mu_noisy) : tuple of np.ndarray
        Both shape (M, M), float64.
    """
    mu_raw = mu_raw_clean(M, E0)

    if kernel == "clean":
        mu_true = mu_raw  # g_n ≡ 1
    elif kernel == "jackson":
        kv = jackson_kernel_vector(M)
        mu_true = apply_kernel(mu_raw, kv, kv)
    elif kernel == "lorentz":
        kv = lorentz_kernel_vector(M, lorentz_lambda)
        mu_true = apply_kernel(mu_raw, kv, kv)
    else:
        raise ValueError(f"Unknown kernel: '{kernel}'. "
                         f"Use 'clean', 'jackson', or 'lorentz'.")

    mu_noisy = mu_noise_layer(mu_true, noise_level, seed)
    return mu_true, mu_noisy


# --- self-test ---
if __name__ == "__main__":
    M = 64

    # 1. raw clean: values in [-1, 1]
    mu = mu_raw_clean(M, E0=0.0)
    assert mu.shape == (M, M)
    assert np.all(np.abs(mu) <= 1.0 + 1e-14), "mu_raw out of [-1,1]"
    # T_0(0)=1, T_n(0)=0 for odd n, ±1 for even n
    assert abs(mu[0, 0] - 1.0) < 1e-14

    # 2. Jackson kernel
    g0 = jackson_kernel(0, M)
    g_last = jackson_kernel(M - 1, M)
    assert abs(g0 - 1.0) < 1e-14, f"g0={g0} != 1"
    assert g_last > 0, f"g_{{{M-1}}}={g_last} ≤ 0"
    print(f"Jackson kernel: g_0={g0:.4f}, g_{{{M-1}}}={g_last:.6f}")

    # 3. Lorentz kernel
    gl0 = lorentz_kernel(0, M, lam=4.0)
    gl_last = lorentz_kernel(M - 1, M, lam=4.0)
    assert abs(gl0 - 1.0) < 1e-14
    assert gl_last > 0
    print(f"Lorentz kernel(λ=4): g_0={gl0:.4f}, g_{{{M-1}}}={gl_last:.6f}")

    # 4. mu_matrix_generate
    mu_true, mu_noisy = mu_matrix_generate(M, kernel="jackson", seed=42)
    assert mu_true.shape == (M, M)
    assert mu_noisy.shape == (M, M)
    delta = mu_noisy - mu_true
    # Noise should be small
    assert np.abs(delta).max() < 10 * 2.2e-16
    print(f"μ noise max|δ| = {np.abs(delta).max():.1e}")

    # 5. Verify vectorized jackson matches scalar
    kv = jackson_kernel_vector(M)
    for i in range(M):
        assert abs(kv[i] - jackson_kernel(i, M)) < 1e-15

    # 6. Verify vectorized lorentz matches scalar
    lv = lorentz_kernel_vector(M, lam=4.0)
    for i in range(M):
        assert abs(lv[i] - lorentz_kernel(i, M, 4.0)) < 1e-15

    print("mu_matrix.py: all self-tests passed.")
