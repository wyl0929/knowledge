#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-07-01 00:56:41
#LastEditors  : Yulong Wang
#LastEditTime : 2026-07-01 00:56:41
#FilePath     : /MG/test/TK5_kite_hall_Mscan.py
#Description  :

#!/usr/bin/env python3
"""
TK5: quantum-kite 侧 M 扫描 — monolayer graphene σ_xy(E) at B≈100T
与 tbplas 交叉验证: M = 64, 256, 512, 1024, 2048, 4096

用法: python test/TK5_kite_hall_Mscan.py <M>
示例: python test/TK5_kite_hall_Mscan.py 256

Workflow: Python → HDF5 → KITEx → KITE-tools → condDC.dat
"""

import sys
import os
import subprocess
import numpy as np
import pybinding as pb
import kite

# ============================================================
# 路径配置 (集群路径, 可被环境变量覆盖)
# ============================================================
PROJECT_ROOT = os.environ.get('MG_ROOT', os.path.expanduser('~/scratch/MG'))
KITE_BUILD = os.environ.get('KITE_BUILD', os.path.expanduser('~/scratch/quantum-kite/build'))
OUTPUT_DIR = os.environ.get('KITE_OUTPUT',
    f'{PROJECT_ROOT}/runs/kite/phase2_cross_check')
FIG_DIR = f'{PROJECT_ROOT}/figures/kite/phase2'

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(FIG_DIR, exist_ok=True)

# ============================================================
# TB 参数 (与 MG/src/model.py 完全一致)
# ============================================================
t = 2.7         # nearest-neighbor hopping (eV)
a_cc = 0.142    # carbon-carbon distance (nm)
a_uc = 0.246    # unit cell length (nm)

# ============================================================
# 公共 KPM 参数 (与 tbplas 对齐)
# ============================================================
rs = 1                          # 随机向量数
T_K = 10.0                      # 温度 (K)
B_TARGET = 100.0                # 目标磁场 (T), quantum-kite 自动量子化
E_MIN, E_MAX = -0.6, 1.0        # eV (从 valence 到 conduction)
E_POINTS = 401

# ============================================================
# 超胞参数: lx=64 (匹配 tbplas m=64), ly=784 (B 量化要求)
# lx/ly 必须满足 TILE×divisions=16 的倍数约束: 64/16=4 ✓, 784/16=49 ✓
# B_min ≈ φ₀/(ly·A_uc) ≈ 78904/784 ≈ 100.6T → 1×100.6≈100.6T (target 100T, 0.6% off)
# 总原胞: 64×784 = 50,176 (tbplas: 64×64 = 4,096; 洁净体系 σ_xy 独立于尺寸)
# ============================================================
LX, LY = 64, 784
NX, NY = 2, 2

# 能带范围 (±3t = ±8.1 eV, 加安全余量)
SPECTRUM_RANGE = [-9.0, 9.0]


def graphene_monolayer(t_hop=t):
    """单层石墨烯 pybinding 晶格 (与 TK3/TK4 完全一致)"""
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


def run_kite_hall(lattice, B_field, M, output_h5):
    """运行 quantum-kite Hall 计算 (单 M, 单 B)"""
    configuration = kite.Configuration(
        divisions=[NX, NY],
        length=[LX, LY],
        boundaries=["periodic", "periodic"],
        is_complex=True,
        precision=1,               # double
        spectrum_range=SPECTRUM_RANGE
    )

    calculation = kite.Calculation(configuration)
    calculation.conductivity_dc(
        direction='xy',
        num_points=E_POINTS,
        num_moments=M,
        num_random=rs,
        num_disorder=1,            # 干净体系
        temperature=T_K
    )

    modification = kite.Modification(magnetic_field=B_field)

    print(f"\n{'='*60}")
    print(f"TK5 kite: B≈{B_field}T, M={M}, rs={rs}, T={T_K}K")
    print(f"  Supercell: {LX}×{LY}, DD: {NX}×{NY}")
    print(f"  Energy: [{E_MIN}, {E_MAX}] eV, {E_POINTS} points")
    print(f"  Spectrum: {SPECTRUM_RANGE} eV")
    print(f"{'='*60}")

    kite.config_system(lattice, configuration, calculation,
                       modification=modification, filename=output_h5)

    # ── KITEx ──
    print(f"[KITEx] M={M}...", flush=True)
    result = subprocess.run(
        [f'{KITE_BUILD}/KITEx', output_h5],
        capture_output=True, text=True,
        cwd=os.path.dirname(output_h5),
        timeout=3600               # 1h per M (M=4096 可能需要更久)
    )
    if result.returncode != 0:
        print(f"KITEx stdout:\n{result.stdout[-2000:]}")
        print(f"KITEx stderr:\n{result.stderr[-2000:]}")
        raise RuntimeError(f"KITEx failed (M={M}, B={B_field}T)")

    # ── KITE-tools ──
    print(f"[KITE-tools] M={M}...", flush=True)
    result = subprocess.run(
        [f'{KITE_BUILD}/KITE-tools', output_h5],
        capture_output=True, text=True,
        cwd=os.path.dirname(output_h5),
        timeout=600
    )
    if result.returncode != 0:
        print(f"KITE-tools stderr:\n{result.stderr[-2000:]}")
        raise RuntimeError(f"KITE-tools failed (M={M}, B={B_field}T)")

    # ── 定位输出 condDC.dat ──
    h5_dir = os.path.dirname(output_h5)
    dat_file = os.path.join(h5_dir, 'condDC.dat')
    if not os.path.exists(dat_file):
        if os.path.exists('condDC.dat'):
            os.rename('condDC.dat', dat_file)
        else:
            raise FileNotFoundError(f"Cannot find condDC.dat for M={M}")

    return dat_file


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <M>", file=sys.stderr)
        print(f"Example: python {sys.argv[0]} 256", file=sys.stderr)
        sys.exit(1)

    M = int(sys.argv[1])
    print(f"TK5 quantum-kite: M={M}, B_target={B_TARGET}T")

    lattice = graphene_monolayer(t)

    output_h5 = f'{OUTPUT_DIR}/kite_monolayer_B100_M{M}.h5'
    dat_file = run_kite_hall(lattice, B_TARGET, M, output_h5)

    # 重命名为更清晰的输出文件名
    target_txt = f'{OUTPUT_DIR}/kite_monolayer_B100_M{M}_hall.txt'
    os.rename(dat_file, target_txt)
    print(f"\n✅ Output saved: {target_txt}")

    # 打印前几行供冒烟检查
    with open(target_txt, 'r') as f:
        lines = f.readlines()[:5]
    print("First 5 lines:")
    for line in lines:
        print(f"  {line.rstrip()}")


if __name__ == '__main__':
    main()
