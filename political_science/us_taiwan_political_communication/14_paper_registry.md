<!--
Field: us_taiwan_political_communication
Mode: full_onboarding
Domain archetype: social_science
Created date: 2026-08-30
-->

# 14 Source Registry / 来源与阅读入口注册表

Last updated: 2026-08-30

## 使用说明

本文件记录 seed sources 和关键阅读入口。对理工方向，它通常以论文为主；对文学、人文和兴趣了解包，它也可以包含第一手作品、期刊、研究共同体、理论入口、近期趋势信号和可靠阅读路径。

不要为了填表编造作者、年份、DOI、作品或结论；未核验信息标 `NEEDS_VERIFICATION`。生成或更新前必须先读取 `USER_BRIEF.md`。

**本包证据纪律（LITERATURE_QC_PROTOCOL）**：条目元数据（作者/年份/标题/期刊/DOI）分为 `📜Q`（OpenAlex/arXiv API 直接核验，2026-08-30 检索）与 `⚠️待核验`（仅搜索摘要可见，引用前必须补核）。全文论点级证据（数值、结论）目前均为"未精读"状态——在完成精读（paper_review_*.md）前，正文引用这些论文时只能使用条目级信息，并标注 NEEDS_VERIFICATION。

Field / 领域：us_taiwan_political_communication

## 来源类型

- `primary work`：第一手作品、文本、档案、案例或实验对象；
- `foundational theory`：基础理论或经典概念来源；
- `recent study`：近期研究；
- `review`：综述或导读；
- `journal / venue`：期刊、会议、出版社或栏目；
- `institution / community`：研究中心、学会、共同体；
- `tool / dataset`：工具、数据集、语料库；
- `trend signal`：近期趋势线索，需要后续核验。

## 证据角色

概念定义；领域入口；代表论证；近期趋势；第一手阅读对象；方法资源。

## Source Entry / 来源条目（★ 核心入口）

**Source ID / 来源编号：** T1-ENTMAN93

**来源类型：** foundational theory
**证据角色：** 概念定义

**Title / 题名：** Framing: Toward Clarification of a Fractured Paradigm
**Authors / 作者或机构：** Robert M. Entman
**Year / 年份：** 1993
**Venue / Source / 来源：** Journal of Communication, 43(4)
**URL / DOI：** 10.1111/j.1460-2466.1993.tb01304.x

**Status:** skimmed（条目级核验 📜Q；全文论点待精读）

**人话摘要：** 框架研究的"宪法"：框架是文本中选择并凸显某些要素的呈现方式，包含问题定义、因果归因、道德评价、对策建议四个功能位置。本包所有"框架"的操作化都从这四位置出发。

**核心贡献或用途：** 用户研究问题一（框架建构）的理论锚点与编码手册骨架。

**关键假设或边界：** 四功能定义面向文本呈现，不含受众效果；框架≠偏见。

**与本 field pack 的关系：** 11_term_disambiguation 概念契约的直接依据；22/23 编码方案的顶层设计。

**Need verification / 待核验：** 四功能条款的精确页码引用（精读时补）。

**Last updated / 最后更新：** 2026-08-30

---

**Source ID / 来源编号：** T5-SCHEUFELE99
**来源类型：** foundational theory
**证据角色：** 概念定义
**Title / 题名：** Framing as a Theory of Media Effects
**Authors / 作者或机构：** Dietram A. Scheufele
**Year / 年份：** 1999
**Venue / Source / 来源：** Journal of Communication, 49(1)
**URL / DOI：** 10.1111/j.1460-2466.1999.tb02784.x
**Status:** skimmed（📜Q）
**人话摘要：** 把 framing 拆成 frame building（框架建构：框架怎么被生产）与 frame setting（框架效果：框架怎么影响受众）。用户研究问题一属于前者。
**核心贡献或用途：** 界定用户"框架建构"研究问题的合法范围，挡住效果研究的要求。
**关键假设或边界：** 生产端与效果端是两个数据世界；本包只承诺生产端。
**与本 field pack 的关系：** 概念契约"框架建构≠框架效果"的直接来源。
**Need verification / 待核验：** 模型细节（精读）。
**Last updated / 最后更新：** 2026-08-30

