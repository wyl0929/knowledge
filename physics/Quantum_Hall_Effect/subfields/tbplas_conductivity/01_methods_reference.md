<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-21 02:31:19
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-21 02:31:20
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/01_methods_reference.md
 * @Description  :
-->
<!--
Subfield: tbplas 电导率计算方法
Parent: 量子霍尔效应
Source: /home/wyl/project/shared/tbplas-internals.md §9–§12
Python source: ~/anaconda3/envs/tbplas-alpha/lib/python3.12/site-packages/tbplas/
C++ source: /home/wyl/tbplas/source/tbplas-cpp-a021ca8/
Created date: 2026-06-21
Last updated: 2026-06-21 (源码审计: 对照 tbplas-alpha solver.py / analysis.py / lindhard.py / config.py)
-->

# tbplas 电导率计算方法参考

> **Python 源码基准**：`~/anaconda3/envs/tbplas-alpha/lib/python3.12/site-packages/tbplas/`
> （`tbpm/solver.py`, `tbpm/analysis.py`, `tbpm/config.py`, `diag/lindhard.py`, `diag/config.py`）
> **C++ 源码基准**：`/home/wyl/tbplas/source/tbplas-cpp-a021ca8/`
> **跨项目知识库**：`tbplas-internals.md` §9（电导率全景）、§11（temperature）、§12（Kubo-Bastin 详解）

---

## 1. 全景总览

tbplas 提供 **4 种电导率计算路径**，按算法范式分为两个家族：

| # | 方法 | Python 调用 | 中间产物 | 最终输出 | 算法范式 | 体系规模 |
|---|------|-----------|---------|------|---------|:---:|
| ① | **TBPM Kubo-Bastin** | `solver.calc_hall_cond()` | — | `(energies, sigma)` — 单分量 $(\mu)$ 扫描 | KPM Chebyshev 矩 → θ 积分 | 大（$>10^4$ 轨道） |
| ② | **TBPM DC 关联函数** | `solver.calc_corr_dc_cond()` → `Analyzer.calc_dc_cond()` | `(corr_dos, corr_dc)` — 关联函数 | `(energies, dc)` — $\sigma_{xx}(E),\ \sigma_{yy}(E)$ | 准本征态投影 → 时间演化 → 傅里叶积分 | 大 |
| ③ | **TBPM AC 关联函数** | `solver.calc_corr_ac_cond()` → `Analyzer.calc_ac_cond()` | `corr_ac` — 关联函数 `(4, N_t)` | `(omegas, ac_cond)` — $\sigma_{\alpha\beta}(\omega)$ 4分量 | 传播子+Fermi-Dirac → 时间演化 → FFT+Hilbert | 大 |
| ④ | **Diag Lindhard AC** | `lindhard.calc_ac_cond()` | — | `(omegas, ac_cond)` — 单分量 $\sigma(\omega)$ | k 空间对角化 → 速度矩阵 Kubo 求和 | 中小（$<10^3$ 轨道） |

**补充**：Diag Lindhard 路径还提供动态极化率 $\Pi(\mathbf{q},\omega)$ 和介电函数 $\epsilon(\mathbf{q},\omega)$（见 §6）。

### 核心直觉：先理解"自变量"再选方法

四种方法输出的**横轴含义不同**，这是最容易混淆的地方：

| 方法 | 横轴 | 物理问题 |
|------|------|---------|
| Kubo-Bastin | 化学势 $\mu$（= 栅极电压 $V_g$） | "栅极调到某个电压时，Hall 电导是多少？" |
| DC 关联函数 | 电子能量 $E$ | "能量为 $E$ 的那些电子态，导电能力如何？" |
| AC 关联函数 | 频率 $\omega$ | "对某个频率的光，电导率是多少？" |
| Lindhard AC | 频率 $\omega$ | 同上，但确定性计算 |

**只有 Kubo-Bastin 的横轴与 QHE 实验（$\sigma_{xy}$ vs $V_g$）直接对应。**

---

## 2. 方法一：TBPM Kubo-Bastin Hall 电导率

### 2.1 物理意义

计算 **Hall 电导率随化学势的变化** $\sigma_{xy}(\mu)$，或纵向电导率 $\sigma_{xx}(\mu)$。

