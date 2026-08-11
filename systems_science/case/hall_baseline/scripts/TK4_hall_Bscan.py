#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-07-01 00:13:57
#LastEditors  : Yulong Wang
#LastEditTime : 2026-07-01 00:14:04
#FilePath     : /MG/test/TK4_hall_Bscan.py
#Description  :

#!/usr/bin/env python3
"""
TK4: quantum-kite B≠0 QHE 信号初探
Monolayer graphene σ_xy(E) at B=50T, 100T, 200T
验证 QHE 平台: σ_xy = ±2, ±6, ±10 e²/h

Workflow: Python → HDF5 → KITEx → KITE-tools → .dat 文本
"""

import sys
sys.path.insert(0, '/home/wyl/quantum-kite')

import os
import subprocess
import numpy as np
import pybinding as pb
import kite
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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
a_uc = 0.246    # unit cell length (nm)

# ============================================================
# KPM 参数 (TK4 规格)
# ============================================================
M = 256
rs = 8
T_K = 1.0
E_MIN, E_MAX = -1.5, 1.5
E_POINTS = 301
LX, LY = 128, 1584     # 超胞大小 (ly 需满足: TILE×NY=16 的倍数, 且 B 量子化)
NX, NY = 2, 2

# B 场扫描
B_VALUES = [50.0, 100.0, 200.0]


def graphene_monolayer(t_hop=t):
    """单层石墨烯 pybinding 晶格 (3D, z=0 平面)"""
    a1 = a_uc * np.array([1, 0, 0])
    a2 = a_uc * np.array([1/2, 1/2 * np.sqrt(3), 0])
    lat = pb.Lattice(a1=a1, a2=a2)
    lat.add_sublattices(
        ('A', [0, -a_cc/2, 0], 0.0),
        ('B', [0,  a_cc/2, 0], 0.0)
    )
    lat.add_hoppings(
        ([0, 0, 0], 'A', 'B', -t_hop),
        ([1, -1, 0], 'A', 'B', -t_hop),
        ([0, -1, 0], 'A', 'B', -t_hop)
    )
    return lat


def run_kite_hall_B(lattice, B_field, output_h5):
    """运行 quantum-kite Hall 计算 (单 B 值)"""
    spectrum_range = [-3.01 * t, 3.01 * t]

    configuration = kite.Configuration(
        divisions=[NX, NY],
        length=[LX, LY],
        boundaries=["periodic", "periodic"],
        is_complex=True,              # B≠0 需要复数
        precision=1,
        spectrum_range=spectrum_range
    )

    calculation = kite.Calculation(configuration)
    calculation.conductivity_dc(
        direction='xy',
        num_points=E_POINTS,
        num_moments=M,
        num_random=rs,
        num_disorder=1,
        temperature=T_K
    )

    modification = kite.Modification(magnetic_field=B_field)

    print(f"\n{'='*60}")
    print(f"TK4: B={B_field}T, M={M}, rs={rs}, T={T_K}K")
    print(f"  Supercell: {LX}×{LY}, DD: {NX}×{NY}")
    print(f"  Energy: [{E_MIN}, {E_MAX}] eV, {E_POINTS} points")
    print(f"{'='*60}")

    kite.config_system(lattice, configuration, calculation,
                       modification=modification, filename=output_h5)

    # KITEx
    print(f"Running KITEx for B={B_field}T...")
    result = subprocess.run(
        [f'{KITE_BUILD}/KITEx', output_h5],
        capture_output=True, text=True,
        cwd=os.path.dirname(output_h5)
    )
    if result.returncode != 0:
        print(f"KITEx stderr:\n{result.stderr}")
        raise RuntimeError(f"KITEx failed (B={B_field}T)")

    # KITE-tools
    print(f"Running KITE-tools for B={B_field}T...")
    result = subprocess.run(
        [f'{KITE_BUILD}/KITE-tools', output_h5],
        capture_output=True, text=True,
        cwd=os.path.dirname(output_h5)
    )
    if result.returncode != 0:
        print(f"KITE-tools stderr:\n{result.stderr}")
        raise RuntimeError(f"KITE-tools failed (B={B_field}T)")

    # 输出文件 (condDC.dat: energy, sigma_xx, sigma_xy)
    h5_dir = os.path.dirname(output_h5)
    dat_file = os.path.join(h5_dir, 'condDC.dat')
    if not os.path.exists(dat_file):
        # try CWD
        if os.path.exists('condDC.dat'):
            os.rename('condDC.dat', dat_file)
        else:
            raise FileNotFoundError(f"Cannot find condDC.dat for B={B_field}T")

    return dat_file


