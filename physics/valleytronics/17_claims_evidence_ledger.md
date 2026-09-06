<!--
Field: 量子谷霍尔效应与谷电子学（Quantum Valley Hall Effect & Valleytronics）
Mode: full_onboarding
Domain archetype: science_technical
Created date: 2026-09-02
-->

# 17 Claims Evidence Ledger / 中心论断与证据账本

Last updated: 2026-09-02

## 使用说明

本文件是生成 `20_gap_table.md`、`22_project_candidates.md`、`23_mvp_experiment_plan.md` 前的 Core Claims Gate，并记录进入项目执行前的 Operationalization Gate 结论。下游判断必须引用或继承这里的中心论断、任务可操作化状态和允许结论层级。

证据分级：📜Q=原文事实 / 推导 / 📊F=读图估算 / 💭I=推断。

## Gate verdict / 门控结论

- 概念边界状态：**source_checked**（谷陈数约定已对照 Huang 2018 / ZMM 2013 / Verbakel 2021 原文定稿；trilayer 部分仍 NEEDS_VERIFICATION）。
- 中心论断状态：核心机制论断（C-001~C-005）source_checked；trilayer 泛化（C-006）suspected；工具可行性（C-007）NEEDS_VERIFICATION。
- 任务可操作化状态：**provisional**（priority project 的谷分辨读出指标尚未 code-audit，见 C-007）。
- 允许用于什么层级（允许进入的下游层级）：introductory_explanation、provisional_gap、project_candidate、mvp_design（消歧型）；strong_claim_not_allowed（禁止"谷保护已量化/三层已证"）。

## Core Claim / 中心论断

### C-001：QVH 不属量子霍尔效应