> ⚠️ **每次调用只计算一个分量**，由 `config.dckb_component` 控制（1=XX, 2=XY）。如需同时获得 $\sigma_{xx}(\mu)$ 和 $\sigma_{xy}(\mu)$，需要两次独立调用并在两次调用之间修改 `dckb_component`。

这是 tbplas 中**唯一能直接与 QHE 实验对比的方法**——实验测量 $\sigma_{xy}(V_g)$，而 $V_g \propto \mu$。

在量子霍尔体系中，$\sigma_{xy}(\mu)$ 应呈现**量子化平台**：$\sigma_{xy} = \nu \cdot e^2/h$（$\nu$ 为填充因子）。平台之间 $\sigma_{xx}$ 出现峰值（Landau 能级间的跃迁）。

### 2.2 算法简述

基于 Kubo-Bastin 公式的 KPM（Kernel Polynomial Method）实现（参考：PRL 114.116602, 2015）：

$$\sigma_{xy}(E_F) = \frac{4e^2\hbar}{\pi\Omega}\sum_{m,n}\frac{1}{(1+\delta_{0,m})(1+\delta_{0,n})}\int_{-\pi}^{\pi}\Gamma_{mn}(\theta)\,F(E_F,\cos\theta)\,\mu_{mn}\,d\theta$$

**算法流程**（C++ `KuboBastinCPU::kbdc_mu()`）：

```
1. 构建 Hamiltonian (CSR) + 电流算符 j_x, j_y
2. 对每个随机样本 |ψ₀⟩：
   a. 第一路 Chebyshev 三项递推：|t_n⟩ = T_n(H̃) · v_β |ψ₀⟩  (n = 0,1,...,M-1)
   b. 第二路 Chebyshev 三项递推：|t_m⟩ = T_m(H̃) · v_α |ψ₀⟩  (m = 0,1,...,M-1)
   c. 构建 Chebyshev 矩：μ_{mn} = ⟨t_m | t_n⟩
   d. Jackson 核加权抑制 Gibbs 振荡
   e. 样本平均
3. cond_from_trace()：θ ∈ (0,π) 数值积分
4. 对每个化学势 μ：二重求和 Σ_{m,n} Γ_{mn}(θ) · μ_{mn} · F(μ)
5. 乘以 prefactor (含体系面积/体积、自旋简并度)
```

其中 $\Gamma_{mn}(\theta)$ 是解析已知的积分核，$F(E_F, E)$ 是 Fermi-Dirac 分布。

### 2.3 返回类型与关键参数

**Python 返回**（`solver.py:305-327`）：
```python
energies, conductivity = solver.calc_hall_cond()
# energies:    (num_eng,) float64 — 化学势列表 (eV)，来自 config.dckb_energies
# conductivity: (num_eng,) float64 — 单分量电导率（实数值）
# 单位: e²/ħ (2D, dckb_unit="hbar") 或 e²/h (2D, dckb_unit="h")
```

| 参数 | 默认值 | 含义 | 调优建议 |
|------|--------|------|---------|
| `dckb_num_kernel` (M) | 2048 | Chebyshev 展开阶数 | QHE 需 ≥4096（物理）；实用窗口 M∈[512, 4096]，须配合 int ≥ M（见 §2.4） |
| `dckb_num_integ_steps` | 2048 | θ 积分点数 | **必须 ≥ M**（Nyquist 条件），推荐 ≥ 2M；默认 2048 对 M>2048 不足（见 §2.4） |
| `dckb_component` | 1 (XX) | 分量：1=XX, 2=XY | QHE 用 2；纵向用 1 |
| `dckb_energies` | `linspace(-0.2,0.2,40)` | 化学势扫描列表 (eV) | 细扫用 500-1200 点 |
| `dckb_unit` | `"hbar"` | 单位：`"hbar"` → $e^2/\hbar$，`"h"` → $e^2/h$ | QHE 对比实验用 `"h"` |
| `temperature` | 300 K | 温度，影响 Fermi-Dirac 展宽 | QHE 用 1-10 K |

### 2.4 ⚠️ 收敛性关键：θ-积分 Nyquist 条件

