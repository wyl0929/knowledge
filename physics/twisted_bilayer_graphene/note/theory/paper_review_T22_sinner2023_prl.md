<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-11
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_sinner2022_prl.md
 * @Description  : T22: Sinner, Pantaleón & Guinea 2022 — 应变诱导 moire 准 1D 通道
-->
# Paper Review: Sinner, Pantaleón & Guinea (2022)

| 字段 | 内容 |
|------|------|
| **编号** | T22 |
| **标题** | Strain induced quasi-1D channels in twisted moiré lattices |
| **作者** | Sinner, Pantaleón & Guinea |
| **期刊** | PRL 131, 166402 (2023, arXiv:2210.07262) |
| **类型** | 理论 — 应变诱导准 1D 通道 |
| **PDF** | ❓ 待确认 |
| **DW.bib** | ❌ 未收录 |
| **Phase S 卡片** | [T22.md](../../Phase_S/cards.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

提出**第三种畴壁形成机制**——应变诱导准 1D 通道。⚠️ 2026-08-20 修正（§B.5#21）: 机制为**层内单轴应变**（类矢量势项、保持时间反演）与转角相互作用 → 倒空间单胞坍塌 → 近乎完美的 1D moiré 条纹 → 准 1D 通道 📜Q；临界应变由转角、应变与材料泊松比的简单关系给出 📜Q。旧版 "非均匀应变梯度 → 赝磁场" 表述无源已弃（原文无应变梯度、无赝磁场讨论）。

## 2. 物理机制

- 单轴应变（层内）+ 转角 → 倒空间单胞在临界应变处坍塌 → 1D moiré 图案 📜Q
- 应变项类似矢量势，但**不破坏时间反演对称**（原文 "resembles the conventional vector potential, which however does not break the time-reversal symmetry"）📜Q
- 临界应变判据: $\epsilon_c \approx 4.4\%$（石墨烯 $\nu\approx0.165$）/ $\approx 8\%$（TMD $\nu\approx0.19$）📜Q
- 诱导的 1D 行为由两个通常不可公度的周期刻画 📜Q
- 与 EFW/LSW 的关键区别：无需栅压图案化、无需特定堆垛——纯机械手段

## 3. 关键结果

1. 临界应变 $\epsilon_c$（≈4.4%/≈8%）处 mBZ 退化为 1D 条纹 → 准 1D 通道 📜Q
2. 通道方向由应变主轴决定，可设计
3. 通道间耦合随间距指数衰减 → 隔离度可控
4. 可为低转角 TBG 与 TMD 双层中观测到的 1D 通道图案提供解释 📜Q

## 4. 局限与开放问题

- 仅考虑静态应变，未涉及动态调控
- 单粒子图像，无序和温度效应未定量化
- 应变实现的实验精度要求极高（⚠️ 旧版 "~0.01% 控制精度" 无源已删，grep "0.01"=0）

## 5. 与用户研究的相关性

- **直接相关**：TBPM 可引入应变模块计算准 1D 通道的输运
- 若 DW 项目需探索非栅压畴壁机制，这是理论入口

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
层内单轴应变 + 转角 → 倒空间单胞在临界应变（≈4.4%/≈8%）处坍塌 → 近乎完美的 1D moiré 条纹 → 准 1D 弹道通道 📜Q。机制独立于电场和堆垛，是第三种产生拓扑通道的路径。

### Q3: 理论如何与实验结合?
预言应变可产生和操纵 1D 通道——无需栅压。与 Hsu 2020 (E8) 应变工程实验直接对话。为"应变电子学"提供可检验预言。

---

## 更正日志 (2026-08-20, S-REV)

- **§1–§3 机制重写**: 旧版 "非均匀应变梯度 → 有效矢量势/赝磁场"、"应变梯度 ≳0.1%/nm"、"赝磁场 ~100T" 均无源 → 改为原文机制: 层内单轴应变（类矢量势、保持 TRS）+ 转角 → 倒空间单胞坍塌 → 1D 条纹/准 1D 通道；临界应变 $\epsilon_c\approx4.4\%$（石墨烯）/≈8%（TMD）（grep "uniaxial"=11、"4.4"✓、"8%"✓）。依据: §B.5#21 + cards.md T22。
- **§4 删除 "~0.01% 控制精度"**: grep "0.01"=0 无源。依据: QC 无源数字规则。
