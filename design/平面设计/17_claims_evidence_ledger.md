<!--
Field: 平面设计
Mode: quick_scan
Domain archetype: mixed
Created date: 2026-08-30
-->

# 17 Claims Evidence Ledger / 中心论断与证据账本

Last updated: 2026-08-30

## 使用说明

本文件是生成 gap table 和 project candidates 前的 Core Claims Gate，并记录进入项目执行前的 Operationalization Gate 结论。下游判断必须引用或继承这里的中心论断与允许结论层级。

本包为兴趣/实践型进入，中心论断聚焦"设计基础原则"与"壁纸设计约束"，不生产学术 novelty 强声称。

## Gate verdict / 门控结论

概念边界状态：`working_definition`（核心概念——四原则、色彩三属性、网格、层级、对比度——已给出可操作定义，见 `11_term_disambiguation.md`）。

中心论断状态：`source_checked`（对设计领域广泛共识的来源，如四原则、WCAG 对比度、瑞士网格；具体年份/版本仍标 NEEDS_VERIFICATION）。

任务可操作化状态：`provisional`（壁纸项目可给出可测维度——对比度/对齐/焦点——但"审美达标"无法量化，故不能达到 `metric_checked`）。

允许进入的下游层级：
- introductory_explanation
- provisional_gap
- project_candidate
- mvp_design（仅限可测维度：对比度、对齐、层级；不含"好看"）

不允许：strong_claim_not_allowed（不做"这壁纸必然好看""程序=设计"等强声称）

Need verification: 具体年份/版本/公式系数。NEEDS_VERIFICATION

## Core Claim / 中心论断

### C-001：平面设计的核心是"约束下组织视觉元素"，不是装饰

- 论断类型：concept_definition
- 依赖哪些概念边界：设计 vs 艺术、设计 vs 工具（见 `11_term_disambiguation.md` 对比组 1）
- 支持哪些下游文件或项目：field map 边界、frontier compass 内圈、所有壁纸方案的设计前提
- 证据：设计领域广泛共识；现代主义"形式服从功能"、瑞士风格"客观传达"均指向同一结论
- 反证或替代解释：装饰派/表现派会强调情绪与形式的价值，但它们仍默认"有传达目标"
- 证据状态：source_checked
- 允许用于什么层级的结论：introductory_explanation, project_candidate
- 若该论断失效，需要撤回或修改什么：若"设计无传达目标"成立，则本包"以任务和受众为起点"的所有方案都要重写
- Need verification：无（属领域共识）

### C-002：对比/重复/对齐/亲密性（CRAP）是可教学、可迁移的基础原则

- 论断类型：mechanism
- 依赖哪些概念边界：四原则定义、对比 vs 冲突
- 支持哪些下游文件或项目：beginner guide 第 4-5 节、field map 核心假设、壁纸方案的自检清单
- 证据：Robin Williams《The Non-Designer's Design Book》(1994) 的提炼；设计教学通行
- 反证或替代解释：四原则是"事后解释工具"，未必是"生成算法"——它解释为什么清楚，但不自动生成清楚
- 证据状态：source_checked
- 允许用于什么层级的结论：introductory_explanation, project_candidate
- 若该论断失效，需要撤回或修改什么：若四原则不可迁移，壁纸自检清单将失去依据
- Need verification：无（领域共识；初版年份 NEEDS_VERIFICATION）

### C-003：色彩可由 HSL 三属性描述，且色相环关系提供配色起点

- 论断类型：concept_definition
- 依赖哪些概念边界：HSL vs RGB vs CMYK、色相/饱和度/明度
- 支持哪些下游文件或项目：field map 色彩子方向、壁纸配色方案（P-002/P-004）
- 证据：色彩理论通行；HSL/HSB 是主流取色工具的基础
- 反证或替代解释：HSL 数值不等于"看起来和谐"，和谐受面积、明度对比、文化语境影响
- 证据状态：source_checked
- 允许用于什么层级的结论：introductory_explanation, project_candidate
- 若该论断失效，需要撤回或修改什么：若 HSL 不能覆盖配色决策，程序化配色需换模型
- Need verification：HSL/HSB/HSV 口径差异。NEEDS_VERIFICATION

### C-004：网格通过约束把版式变成可重复、可学习的过程

- 论断类型：mechanism
- 依赖哪些概念边界：网格 vs 参考线 vs 对齐
- 支持哪些下游文件或项目：field map 网格子方向、壁纸方案"秩序之网格"(P-001)、程序化生成器(P-004)
- 证据：Müller-Brockmann《Grid Systems》(1981)、瑞士国际主义风格
- 反证或替代解释：网格提升清晰度与可复现，但会压抑情绪；破格需要判断力
- 证据状态：source_checked
- 允许用于什么层级的结论：introductory_explanation, project_candidate
- 若该论断失效，需要撤回或修改什么：若网格不提升可复现性，则"代码复刻网格"失去价值
- Need verification：无（领域共识；出版社年份 NEEDS_VERIFICATION）

### C-005：桌面壁纸的核心约束是"图标可读性 + 负空间 + 多分辨率"，不同于海报

