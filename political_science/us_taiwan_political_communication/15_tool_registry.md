<!--
Field: us_taiwan_political_communication
Mode: full_onboarding
Domain archetype: social_science
Created date: 2026-08-30
-->

# 15 Tool Registry / 工具生态注册表

Last updated: 2026-08-30

## 使用说明

本文件记录软件、数据库、benchmark、硬件平台或官方工具。工具状态可能变化，涉及版本和能力时优先查官方文档。本包的工具分四类：语料获取、文本分析、信度/评估指标、文献与事件数据。时效性信息（API 价格、工具存活）标注核对日期，过期前需复查。

Field / 领域：us_taiwan_political_communication

## Tool Entry / 工具条目（语料获取）

Tool / 工具：X/Twitter API（现行分层：Free / Basic / Pro / Enterprise）
Plain-language summary / 人话摘要：从 X 官方获取推文的唯一合规接口；2023 年学术研究轨（Academic Research product track，2021–2023 存在，免费 10M 推文/月、全档案搜索）已被取消，现为付费分层，免费层限额极小（约 500 条/月量级，2024-11 报道），回溯能力有限。
Maintainer / institution / 维护者或机构：X Corp.
URL：https://developer.x.com/
Status: verified
Domain / 领域：社交平台数据
Primary use / 主要用途：获取 2026 年起的涉台事件窗口推文；近窗口回溯
Supported platforms / 支持平台：HTTP API
Inputs / 输入：查询式（关键词/用户/时间窗）
Outputs / 输出：推文 JSON（文本、时间戳、转发/点赞、URL）
Strengths / 优点：合规、元数据完整
Limitations / 局限：无法回溯 2017–2023 历史全量；价格高；条款限制再分发
License / access / 许可或访问：付费分层；学术优惠取消
Relation to user assets / 与用户资产关系：用户是否订阅/能否申请预算 UNKNOWN_USER_ASSET
Possible benchmark role / 可作 benchmark 的方式：前瞻采集的事件窗口样本作为"官方口径"参照集
Need verification / 待核验：各层回溯天数、当前价格
Last updated / 最后更新：2026-08-30

---

Tool / 工具：Wayback Machine（Internet Archive CDX API）
Plain-language summary / 人话摘要：网页历史快照库；可用于按日期抓取 news.yahoo.com 的历史页面，是 Yahoo News 历史语料最现实的免费路径。
Maintainer / institution / 维护者或机构：Internet Archive
URL：https://web.archive.org/
Status: skimmed
Domain / 领域：网页存档
Primary use / 主要用途：事件窗口内 Yahoo News 涉台页面的历史文本
Supported platforms / 支持平台：HTTP API（CDX 索引 + 页面回放）
Inputs / 输入：URL 模式 + 时间范围
Outputs / 输出：快照列表、HTML
Strengths / 优点：免费、覆盖长、可编程
Limitations / 局限：快照密度不均（重要事件日可能密、平日稀）；HTML 需清洗；无全文搜索（按 URL/关键词定位受限）
License / access / 许可或访问：免费（尊重 robots 与条款）
Relation to user assets / 与用户资产关系：Python 可脚本化（高匹配）
Possible benchmark role / 可作 benchmark 的方式：单事件 pilot 验证可行性（MVP 第一步）
Need verification / 待核验：快照密度、与 GDELT 联动的定位效果
Last updated / 最后更新：2026-08-30

---

Tool / 工具：Media Cloud
Plain-language summary / 人话摘要：开源全球新闻抓取与分析平台，提供新闻全文/元数据检索与分析 API；若其美国源列表包含 Yahoo News，则是最省力的 Yahoo 侧语料来源。
Maintainer / institution / 维护者或机构：Media Cloud 项目（MIT / Northeastern 等合作）
URL：https://mediacloud.org/
Status: skimmed
Domain / 领域：新闻数据基础设施
Primary use / 主要用途：按事件/关键词检索美国新闻语料
Supported platforms / 支持平台：Web 界面 + Python 客户端
Inputs / 输入：关键词、日期范围、媒体源
Outputs / 输出：新闻条目（标题、正文、来源、时间戳）
Strengths / 优点：结构化、免费额度、学界通行
Limitations / 局限：源列表偏主流报纸/电视台，聚合器收录不确定；历史覆盖可能不达 2017
License / access / 许可或访问：开源 + 免费 API（有配额）
Relation to user assets / 与用户资产关系：Python 友好（高匹配）
Possible benchmark role / 可作 benchmark 的方式：与 Wayback 抓取结果做覆盖交叉验证
Need verification / 待核验：Yahoo News 收录情况、2017+ 覆盖
Last updated / 最后更新：2026-08-30

---

