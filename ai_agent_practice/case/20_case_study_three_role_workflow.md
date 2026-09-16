<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-09-15
 * @FilePath     : /home/wyl/project/knowledge/ai_agent_practice/case/20_case_study_three_role_workflow.md
 * @Description  : 案例研究 — 三角色工作架构（人类 principal / planning / execution）：R02 重启复盘的推导、角色建模、结构模型与成本账
-->

# 案例研究: 三角色工作架构 — 人类 principal / planning / execution 的推导、建模与成本账

> **案例 ID**: `#110`
> **类型**: 设计 + 回溯（基于 R02 重启复盘与 case 19 试点报告的推导；**流程级方案尚未试点**）
> **状态**: 🧪 **提案**（待 R03 试点验证；执行手册与退出标准见 `TBG/docs/three_role_workflow.md`）
> **领域标签**: AI agent toolcraft · 委托-代理 · 会话角色分工 · 上下文加载 · 成本建模
> **时间跨度**: 2026-09-06 ~ 09-15（R02 重启执行期）+ 09-15 推导成文
> **相关项目**: `/home/wyl/project/TBG/`
> **原始数据**: `/home/wyl/project/knowledge/ai_agent_practice/references/R02_archive/*.jsonl`（25 会话 / 202 轮 / 300 条人类消息）
> **关联案例**:
>   - `19_case_study_cross_conversation_task_handoff.md`（#109）— 交接层模型与 R02 试点报告（本案例是其**上游框架**，由 §5.3 的 P2/P3/P5/P6 导出）
>   - `14_case_study_session_workflow_state_persistence.md`（#104）— 会话工作流与状态持久化（三角色是其在多会话执行链上的角色化）
>   - `../systems_science/case/06_case_study_diagnostic_knowledge_promotion.md`（#96）— 事实/推论/建议三层增益控制（本案例「确认状态」标注的直接依据）
>   - `TBG/docs/phase_R02_mtb_domain_wall/REVIEW.md` — 委托-代理三问题 + 输出契约（人类 principal 角色的理论依据）
>   - `TBG/docs/phase_R02_mtb_domain_wall/RETROSPECTIVE.md` §8 — 本案例 §6 成本账的量化证据

---

## 摘要

TBG Phase R02 重启（T1–T19）的全程复盘暴露一个模式：**执行会话在做 planning 的活**。plan 修订混在执行会话里下指令（人类在 T9/T13 会话下「按这个方案修改 plan 和 task」），执行会话为重建规划状态付 ~98k plan+log 重读（T17 读 log ×7 = 29.9k）；契约依赖图残缺（T14 实际依赖 5 个生产者、tasks 只写 2 项），执行者被迫自行重建依赖。而「该更新时没更新」（§0.2 漏 Goal 4、分工铁律事后才补）的根因是没有 executor→planner 的正式反馈通道。

本案例把会话按角色分成三个：**人类 principal**（定目标/判据/门禁、审图回填收敛、纠错）、**planning**（少而重，维持项目结构模型，在离散修订点更新，组装 Handoff_{消费者}）、**execution**（多而轻，只读契约 + 组装视图，产出证据 + 晋升一句话结论 + 上报偏差）。原则一句话：**把「宽读」路由到少数 planning 会话，多数 execution 会话保持窄读**；类比上 SSOT（KNOWN/plan）是「库」，task 是「main()」——库可以无限膨胀，只要 main() 的接口（输入/输出/依赖清单）稳定。

成本账（R02 Stage 3 实测口径）：「获取信息」token 从现状 ~1250k 降到理想 ~185–295k，净收益 3–7 倍；且 planning 投入 ≈ 现状已付的规划型开销，是**重新分配**而非新增成本。**本方案尚未按流程试点**——R03 是第一个试点 Phase，验收口径与退出标准见执行手册。

---

## 1. 推导：R02 重启的三个直接证据

1. **executor 做 planning 的反模式**（case 19 §5.3 P2）：人类在 T9/T13 **执行会话**里下「按这个方案修改 plan 和 task」的指令，执行会话为重建规划状态付 plan+log 重读 ≈98k（T17 读 log ×7 = 29.9k 即实例）。plan 修订散落在执行会话里，既贵（执行者没有规划上下文）又不可追踪。
2. **依赖图是 DAG 且残缺**（P3/P5）：T14 实际依赖 5 个生产者（T13 峰位 + T12 参数 + T17 E_F + T18 d + T15 ξ，含编号更大的交叉边），tasks「输入」只写 2 项；编号、执行序、依赖序三者不一致。契约残缺时执行者被迫自行重建依赖——这正是「执行会话读他任务 REPORT ~27 次」和「T17 读 log ×7」的同一根因。
3. **「该更新时没更新」**（P8 的另一半）：§0.2 漏写 Goal 4、分工铁律 09-08 才补、plan §3 初版重犯 REVIEW 批评过的错——都是**人类点破后**才修订。根因是没有把「plan 级修订」显式指派给一个角色，也没有 executor 上报偏差的正式通道。

