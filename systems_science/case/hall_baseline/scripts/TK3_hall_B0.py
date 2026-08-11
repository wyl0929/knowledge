#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-07-01 00:10:34
#LastEditors  : Yulong Wang
#LastEditTime : 2026-07-01 00:10:37
#FilePath     : /MG/test/TK3_hall_B0.py
#Description  :

#!/usr/bin/env python3
"""
TK3: quantum-kite B=0 零磁场 Hall 验证
Monolayer graphene σ_xy(E) at B=0 — 基准测试
时间反演对称性要求 σ_xy(E) ≈ 0 ∀E

Workflow: Python → HDF5 → KITEx → KITE-tools → .dat 文本
"""

import sys
sys.path.insert(0, '/home/wyl/quantum-kite')

import os
import subprocess
import numpy as np
import pybinding as pb
import kite

# ============================================================
# 路径配置
# ============================================================
PROJECT_ROOT = '/home/wyl/project/MG'
KITE_BUILD = '/home/wyl/quantum-kite/build'
OUTPUT_DIR = f'{PROJECT_ROOT}/runs/kite/phase1_first_run'
FIG_DIR = f'{PROJECT_ROOT}/figures/kite/phase1'
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(FIG_DIR, exist_ok=True)

# ============================================================
# TB 参数 (与 MG/src/model.py 完全一致)
# ============================================================
t = 2.7         # nearest-neighbor hopping (eV)
a_cc = 0.142    # carbon-carbon distance (nm)
a_uc = 0.246    # unit cell length (nm) = sqrt(3) * a_cc

# ============================================================
# KPM 参数 (对齐 TK3 规格)
# ============================================================
M = 256                # Chebyshev 矩数
rs = 8                 # 随机向量数
T_K = 1.0              # 温度 (K)
E_MIN, E_MAX = -1.5, 1.5
E_POINTS = 301
LX, LY = 128, 128      # 超胞大小 (B=0 测试用小胞即可)
NX, NY = 2, 2           # domain decomposition

# ============================================================
# 构建 monolayer graphene 晶格
# ============================================================
def graphene_monolayer(t_hop=t):
    """与 tbplas 等价 TB 参数的单层石墨烯 pybinding 晶格"""
    a1 = a_uc * np.array([1, 0])
    a2 = a_uc * np.array([1/2, 1/2 * np.sqrt(3)])

    lat = pb.Lattice(a1=a1, a2=a2)
    lat.add_sublattices(
        ('A', [0, -a_cc/2], 0.0),
        ('B', [0,  a_cc/2], 0.0)
    )
    lat.add_hoppings(
        ([0, 0], 'A', 'B', -t_hop),       # 胞内
        ([1, -1], 'A', 'B', -t_hop),      # 胞间
        ([0, -1], 'A', 'B', -t_hop)       # 胞间
    )
    return lat


