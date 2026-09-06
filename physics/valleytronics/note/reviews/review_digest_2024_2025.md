<!--
@Author       : AI 精读（paper-reading SKILL，综述类 → 谱系/观点地图，简报式）
@Date         : 2026-09-02
@Description  : 4 篇 valleytronics 综述的 QVH 相关性简报（非逐篇四块模板；QVH 核心见 paper_review_zandvliet2023_review.md）
-->

# 综述简报：4 篇 valleytronics 综述的 QVH 相关性

Last updated: 2026-09-02

> 本文件是简报，不是逐篇四块精读。结论先行：这 4 篇的**主战场是 TMD（或磁性 2D）谷电子学**，QVH（石墨烯/双层畴壁螺旋态）只是边缘章节；真正 QVH 本体的综述只有 `paper_review_zandvliet2023_review.md` 那一篇。

## 1. Schaibley et al. 2016 — Valleytronics in 2D materials（Nature Reviews Materials 1, 16055）

- **定位**：谷电子学的经典奠基综述，**TMD 为主**（MoS₂/WSe₂ 的谷 Zeeman、光谷选择性、谷 Hall）。
- **QVH 相关度**：低。仅在"Box 1: Physics of the valley Hall effect"给出谷霍尔电导通用公式 $\sigma_H^V\propto\int\Omega_{n,k}\,d^2k$，并把石墨烯/BLG 的谷 Hall（Shimazaki 2015、Su 2015）作为"破反演对称开谷 Hall"的例子一笔带过。
- **对本 field 价值**：术语口径参考（valley Hall effect 的 TMD 定义 vs 我们的 QVH 畴壁定义）；不作为 QVH 证据来源。
- 状态：skimmed（QVH 边缘，未逐段精读）。

## 2. Xu et al. 2025 — Valleytronics: Fundamental Challenges and Materials Beyond Transition Metal Chalcogenides（Small）

- **定位**：较新综述，明确**把视野扩展到 TMD 之外**（石墨烯/BLG/Xene）。
- **QVH 相关段落**（§2.3，已读）：AB/BA 双层石墨烯畴壁"exhibit chiral boundary states of quantum valley Hall insulators [79]"；平滑畴壁保持谷指标 → 垂直电场调制双层 gap → 谷极化电子沿畴壁反向传播；"intervalley scattering from smooth domain walls can be effectively neglected"。
- **对本 field 价值**：中。是"QVH 畴壁 = 谷保护 1D 通道"的**第二篇综述背书**，且明确"平滑畴壁 → 谷保护"的软保护逻辑（与本 field [PHY-QPI] §3.1 一致）。注意其用词 "chiral" 仍是本 field 已纠正的 helical/chiral 混用（`11_term_disambiguation.md` §2.4）。
- 状态：parsed（只精读 §2.3 QVH 段）。

## 3. Luo et al. 2024 — Valleytronics in two-dimensional magnetic materials（J. Phys. Mater. 专题综述）

- **定位**：磁性 2D 材料的**反常谷霍尔效应（anomalous valley Hall / ferrovalley）**——靠磁序自发改谷极化，而非电场开隙。
- **QVH 相关度**：低。与我们的 QVH（时间反演保护、总 σ_xy=0、电场开隙）是**不同物理**：它破时间反演（有净反常谷霍尔），我们是时间反演保护的 helical 畴壁态。
- **对本 field 价值**：低。只作为"谷电子学的磁性分支"边界对照（见 `12_field_map.md` Axis 1 的"内部量子数"轴）。
- 状态：skimmed（边界对照，未精读）。

## 4. Expanding our 2D vision（Nature Reviews Materials 2016 短评）

- **定位**：Nature Reviews Materials 创刊社论/短评（~2 页）。
- **QVH 相关度**：无实质内容，仅背景。可删或仅作"期刊栏目"索引。
- 状态：skimmed（130 行，无 QVH 实质）。

## 汇总

| 综述 | 年份 | 主战场 | QVH 相关度 | 处置 |
|---|---|---|---|---|
| Zandvliet et al. | 2023 | group IV Dirac 材料（QSHE + QVH） | **高（核心）** | 独立精读 `paper_review_zandvliet2023_review.md` |
| Xu et al. (Small) | 2025 | 超出 TMD 的谷电子学 | 中（§2.3 一段） | 本简报 + registry 登记 |
| Schaibley et al. (NRM) | 2016 | TMD 谷电子学 | 低（Box 1） | 本简报 + registry 登记 |
| Luo et al. (J. Phys. Mater.) | 2024 | 磁性 2D 反常谷霍尔 | 低（不同物理） | 本简报 + registry 登记（边界对照） |
| Expanding our 2D vision | 2016 | 创刊短评 | 无 | registry 登记（可略） |

*Last updated: 2026-09-02*
