<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-14 22:03:29
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-14 22:03:30
 * @FilePath     : /project/knowledge/physics/强关联效应/10_self_inventory.md
 * @Description  :
-->
<!--
Field: 强关联电子体系
Mode: quick_scan
Domain archetype: science_technical
Created date: 2026-06-14
-->

# 10 Self Inventory / 用户背景快照

Last updated: 2026-06-14

## 使用说明

本文件是当前 field pack 使用的 profile 快照。它记录"这次生成时默认假设用户是谁、有没有研究资产、是否需要资产匹配"。它不同于 `USER_BRIEF.md`：profile 是长期背景或默认画像，brief 是本次任务的写作与调研要求。

不建议在旧 field pack 中自动同步最新 profile；旧包应保留当时快照，避免历史判断不可追溯。若需要更新旧包背景，请在 `99_update_log.md` 记录。

Field / 领域：强关联电子体系

Depth mode / 深度模式：quick_scan

## Profile source / 背景来源

/home/wyl/.agents/skills/research_onboarding_skill/profiles/default_user_profile.md

## Snapshot date / 快照日期

2026-06-14

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
- 理论合作：NEEDS_VERIFICATION
- 实验合作：NEEDS_VERIFICATION

### 与强关联领域的现有连接

- 已有：量子霍尔效应 field pack（分数量子霍尔效应本质是强关联问题）
- 已有：转角石墨烯 field pack（魔角石墨烯是当前最活跃的强关联实验平台之一）
- 缺口：用户目前的计算工具（TBPM、紧束缚）主要面向无相互作用或弱相互作用体系。进入强关联领域可能需要方法拓展或工具替换。
- 潜在桥梁：TBPM 可以计算单粒子谱函数，配合 DMFT 自洽可以做强关联 + 无序的输运研究；或利用量子霍尔效应的 existing knowledge 切入 FQHE 数值研究。
