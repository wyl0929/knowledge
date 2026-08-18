<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-17 20:58:18
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-17 20:58:18
 * @FilePath     : /.agents/home/wyl/project/knowledge/sociology/fundamentals/USER_BRIEF.md
 * @Description  :
-->
<!--
Field: 社会学入门——基本概念与基础理论
Mode: quick_scan
Domain archetype: social_science
Created date: 2026-08-17
-->

# USER BRIEF / 本次需求说明

Last updated: 2026-08-17

## 这份文件的作用

这里保存用户对本 field pack 的特殊要求。内容可以直接用自然语言书写。
生成或更新本包中的任何主体文档前，agent 都必须先读取本文件。

本文件与其他文件的区别：

- `10_self_inventory.md`：记录本次使用的 profile 或用户背景快照；
- `USER_BRIEF.md`：记录本次调研的目标、重点、写作方式和回避事项；
- `90_QA.md`：保存后续自由讨论，默认不自动成为持续要求；
- `99_update_log.md`：保存修改历史。

## 路由决策

```yaml
detected_mode: quick_scan
selected_profile: general_interest（一般兴趣了解）
domain_archetype: social_science
confidence: high
```

## 用户原始需求

> 创建一个 field，介绍社会学入门和基础理论。

## 当前有效要求

- 在 `sociology/` 下新建入门 field pack，与同目录的 `social_survey_methods/` 平行，与 `political_science/fundamentals/` 结构同构。
- 按 quick_scan + general_interest_profile 默认规则执行：不假设用户有研究背景，不强行生成个人资产匹配，不把方向推成个人研究项目。
- `20_gap_table.md` 与 `22_project_candidates.md` 仅作为"学科开放问题与可选延伸方向"的轻量登记（满足 quick_scan 结构要求），不构成对用户的研究建议。

## 内容侧重点

- 希望重点展开：社会学的基本概念体系（社会、社会结构、文化、社会化、互动、制度、分层）、三大古典奠基（涂尔干、韦伯、马克思）与主要理论传统（功能主义、冲突论、符号互动论、常人方法学、交换论、现象学社会学、批判理论、结构化与实践理论、理性选择）、方法论概览（定量/定性/比较/历史）。
- 希望简略处理：过于细节的国别社会史、当代前沿争论的技术细节。
- 暂时不需要涉及：以社会调研方法论为主题的内容（已有独立 pack `social_survey_methods/`，本包只做交叉引用）。

## 写作与呈现偏好

- 语言与风格：主体中文，关键术语初次出现附英文；先讲直觉，再讲术语；把分类写成谱系、坐标轴与 trade-off，而非百科清单。
- 期望深度：适合有学术训练但无社会学专业背景的读者，能建立基本地图与边界感。
- 是否需要公式 / 流程 / 作品例子 / 图表：适当使用流程图与比较表格；给出经典学者/著作作为锚点。
- 是否需要阅读清单：是，在 `14_paper_registry.md` 与 `00_beginner_guide.md` 中给出入门阅读路径。
- 是否需要派生子方向：暂不需要，但保留后续派生可能（如具体理论流派的深入包）。

## 与父方向的继承关系

本包为 `sociology/` 一级目录下的独立 field pack，不继承自任何父包。与 `sociology/social_survey_methods/`、`political_science/` 各包为平行关系。

## 修改记录

| 日期 | 修改内容 | 来源 |
|---|---|---|
| 2026-08-17 | 初始化本次需求说明 | initial user prompt |
