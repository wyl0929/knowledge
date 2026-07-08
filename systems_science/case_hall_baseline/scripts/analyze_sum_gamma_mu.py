#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-24 15:28:58
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-24 15:29:00
#FilePath     : /MG/test/analyze_sum_gamma_mu.py
#Description  :

#!/usr/bin/env python3
"""
analyze_sum_gamma_mu.py — VBL Phase B: sum(θ) 分析 (B4–B5)

功能:
  B4 — sum(θ) 曲线对比分析 (多 M 值 sum_gamma_mu vs θ 曲线)
  B5 — sum(θ) 积分收敛分析

用法:
  python test/analyze_sum_gamma_mu.py
"""

import re
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

# ─── 配置 ─────────────────────────────────────────────────────────────────
RUNS_DIR = "runs/0624"
OUT_DIR = "test"
os.makedirs(OUT_DIR, exist_ok=True)

# θ 积分的固定参数
# dckb_num_integ_steps = 2048 → theta_array 有 2048 个点
NUM_THETA = 2048


# ─── 工具函数 ─────────────────────────────────────────────────────────────

def parse_vbl_sum(log_path):
    """
    解析 [VBL_SUM] 行 → list of dicts {M, rs, theta:[], sum:[]}
    每行格式: [VBL_SUM] M=<num> rs=<num> <theta1>:<sum1> <theta2>:<sum2> ...
    """
    results = []
    pattern = re.compile(r"\[VBL_SUM\] M=(\d+) rs=(\d+)(.*)")

    with open(log_path, "r") as f:
        for line in f:
            m = pattern.search(line)
            if not m:
                continue
            M = int(m.group(1))
            rs = int(m.group(2))
            pairs_str = m.group(3).strip()
            pairs = pairs_str.split()
            theta_vals = []
            sum_vals = []
            for pair in pairs:
                t, s = pair.split(":")
                theta_vals.append(float(t))
                sum_vals.append(float(s))
            results.append({
                "M": M,
                "rs": rs,
                "theta": np.array(theta_vals),
                "sum": np.array(sum_vals),
            })
    return results


def find_slurm_logs():
    """查找集群 SLURM 输出文件 (本地或指定路径)"""
    # 尝试本地 runs 目录
    log_dir = RUNS_DIR
    matches = []
    for f in os.listdir(log_dir):
        if f.startswith("slurm-") and f.endswith(".out"):
            matches.append(os.path.join(log_dir, f))
    return sorted(matches)


def fetch_from_cluster(ssh_cmd="ssh h3clogin"):
    """从集群 grep [VBL_SUM] 日志"""
    import subprocess
    cmd = f'{ssh_cmd} "cd ~/scratch/MG && grep -h \\'\\[VBL_SUM\\]\\' slurm-*.out"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Warning: cluster fetch failed: {result.stderr}")
        return None

    # 解析输出
    lines = result.stdout.strip().split("\n")
    data = []
    pattern = re.compile(r"\[VBL_SUM\] M=(\d+) rs=(\d+)(.*)")
    for line in lines:
        m = pattern.search(line)
        if not m:
            continue
        M = int(m.group(1))
        rs = int(m.group(2))
        pairs_str = m.group(3).strip()
        pairs = pairs_str.split()
        theta_vals = []
        sum_vals = []
        for pair in pairs:
            t, s = pair.split(":")
            theta_vals.append(float(t))
            sum_vals.append(float(s))
        data.append({
            "M": M,
            "rs": rs,
            "theta": np.array(theta_vals),
            "sum": np.array(sum_vals),
        })
    return data


# ═══════════════════════════════════════════════════════════════════════════
# B4 — sum(θ) 曲线对比分析
# ═══════════════════════════════════════════════════════════════════════════

def jackson_kernel(M):
    """标准 Jackson kernel 系数 g_m (m=0..M-1)"""
    m = np.arange(M)
    alpha = np.pi / (M + 1)
    g = ((M - m + 1) * np.cos(alpha * m) + np.sin(alpha * m) / np.tan(alpha)) / (M + 1)
    return g


def reconstruct_sum_vs_theta(data_by_M, E_idx=0):
    """
    对于每个 M，用 sum_gamma_mu[θ] 数值积分重建 σ_xy
    用于验证内积正确性
    """
    pass  # 在 B5 中实现


def run_b4(data_by_M):
    """B4 — sum(θ) 曲线对比分析"""
    print("=" * 60)
    print("B4 — sum(θ) 曲线对比分析")
    print("=" * 60)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # 按 M 排序
    sorted_M = sorted(data_by_M.keys())

    for M in sorted_M:
        entry = data_by_M[M]
        theta = entry["theta"]
        sum_val = entry["sum"]

        label = f"M={M}"
        axes[0].plot(theta, sum_val, "-", label=label, linewidth=1.5)
        axes[1].plot(theta, np.abs(sum_val), "-", label=label, linewidth=1.5)

    axes[0].set_xlabel(r"$\theta$")
    axes[0].set_ylabel(r"$sum\_gamma\_mu(\theta)$")
    axes[0].set_title(r"$sum\_gamma\_mu$ vs $\theta$")
    axes[0].legend(fontsize=8)
    axes[0].grid(True, alpha=0.3)

    axes[1].set_xlabel(r"$\theta$")
    axes[1].set_ylabel(r"$|sum\_gamma\_mu(\theta)|$")
    axes[1].set_title(r"$|sum\_gamma\_mu|$ vs $\theta$ (对数)")
    axes[1].set_yscale("log")
    axes[1].legend(fontsize=8)
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    outpath = os.path.join(OUT_DIR, "sum_vs_theta_all_M.png")
    fig.savefig(outpath, dpi=150)
    plt.close()
    print(f"  sum(θ) 对比图已保存: {outpath}")

    return sorted_M


