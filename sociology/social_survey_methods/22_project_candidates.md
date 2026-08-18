<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-17 20:16:47
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-17 20:16:51
 * @FilePath     : /.agents/home/wyl/project/knowledge/sociology/social_survey_methods/22_project_candidates.md
 * @Description  :
-->
<!--
Field: 社会调研方法论——从日常对话到结构化判断
Mode: quick_scan
Domain archetype: social_science
Created date: 2026-08-17
-->

# 22 Project Candidates / 候选研究项目

Last updated: 2026-08-17

## 0. 说明

本文件把 `20_gap_table.md` 中的缺口压成候选项目。所有项目均为**方法落地型**项目，不承诺学术创新或可发表性。

**关于 `unresolved` 概念的降级确认**：`11_term_disambiguation.md` 中"信号强度加权"的 `concept_status` 为 `unresolved`。本文件所有依赖该概念的项目均已相应降级——P1、P2 标为 `provisional`（不以该概念为必要输入），P3、P4 标为 `unspecified`（不得进入 MVP）。不依赖该概念的项目不存在。

`operational_status` 说明：

- `unspecified`：任务尚未定义清楚，不得进入 MVP；
- `provisional`：任务定义初步成立但依赖未核验的概念（如信号强度加权），只能做消歧型验证。

## 1. 项目速览

| ID | 项目 | 对应 gap | 优先级 | operational_status |
|---|---|---|---|---|
| P1 | 分层调研问题库 v0.1 | G-01 | 高 | provisional |
| P2 | 三值编码手册与信度自检 | G-02 | 中 | provisional |
| P3 | 矛盾信息仲裁流程 | G-03 | 中 | unspecified |
| P4 | 微型半定量指数试验 | G-04 | 低 | unspecified |

---

## 2. 项目详情

### P1：分层调研问题库 v0.1

**给用户看的项目解释**：把"聊什么"落成一张按人群分层的清单——老人聊什么、小商户聊什么、上班族聊什么，每个敏感问题都翻译成日常话题。这是整条流水线第一环，一周内能启动。

- **problem**：没有结构化问题库，聊天维度覆盖随机（G-01）。
- **existing work**：半结构访谈提纲设计；种子文档 §4.4 维度清单（经济 6 项 + 治理 6 项）与 §4.6 敏感话题转译惯例。
- **gap**：面向具体人群与场景的日常化问题清单不存在。
- **core idea**：以"维度 × 人群"矩阵生成问题卡片，每个问题附带「敏感度标记 / 转译策略 / 期望信息类型」。
- **为什么不只是重复造轮子 (why not wheel-reinventing)**：设计原则用现成的，只做本地化转译；目标是工具化而非方法创新。
- **minimal experiment**：为 3 个人群（小商户、上班族、老人）各写 8-10 个问题 → 在 2-3 次真实聊天中试用 → 回收覆盖与回避数据。
- **input**：维度清单（种子文档 §4.4）、人群定义（年龄/职业）。
- **output**：问题卡片库 + 试用记录。
- **expected figures**：问题-维度覆盖矩阵热图；每个问题的回避率条形图。
- **Baselines / 基线：** 无问题库的自由聊天（记录维度覆盖作为对照）。
- **Metrics / 指标：** 单次聊天的维度覆盖率、回避率、冷场率。
- **Risks / 风险：** 案头设计脱离实际语言习惯；敏感问题转译过度或不足。
- **Success criteria / 成功标准：** 单次聊天覆盖 ≥ 5 个预设维度，且回避率低于 30%。
- **Stop criteria / 止损标准：** 试用 3 次后覆盖率无改善，或某人群所有敏感转译均触发回避 → 停止该人群的问题库设计，改为观察法补充。
- **paper contribution**：无（个人工具）。
- **priority**：高。
- **operational_status**：provisional（依赖"维度清单足够完备"这一未验证假设）。

### P2：三值编码手册与信度自检

**给用户看的项目解释**：给"事实/评价/传闻"写判定规则，并用两次独立编码的一致性检验规则是否可执行。是保证后续所有判断质量的质检环节。

- **problem**：三值编码判定边界模糊，编码信度无保障（G-02）。
- **existing work**：内容分析编码传统、Krippendorff 信度工具（见 `14_paper_registry.md` P-14）。
- **gap**：面向口语闲聊文本的判定规则手册缺失。
- **core idea**：10 条规则 + 20 条真实例句试标定，两轮迭代后固定 v1.0 手册。
- **为什么不只是重复造轮子 (why not wheel-reinventing)**：编码哲学与信度计算全部用现成工具，只写本地化判定规则。
- **minimal experiment**：同一批 20 条对话记录，间隔一周编码两次，计算自编码一致率。
- **input**：真实聊天记录 ≥ 20 条；判定规则草稿。
- **output**：编码手册 v1.0 + 一致性报告。
- **expected figures**：规则修订前后的一致性对比条形图；争议例句清单。
- **Baselines / 基线：** 凭直觉无规则编码的一致性（预计较低，NEEDS_VERIFICATION）。
- **Metrics / 指标：** 自编码一致率；有条件时双人 Krippendorff's alpha。
- **Risks / 风险：** 规则过细不可执行；自编码一致性高估真实信度（同一个人两次编码的偏差相关）。
- **Success criteria / 成功标准：** 一致率 ≥ 85% 且每条规则的争议例句数下降。
- **Stop criteria / 止损标准：** 两轮修订后一致率 < 80% → 放弃即时三值编码，改用“原话摘录 + 事后归类”。
- **paper contribution**：无。
- **priority**：中。
- **operational_status**：provisional（自编码不能完全替代互编码，信度结论受限）。

