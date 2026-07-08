<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-21 05:08:25
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-21 05:08:26
 * @FilePath     : /.agents/home/wyl/project/knowledge/systems_science/99_update_log.md
 * @Description  :
-->
<!--
Field: 系统科学与控制论
Mode: full_onboarding
Domain archetype: science_technical
Created date: 2026-06-21
-->

# 99 Update Log / 更新日志

Last updated: 2026-07-01

---

## 2026-07-01: 案例研究 — Hall 电导基线偏移归因 (v1.5)

### 变更

| 文件 | 操作 | 说明 |
|------|------|------|
| `91_case_study_hall_conductance_baseline.md` | ➕ 新建 | Kubo-Bastin Hall 电导基线偏移归因全流程案例 |
| `99_update_log.md` | ✅ 更新 | 记录本次变更 |

### 案例要点

- **时间跨度**: 2026-06-21 ~ 2026-07-01 (10 天)
- **四阶段诊断**: 假说驱动判别实验 → 数据驱动变量追踪 → 机制建模与独立验证 → 跨代码对比突破
- **9 假说全部排除**: H₀ (M²), H₁ (Krylov), H_A (范数), H_B (Jackson核), H_C (谱泄漏), H_D (double精度), H_μ, H_Γ, H_θ, H_J, H_bias
- **最终根因**: Nyquist 采样定理 — θ 积分点数 `num_integ_steps` 不足 → 混叠
- **推翻**: VBL Phase A-M 的"条件收敛+随机游走"结论 (2026-06-27) 被标记 SUPERSEDED
- **核心教训**: 未检查的默认假设、收敛性≠正确性、诊断工具不能与被诊断对象共享缺陷

### 与前四篇 QA 的关系

| QA | 分析的 pipeline | 失效模式 | 核心教训 |
|----|---------------|---------|---------|
| QA-001 | 计算 pipeline | 数值不稳定性 (NaN) | 需要反馈控制 |
| QA-002 | 知识 pipeline | 分布式状态不一致 | 需要同步协议 |
| QA-003 | — | — | 将方法论形式化为 debug-workflow skill |
| QA-004 | 计划 pipeline | plan 增殖废弃 | 需要闭环修订 |
| **本案例** | **诊断 pipeline** | **隐性默认假设** | **诊断盲区需显式扫描** |

### 五篇的完整链条

```
QA-001 (NaN) → QA-002 (知识同步断裂) → QA-003 (形式化诊断) → QA-004 (plan退化)
                                                                      ↓
                                          本案例 (基线偏移归因全过程)
                                          — 演示了 QA-001~004 所有教训的综合体现
```

---

## 2026-06-21: QA-004 + quick_reference 扩展 (v1.4)

### 变更

| 文件 | 操作 | 说明 |
|------|------|------|
| `90_QA.md` | ✅ 追加 | QA-004: plan-task-run 工作流退化 — 开环控制在非线性环境中的失效 |
| `../.agents/skills/debug-workflow/references/quick_reference.md` | ✅ 扩展 | 新增 Plan 文件审计速查 + Plan 一致性检查 |
| `99_update_log.md` | ✅ 更新 | 记录本次变更 |

### QA-004 要点

- 诊断：plan 被当作静态预设轨迹而非动态状态估计，每次意外发现创建新 plan 而非修订原 plan → plan 增殖废弃
- 审计了 MG/docs/ 下 5 个 plan 文件，发现：M_scan_test_plan 含已证伪数据、sigma/plan 未反映 monolayer 先行路径、docs/plan 未引用 sigma 子目录、父子关系缺失、无归档机制
- 提出 5 条具体修订建议 + plan 文件状态标记规范
- 将 plan 一致性检查纳入 debug-workflow Phase 4 扩展

### 四篇 QA 的完整链条