def main():
    lattice = graphene_monolayer(t)

    all_data = {}

    for B in B_VALUES:
        B_str = f"{int(B)}"
        output_h5 = f'{OUTPUT_DIR}/kite_monolayer_B{B_str}_M{M}.h5'
        dat_file = run_kite_hall_B(lattice, B, output_h5)

        # 重命名保存
        target_txt = f'{OUTPUT_DIR}/kite_monolayer_B{B_str}_M{M}_hall.txt'
        os.rename(dat_file, target_txt)
        print(f"Saved: {target_txt}")

        # 加载数据
        data = np.loadtxt(target_txt)
        all_data[B] = {
            'energy': data[:, 0],
            'sigma_xx': data[:, 1],
            'sigma_xy': data[:, 2]
        }

        # 快速统计
        sxy = data[:, 2]
        print(f"  σ_xy: [{sxy.min():.4f}, {sxy.max():.4f}] e²/h")
        print(f"  σ_xy mean: {sxy.mean():.4f}, std: {sxy.std():.4f}")

    # ============================================================
    # 绘图: 3 B 值 σ_xy(E) 叠加
    # ============================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    colors = {50.0: 'blue', 100.0: 'green', 200.0: 'red'}

    # 主图: σ_xy 叠加
    ax = axes[0, 0]
    for B in B_VALUES:
        d = all_data[B]
        ax.plot(d['energy'], d['sigma_xy'], color=colors[B],
                linewidth=0.8, label=f'B={int(B)}T')
    # 标注预期 QHE 平台
    for plateau in [2, 6, 10]:
        ax.axhline(y=plateau, color='gray', linestyle=':', linewidth=0.5, alpha=0.5)
        ax.axhline(y=-plateau, color='gray', linestyle=':', linewidth=0.5, alpha=0.5)
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('σ_xy (e²/h)')
    ax.set_title(f'quantum-kite Monolayer Graphene Hall, M={M}, rs={rs}')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # 各 B 值子图: σ_xx + σ_xy
    for i, B in enumerate(B_VALUES):
        ax = axes.flat[i + 1]
        d = all_data[B]
        ax.plot(d['energy'], d['sigma_xy'], 'b-', linewidth=0.8, label='σ_xy')
        ax_twin = ax.twinx()
        ax_twin.plot(d['energy'], d['sigma_xx'], 'r-', linewidth=0.5, alpha=0.6, label='σ_xx')
        ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
        for plateau in [2, 6, 10]:
            ax.axhline(y=plateau, color='gray', linestyle=':', linewidth=0.3, alpha=0.4)
            ax.axhline(y=-plateau, color='gray', linestyle=':', linewidth=0.3, alpha=0.4)
        ax.set_xlabel('Energy (eV)')
        ax.set_ylabel('σ_xy (e²/h)')
        ax.set_title(f'B={int(B)}T')
        ax.grid(True, alpha=0.3)
        ax.legend(loc='upper left')
        ax_twin.legend(loc='upper right')

    plt.tight_layout()
    fig_path = f'{FIG_DIR}/hall_monolayer_Bscan_M{M}.png'
    fig.savefig(fig_path, dpi=150, bbox_inches='tight')
    print(f"\nFigure saved: {fig_path}")
    plt.close()


if __name__ == '__main__':
    main()
