<!--
Field: 量子谷霍尔效应与谷电子学（Quantum Valley Hall Effect & Valleytronics）
Mode: full_onboarding
Domain archetype: science_technical
Created date: 2026-09-02
-->

# 10 Self Inventory / 用户背景快照

Last updated: 2026-09-02

## 使用说明

本文件是当前 field pack 使用的 profile 快照。它记录"这次生成时默认假设用户是谁、有没有研究资产、是否需要资产匹配"。它不同于 `USER_BRIEF.md`：profile 是长期背景或默认画像，brief 是本次任务的写作与调研要求。

Field / 领域：量子谷霍尔效应与谷电子学（QVH / Valleytronics）

Depth mode / 深度模式：full_onboarding

## Profile source / 背景来源

/home/wyl/.agents/skills/research-onboarding/profiles/default_user_profile.md（叠加本次 handoff §6 的覆盖项）

## Snapshot date / 快照日期

2026-09-02

## 用户研究背景

- **身份与学科背景**：计算凝聚态物理研究者（研究生/博士后进行中）。
- **主要研究方向**：石墨烯及相关二维材料的电子性质计算；TBPM（紧束缚传播法）大规模量子输运模拟；拓扑物态、量子输运、DOS 计算。
- **已有领域知识**：量子霍尔效应（已有独立 field pack）、TBG 畴壁态/边缘态（`twisted_bilayer_graphene` field pack + Phase S）、多层/转角石墨烯（`multilayer_graphene`）。
- **数学/理论/实验/写作基础**：紧束缚模型、能带理论、量子输运（中等）；MPI 并行、大规模对角化、TBPM（熟练）；matplotlib/LaTeX（熟练）。

## 用户已有工具或材料

| 工具 / 材料 | 类型 | 位置 | 成熟度 | 相关性 | 备注 |
|---|---|---|---|---|---|
| graphene.py | code | test/graphene.py | usable | high | 单层石墨烯紧束缚计算 |
| tbplas | code | 工作区（tight-binding propagation） | usable | high | 含 Kubo-Bastin Hall 电导能力 |
| kubo_bastin.h | code | Quantum_Hall_Effect/subfields/tbplas_conductivity/ | usable | high | Hall 电导数值（若新 field 做谷霍尔电导） |
| TBPM/DOS 计算 | code | 工作区 | usable | high | 紧束缚传播法态密度/输运 |
| submit.py + SLURM 脚本 | tool | ~/.agents/skills/cluster-workflow/assets/ + slurm/ | mature | medium | h3clogin 集群一键提交 |
| TBG 精读笔记与 PDF 库 | data/archive | twisted_bilayer_graphene/note/ + reference/pdfs/ | mature | high | 本 field 的种子来源（不重搜） |

## 本次调用中的特殊覆盖项（来自 handoff §6，优先于默认 profile）

| 覆盖项 | 来源 | 对 field pack 的影响 | Last updated |
|---|---|---|---|
| **约束：TBPM 规模上限 M≤2560** | handoff §6 | MVP/project 的模型规模必须在此上限内，超大体系需降尺度或另想办法 | 2026-09-02 |
| **约束：rescale 需 =−1（半带宽自动）** | handoff §6 | 数值实现细节约束，MVP 任务单须沿用此约定 | 2026-09-02 |
| **约束：FQHE 级多体方法不可及**（DMRG/精确对角化） | handoff §6 | 排除"谷物理 + 强关联多体"型 project，只在单粒子紧束缚层面切入 | 2026-09-02 |
| 现有代码：`graphene.py`（单层）+ QHE field 的 `kubo_bastin.h` | handoff §6 | 谷陈数/谷霍尔电导数值可直接对标这两份资产 | 2026-09-02 |

## 可调用资源

- **算力**：远程 SLURM 集群（h3clogin），Intel oneAPI + MKL，多节点 MPI 并行。
- **数据**：自产紧束缚计算数据；TBG reference/pdfs 文献库。
- **内部代码**：TBPM、DOS、graphene.py、tbplas。
- **合作者/领域专家/组会反馈**：NEEDS_VERIFICATION。

## 方法能力

- 理论建模：紧束缚模型、能带理论、量子输运（中等）。
- 数值模拟：MPI 并行、大规模矩阵对角化、TBPM（熟练）。
- 机器学习 / 控制优化：NEEDS_VERIFICATION。
- 软件工程：Python、Shell、Git、SLURM（熟练）。

## 当前科研目标

- 理解拓扑物态（量子霍尔效应等）的计算方法。
- 寻找可结合现有 TBPM/石墨烯/tbplas 代码的研究切口。
- 本 field 的直接目标：把谷陈数/谷输运/谷保护的通用理论做成可与 TBPM/Kubo-Bastin 对标的计算切口（具体见 `22_project_candidates.md` / `23_mvp_experiment_plan.md`）。

## Claims to Verify / 待核验判断

| 判断 | 为什么重要 | 需要来源 | 状态 |
|---|---|---|---|
| tbplas 是否已能直接算"谷分辨"霍尔电导（需把 Kubo-Bastin 分解到 K/K′ 谷） | 决定谷霍尔电导 MVP 是"改代码"还是"用现成能力" | code audit（QHE subfields/tbplas_conductivity + tbplas 源码） | NEEDS_VERIFICATION |
| TBPM M≤2560 对 ABC/ABA 三层畴壁体系的够用性 | 决定 TMBG 三层泛化项目在用户算力下是否可跑 | 手算 + 小规模试算 | NEEDS_VERIFICATION |
