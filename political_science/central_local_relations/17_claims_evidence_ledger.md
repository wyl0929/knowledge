<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-08 16:47:42
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-08 16:47:43
 * @FilePath     : /.agents/home/wyl/project/knowledge/political_science/central_local_relations/17_claims_evidence_ledger.md
 * @Description  :
-->
<!--
Field: 央地矛盾、集权与分权的治理逻辑
Mode: quick_scan
Domain archetype: social_science
Created date: 2026-07-08
-->

# 17 Claims & Evidence Ledger / 论断-证据台账

Last updated: 2026-07-08

---

## 使用说明

本台账记录本 field pack 中的核心论断，标注类型和证据状态。这是 **Core Claims Gate** 的产出——在生成 gap 或 project 之前，必须审查支撑下游判断的关键论断。

---

## 标注体系

### 论断类型
| 标注 | 含义 |
|------|------|
| `concept_definition` | 概念定义 |
| `mechanism` | 因果机制主张 |
| `phenomenon` | 对经验现象的描述或分类 |
| `platform_bridge` | 跨领域类比或方法迁移 |
| `novelty` | 创新性或独特性的主张 |
| `feasibility` | 关于某个研究方向的可行性判断 |
| `recommendation` | 对研究方向或方法的建议 |

### 证据状态
| 标注 | 含义 |
|------|------|
| `working_definition` | 本包内部工作定义，尚未对照文献核验 |
| `source_checked` | 已对照可靠来源核验 |
| `contested` | 在学术界存在争议 |
| `unresolved` | 尚无定论 |
| `NEEDS_VERIFICATION` | 无法在当前条件下核验 |

### 允许结论层级
| 层级 | 条件 |
|------|------|
| `introductory_explanation` | 概念状态至少为 `working_definition` |
| `provisional_gap` | 概念状态至少为 `working_definition`，证据不矛盾 |
| `project_candidate` | 支撑主张至少为 `source_checked` 或明确标为 `contested` |
| `mvp_design` | 所有支撑主张满足 operationalization 条件 |

---

## 台账

### C1：传统"集权/分权"话语混淆了权力流向和权力形态

| 项目 | 内容 |
|------|------|
| **位置** | `conflict.md` §一、§二；本包 `00_beginner_guide.md` §1 |
| **类型** | `concept_definition` |
| **证据基础** | 通过对宋朝（权力流向中央但执行权分散）和唐朝（权力流向地方但执行权集中）的对比分析，展示了"集权/分权"一维话语无法捕捉这两种情形的结构性差异 |
| **可能的反驳** | 政治学文献中关于 centralization/decentralization 已有更精细的概念工具（如 deconcentration vs devolution），本包提出的"行政分权/行动集权"区分是否已有文献覆盖？ |
| **证据状态** | `working_definition` — 分析上有用，但需要与已有学术术语对齐 |
| **允许结论层级** | `introductory_explanation` |

---

### C2：中国古代央地关系的核心矛盾是"维护中央安全的行政分权需求"与"完成治理任务的行动集权需求"之间的张力

| 项目 | 内容 |
|------|------|
| **位置** | `conflict.md` §二、§六 |
| **类型** | `mechanism` |
| **证据基础** | 唐/宋/明三朝案例均展示了这一张力：唐偏行动集权→藩镇之乱，宋偏行政分权→对外积弱，明试图折中但未能根本解决 |
| **可能的反驳** | (a) 三案例是否构成对这一主张的系统检验？还是选择性使用历史证据？(b) "外部压力"和"内部稳定"是否总是互相排斥？有些历史时期两者可能同时被满足 |
| **证据状态** | `working_definition` — 分析框架有启发性，但需要更多历史案例（包括反例）的检验 |
| **允许结论层级** | `provisional_gap` |

---

### C3：信息技术（大数据、实时监控、在线审计）从根本上改变了央地关系中的信息不对称

