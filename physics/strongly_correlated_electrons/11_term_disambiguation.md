<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-14 22:04:11
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-14 22:04:12
 * @FilePath     : /project/knowledge/physics/strongly_correlated_electrons/11_term_disambiguation.md
 * @Description  :
-->
<!--
Field: 强关联电子体系
Mode: quick_scan
Domain archetype: science_technical
Created date: 2026-06-14
-->

---
document_type: term_disambiguation
schema_version: v0.10-rc2
field: "强关联电子体系"
last_updated: 2026-06-14
---

# 11 关键概念与边界说明

Last updated: 2026-06-14

## 概念边界契约 / Concept Boundary Contract

### 用户原始术语

用户使用了"强关联效应"、"强关联现象"、"强关联理论"和"强关联计算"这四个关联术语。

### 规范工作范围

本 field pack 实际讨论的范围包括：

1. **强关联电子体系 (Strongly Correlated Electron Systems, SCES)**：电子-电子相互作用能与动能可比或更大，导致朗道费米液体理论失效的多体量子体系。核心判据：$U/W \gtrsim 1$，其中 $U$ 是 onsite Coulomb 排斥，$W$ 是裸带宽。

2. **莫特物理 (Mott Physics)**：由强库仑排斥驱动的金属-绝缘体转变（莫特转变）及其附近物理。核心概念是：即使能带理论预言为金属（半满），电子也可以因彼此排斥太大而局域化。莫特绝缘体（Mott insulator）是其标志性相。

3. **非费米液体 (Non-Fermi Liquid, NFL)**：准粒子图像失效的金属态。费米液体中准粒子权重 $Z > 0$、电阻率 $\rho \propto T^2$；NFL 中准粒子可能不存在，或散射率呈反常温度依赖（如 $\rho \propto T$）。

4. **量子临界性 (Quantum Criticality)**：连续量子相变点及其附近有限温区域中的标度行为。量子临界点（Quantum Critical Point, QCP）通常分离有序相和无序相，其上方可能出现奇异金属（strange metal）等非费米液体行为。

5. **高温超导 (High-Temperature Superconductivity, HTSC)**：转变温度显著超过 BCS 理论预期（通常指 $T_c > 30$ K，尤其是铜氧化物中超过液氮温度的 $T_c$）。普遍认为其配对机制来自强关联效应而非传统声子媒介。

6. **自旋液体 (Quantum Spin Liquid, QSL)**：即使到绝对零温也不形成磁序的量子无序态，存在长程量子纠缠和分数化激发（如自旋子 spinon）。是强阻挫磁性绝缘体中的典型强关联相。

7. **重费米子 (Heavy Fermion)**：f 电子与传导电子杂化导致准粒子有效质量 $m^*$ 可达裸电子质量的 $10^2$–$10^3$ 倍的金属态。典型材料为含 Ce、Yb、U 的金属间化合物。

### 上位概念、下位概念与相邻概念

- **上位概念**：量子多体物理 (quantum many-body physics)、关联电子材料 (correlated electron materials)
- **下位概念**（核心物理效应）：莫特转变、电荷序（charge ordering）、轨道序（orbital ordering）、自旋密度波（SDW）/ 电荷密度波（CDW）、高温超导、非费米液体、奇异金属（strange metal）、赝能隙（pseudogap）、重费米子、近藤效应（Kondo effect）、价键固体（valence bond solid）、自旋液体、量子临界点、分数化激发、Luttinger 液体（一维）
- **下位概念**（理论框架）：Hubbard 模型、t-J 模型、Anderson 杂质模型、近藤晶格模型、动力学平均场（DMFT）、Gutzwiller 投影、隶粒子方法（slave particle）、共形场论（CFT）、全息对偶（AdS/CFT）
- **下位概念**（计算方法）：量子蒙特卡罗（QMC）、密度矩阵重整化群（DMRG）、张量网络（tensor networks）、精确对角化（exact diagonalization）、动力学平均场 + 第一性原理（DFT+DMFT）、泛函重整化群（fRG）
- **相邻但不同的概念**：
  - 弱关联金属 / 费米液体（准粒子存在，$Z > 0$）
  - 能带绝缘体 / 半金属（由能带填充决定，非关联驱动）
  - 弱耦合超导（BCS 机制，电声子耦合 $\lambda \ll 1$）
  - 安德森局域化（无序驱动，非相互作用）
  - 密度泛函理论（DFT）的 Kohn-Sham 能带（基态单粒子图像，通常低估关联效应）
  - 拓扑绝缘体（能带拓扑，虽然可与强关联共存但原则上独立）

### 常见过度等同

| 方便说法 | 可能导致错误结论的原因 |
|---------|---------------------|
| "强关联 = Hubbard 模型" | Hubbard 模型是最简玩具模型，但真实材料中轨道结构、p-d 杂化、多带效应、自旋-轨道耦合等同样重要。把强关联完全等同于 Hubbard 模型会漏掉多轨道物理的丰富性。 |
| "强关联 = 莫特绝缘体" | 强关联不仅导致绝缘体，也产生非费米液体金属、奇异金属、非常规超导等多种非平庸金属态。只说"莫特"会漏掉强关联金属物理这一整个分支。 |
| "DMFT = 精确解" | DMFT 在无限维严格，但在有限维（尤其是二维）是近似。它精确处理了局域关联，但忽略了空间涨落。二维强关联体系通常需要 DMFT 以外的空间关联修正（如 cluster DMFT、D$\Gamma$A）。 |
| "DFT 算不准强关联体系" | 部分正确但不完整。DFT（Kohn-Sham）做能带确实会错失关联驱动的绝缘体（如莫特绝缘体被错误地预测为金属），但 DFT+U、DFT+DMFT 等延伸方案已经把强关联效应部分恢复。问题不在于"DFT 错了"，而在于需要超越标准 Kohn-Sham 范式。 |
| "自旋液体 = 无磁序" | 无磁序只是必要条件，不是充分条件。真正的量子自旋液体要求分数化激发和长程纠缠。许多自旋玻璃（spin glass）或无序诱导的无序态也不形成磁序，但不是自旋液体。 |
| "强关联 = 不可计算" | 特定体系和方法确实面临指数墙（指数大的希尔伯特空间），但过去三十年发展了 QMC、DMRG、张量网络、DMFT 等工具，很多强关联问题已经可以定量计算。关键在于选择合适的方法和体系。 |

### 本包使用的操作定义

在本 field pack 中，强关联电子体系的"操作定义"为：

> 电子体系满足以下两个条件之一：
> 1. 局域库仑排斥 $U$ 与带宽 $W$ 之比 $\gtrsim 1$，使得微扰论（以 $U/W$ 为小量）失效；
> 2. 观测到的物理性质（输运、热力学、光谱）无法用朗道费米液体理论或单粒子能带图像定性解释。
>
> 这两个条件不需要同时满足；第二个条件包含了目前理论尚不完整的体系。

### 操作定义的自洽检查

- [x] 定义包含已知的核心强关联体系：莫特绝缘体、铜氧化物超导体、重费米子、自旋液体等。
- [x] 定义排除弱关联费米液体（如碱金属、简单金属）。
- [x] 定义避免完全依赖尚存争议的理论概念（如非费米液体的微观起源）作为判据。
- [x] 定义中的两个条件互相独立——条件 1 是理论参数判据，条件 2 是实验现象判据。
