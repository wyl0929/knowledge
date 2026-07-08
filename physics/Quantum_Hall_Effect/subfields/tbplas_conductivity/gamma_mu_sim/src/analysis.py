#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-27 23:13:33
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-27 23:13:34
#FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/src/analysis.py
#Description  :

"""
analysis.py — error analysis and scaling law fitting.

Plan reference: docs/plan.md §4.5
"""

import numpy as np


def rms_error(errors: np.ndarray) -> float:
    """Root-mean-square error: sqrt(mean(e²)).

    Parameters
    ----------
    errors : np.ndarray
        1-d array of error values.

    Returns
    -------
    float
    """
    return float(np.sqrt(np.mean(np.square(errors))))


def fit_scaling_law(M_list: list, rms_list: list) -> tuple:
    """Fit log10(RMS) = α·log10(M) + β via linear regression.

    Parameters
    ----------
    M_list : list
        M values (Chebyshev order).
    rms_list : list
        Corresponding RMS errors.

    Returns
    -------
    (α, β, R²) : tuple of float
        Scaling exponent, intercept, and coefficient of determination.
    """
    x = np.log10(np.asarray(M_list, dtype=np.float64))
    y = np.log10(np.asarray(rms_list, dtype=np.float64))

    # Linear regression: y = α·x + β
    coeffs = np.polyfit(x, y, 1)
    α, β = coeffs[0], coeffs[1]

    # R²
    y_pred = α * x + β
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    R2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0

    return float(α), float(β), float(R2)


def n_trials_statistics(M: int, n_trials: int,
                        errors: np.ndarray = None,
                        **kwargs) -> dict:
    """Compute statistics over multiple trials at fixed M.

    Parameters
    ----------
    M : int
        Chebyshev order.
    n_trials : int
        Number of trials.
    errors : np.ndarray, optional
        Pre-computed absolute errors. If None, kwargs must contain
        the necessary parameters to generate them.
    **kwargs
        Passed through (unused if errors is provided).

    Returns
    -------
    dict
        {mean, std, min, max, rms}
    """
    if errors is None:
        raise ValueError("errors must be provided.")

    errors = np.asarray(errors, dtype=np.float64)
    return {
        "M": M,
        "n_trials": n_trials,
        "mean": float(np.mean(errors)),
        "std": float(np.std(errors, ddof=1)),
        "min": float(np.min(errors)),
        "max": float(np.max(errors)),
        "rms": rms_error(errors),
    }


def convergence_diagnostic(M_list: list,
                           errors_dict: dict,
                           threshold: float = 1e-10) -> dict:
    """Find the first M where RMS error exceeds threshold.

    Parameters
    ----------
    M_list : list
        Sorted M values.
    errors_dict : dict
        Mapping M → RMS error.
    threshold : float
        Error threshold.

    Returns
    -------
    dict
        {first_exceed_M, first_exceed_rms, all_exceed: bool}
        first_exceed_M = None if never exceeded.
    """
    for M in sorted(M_list):
        if errors_dict.get(M, 0.0) > threshold:
            return {
                "first_exceed_M": M,
                "first_exceed_rms": errors_dict[M],
                "all_exceed": False,
            }
    return {
        "first_exceed_M": None,
        "first_exceed_rms": None,
        "all_exceed": True,
    }


# --- self-test ---
if __name__ == "__main__":
    # Test rms_error
    e = np.array([1.0, 2.0, 3.0])
    assert abs(rms_error(e) - np.sqrt(14.0/3.0)) < 1e-14

    # Test fit_scaling_law with known data: log10(RMS) = 2.0*log10(M) + 1.0
    M = [10, 100, 1000]
    rms = [1000.0, 100000.0, 10000000.0]  # RMS = 10·M²
    α, β, R2 = fit_scaling_law(M, rms)
    print(f"Known data: α={α:.4f}, β={β:.4f}, R²={R2:.6f}")
    assert abs(α - 2.0) < 0.01, f"α={α} != 2.0"
    assert R2 > 0.999, f"R²={R2} < 0.999"

    # Test n_trials_statistics
    stats = n_trials_statistics(64, 5, errors=np.array([1e-15, 2e-15, 3e-15, 4e-15, 5e-15]))
    assert abs(stats["mean"] - 3e-15) < 1e-16
    assert "rms" in stats

    # Test convergence_diagnostic
    M_list = [64, 128, 256]
    err_dict = {64: 1e-15, 128: 1e-12, 256: 1e-8}
    diag = convergence_diagnostic(M_list, err_dict, threshold=1e-10)
    assert diag["first_exceed_M"] == 256
    diag2 = convergence_diagnostic(M_list, err_dict, threshold=1e-6)
    assert diag2["first_exceed_M"] is None

    print("analysis.py: all self-tests passed.")
