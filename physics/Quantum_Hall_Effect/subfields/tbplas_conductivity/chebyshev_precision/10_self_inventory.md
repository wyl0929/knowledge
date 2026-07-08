<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27 23:47:56
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-27 23:48:03
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/chebyshev_precision/10_self_inventory.md
 * @Description  :
-->
<!--
Field: 切比雪夫迭代浮点精度问题
Parent: tbplas_conductivity
Created date: 2026-06-27
-->

# 10 Self Inventory / 用户背景快照

Last updated: 2026-06-27

## 使用说明

本文件是当前子方向 field pack 使用的 profile 快照。继承自父级 `Quantum_Hall_Effect/10_self_inventory.md`（2026-06-10），并补充了 2026-06-22~27 期间与本子方向直接相关的新增资产。

## Profile source

- 父级快照：`../../10_self_inventory.md`（2026-06-10）
- 补充来源：Phase A–M 诊断过程中积累的工具和代码

## 与本子方向直接相关的资产

### 代码与工具

| 工具 / 代码 | 类型 | 位置 | 成熟度 | 备注 |
|---|---|---|---|---|
| gamma_mu_sim | simulation | `../gamma_mu_sim/` | active | Γ-μ 随机游走数值验证（Python） |
| t4_scan.py | simulation | `../gamma_mu_sim/src/t4_scan.py` | running | M 系统性扫描（6 kernel×method + float32） |
| tbplas C++ 源码 | code | `/home/wyl/tbplas/source/tbplas-cpp-a021ca8/sources/` | reference | Kubo-Bastin, KPM, Chebyshev 迭代实现 |
| kubo_bastin.h | header | `../kubo_bastin.h` | reference | C++ gamma_matrix() 实现参考 |

### 已完成的关键诊断

| 阶段 | 日期 | 内容 | 结论 |
|------|------|------|------|
| Phase A | 06-22 | Chebyshev 正交性（norm inflation） | ❌ 排除 |
| Phase B | 06-23 | Jackson 核退化 | ❌ 排除 |
| Phase C | 06-23 | 能谱边缘泄漏 | ❌ 排除 |
| Phase D | 06-24 | double 精度单次加法 | ❌ 排除（累积才是问题） |
| Phase θ | 06-24 | θ 积分奇异性 | ❌ 排除 |
| Phase Γ | 06-25 | Γ 矩阵计算精度 | ❌ 排除 |
| Phase μ | 06-25 | μ 矩阵 M 依赖性 | ❌ 排除 |
| Phase J | 06-25 | Jackson 核 M 依赖性 | ❌ 排除 |
| Phase bias | 06-26 | δμ 系统性偏差 | ❌ 排除（是零均值随机噪声） |
| **Phase M** | **06-27** | **随机游走假说封闭验证** | **✅ 确认根因** |

### Phase M 三项验证

| 子验证 | 内容 | 结果 |
|:---:|------|------|
| M1 | 噪声注入 ΔS = ΣΓ·η 验证 | ✅ dS_obs/dS_pred = 1.000±0.001, RMS ∝ σ^0.999 |
| M2 | 求和精度限制检测（f32 vs f64） | ✅ S_f32 ≈ S_f64, δμ 在 C++ KPM 迭代层产生 |
| M3 | Γ 加权确认 | ✅ 高 |Γ| 项主导 S |

### 方法能力矩阵

| 方法 | 熟练度 | 与本子方向的相关性 |
|------|:---:|------|
| KPM / Chebyshev 展开 | 深入 | 核心分析对象 |
| Kubo-Bastin 公式 | 深入 | 父级专长 |
| 浮点误差分析 | 熟练 | Phase M 核心方法 |
| Python 数值模拟 | 熟练 | gamma_mu_sim 实现 |
| C++ 源码追踪 | 熟练 | 噪声源定位 |
| mpmath 高精度基准 | 熟练 | reference.py |
| Kahan 补偿求和 | 熟练 | summation.py |

### 硬件与算力

- 本地：单机 Python 数值实验（gamma_mu_sim）
- 远程：SLURM 集群（h3clogin），用于 tbplas C++ 大规模计算
- 本子方向主要为本地 Python 分析，不依赖集群

## 缺失资源

| 缺失项 | 影响 | 优先级 |
|------|------|:---:|
| C++ quad precision KPM 实现 | 无法验证 M≥4096 精度修复方案 | P1 |
| 其他 KPM 库（如 GPAW/Siesta）的精度对比 | 无法判断是否为 tbplas 特有问题 | P2 |
| 已发表文献中关于 KPM 浮点精度的系统研究 | 无法确定是否已有已知解决方案 | P3 |
