<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-16 18:19:30
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-16 20:47:07
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/stacking-dw/paper_review_li2012_prb.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-16
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/stacking-dw/paper_review_li2012_prb.md
 * @Description  : Li et al. (2012) PRB Rapid Comm. 阅读笔记
-->
# 论文精读：Li et al., PRB 85, 201404(R) (2012)

> **Xiao Li, Zhenhua Qiao, Jeil Jung, Qian Niu**
> "Unbalanced edge modes and topological phase transition in gated trilayer graphene"
> Phys. Rev. B 85, 201404(R) (2012) | arXiv:1203.4033
>
> 作者单位：UT Austin (Niu 组) + 合作者
>
> **DOI**: [10.1103/PhysRevB.85.201404](https://doi.org/10.1103/PhysRevB.85.201404)
> **Zotero Key**: `DNEATICJ`

---

## 1. 一句话总结

门控**手性堆叠（ABC）三层石墨烯**具有半整数谷霍尔电导（$\sigma_{xy}^V = 3/2$），导致**相反的 zigzag 边界上边缘模数量不同**——体系天然成为谷电流极化器。引入 Rashba SOC 后转变为 $Z_2$ 拓扑绝缘体。这是 ABA/ABC 堆叠畴壁拓扑态的先驱理论。

---

## 2. 背景与动机

### 2.1 已有知识背景：ABC 三层的特殊性

- ABC（rhombohedral）三层：低能色散 $E \propto k^3$，手征性 $l=3$
- 门控（施加层间电势差 $U$）→ 体能隙打开 → 体系成为**谷霍尔绝缘体**
- 谷 Chern 数：$C_V = 3 \times \text{sgn}(U)$（per valley, per spin）→ 半整数谷霍尔电导 $\sigma_{xy}^V = 3e^2/2h$

### 2.2 未解问题 / 本文填补的空白

- 体能隙内出现的手征边缘态数量 = $|C_V|$
- 但在 zigzag 边界处，谷 Hall 边缘态与**谷间耦合**相互作用 → 边缘态在两侧边界的分布**不对称**
- 结果：一侧有 $M$ 条，另一侧有 $M+1$ 条 → "非平衡"
- **核心空白**：ABC 三层的边缘态拓扑特征——特别是非平衡分布和谷极化——尚未被系统研究

---

## 3. 方法与模型

- **体系**: 门控 ABC 三层石墨烯，zigzag 纳米带几何
- **方法**: 连续模型 + 有效紧束缚哈密顿量，$k$-space 对角化计算能带和边缘态
- **核心参数**: 层间电势差 $U$（位移场），Rashba SOC 强度 $\lambda_R$
- **拓扑不变量**: 谷 Chern 数 $C_V$（谷霍尔相）、$Z_2$ 不变量 $\nu$（Rashba SOC 下）

---

## 4. 核心结果

### 4.1 非平衡边缘模

- **一侧 zigzag 边界**：$|C_V|$ 条边缘态
- **另一侧 zigzag 边界**：$|C_V| + 1$ 条边缘态（额外的态来自谷间耦合产生的边界束缚态）
- 对于 ABC 三层（$C_V = 3$）：一边 3 条，另一边 4 条

### 4.2 天然谷电流极化器

- $K$ 谷和 $K'$ 谷的边缘态具有**相反的手征性**
- 非平衡分布 → 不同谷的电流被导向**相反的边界**
- 无需任何外部设计 → 器件本身就是一个谷过滤器

### 4.3 Rashba SOC 诱导的 $Z_2$ 拓扑绝缘体

- 引入 Rashba 自旋轨道耦合（例如通过 TMD 衬底邻近效应）→ 自旋与动量锁定
- 体系从谷霍尔绝缘体 → **$Z_2$ 拓扑绝缘体**
- $Z_2$ 不变量 $\nu = 1$（奇数）→ 出现**奇数对螺旋边缘模**（helical edge modes）
- 螺旋边缘模 = 时间反演对称性保护的、自旋-动量锁定的无耗散边缘通道

### 4.4 拓扑相变

- 通过改变 $U$（位移场强度）或 Rashba SOC 强度，可以在以下相之间切换：
  - 普通绝缘体（$C_V = 0$）
  - 谷霍尔绝缘体（$C_V = 3$）
  - $Z_2$ 拓扑绝缘体（$\nu = 1$）

---

## 5. 与其他工作的关系

本文研究的是 ABC 三层的**外边界**（物理边缘），而非 ABA/ABC **内边界**（堆叠畴壁）。但两者共享相同的物理根源：

| 本文（外边界） | ABA/ABC 畴壁（内边界） |
|---|---|
| 体能隙由 $U$（门控）打开 | 体能隙由 $U$（门控）打开 |
| 边界处的拓扑态来自 $\Delta C_V$（真空 vs ABC 的谷 Chern 数差） | 畴壁处的拓扑态来自 $\Delta C_V$（ABA vs ABC 的谷 Chern 数差） |
| 非平衡边缘模 | 畴壁处的 1D 导电通道 |

**本文是 Jaskólski 2020（研究 ABA/ABC 内边界拓扑态）的直接理论基础。**

---

## 6. 亮点与局限

### 亮点

1. **谷 Chern 数系统计算**：首次给出 ABC 三层 $C_V=3$（per valley, per spin）→ $\sigma_{xy}^V = 3e^2/2h$
2. **非平衡边缘模概念**：两侧 zigzag 边界模式数不等 → 天然谷极化器
3. **Rashba SOC → $Z_2$ 拓扑绝缘体**：提供从谷霍尔相到 $Z_2$ 相的拓扑相变路径

### 局限

| 局限 | 说明 |
|---|---|
| 仅 zigzag 边界 | armchair 边界的边缘态行为可能不同 |
| 无真实堆叠畴壁 | 未研究 ABA/ABC 过渡区域本身的电子结构 |
| 简化模型 | 连续 + 有效 TB，未包含全部层间耦合参数 |
| 未包含无序 | 实际样品中的无序如何影响非平衡边缘态？ |

---

## 7. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **TBPM 验证** | 计算 ABC 三层 zigzag 纳米带的 $\sigma_{xx}$ 和 $\sigma_{xy}^V$，验证非平衡边缘模 |
| **谷极化器概念** | TBPM 可计算两侧边界的谷分辨电流 → 验证天然谷极化效应 |
| **DW 项目基础** | 本文的 $C_V=3$ 是理解 ABA/ABC 畴壁 $|\Delta C_K|$ 的关键参数 |
| **Rashba SOC 扩展** | 若 tbplas 支持 SOC，可验证 $Z_2$ 拓扑相变 |

---

## 8. 参考文献链

```
ABC 三层拓扑理论基础
├── Zhang et al., PRL 106, 156801 (2011) — ABC N 层谷 Chern 数 = N
├── ★ 本文 — ABC 三层 C_V=3，非平衡边缘模，Rashba → Z_2
└── Jaskólski & Sarbicki, PRB 102, 035424 (2020) — ABA/ABC 畴壁拓扑态（基于本文 C_V）

谷霍尔效应实验
├── Ju et al., Nature 520, 650 (2015) — 双层 AB/BA DW 实验
├── Li et al., Nat. Nanotech. 11, 1060 (2016) — 双层 EFW 实验
└── Yin et al., PRB 95, 081402(R) (2017) — 三层 ABA/ABC STM 实验（唯一实验基准）
```

---

*报告生成日期：2026-07-16 | 基于 arXiv:1203.4033 + PRB 85, 201404(R) (2012)*