**这是 Kubo-Bastin 计算中最重要的数值约束。** 详见父文档 `tbplas-internals.md` §12.4。

#### 物理机制

$\Gamma_{mn}(\theta)$ 核的振荡频率由 $m,n$ 决定（最高到 $M-1$），最高频分量周期为 $2\pi/M$。在 $[0,\pi]$ 上用中点法则做数值积分，必须满足 **Nyquist 采样条件**：

$$\boxed{N_{\text{int}} \ge M \quad \text{（强制要求）}}$$

#### 违反后果

`dckb_num_integ_steps < dckb_num_kernel` → Nyquist 欠采样 → 混叠伪影 → $\sigma_{xy}$ 和 $\sigma_{xx}$ 出现**系统性基线偏移**（全能量范围恒加偏移）。这是此前 MG 项目中观测到的"基线偏移"的**真实根因**，而非 Chebyshev 递推不稳定性。

#### 实验证据（MG 项目 2026-07-01 M_int 扫描, m=512, B=100T）

| int/M | M=1024 | M=2048 | M=3072 | M=4096 |
|:-----:|:------:|:------:|:------:|:------:|
| 0.25 | — | 🔴 88 | — | 🔴 505 |
| 0.50 | 🟡 5.5 | 🔴 37 | — | 🔴 176 |
| 0.75 | — | — | — | 🟡 0.24 |
| **1.00** | ✅ 0.3 | ✅ 0.2 | ✅ 0.2 | — |

> RMS 误差 vs int=4096 参考值 ($e^2/h$)。🔴 >10, 🟡 1–10, ✅ <1

#### 安全使用规则

| 规则 | 说明 |
|------|------|
| `num_integ_steps ≥ num_kernel` | **强制要求**（Nyquist 条件） |
| `num_integ_steps ≥ 2 × num_kernel` | **推荐**（过采样 2×，安全余量） |
| `num_integ_steps = 2048`（默认） | ⚠️ **对 M > 2048 不安全**——默认值不随 M 自动调整 |
| 最大 M 推荐 | M ≤ 4096，int ≥ 4096（或更高） |

#### 其他已排除的历史误判

| 历史假设 | 实际状态 | 说明 |
|------|:---:|------|
| "Chebyshev 三项递推 M>512 发散" | ❌ 已证伪 | NaN 的真实原因是 `rescale` 误配（`rescale` < 带宽 → 特征值超出 Chebyshev 域）。设置 `rescale: -1`（自动检测）即可修复 |
| "C++ 浮点精度导致随机游走" | ❌ 已证伪 | VBL Phase A–M 全 9 假说排除，δμ 噪声实际是混叠伪影在 Γ·μ 空间的确定性表现 |
| "Kubo-Bastin 无法复现 QHE 平台" | ❌ 已证伪 | int ≥ M 即可正确计算；MG 实测 $\sigma_{xy}$ 平台结构正常 |

#### 推荐起步配置

```yaml
hall:
  dckb_num_kernel: 2048          # M=2048
  dckb_num_integ_steps: 4096     # int = 2M（过采样安全）
  dckb_component: 2              # 2=XY (Hall), 1=XX (纵向)
  rescale: -1                    # ⚠️ 必须用 auto-detect
  dckb_energies:
    min: -0.6
    max: 0.6
    num: 1200
```

---

## 3. 方法二：TBPM DC 关联函数

### 3.1 物理意义

计算**能量分辨的纵向 DC 电导率** $\sigma_{xx}(E)$ 和 $\sigma_{yy}(E)$。回答的问题是：

> "能量为 $E$ 的那些电子态，对直流导电的贡献有多大？"

适用于分析能带结构中哪些能量区域是"导电通道"、哪些是"绝缘区"。典型用法：在带隙内 $\sigma_{xx}(E) \approx 0$（绝缘），在扩展态区域 $\sigma_{xx}(E)$ 取峰值。

### 3.2 ⚠️ 不能直接与 QHE 实验对比

DC 关联函数输出 $\sigma_{xx}(E)$（横轴 = 电子能量 $E$），而 QHE 实验测量 $\sigma_{xx}(V_g)$（横轴 = 栅极电压 $\propto$ 化学势 $\mu$）。两者横轴不同，无法直接叠图。

