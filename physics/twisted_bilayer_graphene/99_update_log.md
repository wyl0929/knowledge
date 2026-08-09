<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 03:44:27
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 03:44:28
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/99_update_log.md
 * @Description  :
-->
<!--
 * @Author       : AI-generated (research_onboarding_skill, quick_scan)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/99_update_log.md
 * @Description  : TBG field pack 更新日志
-->

# 99 Update Log — TBG Edge State Field Pack

## 2026-08-06: quick_scan 初始化 (paper-search + research_onboarding_skill)

**来源**：
- DW.bib (17篇已收录文献 + PDF)
- bl-dw field pack (`multilayer_graphene/subfields/bl-dw/`, 18篇精读报告)
- 7层递进搜索 (Semantic Scholar API + arXiv keyword + author tracking)
- Semantic Scholar: citations of Rickhaus 2018, Yoo 2019
- arXiv: 8组关键词搜索 + 4组概念扩展 + 10位作者追踪

**新建文件**：
- `14_paper_registry.md` — 62篇文献注册（理论39 + 实验18 + 辅助3 + 综述4）
- `01_research_overview.md` — 理论五层图景 + 六种实验探针能力矩阵
- `12_field_map.md` — 问题链 + 方法谱系 + 成熟度评价
- `13_actor_map.md` — 8理论组 + 6实验组谱系 + 合作网络
- `02_frontier_compass.md` — 内圈/基线/边界/伪gap + 用户切入点
- `99_update_log.md` — 本文件

**更新文件**：
- `task_edge_state_search.md` — 状态更新为 ✅ 已完成

**NEEDS_VERIFICATION**：
- 几篇 2026 年预印本 (McDowell, Hung, Phong) 的期刊发表状态
- 部分 arXiv-only 论文 (Li S.-Y. 2016, Sánchez-Sánchez 2024) 的正式发表状态
- 三层石墨烯畴壁态的理论和实验文献仍可能在搜索盲区中
- Shimazaki 2015 (谷电流) 与畴壁物理的相关性需进一步确认

**下一步建议**：
- 优先补入 DW.bib：Li J. 2016, Rickhaus 2018, Yoo 2019, Tsim 2020, Fujimoto 2020, Verbakel 2021, Mahapatra 2022, Barrier 2024
- 如需深入某个子方向，从 `subfields/` 派生子包（如 `subfields/tzm-theory/`）
- 通过 `research_onboarding_skill` 的 project_incubation 模式从 frontier_compass 中的切入点评出 MVP 方案

---

## 2026-08-06 (下午): 奠基理论7篇精读

**操作**：阅读 2008-2013 年 7 篇奠基理论论文的 PDF 全文（pdftotext 提取），撰写详细精读笔记。

**新增文件**（7篇 paper_review）：
- `paper_review_martin2008_prl.md` — T1: 电场畴壁拓扑零模首次预言
- `paper_review_li2010_prb.md` — T2: 单谷体-边对应关系的非普适性
- `paper_review_jung2011_prb.md` — T3: 多层石墨烯边缘态 vs 扭结态
- `paper_review_qiao2011_nanolett.md` — T4: 扭结态弹道输运 + 谷赝自旋记忆
- `paper_review_sanjose2013_prb.md` — T5: 螺旋网络模型奠基
- `paper_review_zhang2013_pnas.md` — T6: 三类畴壁拓扑分类统一框架
- `paper_review_vaezi2013_prx.md` — T7: 倾斜边界拓扑态 + SPT 分类

**更新文件**：
- `14_paper_registry.md` — T1-T7 标记更新为 📄（已有精读笔记）
- `reference/` — 精简为 `DW.bib` + `pdfs/`（28 PDF 扁平化）
- `99_update_log.md` — 本条目

**关键发现（跨论文综合）**：
1. 奠基理论的核心演进：EFW 预言 (Martin 2008) → 单谷拓扑的严格性检验 (Li 2010) → 边缘态/扭结态区分 (Jung 2011) → 弹道输运验证 (Qiao 2011) → 螺旋网络 (San-Jose 2013) → 三类畴壁统一 (Zhang 2013) → 真实缺陷平台 (Vaezi 2013)
2. 所有奠基论文的共同前提：谷守恒近似（valley as good quantum number）——这在真实器件中不严格成立
3. T2 (Li 2010) 的关键洞察至今未过时：单谷"谷陈数"不是真正拓扑不变量，但畴壁两侧的差是——这对 DW 项目的计算建模有深刻影响
4. T3+T4 (Jung+Qiao 2011) 确立的内部畴壁优于边缘的结论，直接支持 DW 项目以 LSW/EFW 为平台的路线选择
