<!--
Field: phenomenology
Mode: orientation
Domain archetype: humanities_cultural
Created date: 2026-08-21
-->

# USER BRIEF / 本次需求说明

Last updated: 2026-08-21

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
initial_mode: orientation
current_mode: orientation
selected_profile: general_interest_profile
domain_archetype: humanities_cultural
confidence: high
```

## 用户原始需求

> 在 philosophy/ 下创建一个现象学（phenomenology）的入门 field pack。

## 当前有效要求

- 定位：一般兴趣入门，读懂现象学是什么、为什么出现、有哪些主要路线与代表著作。
- 不结合个人研究背景，不找研究课题，不生成 gap table / asset match / project candidates / MVP。
- 需要代表作品、案例与可执行的阅读路径。
- 中文为主，关键术语第一次出现时先中文解释、再括号标注原文。

## 需求解析

| 维度 | 内容 |
|------|------|
| 目标领域 | 现象学（phenomenology） |
| 定位 | 一般兴趣入门，读懂现象学是什么、为什么出现、有哪些主要路线与代表著作 |
| 是否结合个人背景 | 否（general_interest_profile，不假设任何研究资产） |
| 是否找课题 / 项目 | 否（不生成 gap table、asset match、project candidates、MVP） |
| 是否需要作品 / 案例 / 阅读路径 | 是（哲学人文方向，用第一手著作与阅读路径承载理解） |
| 语言偏好 | 中文为主，关键术语第一次出现先中文解释、再括号标注英文/德文/法文原文 |
| 回避事项 | 不强行推向研究选题；不对活着的争议做确定性裁决 |

## 内容侧重点

- 希望重点展开：现象学的核心主张（意向性、悬搁、还原、回到事情本身）、Husserl 奠基与后继谱系（Heidegger / Merleau-Ponty / Sartre / Levinas 等）、可执行的阅读路径。
- 希望简略处理：纯考据式的文本细枝、学派内部琐碎论战。
- 暂时不需要涉及：gap 分析、项目候选、MVP 实验计划、与用户代码/工具的结合。

## 写作与呈现偏好

- 语言与风格：先讲直觉再讲术语；连续中文叙述，表格只作索引。
- 期望深度：入门可读、概念边界清楚；不要求论文级论证重建。
- 是否需要公式 / 流程 / 作品例子 / 图表：用文字流程图和具体案例（如萨特的咖啡馆、胡塞尔的立方体知觉、海德格尔的锤子）承载理解。
- 是否需要阅读清单：是。
- 是否需要派生子方向：暂不需要。

## 与父方向的继承关系

本文件不是子方向包，无父方向继承关系（N/A）。

## 修改记录

| 日期 | 修改内容 | 来源 |
|---|---|---|
| 2026-08-21 | 初始化本次需求说明并明确路由决策 | initial user prompt / init script |
