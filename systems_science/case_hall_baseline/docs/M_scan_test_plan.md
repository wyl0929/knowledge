<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-21 03:21:45
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-21 03:21:59
 * @FilePath     : /MG/docs/sigma/M_scan_test_plan.md
 * @Description  :
-->
<!--
Subfield: tbplas 电导率计算方法
Document: Kubo-Bastin M 发散测试方案
Parent: 02_kubo_bastin_deep_dive.md
Created date: 2026-06-21
-->

# Kubo-Bastin Hall M 发散测试方案 — 单层石墨烯

> **状态**: ✅ 已完成（2026-06-21，log AI:0621_0324）
> **父计划**: `sigma/plan.md`（ABC trilayer QHE 复现）
> **归档说明**: 本 plan 已执行完毕并移入 `archive/`，实际结果以 `../../log.md` AI:0621_0324 为准。

> 目标：系统表征 `dckb_num_kernel` (M) 增大时 Hall 电导率从信号 → 噪声 → NaN 的完整演化轨迹。
> 项目路径：`/home/wyl/project/MG/`
> 环境：`conda activate tbplas-alpha`（或 `tbplas`）

---

## 1. 测试矩阵

### 1.1 核心扫描参数

> **⚠️ 本节的"预期行为"基于旧 rescale 假设（2026-06-21 初版）。**
> 实测结果（`../../log.md` AI:0621_0324）已证伪以下预测：
> M=1024 在 rescale=-1 下 NaN=0, exit 0。
> RMS 增长模式为线性（非指数），M=256 仍为最优平衡点。
> **以下表格保留为历史记录，实际结果以 log 为准。**

固定一切参数，仅变化 M（`dckb_num_kernel`）。基于此前实测（`tbplas-internals.md` §12），预期行为分为三个区：

| M 区段 | 预期行为 | 说明 |
|:---:|------|------|
| 64–256 | 信号逐渐增强，噪声可接受 | "可用区" |
| 384–512 | 噪声指数增长，物理信号被淹没 | "发散区" |
| 1024+ | **全 NaN** | "崩溃区" |

### 1.2 推荐 YAML 配置

在 `/home/wyl/project/MG/configs/` 下创建以下配置文件：

#### `hall_M064.yaml` → `hall_M128.yaml` → ... → `hall_M2048.yaml`

只需修改 `hall.dckb_num_kernel` 和 `model.tag` 字段：

```yaml
# ============================================================================
# Hall M 扫描配置 — 单层石墨烯 Kubo-Bastin 收敛性测试
# ============================================================================
calc_type: "hall"
solver_type: "tbpm"

model:
  num: 1                          # 单层 graphene
  delta: 0.0                      # 无偏压（单层不需要）
  pbc: [true, true, false]
  B_values: [100.0]               # 强磁场以分辨 LL（对标 speedtest / Yuan 2016）
  gauge: 0
  tag: "M064"                     # ← 每文件改此标签（M128, M256, ...）

tbpm:
  rescale: -1                     # auto-detect
  rescale_center: 0.0
  m: 256                          # 超胞大小（此前验证 m=256 最优）
  rs: 8                           # 8 个随机样本平均
  ts: 64                          # Hall 计算不依赖 ts
  num_spin: 2                     # 含自旋简并（对标 speedtest）
  algo: "cpu"                     # Kubo-Bastin 不区分 cpu/cpu_fast（同后端）
  temperature: 10.0               # 低温（对标 García 2015 / speedtest）

hall:
  dckb_component: 2               # XY (Hall)，亦可单独测试 XX (component=1)
  dimension: 2
  dckb_energies:
    min: -1.5                     # 覆盖低能 LL 平台区
    max: 1.5
    num: 1200                     # 1.5 meV 步长
  dckb_unit: "h"                  # e²/h
  dckb_num_kernel: 64             # ← 每文件改此值
  dckb_num_integ_steps: null      # 使用 tbplas 默认 2048
```

### 1.3 完整文件列表（8 个 YAML + 母配置）

```bash
cd /home/wyl/project/MG/configs

# 生成母配置（不变参数）
cat > hall_M_base.yaml << 'YAML'
calc_type: "hall"
solver_type: "tbpm"
model:
  num: 1
  delta: 0.0
  pbc: [true, true, false]
  B_values: [100.0]
  gauge: 0
tbpm:
  rescale: -1
  rescale_center: 0.0
  m: 256
  rs: 8
  ts: 64
  num_spin: 2
  algo: "cpu"
  temperature: 10.0
hall:
  dckb_component: 2
  dimension: 2
  dckb_energies:
    min: -1.5
    max: 1.5
    num: 1200
  dckb_unit: "h"
  dckb_num_integ_steps: null
YAML

# 为每个 M 值生成独立配置
for M in 64 128 256 384 512 768 1024 2048; do
  cp hall_M_base.yaml "hall_M${M}.yaml"
  # 用 Python 修改 tag 和 dckb_num_kernel
  python3 -c "
import re
with open('hall_M${M}.yaml', 'r') as f:
    text = f.read()
text = text.replace('  tag: \"\"', '  tag: \"M${M}\"')
text = re.sub(r'dckb_num_kernel:.*', 'dckb_num_kernel: ${M}', text)
with open('hall_M${M}.yaml', 'w') as f:
    f.write(text)
print(f'Created hall_M${M}.yaml')
"
done

rm hall_M_base.yaml
echo "Done. Created 8 config files."
```

