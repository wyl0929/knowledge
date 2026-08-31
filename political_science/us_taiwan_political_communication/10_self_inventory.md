<!--
Field: us_taiwan_political_communication
Mode: full_onboarding
Domain archetype: social_science
Created date: 2026-08-30
-->

# 10 Self Inventory / 用户背景快照

Last updated: 2026-08-30

## 使用说明

本文件是当前 field pack 使用的 profile 快照。它记录“这次生成时默认假设用户是谁、有没有研究资产、是否需要资产匹配”。它不同于 `USER_BRIEF.md`：profile 是长期背景或默认画像，brief 是本次任务的写作与调研要求。

不建议在旧 field pack 中自动同步最新 profile；旧包应保留当时快照，避免历史判断不可追溯。若需要更新旧包背景，请在 `99_update_log.md` 记录。

Field / 领域：us_taiwan_political_communication

Depth mode / 深度模式：full_onboarding

## Profile source / 背景来源

/home/wyl/.agents/skills/research-onboarding/profiles/default_user_profile.md

## Snapshot date / 快照日期

2026-08-30

## Profile snapshot / Profile 快照

```markdown
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-10 17:08:03
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-10 17:08:03
 * @FilePath     : /project/.agents/skills/research-onboarding/profiles/default_user_profile.md
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

- 身份与学科背景：默认 profile 为计算凝聚态物理研究者；本包属于用户跨学科阅读/研究线（政治学、社会学类 field packs 已有多包）。
- 主要研究方向：TBPM 量子输运模拟（与本包无直接方法重叠，但提供了计算思维与数据处理习惯）。
- 已有领域知识：`political_science/fundamentals`（政治学基本概念与研究范式）、`us_two_party_politics`（美国两党政治，含 subfields/dsa_2026_wave）、`central_local_relations`、`corporatism`、`sociology/fundamentals`、`social_survey_methods`。尚无专门的传播学/媒体研究 field pack。
- 数学、理论、实验或写作基础：Python（熟练）、Shell、Git、LaTeX（熟练）；定量社会科学方法（回归、实验设计、编码）的掌握程度 UNKNOWN_USER_ASSET；英语阅读能力 UNKNOWN_USER_ASSET（涉台美国舆论研究几乎全部依赖英文文献与英文语料）。

## 用户已有工具或材料

| 工具 / 材料 | 类型 | 位置 | 成熟度 | 相关性 | 备注 |
|---|---|---|---|---|---|
| Python 环境 | code | 本机 | usable | high | 文本处理、API 调用、主题模型的基础 |
| LaTeX 写作 | tool | 本机 | mature | high | 后续论文/开题写作 |
| political_science/* field packs | archive | ~/project/knowledge/political_science/ | mature | medium | 政治学概念背景，不含媒体研究 |
| X/Twitter 数据访问权限（Academic API 或商业 Firehose） | data | — | — | high | UNKNOWN_USER_ASSET，直接决定回溯取样可行性 |
| 新闻档案订阅（NewsBank / LexisNexis / ProQuest） | data | — | — | high | UNKNOWN_USER_ASSET，影响 Yahoo News 历史语料获取 |
| 计算资源（SLURM 集群 h3clogin） | hardware | 远程集群 | mature | low | 大规模语料建模时可借力，MVP 阶段用不到 |
| 本研究设计文本 | draft | 用户消息 | seed | high | 本包 project candidate 的锚点 |

## 本次调用中的特殊覆盖项

这里记录用户在本次调用中明确给出的、与 profile 不一致或比 profile 更新的信息。写作偏好、内容重点和回避事项应优先写入 `USER_BRIEF.md`。

| 覆盖项 | 来源 | 对 field pack 的影响 | Last updated |
|---|---|---|---|
| 用户正在撰写"美国涉台政治传播"方向的新 field pack，并给出了含时段、平台、事件取样与三大研究问题的完整研究设计 | user input | 本包采用 full_onboarding + social_science；研究设计进入 20/21/22/23 层作为 priority project | 2026-08-30 |
| 默认 profile 是物理研究者，与政治传播领域无专业重叠 | profile 与任务的领域差距 | 资产匹配按"通用计算+写作资产 + 未知的数据资产"处理，不做过度假设 | 2026-08-30 |

## Claims to Verify / 待核验判断

| 判断 | 为什么重要 | 需要来源 | 状态 |
|---|---|---|---|
| 用户能否获得 X/Twitter 2017–2026 历史推文（API 或公开数据集） | 决定 MVP 的数据可行性 | 用户确认（订阅状态）/ 平台政策文档 | UNKNOWN_USER_ASSET |
| 用户能否获得 Yahoo News 历史文章（站内搜索/档案库/存档机构） | 决定新闻组织一侧取样方式 | 用户确认 / 档案库目录 | UNKNOWN_USER_ASSET |
| 用户是否具备人工内容分析（编码）或计算文本分析经验 | 决定 MVP 选人工编码还是计算路径 | 用户确认 | UNKNOWN_USER_ASSET |
| 本研究设计是否已有对应开题/导师/时间预算 | 决定研究推进层的优先级 | 用户确认 | NEEDS_VERIFICATION |