若需实验可比的 $\sigma_{xx}(\mu)$，应使用 Kubo-Bastin 方法（§2）设 `dckb_component=1`。

### 3.3 算法简述

**两步法**——C++ 计算关联函数，Python `Analyzer` 做后处理。

**第一步**（`TBPMSolver.calc_corr_dc_cond()`, `solver.py:284-299`）：
```python
corr_dos, corr_dc = solver.calc_corr_dc_cond()
# corr_dos: (num_steps,) complex128 — 无量纲 DOS 关联函数
# corr_dc:  (2, num_eng, num_steps_dc) complex128 — DC 关联函数
#          维度0: xx, yy 两方向
#          维度1: 准本征态能量索引
#          维度2: DC 时间步
# 单位: e²/ħ² · (eV)² · nm²
```

**第二步**（`Analyzer.calc_dc_cond()`, `analysis.py:684-773`）：

**C++ 层**（`TBPMCPU::tbpm_dc_cond()`，由 `dc_method` 选择算法）：

- `dc_method="cheby_poly"`（默认）：Chebyshev 多项式展开准本征态
- `dc_method="block_time"`：分块时间演化

```
1. 构建 Hamiltonian + 电流算符 j_x, j_y
2. 确定准本征态能量窗口（从 dc_cond_energy_limits 筛选）
3. 对每个随机样本：
   a. 生成 |ψ₀⟩，传播 |ψ₀(t)⟩ = exp(-iHt)|ψ₀⟩
   b. 计算 DOS 关联函数 corr_dos
   c. 构造准本征态 |ψ(E)⟩（通过 FFT 或 Chebyshev 展开）
   d. 电流注入：j_x|ψ₀⟩, j_y|ψ₀⟩
   e. DC 关联函数：
      corr_dc[0,E](t) = ⟨exp(-iHt)·j_x·ψ₀ | j_x·ψ(E)⟩
      corr_dc[1,E](t) = ⟨exp(-iHt)·j_y·ψ₀ | j_y·ψ(E)⟩
4. 样本平均
```

**Python 层**（`Analyzer.calc_dc_cond()`, `analysis.py:684-773`）：

1. 先从 `corr_dos` 计算 DOS(E)
2. 对每个准本征态能量 $E$，对 DC 关联函数做傅里叶积分：

$$\sigma_{xx}(E) = \frac{N_\text{orb}}{\Omega} \cdot \Delta t \cdot \text{DOS}(E) \cdot \sum_{k=0}^{N_t^{dc}-1} w_k \cdot \text{Re}\left[e^{-iE t_k} \cdot C_{xx}(E,t_k)\right]$$

其中 $\Delta t = 2\pi/E_\text{range}$，$w_k$ 是窗函数。

> 注意：`corr_dos` 从 `calc_corr_dc_cond()` 返回的长度为 `num_steps`（而非 `num_steps+1`），Analyzer 内部在头部插入 1.0 后再调用 `calc_dos()`。

### 3.4 关键参数

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `dc_cond_energy_limits` | `[(-0.5, 0.5)]` | 关注的能量窗口列表 `[(E_min,E_max), ...]` (eV) |
| `dc_cond_num_time_steps` | 1024 | DC 关联函数时间步数 |
| `num_time_steps` | 1024 | DOS/准本征态的时间步数 |
| `dc_method` | `"cheby_poly"` | 准本征态算法：`"cheby_poly"` 或 `"block_time"` |
| `num_random_samples` | 1 | 随机样本数 |
| `window_dc` | `window_exp` | DC 傅里叶积分窗函数（传给 Analyzer） |

---

## 4. 方法三：TBPM AC 关联函数

### 4.1 物理意义

计算**频率依赖的 AC 电导率** $\sigma_{\alpha\beta}(\omega)$，输出 4 个分量（XX, YX, XY, YY）。回答的问题是：

> "体系对不同频率的光（从 DC 到紫外）的导电响应是怎样的？"

典型特征：
- **Drude 峰**：$\omega \to 0$ 处金属行为的准自由电子响应
- **带间跃迁峰**：$\hbar\omega$ 匹配能带间距时的吸收增强
- $\text{Re}[\sigma_{xx}(\omega)]$ 的积分满足 $f$-sum rule