### 1.4 推荐提交脚本

使用 `/home/wyl/project/MG/slurm/slm_single.sh`（单节点，纯 Python），或 `slm.sh`（多节点 MPI）：

```bash
# 批量提交所有 M 扫描
cd /home/wyl/project/MG
for M in 64 128 256 384 512 768 1024 2048; do
  sbatch --job-name=hall_M${M} slurm/slm_single.sh
done
```

> **注意**：slm.sh 中 CONFIG_FILE 路径为 `/home/ylwang/scratch/MG/configs/${SLURM_JOB_NAME}.yaml`。如果项目路径不同，需修改 `slm_single.sh` 中的路径，或直接改 slm.sh 的 CONFIG_FILE 变量。

---

## 2. 结果分析方案

### 2.1 数据文件格式

每次运行在 `runs/MMDD/` 目录下生成：

```
runs/0621/
  hall_ABC_d0.000_M064_B100.yaml      # 运行时配置存档
  hall_ABC_d0.000_M064_B100.dat       # 原始数据 (eng, sigma_xy)
  hall_ABC_d0.000_M064_B100.png       # 自动生成的图
  slurm-XXXXX.out                      # SLURM 日志
```

### 2.2 分析脚本

在 `/home/wyl/project/MG/test/` 下创建 `analyze_M_scan.py`：

```python
"""分析 Kubo-Bastin M 扫描结果 — 信噪比 vs M"""
import numpy as np
import matplotlib.pyplot as plt
import os
import re

# ── 配置 ──
RUNS_DIR = "../runs/0621"  # 修改为实际日期
PREFIX = "hall_ABC_d0.000"
M_VALUES = [64, 128, 256, 384, 512, 768, 1024, 2048]

# ── 读取数据 ──
def read_hall_data(filename):
    data = np.genfromtxt(filename, skip_header=1)
    eng = data[:, 0]
    sigma = data[:, 1]
    return eng, sigma

# ── 计算信噪比指标 ──
def compute_metrics(eng, sigma):
    """计算 RMS、NaN 比例、窗口内 σ_xy 均值"""
    # NaN 比例
    nan_ratio = np.sum(np.isnan(sigma)) / len(sigma)

    # 将 nan 暂时用 0 填充用于后续分析
    sigma_clean = np.where(np.isnan(sigma), 0.0, sigma)

    # 低能窗口 [-0.5, 0.5] eV 的 RMS（预期 QHE 平台区）
    mask_low = (eng >= -0.5) & (eng <= 0.5)
    rms_low = np.sqrt(np.mean(sigma_clean[mask_low] ** 2))

    # 全窗口 RMS
    rms_full = np.sqrt(np.mean(sigma_clean ** 2))

    return {
        "nan_ratio": nan_ratio,
        "rms_low": rms_low,
        "rms_full": rms_full,
    }

# ── 主分析 ──
results = []
for M in M_VALUES:
    filename = os.path.join(RUNS_DIR, f"{PREFIX}_M{M}_B100.dat")
    if not os.path.exists(filename):
        print(f"  [SKIP] M={M}: file not found")
        results.append({"M": M, "nan_ratio": 1.0, "rms_low": np.nan, "rms_full": np.nan})
        continue

    eng, sigma = read_hall_data(filename)
    metrics = compute_metrics(eng, sigma)
    metrics["M"] = M
    results.append(metrics)
    print(f"  M={M:4d}: nan={metrics['nan_ratio']:.3f}  "
          f"rms_low={metrics['rms_low']:.3f}  rms_full={metrics['rms_full']:.3f}")

# ── 汇总表 ──
print("\n┌──────┬──────────┬──────────┬──────────┐")
print("│  M   │ NaN 比例 │ RMS low  │ RMS full │")
print("├──────┼──────────┼──────────┼──────────┤")
for r in results:
    print(f"│ {r['M']:4d} │  {r['nan_ratio']:.4f}  │ "
          f"{r['rms_low']:8.4f} │ {r['rms_full']:8.4f} │")
print("└──────┴──────────┴──────────┴──────────┘")

# ── 可视化 ──
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# 子图 1: 各 M 的 σ_xy 叠加
ax = axes[0]
for M in [64, 128, 256, 384, 512]:
    filename = os.path.join(RUNS_DIR, f"{PREFIX}_M{M}_B100.dat")
    if os.path.exists(filename):
        eng, sigma = read_hall_data(filename)
        ax.plot(eng, sigma, lw=0.5, alpha=0.7, label=f"M={M}")

# 标注预期 QHE 平台值（单层 graphene: ±2, ±6, ±10 e²/h）
for plateau in [2, 6, 10, -2, -6, -10]:
    ax.axhline(y=plateau, color='gray', ls='--', lw=0.5, alpha=0.3)

ax.set_xlabel("Chemical Potential μ (eV)")
ax.set_ylabel("σ_xy (e²/h)")
ax.set_title("Kubo-Bastin Hall Conductivity — M Scan (monolayer graphene, B=100T)")
ax.set_xlim(-1.0, 1.0)
ax.legend(ncol=2, fontsize=8)
ax.grid(alpha=0.2)

# 子图 2: RMS vs M（对数 y 轴）
ax = axes[1]
M_arr = [r["M"] for r in results if r["nan_ratio"] < 1.0]
rms_arr = [r["rms_low"] for r in results if r["nan_ratio"] < 1.0]
ax.semilogy(M_arr, rms_arr, 'o-', markersize=8, color='#d62728')
ax.axvline(x=512, color='red', ls='--', lw=1, alpha=0.5, label='≈稳定上限 (512)')
ax.set_xlabel("M (dckb_num_kernel)")
ax.set_ylabel("RMS σ_xy (e²/h) [log scale]")
ax.set_title("Noise Level vs M (lower E window [-0.5, 0.5] eV)")
ax.legend()
ax.grid(alpha=0.2)

fig.tight_layout()
fig.savefig(os.path.join(RUNS_DIR, "M_scan_summary.png"), dpi=200)
print(f"\nSaved to {RUNS_DIR}/M_scan_summary.png")
```

