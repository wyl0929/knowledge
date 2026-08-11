#coding=utf-8

#Author       : Yulong Wang
#Date         : 2026-07-01 01:40:54
#LastEditors  : Yulong Wang
#LastEditTime : 2026-07-01 01:40:56
#FilePath     : /MG/test/TK5_plot_comparison.py
#Description  :

#!/usr/bin/env python3
"""
TK5: 双代码 σ_xy(E) 对比图 — tbplas vs quantum-kite
数据路径: runs/kite/phase2_cross_check/
输出路径: figures/kite/phase2/
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import os
import glob

# ============================================================
# 路径
# ============================================================
DATA_DIR = '/home/wyl/project/MG/runs/kite/phase2_cross_check'
FIG_DIR = '/home/wyl/project/MG/figures/kite/phase2'
os.makedirs(FIG_DIR, exist_ok=True)

# ============================================================
# M 值列表 (按现有数据)
# ============================================================
M_VALUES_TBPLAS = [64, 1024, 2048, 4096]   # M=256/512 待补
M_VALUES_KITE = [64, 256, 512, 1024, 2048, 4096]

# 颜色
C_TBPLAS = '#d62728'   # 红
C_KITE = '#1f77b4'     # 蓝

# ============================================================
# 数据加载
# ============================================================

def load_tbplas(M):
    """加载 tbplas 数据: E, σ_xy (2 columns, skip header)"""
    fpath = f'{DATA_DIR}/hall_none_d0.000_m64_M{M}_cross_B100.0.txt'
    if not os.path.exists(fpath):
        # 尝试零填充格式
        fpath = f'{DATA_DIR}/hall_none_d0.000_m64_M{M:04d}_cross_B100.0.txt'
    if not os.path.exists(fpath):
        return None, None
    data = np.loadtxt(fpath, skiprows=1)
    return data[:, 0], data[:, 1]


def load_kite(M):
    """加载 quantum-kite 数据: E, Re{σ}, Im{σ} (3 columns)"""
    fpath = f'{DATA_DIR}/kite_monolayer_B100_M{M}_hall.txt'
    if not os.path.exists(fpath):
        return None, None
    data = np.loadtxt(fpath)
    return data[:, 0], data[:, 1]  # E, Re{σ} (Col3 Im 恒为0)

# ============================================================
# 图 1: 双代码 σ_xy(E) 叠加对比 (每 M 值一个子图)
# ============================================================

# 确定公共 M 值
common_M = sorted(set(M_VALUES_TBPLAS) & set(M_VALUES_KITE))
all_kite_M = sorted(M_VALUES_KITE)

# 子图布局: 2 行 × 3 列 (6 个 kite M 值)
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
axes = axes.flatten()

for idx, M in enumerate(all_kite_M):
    ax = axes[idx]

    # kite data
    Ek, sk = load_kite(M)

    # tbplas data (if available)
    Et, st = load_tbplas(M)

    if sk is not None:
        ax.plot(Ek, sk, '-', color=C_KITE, linewidth=1.2, label='quantum-kite')
    if st is not None:
        ax.plot(Et, st, '--', color=C_TBPLAS, linewidth=1.2, label='tbplas')

    ax.axhline(y=0, color='gray', linestyle=':', alpha=0.5)

    # 标注预期 QHE 平台
    for plateau in [-6, -2, 2, 6]:
        ax.axhline(y=plateau, color='green', linestyle=':', alpha=0.25, linewidth=0.8)

    ax.set_title(f'M = {M}', fontsize=12, fontweight='bold')
    ax.set_xlabel('E (eV)', fontsize=9)
    ax.set_ylabel(r'$\sigma_{xy}$ ($e^2/h$)', fontsize=9)
    ax.legend(fontsize=7, loc='best')
    ax.grid(True, alpha=0.3)
    ax.tick_params(labelsize=8)

    # 自动 y 范围裁剪 (排除极端发散)
    if sk is not None:
        ydata = sk
        if st is not None:
            ydata = np.concatenate([ydata, st])
        y_abs = np.abs(ydata)
        y_p98 = np.percentile(y_abs, 98)
        if y_p98 < 10:
            ax.set_ylim(-8, 8)

# 隐藏空子图
for idx in range(len(all_kite_M), len(axes)):
    axes[idx].set_visible(False)

plt.suptitle('TK5: tbplas (dashed) vs quantum-kite (solid) — Monolayer Graphene Hall Conductivity',
             fontsize=14, fontweight='bold', y=1.01)
plt.tight_layout()
fig.savefig(f'{FIG_DIR}/sigma_xy_comparison_Mscan.png', dpi=150, bbox_inches='tight')
plt.close()
print(f'✅ 图1: sigma_xy_comparison_Mscan.png')

# ============================================================
# 图 2: 低 M 放大视图 (M=64, 256, 512 — 未发散区)
# ============================================================

low_M = [64, 256, 512]
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for idx, M in enumerate(low_M):
    ax = axes[idx]
    Ek, sk = load_kite(M)
    Et, st = load_tbplas(M)

    if sk is not None:
        ax.plot(Ek, sk, '-', color=C_KITE, linewidth=1.5, label='quantum-kite')
    if st is not None:
        ax.plot(Et, st, '--', color=C_TBPLAS, linewidth=1.5, label='tbplas')

    ax.axhline(y=0, color='gray', linestyle=':', alpha=0.5)
    for plateau in [-2, 2, 6]:
        ax.axhline(y=plateau, color='green', linestyle=':', alpha=0.3, linewidth=0.8)

    ax.set_title(f'M = {M}', fontsize=13, fontweight='bold')
    ax.set_xlabel('E (eV)', fontsize=10)
    ax.set_ylabel(r'$\sigma_{xy}$ ($e^2/h$)', fontsize=10)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.tick_params(labelsize=9)

plt.suptitle('TK5: Low-M Comparison — Clean QHE Regime', fontsize=14, fontweight='bold')
plt.tight_layout()
fig.savefig(f'{FIG_DIR}/sigma_xy_lowM_zoom.png', dpi=150, bbox_inches='tight')
plt.close()
print(f'✅ 图2: sigma_xy_lowM_zoom.png')

# ============================================================
# 图 3: RMS 差异 vs M (双代码在公共能量区间的差异)
# ============================================================

rms_data = []
M_list = []

for M in common_M:
    Ek, sk = load_kite(M)
    Et, st = load_tbplas(M)
    if sk is None or st is None:
        continue

    # 在公共能量区间插值: [-0.6, 1.0] eV
    E_common = np.linspace(-0.6, 1.0, 401)
    sk_interp = np.interp(E_common, Ek, sk)
    st_interp = np.interp(E_common, Et, st)

    rms = np.sqrt(np.mean((sk_interp - st_interp) ** 2))
    rms_data.append(rms)
    M_list.append(M)
    print(f'  M={M:4d}: RMS(tbplas - kite) = {rms:.4f}')

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(M_list, rms_data, 'o-', color='#9467bd', markersize=8, linewidth=1.5)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('M (Chebyshev moments)', fontsize=11)
ax.set_ylabel(r'RMS $\Delta\sigma_{xy}$ ($e^2/h$)', fontsize=11)
ax.set_title('TK5: RMS Difference vs M (tbplas − kite)', fontsize=13, fontweight='bold')
ax.grid(True, alpha=0.3, which='both')
for M, r in zip(M_list, rms_data):
    ax.annotate(f'{r:.2f}', (M, r), textcoords="offset points", xytext=(0, 10),
                ha='center', fontsize=8)
fig.tight_layout()
fig.savefig(f'{FIG_DIR}/rms_diff_vs_M.png', dpi=150, bbox_inches='tight')
plt.close()
print(f'✅ 图3: rms_diff_vs_M.png')

# ============================================================
# 图 4: kite-only M 扫描全览 (单图多曲线)
# ============================================================

fig, ax = plt.subplots(figsize=(12, 7))
colors = plt.cm.viridis(np.linspace(0, 1, len(all_kite_M)))

for idx, M in enumerate(all_kite_M):
    Ek, sk = load_kite(M)
    if sk is None:
        continue
    ax.plot(Ek, sk, '-', color=colors[idx], linewidth=1.0, alpha=0.8, label=f'M={M}')

ax.axhline(y=0, color='gray', linestyle=':', alpha=0.5)
for plateau in [-6, -2, 2, 6]:
    ax.axhline(y=plateau, color='green', linestyle=':', alpha=0.2, linewidth=0.8)

ax.set_xlabel('E (eV)', fontsize=11)
ax.set_ylabel(r'$\sigma_{xy}$ ($e^2/h$)', fontsize=11)
ax.set_title('TK5: quantum-kite M-Scan — Monolayer Graphene Hall Conductivity',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=8, loc='upper left', ncol=2)
ax.grid(True, alpha=0.3)
ax.tick_params(labelsize=9)

# 裁剪极端值以便观察
ax.set_ylim(-5, 8)

fig.tight_layout()
fig.savefig(f'{FIG_DIR}/kite_Mscan_overview.png', dpi=150, bbox_inches='tight')
plt.close()
print(f'✅ 图4: kite_Mscan_overview.png')

# ============================================================
# 图 5: tbplas-only M 扫描全览
# ============================================================

fig, ax = plt.subplots(figsize=(12, 7))
colors = plt.cm.plasma(np.linspace(0, 1, len(M_VALUES_TBPLAS)))

for idx, M in enumerate(M_VALUES_TBPLAS):
    Et, st = load_tbplas(M)
    if st is None:
        continue
    ax.plot(Et, st, '-', color=colors[idx], linewidth=1.0, alpha=0.8, label=f'M={M}')

ax.axhline(y=0, color='gray', linestyle=':', alpha=0.5)
for plateau in [-6, -2, 2, 6]:
    ax.axhline(y=plateau, color='green', linestyle=':', alpha=0.2, linewidth=0.8)

ax.set_xlabel('E (eV)', fontsize=11)
ax.set_ylabel(r'$\sigma_{xy}$ ($e^2/h$)', fontsize=11)
ax.set_title('TK5: tbplas M-Scan — Monolayer Graphene Hall Conductivity',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=8, loc='upper left')
ax.grid(True, alpha=0.3)
ax.tick_params(labelsize=9)

# 裁剪极端值
ax.set_ylim(-3, 3)

fig.tight_layout()
fig.savefig(f'{FIG_DIR}/tbplas_Mscan_overview.png', dpi=150, bbox_inches='tight')
plt.close()
print(f'✅ 图5: tbplas_Mscan_overview.png')

print(f'\n🏁 全部完成！图片保存在: {FIG_DIR}/')