---

**Source ID / 来源编号：** T1-MATTKOHR08
**来源类型：** recent study（方法经典）
**证据角色：** 方法资源
**Title / 题名：** The Content Analysis of Media Frames: Toward Improving Reliability and Validity
**Authors / 作者或机构：** Jörg Matthes & Matthias Kohring
**Year / 年份：** 2008
**Venue / Source / 来源：** Journal of Communication, 58(2)
**URL / DOI：** 10.1111/j.1460-2466.2008.00384.x
**Status:** skimmed（📜Q）
**人话摘要：** 框架编码不直接贴"框架标签"，而是分别编码问题定义/因果归因/道德评判/对策建议等元素，再由元素组合推导框架——显著提升信度。
**核心贡献或用途：** 用户 MVP 编码手册的操作化蓝本。
**关键假设或边界：** 元素组合法成本高于直接标签法；需要编码员训练。
**与本 field pack 的关系：** 16 指标的编码方案、23 MVP 的编码步骤。
**Need verification / 待核验：** 信度报告数值（精读）。
**Last updated / 最后更新：** 2026-08-30

---

**Source ID / 来源编号：** T4-WANGGUO18
**来源类型：** recent study
**证据角色：** 代表论证
**Title / 题名：** Framing GM mosquitoes in online news and Twitter: Intermedia frame setting
**Authors / 作者或机构：** Wang & Guo
**Year / 年份：** 2018
**Venue / Source / 来源：** Public Understanding of Science
**URL / DOI：** 10.1177/0963662518799564
**Status:** skimmed（📜Q；结论数值待精读）
**人话摘要：** 帧层面的媒介间框架设置研究：同一议题在新闻与 Twitter 上的框架如何互相设置。与用户研究问题三在方法结构上最对口。
**核心贡献或用途：** 帧层面跨平台流向的先行设计模板。
**关键假设或边界：** 议题为科技传播（GM 蚊子），迁移到高政治化议题需论证。
**与本 field pack 的关系：** 22 项目卡片 P1 的方法对标；20 gap 表 G2 的"已做部分"。
**Need verification / 待核验：** 原文流向结论与时滞数值（精读）。
**Last updated / 最后更新：** 2026-08-30

---

**Source ID / 来源编号：** T4-TAN26
**来源类型：** recent study（2026 最新）
**证据角色：** 近期趋势
**Title / 题名：** Intermedia Agenda Setting Between Social and Traditional Media: Taiwan vs U.S. Coverage
**Authors / 作者或机构：** Tan, Grabe & Weaver
**Year / 年份：** 2026
**Venue / Source / 来源：** Mass Communication & Society
**URL / DOI：** 10.1080/15205436.2026.2710692
**Status:** seed（📜Q；2026 年新文，正文未读）
**人话摘要：** 台湾与美国媒体跨媒介议程对比（非政治议题）——与用户"双平台/美台语境"设计最接近的近期先行者。
**核心贡献或用途：** 竞品式参照：确认其议题/方法后定位用户差异点（涉台政治事件 × 帧层面 × 三阶段）。
**关键假设或边界：** 议题为空气污染，政治化程度不同。
**与本 field pack 的关系：** 优先精读对象之一（建议生成 paper_review）。
**Need verification / 待核验：** 全文方法与结论（未读）。
**Last updated / 最后更新：** 2026-08-30

---

