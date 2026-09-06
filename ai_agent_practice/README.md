<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-09-04
 * @FilePath     : /home/wyl/project/knowledge/ai_agent_practice/README.md
 * @Description  : AI Agent 使用经验与能力标定 — 知识包索引
-->

# ai_agent_practice — AI Agent 使用经验与能力标定

> **定位**: 沉淀"如何选型、配置、标定、验证 AI agent / LLM 完成某类工作"的可复用经验。
> **与 `systems_science/` 的区别**: systems_science 是「领域 + 研究方法论」（用系统科学/控制论视角组织研究与工作），本包聚焦「工具手艺（toolcraft）」——具体工具的选型、参数、能力标定与验证，不展开为系统科学理论。

## 与三个知识层的分工

| 层 | 位置 | 内容 |
|---|---|---|
| 项目数据/方法 | `Harness_test/Effort_test/`、`Harness_test/paper_search_test/` | 标定脚本、原始运行、结果数据 |
| **经验结论** | **本包 `ai_agent_practice/`** | 模型/推理深度对某类工作的影响结论、标定范式 |
| 可执行规则 | `~/.agents/skills/` | 固化为 skill 的操作指令 |

## 案例索引

| 全局编号 | 文件 | 标题 | 来源 |
|---|---|---|---|
| #100 | `case/10_case_study_dsh_plugin_design.md` | DSH 插件系统设计（九条通则） | 迁自 systems_science（2026-09-04） |
| #104 | `case/14_case_study_session_workflow_state_persistence.md` | 会话工作流与状态持久化 | 迁自 systems_science（2026-09-04） |
| #108 | `case/18_case_study_model_reasoning_depth_paper_search.md` | 模型与推理深度对搜索类工作的影响 | 迁自 systems_science（2026-09-04） |

## 编号约定

- 案例编号为**全局稳定 ID**，与 `systems_science/case/` 共享单调递增空间（#91 起）。
- 新案例从 **#109** 继续，无论落在哪个包。
- 跨包引用用「相对路径 + 稳定编号」，如 `../systems_science/case/09_case_study_delegation_accuracy_control.md`（#99）。

## 变更记录

- 2026-09-04：创建本包；从 `systems_science/case/` 迁入 #100 / #104 / #108（见 `systems_science/99_update_log.md` 迁移条目）。
