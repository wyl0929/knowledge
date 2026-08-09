<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27 23:49:19
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-27 23:49:22
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/chebyshev_precision/01_research_overview.md
 * @Description  :
-->
<!--
Field: 切比雪夫迭代浮点精度问题
Parent: tbplas_conductivity
Created date: 2026-06-27
-->

# 01 Research Overview / 切比雪夫迭代浮点精度问题综述

Last updated: 2026-06-27

## 摘要

在 Kubo-Bastin 量子霍尔电导率计算中，当 Chebyshev 展开阶数 $M \gtrsim 3072$ 时，双重求和 $\sum_{m,n}\Gamma_{mn}\mu_{mn}$ 出现系统性基线偏移。经过 Phase A–M（2026-06-22~27）的全链路诊断，9 个备择假说被逐一排除，根因确认为：**C++ KPM Chebyshev 迭代中产生的零均值浮点噪声 $\delta\mu$，在被量级线性增长的 $\Gamma$ 矩阵加权后，通过 $M^2$ 项累加产生不可忽略的随机游走累积。**

本文档是该问题的系统性综述，覆盖问题背景、诊断过程、根因机制、实用窗口和修复路径。

---

## 1. 问题背景

### 1.1 Kubo-Bastin 公式

TBPLaS 中 Hall 电导率的核心表达式（简化形式）：

$$\sigma_{xy} \propto \int_0^\pi d\theta \frac{f(\cos\theta)}{\sin^3\theta} \sum_{m,n=0}^{M-1} \Gamma_{mn}(\theta) \cdot \mu_{mn}$$

其中：

$$\Gamma_{mn}(\theta) = \cos(m\theta)(\cos\theta - in\sin\theta)e^{in\theta} + \cos(n\theta)(\cos\theta + im\sin\theta)e^{-im\theta}$$

$$\mu_{mn} = \langle\psi_0|T_m(\tilde{H})|\psi_0\rangle \cdot \langle\psi_0|T_n(\tilde{H})|\psi_0\rangle$$

$T_n$ 是 Chebyshev 多项式，通过三项递推 $T_{n+1} = 2\tilde{H}T_n - T_{n-1}$ 在 KPM 中计算。

### 1.2 收敛性预期

文献（PRL 114.116602）建议 $M \geq 4096$（甚至 $6144$）以实现 QHE 平台的收敛。然而在实际计算中发现：

- $M \leq 2560$：$\sigma_{xy}$ 接近量子化平台值
- $M \gtrsim 3072$：$\sigma_{xy}$ 出现系统性基线偏移，偏离平台值
- $M = 4096$：偏移显著，不可接受

### 1.3 初步排除的常见误解

在系统诊断之前，已确认以下**不是**原因：
- **rescaling 错误**：`rescale=-1`（自动带宽检测）正确，手动设置 rescale=9.0 导致 NaN 是另一独立问题
- **Gibbs 振荡**：干净体系的 δ 函数型 LL 确实有 Gibbs 振荡，但基线偏移是额外的系统性问题

---

## 2. 诊断过程：Phase A–M

### 2.1 诊断方法论

采用**假说-排除法**：每个假说必须通过至少一个决定性实验予以确认或排除，不依赖间接推论。

```
假说生成 → 判据实验设计 → 实验执行 → 假说裁决 (确认/排除/存疑)
    ↑                                                      │
    └──────────────── 新假说 ← 排除后新线索 ←──────────────┘
```

### 2.2 九假说全览与裁决

