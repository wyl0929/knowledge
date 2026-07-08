#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-27 23:11:13
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-27 23:11:19
#FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/src/config.py
#Description  :

"""
config.py — parameter definitions, defaults, M-scan grids.

Plan reference: docs/plan.md §5
"""


def default_config() -> dict:
    """Return default parameter dictionary (plan.md §5.1–5.3)."""
    return {
        # --- core scan parameters (§5.1) ---
        "M_list": [64, 128, 256, 384, 512, 768, 1024, 2048, 3072, 4096, 6144, 8192],
        "theta_grid": [0.1, 0.25, 0.5, 0.75, 0.9],  # in units of π
        "n_trials": 10,
        "noise_level": 2.2e-16,
        "summation_methods": ["sequential", "kahan"],
        "mpmath_dps": 50,
        "output_dir": "./output",

        # --- μ matrix model parameters (§5.2) ---
        "mu_kernel": "clean",       # "clean" | "jackson" | "lorentz"
        "lorentz_lambda": 4.0,
        "mu_E0": 0.0,

        # --- analysis parameters (§5.3) ---
        "error_threshold": 1e-10,
        "scaling_fit_range": (256, 4096),
    }


def M_scan_grid(mode: str = "log") -> list:
    """Return default M list for scanning.

    Parameters
    ----------
    mode : str
        "log"  → logarithmic-ish progression 64 → 8192
        "small"→ tiny M for smoke tests: 16, 32, 64, 128, 256
        "full" → same as "log"
    """
    if mode == "small":
        return [16, 32, 64, 128, 256]
    elif mode == "tiny":
        return [16, 32, 64]
    else:
        return default_config()["M_list"]


# --- self-test (small smoke) ---
if __name__ == "__main__":
    cfg = default_config()
    assert isinstance(cfg, dict)
    assert "M_list" in cfg
    assert cfg["noise_level"] < 1e-15
    grid = M_scan_grid("small")
    assert grid == [16, 32, 64, 128, 256]
    grid2 = M_scan_grid("tiny")
    assert grid2 == [16, 32, 64]
    print("config.py: all self-tests passed.")
