<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-09-03
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-09-03
 * @FilePath     : /project/knowledge/physics/mirror_symmetric_ttg/Phase_S/log.md
 * @Description  : Phase S 执行日志
-->
# Phase S 执行日志

> 格式: `### [AI:YYMMDD_Txx] 描述`（AI 执行条目）/ `### [👤 日期] 描述`（人类条目）。只追加，不删除。

---

## 2026-09-03

- [plan] Phase S 启动：`USER_BRIEF.md`（体系定义+导师假说）→ `paper_search_results.md`（48 篇，含 2026 补漏）→ `plan.md`（三问+三周排期）→ `tasks.md`（16 篇精读清单 + AI 执行队列）已就绪。
- [交接] 本文件随 `tasks.md` 移交 Execution 会话。待办：Week 1 Q1 实验精读 8 篇（人类），PDF 在 `../references/exp/`；理论 PDF（8 篇 Q2）待下载至 `../references/theory/`。
- [AI:260903] **Week 1 Q1 实验精读完成（7/8）**：产出 7 篇 `note/experiments/paper_review_E*.md`（E01/E02/E06/E07/E09/E10/E11，共 1953 行，含三层 QC + 反向核对 pass + 更正日志）。E03 跳过——exp/ 内 "Fischer 2022" PDF 实为 Fischer et al. npj QM 7,5 (2022) 理论论文，非 Cao et al. [2104.10176] 实验论文（原文缺失）。
- [AI:260903] **信息更正**：E10 = Nature Physics 21, 1237–1242 (2025)（非 "Nature 2024"）；E11 = Nature Physics 21, 1773–1779 (2025)，标题 "Gate-tunable double-dome…"（非 "Nature 2024"）；E06 = Adv. Mater. 34, 2205996 (2022)。已同步 `paper_search_results.md` 与 `tasks.md`。
- [AI:260903_T05] **编号 v3 重排 + 元数据核对**（Planning 会话）：① 按 `references/*.bib`（Zotero 导出）核对全部元数据并修正（T3/T4 卷号互换 103,195411↔104,115167；T5 作者 = Bo Xie 等；多篇期刊/年份修正）；② 剔除 5 篇非"顶层底层对齐只转中间"构型（Xia 2025 多摩尔、Kim 2026 螺旋、Davydov 2025、Devakul 2023 螺旋、Zhang 2025 准周期）；③ 编号映射：E10→E13(Pierce)、E11→E14(Zhou)、T10→T13(Yu)、N1→T21(Liang)、N4→T10(Christos)、N9→T20、R2→R1；`note/experiments/` 文件名与内部交叉引用已同步。
- [AI:260903_T06] **删除幻影 "E20 Cao [2104.10176]"**：经核实该 arXiv 实为 Fischer et al. npj Quantum Mater. 7, 5 (2022)（=T11 理论文），不存在独立 Cao TTG 实验文。"Unconventional SC" 实验侧由 E4（Kim/Nadj-Perge, Nature 606, 494）承担，Q1 待读由 E20 改为 E4。同时删除 `references/exp/` 中 Cao 2018 TBG（nature26160，双层基线，out of scope）PDF。

## 2026-09-04

- [AI:260904] **Week 1 Q1 实验精读完成（8/8）**：补读 **E4（Kim/Nadj-Perge, Nature 606, 494, 2022）**，产出 `note/experiments/paper_review_E4_kim2022_nature.md`（4 块辨识结构 + 判别表 D1–D4 + 反向核对 pass + 更正日志）。要点：−3<ν<−2 区谱学超导签名（gap+相干峰+Andreev）、Δ≈1.6 meV、2Δ/kBTC≈15–19、Tc≈2–2.5 K、T*≈7 K、Bc≳1 T、U→V（gapped→nodal）转变 + BEC–BCS 图像、peak–dip–hump（Ω/2Δ≤1）玻色模；器件单背栅、无位移场 D 旋钮（"gate-tunable" 仅指 VGate 掺杂，与 E1/E2 的 D 场可调性区分）。已同步 `tasks.md` 与 `plan.md` 状态计数（Q1 实验 8/8）。