**Source ID / 来源编号：** T3-JACOBS23
**来源类型：** recent study（预印本）
**证据角色：** 第一手阅读对象
**Title / 题名：** Tracking China's cross-strait bot networks against Taiwan
**Authors / 作者或机构：** Jacobs, Ng & Carley（CMU CASOS）
**Year / 年份：** 2023
**Venue / Source / 来源：** arXiv:2310.10851（预印本）
**URL / DOI：** https://arxiv.org/abs/2310.10851
**Status:** skimmed（arXiv API 核验 📜Q；预印本引用需谨慎）
**人话摘要：** 追踪中国大陆对台"跨海峡机器人网络"，含佩洛西事件时段账号画像——涉台 X 语料中机器话语污染的直接证据。
**核心贡献或用途：** 用户 X 侧语料的"机器账号清洗"需求来源；其 Kilthub 数据集（元数据待核验）是潜在数据源。
**关键假设或边界：** 预印本未同行评审；账号分类方法有误报率。
**与本 field pack 的关系：** 23 MVP 数据清洗步骤的依据；20 gap 表 G5 的支撑。
**Need verification / 待核验：** 数据集下载与许可；分类精度。
**Last updated / 最后更新：** 2026-08-30

---

**Source ID / 来源编号：** T2-AMRULLAH23
**来源类型：** recent study
**证据角色：** 代表论证
**Title / 题名：** Interpreting U.S. Public Opinion on Cross-Strait Relations during Tsai's First Term: A Twitter Sentiment Analysis
**Authors / 作者或机构：** Maulana Amrullah
**Year / 年份：** 2023
**Venue / Source / 来源：** Journal of Global and Area Studies
**URL / DOI：** 10.31720/jga.7.4.3
**Status:** skimmed（📜Q；方法质量待评）
**人话摘要：** 与用户 X 样本最贴近的现成研究：用美国涉台 Twitter 文本测"公众舆论"。
**核心贡献或用途：** 正面对照（数据路径）+ 反面对照（它把平台文本直接叫"公众舆论"，正是本包概念契约要避免的越界）。
**关键假设或边界：** Twitter 情绪≠美国民意；覆盖期为蔡英文第一任期（2016–2020 部分）。
**与本 field pack 的关系：** 20 gap 表 G1 的"已做部分"证据；概念契约的教训案例。
**Need verification / 待核验：** 其样本时段与平台采集方式（精读）。
**Last updated / 最后更新：** 2026-08-30

---

**Source ID / 来源编号：** T4-SUBORAH19
**来源类型：** recent study
**证据角色：** 方法资源
**Title / 题名：** Who is the agenda setter? Examining intermedia agenda-setting between Twitter and newspapers
**Authors / 作者或机构：** Yan Su & Porismita Borah
**Year / 年份：** 2019
**Venue / Source / 来源：** Journal of Information Technology & Politics
**URL / DOI：** 10.1080/19331681.2019.1641451
**Status:** skimmed（📜Q）
**人话摘要：** 用时间序列检验 Twitter↔报纸议程方向性的标准模板。
**核心贡献或用途：** 用户研究问题三的计量操作化参照（Granger/交叉滞后）。
**关键假设或边界：** 议程显著性定义（词频/占比）是第一层，非帧层面。
**与本 field pack 的关系：** 16 指标"领先-跟随检验"的文献支撑。
**Need verification / 待核验：** 原文模型设定（精读）。
**Last updated / 最后更新：** 2026-08-30

---

**Source ID / 来源编号：** T5-WALTEROPHIR19
**来源类型：** recent study（方法）
**证据角色：** 方法资源
**Title / 题名：** News Frame Analysis: An Inductive Mixed-method Computational Approach
**Authors / 作者或机构：** Dror Walter & Yotam Ophir
**Year / 年份：** 2019
**Venue / Source / 来源：** Communication Methods and Measures
**URL / DOI：** 10.1080/19312458.2019.1639145
**Status:** skimmed（📜Q）
**人话摘要：** 归纳式混合计算框架分析：词嵌入聚类找候选框架，人工验证定框架——大规模语料做框架建构的方法学首选。
**核心贡献或用途：** 用户全时段新闻语料框架提取的计算路线。
**关键假设或边界：** 归纳框架的命名与理论对话需要额外论证。
**与本 field pack 的关系：** 12 field map 计算文本分析谱系的核心；23 MVP 的 B 路径。
**Need verification / 待核验：** 流程细节（精读）。
**Last updated / 最后更新：** 2026-08-30

