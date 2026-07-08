<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27 22:43:38
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-27 22:43:40
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/docs/plan.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-27
 * @FilePath     : gamma_mu_sim/docs/plan.md
 * @Description  : Γ-μ 随机游走数值模拟 — 前期技术设计计划书
-->

# Γ-μ 随机游走数值模拟 — 计划书

> **状态**: � 部分修订（§8.3 核模型假设已被 T5 证伪）
> **创建日期**: 2026-06-27
> **最后修订**: 2026-06-28 (rev 3)
> **最后修订原因**: T5 实验证伪核加权消除随机游走假设；§8.3 追加证伪警告

---

## 1. 项目概述与物理目标

### 1.1 背景

TBPLaS Kubo-Bastin Hall 电导率计算的核心表达式为：

$$\sigma_{xy} \propto \int_0^\pi d\theta \frac{f(\cos\theta)}{\sin^3\theta} \sum_{m,n=0}^{M-1} \Gamma_{mn}(\theta) \cdot \mu_{mn}$$

VBL Phase A–L 全链路诊断（2026-06-25 完成）确认了 $\sigma_{xy}$ 在 $M \gtrsim 3072$ 时基线偏移的最终根因：

$$\underbrace{\sum_{m,n=0}^{M-1} \Gamma_{mn} (\mu_{mn}^{\text{true}} + \delta\mu_{mn})}_{\text{数值}}$$

其中：
- $\|\Gamma_{mn}\| \sim O(\max(m,n))$ — 线性增长（Phase G 确认：$\max\|\Gamma\| \propto M^{1.001}$）
- $\mu_{mn}^{\text{true}} \sim O(1)$ — 干净体系振荡不衰减
- $\delta\mu_{mn}$ — 零均值随机噪声（Phase L: pos_frac=0.4997）
- 累加项数 $N \sim M^2$，随机游走 RMS $\sim O(\sqrt{N}\cdot\varepsilon_{\text{mach}})$

在 $M=4096$（$N \approx 1.7\times 10^7$）下，RMS 累积 $\approx 9\times 10^{-13}$，与物理信号 $\sim 2\ e^2/h$ 相比在 double 精度下不可忽略。

### 1.2 项目目标

**在纯 Python 环境下，用合成 $\Gamma$ 和 $\mu$ 矩阵（量级匹配真实物理矩阵），定量验证随机游走累积与 $M$ 的标度关系。**

具体目标：
1. 构造量级逼真的合成 $\Gamma_{mn}(\theta)$ 和 $\mu_{mn}$ 矩阵
2. 实现两种求和策略（顺序累加、Kahan 补偿）+ mpmath 高精度参考
3. 对比三种 $\mu$ 物理模型：干净振荡（无核）、Jackson 核加权、Lorentz 核加权
4. 扫描 $M = 64 \to 8192$，测量累积误差 vs $M$ 的标度律
5. 验证 RMS $\propto \sqrt{N}$ 的随机游走预测
6. 评估核加权对条件收敛的改善效果

### 1.3 物理图景

```
Γ 矩阵 (解析核)          μ 矩阵 (Chebyshev 矩)        双重求和
┌─────────────────┐     ┌─────────────────┐     ┌──────────────────────┐
│ ∼ O(max(m,n))   │     │ ∼ O(1) 振荡     │     │ 信号: ~O(1)          │
│ 含 cos/sin 振荡  │  ×  │ + ε_mach 噪声   │  =  │ 噪声: ~O(√N·ε)       │
│ M×M 复矩阵      │     │ M×M 实矩阵      │     │ N = M²               │
└─────────────────┘     └─────────────────┘     └──────────────────────┘
```

---

## 2. 计算步骤方案

```
1. 环境配置 → 2. Γ 矩阵合成 → 3. μ 矩阵合成 → 4. 双重求和计算
                                            → 5. 精度基准（mpmath 高精度）
   → 6. M 系统性扫描 → 7. 误差标度分析 → 8. 可视化与报告
```