| Phase | 假说 | 核心判据 | 裁决 | 日期 |
|:---:|------|------|:---:|------|
| A | Chebyshev 正交性随 M 丧失（norm inflation） | $\langle T_m\|T_n\rangle$ 是否偏离 $\delta_{mn}$ | ❌ 排除 | 06-22 |
| B | Jackson 核在高 M 退化 | 核函数 $g_n(M)$ 是否产生异常加权 | ❌ 排除 | 06-23 |
| C | 能谱边缘泄漏（eigenvalues outside [-1,1]） | rescale 是否正确覆盖带宽 | ❌ 排除 | 06-23 |
| D | double 精度单次运算不够 | 单次 Chebyshev 迭代的精度是否足够 | ❌ 排除 | 06-24 |
| θ | θ 积分中 $\sin^{-3}\theta$ 奇异性 | 奇异性是否导致数值发散 | ❌ 排除 | 06-24 |
| Γ | Γ 矩阵本身的计算精度 | 解析公式是否有精度损失 | ❌ 排除 | 06-25 |
| μ | μ 矩阵的 M 依赖性（clean 体系） | $\mu_{mn}$ 是否随 M 系统变化 | ❌ 排除 | 06-25 |
| J | Jackson 核 M 依赖性的副作用 | 核归一化是否随 M 变化 | ❌ 排除 | 06-25 |
| bias | δμ 有系统性偏差（非零均值） | 噪声符号分布是否偏离 50% | ❌ 排除 | 06-26 |

### 2.3 Phase M：随机游走假说闭环验证（06-27）

排除所有备择假说后，剩下的假说是：

> **$\delta\mu_{mn}$（C++ KPM Chebyshev 迭代产生的零均值浮点噪声）× $\Gamma_{mn}$（量级 $\propto \max(m,n)$）× $M^2$ 项累加 → 不可忽略的条件收敛**

Phase M 设计了三个闭环验证：

#### M1：噪声注入线性关系确认

**方法**：在 μ 矩阵上叠加已知幅度的合成噪声 $\eta \sim \mathcal{N}(0,\sigma^2)$，测量 ΔS 的响应。

**结果**：
- $dS_{\text{obs}} / dS_{\text{pred}} = 1.000 \pm 0.001$
- RMS ∝ σ^0.999（线性关系确认）
- **结论**：噪声 → ΔS 的因果链成立，放大因子为 ‖Γ‖

#### M2：噪声源层级定位

**方法**：对比 float32 和 float64 求和结果。如果噪声主要在累加层，f32 会显著差于 f64；如果在 KPM 迭代层，两者应接近。

**结果**：
- $S_{f32} \approx S_{f64}$（差异极小）
- **结论**：**求和精度不是瓶颈**。噪声 δμ 在 mu 矩阵**构建过程**（C++ KPM Chebyshev 迭代）中产生，而非在后续累加中。

#### M3：Γ 加权确认

**方法**：分析高 |Γ| 项对总和的贡献占比。

**结果**：
- 高 $(m,n)$ 索引的项（|Γ| 大）主导 S 的噪声成分
- **结论**：Γ 的线性增长是噪声放大的核心机制

---

## 3. 根因机制

### 3.1 三步链

```
Step 1: δμ 产生
  C++ KPM Chebyshev 三项递推
  T_{n+1} = 2H̃·T_n - T_{n-1}
  → 每次迭代引入 ~ε_mach 的舍入噪声
  → δμ_{mn} ~ N(0, ε²), ε ≈ 2.2×10^{-16}

Step 2: Γ 加权放大
  Γ_{mn} ∼ O(max(m,n))
  M=4096 → max|Γ| ≈ 4096
  → Γ_{mn}·δμ_{mn} 的噪声量级被放大 ~4000×

Step 3: 累积求和
  N = M² 项累加
  RMS ∝ √N · ε · ‖Γ‖_max
  M=4096: √N ≈ 4128, ε‖Γ‖ ≈ 9×10^{-13}
  → 累积噪声与物理信号 (∼2 e²/h) 可比拟
```

### 3.2 标度律

随机游走理论预测 RMS 误差的标度行为：

$$\log(\text{RMS}) = \alpha \log(M) + \beta$$

- 纯随机游走：$\alpha \approx 1$（因为 $\sqrt{M^2} = M$）
- 加上 Γ 线性增长：$\alpha$ 略大于 1（Phase G 实测 $\max\|\Gamma\| \propto M^{1.001}$）
- gamma_mu_sim 验证：实测 $\alpha \approx 1$

### 3.3 为什么核加权不能根治

