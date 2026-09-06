# 量子谷霍尔效应与谷电子学 Field Pack / 领域包

Field: 量子谷霍尔效应与谷电子学（Quantum Valley Hall Effect & Valleytronics，QVH / Valleytronics）

Mode: full_onboarding

Domain archetype: science_technical

Output path / 输出路径: /home/wyl/project/knowledge/physics/valleytronics

Profile source / 背景来源: /home/wyl/.agents/skills/research-onboarding/profiles/default_user_profile.md（叠加 handoff §6 覆盖项）

Created date: 2026-09-02

Last updated: 2026-09-02

## 用途

本目录是量子谷霍尔效应 / 谷电子学（QVH / valleytronics）的 L1 field pack，覆盖**谷陈数 / 谷输运 / 谷保护**的通用理论，服务 **TBG**（AB/BA 双层畴壁）与 **TMBG**（ABC/ABA 三层畴壁）两个方向。它是"现象/理论"field，与 `Quantum_Hall_Effect`（不同族）、`twisted_bilayer_graphene`/`multilayer_graphene`（下游平台）互补。

种子论文全部从 `twisted_bilayer_graphene/14_paper_registry.md` 筛出（不重搜）；通用物理引用锚点 `[PHY-BERRY]/[PHY-QPI]/[PHY-GATE]/[PHY-EF]` 仍留在 TBG field，本 pack 只引用不复制。

## 关键结论速览

- **QVH ≠ QHE**：总霍尔电导 $\sigma_{xy}=0$，无量子化平台（时间反演 $C_K+C_{K'}=0$）。
- **谷陈数约定（已定稿）**：每谷 $N_\nu=\pm1$（unit magnitude），畴壁跳变 $\Delta N_\nu=\pm2$，每谷每自旋 2 模，两端口 $4e^2/h$。
- **谷保护是软保护**：动量失配只挡平滑势，原子缺陷即破坏。
- **存在性 ≠ 保护**：证据阶梯 ①存在性 ②形态一致 ③谷保护(FFT) ④抗无序量化（未闭环）。
- 唯一"保护"直接证据：Verbakel 2021 PRB 的 FFT intervalley 斑缺失。

## 文件

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
- `16_metrics_and_benchmarks.md`
- `17_claims_evidence_ledger.md`
- `20_gap_table.md`
- `21_asset_match.md`
- `22_project_candidates.md`
- `23_mvp_experiment_plan.md`
- `90_QA.md`
- `99_update_log.md`

## 下一步

推荐下一步（priority project P-001 第一阶段）：code audit 谷分辨 Kubo-Bastin 能力（C-007）→ 均匀 gapped 双层算单谷谷陈数 ±1。详见 `23_mvp_experiment_plan.md`。

## 自检命令

```bash
python /home/wyl/.agents/skills/research-onboarding/scripts/check_pack_integrity.py /home/wyl/project/knowledge/physics/valleytronics
```
