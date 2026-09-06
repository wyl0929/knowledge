<!--
 * @Author       : 
 * @Date         : 
 * @LastEditors  : 
 * @LastEditTime : 
 * @FilePath     : /knowledge/systems_science/13_methodology_anchors.md
 * @Description  : 案例方法论锚点 — case/ 模板的理论支撑层；每条理论 = 一句话 + 核心机制 + 管的节 + 自查清单 + 文献 + SKILL 指针
-->

# 13 Methodology Anchors / 案例方法论锚点

> **用途**：这是 `case/_TEMPLATE_case_study.md` 的理论支撑层。写案例时，模板每节会指向本文件某条理论；跑该理论的**自查清单**，打勾不过的返回补。
> **状态标注**：✅ 原始文献已下载、已精读、清单已提炼；📄 原始文献已定位、待下载精读（清单暂缺）。

## 0. 映射总表：理论 → 体裁/节

| 理论 | 管 `case/` 的哪一节 | 回答的问题 |
|---|---|---|
| STAMP (§1) | 回溯型 §3 系统建模、§5 根因+层级归因 | "事件是哪个控制结构实例？缺陷在哪一类/哪一层？" |
| AcciMap (§2) | 回溯型 §3 系统建模、§5 层级归因 | "多层决策者各自的本地目标如何叠加成事故？" |
| 瑞士奶酪 (§3) | 回溯型 §3、§5 | "多层防线为何同时失守？" |
| Yin 案例研究法 (§4) | 回溯型 §1、§4、§8 | "个案凭什么推广？竞争解释排净了吗？证据链断没断？" |
| Eisenhardt 跨案例 (§5) | 回溯型 §7 与其他案例的连接 | "通则是否被复制/扩展？" |
| SRE 无责复盘 (§6) | 回溯型 §2 时间线、§6 教训 | "事实与解释分开了吗？根因够深吗？" |
| Kolb / Schön (§7/§8) | 回溯型 §6 教训 | "教训是触发式规则，还是空泛道德？" |
| Alexander 模式语言 (§9) | 卡片 §1、§8 | "卡片名能当检索词吗？进关系网了吗？" |
| GoF 设计模式 (§10) | 卡片整体骨架 | "Intent/Applicability/Consequences 齐了吗？" |
| GRADE (§11) | 卡片 §5 禁忌、§6 证据等级 | "禁忌写了吗？信心等级标了吗？" |
| Gawande 清单 (§12) | 卡片 §7 速查表 | "致命项提炼出来了吗？" |
| pre-mortem (§13) | 评审 §3/§4 | "风险按严重度分级了吗？" |
| Argyris 双环学习 (§14) | 双向指针 | "回溯有没有编译出卡片？" |

---

## 1. STAMP — 系统论事故模型（Leveson）✅

- **一句话**：用控制论做事故分析——事故不是"事件链"，而是"控制结构未能施加安全约束"。
- **核心机制**（提炼自 Leveson 2004 §3）：
  1. 基本单位是**约束（constraint）**，不是事件。安全是涌现性质，由约束强制；事故 = 约束被违反 + 控制结构未能阻止。
  2. 控制的四个必要条件（Leveson §3.2 引 Ashby 1956）：① 控制器有目标 ② 能影响系统状态 ③ 含系统模型 ④ 能感知系统状态。
  3. **控制缺陷分类**（§3.4, Fig.5，这是自查的核心）：
     - **1 约束未被充分强制**：1.1 危险/约束未被识别；1.2 控制动作不充分 → 1.2.1 控制算法缺陷、1.2.2 **过程模型与实际状态不一致**、1.2.3 多控制器协调失效（边界区/重叠区）。
     - **2 控制动作执行不足**（执行器/参考通道失效）。
     - **3 反馈缺失或不充分**（设计未含 / 通道缺陷 / 不及时 / 测量仪器失效）。
  4. 最常被强调的根因：**过程模型（控制器以为的状态）与实际状态发散**（§3.4.1.2）——对应语料里的"心智模型错配"与"执行器假成功"（#10）。