### P3：矛盾信息仲裁流程

**给用户看的项目解释**：遇到说法打架时按固定流程处理：分类冲突 → 追溯信源 → 找物证 → 记录处置结果。先把流程跑通再谈优化。

- **problem**：冲突信息仲裁无流程，判断退化为"听谁的多"（G-03）。
- **existing work**：三角验证原则、新闻溯源惯例。
- **gap**：面向个人调研的可执行仲裁流程缺失。
- **core idea**：冲突分类学（立场冲突/信息差异/传闻重复）+ 处置顺序 + 处置日志模板。
- **为什么不只是重复造轮子 (why not wheel-reinventing)**：原则全部现成，只做流程化。
- **minimal experiment**：5 组真实冲突案例按流程处置，检验处置是否改变/澄清判断。
- **input**：冲突案例 ≥ 5 组。
- **output**：仲裁流程 v0.1 + 案例处置日志。
- **expected figures**：处置前后判断变化表；重复信号识别案例。
- **Baselines / 基线：** 按信源数量表决。
- **Metrics / 指标：** 处置后判断与可验证事实的一致率。
- **Risks / 风险：** 流程形式化，实际仍是主观选择。
- **Success criteria / 成功标准：** ≥ 3 个案例的处置改变了或显著澄清了判断。
- **Stop criteria / 止损标准：** 3 个案例无任何澄清效果 → 放弃流程，改为结论中并列呈现冲突并标注证据强度。
- **paper contribution**：无。
- **priority**：中。
- **operational_status**：unspecified（"冲突类型学"尚未定义，任务可操作化不完整；需先完成 G-03 的案例收集）。

### P4：微型半定量指数试验

**给用户看的项目解释**：选 1-2 个可验证的小指标（如"夜间经济活跃度"），用手工打分 + 客观数据粗相关，验证"聊天 → 数字"这条映射是否走得通。

- **problem**：聊天数据半定量化无标准映射（G-04）。
- **existing work**：指数构建传统；质性主题频率统计。
- **gap**：从闲聊文本到指数的输入映射缺失。
- **core idea**：手工打分 → 与客观指标做秩相关 → 决定是否扩大。
- **为什么不只是重复造轮子 (why not wheel-reinventing)**：只用最简单的加权求和形态，不做方法论声称。
- **minimal experiment**：2 个微型指数 × 10 条记录手工打分 × 1 个客观指标相关检验。
- **input**：聊天记录 + 1 个可验证客观指标（如一条街的开门店铺数）。
- **output**：微型指数定义 + 相关检验报告。
- **expected figures**：指数 vs 客观指标散点图（Spearman ρ）。
- **Baselines / 基线：** 纯定性描述。
- **Metrics / 指标：** Spearman ρ 及其置信区间；须同时报告 unconditional（全部记录）与 conditional（经规则筛选的记录）两类表现，防止后选择抬高相关。
- **Risks / 风险：** 伪精确；后选择（只报显著者）。
- **Success criteria / 成功标准：** ρ 显著且方向可解释。
- **Stop criteria / 止损标准：** 无显著相关且无法解释 → 降级为“定性为主”，停止扩指数。
- **paper contribution**：无。
- **priority**：低。
- **operational_status**：unspecified（映射与权重未定义；需 P1/P2 产出的数据支撑后才能操作化）。

---

## 3. 执行建议

- **第一步可执行动作**：P1 —— 为小商户、上班族、老人三个人群各写 8-10 个问题卡片，本周内完成 v0.1。
- **最新进展（2026-08-18）**：P1 首个落地案例已就位——Case-01 退休县领导口述聊天池，见 `23_case01_chat_pool.md`（30 卡 × 5 模块）。该案例对象为可反复访谈的亲属（n=1 深度个案），作为问题库 v0.1 的首个试用场，其余三个人群的问题卡待该案例跑通后复用转译原则。
- 唯一建议现在启动的是 **P1**（依赖最少，一周内可出 v0.1）。
- P2 依赖 P1 使用过程中积累的聊天记录，建议 P1 试用 2 次后启动。
- P3、P4 的 operational_status 为 `unspecified`，**不进入 MVP**；待 P1/P2 产出数据后回填本文件并重新评估。
- 所有项目均为个人工具型，不承诺可发表贡献。
