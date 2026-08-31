<!--
Field: 物理学入门
Mode: orientation
Domain archetype: science_technical
Created date: 2026-08-30
-->

# 99 Update Log / 更新日志

Last updated: 2026-08-30

## 使用说明

每次新增或修改 living layer 文件，都要在这里记录。不要静默修改 paper registry、gap table、project candidates 或 MVP plan。

Field / 领域：物理学入门

Maintainer / 维护者：agent（research-onboarding v1.3 流程）

## Status Tags / 状态标签

- `seed`：来自草稿、已有笔记或记忆（待核验）。
- `skimmed`：已通过引文数据库/网络核验题名、年份与 venue。
- `parsed`：已经抽取方法、证据和局限。
- `verified`：已对照 primary source 或官方来源核验。
- `archived`：保留历史但不再作为活跃依据。
- `NEEDS_VERIFICATION`：有用但未核验。

## Log / 日志

| Date | File | Change | Reason | Source | Follow-up |
|---|---|---|---|---|---|
| 2026-08-30 | 全部文件 | 初始化 field pack：物理学入门（orientation，science_technical，general_interest_profile） | 用户要求"在 physics 下写一个物理学入门的包" | init_field_pack.py | 先读取 USER_BRIEF.md，再按 orientation 流程填充 |
| 2026-08-30 | USER_BRIEF.md | 写入用户原始需求、路线判断（orientation，confidence high）与当前有效要求 | Phase 0 意图路由 + brief 捕获 | phase_user_brief_capture.md | 后续若用户追加偏好，按 phase_user_brief_update.md 更新 |
| 2026-08-30 | 10_self_inventory.md | 填充 general_interest_profile 快照与待核验判断 | orientation 模式不结合个人背景 | 模板 | 若转研究型 profile，补充资产并切换模式 |
| 2026-08-30 | 11_term_disambiguation.md | 概念边界契约（规范工作范围/常见过度等同/禁止推出的结论）+ 5 组概念对比展开；concept_status: working_definition | Concept Boundary Gate（v1.0-rc1 门槛） | phase1_term_breaking.md | 前沿表述时效性待核验 |
| 2026-08-30 | 12_field_map.md | 分支谱系（9 分支）+ 4 个分支展开 + 4 坐标轴 + 核心假设与瓶颈 | Phase 2 field map | phase2_field_map.md | 瓶颈即开放问题，不升格为 gap（orientation） |
| 2026-08-30 | 13_actor_map.md | 9 条 actor 条目（历史谱系 + 当代共同体 + 导读入口） | Phase 4 actor map | 模板 + 知识综合 | 各条目的生平细节待核验 |
| 2026-08-30 | 14_paper_registry.md | 17 条 seed 来源，含证据分级（📜Q/💭I）；卷期页码与 DOI 统一不填写 | 文献 QC 协议 v1.3：禁止无源数字、禁止编造文献细节 | phase3_paper_parsing.md | 需按引文数据库补全卷期页码；4 条已 skimmed（题名/年份/venue 经网络核验） |
| 2026-08-30 | 00_beginner_guide.md | 生成正式入门指南：贯穿例子（苹果→微波背景）、3 条核心公式、4 个开放问题、分层阅读路径 | Phase 12 beginner guide | phase_beginner_guide.md | 已通过 readability pass |
| 2026-08-30 | 01_research_overview.md | 生成可读总述：链条位置、误解纠正、路线谱系、成熟度地图、开放问题、阅读顺序 | Phase 11 overview report | phase_summary_overview_report.md | 已通过 readability pass |
| 2026-08-30 | 90_QA.md | 清空模板占位，说明 QA 使用方式 | 保持 QA 为干净缓冲区 | 模板 | 后续追问从这里开始 |
| 2026-08-30 | 全部文件 | check_pack_integrity.py 自检（orientation 模式） | 质量保证 | scripts/check_pack_integrity.py | 修复检出问题后复检通过 |
| 2026-08-30 | 全部文件 | 文献 QC 反向核对 pass：全部数字逐条标注证据等级；未核验数字降级为 💭I 或 NEEDS_VERIFICATION | 文献 QC 协议第二层 | LITERATURE_QC_PROTOCOL.md | 人类抽检建议：14_paper_registry.md 中的 💭I 条目与全部卷期页码待补项 |
| 2026-08-30 | knowledge/README.md、knowledge/UPDATE_LOG.md | 在知识库总索引与工作区日志中登记本包 | 维护约定 | knowledge 根 README | 后续变更需同步两处 |
| 2026-08-30 | README.md | 目录重命名 physics/物理学入门 → physics/introduction，同步包内旧路径引用（Output path、自检命令） | 用户操作 | user rename | 知识库根层 README/UPDATE_LOG 已同步；Field 显示名保持"物理学入门"（与 Quantum_Hall_Effect 等包惯例一致） |
