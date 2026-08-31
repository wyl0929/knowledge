<!--
Field: 物理学入门
Mode: orientation
Domain archetype: science_technical
Created date: 2026-08-30
-->

# 10 Self Inventory / 用户背景快照

Last updated: 2026-08-30

## 使用说明

本文件是当前 field pack 使用的 profile 快照。它记录"这次生成时默认假设用户是谁、有没有研究资产、是否需要资产匹配"。它不同于 `USER_BRIEF.md`：profile 是长期背景或默认画像，brief 是本次任务的写作与调研要求。

不建议在旧 field pack 中自动同步最新 profile；旧包应保留当时快照，避免历史判断不可追溯。若需要更新旧包背景，请在 `99_update_log.md` 记录。

Field / 领域：物理学入门

Depth mode / 深度模式：orientation

## Profile source / 背景来源

/home/wyl/.agents/skills/research-onboarding/profiles/general_interest_profile.md

## Snapshot date / 快照日期

2026-08-30

## Profile snapshot / Profile 快照

```markdown
# General Interest Profile / 一般兴趣了解画像

Last updated: 2026-05-29

这是一个不包含任何个人背景假设的内置 profile。它不是研究型用户画像，也不假设用户拥有任何代码、平台、实验资源、合作者或特定研究方向。

## 适用场景

- 用户只是对某个领域感兴趣；
- 用户只是好奇某个概念是什么意思；
- 用户想先获得可读入门介绍；
- 用户明确表示暂时不考虑做研究、找课题或结合自身资产。

## 使用原则

- 不假设用户拥有任何代码、平台、实验资源或研究背景；
- 不自动生成个人资产匹配；
- 不自动把方向推成项目候选；
- 不强行输出 gap table、project candidates 或 MVP；
- 优先生成易读的 beginner guide、基础 overview、关键概念说明、field map 和 seed paper list；
- 如果用户后续表示想深入研究或寻找切入点，再切换到研究型 profile。

## 输出偏好

- 主体中文；
- 重要术语先解释，再在括号中标注英文术语；
- 适当给出公式、流程或例子；
- 可靠性边界集中说明；
- 不需要强行输出 gap table、project candidates 或 MVP。

## 不确定内容处理偏好

无法核验的论文、年份、工具状态、指标和判断标注 `NEEDS_VERIFICATION`。
```

## General interest mode / 兴趣了解模式说明

本包使用 `general_interest_profile.md`，当前不使用研究资产匹配，也不假设用户拥有代码、硬件、合作者或实验资源。此时：

- `20_gap_table.md`、`21_asset_match.md`、`22_project_candidates.md`、`23_mvp_experiment_plan.md` 不应默认生成；
- 阅读路径整合进 `00_beginner_guide.md` 与 `01_research_overview.md` 的对应小节；
- 若用户后续希望转为研究型进入，再切换到研究型 profile 并补充资产。

## 用户研究背景

- 身份与学科背景：不假设（兴趣了解模式，不结合个人背景）
- 主要研究方向：不适用
- 已有领域知识：不假设
- 数学、理论、实验或写作基础：不假设

## 用户已有工具或材料

| 工具 / 材料 | 类型 | 位置 | 成熟度 | 相关性 | 备注 |
|---|---|---|---|---|---|
| （空表） | — | — | — | — | 兴趣了解模式不登记资产；如需转研究型进入，再按研究型 profile 补充 |

## 本次调用中的特殊覆盖项

这里记录用户在本次调用中明确给出的、与 profile 不一致或比 profile 更新的信息。写作偏好、内容重点和回避事项应优先写入 `USER_BRIEF.md`。

| 覆盖项 | 来源 | 对 field pack 的影响 | Last updated |
|---|---|---|---|
| 无。用户只要求"写一个物理学入门的包"，未提供个人背景，与 general_interest_profile 一致 | user input | 按 orientation 默认规则执行 | 2026-08-30 |

## Claims to Verify / 待核验判断

| 判断 | 为什么重要 | 需要来源 | 状态 |
|---|---|---|---|
| 各经典文献（如 BCS 1957、Einstein 1905）的卷期页码 | 避免编造文献细节 | 出版方目录 / 引文数据库 | NEEDS_VERIFICATION |
| 前沿开放问题（暗能量、高温超导机制等）的当前表述 | 前沿状态随时间变化 | 近期权威综述 | NEEDS_VERIFICATION |
| 推荐教材的版本与出版年份 | 阅读路径需要可执行 | 出版社页面 | NEEDS_VERIFICATION |
