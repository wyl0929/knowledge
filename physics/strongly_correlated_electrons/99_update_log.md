<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-14 22:27:34
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-14 22:27:34
 * @FilePath     : /project/knowledge/physics/strongly_correlated_electrons/99_update_log.md
 * @Description  :
-->
<!--
Field: 强关联电子体系
Mode: quick_scan
Domain archetype: science_technical
Created date: 2026-06-14
-->

# 99 更新日志 / Update Log

Last updated: 2026-07-24

## 2026-07-24：QA-001 追加

- `90_QA.md` 新增 QA-001：「tbplas 处理电子相互作用的路径」——基于单电子态的 tbplas 是否只能通过自洽计算处理强关联/多体相互作用。梳理了五条路径（HF/DFT+U, 隶粒子平均场, DMFT, GW/RPA, ED/DMRG/QMC）的适配度、适用范围和关键判断。指向 Project P1 和 Gap 3/7。

## 2026-06-14：首次生成 (quick_scan)

### 来源
- 用户自然语言输入："强关联效应的现象, 理论与计算"
- Mode: quick_scan（用户选择）
- Profile: default_user_profile
- Domain archetype: science_technical
- 信息来源：基于 AI 训练数据中截至 2026 年初的公开学术知识。未使用实时网络检索。

### 生成文件
| 文件 | 说明 |
|------|------|
| `USER_BRIEF.md` | 本次用户需求记录 |
| `README.md` | 包内目录与阅读指引 |
| `00_beginner_guide.md` | 入门指南（人话版） |
| `01_research_overview.md` | 领域总述（连续可读报告） |
| `02_frontier_compass.md` | 边界罗盘（内圈/中圈/边界/伪gap/用户切口） |
| `10_self_inventory.md` | 用户背景快照 |
| `11_term_disambiguation.md` | 术语澄清与概念边界契约 |
| `12_field_map.md` | 领域地图（问题链、方法谱系、核心假设、计算工具生态） |
| `13_actor_map.md` | 代表研究者与研究组 |
| `14_paper_registry.md` | 关键文献注册表 |
| `17_claims_evidence_ledger.md` | 论断-证据台账 |
| `20_gap_table.md` | 研究缺口表（含用户匹配度评估） |
| `22_project_candidates.md` | 候选项目卡片（P1-P4 + 推荐路线图） |
| `90_QA.md` | QA 缓冲区 |
| `99_update_log.md` | 本文件 |

### 覆盖范围
- ✅ 强关联电子体系的核心现象（莫特绝缘体、高温超导、重费米子、自旋液体、魔角石墨烯关联）
- ✅ 理论方法谱系（Hubbard 模型、DMFT、DMRG/张量网络、QMC、隶粒子方法等）
- ✅ 计算工具生态（TRIQS、ITensor、w2dynamics、ALPS 等）
- ✅ 与用户背景（TBPM、石墨烯紧束缚、MPI、SLURM）的连接和切入点
- ✅ 候选研究项目（4 个，含优先级排序）

### 已知局限与 NEEDS_VERIFICATION
- 所有论文的精确卷号、页码、DOI 标注为 NEEDS_VERIFICATION
- 所有研究者的当前所属机构标注为 NEEDS_VERIFICATION
- 亚洲研究者/研究组的具体信息标注为 NEEDS_VERIFICATION
- 部分工具的最新版本号和功能标注为 NEEDS_VERIFICATION
- 具体实验结果的精确时间线和优先权可能需要核实
- 未生成 `15_tool_registry.md`（quick_scan 模式下工具信息已整合到 `12_field_map.md`）
- 未生成 `16_metrics_and_benchmarks.md`（quick_scan 模式下基准信息已分散在各文档）
- 未生成 `21_asset_match.md`（匹配分析已整合到 `20_gap_table.md` 和 `22_project_candidates.md`）
- 未生成 `23_mvp_experiment_plan.md`（quick_scan 模式下 P1 的初步 operationalization 已放入 `22_project_candidates.md`）
- 未使用实时网络检索，所有信息来自训练数据中的公开学术知识

### 推荐用户下一步
1. 阅读 `00_beginner_guide.md` 建立直觉
2. 阅读 `02_frontier_compass.md` 找到自己的切口
3. 按 P4 → P1 路线开始动手（一维 Hubbard ED → TBPM+DMFT 混合）
