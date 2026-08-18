<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-17 20:15:49
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-17 20:15:49
 * @FilePath     : /.agents/home/wyl/project/knowledge/sociology/social_survey_methods/17_claims_evidence_ledger.md
 * @Description  :
-->
<!--
Field: 社会调研方法论——从日常对话到结构化判断
Mode: quick_scan
Domain archetype: social_science
Created date: 2026-08-17
-->

# 17 Claims & Evidence Ledger / 论断-证据台账

Last updated: 2026-08-17

## 0. 说明

本文记录种子讨论文档（`seed_discussion_20260817.md`）及本包核心文档中的关键论断及其证据状态。每条论断标注类型、置信度和重要性。

**论断类型**：
- `fact`：已有充分经验证据支持的陈述
- `interpretation`：对事实的理论解释（同一事实可能有多种解释）
- `speculation`：具备部分理论基础但缺乏充分证据的推测
- `recommendation`：基于理论和证据的行动建议

**置信度**：
- `high`：大量跨方法、跨情境的证据一致支持
- `medium`：证据存在但不完全一致，或仅限于特定语境
- `low`：证据薄弱或主要基于个案
- `NEEDS_VERIFICATION`：尚未核实

**重要性**：
- `foundational`：构成本包方法论的基石
- `important`：影响操作选择
- `supporting`：补充性知识

---

## 1. 核心论断清单

### 1.1 方法论定位

| ID | 论断 | 类型 | 置信度 | 重要性 | 关键证据 | 主要挑战 |
|---|---|---|---|---|---|---|
| C-01 | 社会调研问题既是社会学课题，也是工程学问题；"社会学提供语法，工程学提供工艺" | interpretation | high | foundational | 质性研究方法论与调查方法论两大传统并行存在（见 `13_actor_map.md` 谱系观察） | 该比喻是组织工具而非理论命题，不可过度延伸 |
| C-02 | 单条聊天信息不可靠，但经过分层、编码与三角验证后的聚合模式可逼近真实状况 | interpretation | medium | foundational | 三角验证（Denzin）、编码分析传统的方法论共识 | "聚合有效性"假设本身缺少严格检验；逼近程度没有公认度量 |
| C-03 | 日常对话可以作为正式研究数据 | fact | high | foundational | 常人方法学与会话分析传统（Garfinkel 1967；Sacks 的会话分析） | 作为"数据"的对话需要系统记录与编码，而非随意引用 |

### 1.2 理论透镜

| ID | 论断 | 类型 | 置信度 | 重要性 | 关键证据 | 主要挑战 |
|---|---|---|---|---|---|---|
| C-04 | 人们依据事物对自己的意义行动，意义在互动中产生 | fact | high | foundational | 符号互动论核心命题（Blumer 1969） | 意义的经验测量困难；追问"你指什么"是操作化解法 |
| C-05 | "没有一句话是废话"——琐碎日常内容可能揭示深层结构 | interpretation | medium | important | 常人方法学对索引性表达的研究 | 过度解读风险：并非每句闲聊都有结构意义 |
| C-06 | 不同阶层对同一问题的感受差异本身构成真实图景 | interpretation | medium | important | 分层研究的阶层差异传统（Blau & Duncan 1967 等） | 需要先证明"分层变量"在本地场景有区分度 |
| C-07 | 频繁出现"各扫门前雪""没人出头"可能意味着社会资本薄弱、基层治理失效 | speculation | low-medium | supporting | 社会资本-治理文献（Putnam 1993）支持"信任/合作→治理"的关联 | 单一话语模式不足以判定；可能只是普遍抱怨风格 |

### 1.3 工程方法

| ID | 论断 | 类型 | 置信度 | 重要性 | 关键证据 | 主要挑战 |
|---|---|---|---|---|---|---|
| C-08 | 愿意聊天的人具有特定特征（空闲、爱抱怨、有立场），导致样本系统性偏离总体 | fact | medium-high | foundational | 调查方法论的样本选择偏差共识 | 偏差的具体方向与强度因场景而异，需在本地验证 |
| C-09 | 信号强度加权（亲身经历 3 / 近距离观察 2 / 泛泛而谈 1 / 二手传闻 0.5）能有效降噪 | recommendation | low | supporting | 无直接文献依据；与证据层级思想一致 | 权重数值未经校准；`unresolved`，详见 `11_term_disambiguation.md` |
| C-10 | 三值编码（事实/评价/传闻）能强制区分信息类型，降低误读 | recommendation | medium | important | 内容分析与编码传统支持分类编码的降噪作用 | 判定规则未细化时信度差；三值只是初筛 |
| C-11 | 双人独立编码一致性低于 70% 需重新定义标准 | recommendation | NEEDS_VERIFICATION | supporting | 编码信度文献存在一致性阈值讨论（Krippendorff） | 70% 阈值的具体出处未核实 |
| C-12 | "以前好"是记忆重构，可能失真；连续三个月的"越来越差"才算趋势 | interpretation + recommendation | medium | important | 记忆偏差的社会心理学研究 | "三个月"阈值是启发式，无严格依据 |
| C-13 | 敏感话题导致自我审查、回避、含糊其辞，造成系统性数据缺失 | fact | high | important | 研究伦理与政治敏感话题研究的方法论共识 | 缺失的规模与结构难以估计 |

## 2. 中心论断（支撑下游判断）

- **C-02（聚合有效性）** 是本包所有 gap 与 project 的总前提。若该论断不成立，则"聊天式调研"整体价值存疑。
- **C-08（采样偏差）** 与 **C-13（自我审查缺失）** 决定本包产出的可信度上限。
- **C-09（信号强度加权）** 状态为 `unresolved` → 所有依赖它的项目必须标 `provisional`，首先验证权重校准而非直接使用。

## 3. 修正记录

| 日期 | 论断 | 修正 | 原因 |
|---|---|---|---|
| 2026-08-17 | C-09 | 从"方法论"降级为 `recommendation` 且置信度 `low` | 无文献依据，属种子文档自创启发式 |
