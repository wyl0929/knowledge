<!--
@Author       : AI 精读（paper-reading SKILL，综述类 → 谱系/观点地图）
@Date         : 2026-09-02
@Description  : 综述精读：Zandvliet et al. 2023 — group IV 2D Dirac 材料中的拓扑保护 1D 态（QSHE + QVH）
@Source       : reference/Zandvliet 等 - 2023 - ...pdf（pdftotext + grep 反向核对）
-->

# Paper Review（综述）：Zandvliet et al. (2023) — group IV 二维 Dirac 材料中的拓扑保护 1D 态

| 字段 | 内容 |
|------|------|
| **标题** | Topologically protected one-dimensional electronic states in group IV two-dimensional Dirac materials |
| **作者** | Harold J.W. Zandvliet, Jort D. Verbakel, Qirong Yao, Kai Sotthewes, Pantelis Bampoulis |
| **机构** | Univ. Twente（Physics of Interfaces and Nanomaterials, MESA+）+ IBS（Pohang） |
| **年份 / 编号** | 2023；arXiv:2109.03071 |
| **期刊 / DOI** | 待核（带 SI 的 report/review，PDF 未显式给期刊名）⚠️ NEEDS_VERIFICATION |
| **类型** | **综述/report**（理论 + 实验图景，非单篇实验） |
| **PDF** | ✅ `reference/Zandvliet 等 - 2023 - ...pdf`（正文 ~26 页 + SI） |
| **精读日期** | 2026-09-02 |

> **阅读目的**：① 领域地图——确认 QVH 的权威综述口径；② 交叉验证本 field 的谷陈数约定（`11_term_disambiguation.md` §2.2）与"软保护"结论。属于 paper-reading 目的层 ②⑤。
> **综述类处理**：paper-reading SKILL 对"综述/其他"暂未定义（标 NEEDS_VERIFICATION），本文按**谱系/观点地图**处理，不做实验四块模板。

---

## TL;DR

这是目前**最贴近 QVH 本体**的综述：从 group IV 二维 Dirac 材料（石墨烯/硅烯/锗烯/锡烯）出发，讲两件事——① SOC 开隙 → $\mathbb{Z}_2$ 拓扑绝缘体 → QSHE（螺旋边缘态）；② 横向电场开隙 → 谷陈数反号 → AB/BA 畴壁上的 1D 拓扑保护态 = **QVH**（hexagonal network）。核心论点是：这类 1D 态**只被"弱"保护**——intervalley 散射（缺陷/杂质）会破坏它。

## 1. 综述的谱系结构（它把领域画成什么地图）

```text
group IV 2D Dirac 材料（graphene/silicene/germanene/stanene）
  ├─ 单层 + SOC → Z₂ 拓扑绝缘体 → QSHE（自旋锁定螺旋边缘态）
  ├─ 单层 + 横向电场 > 临界场 → 谷 Chern 反号 → QVH 绝缘体（谷锁定）
  └─ AB/BA 双层/小角 TBG + 横向电场 → 畴壁 QVH 1D 态（hexagonal network）
        └─ 保护条件：无 intervalley 散射（弱保护）
```

## 2. 本 field 相关的关键事实（📜Q = 原文，逐条 grep 核对）

### 2.1 谷陈数约定（单层 Xene，含 SOC + 电场）

- 单层（有 SOC）谷陈数（每谷每自旋）：$C_{\xi,s} = -\frac{\xi}{2}\frac{\xi s\lambda_{SO}}{|\xi s\lambda_{SO}|} = \pm\frac12$ 📜Q（Eq. 15）。
- 无外场时：总 Chern = 0、自旋 Chern = −2 → QSHE 📜Q（Eq. 16 后）。
- **加横向电场超临界后**："total valley Chern numbers are −1 and +1... the material can also be classified as **quantum valley Hall insulator**" 📜Q（Eq. 20 后）——即单层 QVH 的**每谷总谷陈数 = ±1**（= 2 自旋 × 1/2）。

### 2.2 双层（AB/BA）畴壁 QVH——本 field 的核心口径