### 4.2 算法简述

**两步法**——C++ 计算关联函数，Python `Analyzer` 做后处理。

**第一步**（`TBPMSolver.calc_corr_ac_cond()`, `solver.py:183-190`）：
```python
corr_ac = solver.calc_corr_ac_cond()
# corr_ac: (4, num_steps) complex128 — AC 关联函数
#          维度0: xx, yx, xy, yy 四方向
#          维度1: 时间步
# 单位: e²/ħ² · (eV)² · nm²
```

**第二步**（`Analyzer.calc_ac_cond()`, `analysis.py:501-557`）：

基于 Kubo-Greenwood 公式的随机波函数实现：

$$\sigma_{\alpha\beta}(\omega) = \frac{N_\text{orb}}{\Omega}\int_0^\infty e^{i\omega t}\ C_{\alpha\beta}(t)\ dt$$

$$C_{\alpha\beta}(t) = \langle\psi_0|\ f(H)\,j_\alpha\,e^{-iHt}\,[1-f(H)]\,j_\beta\ |\psi_0\rangle$$

**C++ 层**（`TBPMCPU::tbpm_ac_cond()`，构建上述关联函数）：

```
1. 构建 Hamiltonian + j_x, j_y
2. 初始化 Propagator (exp(-iHΔt)) 和 FermiDiracOperator (f(H))
3. 对每个随机样本：
   a. |ψ₁ˣ⟩ = [1-f(H)] · j_x |ψ₀⟩    ← 未被占据态的电流注入
   b. |ψ₁ʸ⟩ = [1-f(H)] · j_y |ψ₀⟩
   c. |ψ₂⟩  = f(H) |ψ₀⟩             ← 占据态投影
   d. 时间演化（Δt = π/E_range）：
      C_xx(t_n) = ⟨ψ₂| j_x · exp(-iHt_n) |ψ₁ˣ⟩
      C_xy(t_n) = ⟨ψ₂| j_x · exp(-iHt_n) |ψ₁ʸ⟩
      C_yx(t_n) = ⟨ψ₂| j_y · exp(-iHt_n) |ψ₁ˣ⟩
      C_yy(t_n) = ⟨ψ₂| j_y · exp(-iHt_n) |ψ₁ʸ⟩
4. 输出 (4, num_steps) 复矩阵
```

**Python 层**（`Analyzer.calc_ac_cond()`, `analysis.py:501-557`）：

实际计算实部（`analysis.py:514-533`）：

$$\text{Re}[\sigma_{\alpha\beta}(\omega)] = \frac{N_\text{orb}}{\Omega}\cdot\Delta t\cdot\frac{e^{-\beta\omega}-1}{\omega}\sum_k w_k\cdot\sin(\omega t_k)\cdot\text{Im}[C_{\alpha\beta}(t_k)]$$

其中 $\Delta t = \pi/E_\text{range}$，$\beta = 1/(k_B T)$。虚部通过 Kramers-Kronig（`scipy.signal.hilbert`）从实部得到。$\omega=0$ 时显式设为零（`analysis.py:528` 的 `if omega == 0.0: acv = 0.0`）。

### 4.3 温度的作用

温度通过 **Fermi-Dirac 算符** $f(H)$ 和 $1-f(H)$ 直接影响关联函数构造：
- **低温**：$f(H)$ 接近阶跃函数，仅费米面附近态参与导电 → Drude 峰尖锐
- **高温**：$f(H)$ 平滑，更多态参与 → Drude 峰展宽，带间阈值模糊

### 4.4 ⚠️ 高温混叠风险

tbplas 注释掉了一段温度展宽修正代码（`solver.h:317-321`）。原设计意图是 `time_step = 2π / (E_range + 50 k_B T)`，当前实际为 `time_step = 2π / E_range`。室温下 $50 k_B T \approx 1.29$ eV，对于窄带体系可能导致 Nyquist 混叠伪影。

### 4.5 关键参数

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `num_time_steps` | 1024 | 时间步数，决定频率分辨率 $\Delta\omega = E_\text{range}/N_t$ |
| `temperature` | 300 K | 影响 Fermi-Dirac 占据分布 |
| `num_random_samples` | 1 | 随机样本数 |

