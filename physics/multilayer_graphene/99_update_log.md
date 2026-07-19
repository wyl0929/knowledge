<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-11 20:23:00
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-07
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/99_update_log.md
 * @Description  :
-->
# 99 Update Log / 更新日志

Last updated: 2026-07-16

---

---

## 2026-07-16: 新增子方向 — ABA/ABC 堆叠畴壁（Stacking Domain Wall）

- **来源**：用户要求检索 ABA/ABC 堆叠畴壁实验和理论文献
- **新增子方向**：`subfields/stacking-dw/`
  - `01_literature_scan.md` — 合并文献扫描（1 实验 + 4 理论）
- **更新文件**：
  - `14_paper_registry.md` — 新增 §10「ABA/ABC 堆叠畴壁」(SD1–SD5)；阅读优先级新增第六步
- **关键发现**：
  - ★ Yin et al. (2017, Lin He 组) — **唯一实验**：STM 观测 ABA/ABC 堆叠孤子
  - Jaskólski 系列 (2016–2024) — 三层/多层堆叠畴壁的 TB 理论
  - **输运实验完全空白** → TBPM 的天然切入点
- **NEEDS_VERIFICATION**：Jaskólski 2024 为预印本

## 2026-07-08 (late): Zotero 集成 — 文献与笔记桥接

- **问题**：Zotero 管理 PDF / knowledge base 管理笔记，两者物理分离，缺乏连接
- **方案**：在每个 paper review 和 paper registry 条目中嵌入两个稳定链接
  - **DOI**: `https://doi.org/...` — 浏览器打开论文页面
  - **Zotero Key**: `zotero://select/items/KEY` — 一键在 Zotero 中打开 PDF
- **更新文件**：
  - `templates/paper_review.md` — 元信息区新增 DOI + Zotero 链接行
  - `templates/14_paper_registry.md` — 新增 Zotero Key 字段
  - 全部 3 篇 `paper_review_*.md` — 补充 DOI 链接 + Zotero 占位符 `ZT_KEY_NEEDED`
  - `14_paper_registry.md`（父级） — 所有表格新增 Zotero 列（55 行占位）
  - `subfields/domain-wall/14_paper_registry.md` — 每篇论文新增 Zotero Key 行
- **待用户完成**：在 Zotero 中选中文献 → Ctrl+Shift+C 复制 key → 批量替换 `ZT_KEY_NEEDED`

## 2026-07-08 (late): 论文笔记迁移至子领域 + 英文目录重命名

- **目录重命名**：`多层石墨烯：转角与非转角体系/` → `multilayer_graphene/`
- **论文笔记迁移**：
  - `refer/paper_review_hou2024_prb.md` → `subfields/domain-wall/paper_review_hou2024_prb.md`
  - `refer/paper_review_rickhaus2018_nanolett.md` → `subfields/domain-wall/paper_review_rickhaus2018_nanolett.md`
  - 对应 PDF 同步迁移至 `subfields/domain-wall/`
  - 删除临时目录 `refer/`
- **更新文件**：
  - `14_paper_registry.md` — 修复 DW3/DW7 精读链接（`refer/` → `subfields/domain-wall/`）
  - `subfields/domain-wall/14_paper_registry.md` — 新增「mTBG 畴壁输运」补充分类（DW-m1–m4），含两篇精读链接
  - 所有父级 + 子领域文件 `@FilePath` 头注释同步更新为新英文路径
  - `research_onboarding_skill` v1.2 — 正式化 paper_review 命名/放置规范

---

## 2026-07-08 (late): 新增 Hou et al. (2024) 论文精读 + 畴壁分类

- **来源**：用户要求阅读并整理 Hou 2024 文章
- **论文**：Zhe Hou, Kai Yuan, Hua Jiang — "Arrays of one-dimensional conducting channels in minimally twisted bilayer graphene", PRB 110, L161406 (2024) | arXiv:2408.09843
- **新增文件**：
  - `refer/paper_review_hou2024_prb.md` — 论文精读报告（8 节，含方法、结果、局限、与用户关联）