Tool / 工具：GDELT
Plain-language summary / 人话摘要：全球事件/语言/语气数据库，按分钟级记录新闻提及与事件编码；适合做涉台事件时间线定位与新闻侧"事件窗口"锚定。
Maintainer / institution / 维护者或机构：GDELT Project
URL：https://www.gdeltproject.org/
Status: skimmed
Domain / 领域：事件与新闻元数据
Primary use / 主要用途：涉台事件清单的新闻热度曲线、事件窗口标定
Supported platforms / 支持平台：HTTP API、BigQuery
Inputs / 输入：查询式（关键词/国家/时间）
Outputs / 输出：事件条目、提及计数、语气分
Strengths / 优点：免费、全球覆盖、时间粒度细
Limitations / 局限：不是全文库；事件编码（CAMEO）对"台湾"的归属处理需检查；语气分噪声大
License / access / 许可或访问：免费
Relation to user assets / 与用户资产关系：Python 可脚本化（高匹配）
Possible benchmark role / 可作 benchmark 的方式：事件烈度的外部锚定（区分"事件效应 vs 阶段效应"）
Need verification / 待核验：涉台查询式设计与 CAMEO 归属；原始论文（Leetaru & Schrodt 2013）未被 OpenAlex 索引，引用时以 Kwak & An 2021 / Hopp et al. 2019 作出处
Last updated / 最后更新：2026-08-30

---

Tool / 工具：NewsBank / LexisNexis（新闻全文商业库）
Plain-language summary / 人话摘要：商业新闻全文库；若收录 Yahoo News 则提供结构化历史文本。
Maintainer / institution / 维护者或机构：NewsBank Inc. / LexisNexis
URL：https://www.newsbank.com/ | https://www.lexisnexis.com/
Status: skimmed
Domain / 领域：新闻档案
Primary use / 主要用途：Yahoo News 历史文章的结构化检索
Supported platforms / 支持平台：Web 检索 + 导出
Inputs / 输入：关键词、日期、来源过滤器
Outputs / 输出：全文、元数据
Strengths / 优点：结构化、可批量、时间覆盖长
Limitations / 局限：订阅成本；聚合器内容收录不确定
License / access / 许可或访问：订阅（机构）
Relation to user assets / 与用户资产关系：用户机构订阅状态 UNKNOWN_USER_ASSET
Possible benchmark role / 可作 benchmark 的方式：与 Wayback 抓取做完整性对照
Need verification / 待核验：收录范围、机构订阅可用性
Last updated / 最后更新：2026-08-30

---

## Tool Entry / 工具条目（文本分析与评估）

Tool / 工具：stm（Structural Topic Models，R 包）
Plain-language summary / 人话摘要：允许把文档协变量（平台、政府期、事件类型）纳入主题比例模型，直接服务"演变机制"维度的主题层分析。
Maintainer / institution / 维护者或机构：Roberts, Stewart, Tingley 等（哈佛）
URL：https://www.structuraltopicmodel.com/
Status: verified
Domain / 领域：主题建模
Primary use / 主要用途：涉台文本的议题结构随时期/平台的变化
Supported platforms / 支持平台：R
Inputs / 输入：文档-词矩阵 + 协变量矩阵
Outputs / 输出：主题-文档比例 θ、主题-词分布 β、协变量效应
Strengths / 优点：协变量建模、学界引用厚
Limitations / 局限：产出 topic 而非 frame；R 依赖
License / access / 许可或访问：开源（GPL）
Relation to user assets / 与用户资产关系：需少量 R 迁移（用户 Python 熟练，R 成本低）
Possible benchmark role / 可作 benchmark 的方式：topic 层演变的基线模型
Need verification / 待核验：无
Last updated / 最后更新：2026-08-30

---

Tool / 工具：BERTopic / Gensim
Plain-language summary / 人话摘要：Python 生态的主题聚类（BERTopic：嵌入 + c-TF-IDF 主题标签）；适合 Python 用户的 topic 层探索。
Maintainer / institution / 维护者或机构：Maarten Grootendorst（BERTopic）/ Gensim 社区
URL：https://maartengr.github.io/BERTopic/
Status: skimmed
Domain / 领域：主题建模
Primary use / 主要用途：快速探索涉台语料的议题簇
Supported platforms / 支持平台：Python
Inputs / 输入：文本列表
Outputs / 输出：主题簇 + 标签
Strengths / 优点：Python 原生、易上手
Limitations / 局限：同样 topic≠frame；嵌入模型对政治语境的领域漂移
License / access / 许可或访问：开源（MIT）
Relation to user assets / 与用户资产关系：高匹配（Python）
Possible benchmark role / 可作 benchmark 的方式：与 STM 结果互证
Need verification / 待核验：权威引用、版本稳定性
Last updated / 最后更新：2026-08-30

---

Tool / 工具：LLM API（GPT-4/Claude 级模型，zero-shot / few-shot 编码）
Plain-language summary / 人话摘要：把人工编码手册写成 prompt 对全量语料批量编码，是 2017–2026 全时段语料唯一经济可行的语义编码路径（Gilardi et al. 2023 PNAS 支持其标注质量）。
Maintainer / institution / 维护者或机构：OpenAI / Anthropic 等
URL：https://openai.com/api/ | https://www.anthropic.com/api
Status: verified
Domain / 领域：LLM 文本标注
Primary use / 主要用途：框架元素（问题定义/归因/评判/对策）批量编码
Supported platforms / 支持平台：HTTP API / Python SDK
Inputs / 输入：文本 + 编码手册 prompt
Outputs / 输出：框架标签 + 理由/置信度
Strengths / 优点：规模、成本、语义深度兼得
Limitations / 局限：提示敏感性、立场/时态漂移、幻觉；必须人工子样本验证
License / access / 许可或访问：付费 API
Relation to user assets / 与用户资产关系：Python 友好；API 预算待确认
Possible benchmark role / 可作 benchmark 的方式：与人-人信度对标（人机一致性）
Need verification / 待核验：期刊接受惯例、模型版本锁定策略
Last updated / 最后更新：2026-08-30

