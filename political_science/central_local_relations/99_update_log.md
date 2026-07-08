<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-08 16:49:10
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-08 16:49:12
 * @FilePath     : /.agents/home/wyl/project/knowledge/political_science/central_local_relations/99_update_log.md
 * @Description  :
-->
<!--
Field: 央地矛盾、集权与分权的治理逻辑
Mode: quick_scan
Domain archetype: social_science
Created date: 2026-07-08
-->

# 99 Update Log / 更新日志

Last updated: 2026-07-08

---

## 2026-07-08: Field pack 初始化 (v1.0)

### 变更

| 文件 | 操作 | 说明 |
|------|------|------|
| `USER_BRIEF.md` | ➕ 新建 | 路由决策与需求说明 |
| `00_beginner_guide.md` | ➕ 新建 | 人话入门指南 |
| `01_research_overview.md` | ➕ 新建 | 领域总述报告 |
| `02_frontier_compass.md` | ➕ 新建 | 边界罗盘 |
| `10_self_inventory.md` | ➕ 新建 | 用户资产快照 |
| `11_term_disambiguation.md` | ➕ 新建 | 术语辨析与概念边界契约 |
| `12_field_map.md` | ➕ 新建 | 问题链与方法谱系 |
| `17_claims_evidence_ledger.md` | ➕ 新建 | 核心论断-证据台账 |
| `20_gap_table.md` | ➕ 新建 | 研究缺口表 |
| `22_project_candidates.md` | ➕ 新建 | 候选研究项目卡片 |
| `90_QA.md` | ➕ 新建 | 问答缓冲区 |
| `99_update_log.md` | ➕ 新建 | 本更新日志 |

### 种子材料

- `political_science/conflict.md`：用户自著系统性笔记，包含"行政分权 vs 行动集权"核心概念框架、唐/宋/明历史案例、美国联邦主义比较、现代治理方案。

### 关键决策

1. **Mode**: `quick_scan` — 种子文档质量高但用户未表达"正式进入领域"的意图，适合先建立完整知识地图。
2. **Domain archetype**: `social_science` — 政治学/治理研究，非人文文化型。
3. **概念创新处理**: 种子文档的"行政分权/行动集权"二维框架标记为 `working_definition`，需后续与学术文献对齐。
4. **未生成文件**: `13_actor_map.md`, `14_paper_registry.md`, `15_tool_registry.md`, `16_metrics_and_benchmarks.md`, `21_asset_match.md`, `23_mvp_experiment_plan.md` — quick_scan 模式不要求完整注册层和实验计划层。

### NEEDS_VERIFICATION 汇总

| 位置 | 内容 | 原因 |
|------|------|------|
| `01_research_overview.md` §6 | 学术文献方向和具体引用 | 未做系统文献检索 |
| `11_term_disambiguation.md` "行政分权/行动集权" | 是否已有文献做了类似区分 | 未对照政治学概念文献 |
| `17_claims_evidence_ledger.md` C3, C5 | 信息技术效应和控制论映射的分析价值 | 缺乏经验验证 |
| `20_gap_table.md` G1 | 二维框架是否已被覆盖 | 需检索概念文献 |
| `22_project_candidates.md` PC3 | 概念论文的可行性 | 需要系统文献检索确认缺口 |

### 下一步建议

1. **（最高优先）** 验证 G1：检索政治学文献确认"权力形态"维度是否已被覆盖。
2. **（高优先）** 如果好奇计算路线，可以试试 PC1（控制论模型，<200 行 Python）。
3. **（中优先）** 补充关键文献（Oates 1972, Tiebout 1956, Weingast, 周黎安 2007 等原文）。
