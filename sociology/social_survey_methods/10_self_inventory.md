<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-17 20:13:44
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-17 20:13:45
 * @FilePath     : /.agents/home/wyl/project/knowledge/sociology/social_survey_methods/10_self_inventory.md
 * @Description  :
-->
<!--
Field: 社会调研方法论——从日常对话到结构化判断
Mode: quick_scan
Domain archetype: social_science
Created date: 2026-08-17
-->

# 10 Self Inventory / 用户背景快照

Last updated: 2026-08-17

## 快照说明

本文件保存本次 field pack 初始化时使用的 profile 快照。

- Profile source / 背景来源：`research_onboarding_skill/profiles/default_user_profile.md`（快照日期 2026-06-10）
- 本次调研覆盖项见下文“本次调研覆盖项（override）”。

## Profile 快照

### 基本身份与研究背景

- 身份：计算凝聚态物理研究者
- 学科背景：物理学、计算物理
- 当前阶段：研究生/博士后（进行中）
- 主要训练：凝聚态理论、数值模拟

### 主要研究方向

- 石墨烯及相关二维材料的电子性质计算
- TBPM（紧束缚传播法）大规模量子输运模拟
- 相关领域：拓扑物态、量子输运、DOS 计算

### 已有代码和工具

| 工具 / 代码 | 类型 | 位置 | 成熟度 | 备注 |
|---|---|---|---|---|
| graphene.py | code | test/graphene.py | usable | 石墨烯紧束缚计算 |
| test_mpi.py | code | test/test_mpi.py | usable | MPI 并行测试 |
| TBPM/DOS 计算 | code | 工作区 | usable | 紧束缚传播法态密度计算 |
| submit.py | tool | ~/.agents/skills/cluster-workflow/assets/ | mature | SLURM 一键提交 |
| SLURM 脚本 | tool | slurm/ | mature | 集群作业模板 |

### 方法能力

- 理论建模：紧束缚模型、能带理论、量子输运（中等）
- 数值模拟：MPI 并行、大规模矩阵对角化、TBPM（熟练）
- 软件工程：Python、Shell、Git、SLURM（熟练）
- 写作与可视化：matplotlib、LaTeX（熟练）

## 本次调研覆盖项（override）

以下覆盖项在 2026-08-17 由用户本次需求确立：

1. **不结合计算物理背景找研究课题**：本 pack 不试图把社会调研与 TBPM/量子输运强行连接。计算物理背景仅作为"系统化思维 + 数据处理直觉"的一般资产被认可。
2. **定位为跨学科知识整合者**：本 pack 以学术入门级标准写作，不预设社会科学专业训练；目标是建立基本地图、边界感与可执行的操作起点。
3. **无社会科学调研经验**：田野经验、访谈训练、编码实操经验均无（UNKNOWN_USER_ASSET，默认按无处理）。
4. **可用资产**：系统的文档管理习惯（knowledge 体系）、工程化落地能力、可调用 DeepSeek API 作为讨论伙伴。

## 与本领域的资产匹配（初步）

| 本领域需要的 | 用户拥有 | 用户缺少 |
|---|---|---|
| 系统化流程设计 | ✅ 工程化落地能力强 | — |
| 数据分析直觉（噪声/采样/信噪比） | ✅ 可迁移的思维模式 | 社会科学统计训练 |
| 理论透镜（符号互动论等） | 刚起步（本 pack 即起点） | 系统阅读 |
| 访谈与田野经验 | — | ❌ 尚无（默认按无处理） |
| 编码实操 | — | ❌ 尚无（默认按无处理） |
| 伦理审查经验 | — | ❌ 尚无（默认按无处理） |

**含义**：适合用户启动的是"流程工具化"类项目（问题库、编码手册、卡片模板），而非"理论创新"或"大规模田野"类项目。