| 步骤 | 输入 | 核心操作 | 输出 |
|:---:|------|------|------|
| **1. 环境配置** | — | conda env, numpy, scipy, mpmath, matplotlib | 可运行环境 |
| **2. Γ 矩阵合成** | M, θ | 按真实公式 $\Gamma_{mn} = \cos(m\theta)(\cos\theta - in\sin\theta)e^{in\theta} + \text{c.c.}$ 生成 | `gamma_M{N}_theta{N}.npy` |
| **3. μ 矩阵合成** | M, noise_level, kernel_model | 合成 $\mu_{mn} = g_m g_n \cdot \mu_{mn}^{\text{raw}} + \delta\mu_{mn}$，支持 clean / Jackson / Lorentz 三种核模型 | `mu_M{N}_model.npy` |
| **4. 双重求和** | gamma, mu, method | 实现 sequential / Kahan 两种累加策略 | 标量 sum |
| **5. 精度基准** | M, θ, gamma, mu | mpmath 高精度 (50–100 digits) 双重求和作为 ground truth | 参考值 $S_{\text{ref}}$ |
| **6. M 扫描** | M_list, θ_grid, n_trials | 对每个 M 多次测量（随机噪声种子） | 误差分布 (mean, std) |
| **7. 误差标度分析** | M_list, error_stats | 拟合 $\log(\text{RMS}) = \alpha\log(M) + \beta$，检验 $\alpha \approx 1$ | 标度指数 $\alpha$ |

> **⚠️ α 预期值已修订 (2026-06-27)。**
> T4 实验 (log AI:0627_2345) 实测 α≈2.08，非 1.0。
> 原因：Γ 元素 ∝ M，使单项噪声 ∝ M·ε，M² 项的随机游走 RMS ∝ √(M²) × M·ε = M²·ε → α≈2。
> 以下 §7 中"检验 α≈1"为历史预期，实际目标应为 α≈2。
| **8. 可视化与报告** | 所有结果 | 误差 vs M 图、标度律图、方法对比图 | figures/ + report |

---

## 3. 系统架构规划

### 3.1 模块划分

| 模块 | 文件 | 职责 |
|------|------|------|
| **主入口** | `main.py` | 加载配置，调度 M 扫描全流程，输出汇总 |
| **Γ 矩阵生成器** | `gamma_matrix.py` | 按真实解析公式生成 $\Gamma_{mn}(\theta)$，支持单 θ 和 θ 网格 |
| **μ 矩阵生成器** | `mu_matrix.py` | 合成三种核加权模型的 $\mu_{mn}$：clean（无核）/ Jackson 核 / Lorentz 核，叠加 $\varepsilon_{\text{mach}}$ 噪声 |
| **求和引擎** | `summation.py` | 实现 sequential / Kahan 两种求和策略，统一接口 `sum_double(gamma, mu, method)` |
| **精度基准** | `reference.py` | 用 mpmath 高精度计算 ground truth |
| **误差分析** | `analysis.py` | 标度律拟合、RMS 统计、收敛性检验 |
| **可视化** | `visualize.py` | 误差 vs M 图、标度律图、方法对比热图 |
| **配置** | `config.py` | 参数定义、默认值、M 扫描网格 |

### 3.2 模块关系图

```
main.py
  ├── config.py          ← 参数加载
  ├── gamma_matrix.py    ← 生成 Γ(M, θ)
  ├── mu_matrix.py       ← 生成 μ(M, model, noise)
  ├── summation.py       ← 求和 (gamma, mu, method) → S
  ├── reference.py       ← 高精度基准 S_ref
  ├── analysis.py        ← 标度律拟合
  └── visualize.py       ← 图表输出
```

---

## 4. 接口规范（计划）

### 4.1 `gamma_matrix.py`

| 函数 | 计划签名 | 功能说明 |
|------|---------|----------|
| `gamma_element` | `(m: int, n: int, theta: float) -> complex` | 按真实公式计算单个 $\Gamma_{mn}(\theta)$ |
| `gamma_matrix_full` | `(M: int, theta: float, dtype: str = 'complex128') -> np.ndarray` | 生成 M×M $\Gamma$ 矩阵，shape=(M,M)，dtype=complex |
| `gamma_matrix_theta_grid` | `(M: int, n_theta: int) -> np.ndarray` | 生成 θ∈(0,π) 网格上的 Γ，shape=(n_theta, M, M) |

