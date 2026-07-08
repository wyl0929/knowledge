<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-12 14:25:09
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-12 14:25:10
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/tmbg/99_update_log.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-12
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-12
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/tmbg/99_update_log.md
 * @Description  : TMBG 子方向 field pack 更新日志
-->
# 99 Update Log / TMBG · 更新日志

Last updated: 2026-06-12

---

## 2026-06-12 (evening) — TBPM vs diag 拓扑方法限制修正

- **关键发现**：tbplas 的 Berry 曲率仅支持 diag 方法，TBPM 无法访问本征态 → 大体系拓扑分类受阻
- **影响文件**：父 pack `20_gap_table.md`, `21_asset_match.md`, `10_self_inventory.md` + 本 pack `21_asset_match.md`
- **结论**：TMBG 拓扑分类 (TMBG-T04) 需限定在 diag 可达的小体系 (n≤29)，或探索新方法。主方向回归 TBPM 强项。

## 2026-06-12 (late) — 资产同步 + 新增论文精读

- **来源**：审查 `/home/wyl/project/TMBG` 实际代码资产
- **发现**：用户 TMBG 项目已远超 field pack 初始化时的估计——n=183/472 已计算，FWHM/gap 管线就位
- **更新文件**：
  - `21_asset_match.md` — 全面重写，反映实际代码/数据资产
  - `22_project_candidates.md` — P1 卡片更新实际代码路径和已有数据
  - `paper_review_he2021_natcomm.md` — **新增** He et al. (2021) Nat. Commun. 论文精读报告
  - 父 pack 同步: `10_self_inventory.md`, `15_tool_registry.md`, `21_asset_match.md`, `99_update_log.md`
- **关键发现**：
  - He et al. (2021) 论文的 IVC 态论证直接关联 TB 计算（TMBG-P1 的验证目标）
  - 连续模型/Berry 曲率代码已在 `src/arc/` 中，从"待实现"变为"待整合"
  - 已有 n=183 LDOS 101 点 Δ 扫描 + n=472 gap 分析数据

## 2026-06-12 — 初始创建（quick_scan subfield）

**触发**：用户在父 pack（多层石墨烯：转角与非转角体系）中选择 TMBG 子方向进行 quick_scan。

**创建的文件**：
- `USER_BRIEF.md` — 子方向调研需求
- `00_beginner_guide.md` — TMBG 入门指南
- `01_research_overview.md` — TMBG 研究综述
- `02_frontier_compass.md` — TMBG 边界罗盘
- `20_gap_table.md` — TMBG 专属缺口表
- `21_asset_match.md` — 资产-缺口匹配
- `22_project_candidates.md` — 候选项目卡片
- `99_update_log.md` — 本文件

**继承内容**：
- 继承父 pack 的全部术语体系（`11_term_disambiguation.md`）
- 继承父 pack 的文献库（`14_paper_registry.md`）中的 TMBG 条目
- 继承父 pack 的工具生态（`15_tool_registry.md`）
- 继承父 pack 的人物谱系（`13_actor_map.md`）
- 继承父 pack 的 USER_BRIEF.md 写作要求

**未创建的文件（继承父 pack）**：
- `10_self_inventory.md` — 继承父 pack
- `11_term_disambiguation.md` — 继承父 pack（TMBG 术语已在其中定义）
- `12_field_map.md` — TMBG 的问题链已在 `01_research_overview.md` §2 和 `02_frontier_compass.md` §3 中覆盖
- `13_actor_map.md` — 继承父 pack
- `14_paper_registry.md` — 继承父 pack（TMBG 文献已在 §4）
- `15_tool_registry.md` — 继承父 pack
- `17_claims_evidence_ledger.md` — 尚未创建（quick_scan 模式下非必需，可在后续 full_onboarding 时补充）

**NEEDS_VERIFICATION 内容**：
- TMBG 魔角的精确值（理论工作间有 ~0.1° 差异）
- TMBG 超导的可靠性（仅 Shin et al. 2021 一篇报道）
- TMBG 中 ν = ±1 关联绝缘态的序参量
- 位移场在紧束缚中的最佳实现方案
- 晶格弛豫在 TMBG 中的逐层效应

**建议用户下一步**：
1. 阅读 `00_beginner_guide.md` → 建立 TMBG 直觉
2. 阅读 `01_research_overview.md` → 了解实验和理论全景
3. 阅读 `02_frontier_compass.md` → 看你的切入角度
4. 阅读 `21_asset_match.md` + `22_project_candidates.md` → 选择第一个动手项目
5. 推荐从 **P1（TMBG 紧束缚基准）** 开始
