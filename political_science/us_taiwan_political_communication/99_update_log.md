<!--
Field: us_taiwan_political_communication
Mode: full_onboarding
Domain archetype: social_science
Created date: 2026-08-30
-->

# 99 Update Log / 更新日志

Last updated: 2026-08-30

## 使用说明

每次新增或修改 living layer 文件，都要在这里记录。不要静默修改 paper registry、gap table、project candidates 或 MVP plan。

Field / 领域：us_taiwan_political_communication
Maintainer / 维护者：Yulong Wang（用户）+ AI agent

## Status Tags / 状态标签

- `seed`：来自草稿或已有笔记。
- `skimmed`：快速读过标题、摘要或摘要级材料。
- `parsed`：已经抽取方法、证据和局限。
- `verified`：已对照 primary source 或官方来源核验。
- `archived`：保留历史但不再作为活跃依据。
- `NEEDS_VERIFICATION`：有用但未核验。

## Log / 日志

| Date | File | Change | Reason | Source | Follow-up |
|---|---|---|---|---|---|
| 2026-08-30 | field pack | 初始化 `us_taiwan_political_communication`，模式 `full_onboarding`，domain `social_science` | 用户提交新 fields 需求 | init_field_pack.py | 已完成全部正文填充 |
| 2026-08-30 | USER_BRIEF.md | 将用户研究设计拆解为时段/平台/文本对象/研究问题四要素，记录默认聚焦美国舆论场的工作假定 | phase_user_brief_capture | 用户原始消息 + agent 捕获 | 用户确认理论脉络（舆论场）后可更新 |
| 2026-08-30 | _search_notes_a_literature.md | 文献搜索 A（涉台美国舆论与框架研究，约 80 条，62 条 API 核验） | paper-search 7 层法（子代理） | OpenAlex + web_search | 供 13/14 号文件使用，保留为搜索记录 |
| 2026-08-30 | _search_notes_b_methods_data.md | 文献与方法搜索 B（框架方法、平台与数据可行性） | paper-search 7 层法（子代理） | OpenAlex + web_search | 供 15/16/23 号文件使用，保留为搜索记录 |
| 2026-08-30 | 10_self_inventory.md | 填充用户背景、资产表、覆盖项与待核验判断（X/新闻库/编码员为 UNKNOWN_USER_ASSET） | full_onboarding Phase 1 | profile 快照 + 用户消息 | 用户确认数据资产 |
| 2026-08-30 | 11_term_disambiguation.md | 概念边界契约 + 8 个核心概念 + 4 组关键对比（含 Yahoo 聚合器身份、演变≠机制） | Concept Boundary Gate | 经典文献条目 + 公开平台事实 | 经典文献页码级引用待精读补充 |
| 2026-08-30 | 12_field_map.md | 领域地图：4 条方法谱系 + 4 坐标轴 + 假设/瓶颈/过度声称表 | full_onboarding Phase 3 | 搜索笔记 A/B | 子代理文献回填后复核 |
| 2026-08-30 | 13_actor_map.md | 9 个作者/研究组条目（Guo/Vargo、Su/Borah、Walter/Ophir、CMU CASOS 等） | full_onboarding Phase 4 | 搜索笔记 A | 机构任职以 OpenAlex 记录为准 |
| 2026-08-30 | 14_paper_registry.md | 10 个★核心入口 + 4 组汇总表（理论/跨媒介/涉台实证/方法数据）+ 盲区记录；条目级 📜Q/⚠️待核验分级 | full_onboarding Phase 4 | 搜索笔记 A/B | 优先精读 Wang&Guo 2018、Tan 2026 |
| 2026-08-30 | 15_tool_registry.md | 10 个工具条目（语料获取 + 文本分析 + 基准） | full_onboarding Phase 4 | 搜索笔记 B | X API 价格与回溯天数复查 |
| 2026-08-30 | 16_metrics_and_benchmarks.md | 5 个指标 + 2 个 benchmark（含 Granger 流向检验与 Media Frames Corpus） | full_onboarding Phase 4 | 搜索笔记 B + 领域惯例 | α 阈值惯例出处待核验 |
| 2026-08-30 | 17_claims_evidence_ledger.md | C1–C7 中心论断 + Core Claims Gate + Operationalization Gate（P1 provisional） | Core Claims Gate + Operationalization Gate | 11/14 号文件 | MVP 完成后升级 operational_status |
| 2026-08-30 | 20_gap_table.md | G1–G7 缺口（涉台框架清单/帧层面流向/事件-阶段分离/编码手册/机器污染/数据可得性/文本-民意对照）+ 伪缺口表 | full_onboarding Phase 6 | 14/17 号文件 | G1/G4/G6 为 P0，由 23 MVP 验证 |
| 2026-08-30 | 21_asset_match.md | 资产-缺口矩阵 + 强匹配/误导匹配 + 合作需求 | full_onboarding Phase 7 | 10/20 号文件 | 3 项 UNKNOWN_USER_ASSET 待用户确认 |
| 2026-08-30 | 22_project_candidates.md | P1（用户研究设计，priority，provisional，含完整 Operationalization Contract）+ P2 + P3 | full_onboarding Phase 8 | 20/17 号文件 | P1 数据消歧后升级 |
| 2026-08-30 | 23_mvp_experiment_plan.md | 消歧型 MVP：佩洛西事件双平台取样与编码全链路试点（4 周计划 + 结果 A/B/C/D 判定） | full_onboarding Phase 9 | 22 号文件 | 待用户确认资产后启动 |
| 2026-08-30 | 02_frontier_compass.md | 内圈 7 条 + 中圈 7 项 + 边界问题 B-001~B-005 + 伪边界 + 用户切口 + 三条路线 | full_onboarding Phase 10 | 12/14/20/21/22 号文件 | 待读清单随精读推进 |
| 2026-08-30 | 01_research_overview.md | 15 节总述报告（链条位置/误解纠正/路线谱系/成熟度/代表工作/瓶颈/候选方向/阅读顺序） | full_onboarding Phase 11 | 全部结构化文件综合 | 精读后回补论点级证据 |
| 2026-08-30 | 00_beginner_guide.md | 人话入门（佩洛西事件贯穿例子、四派路线、混淆概念表、三困难、一页纸总结） | full_onboarding Phase 12 | 结构化文件 | 保持与 01/02 一致性 |
| 2026-08-30 | README.md | 更新包说明（用途与下一步） | 包级维护 | — | 无 |