三者指向同一个结构性问题：**会话没有被角色化**——同一个对话既执行又规划、既宽读又窄读，宽读的税摊在每个执行会话头上。解法不是让执行会话读得更聪明（case 19 试点已证明 grep 纪律不可靠），而是**把两种读分到两种会话**。

## 2. 模型：三角色定义

| 角色 | 职责 | 掌握的内容 | 对话特征 |
|---|---|---|---|
| **人类 principal** | 定目标/判据/Stage 门禁；审图回填「收敛/主导/惰性」；纠 planning 错误 | 物理意图（不可推导） | 少；出现在门禁处 |
| **planning** | 维持结构模型；在离散修订点更新；创建/修订 task（依赖图）；组装 Handoff_{消费者}；处理 executor 上报的 plan 级偏差 | 结构模型五要素（§3）+ 跨 phase 知识指针 | **少而重**；离散修订点 |
| **execution** | 执行单个 task；产出证据（REPORT+图+golden）；收尾热写 KNOWN 一句话结论；上报 plan 级偏差 | 契约（tasks 条目）+ Handoff_{消费者} + 任务专属资产 | **多而轻**；窄读 |

**三条铁律**（沿 REVIEW §3.2 / plan §3.2，并做两处延伸）：

1. execution 只出：叠加图 + 墙钟 + 客观级差数值；**收敛/主导/惰性判断永远交人类**（门禁处审图回填）。
2. 「事实晋升」executor 可热写（KNOWN 一句话条目）；「结构修订」（目标/Stage/依赖图/判据变更）**必须回 planning**。
3. **分工铁律延伸到 KNOWN 写入口**：executor 晋升的结论**默认标「AI 推论，待人类确认」**，状态翻转只在门禁处由人类做——AI 出线索、人类定事实（case 06 三层分类的事前标注；R02 教训：m=3 R6 阈值 / rs 惰性 / 0.599–0.926 = bulk VHS 都是推论被当事实写进去、再由人类纠一轮，错误各完整发生一轮）。

**产出物读者分工**：REPORT（判据→证据映射 + 图 + 残余风险）= 人类门禁验收 + planning 修订追溯；execution 的信息输入一律走 Handoff/KNOWN，**不读他任务 REPORT**（R02 的 executor 读 REPORT ~27 次是契约残缺的补偿行为）。

**为什么是人类三角色而不是 AI 两角色**：R02 全程显示人类在两处不可替代——科学决策与验收（钉 δ=60meV、审图回填收敛、抓出 E1/E2/E5/E6 四类错误）。窄 executor 的安全网靠「本地证据（判据→图→golden）+ 人类门禁」，**不靠把 executor 变宽**。

## 3. planning 的结构模型（有界）

planning 掌握的「全貌」= **结构模型五要素**，不是全部内容：

| 要素 | 载体 |
|---|---|
| 目标树 + Stage 门禁 | plan.md §0/§2 |
| 依赖图（DAG，含交叉边，标注执行序 ≠ 编号序） | tasks.md「输入」字段 |
| 结论有效性状态机（哪些已撤回/取代/悬置） | KNOWN 顶部 ⚠️ 标记 + STATUS |
| 资产索引（文件/脚本/数据 → 路径 + 一句话用途） | plan.md 交付物节 + CONTEXT |
| 跨 phase 知识指针（R01 WRAPUP / shared/ / knowledge/physics） | 本案例 §3 引用清单 |

**为什么有界**：结构模型的增长速度（任务数、DAG 边数、状态条目数）远慢于内容（R02 末：64 图 + 17 REPORT + 300MB 数据 + 四份长文档 45/44/61/72KB）。planning 按需拉取内容、不全量装上下文——R02 的 plan_task 会话 127k 读入是「planning 读内容」的警讯。

**跨 phase 指针是硬要求**：R02 的 PLL 案例——0.599/0.926 eV 峰归属从「bulk VHS」更正为「PLL（赝朗道能级）」，靠的是 R01 的 DRIP+rebo 结果 + Zheng PRL 2022 笔记，**全在 R02 phase 内文件之外**。若 planning 只把握本 phase 文件，窄 executor 会在「phase 内看似自洽」处静默出错。

## 4. 离散修订点（何时 planning 出场）

- **修订点 = Stage 门禁（人类验收）+ 发现驱动（证伪 / 范围变化 / 新 task 需求）**。
- 禁止：连续更新（贵且不必要）；执行会话内改 plan 结构。
- R02 的修订点盘点（6 个）：09-09 Stage 3 立项、09-10 T13 增补、09-11 建 T16、09-11 建 T17/T18+重排 S4/S5+拆 R03、09-12 重写 T15、09-14 建 T19。
- R02 教训：问题不是修订点太少，而是「**该更新时没更新**」——触发机制靠 §5 的偏差上报 + 门禁，不靠人类事后点破。