- **管的节**：回溯型 §3 系统建模、§5 根因+层级归因。
- **自查清单**：
  - □ 画了控制结构图（控制器 / 控制动作 / 反馈 / 被控过程）吗？
  - □ 根因归到 STAMP 缺陷分类（约束未强制 / 执行不足 / 反馈缺失）了吗？
  - □ 若"约束未强制"，进一步定位到 算法缺陷 / 过程模型不一致 / 协调失效 三者之一了吗？
  - □ 检查了"过程模型 vs 实际状态"是否发散吗（控制器以为的状态 ≠ 真实状态）？
  - □ 检查了反馈是否"报告已执行、实际未执行"（假成功）吗？
- **原始文献**：Leveson, N. (2004). A new accident model for engineering safer systems. *Safety Science*, 42(4), 237–270. doi:10.1016/S0925-7535(03)00047-X — `references/Leveson - 2004 - ...pdf`
- **已编译为 SKILL**：`debug-workflow`（战术诊断五阶段；根因假设与判别实验）。

## 2. AcciMap — 多层社会-技术控制（Rasmussen）✅

- **一句话**：用多层控制结构图（AcciMap）建模事故——事故是"各层决策者忙于各自本地目标时的副作用叠加"。
- **核心机制**（提炼自 Rasmussen 1997 §5/§6/§8）：
  1. 控制层次：政府政策 → 监管机构 → 本地政府/公司管理层 → 一线作业 → 设备/环境；每层对下层施加约束。
  2. **向边界迁移（migration toward the boundary）**：在成本/效率压力下，行为系统性漂向"可接受性能边界"，穿越即事故（§6, Fig.3）。
  3. 事故**不是独立失效的巧合**，而是竞争环境下组织行为系统性迁移的结果（§5）。
  4. 分析第一步是**识别控制者**（§8.1），画出决策者关系图（AcciMap）。
  5. "纵深防御"下，单一防线被违反无立即可见效果 → 被违反而不被察觉（§6 末）。
- **管的节**：回溯型 §3 系统建模、§5 层级归因。
- **自查清单**：
  - □ 画了多层控制结构（至少"策略层 / 管理层 / 执行层 / 设备层"）吗？
  - □ 标出了各层决策者各自的本地目标与压力（成本/工期）吗？
  - □ 检查了是否存在"向边界的系统性迁移"（为省成本逐步逼近安全极限）吗？
  - □ 是否写成了"多层各自优化、副作用叠加"，而非"单一责任人失误"？
- **原始文献**：Rasmussen, J. (1997). Risk management in a dynamic society: a modelling problem. *Safety Science*, 27(2–3), 183–213. doi:10.1016/S0925-7535(97)00052-0 — `references/Rasmussen - 1997 - ...pdf`
- **已编译为 SKILL**：无。语料 #03「层级归因」、#04「天水血铅」已用此框架。

## 3. 瑞士奶酪模型 — 多层防线失效（Reason）📄

- **一句话**：事故发生在多层防线各自的"洞"恰好对齐时；洞 = 隐性条件（latent）与主动失效（active）叠加。
- **管的节**：回溯型 §3 系统建模、§5 层级归因。
- **原始文献**：Reason, J. (1990). *Human Error*. Cambridge University Press；标准短文 Reason, J. (2000). Human error: models and management. *BMJ*, 320(7237), 768–770. doi:10.1136/bmj.320.7237.768
- **状态**：待下载精读后补"核心机制 + 自查清单"。

## 4. 案例研究法（Yin）📄

- **一句话**：单案例靠"分析性推广 + 竞争解释排除 + 证据链"实现可推广性，而非统计抽样。
- **管的节**：回溯型 §1 背景（分析单元）、§4 假设空间（竞争解释）、§8 证据附录（证据链）。
- **原始文献**：Yin, R. K. (2018). *Case Study Research and Applications: Design and Methods* (6th ed.). Sage.
- **状态**：待下载精读后补"核心机制 + 自查清单"。