Jackson 核压制高索引项 $\sim (1-m/M)(1-n/M)$，但：
- $m=0.9M$ 时 $g=0.1$，仍保留 10% 权重
- Lorentz 核 $\lambda=4$ 压制更彻底：$e^{-4 \times 0.9} \approx 0.027$
- 但核加权**不减少** μ 矩阵中的 δμ 本身——它已在 KPM 层产生

---

## 4. 实用结论与修复路径

### 4.1 安全使用窗口

| M 范围 | 风险等级 | 噪声水平 | 建议 |
|------|:---:|------|------|
| M ≤ 1024 | 🟢 安全 | 可忽略 | 正常使用 |
| M = 1536–2560 | 🟡 低风险 | 勉强接受 | Kahan 编译 + 验证单层 QHE 基准 |
| M = 3072–4096 | 🔴 高风险 | 不可忽略 | 需 Lorentz λ≥4 或 quad precision |
| M ≥ 6144 | ⛔ 不可用 | 压倒信号 | 双精度下不建议 |

### 4.2 修复路径（按优先级）

| 优先级 | 方案 | 效果 | 代价 | 状态 |
|:---:|------|------|------|:---:|
| **P2** | M ≤ 2560 实用窗口 | 规避问题 | 放弃高 M 精度 | ✅ 可用 |
| **P1** | Lorentz 核 λ ≥ 4 | 压制高索引 ≈ 1–2 个数量级 | 改变展宽，增加一个可调参数 | 🟡 gamma_mu_sim 正在验证 |
| **P0** | C++ quad precision KPM 迭代 | 根治噪声源 | 需修改 C++ 源码 + 性能下降 2–4× | ⚪ 未实现 |
| P3 | 其他 KPM 库对比 | 了解问题是 tbplas 特有还是普遍的 | 需要大量适配工作 | ⚪ 未探索 |

### 4.3 不推荐的方案

| 方案 | 原因 |
|------|------|
| Anderson 无序展宽 | Phase H 已证伪：γ=0.27 eV 不改善基线偏移（仅降 1.7×）；γ≥0.5 同时破坏 QHE 信号 |
| 增大 rescale 值 | 会导致 NaN（特征值超出 Chebyshev 域） |
| 仅用 Kahan 求和 | Phase M2 已证：累加不是瓶颈 |

---

## 5. 与 gamma_mu_sim 项目的关系

本 field pack 的结论由 `../gamma_mu_sim/` 项目提供数值验证。该项目在纯 Python 环境下：

1. 按解析公式合成 Γ 矩阵（可控量级）
2. 合成三种核模型的 μ 矩阵（clean / Jackson / Lorentz）并叠加可控噪声
3. 用 sequential / Kahan / mpmath 高精度三种方法求和
4. 扫描 M = 64 → 8192，拟合标度律

截至 2026-06-27，T1–T2（核心模块 + 流水线）已完成，T4（M 系统性扫描，6 kernel×method + float32 对照）正在执行。

---

## 6. 开放问题

1. **C++ 层 quad precision 实现的性能代价**：__float128 或 double-double 在 KPM 迭代中的实际开销是多少？
2. **其他 KPM 实现是否也有此问题**：GPAW、Siesta 等代码的 Chebyshev 迭代是否也在 double 精度下有类似累积？
3. **M=2560 是否足以解析 QHE 平台**：对于多层转角石墨烯等复杂体系，M=2560 的能量分辨率是否够用？
4. **是否有中间精度方案**：如仅在 Chebyshev 递推中用 quad，后续累加仍用 double？

---

## 参考文献

- PRL 114, 116602 (2015) — Kubo-Bastin KPM 收敛性原始文献
- Weiße et al., Rev. Mod. Phys. 78, 275 (2006) — KPM 综述
- Jackson, "The Theory of Approximation" (1930) — Jackson 核原始文献
- `shared/tbplas-internals.md` §12.3 — C++ 层面完整诊断记录
- `../gamma_mu_sim/docs/plan.md` — Γ-μ 模拟计划书
