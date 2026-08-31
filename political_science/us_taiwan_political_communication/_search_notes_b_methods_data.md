# 文献与方法搜索 B：框架方法、平台与数据可行性

Last updated: 2026-08-30

> 目的：为「美国涉台政治传播（2017.01–2026.01；Yahoo News ↔ X 跨平台；事件驱动取样）」field pack 的 gap 表、项目卡片与 MVP 计划提供方法操作性与数据可行性依据。
> 数据来源：OpenAlex API（curl，`&mailto=research@example.com`，2026-08-30 检索）+ web_search（时效性事实）。所有文献条目均来自检索可见元数据；时效性事实附出处 URL；无法确证者标 NEEDS_VERIFICATION。
> 术语：frame building=框架建构；intermedia agenda setting=媒介间议程设置；intermedia frame setting=媒介间框架设置。

## 搜索词记录

- OpenAlex（search= 与 filter=title.search）：framing analysis computational；structural topic model political communication；LLM frame detection news；framing measurement content analysis reliability；intermedia agenda setting twitter；cross-platform political communication news social media；agenda setting news media twitter comparison；frame building news sources；content analysis media frames improving reliability validity；media frames corpus；networks big data intermedia agenda；China Taiwan news framing；GDELT；media cloud global news；twitter academic research data collection；twitter api access research；dictionary methods political text；retweet diffusion；frame dynamics news coverage；topic coherence measures；topic model evaluation。
- web_search：Twitter academic API discontinued 2023；X API pricing 2025；snscrape 2025；Yahoo News aggregator original content；Yahoo News archive Wayback；NewsBank/LexisNexis Yahoo；Library of Congress Twitter archive；Internet Archive Twitter Stream Grab；RIP Twitter API；X API 免费层限额。

## 主题 1：框架分析的方法论

### 文献（OpenAlex 元数据）

| 年份 | 作者 | 标题 | 期刊/出处 | 引用 | 对设计的要点 |
|---|---|---|---|---|---|
| 1993 | Entman | Framing: Toward Clarification of a Fractured Paradigm | Journal of Communication | 15890 | 框架四功能定义：界定问题/归因/道德评判/对策建议（doi:10.1111/j.1460-2466.1993.tb01304.x） |
| 2003 | Entman | Cascading Activation: Contesting the White House's Frame After 9/11 | Political Communication | 981 | frame building 的层级激活模型（行政→精英→媒体→公众）（doi:10.1080/10584600390244176） |
| 2008 | Matthes & Kohring | The Content Analysis of Media Frames: Toward Improving Reliability and Validity | Journal of Communication | 1023 | 经典操作化：把框架拆为可编码元素组合（问题定义/归因/评价/对策），显著提升信度（doi:10.1111/j.1460-2466.2008.00384.x） |
| 2011 | David, Atun, Fille, Monterola | Finding Frames: Comparing Two Methods of Frame Analysis | Communication Methods and Measures | 108 | 归纳 vs 演绎帧分析的系统比较（doi:10.1080/19312458.2011.624873） |
| 2012 | Hallgren | Computing Inter-Rater Reliability for Observational Data | TQMP | 3918 | Krippendorff's alpha 等信度指标计算教程（doi:10.20982/tqmp.08.1.p023） |
| 2013 | Grimmer & Stewart | Text as Data: The Promise and Pitfalls of Automatic Content Analysis | Political Analysis | 3284 | 政治文本自动内容分析综述：dictionary/监督/无监督三类路线（doi:10.1093/pan/mps028） |
| 2014 | Roberts, Stewart, Tingley, Lucas | Structural Topic Models for Open-Ended Survey Responses | AJPS | 1991 | STM：主题比例可随协变量（如时间/媒介类型）回归，适合演变机制（doi:10.1111/ajps.12103） |
| 2015 | Card, Boydstun, Gross, Resnik | The Media Frames Corpus: Annotations of Frames Across Issues | ACL 2015 | 233 | 跨议题通用帧标注语料（Media Frames Corpus），监督式帧检测基准（doi:10.3115/v1/p15-2072） |
| 2015 | Lucas, Nielsen, Roberts, Stewart | Computer-Assisted Text Analysis for Comparative Politics | Political Analysis | 489 | 计算文本分析进比较政治：方法选择决策树（doi:10.1093/pan/mpu019） |
| 2015 | Röder, Both, Hinneburg | Exploring the Space of Topic Coherence Measures | WSDM 2015 | 2231 | 主题一致性指标（C_V/NPMI/UMass）统一评估（doi:10.1145/2684822.2685324） |
| 2019 | Walter & Ophir | News Frame Analysis: An Inductive Mixed-method Computational Approach | Communication Methods and Measures | 224 | 归纳式混合计算框架分析：词嵌入聚类+人工验证（doi:10.1080/19312458.2019.1639145） |
| 2019 | Liu, Guo, Mays, Betke | Detecting Frames in News Headlines…US Gun Violence | NAACL 2019 | 102 | 标题级帧检测 + 帧趋势分析 pipeline（doi:10.18653/v1/k19-1047） |
| 2023 | Gilardi, Alizadeh, Kubli | ChatGPT outperforms crowd workers for text-annotation tasks | PNAS | 1056 | LLM 编码在标注任务上优于众包工人（doi:10.1073/pnas.2305016120） |
| 2023 | Ziems et al. | Can Large Language Models Transform Computational Social Science? | Computational Linguistics | 492 | LLM 用于社科编码的系统讨论（doi:10.1162/coli_a_00502） |

