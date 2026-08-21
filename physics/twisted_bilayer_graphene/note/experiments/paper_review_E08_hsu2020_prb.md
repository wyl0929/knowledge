<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-11
 * @Description  : E8: Hsu et al. 2020
-->
# Paper Review: Hsu et al. (2020)

| 字段 | 内容 |
|------|------|
| **编号** | E8 |
| **标题** | Nanoscale Strain Engineering of Giant Pseudo-Magnetic Fields, Valley Polarization, and Topological Channels in Graphene |
| **作者** | Hsu et al. |
| **期刊** | Sci. Adv. 6, eaat9488 (2020) | **arXiv** | 2005.05532 |
| **类型** | 实验 — STM+应变: 赝磁场, 谷极化, 拓扑通道 |
| **Phase S 卡片** | [../../Phase_S/cards.md](../../Phase_S/cards.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

室温 STM/STS 结合**图案化纳米结构应变工程**（非纳米压痕）：将近无应变的大面积（~1 cm²）**单层石墨烯**铺在预先设计（architected）的纳米结构上，诱导整体反演对称性破缺 → 巨赝磁场（**最高 ~800 T**）、整体谷极化、周期性 1D 拓扑通道（手征模受保护传播）📜Q（摘要/正文）。展示应变可作为产生拓扑通道的独立手段。

## 2. 物理机制 / 实验方法

- 室温 STM/STS 📜Q（正文: "nanoscale strain engineering at room temperature"）
- 应变方式：architected 纳米结构（四面体 tetrahedron 阵列 / 平行褶皱 wrinkles）上覆盖单层石墨烯 📜Q（非"纳米压痕"，原文无 nanoindent）
- 赝磁场 B_S(r) 由形貌反演（一阶应变微扰 Dirac 哈密顿量 + MD 模拟）与 STS 中 Landau 能级间隔双重确定，两者一致 📜Q
- 赝朗道能级 E_n = sgn(n)√(...)（STS 谱中等间距特征由 LL 分离表征）📜Q
- 平行褶皱 = 周期性 1D 拓扑通道，用于谷劈裂与谷极化传播 📜Q（Fig. 5）

## 3. 关键结果

1. 赝磁场最高 ~800 T（由形貌计算的最大值）📜Q；某些应变区 ~600 T（由 LL 分离）📜Q——远超实验室真实磁场
2. 赝朗道能级在 dI/dV 谱中观测，Landau 能级分离随位置变化 = 赝磁场空间分布 📜Q
3. 整体谷极化由赝磁场方向决定——应变控制 📜Q（"global valley polarization"）
4. 应变梯度线上 1D 拓扑通道（褶皱 = 手征模保护传播通道）📜Q

## 4. 局限与开放问题

- 赝磁场空间分布不均匀——不同区域 B_S 差异大 📜Q（正文: "spatially varying tunneling spectra"）
- 仅局域 STM 测量——无全局输运 💭I（全文无输运数据）
- 样品为单层石墨烯——与双层畴壁（LSW/EFW）体系不同，属互补路线 💭I

## 5. 与用户研究的相关性

- 应变产生拓扑通道的实验验证——DW 项目若做应变工程，本文是基准
- 赝朗道能级是 TBPM 可直接计算的对标量

---

## 反向核对 pass (2026-08-19)

pdftotext 提取 → grep 逐项核对（PDF: `Hsu 等 - 2020 - Nanoscale strain engineering ...pdf`）：
- ✅ 800 T（最高，×3）/ ~600 T / 7 T（前作对照值）/ room temperature / monolayer / architected / tetrahedron / wrinkles / valley polarization / MD —— 全部在原文找到
- ⚠️ 原文无："~100-300 T"、"应变梯度 ≳0.1%/nm"、"应变不可逆超过 ~0.5%"、"纳米压痕"——旧 review 虚构数字，已删除

## 更正日志 (2026-08-19)

| 原表述 | 问题 | 修正 |
|---|---|---|
| 赝磁场 ~100-300 T / 可高达 ~300 T | 原文为 up to ~800 T（300 仅出现在前作引文标题与衬底厚度） | → 最高 ~800 T 📜Q |
| 纳米压痕/衬底图案化 | 原文方法为 architected 纳米结构（四面体/褶皱）上覆盖石墨烯 | → 图案化纳米结构应变工程 📜Q |
| 应变梯度 ≳0.1%/nm | 原文无 | → 删 |
| 应变不可逆超过 ~0.5% | 原文无 | → 删 |
| 未注明单层石墨烯 | 本文体系为单层石墨烯 | → 已标注 📜Q |

---

## Phase S 补充 (2026-08-11)

### Q1
室温 STM/STS + 图案化纳米结构应变工程（单层石墨烯）产生巨赝磁场（最高 ~800 T 📜Q）和周期性 1D 拓扑通道。dI/dV 谱展示赝朗道能级与谷极化。（2026-08-19 已按 PDF 修正旧版 ~100-300 T 误值）