---

## 5. 方法四：Diag Lindhard AC 电导率

### 5.1 物理意义

与 TBPM AC 关联函数（§4）输出**相同的物理量** $\sigma_{\alpha\beta}(\omega)$，但使用完全不同的算法——k 空间直接对角化 + Kubo 公式解析求和。结果是**确定性的**（无随机误差），适合中小体系的精确计算。

> ⚠️ **每次调用只计算一个分量**，由 `config.ac_cond_component` 控制（1=XX, 2=XY, ..., 9=ZZ）。如需全部分量需多次调用。

### 5.2 返回类型

```python
omegas, ac_cond = lindhard.calc_ac_cond()
# omegas:  (num_omega,) float64 — 频率网格 (eV)，由 diag config 的 e_min/e_max/e_step 决定
# ac_cond: (num_omega,) complex128 — 单分量 AC 电导率
# 单位: e²/ħ (2D) 或 e²/(ħ·nm) (3D)
```

> 注：Lindhard 的 $\omega$ 网格来自 `DiagConfig.e_min/e_max/e_step`，**并非** `num_time_steps`。这与 TBPM AC 路径不同。

### 5.2 算法简述

基于 Kubo 公式的直接对角化实现：

$$\sigma_{\alpha\beta}(\omega) = \frac{ie^2\hbar}{N_k\Omega}\sum_{\mathbf{k}}\sum_{n,m}\frac{f_{n\mathbf{k}}-f_{m\mathbf{k}}}{E_{n\mathbf{k}}-E_{m\mathbf{k}}}\frac{\langle n\mathbf{k}|v_\alpha|m\mathbf{k}\rangle\langle m\mathbf{k}|v_\beta|n\mathbf{k}\rangle}{\hbar\omega + E_{n\mathbf{k}}-E_{m\mathbf{k}} + i\delta}$$

**算法流程**（`Lindhard::calc_ac_cond()`）：

```
1. 从 k_grid_size 生成均匀 k 网格
2. 从 tight-binding 跃迁项构建速度矩阵：
   v_α(k)_{ij} = (i/ħ) Σ_hop e^{ik·r_ij} · t_ij · (r_ij)_α
3. 对每个 k 点（MPI 并行）：
   a. 对角化 H(k) → E_nk, |n,k⟩
   b. 构建速度矩阵在 Bloch 基：v_α^{nm}(k) = ⟨n|v_α|m⟩
   c. 乘积矩阵：
      product(n,m) = v_α^{nm}·v_β^{mn}·(f_n-f_m)/(E_n-E_m)
      (|E_n-E_m| < 10⁻⁷ 时跳过)
4. 对每个频率 ω：
   σ(ω) = Σ_{n,m} product(n,m) / (ħω - (E_m-E_n) + iδ)
5. MPI Allreduce + 乘以 prefactor
```

其中展宽 $\delta$ 由 `config.delta` 控制（Lorentzian HWHM，默认 0.005 eV）。

### 5.3 关键参数

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `k_grid_size` | `(-1,-1,-1)` | k 点网格，第 3 维必须为 1（2D 体系） |
| `delta` | 0.005 eV | Lorentzian 展宽 HWHM |
| `mu` | 0.0 eV | 化学势 |
| `temperature` | 300 K | 影响 Fermi-Dirac 占据数 |
| `e_min/max/step` | -5/5/0.05 eV | 能量网格 |
| `ac_cond_component` | 1 (XX) | 分量：1=XX, 2=XY, ..., 9=ZZ |

---

## 6. 动态极化率与介电函数 — TBPM 与 Diag 双路径

tbplas 提供**两条独立的路径**计算动态极化率和介电函数：

### 6.1 TBPM 路径（`solver.calc_corr_dyn_pol()` → `Analyzer`）

**第一步**（`TBPMSolver.calc_corr_dyn_pol()`, `solver.py:192-200`）：
```python
corr_dyn_pol = solver.calc_corr_dyn_pol()
# corr_dyn_pol: (num_qpt, num_steps) float64 — 无量纲动态极化率关联函数
# q 点来自 config.dyn_pol_q_points
```

