# us_taiwan_political_communication Field Pack / 领域包

Field: us_taiwan_political_communication（美国涉台政治传播：台湾议题在美国舆论场中的框架建构与跨媒介传播）

Mode: full_onboarding

Domain archetype: social_science

Output path / 输出路径: /home/wyl/project/knowledge/political_science/us_taiwan_political_communication

Profile source / 背景来源: /home/wyl/.agents/skills/research-onboarding/profiles/default_user_profile.md

Created date: 2026-08-30

Last updated: 2026-08-30

## 用途

研究美国语境下（Yahoo News 与 X 平台）涉台政治事件触发文本的框架建构、三阶段演变（特朗普一期/拜登/特朗普二期，2017.01–2026.01）与跨媒介传播特征。用户研究设计已转写为 priority project P1（`22_project_candidates.md`），配套消歧型 MVP（`23_mvp_experiment_plan.md`）。

`USER_BRIEF.md` 保存本次调研的目标、重点、写作方式和回避事项。生成或更新主体文档前必须先读取它。

`10_self_inventory.md` 保存本次初始化时使用的 profile 快照。后续若用户背景发生变化，请在该文件记录覆盖项，并同步更新 `99_update_log.md`。

`00_beginner_guide.md` 是给第一次阅读的人看的入门指南；`01_research_overview.md` 是启发型领域总述；`02_frontier_compass.md` 用来回答内圈、中圈、边界、伪 gap 和用户切口。

v0.10-rc3 编号说明：`00-02` 为阅读与判断层，`10-17` 为证据与领域层，`20-23` 为研究推进层，`90-99` 为 QA 与维护层；`USER_BRIEF.md` 是本次需求说明。

## 文件

- `USER_BRIEF.md` — 本次需求说明（研究设计四要素）
- `00_beginner_guide.md` — 人话入门指南
- `01_research_overview.md` — 领域总述报告
- `02_frontier_compass.md` — 边界罗盘（B-001~B-005）
- `10_self_inventory.md` — 用户背景快照
- `11_term_disambiguation.md` — 概念边界契约
- `12_field_map.md` — 领域地图
- `13_actor_map.md` — 作者与研究组
- `14_paper_registry.md` — 文献注册表（含证据分级与盲区）
- `15_tool_registry.md` — 工具生态
- `16_metrics_and_benchmarks.md` — 指标与基准
- `17_claims_evidence_ledger.md` — 中心论断与两道门
- `20_gap_table.md` — 缺口表（G1–G7）
- `21_asset_match.md` — 资产匹配
- `22_project_candidates.md` — 项目卡片（P1 为 priority，provisional）
- `23_mvp_experiment_plan.md` — 消歧型 MVP 计划
- `90_QA.md` — 问答缓冲区
- `99_update_log.md` — 更新日志
- `_search_notes_a_literature.md` / `_search_notes_b_methods_data.md` — 文献搜索原始记录（provenance）

## 下一步

1. 用户确认三项数据资产（X/新闻库订阅、第二编码员、LLM API 预算）——见 `21_asset_match.md`。
2. 精读 Wang & Guo 2018 与 Tan et al. 2026（生成 paper_review），复核 P1 新颖性表述。
3. 按 `23_mvp_experiment_plan.md` 第 1 周启动：佩洛西事件三路数据探测。

## 自检命令

```bash
python /home/wyl/.agents/skills/research-onboarding/scripts/check_pack_integrity.py /home/wyl/project/knowledge/political_science/us_taiwan_political_communication
```
