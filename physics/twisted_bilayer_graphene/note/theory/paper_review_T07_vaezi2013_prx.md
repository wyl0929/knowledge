<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 16:16:34
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 16:16:40
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/paper_review_T07_vaezi2013_prx.md
 * @Description  :
-->
<!--
 * @Author       : AI精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/paper_review_T07_vaezi2013_prx.md
 * @Description  : T7: Vaezi/Liang/Ngai/Yang/Kim 2013 — 多层石墨烯倾斜边界的拓扑边缘态
-->

# Paper Review: Vaezi, Liang, Ngai, Yang & Kim (2013)

| 字段 | 内容 |
|------|------|
| **标题** | Topological Edge States at a Tilt Boundary in Gated Multilayer Graphene |
| **作者** | Abolhassan Vaezi, Yufeng Liang, Darryl H. Ngai, Li Yang, Eun-Ah Kim |
| **期刊** | PRX 3, 021018 (2013) |
| **DOI** | 10.1103/PhysRevX.3.021018 |
| **类型** | 理论 — 倾斜边界 (tilt boundary) 拓扑态 + SPT 分类 |
| **PDF** | ✅ reference/pdfs/ |

---

## 1. 核心贡献

将**倾斜边界 (tilt boundary)**——一种真实存在于 CVD 生长和外延石墨烯中的结构缺陷——提升为拓扑边界态平台。通过紧束缚 + DFT + SPT 分类三线并进，证明 AB-BA tilt boundary 在加栅压多层石墨烯中束缚无隙拓扑边缘态。

核心公式（chirally stacked $N$ 层）：

$$C_K = -C_{K'} = \frac{N}{2}\,\text{sgn}(t_\perp \Delta)$$

→ tilt boundary 两侧谷陈数跳变 → 每谷 $N$ 条螺旋边缘态。

## 2. 方法

- **紧束缚模型**：$t=2.8$ eV, $t_\perp=0.4$ eV, $\Delta=0.5$ eV, 系统大小 $200\times200$ 单元
- **DFT-LDA**：3.1 nm 宽 tilt boundary, 1.5 nm 宽域, 5 V/nm 垂直电场
- **SPT 分类**：Wen 的对称性保护拓扑相框架——将 chirally stacked 多层石墨烯分类为 $\mathbb{Z}$ 型 SPT（在时间反演 + 谷守恒 + $U(1)_c$ 电荷守恒条件下）

## 3. 关键结果

### 3.1 紧束缚结果

- 每个 $K$ 和 $K'$ 谷各 2 条边缘态/自旋（$N=2$）
- 右行和左行模在空间上分离 → 天然的谷过滤
- 边界局域应变导致 $K_1$ 和 $K_2$ Dirac 点能量分裂

### 3.2 DFT 验证

- 3.1 nm 宽 tilt boundary 在 5 V/nm 电场下 → 稳定出现两条 1D Dirac 色散
- 畴壁压缩应变升高一支模的能量，拉伸应变降低另一支

### 3.3 边界几何效应

| 边界类型 | 边界态 |
|------|:---:|
| 宽且平滑的 tilt boundary | ✅ 几乎无隙 |
| armchair-like tilt boundary | ⚠️ 谷投影重叠 → 明显开隙 |
| sharp abrupt boundary | ✅ 有态但谱复杂（额外平带） |

### 3.4 电导估计

- 单条 tilt boundary、无谷间散射：Landauer 电导接近 $N e^2/h$
- 多条 tilt boundary 网络、强谷间散射：整体电导远低于 $e^2/h$（趋于 variable-range-hopping）

### 3.5 SPT 分类新见解

- Chirally stacked $N$ 层在时间反演 + 无谷混合 + $U(1)_c$ 下 → $\mathbb{Z}$ 型 SPT
- 破坏谷守恒 → trivial phase
- LAF 相（layer-antiferromagnetic）→ $\mathbb{Z}_2$ 型而非 $\mathbb{Z}$ 型

## 4. 局限

- 谷守恒是拓扑保护的前提——armchair 边界、强短程杂质会使保护失效
- 紧束缚和 DFT 都揭示局域应变和平带带来的"脆弱模"
- 强关联效应仅在文末简要提及
- 三层（$N=3$）的理论预言缺乏 DFT 验证

## 5. 与 DW 项目关联

⭐⭐⭐⭐⭐ **DW 项目"真实器件网络"的工程约束说明书**。三层实用启示：

1. **结构性缺陷 = 拓扑导线**：tilt boundary 是 CVD 石墨烯中天然形成的——不需额外图案化
2. **边界几何控制谷过滤**：tilt boundary 的弯曲度和原子结构决定了谷过滤效率
3. **网络电导的失效条件**：多条 LSW 并联 + 强谷间散射 → 电导崩溃 → 器件设计的硬约束

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
栅控多层石墨烯中倾角晶界承载拓扑边缘态——晶界两侧不同 valley Chern number 保证模式存在。手征堆垛 N 层产生 N 支/谷，模式局域在倾角线上。从理想模型到实际缺陷几何的关键推广。

### Q3: 理论如何与实验结合?
预言 CVD/外延石墨烯天然晶界本身就是拓扑通道——无需栅压图案化。紧束缚+DFT 验证。为 Zhang 2024 (CVD LSW 束) 等实验提供理论先例。
