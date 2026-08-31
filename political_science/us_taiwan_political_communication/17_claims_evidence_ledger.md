<!--
Field: us_taiwan_political_communication
Mode: full_onboarding
Domain archetype: social_science
Created date: 2026-08-30
-->

# 17 Claims Evidence Ledger / 中心论断与证据账本

Last updated: 2026-08-30

## 使用说明

本文件不只是普通 claim 列表。它是生成 `20_gap_table.md`、`22_project_candidates.md` 和 `23_mvp_experiment_plan.md` 前的 Core Claims Gate，并记录进入项目执行前的 Operationalization Gate 结论。下游研究判断必须引用或继承这里的中心论断、任务可操作化状态和允许结论层级。

生成或更新本文件前必须读取：`USER_BRIEF.md`、`11_term_disambiguation.md` 中的 Concept Boundary Contract、`14_paper_registry.md`、`OPERATIONALIZATION_PROTOCOL.md`。

## Gate verdict / 门控结论

概念边界状态：**通过（full_onboarding 门槛）**——核心概念（框架/框架建构/议程设置/媒介间议程设置）达到 `source_checked`（经典文献条目级核验）；「舆论场」与「演变机制」为 `contested`/`working_definition`，已写入 Concept Boundary Contract 并约束下游措辞。

中心论断状态：**通过，强度受限**——所有支撑研究推进层的论断均 ≤ `working_definition`；novelty 类论断全部降级为 provisional；无 `rejected` 论断。

任务可操作化状态：**priority project P1 为 `provisional`**——任务定义与输入集合已写清，但数据可得性（X 历史语料、Yahoo 快照密度）尚未经实测验证，MVP 必须写成消歧型（先验证取样可行性、编码可复现性与测量定义），不得承诺机制确证。

允许进入的下游层级：
- introductory_explanation ✅
- provisional_gap ✅
- project_candidate ✅
- mvp_design ✅（仅消歧型，受 P1 的 provisional 状态约束）
- strong_claim_not_allowed ❌（"因果机制揭示""美国公众态度"等表述禁止）

Need verification: 数据可行性实测（23 MVP 第 1 周）、事件清单日期核验、经典文献页码级引用（精读后补）。

## Core Claim / 中心论断

Claim ID: C1（概念工作定义）
论断内容：本包"框架"采用 Entman 四功能定义（问题定义/因果归因/道德评价/对策建议的选择与凸显），编码层以 Matthes & Kohring 元素组合法操作化。
论断类型：concept_definition
依赖哪些概念边界：11 号文件 §1-§2。
支持哪些下游文件或项目：12 field map、16 指标、20 gap、22 P1 编码方案、23 MVP。
证据：Entman 1993（📜Q 条目级）；Matthes & Kohring 2008（📜Q 条目级）。全文论点级证据待精读。
反证或替代解释：通用框架清单（Boydstun 等 Media Frames Corpus）与议题专属框架（涉台危机框架）的取舍未定——见 G4。
证据状态：source_checked（条目级）；全文级 NEEDS_VERIFICATION
允许用于什么层级的结论：project_candidate
若该论断失效，需要撤回或修改什么：编码手册需整体重设计；22 P1 的编码步骤作废重写。
Need verification: 精读补页码级引用。Last updated: 2026-08-30

---

Claim ID: C2（平台舆论场限定）
论断内容：本包"舆论场"指平台/媒介上可观察的涉台议题-框架文本分布；X 用户为非概率样本，文本分布不得外推为美国民意。
论断类型：concept_definition
依赖哪些概念边界：11 号文件契约表"舆论场=民意"过度等同条目。
支持哪些下游文件或项目：全部下游结论措辞、02 frontier compass、01 overview。
证据：抽样与平台偏差的领域共识（推断）；X 用户结构偏差为平台研究常识，具体数据 NEEDS_VERIFICATION。
反证或替代解释：若未来补入民调数据（Chicago Council 等）可做文本-民意对照，但那是另一研究设计。
证据状态：working_definition
允许用于什么层级的结论：project_candidate（作为结论边界条款，非实证命题）
若该论断失效，需要撤回或修改什么：所有"平台舆论场"限定语可放松，但不影响其他层。
Need verification: X 用户人口学偏差的具体出处。Last updated: 2026-08-30

---