**量级约束**（来自 Phase G 实测）：
- $\max_{m,n}\|\Gamma_{mn}\| \propto M^{1.001}$
- 例如 $M=4096, \theta=\pi/4$ 时 $\max\|\Gamma\| \approx 4096$

### 4.2 `mu_matrix.py`

> ⚠️ **已废弃模型**（rev 1）：`mu_ideal_decay`（指数衰减）、纯随机模型已从当前计划移除。
> 替代方案：Jackson 核和 Lorentz 核通过**改变 $\mu_{mn}$ 的有效幅度**来模拟物理展宽效果，
> 比指数衰减更贴合 KPM 实际计算流程（核加权发生在 Chebyshev 递推之后、双重求和之前）。

| 函数 | 计划签名 | 功能说明 |
|------|---------|----------|
| `mu_raw_clean` | `(M: int, E0: float = 0.0, seed: int = None) -> np.ndarray` | 生成原始 Chebyshev 矩：$\mu_{mn}^{\text{raw}} = T_m(E_0)T_n(E_0)$，干净振荡不衰减，shape=(M,M) |
| `jackson_kernel` | `(n: int, M: int) -> float` | Jackson 核：$g_n^{(M)} = \frac{(M-n+1)\cos\frac{\pi n}{M+1} + \cot\frac{\pi}{M+1}\sin\frac{\pi n}{M+1}}{M+1}$ |
| `lorentz_kernel` | `(n: int, M: int, lam: float = 4.0) -> float` | Lorentz 核：$g_n^{(M)}(\lambda) = \frac{\sinh[\lambda(1 - n/M)]}{\sinh(\lambda)}$，λ 控制展宽 |
| `apply_kernel` | `(mu_raw: np.ndarray, kernel_m: np.ndarray, kernel_n: np.ndarray) -> np.ndarray` | 核加权：$\mu_{mn} = g_m \cdot g_n \cdot \mu_{mn}^{\text{raw}}$ |
| `mu_noise_layer` | `(mu_true: np.ndarray, eps: float, seed: int = None) -> np.ndarray` | 在核加权后的 μ 上叠加零均值随机噪声 $\sim \mathcal{N}(0, \varepsilon)$ |
| `mu_matrix_generate` | `(M: int, kernel: str, **kwargs) -> Tuple[np.ndarray, np.ndarray]` | 统一接口：`kernel='clean'|'jackson'|'lorentz'`，返回 (mu_true, mu_noisy) |

**三种 μ 模型对比**：

| 模型 | `kernel` 参数 | 核函数 | 高阶 $\mu_{mn}$ 行为 | 物理对应 |
|------|:---:|------|------|------|
| **干净振荡** | `'clean'` | $g_n \equiv 1$ | $\sim O(1)$ 振荡不衰减 | 无展宽的干净极限 → 条件收敛最差 |
| **Jackson 核** | `'jackson'` | Jackson (1982) | $\sim 1 - n/M$ 线性衰减 | tbplas 当前默认方案 |
| **Lorentz 核** | `'lorentz'` | Lorentz ($\lambda=4$) | $\sim e^{-\lambda n/M}$ 指数衰减 | García 2015 等效展宽方案 |

**量级约束**（来自 Phase L 实测）：
- $\|\mu_{mn}^{\text{raw}}\| \sim O(1)$，干净体系振荡
- Jackson 核使 $\|\Gamma_{mn}\mu_{mn}\|$ 在高 $(m,n)$ 区被抑制 $\sim (1-m/M)(1-n/M)$ 倍
- Lorentz 核 ($\lambda=4$) 抑制更强：$\sim e^{-\lambda(m+n)/M}$
- $\delta\mu \sim \mathcal{N}(0, \varepsilon_{\text{mach}} \cdot \sigma_\mu)$，$\varepsilon \approx 2.2\times 10^{-16}$

### 4.3 `summation.py`

> ⚠️ **已移除**（rev 2）：`sum_pairwise`（树形归约）从当前计划移除——先聚焦最基本的 sequential vs Kahan 对比，
> pairwise 作为后续扩展方向保留在 §10 "已知限制与后续扩展" 中。

