<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-19 04:59:36
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-19 04:59:37
 * @FilePath     : /project/knowledge/philosophy/power_reductionism/99_update_log.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-19
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-19
 * @FilePath     : /project/knowledge/philosophy/power_reductionism/99_update_log.md
 * @Description  : 更新日志——权力还原论 field pack 的创建与修改记录
-->
# 99 Update Log / 更新日志

Last updated: 2026-07-19

---

## 2026-07-19 — 交叉引用更新

- 新增姊妹包：`reductionism/subfields/power_reductionism_as_case/`（还原论哲学根源分析）
- 分工约定：本包负责具体实例与历史叙事；姊妹包负责在方法论和认识论上的还原论根源诊断
- 两包互补：读者先读本包了解"是什么"，再读姊妹包理解"为什么这是一种还原论"

---

## 2026-06-19 — Round 1: 初始创建（quick_scan 级别）

### 触发
用户在观看 YouTube 中国政治视频后，发现一种普遍的解释模式——将所有政治事件归结为政治人物对"权力"的个人私欲。用户认为这种解释不符合历史唯物主义，但好奇其在历史学中的渊源和流行原因。

### 路由决策

```yaml
initial_mode: orientation
actual_mode: quick_scan
selected_profile: general_interest_profile
domain_archetype: humanities_cultural
confidence: high
reason: 用户为一般智识兴趣，不需要结合个人背景或找研究课题
```

### 本轮创建文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `USER_BRIEF.md` | ✅ 新增 | 本次用户需求记录、路由决策和输出计划 |
| `00_beginner_guide.md` | ✅ 新增 | 入门指南：先讲直觉再讲术语，从 YouTube 场景出发解释权力还原论 |
| `01_research_overview.md` | ✅ 新增 | 领域总述：概念定义、七条思想谱系、流行机制分析、三重批判 |
| `02_frontier_compass.md` | ✅ 新增 | 边界罗盘：内圈共识 5 项、中圈争论 4 项、边界开放问题 4 项、伪 gap 3 项 |
| `11_term_disambiguation.md` | ✅ 新增 | 术语辨析：权力/历史观/还原论/历史唯物主义/犬儒主义/宫廷政治 + 概念边界契约 |
| `12_field_map.md` | ✅ 新增 | 思想谱系图：七条脉络（古典现实主义→伟人史观→精英理论→心理史学→克里姆林学→宫廷政治→媒介生态）+ 谱系总图 + 关系矩阵 |
| `13_actor_map.md` | ✅ 新增 | 关键思想家登记：A 组 9 人（谱系源头）+ B 组 5 人（批判者）+ C 组（当代相关）+ 思想关系图 |
| `15_primary_materials_and_reading_path.md` | ✅ 新增 | 阅读路径：路径 A（史学理论）、路径 B（权力分析谱系）、路径 C（历史唯物主义）、路径 D（媒介批判）+ 自检清单 |
| `17_claims_evidence_ledger.md` | ✅ 新增 | 论断-证据台账：10 条核心 claims 按 Fact/Interpretation/Speculation/Recommendation 分级 |
| `99_update_log.md` | ✅ 新增 | 本文件 |

### 未生成文件
- `10_self_inventory.md`（用户未要求结合个人背景）
- `14_paper_registry.md`（学术文献注册——本主题以经典著作为主，已在 `15_reading_path.md` 和 `13_actor_map.md` 中覆盖）
- `16_key_questions_and_cases.md`（学术汇报用的问题与案例——用户为一般智识兴趣而非学术汇报）
- `20_gap_table.md`、`21_asset_match.md`、`22_project_candidates.md`、`23_mvp_experiment_plan.md`（用户不需要研究切入点）
- `90_QA.md`（尚无自由问答记录）
- `subfields/`（无子方向派生需求）

### 本轮 NEEDS_VERIFICATION 汇总

| 项目 | 位置 |
|------|------|
| YouTube 中国政治内容中权力还原论的精确占比（未做系统性内容分析） | `01`, `17`（Claim 1） |
| YouTube 推荐算法对政治内容的精确偏好参数（商业机密） | `01`, `02`, `12`, `17`（Claim 6） |
| 心理史学在当代的具体接受状态（未检索最新综述） | `01`, `12` |
| 斯洛特戴克理论在当代中国受众中的适用性 | `17`（Claim 8） |
| 《厚黑学》与当代犬儒主义的具体传承关系 | `12` |
| 克里姆林学在后冷战中国研究中的具体延续 | `12` |
| 当代媒介研究的代表学者和精确文献（C 组） | `13` |
| 全部推荐著作的中译本最新出版信息 | `15` |
| 媒介素养教育的实际效果研究 | `02` |
| 犬儒主义→政治冷漠的因果效应经验研究 | `02` |

### 用户下一步建议

1. 如果只是好奇 → 本 field pack 已足够回答初始问题。推荐先读 `00_beginner_guide.md`（5 分钟快速进入），然后根据兴趣选择 `15_reading_path.md` 中的阅读路径。
2. 如果想深入讨论 → 可在 `90_QA.md` 中记录后续问答。
3. 如果想从某个 gap 派生研究方向 → 可走 `subfield` 流程在父包下创建子方向（如"算法与政治叙事的经验研究""当代中国犬儒主义的政治后果"）。
4. 如果想将此转化为学术写作 → 需要升级为 `full_onboarding` 或 `project_incubation` 模式，补全 `14_paper_registry.md`、`20_gap_table.md`、`22_project_candidates.md` 等文件。

### 格式与风格说明

- 本 field pack 的中文写作遵循 `WRITING_STYLE.md` 的"先讲直觉，再讲术语"原则；
- 分类采用谱系和坐标轴思维，避免百科全书式清单；
- 所有 `NEEDS_VERIFICATION` 标记均在正文和每文件末尾汇总中明确标注；
- 不编造论文、作者、年份或研究结果——经典著作部分基于通识可验证，当代研究部分给出检索方向而非具体条目；
- 不将 suspected gap 写成 confirmed gap，不将 interpretation 写成 fact。
