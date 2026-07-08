<!--
Field: 量子霍尔效应
Mode: quick_scan
Domain archetype: science_technical
Created date: 2026-06-10
-->

# 10 Self Inventory / 用户背景快照

Last updated: 2026-06-10

## 使用说明

本文件是当前 field pack 使用的 profile 快照。它记录“这次生成时默认假设用户是谁、有没有研究资产、是否需要资产匹配”。它不同于 `USER_BRIEF.md`：profile 是长期背景或默认画像，brief 是本次任务的写作与调研要求。

不建议在旧 field pack 中自动同步最新 profile；旧包应保留当时快照，避免历史判断不可追溯。若需要更新旧包背景，请在 `99_update_log.md` 记录。

Field / 领域：量子霍尔效应

Depth mode / 深度模式：quick_scan

## Profile source / 背景来源

/home/wyl/.agents/skills/research_onboarding_skill/profiles/default_user_profile.md

## Snapshot date / 快照日期

2026-06-10

## Profile snapshot / Profile 快照

### 基本身份与研究背景

- 身份：计算凝聚态物理研究者（Yulong Wang）
- 学科背景：物理学、计算物理
- 当前阶段：研究生/博士后
- 主要训练：凝聚态理论、数值模拟

### 主要研究方向

- 方向 1：石墨烯及相关二维材料的电子性质计算
- 方向 2：TBPM（紧束缚传播法）大规模量子输运模拟
- 相关领域：拓扑物态、量子输运、DOS 计算

### 已有代码和工具

| 工具 / 代码 | 类型 | 位置 | 成熟度 | 备注 |
|---|---|---|---|---|
| graphene.py | code | test/graphene.py | usable | 石墨烯紧束缚计算 |
| test_mpi.py | code | test/test_mpi.py | usable | MPI 并行测试 |
| TBPM/DOS 计算 | code | 工作区 | usable | 紧束缚传播法态密度计算 |
| submit.py | tool | ~/.agents/skills/cluster-workflow/assets/ | mature | SLURM 一键提交 |
| SLURM 脚本 | tool | slurm/ | mature | 集群作业模板 |

### 可调用资源

- 算力：远程 SLURM 集群（h3clogin），Intel oneAPI + MKL，多节点 MPI
- 数据：自产紧束缚计算数据
- 方法能力：紧束缚模型、能带理论、量子输运、MPI 并行、TBPM（熟练）
- 软件工程：Python、Shell、Git、SLURM（熟练）
- 写作与可视化：matplotlib、LaTeX（熟练）

### 当前科研目标

- 理解拓扑物态（量子霍尔效应等）的计算方法
- 寻找可结合现有 TBPM/石墨烯代码的研究切口

```markdown
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-10 17:08:03
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-10 17:08:03
 * @FilePath     : /project/.agents/skills/research_onboarding_skill/profiles/default_user_profile.md
 * @Description  :
-->
# Default User Profile / 默认用户背景

Last updated: 2026-06-10

## 基本身份与研究背景

- 身份：计算凝聚态物理研究者
- 学科背景：物理学、计算物理
- 当前阶段：研究生/博士后（进行中）
- 主要训练：凝聚态理论、数值模拟

## 主要研究方向

- 方向 1：石墨烯及相关二维材料的电子性质计算
- 方向 2：TBPM（紧束缚传播法）大规模量子输运模拟
- 相关领域：拓扑物态、量子输运、DOS 计算

## 已有代码和工具

| 工具 / 代码 | 类型 | 位置 | 成熟度 | 备注 |
|---|---|---|---|---|
| graphene.py | code | test/graphene.py | usable | 石墨烯紧束缚计算 |
| test_mpi.py | code | test/test_mpi.py | usable | MPI 并行测试 |
| TBPM/DOS 计算 | code | 工作区 | usable | 紧束缚传播法态密度计算 |
| submit.py | tool | ~/.agents/skills/cluster-workflow/assets/ | mature | SLURM 一键提交 |
| SLURM 脚本 | tool | slurm/ | mature | 集群作业模板 |

## 可调用课题组资源

- 算力：远程 SLURM 集群（h3clogin），Intel oneAPI + MKL
- 硬件：多节点 MPI 并行
- 数据：自产紧束缚计算数据
- 内部代码：TBPM、DOS 计算代码
- 组会或反馈机制：NEEDS_VERIFICATION

## 可调用合作者资源

- 理论合作：NEEDS_VERIFICATION
- 实验合作：NEEDS_VERIFICATION
- 工程合作：NEEDS_VERIFICATION
- 领域专家：NEEDS_VERIFICATION

## 方法能力

- 理论建模：紧束缚模型、能带理论、量子输运（中等）
- 数值模拟：MPI 并行、大规模矩阵对角化、TBPM（熟练）
- 机器学习：NEEDS_VERIFICATION
- 控制 / 优化：NEEDS_VERIFICATION
- 软件工程：Python、Shell、Git、SLURM（熟练）
- 写作与可视化：matplotlib、LaTeX（熟练）

## 当前科研目标

- 理解拓扑物态（量子霍尔效应等）的计算方法
- 寻找可结合现有 TBPM/石墨烯代码的研究切口
- NEEDS_VERIFICATION：具体论文目标
```

## General interest mode / 兴趣了解模式说明

如果本包使用 `general_interest_profile.md`，当前不使用研究资产匹配，也不假设用户拥有代码、硬件、合作者或实验资源。此时：

- `20_gap_table.md`、`21_asset_match.md`、`22_project_candidates.md`、`23_mvp_experiment_plan.md` 不应默认生成；
- 如需作品、案例、阅读路径，优先使用 `15_primary_materials_and_reading_path.md` 和 `16_key_questions_and_cases.md`；
- 若用户后续希望转为研究型进入，再切换到研究型 profile 并补充资产。

## 用户研究背景

- 身份与学科背景：
- 主要研究方向：
- 已有领域知识：
- 数学、理论、实验或写作基础：

## 用户已有工具或材料

| 工具 / 材料 | 类型 | 位置 | 成熟度 | 相关性 | 备注 |
|---|---|---|---|---|---|
|  | code / data / simulator / draft / primary works / archive / contact / other |  | seed / usable / mature | high / medium / low |  |

## 本次调用中的特殊覆盖项

这里记录用户在本次调用中明确给出的、与 profile 不一致或比 profile 更新的信息。写作偏好、内容重点和回避事项应优先写入 `USER_BRIEF.md`。

| 覆盖项 | 来源 | 对 field pack 的影响 | Last updated |
|---|---|---|---|
|  | user input / local note / other |  | YYYY-MM-DD |

## Claims to Verify / 待核验判断

| 判断 | 为什么重要 | 需要来源 | 状态 |
|---|---|---|---|
|  |  |  | NEEDS_VERIFICATION |