### 方法/事实要点

- **人工编码路线（可信基准）**：Matthes & Kohring（2008）"元素组合法"是当前通信学框架测量的主流操作化——不直接给整篇文本"贴框架标签"，而是分别编码问题定义/因果归因/道德评判/处理建议等元素，再由元素组合推导框架；此法提升编码者间信度。信度惯例：Krippendorff's alpha，探索性 ≥ .67、结论性 ≥ .80（阈值惯例为经验共识，NEEDS_VERIFICATION 具体文献出处）。
- **计算路线三分**：① dictionary（如 Lexicoder 情感词典，Young & Soroka 2012，doi:10.1080/10584609.2012.671234）适合情绪/价值维度，不适合语义框架；② 无监督（LDA/STM）得的是 **topic 而非 frame**——frame 需语义角色成分，STM 只能做"主题演变"（对 RQ-b 演变机制有用），frame 识别仍需词典/监督/LLM；③ 监督学习依赖标注语料（Media Frames Corpus 是唯一跨议题通用帧集，2015 后仍是 benchmark）。
- **LLM/prompt-based 编码（2022 后新常态）**：Gilardi 2023 表明 ChatGPT 零样本标注质量高；通信学期刊接受度仍要求与人工编码子样本交叉验证（报道口径，NEEDS_VERIFICATION 具体期刊政策）。推断：对 2017–2026 全时段语料，LLM 编码是唯一经济可行的大规模方案，但必须设人工编码子样本（~10%）测一致性。
- **关键操作化建议（推断）**：以 Entman 四功能为理论框架 + Matthes-Kohring 元素编码手册 + LLM 辅助编码 + 人工子样本信度验证，是同时满足"可发表（有人工信度）"与"可规模化"的组合。

## 主题 2：跨平台/跨媒介比较研究设计

### 文献（OpenAlex 元数据）