| 函数 | 计划签名 | 功能说明 |
|------|---------|----------|
| `sum_sequential` | `(gamma: np.ndarray, mu: np.ndarray) -> float` | 标准双重循环顺序累加 $\sum_{m=0}^{M-1}\sum_{n=0}^{M-1} \text{Re}[\Gamma_{mn}\cdot\mu_{mn}]$ |
| `sum_kahan` | `(gamma: np.ndarray, mu: np.ndarray) -> float` | Kahan 补偿求和：维护 running compensation 项修正低位舍入误差 |
| `sum_dispatch` | `(gamma: np.ndarray, mu: np.ndarray, method: str) -> float` | 统一分发：`method='sequential'|'kahan'` |

**精度需求**：支持 `float64`；可选 `float32` 对照以放大随机游走效应。

### 4.4 `reference.py`

| 函数 | 计划签名 | 功能说明 |
|------|---------|----------|
| `sum_exact_mpmath` | `(gamma: np.ndarray, mu: np.ndarray, dps: int = 50) -> mpf` | mpmath 高精度 (50+ decimal digits) 计算 ground truth |
| `gamma_element_mpmath` | `(m: int, n: int, theta: float, dps: int = 50) -> mpc` | mpmath 版本的 $\Gamma_{mn}$ |
| `error_absolute` | `(S_approx: float, S_ref: float) -> float` | 绝对误差 $\|S_{\text{approx}} - S_{\text{ref}}\|$ |
| `error_relative` | `(S_approx: float, S_ref: float) -> float` | 相对误差 |

### 4.5 `analysis.py`

| 函数 | 计划签名 | 功能说明 |
|------|---------|----------|
| `rms_error` | `(errors: np.ndarray) -> float` | RMS 误差 $\sqrt{\frac{1}{n}\sum e_i^2}$ |
| `fit_scaling_law` | `(M_list: list, rms_list: list) -> Tuple[float, float, float]` | 拟合 $\log(\text{RMS}) = \alpha\log(M) + \beta$，返回 $(\alpha, \beta, R^2)$ |
| `n_trials_statistics` | `(M: int, n_trials: int, **kwargs) -> dict` | 对固定 M 多次试验，返回 {mean, std, min, max} |
| `convergence_diagnostic` | `(M_list, errors_dict) -> dict` | 判断误差在哪个 M 达到阈值 |

### 4.6 `visualize.py`

| 函数 | 计划签名 | 功能说明 |
|------|---------|----------|
| `plot_error_vs_M` | `(M_list, error_dict, methods, output_path)` | 主图：RMS error vs M，不同求和方法多线 |
| `plot_scaling_law` | `(M_list, rms_list, fit_result, output_path)` | 标度律图：log-log + 拟合线 |
| `plot_gamma_heatmap` | `(gamma: np.ndarray, M: int, output_path)` | Γ 矩阵热图（幅度），验证 O(n) 增长 |
| `plot_mu_heatmap` | `(mu: np.ndarray, M: int, output_path)` | μ 矩阵热图 |

### 4.7 `config.py`

| 函数 | 计划签名 | 功能说明 |
|------|---------|----------|
| `default_config` | `() -> dict` | 返回默认参数字典 |
| `M_scan_grid` | `(mode: str = 'log') -> list` | 返回 M 扫描列表 |

---

## 5. 参数设计表

### 5.1 核心参数

| 参数 | 类型 | 默认值 | 含义 |
|------|:---:|------|------|
| `M_list` | `list[int]` | `[64, 128, 256, 384, 512, 768, 1024, 2048, 3072, 4096, 6144, 8192]` | Chebyshev 展开阶数扫描列表 |
| `theta_grid` | `list[float]` | `[0.1π, 0.25π, 0.5π, 0.75π, 0.9π]` | θ 采样点（避开 0, π 奇点） |
| `n_trials` | `int` | `10` | 每个 (M, θ) 的随机噪声试验次数 |
| `noise_level` | `float` | `2.2e-16` | δμ 噪声幅度，默认 double 精度 $\varepsilon_{\text{mach}}$ |
| `summation_methods` | `list[str]` | `['sequential', 'kahan']` | 待测试的求和方法 |
| `mpmath_dps` | `int` | `50` | mpmath 高精度 decimal places |
| `output_dir` | `str` | `./output` | 输出根目录 |