- **更新文件**：
  - `14_paper_registry.md` — 新增 §8「小转角与畴壁物理」分类（DW1–DW9），原 §7–§8 顺延为 §9–§10；阅读优先级新增第五步
- **核心发现**：
  - 裁决了 mTBG 畴壁 THS 的传播方式争议：THS 形成独立一维 TZM（非二维三角网络）
  - 预言近量子化电导平台 NQCP = 1, 2, 3 × 2e²/h 可作为 TZM 的决定性实验特征
  - 所有导电通道 100% 谷极化 → valleytronics 应用前景
  - 方法：真实空间紧束缚 + NEGF 量子输运 → 与用户的 TB 代码同源，可直接复现

## 2026-07-08: 文件夹重命名 — 扩展范围至非转角体系

- **原因**：原名称"三层和多层转角石墨烯"无法覆盖已纳入的三个非转角子方向（aba-tlg、abc-tlg、domain-wall-experiments）
- **变更**：`三层和多层转角石墨烯/` → `多层石墨烯：转角与非转角体系/`
- **配套更新**：
  - `01_research_overview.md` — 新增 §0 覆盖范围说明，明确转角/非转角/畴壁三线并行
  - `USER_BRIEF.md` — 扩展调研领域描述
  - `12_field_map.md` — 更新领域定位图
  - `00_beginner_guide.md` — 标题更新
  - 所有父级文档 `@FilePath` 头注释同步更新

---

## 2026-07-07 (late): 新增子方向 — ABC 三层石墨烯（菱方堆叠）实验文献扫描

- **来源**：用户要求检查 ABC TLG 近期实验论文，arXiv 检索
- **新增子方向**：`subfields/abc-tlg/`（quick_scan 模式）
  - `USER_BRIEF.md` — 调研需求记录
  - `01_research_overview.md` — 实验综述（2021–2025）
  - `99_update_log.md` — 子方向更新日志
- **关键发现**：
  - ABC（rhombohedral）三层石墨烯是近年最热的非转角强关联平台——Zhou et al. (Nature 2021) 发现超导后领域爆发
  - Andrea Young 组 (UCSB) 绝对主导：SC 发现 → 详细相图 → QAH+SC 共存（四层）→ STM 可视化 IVC
  - Long Ju 组 (MIT) 在 WSe₂ 邻近 SOC 方向独立推进：创纪录 Pauli 极限违反
  - 2024–2025 核心突破：零磁场 QAH + FCI（四层已证实），三层待确认
- **与父 pack 的关系**：ABC TLG + hBN 对齐 = 非转角的"魔角替代方案"，其平带+拓扑+关联的物理与转角体系深层相通
- **注**：本次为纯文献扫描，不生成 gap table 或 project candidates

## 2026-07-07 (evening): 新增子方向 — Graphene Domain Wall 实验研究文献扫描

- **来源**：用户要求检查 graphene 体系 Domain wall 的实验研究（两层/三层/多层），文献验证 + 迁移
- **新增子方向**：`subfields/domain-wall-experiments/`（quick_scan 模式）
  - `USER_BRIEF.md` — 调研需求记录
  - `01_research_overview.md` — 实验综述（arXiv 验证后重写）
  - `14_paper_registry.md` — 已验证关键文献详细总结（7 篇）
  - `99_update_log.md` — 子方向更新日志
- **迁移历史**：原始文档 `DW/docs/experimental_domain_wall_survey.md`（含大量未核实条目）已删除，DW 项目修改全部撤销
- **关键发现**：
  - **7 篇论文经 arXiv + DOI 验证为真实**：Ju 2015 Nature, Li 2016 Nat. Nanotech., Jiang 2017 Nano Lett., Shimazaki 2015 Nat. Phys., Mania 2019 Commun. Phys., Li S.-Y. 2016 (STM), Hsu 2020 Sci. Adv.
  - **8 条原始 AI 列举条目被证伪/未找到**：Yin 2014/2015, Rickhaus 2018, Kim 2019, Sunku 2018, Huang 2018, McGilly 2020, Edelberg 2022 ——AI 训练记忆的文献不可靠
  - **双层 LSW 畴壁实验已成熟**（2015–2019 期间 5 篇顶刊实验）
  - **三层畴壁实验完全空白**——arXiv 未找到任何 ABC 或 ABA 三层畴壁实验
  - **EFW 实验空白**——分裂栅加工难度导致