def run_kite_hall(lattice, B_field, output_h5, M=M, rs=rs, T_K=T_K,
                  e_min=E_MIN, e_max=E_MAX, e_points=E_POINTS,
                  lx=LX, ly=LY, nx=NX, ny=NY):
    """
    生成 quantum-kite HDF5 配置并运行 KITEx + KITE-tools

    Parameters
    ----------
    lattice : pb.Lattice
    B_field : float
        磁场强度 (Tesla), B=0 表示零场
    output_h5 : str
        输出 HDF5 文件名
    """
    # ── 1. Configuration ──
    # 带宽: ±3t = ±8.1 eV, 加 safety buffer
    spectrum_range = [-3.01 * t, 3.01 * t]  # ≈ [-8.127, 8.127]

    # B=0 时不需要复数哈密顿量; B≠0 时 Modification 会触发自动切换
    is_complex = (B_field > 0)

    configuration = kite.Configuration(
        divisions=[nx, ny],
        length=[lx, ly],
        boundaries=["periodic", "periodic"],
        is_complex=is_complex,
        precision=1,                    # double
        spectrum_range=spectrum_range
    )

    # ── 2. Calculation ──
    calculation = kite.Calculation(configuration)
    calculation.conductivity_dc(
        direction='xy',
        num_points=e_points,
        num_moments=M,
        num_random=rs,
        num_disorder=1,                 # 干净体系
        temperature=T_K
    )

    # ── 3. Modification (磁场) ──
    if B_field > 0:
        modification = kite.Modification(magnetic_field=B_field)
    else:
        modification = None

    # ── 4. 生成 HDF5 ──
    print(f"\n{'='*60}")
    print(f"Generating HDF5: {output_h5}")
    print(f"  B = {B_field} T, M = {M}, rs = {rs}, T = {T_K} K")
    print(f"  Energy: [{e_min}, {e_max}] eV, {e_points} points")
    print(f"  Supercell: {lx}×{ly}, DD: {nx}×{ny}")
    print(f"  is_complex = {is_complex}")
    print(f"{'='*60}")

    kite.config_system(lattice, configuration, calculation,
                       modification=modification, filename=output_h5)

    # ── 5. 运行 KITEx ──
    print(f"\nRunning KITEx...")
    result = subprocess.run(
        [f'{KITE_BUILD}/KITEx', output_h5],
        capture_output=True, text=True, cwd=os.path.dirname(output_h5)
    )
    print(result.stdout)
    if result.returncode != 0:
        print(f"KITEx stderr:\n{result.stderr}")
        raise RuntimeError(f"KITEx failed with return code {result.returncode}")

    # ── 6. 运行 KITE-tools ──
    print(f"\nRunning KITE-tools...")
    result = subprocess.run(
        [f'{KITE_BUILD}/KITE-tools', output_h5],
        capture_output=True, text=True, cwd=os.path.dirname(output_h5)
    )
    print(result.stdout)
    if result.returncode != 0:
        print(f"KITE-tools stderr:\n{result.stderr}")
        raise RuntimeError(f"KITE-tools failed with return code {result.returncode}")

    # ── 7. 查找输出文件 ──
    h5_dir = os.path.dirname(output_h5)
    # KITE-tools outputs condDC.dat (energy, sigma_xx, sigma_xy)
    expected_dat = os.path.join(h5_dir, 'condDC.dat')
    if os.path.exists(expected_dat):
        print(f"\nOutput: {expected_dat}")
        return expected_dat
    else:
        # also check current working directory
        alt_dat = 'condDC.dat'
        if os.path.exists(alt_dat):
            target = os.path.join(h5_dir, alt_dat)
            os.rename(alt_dat, target)
            print(f"\nOutput (moved): {target}")
            return target
        else:
            raise FileNotFoundError(f"Cannot find condDC.dat in {h5_dir} or CWD")


# ============================================================
# TK3: B=0 Hall 验证
# ============================================================
def main():
    lattice = graphene_monolayer(t)

    # B=0 计算
    output_h5 = f'{OUTPUT_DIR}/kite_monolayer_B0_M{M}.h5'
    dat_file = run_kite_hall(lattice, B_field=0.0, output_h5=output_h5)

    # 重命名输出为任务约定名称
    target_txt = f'{OUTPUT_DIR}/kite_monolayer_B0_M{M}_hall.txt'
    os.rename(dat_file, target_txt)
    print(f"\nSaved: {target_txt}")

    # ── 快速验证 ──
    data = np.loadtxt(target_txt)
    energy = data[:, 0]
    sigma_xx = data[:, 1]
    sigma_xy = data[:, 2]

    print(f"\n{'='*60}")
    print(f"TK3 B=0 结果快速验证:")
    print(f"  Energy range: [{energy[0]:.4f}, {energy[-1]:.4f}] eV")
    print(f"  σ_xy range: [{sigma_xy.min():.6f}, {sigma_xy.max():.6f}] e²/h")
    print(f"  σ_xy mean: {sigma_xy.mean():.6f} e²/h")
    print(f"  σ_xy std:  {sigma_xy.std():.6f} e²/h")
    print(f"  |σ_xy| < 0.1: {(np.abs(sigma_xy) < 0.1).all()}")
    print(f"{'='*60}")

    # ── 绘图 ──
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(energy, sigma_xy, 'b-', linewidth=0.8)
    ax.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
    ax.axhline(y=0.1, color='r', linestyle=':', linewidth=0.5, label='±0.1 e²/h')
    ax.axhline(y=-0.1, color='r', linestyle=':', linewidth=0.5)
    ax.fill_between([energy[0], energy[-1]], -0.1, 0.1, alpha=0.1, color='gray')
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('σ_xy (e²/h)')
    ax.set_title(f'quantum-kite Monolayer Graphene B=0, M={M}, rs={rs}, T={T_K}K')
    ax.legend()
    ax.grid(True, alpha=0.3)

    fig_path = f'{FIG_DIR}/hall_monolayer_B0_M{M}.png'
    fig.savefig(fig_path, dpi=150, bbox_inches='tight')
    print(f"Figure saved: {fig_path}")
    plt.close()


if __name__ == '__main__':
    main()