### 5.2 μ 矩阵模型参数

> ⚠️ **已废弃**（rev 2）：`mu_decay_gamma`、`mu_oscillation_freq` 随旧模型移除。

| 参数 | 类型 | 默认值 | 含义 |
|------|:---:|------|------|
| `mu_kernel` | `str` | `'clean'` | 核模型：`'clean'`（无核）/ `'jackson'`（Jackson 核）/ `'lorentz'`（Lorentz 核） |
| `lorentz_lambda` | `float` | `4.0` | Lorentz 核展宽参数 $\lambda$（仅 lorentz 模型，$\lambda > 0$） |
| `mu_E0` | `float` | `0.0` | 干净振荡的中心能量 $E_0 \in [-1, 1]$（Chebyshev 域） |

### 5.3 分析参数

| 参数 | 类型 | 默认值 | 含义 |
|------|:---:|------|------|
| `error_threshold` | `float` | `1e-10` | 误差告警阈值（相对物理信号 ~1） |
| `scaling_fit_range` | `tuple[int,int]` | `(256, 4096)` | 标度律拟合的 M 范围 |

---

## 6. 文件结构规划

```
gamma_mu_sim/
├── src/                        ← 核心代码
│   ├── __init__.py
│   ├── main.py                 ← 主入口：M 扫描全流程
│   ├── config.py               ← 参数定义
│   ├── gamma_matrix.py         ← Γ 矩阵生成
│   ├── mu_matrix.py            ← μ 矩阵生成
│   ├── summation.py            ← 求和引擎
│   ├── reference.py            ← mpmath 高精度基准
│   ├── analysis.py             ← 误差分析与标度律
│   └── visualize.py            ← 可视化
├── tests/                      ← 单元测试
│   ├── test_gamma.py           ← Γ 矩阵正确性（对称性、量级）
│   ├── test_mu.py              ← μ 矩阵统计性质
│   ├── test_summation.py       ← 求和方法一致性（小 M 下与 exact 对比）
│   └── test_scaling.py         ← 标度律回归测试
├── output/                     ← 输出结果
│   ├── data/                   ← 数值结果 (CSV/NPY)
│   └── figures/                ← 图表 (PNG/PDF)
├── docs/                       ← 文档
│   ├── plan.md                 ← 本文件
│   ├── log.md                  ← 执行日志（开发中追加）
│   └── report.md               ← 最终分析报告
└── README.md                   ← 快速启动（代码完成后生成）
```

---

## 7. 数据格式规范

### 7.1 输入/输出文件

| 文件 | 格式 | 命名规则 | 列/键说明 |
|------|:---:|------|------|
| 合成 Γ 矩阵 | `.npy` | `gamma_M{M}_theta{idx}.npy` | shape=(M,M), dtype=complex128 |
| 合成 μ 矩阵 | `.npy` | `mu_M{M}_model{name}_trial{t}.npy` | shape=(M,M), dtype=float64 |
| M 扫描结果 | `.csv` | `scan_results.csv` | 列: `M, theta, method, trial, S_approx, S_ref, abs_err, rel_err` |
| 标度律拟合 | `.json` | `scaling_fit.json` | `{method: {alpha, beta, R2}}` |

### 7.2 scan_results.csv 列规范

```
M, theta_idx, theta_val, mu_kernel, method, trial, S_approx, S_ref, abs_err, rel_err, N_terms
64, 2, 1.5708, jackson, sequential, 0, 3.14159e-2, 3.14159e-2, 1.2e-15, 3.8e-14, 4096
...
```

---

## 8. 交付物清单

### 8.1 基础验证

| # | 任务 | M 范围 | 交付物 | 状态 |
|:---:|------|:---:|------|:---:|
| V1 | Γ 矩阵量级验证 | 64, 256, 1024, 4096 | `max|Γ| vs M` 图，验证 $\propto M$ | ⬜ |
| V2 | μ 矩阵统计验证 | 256 | δμ 正态性检验、自相关检验 | ⬜ |
| V3 | 小 M 求和方法一致性 | 32, 64, 128 | 2 种方法（sequential, Kahan）在 $M\le 128$ 时与 mpmath exact 一致 | ⬜ |