---

**Source ID / 来源编号：** T2-GILARDI23
**来源类型：** recent study
**证据角色：** 方法资源
**Title / 题名：** ChatGPT outperforms crowd workers for text-annotation tasks
**Authors / 作者或机构：** Fabrizio Gilardi, Meysam Alizadeh, Maël Kubli
**Year / 年份：** 2023
**Venue / Source / 来源：** PNAS
**URL / DOI：** 10.1073/pnas.2305016120
**Status:** skimmed（📜Q）
**人话摘要：** LLM 在多项文本标注任务上优于众包工人的系统证据——支持"LLM 批量编码 + 人工子样本验证"的经济可行性。
**核心贡献或用途：** 23 MVP 编码管线的可行性依据。
**关键假设或边界：** 任务类型覆盖偏标注类；政治敏感议题的模型立场偏差未在该文处理。
**与本 field pack 的关系：** 16 指标"人机一致性"的 benchmark 依据。
**Need verification / 待核验：** 具体任务集与效应量（精读）。
**Last updated / 最后更新：** 2026-08-30

---

## Registry Table / 汇总表（按主题分组）

### A. 框架理论与方法（概念与操作化底座）

| Source ID | 来源类型 | 证据角色 | Title | Year | Status | 人话摘要 | 证据 | Need verification |
|---|---|---|---|---|---|---|---|---|
| T1-ENTMAN93 | foundational theory | 概念定义 | Framing: Toward Clarification of a Fractured Paradigm | 1993 | skimmed | 框架四功能定义 | 📜Q | 页码级引用 |
| T5-SCHEUFELE99 | foundational theory | 概念定义 | Framing as a Theory of Media Effects | 1999 | skimmed | frame building vs setting | 📜Q | 模型细节 |
| T1-MATTKOHR08 | recent study | 方法资源 | The Content Analysis of Media Frames | 2008 | skimmed | 元素组合编码法 | 📜Q | 信度数值 |
| T5-MCCOMBS72 | foundational theory | 概念定义 | The Agenda-Setting Function of Mass Media | 1972 | skimmed | 议程设置开山 | 📜Q | 无 |
| T5-GAMSON89 | foundational theory | 概念定义 | Media Discourse and Public Opinion on Nuclear Power | 1989 | skimmed | 媒体话语-舆论建构主义 | 📜Q | 无 |
| T5-IYENGAR91 | foundational theory | 概念定义 | Is Anyone Responsible? | 1991 | skimmed | 事件性/主题性框架 | 📜Q | 无 |
| T5-CHONGDRUCK07 | foundational theory | 概念定义 | A Theory of Framing and Opinion Formation | 2007 | skimmed | 竞争性框架环境 | 📜Q | 无 |
| T5-BORAH11 | review | 领域入口 | Conceptual Issues in Framing Theory | 2011 | skimmed | 十年框架研究审查 | 📜Q | 无 |
| T5-CACCIATORE15 | recent study | 领域入口 | The End of Framing as we Know it | 2015 | skimmed | 框架/议程/启动混淆批判 | 📜Q | 无 |
| T5-WALTEROPHIR19 | recent study | 方法资源 | News Frame Analysis: Inductive Mixed-method | 2019 | skimmed | 计算框架分析 | 📜Q | 流程细节 |
| T5-GILARDI23 | recent study | 方法资源 | ChatGPT outperforms crowd workers | 2023 | skimmed | LLM 标注质量 | 📜Q | 效应量 |
| T5-ZIEMS23 | recent study | 方法资源 | Can LLMs Transform Computational Social Science? | 2023 | skimmed | LLM 社科编码讨论 | 📜Q | 无 |
| T1-CARD15 | tool / dataset | 方法资源 | The Media Frames Corpus | 2015 | skimmed | 通用框架标注语料 | 📜Q | 语料规模 |
| T5-GRIMSTEW13 | review | 方法资源 | Text as Data: Promise and Pitfalls | 2013 | skimmed | dictionary/监督/无监督三分 | 📜Q | 无 |
| T5-ROBERTS14 | recent study | 方法资源 | Structural Topic Models (AJPS) | 2014 | skimmed | STM 协变量主题模型 | 📜Q | 无 |
| T5-HALLGREN12 | recent study | 方法资源 | Computing Inter-Rater Reliability (TQMP) | 2012 | skimmed | Krippendorff alpha 教程 | 📜Q | 无 |
| T5-RODER15 | recent study | 方法资源 | Exploring the Space of Topic Coherence Measures | 2015 | skimmed | C_V/NPMI 指标 | 📜Q | 无 |
| T5-DEVREESE05 | foundational theory | 概念定义 | News Framing: Theory and Typology | 2005 | seed | 框架类型学经典 | ⚠️待核验 | OpenAlex 未命中，补核后引用 |
| T5-WICHGERS20 | recent study | 代表论证 | The Battle of Frame Building | 2020 | seed | 框架赞助者博弈 | 📜Q | 无 |

