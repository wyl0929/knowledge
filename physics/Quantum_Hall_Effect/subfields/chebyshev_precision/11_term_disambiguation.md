<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27 23:48:02
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-27 23:48:07
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/chebyshev_precision/11_term_disambiguation.md
 * @Description  :
-->
<!--
Field: 切比雪夫迭代浮点精度问题
Parent: tbplas_conductivity
Created date: 2026-06-27
-->

# 11 Term Disambiguation / 术语澄清与概念边界

Last updated: 2026-06-27

## Gate verdict / 门控结论

- **概念边界状态**：`resolved` — 以下 6 组核心概念区分清晰，无需进一步澄清即可进入 claims 和 gap 阶段

---

## 概念边界契约

### CB-01: "Chebyshev 迭代不稳定" vs "浮点累积精度损失"

| | Chebyshev 三项递推不稳定 | 浮点累积精度损失 |
|------|------|------|
| 含义 | Chebyshev 多项式 $T_n(x)$ 的三项递推 $T_{n+1}=2xT_n-T_{n-1}$ 在 $n$ 大时丧失正交性，$T_n$ 本身偏离真值 | 每次浮点运算引入 $\sim\varepsilon_{\text{mach}}$ 的舍入误差，在大量（$N \sim M^2$）累加中 RMS 按 $\sqrt{N}$ 增长 |
| 在本问题中的角色 | **已被排除**（Phase A）：正交性保持良好，$\langle T_m T_n\rangle$ 仍接近 $\delta_{mn}$ | **确认为根因之一**（Phase M）：不是递推发散，而是每次迭代的微小噪声在高权重累加中被放大 |
| 区分判据 | 如果递推不稳定，$\mu_{mn}$ 会系统偏离 $\cos(m\arccos E_0)\cos(n\arccos E_0)$ | 实际 $\mu_{mn}$ 在真值附近随机涨落（零均值），非系统性偏差 |

**边界规则**：说"Chebyshev 迭代不稳定"在本语境中是**不准确的**。正确表述是"Chebyshev 迭代中的浮点噪声在 Γ 加权下的条件累积"。

### CB-02: "条件收敛" vs "发散"

| | 条件收敛 | 真发散 |
|------|------|------|
| 含义 | 求和结果依赖于求和方法（如求和顺序），但存在一个确定的极限值 | 求和结果随项数增加无限增大，不存在有限极限 |
| 在本问题中的角色 | **确认**（Phase L）：Sequential vs Kahan 求和结果不同，差异随 M 增大 | **被排除**：S(M) 并非单调发散，而是围绕真值随机游走 |

**边界规则**：$S(M)$ 是一个条件收敛的随机游走过程，不是发散级数。说"发散"会误导修复方向。

### CB-03: "噪声" vs "系统性偏差 (bias)"

| | 零均值随机噪声 (δμ) | 系统性偏差 |
|------|------|------|
| 含义 | $\mathbb{E}[\delta\mu]=0$，正负概率均等，无方向偏好 | 误差有固定符号或方向，$\mathbb{E}[\delta\mu]\neq 0$ |
| 在本问题中的角色 | **确认**（Phase L: pos_frac=0.4997，Phase bias: 无系统性 Krylov 漂移） | **被排除** |
| 对修复的意义 | 噪声累积可通过核加权抑制（压低高 |Γ| 项），也可以通过 Kahan 补偿减少低位舍入 | 系统性偏差需要不同策略（如重新标定或校准） |

### CB-04: "Γ 矩阵" vs "权重矩阵"

| | Γ 矩阵 | 一般权重矩阵 |
|------|------|------|
| 定义 | Kubo-Bastin 公式中 $\Gamma_{mn}(\theta) = \cos(m\theta)(\cos\theta - in\sin\theta)e^{in\theta} + \cos(n\theta)(\cos\theta + im\sin\theta)e^{-im\theta}$ | 泛指任何双重求和的系数矩阵 |
| 关键性质 | 量级 $\sim O(\max(m,n))$，线性增长；含 θ 参数；复矩阵；实部用于电导率 | 不一定有线性增长性质 |
| 为什么重要 | 线性增长是噪声被放大的核心机制：$\|\Gamma_{mn}\cdot\delta\mu_{mn}\| \propto \max(m,n)\cdot\varepsilon_{\text{mach}}$ | — |

### CB-05: "Jackson 核" vs "Lorentz 核" vs "无核 (clean)"

| | Jackson 核 | Lorentz 核 | 无核 (clean) |
|------|------|------|------|
| 公式 | $g_n = \frac{(M-n+1)\cos\frac{\pi n}{M+1} + \cot\frac{\pi}{M+1}\sin\frac{\pi n}{M+1}}{M+1}$ | $g_n = \frac{\sinh[\lambda(1-n/M)]}{\sinh(\lambda)}$ | $g_n \equiv 1$ |
| 衰减行为 | $\sim 1-n/M$（线性） | $\sim e^{-\lambda n/M}$（指数） | 不衰减 |
| 对噪声的抑制 | 中等：$g_m g_n \sim (1-m/M)(1-n/M)$ | 强：$g_m g_n \sim e^{-\lambda(m+n)/M}$ | 无抑制 |
| tbplas 默认 | ✅ 当前默认 | 可选 | 不用 |

**边界规则**：核加权发生在 Chebyshev 递推之后、双重求和之前。它不减少 μ 矩阵的噪声本身，但压制高索引（大 Γ）项对求和的贡献，从而降低条件收敛的严重程度。

### CB-06: "Kahan 求和" vs "高精度算术"

| | Kahan 补偿求和 | 高精度算术（quad/arbitrary precision） |
|------|------|------|
| 机制 | 维护一个补偿项，捕获每次加法中被丢弃的低位比特 | 用更多比特表示每个浮点数（如 128-bit quad 替代 64-bit double） |
| 改善什么 | 减少**累加过程中**的舍入误差 | 减少**每次运算产生**的舍入误差 |
| 局限 | 不能修复 μ 矩阵中已经存在的噪声（噪声在 KPM 迭代层已产生） | 从源头减少 δμ 的产生 |
| 在本问题中的角色 | Phase M2 确认：Kahan vs Sequential 差异极小（S_f32≈S_f64），说明累加不是瓶颈 | 长期修复路径（P0） |

---

## 错误等同警告

以下等同是**不正确**的，在阅读和讨论中需要区分：

| ❌ 错误等同 | ✅ 正确区分 |
|------|------|
| "Chebyshev 迭代发散" = "浮点精度问题" | Chebyshev 迭代本身稳定；问题是浮点噪声在 Γ 加权下的累积 |
| "增大 M 总能提高精度" | 对 Kubo-Bastin 双重求和，M > 2560 后噪声增长快于信号改善 |
| "用 Kahan 求和就能解决" | Kahan 只改善累加层；噪声源在 KPM 迭代层（C++），需要 quad precision |
| "加 Anderson 无序就能压住噪声" | Phase H 已证伪：γ=0.27 eV 对 M=1024 的基线偏移无效；γ≥0.5 同时破坏 QHE 信号 |