## 5. executor → planner 反馈通道（R02 缺失的一环）

| 上报物 | 谁写 | 载体 | 处理方 |
|---|---|---|---|
| 事实晋升（新结论/坑） | executor 收尾热写 | KNOWN 一句话条目 + § 锚 + 确认状态 | （无需处理，直接生效） |
| **plan 级偏差**（证伪 / 新发现 / 范围变化 / 依赖图残缺 / 判据不可达） | executor 发现即报 | STATUS「📋 待 Planning 会话处理」+ 门禁处交人类 | planning 会话（修订 plan/tasks） |

- 目标：plan 级修订不再等人类点破。
- **判据不可达不算失败，是上报物**（R02 实例：T17 的「E_F meV 级」判据因 `calc_Fermi_dos` 算法缺陷不可达——正确处置是修订判据/转遗留，由 planning + 人类决定，而不是执行会话硬撑或自行改判据）。

## 6. 成本模型（R02 Stage 3 实测口径）

测量口径 = case 19 §2.1（tool/result 文本、中文 1 token/字、ASCII 1/4 字符、四分类），对 25 个会话逐条测量，基线复算验证一致（T1_T2 35.1k 复现）。

| | 获取信息 token（传入+重发现） |
|---|---|
| **现状（as-is）** | ~1250k = 执行主会话+planning 729k + fork 分支重复 522k；另含执行内规划 98k |
| **理想（本架构）** | execution 10 任务 × 5–10k（契约 2–3k + Handoff 1–2k + STATUS 0.5k + 监控 1–2k）+ planning 6 修订点 × 15–70k（立项全量 60–70k + 增量 ×5 15–25k）≈ **185–295k** |
| **净收益** | 节省 460–1000k，**3–7 倍** |

四个关键判断：

1. **planning 投入 ≈ 现状已付的规划型开销**：as-is 里已有 85k 专用 planning 会话 + 98k 混在执行会话的修订重读 ≈ 183k；理想架构的 planning 投入 135–195k 与之同量级——**不是新增成本，是重新分配**，净收益全部来自执行侧 55–97k/任务 → 5–10k/任务。
2. **敏感项 = 修订点密度**：每个修订点服务的任务数越多越划算。R02 最优模式是 09-11 一次修订建 T17+T18 + 重排 S4/S5 + 拆 R03（一笔规划钱服务四个对象）；修订点过密则账打平（§7 风险 2）。
3. **未计入的正向项**：推理 token（窄读减少无关上下文 → 推理混淆少；case 19 记为「未证实的正向假说」），以及 fork 分支重复读的消除（每个 fork 只读 1–2k 组装视图，而非 50–90k 全文）。
4. **前提条件**：durable-session 环境（当前 DSH）。零内存环境下 execution 会话死在等待上、自续接成本另算——本成本账不适用（见 §7 边界）。

## 7. 边界与风险

- **风险 1：planner 结构模型残缺 → 窄 executor 静默出错**（R02 实例：T14 依赖图漏写 T15/T17/T18）。安全网 = 人类门禁 + executor 本地证据（判据→图→golden），不靠把 executor 变宽；依赖图完整性纳入偏差上报项。
- **风险 2：修订点过密 → planning 开销打平收益**。对策：修订点只在门禁 + 真发现时触发，任务创建合并批量处理。
- **边界：环境依赖**。本架构的窄读假设会话 durable（等待作业时不丢上下文）。零内存环境下「任务→自己」的续接需要独立快照（protocol v2 §2.2 例外判据），执行侧成本模型需相应调整。

## 8. 试点方案与升格路径

```
TBG 试点（R03，执行手册 three_role_workflow.md + 交接协议 context_handoff_protocol.md v2）
  → 退出标准全过（protocol v2 §8 九条 + 手册两条：plan 级修订 0 次由人类点破、执行会话 plan+log=0）
  → 本案例定稿（回填 R03 验收数据，状态 提案 → 定稿）
  → skill 强制层: create-plan（结构模型+输出契约约定）/ create-task（契约+依赖图）
                / run-task（窄读序+偏差上报）/ phase-wrapup（门禁+晋升）
```

## 9. 证据附录

- 原始会话日志：`/home/wyl/project/knowledge/ai_agent_practice/references/R02_archive/*.jsonl`（25 个文件）
- 量化证据：`TBG/docs/phase_R02_mtb_domain_wall/RETROSPECTIVE.md` §8（逐任务表 + 聚合）
- 上游试点报告：`19_case_study_cross_conversation_task_handoff.md` §5（8 个新问题）
- 交接层规范：`TBG/docs/context_handoff_protocol.md` v2
- 执行手册（试点用）：`TBG/docs/three_role_workflow.md`