# ═══════════════════════════════════════════════════════════════════════════
# B5 — sum(θ) 积分收敛分析
# ═══════════════════════════════════════════════════════════════════════════

def integrate_sum(data_by_M, energies=None):
    """
    对每个 M 和能量点做 θ 积分:
    σ(E) = ∫ sum(θ) · f(E, cosθ) / sin³θ · dθ
    """
    if energies is None:
        energies = [-1.5, 0.0, 1.5]

    results = {}
    for M, entry in data_by_M.items():
        theta = entry["theta"]
        sum_val = entry["sum"]
        dtheta = theta[1] - theta[0] if len(theta) > 1 else np.pi / len(theta)

        eng_results = []
        for E in energies:
            # Fermi-Dirac 函数 (T=10K, beta=1/kT)
            efermi_re = E / 17.0  # meta.rescale = 17.0 (auto-detect)
            eng_re = np.cos(theta)
            div = np.sin(theta) ** 3

            # T=10K → beta = 1/(kB*10) ≈ 11604 K/eV / 10 = 1160.4 eV^-1
            beta = 1160.0  # approx for T=10K
            fd = 1.0 / (1.0 + np.exp(beta * (eng_re - efermi_re)))

            integrand = sum_val * fd * dtheta / div
            dcx = np.sum(integrand)
            eng_results.append(dcx)

        results[M] = {
            "energies": energies,
            "sigma": np.array(eng_results),
        }

    return results


def run_b5(data_by_M, sorted_M):
    """B5 — sum(θ) 积分收敛分析"""
    print("\n" + "=" * 60)
    print("B5 — sum(θ) 积分收敛分析")
    print("=" * 60)

    # 计算积分
    energies = [-1.5, 0.0, 1.5]
    integ_results = integrate_sum(data_by_M, energies)

    # 打印结果
    print(f"\n{'M':>6} | {'E=-1.5':>12} {'E=0.0':>12} {'E=1.5':>12}")
    print("-" * 46)
    for M in sorted_M:
        res = integ_results[M]
        vals = res["sigma"]
        print(f"{M:>6} | {vals[0]:>12.4f} {vals[1]:>12.4f} {vals[2]:>12.4f}")

    # 绘图: 积分值 vs M
    fig, ax = plt.subplots(figsize=(8, 6))
    M_vals = np.array(sorted_M)
    for i, E in enumerate(energies):
        sigma_vals = np.array([integ_results[M]["sigma"][i] for M in sorted_M])
        ax.plot(M_vals, sigma_vals, "o-", label=f"E={E} eV", linewidth=1.5, markersize=6)

    ax.set_xlabel("M (Chebyshev kernel size)")
    ax.set_ylabel(r"$\sigma_{xy}$ (e²/h)")
    ax.set_title("积分值收敛性 vs M")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    outpath = os.path.join(OUT_DIR, "sum_integral_convergence.png")
    fig.savefig(outpath, dpi=150)
    plt.close()
    print(f"\n  积分收敛图已保存: {outpath}")

    return integ_results


# ═══════════════════════════════════════════════════════════════════════════
# 主入口
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("VBL Phase B — sum(θ) 分析")
    print("=" * 60)

    # 从集群获取 [VBL_SUM] 日志
    print("\n从集群获取 [VBL_SUM] 日志...")
    data = fetch_from_cluster()
    if data is None or len(data) == 0:
        print("集群日志未就绪，尝试本地 SLURM 日志...")
        log_files = find_slurm_logs()
        if log_files:
            combined_data = []
            for lf in log_files:
                combined_data.extend(parse_vbl_sum(lf))
            data = combined_data
        else:
            print("未找到任何 [VBL_SUM] 日志。")
            print("请确保 B2/B3 Job 已完成，且输出文件已回传。")
            exit(1)

    # 按 M 重组
    data_by_M = {}
    for entry in data:
        M = entry["M"]
        if M not in data_by_M:
            data_by_M[M] = entry
        else:
            # 如果有多个能量点，取第一个
            pass

    print(f"  找到 {len(data_by_M)} 个 M 值: {sorted(data_by_M.keys())}")

    # B4
    sorted_M = run_b4(data_by_M)

    # B5
    run_b5(data_by_M, sorted_M)

    print("\n" + "=" * 60)
    print("B4/B5 分析完成!")
    print("=" * 60)