**第二步**（`Analyzer.calc_dyn_pol()`, `analysis.py:559-619`）：
- 对关联函数做傅里叶积分得到 $\Pi(\mathbf{q},\omega)$
- `Analyzer.calc_epsilon(dyn_pol)` → $\epsilon(\mathbf{q},\omega) = 1 - V(q)\Pi(\mathbf{q},\omega)$
- `Analyzer.calc_epsilon_q0(omegas, ac_cond)` → $\epsilon(\omega)$（仅 3D）

Coulomb 势由 `config.dyn_pol_coulomb_factor`（默认 1.0）和 `config.dyn_pol_back_epsilon`（默认 1.0）控制。

### 6.2 Diag Lindhard 路径（`lindhard.calc_dyn_pol()` → `lindhard.calc_epsilon()`）

| 方法 | Python 调用 | 输出 | 用途 |
|------|-----------|------|------|
| **动态极化率** | `lindhard.calc_dyn_pol()` | $\Pi(\mathbf{q},\omega)$ | 电荷密度-密度响应函数，Plasmon 色散 |
| **介电函数（有限 q）** | `lindhard.calc_epsilon(dyn_pol)` | $\epsilon(\mathbf{q},\omega) = 1 - V(q)\Pi(\mathbf{q},\omega)$ | 屏蔽效应、EELS 谱模拟 |
| **介电函数（q→0）** | `lindhard.calc_epsilon_q0(omegas, ac_cond)` | $\epsilon(\omega)$ | 光学介电函数（**仅 3D**） |

Lindhard 路径的 q 点来自 `DiagConfig.q_points`，展宽来自 `DiagConfig.delta`。

### 6.3 两条路径的差异

| 特性 | TBPM 路径 | Lindhard 路径 |
|------|----------|-------------|
| Coulomb 因子 | `dyn_pol_coulomb_factor` (可调) | 固定 1.0 |
| q 点参数 | `dyn_pol_q_points` (TBPMConfig) | `q_points` (DiagConfig) |
| 展宽控制 | 窗函数 | Lorentzian δ |
| 适用规模 | 大体系 | 中小体系 |

---

## 7. TBPMSolver 其他计算方法（补充）

除电导率外，`TBPMSolver`（`solver.py`）还提供以下计算入口：

| 方法 | Python 调用 | 输出 | 用途 |
|------|-----------|------|------|
| **DOS 关联函数** | `solver.calc_corr_dos()` | `corr_dos: (N_t+1,)` complex128 | TBPM 传播法 DOS 输入 |
| **Haydock LDOS** | `solver.calc_ldos_haydock()` | `(energies, ldos)` | 单 site 精确 LDOS（连分式 Green 函数） |
| **准本征态** | `solver.calc_quasi_eigenstates()` | `(num_qe, num_orb)` float64 | 平方准本征态波函数 |
| **Interior 特征值** | `solver.calc_interior_eigenspace()` | `dict` (eigenvalues, eigenvectors, residuals) | 能量窗口内特征对求解 |
| **波函数时间演化** | `solver.calc_wft(wf0)` | `(num_time, num_orb)` complex128 | 给定初态的时间传播 |
| **能带关联函数** | `solver.calc_corr_bands()` | `(k_len, corr_bands)` | k 路径上的 DOS 关联函数 |
| **电荷密度** | `solver.calc_charge_density()` | `(n_wf,)` float64 | 电荷密度 ρ(r) |

> `Analyzer.calc_diff_coeff(corr_dc)` 还可以从 DC 关联函数计算扩散系数 $D(E,t)$。

---

## 8. 跨方法对比与选型指南

### 8.1 TBPM vs Diag：算法范式差异

| 特性 | TBPM（①②③） | Diag Lindhard（④） |
|------|------------|-------------------|
| **计算瓶颈** | 稀疏矩阵-向量乘法 O(N) | 稠密对角化 O(N³) |
| **适用轨道数** | $10^4$–$10^6$ | $< 10^3$ |
| **k 点采样** | 超胞 m 隐式采样 | 显式 k 网格 |
| **随机误差** | 有（需多样本平均） | 无（确定性） |
| **有限尺寸效应** | 超胞 m 控制 | k 网格密度控制 |
| **展宽控制** | 窗函数 (Hanning/exp) | Lorentzian δ 参数 |
| **MPI 并行** | 分样本 | 分 k 点 |
| **GPU 支持** | ✅ (`algo="gpu"`) | ❌ |

