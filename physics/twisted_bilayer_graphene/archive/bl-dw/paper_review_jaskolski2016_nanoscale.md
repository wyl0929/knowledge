<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-16 18:19:31
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-16 18:19:32
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/stacking-dw/paper_review_jaskolski2016_nanoscale.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-16
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/stacking-dw/paper_review_jaskolski2016_nanoscale.md
 * @Description  : Jaskólski et al. (2016) Nanoscale 阅读笔记
-->
# 论文精读：Jaskólski et al., Nanoscale 8, 6079 (2016)

> **W. Jaskólski, M. Pelc, L. Chico, A. Ayuela**
> "Existence of nontrivial topologically protected states at grain boundaries in bilayer graphene: signatures and electrical switching"
> Nanoscale 8, 6079 (2016) | arXiv:1603.04390
>
> 作者单位：Nicolaus Copernicus University (Poland) + CSIC (Spain)
>
> **DOI**: [10.1039/C5NR09018K](https://doi.org/10.1039/C5NR09018K)
> **Zotero Key**: `ZT_KEY_NEEDED`

---

## 1. 一句话总结

双层石墨烯中 AB/BA 堆叠晶界的拓扑保护态**对原子尺度缺陷具有稳健性**——即使晶界含有混合子晶格的五边形缺陷，无能隙态仍然存活。且栅压极性的反转可**改变**导电通道数量 → 电控开关效应。

---

## 2. 背景与动机

### 2.1 已有知识背景

- **Ju et al., Nature 520, 650 (2015)**：首次在门控双层石墨烯中实验观测到 AB/BA 畴壁处的导电通道——该领域的关键实验先驱
- 此前理论预测：拓扑保护态**仅**出现在保持子晶格序的畴壁中（即纯粹的 AB↔BA 堆叠翻转）
- **本文挑战**：如果晶界含有五边形-八边形缺陷（混合 $A$ 和 $B$ 子晶格），拓扑保护态还能存活吗？

### 2.2 未解问题 / 本文填补的空白

真实晶界几乎总是含有原子尺度缺陷。此前理论假设完美的子晶格序——本文首次测试了拓扑保护对缺陷的稳健性。

---

## 3. 方法与模型

### 3.1 模型

- **双层石墨烯紧束缚模型**：单 $p_z$ 轨道，层内最近邻 hopping $\gamma_0$，层间耦合 $\gamma_1, \gamma_3, \gamma_4$
- **晶界结构**：底层为完整 graphene，顶层含有一条**八边形-双五边形（8-5-5）缺陷线**——这种缺陷混合了子晶格
- 沿晶界方向的平移对称性 → 可用 $k_{\parallel}$ Bloch 波矢分类态

### 3.2 与之前模型的区别

| 之前模型 | 本文模型 |
|---|---|
| 纯 AB↔BA 堆叠翻转（无缺陷） | 晶界含有 8-5-5 拓扑缺陷 |
| 子晶格序完好 | **子晶格被缺陷混合** |
| 预测无能隙态 | ？ |

---

## 4. 核心结果

### 4.1 拓扑态对缺陷的稳健性

- **即使在含有 8-5-5 缺陷的晶界中，无能隙拓扑保护态仍然出现**
- 态的数量与纯堆叠翻转的预测一致 → 拓扑保护**不要求完美的子晶格序**
- 这一结果大大扩展了拓扑晶界态的适用范围——真实的晶界几乎总是含有缺陷

### 4.2 栅压反转下的不对称电导（电开关效应）

- 改变栅压极性（$+V_g \leftrightarrow -V_g$）→ **晶界处的导电通道数量发生变化**
- 正向栅压下：$N$ 条通道 → 电导 $G \approx N \times 2e^2/h$
- 反向栅压下：$M$ 条通道（$M \neq N$）→ 电导不同
- **应用**：栅压极性可作为**电开关**控制晶界的导电状态

### 4.3 缺陷态的角色

- 8-5-5 缺陷引入了**缺陷束缚态**（在体能隙内）
- 这些缺陷态与拓扑态杂化 → 在某些栅压下改变边缘态的有效数量
- 这解释了栅压不对称性的微观起源

---

## 5. 与其他工作的关系

| 本文（双层晶界） | 三层 ABA/ABC 畴壁（Jaskólski 2020） |
|---|---|
| 拓扑态对缺陷稳健 → 真实样品中可观测 | 三层畴壁态应对堆叠过渡区的无序稳健 |
| 栅压反转 → 不对称电导 | 栅压调控 → 金属-半导体转变（Jaskólski 2024） |
| 8-5-5 缺陷引入束缚态 | 三层畴壁的裂纹/缺陷可能引入类似效应 |

**本文是 Jaskólski 系列（2020, 2024）的方法论前驱**——建立了处理堆叠畴壁中拓扑态和缺陷相互作用的 TB 框架。

---

## 6. 亮点与局限

### 亮点

1. **拓扑保护对缺陷稳健**：首次证明 AB/BA 晶界的无能隙态可在 8-5-5 缺陷存在下存活
2. **电开关效应**：栅压极性反转改变导电通道数量 → 可编程拓扑电子学
3. **缺陷-拓扑态杂化机制**：揭示了缺陷束缚态如何与拓扑态耦合

### 局限

| 局限 | 说明 |
|---|---|
| 仅沿晶界方向的平移对称性 | 无法处理有限长度晶界或弯曲晶界 |
| 忽略电子-电子相互作用 | 纯单粒子紧束缚 |
| 未与实验定量对比 | Ju 2015 的实验数据未在本文中直接复现 |

---

## 7. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **TBPM 验证** | 构造含缺陷的 AB/BA DW → TBPM 计算 $\sigma_{xx}$ → 验证缺陷稳健性 |
| **电开关效应** | TBPM 扫 $D$ 正负极性 → 验证导电通道数量变化 |
| **DW 项目** | 本文证明 DW 拓扑态对缺陷稳健——你的 DW 计算的简并度结果应有类似稳健性 |

---

## 8. 参考文献链

```
AB/BA 畴壁拓扑态（双层）
├── Martin et al., PRL 100, 036804 (2008) — EFW 理论
├── Qiao et al., Nano Lett. 11, 3453 (2011) — LSW 的 TB 计算
├── Ju et al., Nature 520, 650 (2015) — 首个 DW 实验
├── ★ 本文 — 缺陷稳健性 + 电开关
├── Jaskólski & Sarbicki, PRB 102, 035424 (2020) — 三层 ABA/ABC 畴壁
└── Jaskólski, arXiv:2403.11143 (2024) — 多层金属-半导体转变
```

---

*报告生成日期：2026-07-16 | 基于 arXiv:1603.04390 + Nanoscale 8, 6079 (2016)*