### B. 媒介间议程设置 / 跨平台流动（研究问题三的谱系）

| Source ID | 来源类型 | 证据角色 | Title | Year | Status | 人话摘要 | 证据 | Need verification |
|---|---|---|---|---|---|---|---|---|
| T4-GOLAN06 | recent study | 代表论证 | Intermedia Agenda Setting and Global News Coverage | 2006 | seed | NYT→电视网经典 | ⚠️待核验 | OpenAlex 未命中，补核后引用 |
| T4-NEUMAN14 | recent study | 代表论证 | The Dynamics of Public Attention | 2014 | skimmed | 议程×大数据 | 📜Q | 无 |
| T4-CONWAY15 | recent study | 代表论证 | The Rise of Twitter in the Political Campaign | 2015 | skimmed | Twitter↔报纸方向性 | 📜Q | 无 |
| T4-HARDER17 | recent study | 代表论证 | Intermedia Agenda Setting in the Social Media Age | 2017 | skimmed | 传统媒体仍主导 | 📜Q | 无 |
| T4-GUOVARGO17 | recent study | 代表论证 | Global Intermedia Agenda Setting | 2017 | skimmed | 全球新闻流动 | 📜Q | 无 |
| T4-WANGGUO18 | recent study | 代表论证 | Framing GM mosquitoes: Intermedia frame setting | 2018 | skimmed | 帧层面跨平台（★） | 📜Q | 流向数值 |
| T4-SUBORAH19 | recent study | 方法资源 | Who is the agenda setter? | 2019 | skimmed | 方向性检验模板 | 📜Q | 模型设定 |
| T4-VALENZUELA17 | recent study | 代表论证 | Comparing Disaster News on Twitter and Television | 2017 | skimmed | 同事件跨平台模板 | 📜Q | 无 |
| T4-SUXIAO21 | review | 领域入口 | Mapping the intermedia agenda setting literature | 2021 | skimmed | IAS 文献地图 | 📜Q | 无 |
| T4-SUHULEE20 | recent study | 方法资源 | Transnational Network Agenda-Setting (ML) | 2020 | skimmed | 报纸↔Twitter 网络议程 | 📜Q | 无 |
| T4-OBOYLE21 | recent study | 代表论证 | How Twitter drives the global news agenda | 2021 | skimmed | 社交→新闻方向 | 📜Q | 无 |
| T4-WATANABE17 | recent study | 方法资源 | The spread of the Kremlin's narratives | 2017 | skimmed | 叙事经通讯社扩散 | 📜Q | 无 |
| T4-ABDULNABI24 | recent study | 代表论证 | Facebook users' responses to China-Taiwan coverage | 2024 | seed | 媒体→社交反应链 | 📜Q | 无 |
| T4-TYLER21 | recent study | 背景 | Partisan Enclaves and Information Bazaars | 2021 | skimmed | 美国在线新闻消费版图 | 📜Q | 无 |
| T4-TAN26 | recent study | 近期趋势 | IAS: Taiwan vs U.S. Coverage | 2026 | seed | 与用户设计最接近先行者（★精读） | 📜Q | 全文未读 |