## 5. 跨案例建理论（Eisenhardt）✅

- **一句话**：从多个案例归纳理论的标准流程——"复制逻辑（replication）+ 跨案例模式搜索"，而非统计抽样。
- **核心机制**（提炼自 Eisenhardt 1989 Table 1 八步）：
  1. 起步：定义研究问题；可用先验构念，但**不预设理论/假设**。
  2. 选案例：指定总体，**理论抽样**（非随机）——选能"复制或扩展理论"的案例。
  3. 造工具：多数据源三角验证。
  4. 进场：数据收集与分析重叠、方法灵活。
  5. 分析数据：**within-case（单案内）→ cross-case（跨案模式搜索）**。
  6. 塑形假设：迭代制表 + **复制逻辑** + 追问关系背后的"为什么"。
  7. 折入文献：与**冲突**文献对比（内部效度）+ 与相似文献对比（普遍性）。
  8. 收尾：理论饱和时停止。
- **管的节**：回溯型 §7 与其他案例的连接（跨案例分析是理论真正形成处）。
- **自查清单**：
  - □ 这个案例的通则，是否在 ≥1 个其他案例里被"复制"（同向证据）或"扩展"（新情境）？
  - □ 是否先做了 within-case（把本案例内部逻辑理清）再跨案比较？
  - □ 是否追问了关系背后的"为什么"（机制），而不只是"A 伴随 B"？
  - □ 是否把结论与**冲突**的既有结论对照过（而非只找支持自己的）？
- **原始文献**：Eisenhardt, K. M. (1989). Building theories from case study research. *Academy of Management Review*, 14(4), 532–550. doi:10.2307/258557 — `references/Eisenhardt - 1989 - ...pdf`
- **已编译为 SKILL**：无。案例间"复制/扩展"关系建议在 `case/README.md` 注册表显式标注。

## 6. 无责复盘（SRE blameless postmortem）✅

- **一句话**：事故后的书面记录——影响 + 时间线 + 缓解 + 根因 + 跟进行动；纪律是"无责"。
- **核心机制**（提炼自 Lunney & Lueder 2016 第 15 章）：
  1. postmortem 定义：incident 的书面记录，含 **impact / mitigation / root cause(s) / follow-up actions（防复发）**。
  2. **无责（blameless）**：只找贡献性原因，不追责个人；假设"每个人在当下信息下做了正确的事"。"不能修人，只能修系统和流程。"
  3. **触发条件在事故前定义**：用户可见宕机 / 数据丢失 / 超阈值恢复时间 / 监控失效。
  4. **评审五问**：① 关键数据收了吗 ② 影响评估完整吗 ③ 根因够深吗 ④ 行动计划合适、优先级对吗 ⑤ 分享给相关人了吗。
  5. "未评审的 postmortem 等于不存在。"
- **管的节**：回溯型 §2 时间线（事实/解释分节）、§6 教训（跟进行动）。
- **自查清单**：
  - □ 时间线只写事实、不掺"某人做错了"的归因吗？
  - □ 根因是否"足够深"（不停在"人失误"，追到"为什么信息不完整"）？
  - □ 行动计划是否可执行、有优先级（而非"下次注意"）？
  - □ 结论是否分享给了会从教训中受益的人？
- **原始文献**：Lunney, J., & Lueder, S. (2016). Postmortem Culture: Learning from Failure. In *Site Reliability Engineering*. O'Reilly. — `references/postmortem-culture.html`
- **已编译为 SKILL**：无。语料 #01「诊断检查清单」、#07「关闭报告」是同类实践。

## 7. 经验学习环（Kolb）📄