---

Tool / 工具：Media Frames Corpus
Plain-language summary / 人话摘要：跨议题通用框架标注语料（15 类政策框架），监督式帧检测的起点与 benchmark。
Maintainer / institution / 维护者或机构：Boydstun, Card, Gross, Resnik, Smith（UW 等）
URL：https://github.com/dallascard/media_frames_corpus
Status: verified
Domain / 领域：帧标注语料
Primary use / 主要用途：通用框架（经济/安全/道德等）的分类器训练与评估
Supported platforms / 支持平台：数据文件（JSON/CSV）
Inputs / 输入：—（语料）
Outputs / 输出：标注文本 + 框架标签
Strengths / 优点：公开、跨议题、学界 benchmark
Limitations / 局限：新闻标题为主；不含涉台专属框架（需自建/扩展）
License / access / 许可或访问：开放研究语料
Relation to user assets / 与用户资产关系：高——可迁移预训练
Possible benchmark role / 可作 benchmark 的方式：通用框架检测的 F1 基线
Need verification / 待核验：许可证细节
Last updated / 最后更新：2026-08-30

---

Tool / 工具：VADER / Lexicoder（词典法）
Plain-language summary / 人话摘要：社交文本情感（VADER）与新闻文本情感（Lexicoder）词典；适合涉台话语的情感/价值维度辅助，不适合语义框架。
Maintainer / institution / 维护者或机构：Hutto & Gilbert（VADER）；Young & Soroka（Lexicoder）
URL：https://github.com/cjhutto/vaderSentiment
Status: verified
Domain / 领域：词典文本分析
Primary use / 主要用途：涉台文本情感极性与强度趋势
Supported platforms / 支持平台：Python（VADER）/ R 等
Inputs / 输入：文本
Outputs / 输出：情感分数
Strengths / 优点：零成本、可复现
Limitations / 局限：词典对政治术语（如"China threat"）语义粗糙
License / access / 许可或访问：开源
Relation to user assets / 与用户资产关系：高匹配
Possible benchmark role / 可作 benchmark 的方式：情感维度的描述基线
Need verification / 待核验：无
Last updated / 最后更新：2026-08-30

---

## Tool Comparison Table / 工具对比表

| Tool | 人话摘要 | Domain | Primary use | Strengths | Limitations | Relation to user assets | Status | Last updated |
|---|---|---|---|---|---|---|---|---|
| X API | 官方推文接口，回溯受限 | 社交平台数据 | 2026 起事件窗口采集 | 合规、元数据全 | 无 2017–2023 全量回溯 | 订阅状态 UNKNOWN_USER_ASSET | verified | 2026-08-30 |
| Wayback Machine | 网页历史快照 | 网页存档 | Yahoo News 历史页面 | 免费、可脚本 | 快照密度不均、需清洗 | Python 高匹配 | skimmed | 2026-08-30 |
| Media Cloud | 开源新闻语料平台 | 新闻数据设施 | 美国新闻检索 | 结构化、免费额度 | Yahoo 收录待验证 | Python 高匹配 | skimmed | 2026-08-30 |
| GDELT | 全球新闻事件/语气数据 | 事件数据 | 涉台事件时间线锚定 | 免费、分钟级 | 非全文、编码归属需查 | Python 高匹配 | skimmed | 2026-08-30 |
| NewsBank/LexisNexis | 商业新闻全文库 | 新闻档案 | Yahoo 历史全文 | 结构化、批量 | 订阅成本、收录待验证 | 订阅状态 UNKNOWN_USER_ASSET | skimmed | 2026-08-30 |
| stm | 协变量主题模型 | 主题建模 | 议题演变建模 | 协变量建模、引用厚 | topic≠frame；R | 低迁移成本 | verified | 2026-08-30 |
| BERTopic/Gensim | Python 主题聚类 | 主题建模 | 议题簇探索 | Python 原生 | topic≠frame | Python 高匹配 | skimmed | 2026-08-30 |
| LLM API | 大批量框架编码 | LLM 标注 | 框架元素编码 | 规模+语义深度 | 漂移、需人机一致性 | Python 高匹配 | verified | 2026-08-30 |
| Media Frames Corpus | 通用框架标注语料 | 帧检测基准 | 监督训练/评估 | 公开、benchmark | 无涉台专属框架 | 高 | verified | 2026-08-30 |
| VADER/Lexicoder | 情感词典 | 词典分析 | 情感趋势辅助 | 零成本 | 政治语义粗糙 | 高匹配 | verified | 2026-08-30 |
