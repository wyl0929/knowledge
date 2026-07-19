<!--
Field: reductionism
Mode: orientation
Domain archetype: humanities_cultural
Created date: 2026-07-17
-->

# 99 Update Log / 更新日志

Last updated: 2026-07-17

## 使用说明

每次新增或修改 living layer 文件，都要在这里记录。不要静默修改 paper registry、gap table、project candidates 或 MVP plan。

Field / 领域：还原论（Reductionism）
Maintainer / 维护者：AI (research_onboarding_skill)

## Status Tags / 状态标签

- `seed`：来自草稿或已有笔记。
- `skimmed`：快速读过标题、摘要或摘要级材料。
- `parsed`：已经抽取方法、证据和局限。
- `verified`：已对照 primary source 或官方来源核验。
- `archived`：保留历史但不再作为活跃依据。
- `NEEDS_VERIFICATION`：有用但未核验。

## Log / 日志

| Date | File | Change | Reason | Source | Follow-up |
|------|------|--------|--------|--------|-----------|
| 2026-07-17 | ALL | 初始化 field pack | 用户提问"什么是还原论？" | general_interest_profile, orientation mode | 部分出版信息待核验 |
| 2026-07-17 | USER_BRIEF.md | 填充用户需求 | 记录本次调研目标与偏好 | 用户自然语言输入 | — |
| 2026-07-17 | 10_self_inventory.md | 填充背景快照 | 记录 orientation 模式与 profile | general_interest_profile | — |
| 2026-07-17 | 11_term_disambiguation.md | 填充术语澄清 | 区分三层还原论与相邻概念 | 哲学常识 + Nagel/Kim/Anderson | — |
| 2026-07-17 | 12_field_map.md | 填充领域地图 | 建立问题链与方法谱系 | 哲学常识 + 关键文献 | — |
| 2026-07-17 | 13_actor_map.md | 填充人物地图 | 记录 12 位关键人物与思想谱系 | 哲学常识 | 部分出版信息 NEEDS_VERIFICATION |
| 2026-07-17 | 14_paper_registry.md | 填充文献注册表 | 记录 10 篇关键文献 + 3 条阅读路径 | 哲学常识 | 部分 DOI/出版信息 NEEDS_VERIFICATION |
| 2026-07-17 | 00_beginner_guide.md | 生成入门指南 | 写给初学者的可读介绍 | 基于以上结构化文件综合 | — |
| 2026-07-17 | 01_research_overview.md | 生成研究概述 | 连续可读的领域报告 | 基于以上结构化文件综合 | — |
| 2026-07-17 | 90_QA.md | QA-001 社会学还原论 | 用户追问社会学方法论中的还原论 | Durkheim/Weber/Coleman/Archer/Elster | 部分出版信息 NEEDS_VERIFICATION |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
| 2026-07-17 | field pack | 初始化 `reductionism`，模式 `orientation`，domain `humanities_cultural`，profile `/home/wyl/.agents/skills/research_onboarding_skill/profiles/general_interest_profile.md` | 从模板创建 | init_field_pack.py | 先读取 USER_BRIEF.md，再按推荐 prompt 填充正文 |
| 2026-07-17 | subfield | 派生子方向 `power_reductionism_as_case`，模式 `quick_scan`，位置 `/home/wyl/project/knowledge/philosophy/reductionism/subfields/power_reductionism_as_case` | QA QA-001, user request | init_subfield_pack.py | 子方向继承父方向 USER_BRIEF；结论默认不回写父方向 |