### 2.3 预期输出解读

| M | NaN 比例 | RMS (低能) | 定性判断 |
|:---:|:---:|:---:|------|
| 64 | 0 | ~0.03 | 欠分辨，信号弱 |
| 128 | 0 | ~0.05 | 信号初现 |
| 256 | 0 | ~0.3 | **最优平衡** |
| 384 | 0 | ~1.5 | 开始发散 |
| 512 | 0 | ~3.0 | 噪声量级 ≈ 预期物理值 |
| 768 | ? | ? | 边界区（可能部分 NaN） |
| 1024+ | 1.0 | NaN | **全崩溃** |

---

## 3. 补充测试（可选）

### 3.1 B 场依赖

```yaml
model:
  B_values: [20, 50, 100, 150]  # 扫描不同磁场
```

预期：B 越大 LL 间距越大 → 低 M 更易分辨。但也需注意 PBC 下磁通量子化条件。

### 3.2 m 依赖

```yaml
tbpm:
  m: 128                         # 较小超胞
```

预期：m 越小有限尺寸效应越大，但 Kubo-Bastin 噪声主要来自 M，m 的影响是次要的。

### 3.3 XX 分量（纵向）

```yaml
hall:
  dckb_component: 1               # σ_xx
```

预期：σ_xx 在带隙内应趋于 0（绝缘），在 LL 跃迁处取峰值。M 不足时 σ_xx 整体偏大。

### 3.4 Anderson 无序测试

在 `model.py` 的 `expand_cell` 后添加 on-site 随机势：

```python
# 对 sample 的 on-site 能量加 Anderson 无序
import numpy as np
rng = np.random.default_rng(42)
disorder = 0.1 * 3.0  # γ = 0.1t, t≈3 eV for graphene
for i in range(len(sample._orb_eng)):
    sample._orb_eng[i] += rng.uniform(-disorder, disorder)
```

预期：无序展宽 LL → 降低 Gibbs 振荡 → M 较小即可看到平台结构（但平台宽度被展宽）。这是 García 2015 的关键技巧。

---

## 4. 预期时间估算

单层 graphene m=256 超胞 ≈ 393k 轨道，单次 `calc_hall_cond`（含 xx+xy 两次调用）的时间估算：

| M | 预计 wall time（单节点 32 核） |
|:---:|------|
| 64 | ~5 min |
| 128 | ~15 min |
| 256 | ~45 min |
| 512 | ~2 h |
| 1024 | ~6 h（但全 NaN） |

> 建议优先提交 M=64,128,256,384,512 五组，观测 NaN 出现后再决定是否提交 M≥1024。

---

## 5. 成功标准

1. ✅ 复现 M=256 为最优平衡点（RMS ~0.3 e²/h）
2. ✅ 观察到 M=384→512 噪声指数增长（RMS 从 1.5→3.0+）
3. ✅ 确认 M≥1024 全 NaN
4. ✅ （高级）复现 García 2015 Fig.2 的 M 收敛趋势——即使 M=256~512 仍可看到 $\sigma_{xy}$ 台阶结构的雏形（B=100T 下单层 graphene 应有 $\sigma_{xy} \approx \pm 2, \pm 6, \pm 10\ e^2/h$ 的量子化趋势）
