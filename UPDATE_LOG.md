<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-11 20:23:12
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-11 20:23:13
 * @FilePath     : /.agents/home/wyl/project/knowledge/UPDATE_LOG.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-11
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-11
 * @FilePath     : /.agents/home/wyl/project/knowledge/UPDATE_LOG.md
 * @Description  : knowledge/ workspace 级别变更日志
-->

# UPDATE_LOG / 工作区变更日志

> 记录 workspace 级别事件：目录结构重组、新 field pack 创建、跨 pack 约定变更。
> 各 field pack 内部变更请参见对应 `99_update_log.md`。

---

## 2026-10-28

### 新文件
- **philosophy/zhanguan_yutonglu/**: 新建读书札记「思岂可废得」——湛若水《天关语通录》一则语录的源流与评价（`zhan_ruoshui_si_buke_fei.md`）。含作者简介、卷二十三《天关语通录》简介、儒家经典／湛若水思想／王湛之争三层背景，以及针对「思不可废」命题的时人与后人评价；评价部分明确区分「对命题的评价」与「对湛若水其人的评价」。同步在 README 的 philosophy 结构块与状态表下加注。

---

## 2026-09-27

### 目录结构（physics/twisted_bilayer_graphene 重构）
- **TBG 包身份补齐**：`twisted_bilayer_graphene/` 早已从 `multilayer_graphene/subfields/tbg` 提升为 `physics/` 下独立包，但根 `README.md` 的结构块与状态表仍把它写成 `multilayer_graphene` 的子方向 ⇒ 本次改正（结构块 + 状态表新增一行）。
- **包内三层收敛**（详见 `physics/twisted_bilayer_graphene/99_update_log.md`）：
  - 任务/阶段层统一到 `tasks/`（原 `Phase_S/` → `tasks/phase_S/`，原 `miniband_theory/` → `tasks/miniband_theory/`，根目录 `task_edge_state_search.md` → `tasks/archive/`）；
  - 方法论层从 `note/shared/method/` 提升到 `methods/`（并归档 `theory_paper_reading_v3_DRAFT.md`）；
  - 归档分组：`archive/*.backup_*.md` → `archive/_backups/`；
  - 会话日志 `*.jsonl`（17.6 MB）移出笔记树到 `_logs/`。
- **新增入口文档**（该包此前无 README / USER_BRIEF）：`README.md` · `USER_BRIEF.md` · `tasks/README.md` · `methods/README.md` · `reference/README.md`（PDF ↔ 文献号索引，因 `pdfs/` 文件名不含 T/E 号）。
- **索引修复**：`note/index.md` 登记 T40–T42 并更新目录范围（T00–T39 → T00–T42）。

---

## 2026-09-02

### 新文件
- **physics/valleytronics/**: 新建「量子谷霍尔效应与谷电子学」field pack（full_onboarding，science_technical）。scope = 谷陈数/谷输运/谷保护的通用理论，服务 TBG（AB/BA 双层）+ TMBG（ABC/ABA 三层）。种子论文从 TBG registry 筛出（不重搜），通用物理锚点 [PHY-BERRY]/[PHY-QPI]/[PHY-GATE]/[PHY-EF] 只引用不复制。

### 跨 pack 约定
- **谷陈数约定定稿**（本 pack 内 + 待回写 TBG）：每谷谷陈数 $N_\nu=\pm1$（unit magnitude）、畴壁跳变 $\Delta N_\nu=\pm2$、每谷每自旋 2 模、4e²/h；判定 TBG `[PHY-BERRY]` 笔记 "$C_v=\pm2$" 是把"畴壁跳变"误标成"单谷值"，待用户确认后回写。
- **QVH ≠ QHE 边界**：`Quantum_Hall_Effect` field 已把 QVH 移出子方向、标注为相邻领域；本 pack 作为 QVH 的独立"现象/理论"层落地。

---

## 2026-08-30

### 目录结构
- **design/**: 新建一级目录（设计/视觉领域），与 sociology/、computer_science/ 等平级

### 新文件
- **design/平面设计/**: 新建「平面设计入门」field pack（quick_scan，mixed），双主线：理论基础（四原则/色彩/字体/网格/层级/对比度）+ 具体桌面壁纸设计方案（`22_project_candidates.md` 含 5 张可照做的设计卡片，含色值/构图/导出）。含 `15_primary_materials_and_reading_path.md` 与 `16_key_questions_and_cases.md` 人文型模块
- **physics/introduction/**: 新建「物理学入门」field pack（orientation，science_technical，general_interest 定位），physics/ 的入门层。主线：经典物理 → 现代物理（相对论+量子）→ 当代前沿；含概念边界契约（working_definition）、9 分支谱系、4 坐标轴、17 条证据分级 seed 来源（📜Q/💭I，卷期页码统一不填防编造）、贯穿例子（苹果→微波背景）、分层阅读路径，与 physics/ 已有凝聚态 pack 互指。不生成 gap/project/MVP（兴趣了解）。完整性检查 0 error / 0 warning
- **political_science/us_taiwan_political_communication/**: 新建「美国涉台政治传播」field pack（full_onboarding，social_science）。研究设计：2017.01–2026.01 三阶段（特朗普一期/拜登/特朗普二期）× Yahoo News + X 双平台 × 涉台政治事件触发取样，考察框架建构、演变机制与跨媒介传播。用户研究设计转写为 priority project P1（provisional，含完整 Operationalization Contract）+ 消歧型 MVP（佩洛西事件试点）。文献层由 paper-search 双子代理（OpenAlex + web_search）完成：约 80+ 条文献条目级核验，含 2 份搜索原始记录（`_search_notes_a/b`）。完整性检查 0 error / 0 warning

---

## 2026-08-27

### 目录结构
- **sociology/field_notes/**: 从公开 knowledge 仓库**物理移出**（含敏感个人故事），迁至本地私有目录（路径不写入本仓）；公开仓库不再包含田野日志原始层

---

## 2026-08-26

### 目录结构
- **sociology/field_notes/**: 新建「田野日志」原始层目录（游离故事按日期记录 + `_index.md` 索引），与 `social_survey_methods` pack 平级；pack 内只放指针与"晋升后"的结构化内容

### 跨 pack 约定
- 游离故事（超出问题池 Q&A 的见闻/传闻）记录约定：正文按日期（不按人物），检索靠索引，信号强者晋升进 pack 的 `cases/` 或 `17_claims_evidence_ledger.md`，原始日志留底。详见 `sociology/field_notes/README.md`

---

## 2026-08-21

### 新文件
- **philosophy/phenomenology/**: 新建「现象学」入门 field pack（orientation，humanities_cultural，general_interest 定位），含 `00/01/10/11/12/13/14/15/16/90/99` 与 `USER_BRIEF.md`、`README.md`

---

## 2026-08-17

### 目录结构
- **sociology/**: 新建一级目录（社会学领域），与 political_science/ 平级
- **political_science/**: 根目录下的 `deepseek_markdown_20260817_f7db5f.md` 移出

### 新文件
- **sociology/social_survey_methods/**: 新建「社会调研方法论」field pack（quick_scan，social_science），含全部主体文档
- **sociology/social_survey_methods/seed_discussion_20260817.md**: 种子讨论文档（自 political_science 移入并重命名）
- **sociology/fundamentals/**: 新建「社会学入门——基本概念与基础理论」field pack（quick_scan，social_science，general_interest 定位）

---

## 2026-08-11

### 目录结构
- **systems_science/**: 建立 `case/` 子目录，8 个 case study 文件从根目录移入，编号从 91–98 重编为 01–08
- **systems_science/**: `case_hall_baseline/` → `case/hall_baseline/`

### 新文件
- **workspace**: 创建 `UPDATE_LOG.md`（本文件）
- **workspace**: 更新 `README.md`，同步至当前目录结构

### 跨 pack 约定
- case study 编号体系：独立 `case/` 目录内使用 01–NN 自然序号，不再与 field pack 的 90–99 段混用

---

## 2026-07-27
- **political_science/central_local_relations/**: 新增案例研究「土地财政」(v1.3)

## 2026-07-17
- **philosophy/**: 新建 `reductionism/` field pack（还原论，含 subfields/power_reductionism_as_case/）

## 2026-07-11
- **political_science/**: 新建 `corporatism/` field pack（法团主义，从 central_local_relations QA 派生）
- **workspace**: 更新 `README.md` 各包状态表

## 2026-07-08
- **political_science/**: 新建 `central_local_relations/` field pack（央地矛盾）

## 2026-07-03
- **political_science/**: 新建 `us_two_party_politics/` field pack（美国两党政治，含 subfields/dsa_2026_wave/）

---

## 2026-11

### 迁入项目级方法论 REVIEW（自 TBG 仓库）
- **`ai_agent_practice/references/REVIEW_phase_division_2026-11.md`** —— Phase 划分体检 + 重划方案（Part A，2026-11-01）+ 第三方复检与手册审计（Part B，2026-11-02），**两份合并为单文件**。
- **`ai_agent_practice/references/REVIEW_data_layout_2026-11.md`** —— 数据资产按模型组织（提案）。
- **归属判据**：跨项目可复用的方法论 → `knowledge/`；绑定具体仓库路径/命令 → 留在该仓库 `docs/`。TBG 侧保留指针 `docs/REVIEWS.md`。

---

## 2026-06

### 初始化
- **workspace**: `knowledge/` repo 初始化（2026-06-19）
- **physics/**: 四个 field pack 创建（QHE, multilayer_graphene, TBG, strongly_correlated）
- **philosophy/**: `mental_causation_closure/`、`power_reductionism/` 创建
- **Economics/**: `macroeconomics/` 创建
- **systems_science/**: 控制论与系统工程 field pack 创建（2026-06-21）
- **computer_science/**: `cpp_for_tbplas/` 创建（2026-06-22）
