# 量子霍尔效应 Field Pack / 领域包

Field: 量子霍尔效应

Mode: quick_scan

Domain archetype: science_technical

Output path / 输出路径: /home/wyl/project/project/knowledge/physics/量子霍尔效应

Profile source / 背景来源: /home/wyl/.agents/skills/research_onboarding_skill/profiles/default_user_profile.md

Created date: 2026-06-10

Last updated: 2026-06-10

## 用途

本目录由 `research_onboarding_skill` 模板初始化，用于建立一个可检查、可迭代、可执行的科研领域进入包。

`USER_BRIEF.md` 保存本次调研的目标、重点、写作方式和回避事项。生成或更新主体文档前必须先读取它。

`10_self_inventory.md` 保存本次初始化时使用的 profile 快照。后续若用户背景发生变化，请在该文件记录覆盖项，并同步更新 `99_update_log.md`。

`00_beginner_guide.md` 是给第一次阅读的人看的入门指南；`01_research_overview.md` 是启发型领域总述；`02_frontier_compass.md` 用来回答内圈、中圈、边界、伪 gap 和用户切口。初始化时这些文件都是模板；结构化文件填充后，必须使用对应 prompts 生成正式文本。

`orientation` 模式用于兴趣了解，默认不生成 gap table、资产匹配、项目候选或 MVP。若 `domain_archetype` 是 `humanities_cultural` 且 brief 要求作品、案例或阅读路径，可生成 `15_primary_materials_and_reading_path.md` 与 `16_key_questions_and_cases.md`。

v0.10-rc3 编号说明：`00-02` 为阅读与判断层，`10-17` 为证据与领域层，`20-23` 为研究推进层，`90-99` 为 QA 与维护层；`USER_BRIEF.md` 是本次需求说明。

## 文件

- `USER_BRIEF.md`
- `00_beginner_guide.md`
- `01_research_overview.md`
- `02_frontier_compass.md`
- `10_self_inventory.md`
- `11_term_disambiguation.md`
- `12_field_map.md`
- `13_actor_map.md`
- `14_paper_registry.md`
- `17_claims_evidence_ledger.md`
- `20_gap_table.md`
- `22_project_candidates.md`
- `90_QA.md`
- `99_update_log.md`

## 下一步

建议使用：`prompts/phase_user_brief_capture.md -> phase1_term_breaking.md -> phase2_field_map.md -> phase4_gap_table.md -> phase6_project_ideas.md -> phase_frontier_compass.md -> phase_beginner_guide.md -> phase_summary_overview_report.md -> phase_readability_pass.md`。

## 自检命令

```bash
python research_onboarding_skill/scripts/check_pack_integrity.py /home/wyl/project/project/knowledge/physics/量子霍尔效应
```
