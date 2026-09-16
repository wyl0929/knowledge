<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-17 20:17:04
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-17 20:17:05
 * @FilePath     : /.agents/home/wyl/project/knowledge/sociology/social_survey_methods/99_update_log.md
 * @Description  :
-->
<!--
Field: 社会调研方法论——从日常对话到结构化判断
Mode: quick_scan
Domain archetype: social_science
Created date: 2026-08-17
-->

# 99 Update Log / 更新日志

Last updated: 2026-09-12

## 说明

记录本 field pack 的修改历史。workspace 级变更（目录结构等）另见 `knowledge/UPDATE_LOG.md`。

---

| 日期 | 类型 | 变更内容 | 来源 | 执行者 | 下一步 |
|---|---|---|---|---|---|
| 2026-08-17 | field pack | 初始化 `社会调研方法论` field pack，模式 `quick_scan`，domain `social_science`，profile `default_user_profile`（覆盖项：跨学科知识整合者） | 用户请求：新建社会学一级目录，将社会调研内容作为其下 field | AI agent（research_onboarding_skill 流程） | 先读取 USER_BRIEF.md，再按推荐 prompt 填充正文 |
| 2026-08-17 | 目录 | 新建 `knowledge/sociology/` 一级目录；种子讨论文档从 `political_science/deepseek_markdown_20260817_f7db5f.md` 移入本包并重命名为 `seed_discussion_20260817.md` | 用户请求 | AI agent | — |
| 2026-08-17 | 内容 | 生成全部主体文档：USER_BRIEF、00/01/02、10/11、12/13/14、17、20/22、90、README | 种子文档 + skill 流程 | AI agent | 按 `22_project_candidates.md` 启动 P1 |
| 2026-08-17 | QA | 追加 QA-001（《中县干部》是否为典范文章的分层次评价）；`14_paper_registry.md` 注册 P-16《中县干部》（seed）；更新覆盖缺口说明 | 用户提问 + 用户提供 PDF | AI agent | 待核验田野时长、导师、传播影响等细节 |
| 2026-08-18 | 案例 | 新建 `23_case01_chat_pool.md`：Case-01 退休县领导口述聊天池（P1 首个落地案例）。30 卡 × 5 模块（生涯晋升/财政税费/县域经济/民生治理/观念对比），含四透镜落点、六工程问题映射、七种专属偏差、n=1 交叉验证方案、与《中县干部》对照使用法 | 用户请求：以爷爷为对象制定聊天池 | AI agent | 第一次会话登记 00 号卡片；从本地 PDF 核验《中县干部》数据 |
| 2026-08-26 | 案例 | `23_case01_chat_pool.md` 回填首次会话回答整理（§12，13/30 卡已答、E 模块 0 答），并核验全部 NV 标记（§13）：A3"50 岁不得升县处级"中央文件未获原文支持（最接近为 1983 年县级机构改革通知，且与年龄推算矛盾）、A6"35 岁现象"论文无此提法、C3 合阳县县属企业基本证实（《合阳县志 1991—2005》）、§8"中县为中原人口大县"证实（河南省 80 万人）；`90_QA.md` QA-001 待核验项回填（田野近 2 年、导师郑也夫 ✓） | 用户请求：整理回答并核实 NV 真实性 | AI agent | 按 §13.2 回访清单澄清：A3 政策年份与年龄矛盾、C5 特产税 500 万年份、新池村数 21/22、B1"70% 发放"口径；正文地名按 §9 化名处理 |
| 2026-08-26 | 结构 | 拆分 `23_case01_chat_pool.md` → `23_chat_pool.md`（问题池 v0.1，可复用：30 卡 + 使用协议 + 通用方法，去除案例专属内容与回答行）+ `cases/case01/`（README 登记卡/背景/计划/遗留问题、answers 原始回答+整理表+覆盖矩阵、verification NV 核验+回访清单）；同步更新 README、`22_project_candidates.md` P1、`90_QA.md` 交叉引用 | 用户请求：访谈对象将增多，回答与问题池分离 | AI agent | 后续每个新访谈对象新建 `cases/caseNN/`；回收阶段按卡片跨案例汇总回避率/冷场率回填 `22_project_candidates.md` P1 |
| 2026-08-26 | 结构 | 案例目录改为单文件：`cases/case01/`（README/answers/verification 三文件）合并为 `cases/case01.md`（登记卡+回答+核验合并在一个文件）；更新 `23_chat_pool.md` 目录约定、README、`22_project_candidates.md`、`90_QA.md` 交叉引用 | 用户请求：每个案例作为一个文件 | AI agent | 后续每个新访谈对象新建 `cases/caseNN.md` 单文件 |
| 2026-08-26 | 结构 | 新建包外原始层 `sociology/field_notes/`（田野日志：游离故事按日期记录 + `_index.md` 索引 + 晋升规则），与 pack 平级；pack `README.md` 增加"田野日志"指引 | 用户请求：游离故事如何记录（按日期 vs 按人物） | AI agent | 从下次会话起按天建 `YYYY-MM-DD.md`；记录时顺手补 `_index.md`；信号强者晋升进 `cases/` 或 `17_claims_evidence_ledger.md` |
| 2026-08-27 | 案例 | `cases/case01.md`：①登记出生年 1952（农历闰五月）；②全文化名脱敏（H 县/X 镇/F 镇/B 村，受访者关系仅记"亲属"，县级原始链接与真名对照表离线）；③B1 补充 2025 年县财政（工业局局长：财政收入约 2 亿、工资需 11 亿、缺口约 2 亿）并核验为 NV9（2025 一般公共预算收入 2.78 亿吻合；支出 35 亿靠转移支付+债券；"挪用/两亿缺口"无公开数据，标单一信源待核） | 用户请求：登记生日 + 化名脱敏 + 补充核实县财政 | AI agent | 回访：A3 政策年份、B1"70% 发放"口径、B1·2025 缺口口径与"挪用"说法、X 镇村数 21/22 |
| 2026-08-27 | 结构 | 将 `sociology/field_notes/` 从公开仓库**物理移出**（含敏感个人故事），迁至本地私有田野日志目录（路径不写入本仓）；本 pack README 的"田野日志"指引改为抽象措辞 | 用户请求：knowledge 为公开包，敏感故事不应留在公开仓库工作树 | AI agent | 私有根下的日记（1.5G LaTeX 项目）迁移方式待定；field_notes 内部 README 路径随迁移一并更新 |
| 2026-09-12 | 内容 | 阅读受访者（亲属长辈）在高校管理岗期间形成的公开治理理念随笔集并做摘要；因原文与摘要含受访者身份信息，已随原 PDF 一并移入私有库 `field_notes/`，公开包内不保留原文与摘要 | 用户请求：探望长辈前先读其高校供职经验形成的文章并总结落到文档 | AI agent | 探望后按 pack 协议登记新案例（问题清单见 `cases/case02.md`） |
| 2026-09-12 | 案例 | 新建 `cases/case02.md`：高校管理精英口述案例档案（单文件：登记卡 + 问题清单 + 回答 + 核验）。问题清单为本案例专属（5 模块 × 25 卡），围绕用户的 11 个话题（大学功能 / 大学科研 vs 企业科研 / 通识教育 / 道德与制度 / 教育公平 / 地域办学 / AI 与就业悲观 / K 型分化等）+ 受访者《文集》作文章参照；单位化名 S 大学、文集化名《文集》、关系仅记"亲属" | 用户请求：结合受访者文章整理一份类似 case01 的问题清单 | AI agent | 探望后按 §4.1 节奏带卡访谈，回答回填 §5、核验回填 §6 |