- "the Chern numbers per valley are approximately quantized, i.e. $C_K = -C_{K'} \approx V/|V|$" 📜Q → **每谷谷陈数 = ±1（unit magnitude）**。✅ 印证本 field §2.2 定稿。
- "If V or the stacking order changes sign, **two topologically protected modes per valley** will emerge along the boundary" 📜Q → 每谷 2 条模。
- "the total number of conducting channels is **4 (2 channels per valley)** resulting a conductance of **4e²/h**" 📜Q ✅ 印证 4e²/h。
- "Intervalley scattering, i.e. scattering from valley to valley, **destroys the topological protection**" 📜Q → 软保护。

### 2.3 谷保护的判定（FFT）与"弱保护"定性

- intervalley 散射 → FFT 出现 $(\sqrt3\times\sqrt3)R30^\circ$ 斑；Verbakel 2021 用它证明网络态谷保护 📜Q。
- **Summary 原话**："These states are, however, **only weakly topologically protected**. The occurrence of defects or impurities... can give [rise] to intervalley scattering processes that have a detrimental effect" 📜Q —— 这是"谷保护=软保护"的**权威综述级措辞**，可直接引用。

### 2.4 机制细节（与本 field 证据阶梯对应）

- 网络 1D 态只在 $\theta\lesssim1^\circ$（AB/BA 畴足够大）可测 📜Q。
- AA 节点处 K/K′ 模只能直行或 ±60° 转弯（谷保持散射方向 3/6）📜Q。
- 双层同时有 intravalley 与 intervalley 散射；单层 intravalley 被赝自旋-动量锁定抑制 📜Q。

## 3. 引文挖掘（对 QVH 理论有价值的文章）

| 引文 | 为什么有价值 | 是否已在本 field |
|---|---|---|
| **[26] McCann & Koshino, Rep. Prog. Phys. 76, 056503 (2013)** | **双层石墨烯电子性质的权威综述**，是 2-band 有效模型（本 field 谷陈数推导的起点）的母本 | ❌ 新增 |
| **[44] Zhang, Jung, Fiete, Niu, MacDonald, PRL 106, 156801 (2011)** | **chirally-stacked N 层石墨烯**的谷陈数 $C_K=N/2$ 出处 → 直接解决 §8.2（三层 $C_v=3/2$ 而非 ±3） | ❌ 新增（关键） |
| **[42] Yao, Yang, Niu, PRL 102, 096801 (2009)** | 石墨烯谷霍尔边缘态理论（valley Hall edge states） | ❌ 新增 |
| **[21] Ezawa, JPSJ 84, 121003 (2015)** | Xene 单层拓扑绝缘体（SOC + 电场 → QVH/QSHE 相变）的权威理论综述 | ❌ 新增 |
| [43] ZMM 2013 PNAS / [45] San-Jose & Prada 2013 / [46] Martin 2008 / [65] Ramires & Lado 2018 | 谷陈数分类 / 螺旋网络 / EFW 零模 / PLL | ✅ 已在 registry |

## 4. 与本 field pack 的关系（增量价值）

1. **交叉验证**：逐条印证 `11_term_disambiguation.md` §2.2 的谷陈数定稿（每谷 ±1、ΔC_v=±2、2 模/谷、4e²/h），并给出"only weakly topologically protected"这一可引用的综述级措辞。
2. **§8.2 半解决**：单层每谷谷陈数 = 1/2（Eq. 15）、双层 = 1、chirally-stacked N 层 = N/2（引文 [44] 佐证）→ 三层 ABC 的"谷陈数"应为 ±3/2，而 [PHY-BERRY] 的"±3"是**每谷边界模数**（N=3），不是谷陈数。
3. **伪 gap 再确认**：综述明确区分 QSHE（自旋锁定，SOC）与 QVH（谷锁定，电场），且总 Chern 均为 0 —— 支持本 field 的"QVH ≠ QHE / ≠ QSHE"边界。

## 5. 反向核对 pass (2026-09-02)

pdftotext + grep 核对：$C_K=-C_{K'}\approx V/|V|$、"two modes per valley"、"4 channels"、"4e²/h"、"intervalley scattering... destroys the topological protection"、"only weakly topologically protected"、"quantum valley Hall insulator"、Eq. 15 $C_{\xi,s}=\pm1/2$ —— 均在原文命中。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-09-02 | 初读建档（综述 → 谱系/观点地图，非实验四块模板） |

*Last updated: 2026-09-02*
