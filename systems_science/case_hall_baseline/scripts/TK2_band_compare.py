#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-30 23:58:07
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-30 23:58:09
#FilePath     : /MG/test/test/TK2_band_compare.py
#Description  :

#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-30 23:44:18
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-30 23:44:20
#FilePath     : /MG/test/TK2_band_compare.py
#Description  :

#!/usr/bin/env python3
"""
TK2 Step 1.3: quantum-kite/pybinding monolayer graphene 能带 vs tbplas 对比
使用 pybinding + kite 构建与 tbplas 相同 TB 参数的单层石墨烯模型。
"""

import sys
sys.path.insert(0, '/home/wyl/quantum-kite')

import numpy as np
import pybinding as pb
import kite
import matplotlib.pyplot as plt

# ============================================================
# TB 参数 (与 MG/src/model.py 一致)
# ============================================================
t = 2.7         # nearest-neighbor hopping (eV), = gamma0
a_cc = 0.142    # carbon-carbon distance (nm)
a_uc = 0.246    # unit cell length (nm) = sqrt(3) * a_cc

# ============================================================
# 构建 monolayer graphene 晶格 (pybinding)
# ============================================================
def graphene_monolayer(t_hop=t):
    """返回与 tbplas 等价 TB 参数的单层石墨烯 pybinding 晶格"""
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

# ============================================================
# 能带计算 (pybinding 自带 solver)
# ============================================================
def calc_band_pybinding(lat, k_points, num_points=121):
    """用 pybinding 精确对角化计算能带"""
    model = pb.Model(lat)
    # k_points: list of (kx, ky) arrays
    # 计算路径总长度用于 step 参数
    total_len = sum(np.linalg.norm(k_points[i+1] - k_points[i])
                    for i in range(len(k_points)-1))
    step = total_len / (num_points - 1)
    solver = pb.solver.lapack(model)
    bands = solver.calc_bands(*k_points, step=step)
    return bands

# ============================================================
# Γ-M-K-Γ 路径定义
# ============================================================
# 倒格矢 (pybinding 内部使用)
# b1 = 2π/a_uc * (1, -1/√3)
# b2 = 2π/a_uc * (0, 2/√3)
#
# Γ = (0, 0)
# M = (1/2, 0) in reciprocal lattice units
# K = (2/3, 1/3) in reciprocal lattice units
def make_k_path_graphene():
    """生成 Γ-M-K-Γ 路径的 k 点坐标 (直角坐标, 1/nm)"""
    # 倒格矢长度 |b1| = 4π/(√3 * a_uc)
    # Γ=(0,0), M, K 的直角坐标
    a = a_uc
    b_mag = 4*np.pi / (np.sqrt(3) * a)  # 倒格矢长度
    # M 点在 b1 方向的中点
    M = np.array([b_mag/2, 0])
    # K 点: 2/3*b1 + 1/3*b2, b1=(b_mag,0), b2=(b_mag/2, b_mag*√3/2)
    K = np.array([2/3*b_mag + 1/3*b_mag/2, 1/3*b_mag*np.sqrt(3)/2])

    return [np.array([0, 0]), M, K, np.array([0, 0])]

# ============================================================
# 主程序
# ============================================================
if __name__ == "__main__":
    import os
    os.makedirs('/home/wyl/project/MG/figures/kite/phase1', exist_ok=True)

    # 1. 构建模型
    lat = graphene_monolayer(t)

    # 2. pybinding 能带
    k_path = make_k_path_graphene()
    bands_pb = calc_band_pybinding(lat, k_path, num_points=121)

    # 3. 加载 tbplas 参考能带
    tbplas_data = np.loadtxt('/home/wyl/project/MG/data/band/graphene_L1_band.dat')
    k_tbplas = tbplas_data[:, 0]
    bands_tbplas = tbplas_data[:, 1:]  # columns: band1, band2

    # 4. 绘图对比
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # pybinding 能带
    k_pb = np.arange(len(bands_pb.k_path))
    n_pts = len(k_pb)
    for i in range(bands_pb.num_bands):
        ax1.plot(k_pb, bands_pb.energy[:, i], 'b-', lw=1)
    ax1.set_title(f'pybinding (t={t} eV)')
    ax1.set_ylabel('Energy (eV)')
    ax1.set_xlabel('k-path')
    ax1.axhline(0, color='gray', ls='--', lw=0.5)
    ax1.set_xticks([0, n_pts//3, 2*n_pts//3, n_pts-1])
    ax1.set_xticklabels(['Γ', 'M', 'K', 'Γ'])

    # tbplas 能带
    for i in range(bands_tbplas.shape[1]):
        ax2.plot(k_tbplas, bands_tbplas[:, i], 'r-', lw=1)
    ax2.set_title('tbplas (SK, γ₀=2.7 eV)')
    ax2.set_xlabel('k-path')
    ax2.axhline(0, color='gray', ls='--', lw=0.5)
    n_tb = len(k_tbplas)
    ax2.set_xticks([k_tbplas[0], k_tbplas[n_tb//3], k_tbplas[2*n_tb//3], k_tbplas[-1]])
    ax2.set_xticklabels(['Γ', 'M', 'K', 'Γ'])

    plt.suptitle('Monolayer Graphene Band Structure: pybinding vs tbplas', fontsize=14)
    plt.tight_layout()
    outpath = '/home/wyl/project/MG/figures/kite/phase1/band_monolayer_kite_vs_tbplas.png'
    plt.savefig(outpath, dpi=150)
    print(f'Band comparison saved to: {outpath}')

    # 5. K 点 Dirac 锥位置对比
    print(f'\n=== K-point Dirac cone comparison ===')
    n_pb = bands_pb.energy.shape[0]
    print(f'pybinding bands at K (idx={2*n_pb//3}): {bands_pb.energy[2*n_pb//3, :]}')
    print(f'tbplas bands at K (idx={2*len(k_tbplas)//3}):   {bands_tbplas[2*len(k_tbplas)//3, :]}')

    # 6. 保存 pybinding 能带数据
    pb_band_file = '/home/wyl/project/MG/runs/kite/phase1_install/pybinding_L1_band.dat'
    header = '# pybinding monolayer graphene band, t=2.7 eV, a_cc=0.142 nm\n'
    header += '# k_idx  band_1  band_2'
    np.savetxt(pb_band_file,
               np.column_stack([np.arange(len(bands_pb.k_path)),
                                bands_pb.energy[:, 0], bands_pb.energy[:, 1]]),
               header=header)
    print(f'pybinding band data saved to: {pb_band_file}')