### C. 涉台/涉华实证线（领域内容）

| Source ID | 来源类型 | 证据角色 | Title | Year | Status | 人话摘要 | 证据 | Need verification |
|---|---|---|---|---|---|---|---|---|
| T1-OOI17 | recent study | 代表论证 | Framing China: Discourses of othering | 2017 | skimmed | 美媒他者化中国框架 | 📜Q | 无 |
| T1-YUANFU20 | recent study | 代表论证 | Narrative Framing and Threat Construction | 2020 | skimmed | 威胁建构机制 | 📜Q | 无 |
| T1-MCCOURT21 | recent study | 代表论证 | Framing China's rise (US/AUS/UK) | 2021 | skimmed | 三国比较框架 | 📜Q | 无 |
| T1-CHENWANG20 | recent study | 代表论证 | A war or merely friction? | 2020 | skimmed | NYT vs China Daily | 📜Q | 无 |
| T1-TU24 | recent study | 代表论证 | Aftermath of the Fourth Taiwan Strait Crisis | 2024 | seed | 危机后"中国威胁"话语 | 📜Q | 无 |
| T1-CHANG25 | recent study | 近期趋势 | Dynamic Public Perceptions of Military Threats to Taiwan | 2025 | seed | 媒体→威胁感知动态 | 📜Q | 无 |
| T1-HOOSWORN20 | recent study | 背景 | Strategic ambiguity and the Trumpian approach | 2020 | skimmed | 特朗普一期政策框架 | 📜Q | 无 |
| T1-LIU23 | recent study | 背景 | From "Strategic Ambiguity" Toward "Strategic Clarity" | 2023 | skimmed | 拜登期话语转向 | 📜Q | 无 |
| T2-WULIN22 | recent study | 代表论证 | Will the US come to Taiwan's defense? | 2022 | skimmed | 协防台湾民意 | 📜Q | 无 |
| T2-RICH23 | recent study | 代表论证 | Outlooks and affinities (defending Taiwan) | 2023 | skimmed | 协防支持动因 | 📜Q | 无 |
| T2-NACHMAN25 | recent study | 近期趋势 | Can Taiwan survive partisanship? | 2025 | seed | 党派性调查实验 | 📜Q | 无 |
| T2-PAN23 | recent study | 代表论证 | US public opinion on cross-strait relations | 2023 | seed | 中国威胁→两岸态度 | 📜Q | 无 |
| T2-YEHWU20 | recent study | 代表论证 | Is the enemy's enemy my friend? | 2020 | seed | 贸易战语境对台支持 | 📜Q | 无 |
| T2-WANGWUYEH23 | recent study | 代表论证 | High-level visit and national security policy | 2023 | seed | 佩洛西访台准实验 | 📜Q | 无 |
| T2-CHICAGO | institution / community | 背景 | Chicago Council 涉台民调报告 | ~2023 | seed | 民调数据源（灰色文献） | ⚠️待核验 | 作者/年份补核 |
| T3-AMRULLAH23 | recent study | 代表论证 | US Public Opinion on Cross-Strait via Twitter | 2023 | skimmed | 涉台 Twitter 情绪（★正反对照） | 📜Q | 采集方式 |
| T3-AMRULLAH24 | recent study | 近期趋势 | Shifts in U.S. Public Opinion (Tsai years, social media) | 2024 | seed | 社交→涉台舆论变迁 | 📜Q | 无 |
| T3-CHOO22 | recent study | 代表论证 | How #TaiwanCanHelp Reverberates | 2022 | seed | 标签扩散 | 📜Q | 无 |
| T3-LIUOPHIR22 | recent study | 代表论证 | Hashtag activism: Taiwan in the WHO | 2022 | skimmed | 台湾入世卫标签框架（★方法范本） | 📜Q | 无 |
| T3-JACOBS23 | recent study | 第一手阅读对象 | Tracking China's cross-strait bot networks | 2023 | skimmed | 涉台机器人网络 | 📜Q（arXiv） | 数据集许可 |
| T3-CHEN23 | recent study | 代表论证 | Public Opinion Evolution: Pelosi's Visit | 2023 | seed | 佩洛西舆情演化建模 | 📜Q | 无 |
| T3-CHANG24 | recent study | 代表论证 | US-skepticism in 2024 Taiwanese election | 2024 | seed | 疑美论叙事 | 📜Q | 无 |
| T3-KILTHUB | tool / dataset | 第一手阅读对象 | Pelosi Visit Twitter dataset (~1.76M tweets) | ~2022 | seed | 佩洛西事件全周期推文（★潜在数据源） | ⚠️待核验 | 元数据/许可 |
| T3-BRADSHAW19 | institution / community | 背景 | The Global Disinformation Order | 2019 | skimmed | 组织化操纵全球清单 | 📜Q | 无 |

