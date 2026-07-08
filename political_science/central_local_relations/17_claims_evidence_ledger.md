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

## 门控总结

| 论断 | 类型 | 证据状态 | 允许的结论层级 |
|------|------|---------|--------------|
| C1 话语混淆 | concept_definition | working_definition | introductory_explanation |
| C2 核心张力 | mechanism | working_definition | provisional_gap |
| C3 信息技术 | mechanism | unresolved | introductory_explanation |
| C4 任务型组织 | mechanism + novelty | working_definition | provisional_gap |
| C5 控制论映射 | platform_bridge | working_definition | introductory_explanation |
| C6 晋升锦标赛 | mechanism | contested | introductory_explanation |

**总体判断**：本包的核心概念创新（C1、C2）处于 `working_definition` 状态，足以支持入门级解释和 provisional gap 识别，但尚未达到可以作为学术研究项目核心依赖的标准。建议后续步骤：（a）将 C1 与已有学术术语对齐；（b）为 C2 增加更多比较历史案例检验。
