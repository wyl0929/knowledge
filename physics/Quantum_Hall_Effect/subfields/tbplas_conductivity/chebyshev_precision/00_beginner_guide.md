<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27 23:47:55
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-27 23:47:56
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/chebyshev_precision/00_beginner_guide.md
 * @Description  :
-->
<!--
Field: 切比雪夫迭代浮点精度问题
Parent: tbplas_conductivity
Created date: 2026-06-27
-->

# 00 Beginner Guide / 切比雪夫迭代精度问题入门

Last updated: 2026-06-27

## 先讲直觉，再讲术语

想象你在数一堆硬币。每枚硬币面值不同，有的 $1，有的 $1000。你要把它们全部加起来算出总金额。

如果每枚硬币的面值你都**精确知道**，那就没有误差——无论加的顺序如何，答案都一样。

但如果每枚硬币的面值有微小误差（比如实际 1.000000000000001 元，但你只能读到 1.00 元），问题就来了：

- 当你把 $1000$ 的硬币上的小误差累加 $N$ 次，总误差大约按 $\sqrt{N}$ 增长
- 如果 $N$ 很大（比如一千万次），这个误差累积起来可能就不再可忽略了

**这就是 Kubo-Bastin 量子霍尔电导率计算中发生的事。**

---

## 问题是什么？

TBPLaS（紧束缚传播法大规模模拟）用 **KPM（Kernel Polynomial Method，核多项式方法）** 计算量子霍尔电导率 $\sigma_{xy}$。核心公式是双重求和：

$$\sigma_{xy} \propto \sum_{m,n=0}^{M-1} \Gamma_{mn}(\theta) \cdot \mu_{mn}$$

其中：

| 符号 | 物理含义 | 量级 |
|------|---------|------|
| $M$ | Chebyshev 展开阶数 | 256–8192 |
| $\Gamma_{mn}$ | 解析可算的"权重矩阵" | $\sim O(\max(m,n))$，线性增长 |
| $\mu_{mn}$ | Chebyshev 矩的乘积：$\langle T_m(H)T_n(H)\rangle$ | $\sim O(1)$，含浮点噪声 |

**问题**：当 $M \gtrsim 3072$ 时，求和结果 $\sigma_{xy}$ 出现系统性基线偏移——计算的霍尔电导率偏离正确的量子化平台值。

---

## 不是什么问题？

先澄清几个**已被排除**的常见误解：

| ❌ 被排除的假说 | 为什么不对 |
|------|------|
| Chebyshev 递推不正交（超出稳定域） | 不是。正交性保持良好。 |
| Jackson 核在高 M 退化 | 不是。核函数行为正常。 |
| 能谱边缘泄漏 | 不是。rescaling 正确（`rescale=-1` 自动检测带宽）。 |
| double 精度本身不够 | 不完全是。单次加法精度够，但累积效应显现。 |
| θ 积分奇异性 | 不是。奇异性可处理。 |
| Γ 矩阵计算精度 | 不是。Γ 是解析可算的，精度可控。 |

---

## 真正的原因（Phase M 结论，2026-06-27）

根因链分三步：

### 第一步：δμ 的产生

在 C++ KPM Chebyshev 迭代中：

$$\mu_n = \langle\psi_0|T_n(\tilde{H})|\psi_0\rangle$$

三项递推 $T_{n+1} = 2\tilde{H}T_n - T_{n-1}$ 在 double 精度下产生零均值的随机噪声 $\delta\mu_{mn}$，量级约为 $\varepsilon_{\text{mach}} \approx 2.2 \times 10^{-16}$。

### 第二步：Γ 的放大

$\Gamma_{mn}$ 的元素量级随索引线性增长：$\max|\Gamma_{mn}| \propto M$。当 $M=4096$ 时，最大的 $\Gamma$ 元素约为 4096。

这意味着 $\Gamma_{mn} \cdot \delta\mu_{mn}$ 中，大索引位置的噪声被放大 $\sim 4000\times$。

### 第三步：条件收敛

双重求和包含 $N = M^2$ 项（$M=4096$ 时 $N \approx 1.7 \times 10^7$）。随机游走 RMS 累积：

$$\text{RMS}(S) \propto \sqrt{N} \cdot \varepsilon_{\text{mach}} \cdot \|\Gamma\|_{\max}$$

当 $M=4096$，这个累积可与物理信号 $\sim 2\,e^2/h$ 相比拟，导致 σ_xy 偏离量子化平台。

---

## 实用结论

| M 范围 | 风险 | 建议 |
|------|:---:|------|
| M ≤ 1024 | 🟢 安全 | 正常使用 |
| M = 1536–2560 | 🟡 低风险 | Kahan 编译 + 验证 |
| M = 3072–4096 | 🔴 高风险 | 需要 quad precision 或 Lorentz λ>4 |
| M ≥ 6144 | ⛔ 不可用 | 双精度下无法收敛 |

**最推荐的实用方案**：M ≤ 2560 + `rescale=-1` + Kahan 补偿求和。

---

## 与你的关系

如果你在用 tbplas 计算 Kubo-Bastin 电导率：

1. **始终用 `rescale=-1`**（自动带宽检测），不要手动设置 rescale
2. **M 不要超过 2560**，除非你清楚精度后果
3. 如果必须用大 M，考虑 Lorentz 核（$\lambda \geq 4$）压制高索引项
4. 长期修复需要 C++ 层的 quad precision Chebyshev 迭代

---

## 进一步阅读

- `01_research_overview.md`：完整综述
- `17_claims_evidence_ledger.md`：Phase A–M 证据链
- `../gamma_mu_sim/`：Γ-μ 随机游走数值验证项目
- `shared/tbplas-internals.md` §12.3：C++ 层面的根因分析