Claim ID: C3（领域空白初步判断）
论断内容：涉台议题在美国舆论场研究中，存在三个交叉盲区：①新闻侧以台湾为主体的框架研究少（多为涉华总框架或中文文献）；②涉台 X/Twitter 话语研究集中在 2020 后，特朗普一期空白；③帧层面（而非第一层议程）的涉台跨平台流动研究极少。
论断类型：novelty
依赖哪些概念边界："未搜到≠没有既有研究"的证据纪律。
支持哪些下游文件或项目：20 gap 表 G1/G2/G3。
证据：两次系统性搜索（OpenAlex 40+ 查询 + web_search）的覆盖盲区记录；搜索非穷尽。
反证或替代解释：可能存在未命中的学位论文、中文期刊、预印本；Tan/Grabe/Weaver 2026 已部分覆盖方法空间。
证据状态：working_definition（搜索证据有限）
允许用于什么层级的结论：provisional_gap（只能写"专门研究有限/未被本次搜索命中"，不能写"没有任何既有研究"）
若该论断失效，需要撤回或修改什么：G1-G3 的缺口定位改写为"已做但缺交叉区"。
Need verification: 补充 Google Scholar/中文库复查。Last updated: 2026-08-30

---

Claim ID: C4（Yahoo News 平台身份）
论断内容：Yahoo News 是"新闻聚合器+有限原创"混合体（通讯社/伙伴内容为主），"新闻组织代表"必须操作化为"聚合新闻流（含来源标签）"或"Yahoo 原创/编辑策划内容"；结论归因只能到"选择/呈现层"。
论断类型：platform_bridge
依赖哪些概念边界：11 号文件 §4 对比组 3。
支持哪些下游文件或项目：12 field map、20 gap、22 P1 输入集合、23 MVP 取样步骤。
证据：公开报道（The Atlantic 2011 ABC 合作、AJR、Media Bias/Fact Check 定性，见 _search_notes_b 来源 URL）。
反证或替代解释：Yahoo 各时期内容构成变化（Oath/Apollo 时代），需取样时记录时间变化。
证据状态：source_checked（平台性质）；内容构成比例 NEEDS_VERIFICATION
允许用于什么层级的结论：project_candidate
若该论断失效，需要撤回或修改什么：若后续发现 Yahoo News 以原创为主，归因边界放松；反之更收紧。
Need verification: 2017–2026 各时段内容来源构成。Last updated: 2026-08-30

---

Claim ID: C5（X 数据可得性）
论断内容：X 平台 2017–2026 官方全时段回溯取样不可行（学术 API 2023 取消、免费层限额极小、LoC 2017 起停档、Stream Grab 不覆盖 2017+）；可行路径为事件窗口子集 + 第三方数据/商业历史 API + 明示"代表性样本"边界。
论断类型：feasibility
依赖哪些概念边界：无；纯数据事实。
支持哪些下游文件或项目：12 field map 瓶颈、20 gap G6、22 P1 数据方案、23 MVP 第 1 周消歧任务。
证据：RIP Twitter API（arXiv:2404.07340，📜Q）；LoC 停止归档（USA Today 报道 URL）；X API 分层报道（Techzine/mynavi URL）——见 _search_notes_b。
反证或替代解释：商业历史 API（Sorsa 类）可能部分覆盖，成本与合规待评估。
证据状态：source_checked
允许用于什么层级的结论：project_candidate（约束数据方案，非否定项目）
若该论断失效，需要撤回或修改什么：若获得全量授权（Enterprise 历史检索），MVP 数据方案升级。
Need verification: 各付费层当前回溯天数与价格。Last updated: 2026-08-30

---

Claim ID: C6（演变≠机制）
论断内容：三阶段框架分布差异是可观察的描述性演变；"演变机制"的因果主张需要事件固定效应/烈度匹配等对照设计排除替代解释（事件供给、平台算法、媒介生态变化）。
论断类型：mechanism
依赖哪些概念边界：11 号文件 §4 对比组 4。
支持哪些下游文件或项目：20 gap G7、22 P1 标题与结论边界、23 MVP 成功标准。
证据：研究设计常识 + 事件-阶段混淆的逻辑论证（推断）；GDELT 可提供事件烈度锚定。
反证或替代解释：若未来加政府话语/政策文本对照，机制主张可升级。
证据状态：working_definition
允许用于什么层级的结论：provisional_gap（机制主张只能作为候选解释）
若该论断失效，需要撤回或修改什么：若用户拿到更强的准实验设计（如政策断点），结论层级可上调。
Need verification: 事件清单的烈度标定数据。Last updated: 2026-08-30

---

Claim ID: C7（编码管线可行性）
论断内容："Entman 四功能 + 元素组合编码 + LLM 批量编码 + 人工子样本 Krippendorff alpha 验证"管线在技术上可行；通信学发表惯例要求人机信度报告。
论断类型：operationalization
依赖哪些概念边界：topic≠frame 边界（12 号文件 Axis 2）。
支持哪些下游文件或项目：16 指标、23 MVP 编码步骤。
证据：Gilardi et al. 2023 PNAS（📜Q 条目级）；期刊接受口径为领域经验（NEEDS_VERIFICATION 具体期刊政策）。
反证或替代解释：纯人工编码同样可行（成本高）；纯无监督不可行（语义深度不足）。
证据状态：working_definition
允许用于什么层级的结论：mvp_design（作为方法假设，MVP 第 2-4 周实证验证）
若该论断失效，需要撤回或修改什么：MVP 编码步骤退回全人工或词典法。
Need verification: 目标期刊的 LLM 编码接受政策。Last updated: 2026-08-30