- **一句话**：具体经历 → 反思观察 → 抽象概念化 → 主动实验的闭环；"教训"段是"抽象概念化"那一步。
- **管的节**：回溯型 §6 教训。
- **原始文献**：Kolb, D. A. (1984). *Experiential Learning*. Prentice-Hall.
- **状态**：待下载精读后补。

## 8. 反思实践（Schön）📄

- **一句话**：专业者在行动中反思（reflection-in-action）；"复盘"即把默会知识显性化。
- **管的节**：回溯型 §6 教训。
- **原始文献**：Schön, D. A. (1983). *The Reflective Practitioner*. Basic Books.
- **状态**：待下载精读后补。

## 9. 模式语言（Alexander）📄

- **一句话**：模式 = "规则 + 起作用的语境 + 与其他模式的关系"；模式是语言不是列表。
- **管的节**：卡片 §1 名称/意图、§8 与其他卡片的连接。
- **原始文献**：Alexander, C., Ishikawa, S., & Silverstein, M. (1977). *A Pattern Language*. Oxford University Press.
- **状态**：待下载精读后补。

## 10. 设计模式（GoF）📄

- **一句话**：Intent / Motivation / Applicability / Structure / Consequences / Related Patterns 的固定骨架。
- **管的节**：卡片整体骨架。
- **原始文献**：Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns*. Addison-Wesley.
- **状态**：待下载精读后补。

## 11. GRADE — 证据质量与推荐强度（Guyatt）📄

- **一句话**：每条建议同时标注"推荐强度 × 证据质量"；卡片 §6 的"信心等级"即此。
- **管的节**：卡片 §5 禁忌（contraindications）、§6 证据等级。
- **原始文献**：Guyatt, G. H., et al. (2008). GRADE: an emerging consensus on rating quality of evidence and strength of recommendations. *BMJ*, 336(7650), 924–926. doi:10.1136/bmj.39489.470347.AD
- **状态**：待下载精读后补。

## 12. 清单革命（Gawande）📄

- **一句话**：清单价值不在全，在"致命项（killer items）"——那几个漏掉就翻车的点。
- **管的节**：卡片 §7 速查表。
- **原始文献**：Gawande, A. (2009). *The Checklist Manifesto*. Metropolitan Books.
- **状态**：待下载精读后补。

## 13. Pre-mortem（Klein）📄

- **一句话**：项目开始前先想象"它已经失败了，为什么"，暴露盲区。
- **管的节**：评审 §3 风险/问题、§4 改进建议。
- **原始文献**：Klein, G. (2007). Performing a project premortem. *Harvard Business Review*, 85(9), 18–19.
- **状态**：待下载精读后补。

## 14. 双环学习（Argyris & Schön）📄

- **一句话**：单环=在既定规则内纠偏；双环=修订治理规则本身。捕捉→编译就是双环。
- **管的节**：双向指针（`→ 已编译为卡片 / ← 来源案例`）。
- **原始文献**：Argyris, C., & Schön, D. A. (1978). *Organizational Learning*. Addison-Wesley；Argyris, C. (1977). Double loop learning in organizations. *Harvard Business Review*, 55(5), 115–125.
- **状态**：待下载精读后补（语料 #107 已引）。

---

## 参考文献

已下载（含文件路径与 `.bib` 条目）：

- Leveson 2004 — `references/System_Sciences.bib` (`leveson_new_2004`) — `references/…pdf`
- Rasmussen 1997 — `references/System_Sciences.bib` (`rasmussen_risk_1997`) — `references/…pdf`
- Eisenhardt 1989 — `references/System_Sciences.bib` (`eisenhardt_building_1989`) — `references/…pdf`
- SRE Postmortem 2016 — `references/System_Sciences.bib` (`noauthor_google_nodate`) — `references/…html`

待下载（文献已定位，见各节原始文献字段）：Reason 1990/2000、Yin 2018、Kolb 1984、Schön 1983、Alexander 1977、GoF 1994、Guyatt 2008、Gawande 2009、Klein 2007、Argyris & Schön 1978。