| 项目 | 内容 |
|------|------|
| **位置** | `conflict.md` §五.2；本包 `02_frontier_compass.md` §3.2 |
| **类型** | `mechanism`（同时具有 `novelty` 成分） |
| **证据基础** | 逻辑论证：信息技术的核心功能是降低信息获取和传输成本，而这正是委托-代理模型中信息不对称的来源。但缺乏系统性经验证据证明实际治理效果 |
| **可能的反驳** | (a) 信息获取能力提升 ≠ 信息处理能力提升（中央可能被数据淹没）；(b) 地方可以发展新的规避策略（数据造假升级）；(c) 监督的"最优密度"可能是一个倒U型而非单调递增 |
| **证据状态** | `unresolved` — 概念上有吸引力，但经验证据薄弱 |
| **允许结论层级** | `introductory_explanation`（不宜上升到 project_candidate 的核心依赖） |

---

### C4：任务型组织（领导小组、指挥部）可以实现"因事而聚，事毕则散"，打破唐朝节度使"临时→永久"的循环

| 项目 | 内容 |
|------|------|
| **位置** | `conflict.md` §五.3 |
| **类型** | `mechanism` + `novelty` |
| **证据基础** | 逻辑论证：现代制度基础设施（公文系统、审计、人事档案）提供了确保"临时"不滑向"永久"的制衡工具。但历史反例存在：明朝督抚就是"临时差遣→常态职位"的案例 |
| **可能的反驳** | "领导小组"也有从临时走向常设的（如某些领导小组存在了几十年）。在什么条件下"事毕则散"成立？这个条件没有被清晰地说明 |
| **证据状态** | `working_definition` — 分析框架有建设性，但需要更严格的机制条件和经验检验 |
| **允许结论层级** | `provisional_gap` |

---

### C5：央地关系研究可以借用控制论/系统科学的语言和建模工具

| 项目 | 内容 |
|------|------|
| **位置** | `02_frontier_compass.md` §5 P1 |
| **类型** | `platform_bridge` |
| **证据基础** | 类比论证：反馈回路 ↔ 监督机制，增益参数 ↔ 地方自由裁量权，传感器噪声 ↔ 信息扭曲。但类比本身不是证据——需要证明这种映射能产生超过现有政治学方法的新洞察 |
| **可能的反驳** | 控制论类比可能只是"重新描述"而非"解释"——政治系统的行为是否真的遵循控制论方程？如果只是语言层面的类比，其价值有限 |
| **证据状态** | `working_definition` — 类比有启发性，但需要最小可验证示例来证明其分析价值 |
| **允许结论层级** | `introductory_explanation`（需先有最小验证才能上升为 project_candidate 核心依赖） |

---

### C6：晋升锦标赛是中国地方政府行为的核心激励机制

| 项目 | 内容 |
|------|------|
| **位置** | `01_research_overview.md` §6.2 |
| **类型** | `mechanism` |
| **证据基础** | 周黎安（2007）及其后续大量实证研究。但该理论也面临批评：晋升与 GDP 的相关性在 2010s 后下降；环境、维稳等指标权重增加可能改变了激励结构 |
| **证据状态** | `contested` — 广泛引用但也受到方法论和经验上的质疑 |
| **允许结论层级** | `introductory_explanation`（在承认争议的前提下使用） |

---

### C7：南方电网是"区域行动集权 + 中央决策集权"组合的成功案例，展示了当代中国已发展出超越"放-乱-收-死"循环的制度工具

