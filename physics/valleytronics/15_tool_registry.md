<!--
Field: 量子谷霍尔效应与谷电子学（Quantum Valley Hall Effect & Valleytronics）
Mode: full_onboarding
Domain archetype: science_technical
Created date: 2026-09-02
-->

# 15 Tool Registry / 工具生态注册表

Last updated: 2026-09-02

## 使用说明

本文件记录谷电子学/QVH 计算与文献工作可用的软件、代码与流程。工具状态可能变化，涉及版本与能力时优先查官方文档/源码。多数工具是用户已有资产或 TBG/QHE field 已登记的资产。

Field / 领域：量子谷霍尔效应与谷电子学（QVH / Valleytronics）

## Tool Entry / 工具条目

### tbplas（tight-binding propagation library）

- 人话摘要：用户主力紧束缚传播库，能做大规模 TBPM、DOS、输运。
- 维护者/机构：课题组自用（位置：工作区）。
- 主要用途：紧束缚哈密顿量构建 + 传播法输运/态密度。
- 输入：晶格 + hopping + 边界/无序/场配置。
- 输出：LDOS、DOS、输运量。
- 优点：可扩展、MPI 并行、已有 Kubo-Bastin 能力。
- 局限：**谷分辨读出待确认**（Kubo-Bastin 默认总电导，是否/如何投影到 K/K′ 谷需 code audit）。
- 与用户资产关系：直接主力工具。
- 可作 benchmark 的方式：复现 E9 Huang 2018 的 tight-binding LDOS（参数已给全：w≈0.45 eV、2u≈60 meV、r_DW/r_AB 坐标）；复现 ZMM 2013 LSW 每谷 2 条模。
- 待核验：谷分辨 Kubo-Bastin 是否现成（NEEDS_VERIFICATION）。

### kubo_bastin.h（QHE field）

- 人话摘要：Kubo-Bastin 电导实现，位于 `Quantum_Hall_Effect/subfields/tbplas_conductivity/`。
- 主要用途：Hall 电导数值（KPM + Kubo-Bastin）。
- 输入：哈密顿量 + 化学势 + 展宽参数。
- 输出：σ_xx/σ_xy（总电导）。
- 优点：线性标度、已有基准（QHE field）。
- 局限：**总电导**；谷霍尔电导需在此之上做谷子空间投影/分解。
- 与用户资产关系：谷霍尔电导 MVP 的起点（改代码而非从零）。
- 待核验：能否直接支持谷分解（NEEDS_VERIFICATION）。

### graphene.py（单层）

- 人话摘要：单层石墨烯紧束缚计算。
- 主要用途：单层 TB 能带/LDOS 基准。
- 与用户资产关系：双层/三层畴壁模型需在其上扩展层间 hopping + 垂直场。
- 待核验：无。

### TBPM/DOS 计算

- 人话摘要：紧束缚传播法态密度/输运。
- 主要用途：大规模 LDOS(r)（可 FFT 对标 Verbakel 2021 的 QPI 判据）。
- 约束：规模上限 M≤2560、rescale=−1（半带宽自动）。
- 与用户资产关系：谷保护 QPI 数值复现的关键工具。

### tflovorn（E9 SI 引用的理论 LDOS 代码）

- 人话摘要：E9 Huang 2018 SI 用的线性四面体法 tight-binding LDOS（`github.com/tflovorn/{tightbinding,blg_moire}`）。
- 主要用途：mTBG 局域带近似 LDOS。
- 与用户资产关系：tbplas 可直接对标其 LDOS 输出。
- 待核验：仓库可访问性/许可（NEEDS_VERIFICATION）。

### pdftotext + grep（文献反向核对流程）

- 人话摘要：paper-reading QC v1.1 的反向核对工具链（PDB 提取 + grep 数字核对）。
- 主要用途：核对原始 PDF 的术语/数字（本次 C_v 约定定稿即用此法）。
- 与用户资产关系：后续 Chen 2021 / Phong 2026 的 $C_v=\pm3$ 核对必须用它。

### SLURM 集群（h3clogin）+ submit.py

- 人话摘要：远程集群算力，Intel oneAPI + MKL，多节点 MPI。
- 主要用途：大规模 TBPM/Kubo 计算。
- 与用户资产关系：三层畴壁体系（M≤2560）能否跑通需试算。

## Tool Comparison Table / 工具对比表

| Tool | 人话摘要 | Domain | Primary use | Strengths | Limitations | Relation to user assets | 成熟度 |
|---|---|---|---|---|---|---|---|
| tbplas | 紧束缚传播库 | TB 输运/DOS | TBPM、Kubo | 可扩展、MPI | 谷分辨待确认 | 主力 | usable |
| kubo_bastin.h | Kubo-Bastin 电导 | Hall 电导 | 总 σ_xx/σ_xy | 线性标度、有基准 | 总电导非谷分辨 | 谷霍尔电导起点 | usable |
| graphene.py | 单层 TB | 单层能带 | LDOS 基准 | 简单 | 仅单层 | 扩展层间项 | usable |
| tflovorn | 四面体法 LDOS | mTBG LDOS | 对标 E9 | 参数已给全 | 外部仓库 | 对标基准 | 待核 |
| pdftotext+grep | 反向核对 | 文献 QC | 数字/术语核对 | 可靠 | 需逐条 | 定稿 C_v 约定 | mature |

*Last updated: 2026-09-02*