| 年份 | 作者 | 标题 | 期刊/出处 | 引用 | 要点 |
|---|---|---|---|---|---|
| 2015 | Conway, Kenski, Wang | The Rise of Twitter in the Political Campaign: …Intermedia Agenda-Setting Effects | JCMC | 398 | 新闻↔Twitter 议程方向性检验（doi:10.1111/jcc4.12124） |
| 2016 | Vargo & Guo | Networks, Big Data, and Intermedia Agenda Setting | Journalism & Mass Communication Quarterly | 212 | 网络法测媒介间议程设置（传统/党派/新兴在线媒体）（doi:10.1177/1077699016679976） |
| 2016 | Rogstad | Is Twitter just rehashing? Intermedia agenda setting between Twitter and mainstream media | JITP | 145 | 议题层面：Twitter 是否只是回声（doi:10.1080/19331681.2016.1160263） |
| 2017 | Harder, Sevenans, Van Aelst | Intermedia Agenda Setting in the Social Media Age | Int'l Journal of Press/Politics | 294 | 选举语境传统媒体主导议程（doi:10.1177/1940161217704969） |
| 2017 | Valenzuela, Puente, Flores | Comparing Disaster News on Twitter and Television | J. Broadcasting & Electronic Media | 109 | 同事件跨平台（灾害事件）比较模板（doi:10.1080/08838151.2017.1344673） |
| 2018 | Wang & Guo | Framing GM mosquitoes in online news and Twitter: Intermedia frame setting | Public Understanding of Science | 39 | **frame 层面**的跨平台议程设置，直接对口用户 RQ（doi:10.1177/0963662518799564） |
| 2019 | Su & Borah | Who is the agenda setter? Examining intermedia agenda-setting between Twitter and newspapers | JITP | 157 | 议程设置者识别（doi:10.1080/19331681.2019.1641451） |
| 2020 | Wells et al. | Trump, Twitter, and news media responsiveness: A media systems approach | New Media & Society | 141 | 政治人物推文→新闻媒体响应时序（doi:10.1177/1461444819893987） |
| 2024 | Su & Xiao | Intermedia Attribute Agenda Setting Between US Mainstream Newspapers and Twitter | JMCQ | 12 | 属性（attribute=框架维度）议程设置两研究（doi:10.1177/10776990231221150） |
| 2023 | Wang, Song, Chen | Tracing the Flow of Climate Change Frames: Intermedia Agenda Setting Between Twitter and News | Emerging Media | 7 | 气候议题帧流动（doi:10.1177/27523543231218296） |
| 2018 | Firdaus, Ding, Sadeghian | Retweet: A popular information diffusion mechanism – A survey | Online Social Networks and Media | 60 | 转发/扩散机制综述（doi:10.1016/j.osnem.2018.04.001） |
| 2023 | Jiang, Ren, Ferrara | Retweet-BERT | ICWSM | 36 | 扩散+语言特征的政治推文分析（doi:10.1609/icwsm.v17i1.22160） |

### 方法/事实要点

- **事件驱动采样是成熟范式**：Valenzuela 2017（灾害事件）、Wang & Guo 2018（议题事件）均以"同一事件/议题"锚定新闻与 Twitter 双语料，再比较帧/议程——正是用户设计的模板。
- **因果/时序方法**：媒介间议程设置常用时间序列（Granger 因果 / VAR，见 Conway 2015、Su & Borah 2019）或网络方法（Vargo & Guo 2016）；帧层面较少见，属可贡献点（推断）。
- **方法学问题清单**：① 文本形态不可比（长新闻 vs ≤280 字符推文）→ 需在分析层面定义可比单元（标题/主题句 vs 推文）；② 时间对齐窗口（事件前后几天/几周）需在编码手册中固定；③ 平台 affordance 差异（转推=广播 vs 新闻=生产）应作为解释变量而非噪声；④ Yahoo 为聚合器时"新闻文本"包含非原创内容，需记录来源标签（见主题 4）。

## 主题 3：Twitter/X 学术数据获取的现实约束

### 文献/元数据

- Barrie & Ho（2021）academictwitteR：访问 Twitter 学术研究产品轨 v2 API 的 R 包（JOSS，doi:10.21105/joss.03272，引用 234）——该轨道现已不存在，包属历史工具。
- Câmpan et al.（2018）Is Data Collection through Twitter Streaming API Useful for Academic Research?（IEEE Big Data，doi:10.1109/bigdata.2018.8621898）。
- Murtfeldt, Paik, Alterman, Kahveci, West（2024）RIP Twitter API: A eulogy to its vast research contributions（arXiv:2404.07340）——对学术 API 关闭后研究影响的系统记录。
- 平台 API 限制的量化综述：arXiv:2505.11577（The Accountability Paradox，含免费层 2018≈50M 推/天→现限额对照表）。

### 时效性事实（带出处）