- 论断类型：phenomenon / platform_bridge
- 依赖哪些概念边界：壁纸 vs 海报、对比度、负空间、多分辨率
- 支持哪些下游文件或项目：gap table G-003、壁纸方案（P-003 图标安全区）、frontier compass B-003
- 证据：通行做法（图标安全区留白、内容居中、边缘可裁）；对比度有 WCAG 可测底线
- 反证或替代解释：极简壁纸可弱化"焦点"需求；"图标安全区"无统一量化规范
- 证据状态：working_definition（约束存在，但量化规范 weak）
- 允许用于什么层级的结论：provisional_gap, project_candidate
- 若该论断失效，需要撤回或修改什么：若壁纸无需考虑图标可读性（如纯展示屏），相关约束可放宽
- Need verification：桌面图标停靠侧与安全区官方约定。NEEDS_VERIFICATION

### C-006：用户可用 Python/PIL 做程序化壁纸，把网格与配色变成可执行参数

- 论断类型：feasibility / recommendation
- 依赖哪些概念边界：网格可代码化、HSL 可数值化
- 支持哪些下游文件或项目：project candidates P-004、frontier compass 用户切口
- 证据：用户资产（Python/matplotlib/LaTeX，见 `10_self_inventory.md`）；Pillow/cairo 可绘图（API 待核验）
- 反证或替代解释：代码能生成图形，但"随机 ≠ 设计决策"；审美仍需人工判断
- 证据状态：working_definition（可行性高，但依赖库可用性与审美积累）
- 允许用于什么层级的结论：project_candidate, mvp_design（仅可测维度）
- 若该论断失效，需要撤回或修改什么：若用户未装绘图库或不接受代码路线，则退回手工方案
- Need verification：Pillow/cairo 是否已装、API 细节。NEEDS_VERIFICATION

### C-007："好看"难以量化，但"清晰/对比度/层级"可部分客观度量

- 论断类型：mechanism
- 依赖哪些概念边界：对比度 vs 和谐
- 支持哪些下游文件或项目：gap table G-001、frontier compass B-001、壁纸方案的"达标"标准
- 证据：WCAG 对比度是可测公式；对齐/层级可检验；美感无公认量化指标
- 反证或替代解释：可用眼动、偏好实验近似测"美感"，但非公式化、非稳定
- 证据状态：source_checked（可测部分）；suspected（美感量化）
- 允许用于什么层级的结论：provisional_gap, project_candidate
- 若该论断失效，需要撤回或修改什么：若"美感可完全量化"成立，则壁纸可全自动达标
- Need verification：WCAG 公式精确系数与版本。NEEDS_VERIFICATION

---

## Operationalization Gate / 任务可操作化门

### 任务可操作化结论

本包优先项目（P-004 程序化壁纸生成器）可以进入 `mvp_design`，但只针对**可测维度**（对比度达标、元素对齐、存在焦点、生成不撞车）。"好看/有情绪"不作为可操作化指标，只作为人工评审的软反馈。

### 支撑下游项目的任务定义（以 P-004 为例）

- 声称要验证的任务：给定"主色/情绪/风格"参数，脚本能稳定输出一套对比度达标、有焦点、构图有据的 1920×1080 壁纸。
- 输入对象与允许输入集合：主色相 H（0-360）、明度基调（暗/亮）、风格（几何/渐变）、配色关系（单色/类比/互补）。
- 目标变换：把参数映射为"背景色 + 焦点图形位置/大小/颜色 + 图标安全区留白"的确定性布局。
- 解码或读出要求：输出 PNG（sRGB）；可自动计算图标区对比度 CR 并拒绝 CR < 3 的组合。
- 失败 / 泄漏 / 后选择处理：不得"生成 100 张挑 1 张"来冒充达标（后选择须明示）；每张必须通过同样的硬约束过滤。
- baseline 公平性要求：对比"随手随机参数生成"与"约束式生成"，在相同数量下比较达标率与不撞车率。
- 阳性结果能证明什么：约束式生成能稳定产出合规壁纸（可测维度）。
- 阳性结果不能证明什么：不能证明壁纸"好看"或"有设计价值"。
- 阴性结果意味着什么：若达标率低，说明参数空间/约束设计有问题，需收紧规则或缩小风格范围。
- operational_status: provisional（可测维度可操作化，审美维度不可操作化）

---

## Ledger Table / 汇总表

| Claim ID | 论断类型 | 论断内容 | 证据状态 | 允许结论层级 | 支持下游文件 | operational_status | Need verification |
|---|---|---|---|---|---|---|---|
| C-001 | concept_definition | 设计是约束下组织元素，非装饰 | source_checked | introductory/project | 12/02/全部方案 | — | 无 |
| C-002 | mechanism | CRAP 四原则可教学可迁移 | source_checked | introductory/project | 00/12/自检清单 | — | 无 |
| C-003 | concept_definition | HSL 三属性 + 色相环提供配色起点 | source_checked | introductory/project | 12/P-002/P-004 | — | HSL/HSB 口径 |
| C-004 | mechanism | 网格使版式可重复可学习 | source_checked | introductory/project | 12/P-001/P-004 | — | 无 |
| C-005 | phenomenon | 壁纸核心约束=图标可读+负空间+多分辨率 | working_definition | provisional_gap/project | 20/G-003/P-003 | — | 图标安全区约定 |
| C-006 | feasibility | 用户可用 Python 做程序化壁纸 | working_definition | project/mvp(可测) | P-004/02 | provisional | Pillow API |
| C-007 | mechanism | 好看难量化，但清晰/对比可测 | source_checked | provisional_gap/project | G-001/B-001 | — | WCAG 系数 |