| QA | 分析的 pipeline | 失效模式 | 核心教训 |
|----|---------------|---------|---------|
| QA-001 | 计算 pipeline | 数值不稳定性 | 需要反馈控制 |
| QA-002 | 知识 pipeline | 分布式状态不一致 | 需要同步协议 |
| QA-003 | — | — | 将方法论形式化为 debug-workflow skill |
| QA-004 | 计划 pipeline | plan 增殖废弃 | 需要闭环修订 |

### 变更

| 文件 | 操作 | 说明 |
|------|------|------|
| `../.agents/skills/debug-workflow/SKILL.md` | ✅ 新建 | 系统化诊断协议 skill (五阶段) |
| `../.agents/skills/debug-workflow/references/quick_reference.md` | ✅ 新建 | 五阶段速查 + 故障模式 + 敏感参数 |
| `90_QA.md` | ✅ 追加 | QA-003: debug-workflow skill 创建记录 |
| `99_update_log.md` | ✅ 更新 | 记录本次变更 |

### QA-003 / skill 要点

- 将 QA-001 (计算 pipeline 诊断) 和 QA-002 (知识 pipeline 诊断) 中验证的方法论形式化为可重复调用的 skill
- 核心设计：Phase 3 审计是独有功能——诊断时主动扫描 shared/knowledge 中的结论新鲜度
- Phase 2 判别实验设计后必须等用户确认，不自动提交集群任务
- Phase 4 晋升机制：MG/log → shared/ → knowledge/ 三层推进 + 旧结论 SUPERSEDED 标记
- 不删除被推翻的旧结论——保留完整审计轨迹

### 变更

| 文件 | 操作 | 说明 |
|------|------|------|
| `90_QA.md` | ✅ 追加 | QA-002: 总部-前线知识同步断裂 — 分布式系统一致性问题 |
| `99_update_log.md` | ✅ 更新 | 记录本次变更 |

### QA-002 要点

- 用户识别出两个 AI 会话（总部 knowledge 工作区 + 前线 MG 工作区）之间的知识同步断裂
- 诊断：NaN 根因从"Chebyshev 发散"更正为"rescale 误配"后，前线更新了 log 但总部文档的核心叙事未重写（仅在末尾追加修正），导致总部 AI 基于陈旧结论否决新计划
- 映射到系统工程概念：分布式状态一致性、陈旧读取、脑裂、变更传播延迟、配置审计缺失
- 产出三套方案：A) 文档结构改革（就地失效标记 + 结论状态表）B) 知识同步协议 C) 单一真相源架构
- 核心洞察：知识管理 pipeline 与计算 pipeline 有同构的反馈控制结构

### 变更

| 文件 | 操作 | 说明 |
|------|------|------|
| `90_QA.md` | ✅ 新建 | QA-001: Kubo-Bastin QHE NaN 调试作为控制论/系统工程案例 |
| `99_update_log.md` | ✅ 更新 | 记录本次变更 |

### QA-001 要点

- 用户将 Kubo-Bastin Hall 电导率的 NaN 调试经历重新理解为控制系统诊断
- 核心洞察：不同能量 E 对应 Chebyshev 递推的不同"模态稳定性"——Dirac cone 附近稳定（收敛到 ±2 e²/h），远离 Dirac cone 不稳定（发散）
- 将调试过程映射到：系统辨识（故障检测与隔离）、稳定性分析（模态依赖性）、反馈回路（假设→实验→修正）
- 产出：5 阶段计算物理调试 checklist（故障表征 → 系统建模 → 判别实验 → 稳定边界映射 → 配置固化）
- 交叉引用：`knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/` 和 `MG/docs/log.md`

---

## 2026-06-21: 首次创建 (v1.0)

### 创建的文件

