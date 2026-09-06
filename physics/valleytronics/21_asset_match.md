<!--
Field: 量子谷霍尔效应与谷电子学（Quantum Valley Hall Effect & Valleytronics）
Mode: full_onboarding
Domain archetype: science_technical
Created date: 2026-09-02
-->

# 21 Asset Match / 用户资产匹配

Last updated: 2026-09-02

## 使用说明

本文件把 gap table 中的机会与用户真实资产对齐，避免只因为方向热门就生成不可执行项目。

Field / 领域：量子谷霍尔效应与谷电子学（QVH / Valleytronics）

## Asset-to-Gap Matrix / 资产-缺口矩阵

| User asset | 成熟度证据 | Matching gap | Why it matches | Missing resource | Risk | Next action |
|---|---|---|---|---|---|---|
| tbplas + TBPM/DOS | usable（主力） | G-001（级④数值）、G-003 | 紧束缚 + 传播法天然适合畴壁边界模 + 无序输运 | 谷分辨投影实现 | 无序下谷标签退化 | 先做 G-003 谷分辨读出 |
| kubo_bastin.h（QHE field） | usable（有基准） | G-003、G-001 | 总电导已能算，谷分解是增量改造 | 谷子空间投影方案 | 投影失效 | code audit 确认现状 |
| graphene.py（单层） | usable | G-001/G-003 起点 | 单层 TB 可扩展为双层 + 垂直场 | 层间 hopping + Δ 项 | 参数未校准 | 扩展为 gapped 双层模型 |
| TBG 精读笔记 + PDF 库 | mature | G-002 | Chen 2021/Phong 2026 PDF 已入库，核对 $C_v=\pm3$ 无需重搜 | 无 | 无 | pdftotext+grep 核对 |
| SLURM 集群（h3clogin） | mature | G-001/G-003 | 大规模畴壁超胞计算算力 | 三层体系 M≤2560 是否够用待试 | 规模上限 | 小规模试算 |

## Strong Matches / 强匹配

- **Gap / 缺口**：G-001（级④抗无序量化输运的**计算侧**）+ G-003（谷分辨读出，前置）。
- **人话匹配解释**：用户已有的紧束缚 + Kubo-Bastin + TBPM 正是"谷陈数→边界模"与"软保护→缺陷破坏"所需的最小方法栈，且三个 benchmark（ZMM 2013 LSW / E9 LDOS / E13 FFT）都给了可复现参数。
- **资产**：tbplas、kubo_bastin.h、graphene.py、TBPM/DOS。
- **为什么可行**：双层畴壁体系在 TBPM 规模上限内；benchmark 参数已给全；无实验依赖。
- **最小证明**：先实现谷分辨读出，在均匀 gapped 双层上算单谷谷陈数 = ±1（解析值对标），再做 AB/BA 畴壁每谷 2 模。

## Weak or Misleading Matches / 弱匹配或误导性匹配

- **方向**："谷霍尔电导严格量子化"（G-004 若被误当成主攻）。
- **人话提醒**：谷不守恒 → 无严格量子化；把它当 QHE 式指标去做，方向从定义上就错。
- **为什么看起来吸引人**：像 QHE 的干净量子化平台，指标漂亮。
- **为什么可能失败**：谷不守恒使 $\sigma_{xy}^V$ 无严格平台，定义有歧义、难复现。
- **停止条件**：若 1 个月内给不出良定义的"偏离量子化度"指标，标为 not-a-gap 并转向 G-001。

- **方向**："三层 tMBG 数值直接上"（在 G-002 约定未核前）。
- **人话提醒**：三层 $C_v=\pm3$ 约定未核、ZMM 明言 ABA 三层谷陈数难定义，直接做数值可能对着错误定义白做。
- **为什么看起来吸引人**：TMBG 是热点、用户有多层平台 field。
- **为什么可能失败**：约定没钉死，算出来的"通道数"无法对标。
- **停止条件**：先做文献核对（P-002），核对不出约定就不做三层数值。

## Collaboration Needs / 合作需求

| Need | Why needed | Possible collaborator | Urgency | Status |
|---|---|---|---|---|
| 谷分辨输运的方法先例 | 无序下谷投影是否良定义需领域内经验 | 理论合作者 | medium | NEEDS_VERIFICATION |
| 三层畴壁实验数据 | tMBG 谷陈数/谷保护无直接实验，纯计算难闭环 | 实验合作者（STM/输运） | low | NEEDS_VERIFICATION |
