#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-07-01 15:27:35
#LastEditors  : Yulong Wang
#LastEditTime : 2026-07-01 15:27:36
#FilePath     : /.agents/home/wyl/project/knowledge/systems_science/case_hall_baseline/scripts/TK2_band_compare_v2.py
#Description  :

#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-06-30 23:59:56
#LastEditors  : Yulong Wang
#LastEditTime : 2026-06-30 23:59:59
#FilePath     : /MG/test/TK2_band_compare_v2.py
#Description  :

#!/usr/bin/env python3
"""
TK2 Step 1.3 v2: monolayer graphene 能带对比 — 手动 Bloch 对角化方案
绕过 pybinding calc_bands 色散问题，直接从 hopping 构建 k 空间哈密顿量。
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eigh

# ============================================================
# TB 参数 (与 MG/src/model.py 一致)
# ============================================================
t = 2.7              # nearest-neighbor hopping (eV) = gamma0
a_cc = 0.142         # carbon-carbon distance (nm)
a_uc = 0.246         # unit cell length (nm) = sqrt(3) * a_cc

# 实空间晶格矢量
a1 = a_uc * np.array([1.0, 0.0])
a2 = a_uc * np.array([0.5, 0.5 * np.sqrt(3.0)])

# 倒格矢 (2π 约定)
b1 = 2 * np.pi * np.array([1.0, -1.0 / np.sqrt(3.0)]) / a_uc
b2 = 2 * np.pi * np.array([0.0, 2.0 / np.sqrt(3.0)]) / a_uc

# ============================================================
# 手动构建 k 空间哈密顿量 (2×2, A/B 子晶格)
# ============================================================
def hamiltonian_k(k1, k2, t_hop=t):
    """
    返回 2×2 k 空间哈密顿量。
    k1, k2: 倒格矢分量 (无单位, 在 b1, b2 基下)
    t_hop: nearest-neighbor hopping (eV)

    Graphene honeycomb:
    - 3 个 hopping: R = (0,0), (1,-1), (0,-1)
    - H_AB(k) = -t * [1 + e^{i(k1-k2)} + e^{-i k2}]
    """
    phase = 1.0 + np.exp(2j * np.pi * (k1 - k2)) + np.exp(-2j * np.pi * k2)
    h_ab = -t_hop * phase
    H = np.array([[0.0, h_ab],
                   [np.conj(h_ab), 0.0]], dtype=complex)
    return H

# ============================================================
# Γ-M-K-Γ 路径 (倒格矢基下的分数坐标)
# ============================================================
# Γ = (0, 0)
# M = (1/2, 0)    ← b1 方向中点
# K = (2/3, 1/3)  ← Dirac 点
# K'= (1/3, 2/3)  ← 另一个 Dirac 点

k_path_labels = ['Γ', 'M', 'K', 'Γ']
k_path_frac = [
    np.array([0.0, 0.0]),           # Γ
    np.array([0.5, 0.0]),           # M
    np.array([2.0/3.0, 1.0/3.0]),   # K
    np.array([0.0, 0.0]),           # Γ
]

# 每段采样点数
n_per_segment = 40
n_total = (len(k_path_frac) - 1) * n_per_segment

# ============================================================
# 计算能带
# ============================================================
k_dist = np.zeros(n_total)
energies = np.zeros((n_total, 2))

idx = 0
cum_dist = 0.0
for seg in range(len(k_path_frac) - 1):
    k_start = k_path_frac[seg]
    k_end = k_path_frac[seg + 1]
    for i in range(n_per_segment):
        t_frac = i / n_per_segment
        k = (1 - t_frac) * k_start + t_frac * k_end
        # 转换到绝对 k 坐标 (1/nm)
        k_abs = k[0] * b1 + k[1] * b2
        # 计算段内弧长
        if i > 0:
            k_prev = ((1 - (i-1)/n_per_segment) * k_start + ((i-1)/n_per_segment) * k_end)
            k_prev_abs = k_prev[0] * b1 + k_prev[1] * b2
            cum_dist += np.linalg.norm(k_abs - k_prev_abs)
        k_dist[idx] = cum_dist
        H = hamiltonian_k(k[0], k[1], t)
        evals, _ = eigh(H)
        energies[idx, :] = evals
        idx += 1

# ============================================================
# 加载 tbplas 参考能带
# ============================================================
tbplas_data = np.loadtxt('/home/wyl/project/MG/data/band/graphene_L1_band.dat')
k_tbplas = tbplas_data[:, 0]
bands_tbplas = tbplas_data[:, 1:]

# ============================================================
# 绘图
# ============================================================
import os
os.makedirs('/home/wyl/project/MG/figures/kite/phase1', exist_ok=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- 左面板: pybinding 等效模型 (手动 Bloch) ---
for i in range(2):
    ax1.plot(k_dist, energies[:, i], 'b-', lw=1.5)
ax1.set_title(f'quantum-kite 等效模型 (t={t} eV)\n手动 Bloch 对角化', fontsize=11)
ax1.set_ylabel('Energy (eV)')
ax1.set_xlabel('k-path')
ax1.axhline(0, color='gray', ls='--', lw=0.5)
# 标注高对称点
seg_boundaries = np.arange(len(k_path_frac)) * n_per_segment
seg_boundaries[-1] = n_total - 1
ax1.set_xticks([k_dist[b] for b in seg_boundaries])
ax1.set_xticklabels(k_path_labels)
for b in seg_boundaries[1:-1]:
    ax1.axvline(k_dist[b], color='gray', ls=':', lw=0.5)

# --- 右面板: tbplas (Slater-Koster) ---
for i in range(bands_tbplas.shape[1]):
    ax2.plot(k_tbplas, bands_tbplas[:, i], 'r-', lw=1.5)
ax2.set_title('tbplas (Slater-Koster, γ₀=2.7 eV)', fontsize=11)
ax2.set_xlabel('k-path')
ax2.axhline(0, color='gray', ls='--', lw=0.5)
ax2.set_xticks([k_tbplas[0], k_tbplas[n_total//3], k_tbplas[2*n_total//3], k_tbplas[-1]])
ax2.set_xticklabels(k_path_labels)

plt.suptitle('Monolayer Graphene Band Structure: quantum-kite vs tbplas', fontsize=14)
plt.tight_layout()
outpath = '/home/wyl/project/MG/figures/kite/phase1/band_monolayer_kite_vs_tbplas.png'
plt.savefig(outpath, dpi=150)
print(f'✅ 能带对比图已保存: {outpath}')

# ============================================================
# 对比分析
# ============================================================
# K 点位置 (第 2 段末尾, 即 2*n_per_segment - 1)
k_idx = 2 * n_per_segment - 1
e_k_kite = np.sort(energies[k_idx, :])
# tbplas K 点 (索引 80 ≈ 2/3 路径)
e_k_tbplas = np.sort(bands_tbplas[80, :])

print(f'\n=== K 点 Dirac 锥对比 ===')
print(f'quantum-kite (NN t=2.7):  E_K = {e_k_kite}')
print(f'tbplas (SK γ₀=2.7):       E_K = {e_k_tbplas}')
print(f'能量差:                   ΔE = {np.abs(e_k_kite - e_k_tbplas)}')
print(f'Dirac 锥位置偏差:          {np.mean(np.abs(e_k_kite - e_k_tbplas)):.1f} meV')

# Γ 点对比
e_g_kite = np.sort(energies[0, :])
e_g_tbplas = np.sort(bands_tbplas[0, :])
print(f'\n=== Γ 点对比 ===')
print(f'quantum-kite: E_Γ = {e_g_kite}')
print(f'tbplas:       E_Γ = {e_g_tbplas}')

# ============================================================
# 保存数据
# ============================================================
os.makedirs('/home/wyl/project/MG/runs/kite/phase1_install', exist_ok=True)

# 保存 quantum-kite 能带数据
pb_band_file = '/home/wyl/project/MG/runs/kite/phase1_install/kite_L1_band.dat'
header = f'# quantum-kite monolayer graphene band, t={t} eV, a_cc={a_cc} nm, a_uc={a_uc} nm\n'
header += '# k_dist(1/nm)  band_1(eV)  band_2(eV)  (Γ-M-K-Γ path)'
np.savetxt(pb_band_file,
           np.column_stack([k_dist, energies[:, 0], energies[:, 1]]),
           header=header, fmt='%.8e')
print(f'\n✅ quantum-kite 能带数据已保存: {pb_band_file}')

# 保存对比数据 (差值)
diff_file = '/home/wyl/project/MG/runs/kite/phase1_install/band_diff.txt'
# 插值 quantum-kite 到 tbplas 的 k 网格
e_kite_interp = np.zeros((len(k_tbplas), 2))
for band in range(2):
    e_kite_interp[:, band] = np.interp(k_tbplas, k_dist, energies[:, band])
diff_header = '# Band difference: |E_kite - E_tbplas| (eV)\n'
diff_header += '# k_dist  diff_band1  diff_band2'
diff = np.abs(e_kite_interp - bands_tbplas)
np.savetxt(diff_file,
           np.column_stack([k_tbplas, diff[:, 0], diff[:, 1]]),
           header=diff_header, fmt='%.8e')
print(f'✅ 能带差值数据已保存: {diff_file}')
print(f'   平均差值: band1={np.mean(diff[:,0]):.3f} eV, band2={np.mean(diff[:,1]):.3f} eV')