| 文件 | 状态 | 说明 |
|------|------|------|
| `USER_BRIEF.md` | ✅ 完成 | 用户本次需求说明（结合计算物理背景） |
| `10_self_inventory.md` | ✅ 完成 | 用户背景与资产快照，标注了 6 项 NEEDS_VERIFICATION |
| `00_beginner_guide.md` | ✅ 完成 | 人话入门指南，物理类比驱动 |
| `11_term_disambiguation.md` | ✅ 完成 | 术语澄清 + 概念边界契约 |
| `12_field_map.md` | ✅ 完成 | 领域地图（8 个子方向 + 方法谱系 + 物理连接） |
| `01_research_overview.md` | ✅ 完成 | 领域总述报告（连续中文叙述） |
| `02_frontier_compass.md` | ✅ 完成 | 边界罗盘 + 5 个个人切口 |
| `99_update_log.md` | ✅ 完成 | 本文件 |

### 待生成的文件

以下文件标记为未来扩展（当用户需要深入时再生成）：

| 文件 | 原因 |
|------|------|
| `13_actor_map.md` | 用户目前不需要关注领域内人物谱系 |
| `14_paper_registry.md` | 核心文献已在 `01_research_overview.md` 中列出 |
| `15_tool_registry.md` | 工具生态在 `12_field_map.md` 中提到，待深入 |
| `16_metrics_and_benchmarks.md` | 暂无具体项目需要指标 |
| `17_claims_evidence_ledger.md` | 本文档偏向入门+连接桥，暂无需要 ledger 级审查的中心论断 |
| `20_gap_table.md` | 已嵌入 `02_frontier_compass.md` |
| `21_asset_match.md` | 已嵌入 `02_frontier_compass.md` 的个人切口部分 |
| `22_project_candidates.md` | 用户尚未选择深入方向 |
| `23_mvp_experiment_plan.md` | 同上 |
| `90_QA.md` | ✅ 已有 QA-001（2026-06-21） |

### 使用的来源

- Wiener, N. (1948/1961). *Cybernetics*.
- Åström, K. J. & Murray, R. M. (2008). *Feedback Systems*.
- Stengel, R. F. (1994). *Optimal Control and Estimation*.
- Ljung, L. (1999). *System Identification: Theory for the User*.
- Glaser, S. J. et al. (2015). "Training Schrödinger's cat." *EPJD*, 69, 279.
- d'Alessandro, D. (2007). *Introduction to Quantum Control and Dynamics*.
- Jaynes, E. T. (2003). *Probability Theory: The Logic of Science*.
- Khalil, H. K. (2002). *Nonlinear Systems*.
- Simon, H. A. (1996). *The Sciences of the Artificial*.
- 用户已有的 field pack 资料（量子霍尔效应、宏观经济学）中的 self-inventory 信息。
- 用户 `profiles/default_user_profile.md` 中的背景信息。

### NEEDS_VERIFICATION 汇总

| 位置 | 内容 | 说明 |
|------|------|------|
| `10_self_inventory.md` | 是否系统学习过控制理论 | 假设未系统学习 |
| `10_self_inventory.md` | 是否有非线性/混沌动力学背景 | 假设无 |
| `10_self_inventory.md` | 是否接触过信号处理 | 假设无 |
| `10_self_inventory.md` | 学习时间预算 | 假设弹性时间 |
| `10_self_inventory.md` | 具体应用场景 | 用户未指定是否要将系统科学用于某个具体物理问题 |
| `10_self_inventory.md` | 是否有经济学领域合作者/导师 | 来自宏观经济学 pack |
| `12_field_map.md` | 各种"卡在哪里"的判断 | 基于已知文献的推断，非一手研究 |

### 最推荐用户下一步

1. 先读 `00_beginner_guide.md` 建立直觉（30 分钟）
2. 再读 `01_research_overview.md` 看全景（45 分钟）
3. 对照 `02_frontier_compass.md` 的 5 个切口，选一个方向（15 分钟）
4. 告诉我想深入哪个切口，我会生成对应的 `22_project_candidates.md` 和 `23_mvp_experiment_plan.md`