---

## Operationalization Gate / 任务可操作化门

### 任务可操作化结论

P1（用户研究设计转写项目）声称的任务是"描述并解释 2017–2026 美国涉台政治传播中，Yahoo News 与 X 平台文本的框架建构、三阶段演变与跨媒介流动"。指标（框架分布 ΔP、流向检验、信度）与读出（编码管线）已写清；失败事件（取样失败、编码不可复现、数据缺口）与后选择政策已定义（见 22 P1 契约）。但**输入集合的可得性尚未实测**（X 历史语料、Yahoo 快照密度），因此 operational_status = `provisional`；23 号文件的 MVP 按消歧型设计：第 1 周先验证数据可行性与测量定义，第 2–4 周验证编码可复现性，然后才允许把 P1 升级为完整执行版。

### 支撑下游项目的任务定义

- 声称要验证的任务：P1 消歧阶段验证——(a) 事件驱动取样在 Yahoo News（Wayback/Media Cloud）与 X（可得子集）上可落地；(b) 框架编码方案可复现（人-人 α 达标）；(c) 双平台框架分布可比。
- 输入对象与允许输入集合：1–2 个涉台事件（建议佩洛西访台 2022.08 + 蔡英文-麦卡锡会面 2023.04）× 事件窗口（建议前后 14 天）× 两平台（Yahoo News 历史快照/档案；X 可得子集：CMU Kilthub 数据集或第三方历史 API 试采）；编码子样本 n≥200（跨平台分层）。
- 目标变换：文本 → 框架元素编码 → 框架标签 → 事件-平台框架分布 P(f)。
- 解码或读出要求：编码手册 v0.1（四功能元素 + 涉台候选框架清单）；LLM 编码与人工编码同手册、同子样本；信度报告 Krippendorff's alpha（人-人、人-机）。
- 失败 / 泄漏 / 后选择处理：取样失败（快照密度不足/数据集不可得）→ 事件或平台侧降级并记录，不静默替换；机器账号清洗失败 → 报告清洗比例与剩余样本偏差；编码失败的文本单独统计，不计入"已编码"分母；LLM 编码不事后按结论挑选提示（提示版本锁定）。
- baseline 公平性要求：LLM 编码与人工编码在同一子样本、同一手册比较；流向检验中两平台序列同粒度同窗口；事件效应对照使用 GDELT 热度序列（同等时间预算）。
- 阳性结果能证明什么：取样路径可行、编码方案可复现、双平台框架分布可比、初步框架差异可描述（描述层）。
- 阳性结果不能证明什么：不能证明机制归因（政府更迭/平台算法）、不能外推到全美民意、不能证明全时段代表性。
- 阴性结果意味着什么：若取样不可行 → P1 改为"2021–2023 学术 API 窗口 + 2026 前瞻"重定义时段；若编码不可复现 → 编码手册重设计（简化框架清单或换纯人工）。
- operational_status: **provisional**

---

## Ledger Table / 汇总表

| Claim ID | 论断类型 | 论断内容 | 证据状态 | 允许结论层级 | 支持下游文件 | operational_status | Need verification |
|---|---|---|---|---|---|---|---|
| C1 | concept_definition | 框架=Entman 四功能 + M&K 元素编码 | source_checked（条目级） | project_candidate | 12/16/22/23 | — | 页码级引用 |
| C2 | concept_definition | 舆论场=平台文本分布，≠民意 | working_definition | project_candidate | 02/01/全部结论措辞 | — | X 用户偏差出处 |
| C3 | novelty | 涉台×帧层面×跨平台交叉区文献稀疏 | working_definition | provisional_gap | 20 G1-G3 | — | 补库复查 |
| C4 | platform_bridge | Yahoo=聚合器，归因限选择/呈现层 | source_checked | project_candidate | 12/20/22/23 | — | 时段内容构成 |
| C5 | feasibility | X 全时段官方回溯不可行，需降级方案 | source_checked | project_candidate | 12/20/22/23 | — | 各层价格/回溯天数 |
| C6 | mechanism | 演变≠机制；机制需对照设计 | working_definition | provisional_gap | 20 G7/22 标题/23 标准 | — | 事件烈度数据 |
| C7 | operationalization | LLM+人工子样本编码管线可行 | working_definition | mvp_design | 16/23 | provisional（P1 整体） | 期刊政策 |