| 项目 | 内容 |
|------|------|
| **位置** | `case_studies/southern_power_grid.md`；`90_QA.md` Q4 |
| **类型** | `phenomenon` + `mechanism` |
| **证据基础** | 南方电网成立于2002年12月29日，覆盖广东、广西、云南、贵州、海南五省区。制度特征：(a) 五省区电网运营权统一打包——区域行动集权；(b) 中组部任命领导班子、国资委持股51%、发改委监管电价——中央决策集权；(c) 广东省属资本持股25.57%——地方利益制度化嵌入；(d) 总部设在广州——非北京央企。运营20+年，西电东送规模超3500万千瓦，未出现类似唐朝藩镇失控或宋朝能力瘫痪的极端情况 |
| **可能的反驳** | (a) 南网与国网不在同一地理市场竞争，双头竞争的信息揭示功能可能被高估；(b) 可推广性存疑——依赖广东经济实力；(c) 广东股权的实质治理参与度可能被夸大；(d) 目前良好运行可能依赖特定政治环境，制度持续性未经重大冲击检验 |
| **证据状态** | `source_checked` — 基本事实（成立时间、股权结构、覆盖区域、运营数据）有公开发布来源支持；关于改革逻辑和中央隐性期待的分析属于 `interpretation`，见案例文档 NEEDS_VERIFICATION 清单 |
| **允许结论层级** | `introductory_explanation`（制度描述和经验事实分析）；上升到 `provisional_gap` 需要更多有关广东股权实质影响和制度持续性的证据 |

---

### C8：南网面临的深层矛盾体现了"区域行动集权"模式在能源转型和市场化改革背景下的制度张力

| 项目 | 内容 |
|------|------|
| **位置** | `case_studies/southern_power_grid.md` §7-8 |
| **类型** | `phenomenon` + `mechanism` |
| **证据基础** | 南网当前面临七个问题领域（新能源消纳、省间壁垒、输配电价改革、电网投资压力、混合股权张力、与国网竞合、国际扩张风险），这些问题可分为三个层次：(a) 技术-经济层（行业普遍性）；(b) 省际利益分配层（南网制度设计的核心考验）；(c) 央企治理层（混合股权的实质影响）。部分问题有可查证的行业报告和学术文献支持（如水电出力下降见 IEA 2023、省间壁垒见 The Economist 2023），部分基于制度推理（`interpretation`） |
| **可能的反驳** | (a) 这些问题并非南网独有——国网也面临新能源消纳、投资回报等问题，不宜过度归因于南网的制度特殊性；(b) 南网运行20+年整体稳定，当前问题的严重性可能被夸大；(c) 缺乏南网内部治理运作（董事会表决、省际电价协商机制）的一手证据，关于"张力"的许多判断属于推测 |
| **证据状态** | `source_checked` — 七个问题领域的存在性和各方立场的多样性有行业报告、政策文件和学术文献支持。但关于这些问题的严重程度、内部博弈的具体方式以及广东股权实质影响的判断，大部分属于 `interpretation` |
| **允许结论层级** | `introductory_explanation`；部分可上升为 `provisional_gap`（如"南网混合股权对央企治理的实际影响"可作为研究缺口） |

---

## 门控总结

| 论断 | 类型 | 证据状态 | 允许的结论层级 |
|------|------|---------|--------------|
| C1 话语混淆 | concept_definition | working_definition | introductory_explanation |
| C2 核心张力 | mechanism | working_definition | provisional_gap |
| C3 信息技术 | mechanism | unresolved | introductory_explanation |
| C4 任务型组织 | mechanism + novelty | working_definition | provisional_gap |
| C5 控制论映射 | platform_bridge | working_definition | introductory_explanation |
| C6 晋升锦标赛 | mechanism | contested | introductory_explanation |
| C7 南方电网 | phenomenon + mechanism | source_checked | introductory_explanation |
| C8 南网制度张力 | phenomenon + mechanism | source_checked | introductory_explanation |

**总体判断**：本包的核心概念创新（C1、C2）处于 `working_definition` 状态，足以支持入门级解释和 provisional gap 识别，但尚未达到可以作为学术研究项目核心依赖的标准。C7（南方电网案例）为本包的二维框架提供了一个 `source_checked` 级别的当代制度验证——这是本包目前证据状态最强的一个经验 anchor。C8 在此基础上进一步揭示了"区域行动集权"模式在能源转型背景下的制度张力，可作为未来研究缺口的出发点。建议后续步骤：（a）将 C1 与已有学术术语对齐；（b）为 C2 增加更多比较历史案例检验；（c）基于 C7 的案例研究方法，收集更多当代中国"区域行动集权"的制度案例（如京津冀协同发展领导小组、长三角一体化办公室等），检验该模式的普遍性。