- **2021–2023 学术 API**：Twitter 学术研究产品轨（Academic Research product track）2021 年推出（免费、10M 推/月、全档案搜索），2023 年 API 全面付费化后被移除/替换；影响综述见 [RIP Twitter API (arXiv:2404.07340)](https://arxiv.org/abs/2404.07340)。
- **现行 X API**：分层付费（Free/Basic/Pro/Enterprise），多次涨价，见 [Techzine: X makes access to APIs more expensive](https://www.techzine.eu/news/devops/125764/x-makes-access-to-apis-more-expensive/)、[X 免费层自动发帖限额报道（2024-11，约 500 条/月）](https://news.mynavi.jp/article/20241101-3057347/)。免费层无法回溯历史推文；付费层回溯窗口有限（NEEDS_VERIFICATION 当前各层具体回溯天数）。
- **官方全量存档不存在**：美国国会图书馆 2017-12 起停止全量推文归档（[USA Today 报道](https://www.usatoday.com/story/news/politics/onpolitics/2017/12/27/library-congress-no-longer-archive-every-tweet/983606001/)）。
- **替代历史数据**：Archive Team 的 Twitter Stream Grab（[archive.org/details/twitterstream](https://archive.org/details/twitterstream)，元数据见 [travisbrown/tsg-metadata](https://github.com/travisbrown/tsg-metadata)）覆盖约 2011–2015，**不含 2017+ 时段**；Internet Archive 对推文仅有零散快照（NEEDS_VERIFICATION 覆盖度）。
- **抓取工具现状**：snscrape 曾为主流（2019–2023），X 强化反爬后稳定性下降，[snscrape.com 状态说明](https://snscrape.com/does-snscrape-still-work/)（2026 现状 NEEDS_VERIFICATION）；twint 已随 API 变化停止维护（社区共识，NEEDS_VERIFICATION 权威出处）；商业替代如 [Scrapfly 的 2026 抓取指南](https://scrapfly.io/blog/posts/how-to-scrape-twitter)、第三方学术接口 [Sorsa API](https://api.sorsa.io/solutions/academic-research)（成本/ToS 合规需评估）。
- 平台 API 限制对透明度研究的系统梳理见 [arXiv:2505.11577](https://arxiv.org/html/2505.11577v2)。

### 对 2017–2026 全时段回溯取样的影响（推断）

- **不存在官方"一键回溯全时段"路径**：2017.01–2020.12 与 2022.05–2026.01 无学术 API 时代数据；2021.01–2023.04 曾有学术 API 可采但已无法回补全量。
- **现实路径**：① 事件窗口内的事前存档（研究者在事件期间用第三方存档/快照持续抓取——对已过去的 2017–2025 不可行）；② 公开数据集拼合（Stream Grab 不覆盖 2017+；ICWSM/数据集仓库中的政治推文集需逐库盘点，本搜索未逐一验证，NEEDS_VERIFICATION）；③ 商业历史 API（Sorsa 等）做 2017+ 回溯，成本与合规待评估；④ **把 X 分析重定义为"可获取子集"**：如聚焦 2021–2023 学术 API 窗口 + 事件期快照补采（2026 起前瞻），或在论文中明确 X 语料为"事件驱动的代表性样本而非全量"。

## 主题 4：Yahoo News 的内容结构与可获得性

### 时效性事实（带出处）

- **性质**：Yahoo News 1996 年上线，长期是**新闻聚合器 + 有限原创**的混合体；与 ABC News 内容合作（2011，[The Atlantic](https://www.theatlantic.com/business/2011/10/abc-news-and-yahoo-link-news/337202/)）；与 Reuters/AP 等通讯社签约转载；自身亦有编辑部原创（媒体观察见 [AJR: Is It Journalism?](https://ajrarchive.org/article.asp?id=2540)、[Media Bias/Fact Check 对 Yahoo News 的定性](https://mediabiasfactcheck.com/yahoo-news/)）。2000s 末期曾并入 HuffPost 内容合作，后随 Verizon/Oath（2017）、Apollo（2021）易主（合作时间线细节 NEEDS_VERIFICATION）。
- **Yahoo 近年战略**：向"新闻首页 + 聚合"定位投入（[INMA: How Yahoo balances product in a news culture](https://www.inma.org/blogs/product-initiative/post.cfm/how-yahoo-balances-product-in-a-news-culture)、[The Drum 2018 报道](https://www.thedrum.com/opinion/2018/04/12/with-zuckerberg-the-ropes-yahoo-aims-displace-social-media-home-news)）。
- **历史存档**：Wayback Machine 对 news.yahoo.com 有长期快照（示例快照见 [web.archive.org](http://web.archive.org/all/20150522221156/http://en.wikipedia.org/wiki/Yahoo!_News)）；美国国会图书馆曾将 Yahoo News 收入网页档案（[LOC 条目](https://www.loc.gov/item/lcwaN0020266/)）；**NewsBank/LexisNexis 是否收录 Yahoo News 全文未确证，NEEDS_VERIFICATION**；Yahoo 站内搜索/API 未见公开可用接口（NEEDS_VERIFICATION）。

### 对"新闻组织代表"取样的影响（推断）

- Yahoo News 更宜定义为**"新闻聚合面"**而非单一编辑部：其涉台报道文本 = 通讯社稿（Reuters/AP）+ 伙伴稿 + 少量原创。取样的方法论含义：① 若研究"新闻组织如何框架"，需在文本层记录原始来源标签，或改用其原创/编辑策划内容；② 若研究"美国公众可见的新闻流"，聚合版恰好是更贴近受众的形态——但须在论文中明确这一操作化定义；③ 跨平台比较时 Yahoo 聚合版与 X 推文的"事件触发"逻辑一致（都围绕事件聚合），可比性反而较好（推断）。
- 事件级回溯取样可行路径：以事件时间线 + 关键词（Taiwan/TSMC/佩洛西访台等）在 Wayback Machine 按日抓取 news.yahoo.com 快照（需评估快照密度，NEEDS_VERIFICATION），或用 GDELT 先定位事件窗口（见主题 5）。

## 主题 5：可复用工具与指标

### 文献/事实

- **Media Cloud**：开源全球新闻抓取与分析平台（Roberts et al. 2021, ICWSM, doi:10.1609/icwsm.v15i1.18127，引用 67）；**是否收录 Yahoo News 需验证（NEEDS_VERIFICATION，其美国源列表公开可查）**；若收录，可大幅简化 Yahoo 侧语料获取。
- **GDELT**：全球事件/语言/语气数据库；原始论文（Leetaru & Schrodt 2013）未在 OpenAlex 索引到，可用 [Kwak & An 2021 的 GDELT/EventRegistry 对比](https://doi.org/10.1609/icwsm.v10i1.14763) 与通信研究界面 [iCoRe（Hopp et al. 2019, doi:10.5117/ccr2019.1.002.hopp）](https://doi.org/10.5117/ccr2019.1.002.hopp) 作为出处；用于事件识别与时间线定位（事件数据，非全文）。
- **词典工具**：VADER（社交文本情感，[Hutto & Gilbert 2014, doi:10.1609/icwsm.v8i1.14550](https://doi.org/10.1609/icwsm.v8i1.14550)）；Lexicoder 情感词典（Young & Soroka 2012）。
- **主题建模**：STM（R 包 stm）；BERTopic（c-TF-IDF 类标签方法——BERTopic 论文未在本轮检索到独立条目，NEEDS_VERIFICATION 权威引用，可用其官方文档）；一致性指标用 Röder et al. 2015（C_V/NPMI）。
- **帧检测基准**：Media Frames Corpus（Card et al. 2015）；Walter & Ophir 2019 的"嵌入+人工验证"归纳流程。
- **Crimson Hexagon**：已被 Brandwatch 收购（2020s 市场事实，NEEDS_VERIFICATION 权威出处），商业社媒分析，历史推文检索能力需商业评估。

### 工具/指标清单

| 名称 | 用途 | 状态/许可 | 对用户设计的适用性 |
|---|---|---|---|
| OpenAlex | 文献元数据 | 免费 API | 已完成；后续 gap 表引用用 |
| Media Cloud | 新闻抓取/全文/分析 | 开源 | 高——若覆盖 Yahoo News（待验证） |
| GDELT | 事件数据（时间线） | 免费 | 中高——事件驱动取样的锚点 |
| Wayback Machine | Yahoo News 历史页面快照 | 免费 | 中——按事件抓快照，密度待验证 |
| NewsBank / LexisNexis | 新闻全文库 | 订阅 | 中——Yahoo 收录待验证 |
| X API（现行分层） | 推文获取 | 付费；学术优惠取消 | 低——仅近窗回溯 |
| academictwitteR | 学术 API 客户端 | 已随轨道失效 | 历史价值 |
| snscrape / twint | 爬取 | twint 失效；snscrape 受限 | 低-中——合规与稳定性风险 |
| Sorsa 等第三方历史 API | 历史推文 | 商业 | 中——需评估成本/ToS |
| Archive Team Stream Grab | 历史推文（2011–2015） | 免费 | 低——时段不覆盖 2017+ |
| stm (R) / BERTopic / Gensim | 主题建模 | 开源 | 高——演变机制（RQ-b） |
| VADER / Lexicoder | 词典情感/价值 | 免费 | 中——情绪维度辅助 |
| Media Frames Corpus | 帧标注基准/迁移 | 开放 | 高——监督帧检测起点 |
| Krippendorff's alpha / coherence (C_V,NPMI) / F1 | 信度与模型评估 | 标准指标 | 高——人工-机器一致性验证 |

## 平台数据可行性小结

- **X 全时段回溯取样（2017–2026）**：**不可行（官方路径）**——学术 API 已取消、免费层近乎不可用、LoC 无全量存档、Stream Grab 不覆盖 2017+。**现实降级方案（按可行性排序）**：① 事件驱动子集 + 商业历史 API（Sorsa 类，成本待估）；② 公开政治推文数据集拼合（需逐库盘点，未验证）；③ 把 X 语料窗口重定义为 2021–2023（学术 API 时代）并加 2026 起前瞻采集；④ 明确声明"代表性样本而非全量"以保住可发表性。**结论：MVP 应把 X 侧限定为 1–3 个事件 × 有限窗口，或依赖第三方数据集，不能承诺全时段全量。**
- **Yahoo News 取样**：**可行但需重构定义**——聚合器性质使"新闻组织代表"必须操作化为"聚合新闻流（含来源标签）"或"Yahoo 原创/编辑策划内容"；历史文本经 Wayback Machine（密度待验证）或订阅库（收录待验证）获取；Media Cloud 若覆盖则最优。**结论：MVP 的 Yahoo 侧可行，建议先做 1 个事件的 Wayback 快照可行性测试（pilot）。**

## 覆盖率说明（盲区、待确认项）

- **盲区**：① LLM-based frame detection 在通信学期刊的具体发表案例（本轮只确认了通用标注与检测技术，未定位"帧检测+LLM"的通信学实证代表作）；② 中国/台湾议题的 US 媒体框架实证文献较少命中（仅 Du et al. 2018「占领中环」跨港台陆框架比较、Fu 2025 佩洛西访台框架分析），说明该子领域文献稀疏——本身可作 gap 论据（推断）；③ Yahoo News 的学术研究文献几乎缺位（仅媒体观察/行业报道）；④ 中文语境研究按要求略过。
- **待确认（NEEDS_VERIFICATION）**：Krippendorff alpha 阈值惯例的具体出处；X API 各付费层当前回溯天数与价格；snscrape/twint 2026 现状；Media Cloud 是否收录 Yahoo News；NewsBank/LexisNexis 对 Yahoo News 的全文收录；Wayback 对 news.yahoo.com 的快照密度；Crimson Hexagon→Brandwatch 收购权威出处；BERTopic 论文权威引用；公开政治推文数据集清单。

## 证据等级说明

- **文献条目**：全部来自 OpenAlex API 返回元数据（标题/作者/年份/期刊/DOI/引用数），未编造；个别标注为"未索引到"（如 Leetaru & Schrodt 2013 GDELT 原始论文）时已给出替代可引用出处。
- **时效性事实**：每条附来源 URL（Techzine、mynavi、USA Today、arXiv、archive.org、Media Bias/Fact Check、The Atlantic、AJR、LOC、snscrape.com、Sorsa、Scrapfly 等）；无法从本次检索直接确证者统一标 NEEDS_VERIFICATION，不臆断。
- **推断**：凡"操作化建议""对取样影响"类判断均明确标注"推断"，与事实性陈述区分。