### D. 方法与平台数据（可行性底座）

| Source ID | 来源类型 | 证据角色 | Title | Year | Status | 人话摘要 | 证据 | Need verification |
|---|---|---|---|---|---|---|---|---|
| T3-RIPAPI24 | recent study | 方法资源 | RIP Twitter API: A eulogy | 2024 | skimmed | 学术 API 关闭影响 | 📜Q（arXiv） | 无 |
| T3-BARRIE21 | tool / dataset | 方法资源 | academictwitteR | 2021 | skimmed | 历史学术 API 客户端 | 📜Q | 无 |
| T3-ACCTBLTY25 | recent study | 方法资源 | The Accountability Paradox (arXiv:2505.11577) | 2025 | seed | API 限额量化梳理 | 📜Q | 无 |
| T2-ROBERTS21 | tool / dataset | 方法资源 | Media Cloud: Massive Open Source Collection | 2021 | skimmed | 新闻语料平台 | 📜Q | Yahoo 收录待验证 |
| T2-KWAK21 | tool / dataset | 方法资源 | GDELT vs EventRegistry (ICWSM) | 2021 | skimmed | 事件数据库出处 | 📜Q | 无 |
| T2-HOPP19 | tool / dataset | 方法资源 | iCoRe (GDELT 通信研究界面) | 2019 | skimmed | 事件数据接口 | 📜Q | 无 |
| T2-VADER14 | tool / dataset | 方法资源 | VADER sentiment | 2014 | skimmed | 社交情感词典 | 📜Q | 无 |
| T2-LEXICODER12 | tool / dataset | 方法资源 | Lexicoder sentiment dictionary | 2012 | skimmed | 新闻情感词典 | 📜Q | 无 |

### 覆盖盲区记录（来自搜索子代理，勿当"没有任何既有研究"使用）

1. NYT/WaPo 以台湾为主体的 2017–2026 同行评审框架研究几乎缺位（多为学位论文/中文文献）——Yahoo News 语料可填补。
2. "China threat × Taiwan"组合框架在美媒的直接实证未见——只有威胁建构邻近文献。
3. 特朗普第一任期（2017–2020）涉台 Twitter 话语研究空白。
4. Yahoo News 平台学术研究缺位（日本 Yahoo News 一篇已撤稿 W4385793133，慎用）。
5. 涉台事件"新闻→社交"定量扩散研究极少（仅方法邻近文献）。
6. de Vreese 2005、Golan 2006 本次 API 未命中，真实性高但引用前必须补核。
