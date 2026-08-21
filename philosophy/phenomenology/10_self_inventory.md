<!--
Field: phenomenology
Mode: orientation
Domain archetype: humanities_cultural
Created date: 2026-08-21
-->

# 10 Self Inventory / 用户背景快照

Last updated: 2026-08-21

## 使用说明

本文件是当前 field pack 使用的 profile 快照。它记录"这次生成时默认假设用户是谁、有没有研究资产、是否需要资产匹配"。它不同于 `USER_BRIEF.md`：profile 是长期背景或默认画像，brief 是本次任务的写作与调研要求。

不建议在旧 field pack 中自动同步最新 profile；旧包应保留当时快照，避免历史判断不可追溯。若需要更新旧包背景，请在 `99_update_log.md` 记录。

Field / 领域：phenomenology（现象学）

Depth mode / 深度模式：orientation

## Profile source / 背景来源

/home/wyl/.agents/skills/research-onboarding/profiles/general_interest_profile.md

## Snapshot date / 快照日期

2026-08-21

## Profile snapshot / Profile 快照

```markdown
# General Interest Profile / 一般兴趣了解画像

这是一个不包含任何个人背景假设的内置 profile。它不是研究型用户画像，也不假设用户
拥有任何代码、平台、实验资源、合作者或特定研究方向。

适用场景：用户只是对某个领域感兴趣、好奇某个概念、想先获得可读入门介绍、
暂时不考虑做研究或结合自身资产。

使用原则：
- 不假设用户拥有任何代码、平台、实验资源或研究背景；
- 不自动生成个人资产匹配；
- 不自动把方向推成项目候选；
- 不强行输出 gap table、project candidates 或 MVP；
- 优先生成易读的 beginner guide、基础 overview、关键概念说明、field map 和 seed paper list。

输出偏好：主体中文；重要术语先解释再括号标注英文；适当给公式/流程/例子；
可靠性边界集中说明；不强行输出 gap/project/MVP。
```

## General interest mode / 兴趣了解模式说明

本包使用 `general_interest_profile.md`，当前不使用研究资产匹配，也不假设用户拥有代码、硬件、合作者或实验资源。此时：

- `20_gap_table.md`、`21_asset_match.md`、`22_project_candidates.md`、`23_mvp_experiment_plan.md` 不应默认生成；
- 作品、案例、阅读路径由 `15_primary_materials_and_reading_path.md` 和 `16_key_questions_and_cases.md` 承载；
- 若用户后续希望转为研究型进入，再切换到研究型 profile 并补充资产。

## 用户研究背景

- 身份与学科背景：未指定（一般兴趣读者）。
- 主要研究方向：未指定。
- 已有领域知识：未假设；按零基础哲学读者设计入门文本。
- 数学、理论、实验或写作基础：未指定。

## 用户已有工具或材料

| 工具 / 材料 | 类型 | 位置 | 成熟度 | 相关性 | 备注 |
|---|---|---|---|---|---|
| — | — | — | — | — | 兴趣了解模式，未登记任何研究资产 |

## 本次调用中的特殊覆盖项

| 覆盖项 | 来源 | 对 field pack 的影响 | Last updated |
|---|---|---|---|
| 目标领域为现象学，且要求入门、含阅读路径 | user input | 采用 orientation + humanities_cultural，生成阅读路径与案例模块 | 2026-08-21 |
| 不找课题、不结合个人背景 | user input | 不生成 gap/project/MVP，不做资产匹配 | 2026-08-21 |

## Claims to Verify / 待核验判断

| 判断 | 为什么重要 | 需要来源 | 状态 |
|---|---|---|---|
| 中文译本的具体出版信息（出版社、年份、译者） | 阅读路径中引用译本需可追溯 | 各出版社目录 / 图书馆著录 | NEEDS_VERIFICATION |
| 当代学者（Zahavi、Gallagher、Thompson 等）具体著作年份与版本 | actor map 与 registry 需准确 | 官方出版信息 | NEEDS_VERIFICATION |
