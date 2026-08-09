<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27 23:51:36
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-27 23:51:40
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/chebyshev_precision/99_update_log.md
 * @Description  :
-->
<!--
Field: 切比雪夫迭代浮点精度问题
Parent: tbplas_conductivity
Created date: 2026-06-27
-->

# 99 Update Log / 更新日志

Last updated: 2026-06-27

## 更新策略

- stable layer：SKILL.md, templates, prompts, rubrics, scripts（由 skill 维护者更新）
- living layer：本 field pack 中的所有主体文档（由研究推进更新）

每次新增或修改 living layer 文档，必须在此记录。

---

## 更新记录

| 日期 | 操作 | 涉及文件 | 说明 |
|------|------|------|------|
| 2026-06-27 | 创建 | 全部文件 | 子方向 field pack 初始化（subfield_onboarding），基于 Phase A–M (2026-06-22~27) 完整诊断结果。父级：`tbplas_conductivity/`。知识来源：user memory (kubo-bastin-convergence.md), `shared/tbplas-internals.md` §12.3, `gamma_mu_sim/` 项目 |
| 2026-06-27 | 创建 | `USER_BRIEF.md` | 记录子方向调研重点与写作偏好 |
| 2026-06-27 | 创建 | `00_beginner_guide.md` | 硬币类比入门指南 |
| 2026-06-27 | 创建 | `01_research_overview.md` | 完整综述：背景→诊断→根因→修复 |
| 2026-06-27 | 创建 | `02_frontier_compass.md` | 边界罗盘：内圈/baseline/边界/伪gap/个人切口 |
| 2026-06-27 | 创建 | `10_self_inventory.md` | 用户资产快照（继承父级 + Phase A–M 新增） |
| 2026-06-27 | 创建 | `11_term_disambiguation.md` | 6 组概念边界契约 |
| 2026-06-27 | 创建 | `12_field_map.md` | 问题链 + 方法谱系 + 成熟度评估 |
| 2026-06-27 | 创建 | `17_claims_evidence_ledger.md` | 9 排除 + 4 确认 + 3 推测 + 2 建议 |
| 2026-06-27 | 创建 | `20_gap_table.md` | 5 缺口（2 confirmed, 2 suspected, 1 weak）+ 6 非缺口 |
| 2026-06-27 | 创建 | `22_project_candidates.md` | 3 候选项目卡片（含操作化契约） |
| 2026-06-27 | 创建 | `90_QA.md` | QA 缓冲区 + 常见问题预案 |

---

## 待办追踪

以下内容在本次初始化中**未创建**（子方向 pack 精简范围），如需补充请在后续更新中追加：

| 未创建文件 | 原因 |
|------|------|
| `13_actor_map.md` | 该子方向主要是内部诊断，暂不涉及外部研究组谱系 |
| `14_paper_registry.md` | 核心文献已在 `01_research_overview.md` 末尾列出 |
| `15_tool_registry.md` | 工具已在 `10_self_inventory.md` 中记录 |
| `16_metrics_and_benchmarks.md` | 指标定义已在 `22_project_candidates.md` 操作化契约中 |
| `23_mvp_experiment_plan.md` | PC-01 (gamma_mu_sim) 已在执行中，其 MVP 计划见 `../gamma_mu_sim/docs/plan.md` |
| `README.md` | 可由 `../README.md` 或父级索引覆盖 |

---

## 信息新鲜度

| 信息类别 | 截止日期 | 是否需要更新 |
|------|:---:|:---:|
| Phase A–M 根因诊断 | 2026-06-27 | 🟢 最新 |
| gamma_mu_sim T4 扫描状态 | 2026-06-27 (running) | 🟡 待 T4 完成后更新 |
| C++ quad precision 实现 | — | ⚪ 未开始 |
| 跨代码 KPM 对比 | — | ⚪ 未开始 |