### 8.2 M 系统性扫描

| # | 任务 | 参数 | 交付物 | 状态 |
|:---:|------|------|------|:---:|
| S1 | Sequential × Clean | M=64→8192, clean 核, sequential, 10 trials | 误差 vs M 曲线（最差情况基准） | ⬜ |
| S2 | Kahan × Clean | 同上, kahan 求和 | Kahan 改善因子 vs M | ⬜ |
| S3 | Sequential × Jackson | M=64→8192, jackson 核, sequential | Jackson 核对条件收敛的改善 | ⬜ |
| S4 | Kahan × Jackson | 同上, kahan 求和 | 核+补偿联合效果 | ⬜ |
| S5 | Sequential × Lorentz | M=64→8192, lorentz 核 (λ=4), sequential | Lorentz 核是否消除随机游走 | ⬜ |
| S6 | Kahan × Lorentz | 同上, kahan 求和 | 最佳组合效果 | ⬜ |
| S7 | float32 对照 | M=64→2048, selected combos | 精度退化对照曲线 | ⬜ |

> ⚠️ **已移除**（rev 2）：原 S3 (Pairwise M 扫描) — pairwise 留作后续扩展。

### 8.3 核模型对比

> **⚠️ 本段核心假设已被 T5 实验证伪 (2026-06-28)。**
> 证伪实验: [log.md](log.md#ai-0628-0000) — T5 核模型对比
> **被证伪的假设**: (a) Lorentz 核可实现绝对收敛 (α→0) → 实测 α≈2, 不随 λ 变化; (b) 核加权可改变标度指数 α → 实测核仅改变 β 不改变 α; (c) 存在"甜点 λ"使 α<0.1 → λ∈[2,8] 全部 α≈2。
> 以下为历史存档。

| # | 任务 | μ 核模型 | 核心问题 | 状态 |
|:---:|------|------|------|:---:|
| P1 | 干净振荡基准 | clean ($g_n \equiv 1$) | 无核时 $\|\Gamma\mu\|$ 是否发散？标度指数 $\alpha$？ | ⬜ |
| P2 | Jackson 核效果 | jackson | Jackson 核是否将 $\alpha$ 从 ~1 压低？压低到多少？ | ⬜ |
| P3 | Lorentz 核效果 | lorentz ($\lambda=4$) | Lorentz 核是否能实现绝对收敛（$\alpha \to 0$）？ | ⬜ |
| P4 | Lorentz λ 扫描 | lorentz ($\lambda=2,3,4,6,8$) | λ 与收敛性的定量关系 | ⬜ |

> ⚠️ **已废弃**（rev 2）：原 P2 (指数衰减扫描)、P3 (纯随机) — 用核加权替代，更贴合 KPM 实际流程。

### 8.4 θ 依赖性

| # | 任务 | θ 值 | 交付物 | 状态 |
|:---:|------|------|------|:---:|
| T1 | θ 扫描 | 5 个 θ ∈ (0, π) | Γ 量级 vs θ，误差 vs θ | ⬜ |
| T2 | 奇点邻近行为 | θ→0 (0.01π), θ→π (0.99π) | $1/\sin^3\theta$ 放大效应 | ⬜ |

### 8.5 最终报告

| # | 任务 | 内容 | 状态 |
|:---:|------|------|:---:|
| R1 | 分析报告 | 标度指数 $\alpha$、最优求和方法、实用 M 上限 | ⬜ |
| R2 | 知识晋升 | 将验证结论写入 `02_kubo_bastin_deep_dive.md` §7 | ⬜ |

---

## 9. 参考文献

| # | 文献 | 关联 |
|:---:|------|------|
| 1 | **García et al. 2015**, PRL 114, 116602 | KPM Kubo-Bastin 原始实现，M=6144 |
| 2 | **Yuan et al. 2016**, PRB 94, 195434 | 黑磷 QHE，M=15000；Eq.12 基准公式 |
| 3 | **Weiße et al. 2006**, RMP 78, 275 | KPM 综述 — Chebyshev 矩收敛理论 |
| 4 | **Higham 2002**, *Accuracy and Stability of Numerical Algorithms*, SIAM | Kahan 补偿求和、pairwise summation 误差分析 |
| 5 | `02_kubo_bastin_deep_dive.md` §7 | 随机游走根因的完整 VBL Phase A–L 诊断 |
| 6 | `shared/tbplas-internals.md` §12.3 | 最终根因总结 |

---

## 附录 A：Γ 矩阵量级约束（来自 Phase G 实测 + Python 模拟确认）

> **🟡 补充说明 (2026-06-27, AI:0627_2300)**：max|Γ| ≈ M·sinθ（非精确 M）。θ=π/4 时 sinθ≈0.707，故 max|Γ| ≈ 0.707M。Phase G 的"~M"近似忽略了 sinθ 因子。以下为实测值：

| M | $\max_{m,n}\|\Gamma_{mn}\|$ (θ=π/4) | 比值 max\|Γ\|/M | 验证 $\propto M$ |
|:---:|:---:|:---:|:---:|
| 64 | ~45 | 0.70 | ✅ |
| 256 | ~181 | 0.71 | ✅ |
| 1024 | ~724 | 0.71 | ✅ |
| 4096 | ~2900 (预测) | 0.71 | — |

> 标度关系 $\propto M$ 仍然成立（max|Γ| ∝ M），仅比例常数 = sinθ。

## 附录 B：随机游走定量预测

| M | N = M² | 预测 RMS $\approx \sqrt{N}\cdot\varepsilon$ | 物理信号 | 信噪比 |
|:---:|:---:|:---:|:---:|:---:|
| 256 | 6.6×10⁴ | ~5×10⁻¹⁴ | ~1 | 5×10⁻¹⁴ ✅ |
| 1024 | 1.0×10⁶ | ~2×10⁻¹³ | ~1 | 2×10⁻¹³ ✅ |
| 2048 | 4.2×10⁶ | ~4.5×10⁻¹³ | ~1 | 4.5×10⁻¹³ ✅ |
| 4096 | 1.7×10⁷ | ~9×10⁻¹³ | ~1 | 9×10⁻¹³ ⚠️ |
| 6144 | 3.8×10⁷ | ~1.4×10⁻¹² | ~1 | 1.4×10⁻¹² ❌ |
| 8192 | 6.7×10⁷ | ~1.8×10⁻¹² | ~1 | 1.8×10⁻¹² ❌ |

> 模拟需验证：实际 RMS 是否吻合 $\sqrt{N}\cdot\varepsilon$ 标度，以及不同求和策略和核模型的改善因子。

---

## 10. 已知限制与后续扩展

### 10.1 当前版本限制

| 限制 | 说明 | 影响 |
|------|------|------|
| 仅单 θ 批量扫描 | 未实现完整 θ 网格积分 + Fermi-Dirac 加权 | 无法直接换算为 $\sigma_{xy}$ 偏移量 |
| μ 为合成模型 | $\mu_{mn}^{\text{raw}} = T_m(E_0)T_n(E_0)$ 是单能级模型，真实 μ 含多 Landau 能级叠加 | 误差量级估计偏保守 |
| 未模拟 θ 奇点放大 | $1/\sin^3\theta$ 在积分中对噪声的放大未纳入 | 实际 $\sigma_{xy}$ 偏移可能大于本模拟估计 |
| 仅 double 精度 | 未测试 long double (80-bit) 或 quad precision | — |

### 10.2 后续扩展方向

| 优先级 | 扩展 | 说明 |
|:---:|------|------|
| 🟡 | **pairwise / tree summation** | 树形归约可降低随机游走 RMS $\sim O(\sqrt{\log N}\cdot\varepsilon)$ |
| 🟡 | **完整 θ 积分模拟** | 加入 $\int d\theta$ + Fermi-Dirac + $1/\sin^3\theta$，直接估算 $\Delta\sigma_{xy}$ |
| 🟡 | **多 Landau 能级 μ 模型** | 合成 $\mu_{mn} = \sum_\ell w_\ell T_m(E_\ell)T_n(E_\ell)$ |
| 🟢 | **long double 精度测试** | numpy float128 (80-bit) 在 M≥4096 时是否足够 |