- **与 DW 项目的关系**：为 DW 计算项目提供实验 benchmark 矩阵（§4），明确了计算可填补的空白
- **注**：本子方向为纯文献扫描，不生成 gap table 或 project candidates

- **来源**：用户要求检查 ABC TLG 近期实验论文，arXiv 检索
- **新增子方向**：`subfields/abc-tlg/`（quick_scan 模式）
  - `USER_BRIEF.md` — 调研需求记录
  - `01_research_overview.md` — 实验综述（2021–2025）
  - `99_update_log.md` — 子方向更新日志
- **关键发现**：
  - ABC（rhombohedral）三层石墨烯是近年最热的非转角强关联平台——Zhou et al. (Nature 2021) 发现超导后领域爆发
  - Andrea Young 组 (UCSB) 绝对主导：SC 发现 → 详细相图 → QAH+SC 共存（四层）→ STM 可视化 IVC
  - Long Ju 组 (MIT) 在 WSe₂ 邻近 SOC 方向独立推进：创纪录 Pauli 极限违反
  - 2024–2025 核心突破：零磁场 QAH + FCI（四层已证实），三层待确认
- **与父 pack 的关系**：ABC TLG + hBN 对齐 = 非转角的"魔角替代方案"，其平带+拓扑+关联的物理与转角体系深层相通
- **注**：本次为纯文献扫描，不生成 gap table 或 project candidates

## 2026-07-07: 新增子方向 — ABA 三层石墨烯 QHE 实验文献扫描

- **来源**：用户要求检查近期 ABA TLG QHE 实验论文，arXiv 检索
- **新增子方向**：`subfields/aba-tlg/`（quick_scan 模式）
  - `USER_BRIEF.md` — 调研需求记录
  - `01_research_overview.md` — 实验论文综述（2011–2025，重点 2023–2025 FQH 突破）
  - `99_update_log.md` — 子方向更新日志
- **关键发现**：
  - **Chanda et al. (arXiv:2502.06245, Feb 2025)**：ABA TLG N=0 LL 中 even-denom FQH（ν=5/2, 7/2），伴随 Levin-Halperin 子态——当前最重磅突破
  - **Kaur et al. (arXiv:2411.18910, Nov 2024)**：PHS 外在破缺机制（D 场 → LL mixing → 三体相互作用）
  - **Chen et al. (arXiv:2312.17204, Dec 2023)**：独立观测 even/odd denom FQH（ν=±9/2, ±3/2）
  - **Kaur, Chanda et al. (Nat. Commun. 15, 8535, 2024)**：IQH/FQH 量子相变普适 scaling
- **与父 pack 的关系**：ABA TLG 为非转角 Bernal 堆叠三层，但在 LL mixing 物理、D 场调控、多带 QHE 方面为转角体系提供重要 baseline
- **NEEDS_VERIFICATION**：多篇预印本发表状态；even-denom FQH 拓扑序待实验确认
- **注**：本次为纯文献扫描，不生成 gap table 或 project candidates

## 2026-06-12 (late): 方法限制修正 — TBPM vs diag 拓扑瓶颈

- **来源**：用户指出 tbplas 的 Berry 曲率计算仅支持 diag 方法，TBPM 无法访问本征态
- **影响**：严重限制了大体系拓扑分类的可行性
  - n=6/29 (diag 可达) → Berry 曲率可行
  - n=183/472 (仅 TBPM) → Berry 曲率不可行
  - 魔角物理 (θ≈1.1°) 需要 n≈100+ → **拓扑分类在魔角区无法直接用现有工具完成**
