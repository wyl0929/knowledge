<!--
Field: 量子谷霍尔效应与谷电子学（Quantum Valley Hall Effect & Valleytronics）
Mode: full_onboarding
Domain archetype: science_technical
Created date: 2026-09-02
-->

# 99 Update Log / 更新日志

Last updated: 2026-09-02

## 使用说明

每次新增或修改 living layer 文件都要在这里记录。不要静默修改 paper registry、gap table、project candidates 或 MVP plan。

Field / 领域：量子谷霍尔效应与谷电子学（QVH / Valleytronics）
Maintainer / 维护者：AI（research-onboarding full_onboarding）

## Status Tags / 状态标签

- `seed`：来自草稿或已有笔记。
- `skimmed`：快速读过标题、摘要或摘要级材料。
- `parsed`：已经抽取方法、证据和局限。
- `verified`：已对照 primary source 或官方来源核验。
- `archived`：保留历史但不再作为活跃依据。
- `NEEDS_VERIFICATION`：有用但未核验。

## Log / 日志

| Date | File | Change | Reason | Source | Follow-up |
|---|---|---|---|---|---|
| 2026-09-02 | field pack | 初始化 `valleytronics`，模式 `full_onboarding`，domain `science_technical` | 从模板创建 | init_field_pack.py | 填充正文 |
| 2026-09-02 | 全部主体文件 | 完整填充 USER_BRIEF/00/01/02/10/11/12/13/14/15/16/17/20/21/22/23/90 | full_onboarding 首轮填充 | 交接表 + TBG registry/note + QHE field | readability pass |
| 2026-09-02 | 11_term_disambiguation.md | **定稿谷陈数约定**：每谷 $N_\nu=\pm1$（unit magnitude）、畴壁跳变 $\Delta N_\nu=\pm2$、每谷每自旋 2 模、4e²/h；判定 `[PHY-BERRY]` 的 "$C_v=\pm2$" 是把跳变误标成单谷值 | 对照 Huang 2018 PRL / ZMM 2013 PNAS / Verbakel 2021 PRB 原文（pdftotext+grep） | primary PDFs | 回写 TBG field `[PHY-BERRY]` 与 `99_update_log.md` |
| 2026-09-02 | 14_paper_registry.md | 从 TBG registry（T1–T39/E1–E18）筛 QVH 种子论文，标注 TBG 精读/PDF 引用锚点，不重搜 | 交接表 §4 要求 | TBG 14_paper_registry.md | 核对 Chen 2021 期刊/DOI |
| 2026-09-02 | 17_claims_evidence_ledger.md | 建立 8 条中心论断 + Operationalization Gate（provisional） | Core Claims Gate | 各结构化文件 | C-007 code audit 后更新 operational_status |
| 2026-09-02 | note/reviews/paper_review_zandvliet2023_review.md | 新增：Zandvliet 2023 QVH 核心综述精读（谱系/观点地图 + 引文挖掘） | 用户委托 paper-reading | reference/Zandvliet 2023 PDF | 核对期刊/DOI |
| 2026-09-02 | note/reviews/review_digest_2024_2025.md | 新增：4 篇 valleytronics 综述的 QVH 相关性简报 | 用户委托 paper-reading | reference/ 4 个 PDF | 无 |
| 2026-09-02 | 14_paper_registry.md | 新增综述节（五.5）+ 理论补充节（五.6：McCann-Koshino 2013 / Zhang 2011 / Yao 2009 / Ezawa 2015） | 引文挖掘 | Zandvliet 2023 引文 | 无 |
| 2026-09-02 | 11_term_disambiguation.md §7.1 | **半解决 §8.2**：chirally-stacked N 层单谷谷陈数 = N/2、每谷模数 = N → 三层 ABC 谷陈数 = ±3/2（半整数），"±3"是模数 | 用户 note.tex 推导 + Zandvliet 2023 Eq.15 + Zhang 2011 PRL | reference/note.tex + 综述 | Chen/Phong 原文核措辞 |
| 2026-09-02 | note/shared/physics/valley_chern_derivation.md + note/shared/README.md | **晋升 note.tex §1+§5** 为 [PHY-VC] 谷陈数推导链笔记（标注"用户自推导"），note.tex 保留为 LaTeX 源 | 用户确认执行迁移方案 | reference/note.tex | 无 |
| 2026-09-02 | 11_term_disambiguation.md §7.1 + 14_paper_registry.md | **Chen 2021 原文核对**：tMBG（θ=1.08°）谷陈数 $|C|=2$（D>0）、$|C|=1$（D<0），**非 ±3**；Phong 2026 用 $k^N$ 色散、每谷 N 模 | pdftotext+grep 原文 | Chen 2021 / Phong 2026 PDF | 确认 Chen 2021 期刊/DOI + $|C|$ 约定细节 |

## 待办 / Follow-up（回写与核对）

1. **回写 TBG field**：`[PHY-BERRY]` 笔记的 "$C_v=\pm2$" 应更正为"每谷 $C_v=\pm1$、畴壁跳变 $\Delta C_v=\pm2$"（TBG `note/shared/physics/04_berry_vs_ab_phase.md` + `99_update_log.md` 记一条）。⚠️ 需用户确认后执行，不擅自改跨 field 文件。
2. **核对 Chen 2021**（twisted monolayer–bilayer）准确期刊/DOI；用原文 grep 核三层 $C_v$ 约定与通道数（C-006 / G-002）。
3. **code audit**：确认 kubo_bastin.h/tbplas 是否已支持谷分辨读出（C-007 / G-003）。
4. 三层谷保护是否"软"（§8.3）：文献检索 + 理论推演，标 NEEDS_VERIFICATION。