- 论断内容：QVH 总霍尔电导恒为 0（时间反演 $C_K+C_{K'}=0$），无 $\sigma_{xy}=\nu e^2/h$ 量子化平台；属谷电子学/畴壁态。
- 论断类型：concept_definition。
- 依赖概念边界：QVH vs QHE（`11_term_disambiguation.md` 对比组 1）。
- 支持下游：gap table（排除"做总霍尔量子化"型项目）、frontier compass（伪 gap）。
- 证据：QHE field 已补"QHE ≠ QVHE"边界；ZMM 2013 "total Chern number N=0 as required by time reversal"（📜Q）。
- 证据状态：source_checked。

### C-002：谷陈数约定（每谷 ±1，畴壁跳变 ±2）

- 论断内容：gapped 双层每谷谷陈数 $N_\nu=\pm1$（unit magnitude），畴壁跳变 $\Delta N_\nu=\pm2$，每谷每自旋 2 条边界模，两端口 $4e^2/h$；`[PHY-BERRY]` 的 "$C_v=\pm2$" 是把跳变误标成单谷值。
- 论断类型：concept_definition。
- 依赖概念边界：谷陈数 vs 畴壁跳变（`11_term_disambiguation.md` §2.2）。
- 支持下游：field map、metrics、MVP 指标定义。
- 证据：Huang 2018 "quantized at unit magnitude"（📜Q，pdftotext+grep）；ZMM 2013 "$N_\nu=\pm1$""$\Delta N_\nu=\pm2$"（📜Q）；Verbakel 2021 "$C_v=\pm1$、$\Delta C_v=\pm2$、4e²/h"（📜Q）。
- 证据状态：source_checked。

### C-003：谷保护是"软"保护

- 论断内容：谷保护靠动量失配（intervalley 需 $|\Delta K|\approx1.70$ Å⁻¹），只挡平滑势，原子点缺陷即破坏；比自旋保护脆弱。
- 论断类型：mechanism。
- 依赖概念边界：谷保护 vs 强保护（`11_term_disambiguation.md` §2.5）。
- 支持下游：project 的缺陷密度约束、MVP 的缺陷建模。
- 证据：[PHY-QPI] §3.1（📜Q 机制 + 💭I 类比）；Verbakel 2021 "单个缺陷即破坏"（📜Q）。
- 证据状态：source_checked。

### C-004：存在性 ≠ 拓扑保护（证据阶梯）

- 论断内容："看到畴壁态"（存在性）是"保护"（散射陈述）的必要非充分证据；证据阶梯 ①存在性 ②形态一致 ③谷保护(FFT) ④抗无序量化，第④级未闭环。
- 论断类型：mechanism。
- 依赖概念边界：存在性 vs 保护（`11_term_disambiguation.md` §2.6）。
- 支持下游：gap table G-001、frontier compass B-001。
- 证据：[PHY-BERRY] 证据阶梯（📜Q 实例 + 💭I 逻辑形式）。
- 证据状态：source_checked。

### C-005：谷保护的唯一直接实验证据是 Verbakel 2021 FFT

- 论断内容：Verbakel 2021 三对照（pristine/H 缺陷/TBG 网络）证 intervalley 背散射被抑制，是"谷保护"迄今唯一直接证据（级③，仍间接）。
- 论断类型：phenomenon。
- 支持下游：gap table、frontier compass 边界。
- 证据：E13 review 三对照表（📜Q）；"fully absent" 是定性判据（📜Q）。
- 证据状态：source_checked。

### C-006：三层（ABC/ABA）$C_v=\pm3$ 与谷保护"软"待核

- 论断内容：[PHY-BERRY] 写 tMBG 谷陈数 $C_v=\pm3$，但 ZMM 2013 对 chirally-stacked N 层给 $C_K=N/2$（N=3 半整数）且明言"ABA 三层谷陈数无法定义"；trilayer 谷保护是否同样"软"无直接实验。
- 论断类型：platform_bridge。
- 支持下游：gap table G-002。
- 证据：ZMM 2013 "$C_K=N/2$""cannot be defined on the ABA trilayer"（📜Q）；[PHY-BERRY] "$C_v=\pm3$"（💭I）。
- 证据状态：suspected（NEEDS_VERIFICATION，待 Chen 2021 / Phong 2026 核）。

### C-007：谷分辨 Kubo-Bastin 读出是否现成未知

- 论断内容：kubo_bastin.h 默认算总电导；能否/如何投影到 K/K′ 谷子空间需 code audit。
- 论断类型：feasibility。
- 支持下游：priority project 的 operational_status、MVP 指标定义。
- 证据：`15_tool_registry.md`（NEEDS_VERIFICATION）。
- 证据状态：NEEDS_VERIFICATION（待 code audit）。

### C-008（recommendation）：priority project 定在"谷陈数 + 谷保护 QPI 数值对标"，而非"谷霍尔电导量化"

- 论断内容：用户资产（tbplas + Kubo-Bastin + TBPM）最强匹配是复现谷陈数/边界模（ZMM 2013 LSW）+ 谷保护 QPI 判据（Verbakel 2021），而非声称"谷霍尔电导严格量子化"。
- 论断类型：recommendation。
- 依赖概念边界：C-002/C-003/C-004。
- 支持下游：22_project_candidates、23_mvp_experiment_plan。
- 证据状态：source_checked（基于资产匹配 + C-002/C-003）。

---

## Operationalization Gate / 任务可操作化门

### 任务可操作化结论

priority project（P-001）的任务可操作化状态为 **provisional**：测量定义（谷陈数、QPI 斑）与任务（"谷陈数反号束缚每谷 2 模""缺陷打开 intervalley 散射"）已在 `16_metrics_and_benchmarks.md` 明确，但"谷分辨读出是否现成"（C-007）未 code-audit，故 MVP 为**消歧型**：先验证测量定义与任务可行性，再谈最终贡献。

### 支撑下游项目的任务定义

- 声称要验证的任务：① gapped 双层 AB/BA 畴壁束缚每谷每自旋 2 条边界模（谷陈数跳变 $\Delta N_v=2$）；② 平滑势下 intervalley 背散射被抑制、原子缺陷打开它。
- 输入对象与允许输入集合：gapped 双层石墨烯紧束缚超胞（含 AB/BA 畴壁 + 垂直场 $\Delta$）；单点缺陷扰动；TBPM 规模 M≤2560。
- 目标变换：从"能带 + 畴壁 + 缺陷"到"边界模数 + QPI 斑有/无"。
- 解码或读出要求：边界模数（色散/态密度）+ 实空间 LDOS 的 2D FFT 斑。
- 失败/泄漏/后选择处理：缺陷算例必须与 pristine 同尺寸/同展宽对照；不得只在"恰好出斑"的参数下报告。
- baseline 公平性：ZMM 2013 LSW（每谷 2 模）与 Verbakel 2021 三对照为公平 baseline，用相同 TB 参数/展宽。
- 阳性结果能证明什么：数值上复现"谷陈数→边界模"与"软保护"机制（不是新发现，是能力验证）。
- 阳性结果不能证明什么：不能证明谷霍尔电导严格量子化；不能证明 trilayer 情形。
- 阴性结果意味着什么：若每谷模数≠2，优先怀疑谷分辨投影/边界条件实现有误，而非理论错。
- operational_status: **provisional**。

---

## Ledger Table / 汇总表

| Claim ID | 论断类型 | 论断内容（摘要） | 证据状态 | 允许结论层级 | 支持下游文件 | operational_status |
|---|---|---|---|---|---|---|
| C-001 | concept_definition | QVH ≠ QHE（总 σ_xy=0） | source_checked | introductory_explanation / provisional_gap | 02/12/20 | — |
| C-002 | concept_definition | 每谷 C_v=±1、ΔC_v=±2、4e²/h | source_checked | mvp_design | 11/16/23 | — |
| C-003 | mechanism | 谷保护是软保护 | source_checked | mvp_design | 11/12/22 | — |
| C-004 | mechanism | 存在性 ≠ 保护（证据阶梯） | source_checked | provisional_gap / project_candidate | 02/20 | — |
| C-005 | phenomenon | Verbakel 2021 = 谷保护唯一直接证据 | source_checked | provisional_gap | 02/20 | — |
| C-006 | platform_bridge | 三层 C_v=±3 / 谷保护软待核 | suspected | provisional_gap | 11/20 | — |
| C-007 | feasibility | 谷分辨 Kubo-Bastin 是否现成未知 | NEEDS_VERIFICATION | project_candidate | 15/22/23 | provisional |
| C-008 | recommendation | priority project 定在谷陈数+QPI 对标 | source_checked | mvp_design | 22/23 | provisional |

*Last updated: 2026-09-02*