- **更新文件**：
  - `20_gap_table.md` — 新增 G-M05（大超胞拓扑不变量计算），G-T03 降级优先级，新增 NG-04（TBPM 不能算 Berry）
  - `21_asset_match.md` — G-T03 可行性从 ⭐⭐⭐⭐ 降为 ⭐⭐，新增 G-M05
  - `10_self_inventory.md` — 拓扑能力标注 diag 限制
  - `subfields/tmbg/21_asset_match.md` — TMBG-T04 标注 diag 限制，新增 TMBG-M05
- **修正后的策略**：
  - 拓扑方面：小体系 (n≤29) 做精确拓扑分类 + 大体系用连续模型算拓扑，TBPM 只做 DOS/输运
  - 主攻方向回归 TBPM 强项：DOS 基准、转角无序、位移场效应
- **标记的 NEEDS_VERIFICATION**：实空间 Chern 标记/Wilson loop 方法的可行性（G-M05 缓解方案）

## 2026-06-12: 资产同步 — 整合 TMBG 项目代码

- **来源**：用户 `/home/wyl/project/TMBG` 项目代码审查
- **发现**：用户已建立完整的 TMBG 紧束缚计算项目，远超 field pack 初始化时的资产估计
- **更新文件**：
  - `10_self_inventory.md` — 更新代码资产表、算力资源、方法能力（反映 TMBG 项目实际状态）
  - `15_tool_registry.md` — 新增 TMBG 项目 + tbplas 依赖条目
  - `21_asset_match.md` — 以实际代码能力为准更新匹配矩阵、资产优势、缺失资源和推荐行动
  - `subfields/tmbg/21_asset_match.md` — 新增完整资产快照和已有数据资产表
  - `subfields/tmbg/22_project_candidates.md` — P1 卡片更新实际代码路径和已有数据
  - `subfields/tmbg/paper_review_he2021_natcomm.md` — 新增 He et al. (2021) 论文精读报告
- **关键变更**：
  - 原 field pack 假设用户仅有 `test/graphene.py` 和基础 TBPM，实际已具备 n=472 (~4M 轨道) 生产级能力
  - 连续模型/Berry 曲率代码已在 `src/arc/` 中，从"待实现"变为"待整合"
  - LAMMPS 弛豫支持已上线（rlxd 结构），G-T04 可行性从 ⭐⭐ 提升到 ⭐⭐⭐⭐
  - 已有 n=183/472 LDOS 数据，可直接整理为公开基准
- **标记的 NEEDS_VERIFICATION 项**：方法能力中机器学习仍为 NEEDS_VERIFICATION

## 2026-06-11: Field pack 初始化（quick_scan）

- **模式**：quick_scan
- **领域**：多层石墨烯：转角与非转角体系
- **用户 profile**：default_user_profile（计算凝聚态物理，TBPM/石墨烯紧束缚）
- **生成文件**：
  - `USER_BRIEF.md`
  - `00_beginner_guide.md`
  - `01_research_overview.md`
  - `02_frontier_compass.md`
  - `10_self_inventory.md`
  - `11_term_disambiguation.md`
  - `12_field_map.md`
  - `13_actor_map.md`
  - `14_paper_registry.md`
  - `15_tool_registry.md`
  - `17_claims_evidence_ledger.md`
  - `20_gap_table.md`
  - `21_asset_match.md`
  - `22_project_candidates.md`
  - `99_update_log.md`
- **未生成文件**（quick_scan 不要求）：
  - `16_metrics_and_benchmarks.md`
  - `23_mvp_experiment_plan.md`
  - `90_QA.md`
- **标记的 NEEDS_VERIFICATION 项**：多处（主要涉及论文精确卷期页码、部分实验结果的确认、华人研究者名单完整性等）
- **推荐下一步**：若用户决定推进某个候选项目（P1–P4），可切换到 `project_incubation` 模式生成 MVP 实验计划