### 8.2 场景 → 方法速查

| 场景 | 推荐方法 | 理由 |
|------|---------|------|
| 与 QHE 实验对比 $\sigma_{xy}(\mu)$ + $\sigma_{xx}(\mu)$ | **Kubo-Bastin** 两分量（两次调用） | 横轴一致（化学势），可直接叠图 |
| 分析"哪些能量态导电" | **DC 关联函数** | 能量分辨输出 |
| 光学响应 $\sigma(\omega)$（大体系） | **AC 关联函数** | 一次计算全频段（4 分量） |
| 光学响应 $\sigma(\omega)$（小体系精确） | **Lindhard AC** | 确定性，精细控制展宽 |
| Plasmon / 屏蔽效应（大体系） | **TBPM** `calc_corr_dyn_pol()` → `Analyzer` | 一次全 q 范围 |
| Plasmon / 屏蔽效应（小体系） | **Lindhard** `calc_dyn_pol()` / `calc_epsilon()` | 确定性 |

### 8.3 精度调优优先级

| 方法 | 第一优先调参 | 第二优先 |
|------|------------|---------|
| Kubo-Bastin | `dckb_num_integ_steps`（**必须 ≥ M**） | `dckb_num_kernel`, `rs`（≥8） |
| DC 关联函数 | `dc_cond_num_time_steps` | `num_random_samples`, `dc_method` |
| AC 关联函数 | `num_time_steps` | `num_random_samples`, `temperature` |
| Lindhard AC | `k_grid_size` | `delta`（展宽）, `e_step` |

---

## 9. 已知限制与风险

| 限制 | 影响的方法 | 严重程度 | 说明 |
|------|:---:|:---:|------|
| **θ-积分 Nyquist 混叠**（`int < M` → 基线偏移） | ① Kubo-Bastin | 🟡 中 | 设 `int ≥ M`（推荐 `int ≥ 2M`）即可消除。详见 §2.4 和 `tbplas-internals.md` §12.4 |
| **DC 关联函数横轴不匹配实验** | ② DC 关联 | 🟡 中 | 输出 $\sigma_{xx}(E)$ 而非 $\sigma_{xx}(\mu)$，不能直接与 QHE 实验叠图 |
| **高温混叠风险**（无温度展宽修正） | ③ AC 关联 | 🟡 中 | 注释掉的代码本应扩展 Nyquist 带宽；室温下可能已有影响 |
| **Lindhard 对角化标度** O(N³) | ④ Lindhard | 🟡 中 | 仅适用于小体系（轨道数 $< 10^3$） |
| **`dckb_unit` 转换方向待验证** | ① Kubo-Bastin | 🟢 低 | `"h"` 模式乘 $2\pi$ 而非除，存疑；不影响定性结论 |
| **`algo` 对 Kubo-Bastin 无影响** | ① Kubo-Bastin | 🟢 信息 | 非 GPU 所有 algo 值均走同一 `KuboBastinCPU` 后端 |
| **Kubo-Bastin 和 Lindhard AC 均为单分量调用** | ①④ | 🟢 信息 | 每次调用只输出一个分量；需多次调用获取完整张量 |

---

## 10. 相关文档

- 父领域包：[量子霍尔效应](/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/)
- 跨项目知识库：[tbplas-internals.md](/home/wyl/project/shared/tbplas-internals.md)（§9 电导率全景、§11 temperature 参数、§12 Kubo-Bastin 详解）
- 计算项目：MG、TMBG、TBG（`~/project/` 下各目录）
- Python 源码：`~/anaconda3/envs/tbplas-alpha/lib/python3.12/site-packages/tbplas/tbpm/solver.py`、`analysis.py`、`config.py`
- Diag 源码：`~/anaconda3/envs/tbplas-alpha/lib/python3.12/site-packages/tbplas/diag/lindhard.py`
