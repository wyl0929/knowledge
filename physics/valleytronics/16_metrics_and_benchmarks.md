<!--
Field: 量子谷霍尔效应与谷电子学（Quantum Valley Hall Effect & Valleytronics）
Mode: full_onboarding
Domain archetype: science_technical
Created date: 2026-09-02
-->

# 16 Metrics and Benchmarks / 指标与基准

Last updated: 2026-09-02

## 使用说明

本文件记录谷电子学/QVH 的常用指标、benchmark、baseline 与评估风险。每个指标说明"测量什么"和"不测量什么"，以及怎样构成公平 baseline。

Field / 领域：量子谷霍尔效应与谷电子学（QVH / Valleytronics）

## Metric 1：谷陈数 $N_\nu$（valley Chern number）

**人话解释：** 单个谷的能带绕布里渊区一圈积累的几何相位整数，决定畴壁上有几条边界模。

**定义：**（ZMM 2013）$N_\nu = -\nu\,\mathrm{sgn}(\Delta)=\pm1$（gapped 双层，单位幅度）；畴壁两侧跳变 $\Delta N_\nu=\pm2$。

**测量什么：** 每谷的拓扑电荷；畴壁边界模数 = $|\Delta N_\nu|$。

**不测量什么：** 总 Chern 数（那是 $\sum_\nu N_\nu=0$）；谷保护强度（谷陈数≠保护，保护是散射陈述）。

**常见误用：** 把 $\Delta N_\nu=\pm2$ 标成"每谷 $C_v=\pm2$"（本次已定稿纠正，见 `11_term_disambiguation.md` §2.2）。

**与用户目标关系：** 谷陈数数值计算是 MVP 的指标之一；计算方式 = Berry 曲率离散积分（Fukui-Hatsugai-Suzuki）或 Wilson loop。

## Metric 2：谷霍尔电导 $\sigma_{xy}^V$（valley Hall conductivity）

**人话解释：** 只算一个谷贡献的横向电导，两谷反号、总合为零。

**定义：** $\sigma_{xy}^{V}=N_\nu e^2/h$（谷守恒近似下），$\sigma_{xy}^K=-\sigma_{xy}^{K'}$，总 $\sigma_{xy}=0$。

**测量什么：** 谷分辨横向流。

**不测量什么：** 总霍尔电导（恒 0）；**不测**严格量子化（谷不守恒 → 无严格平台）。

**常见误用：** 把谷霍尔电导当 QHE 式精确平台。

**与用户目标关系：** 数值上需把 Kubo-Bastin 分解到 K/K′ 谷（G-003）。

## Metric 3：intervalley 散射指纹（QPI 斑有/无）

**人话解释：** 傅里叶变换 STM 图后，(√3×√3)R30° 斑对应翻谷散射；斑缺失 = intervalley 背散射被抑制 = 谷保护。

**定义：**（[PHY-QPI]）$|\Delta K|=\frac{4\pi}{3\sqrt3 a}\approx1.70$ Å⁻¹（intervalley 斑）；$|b|=\frac{4\pi}{3a}\approx2.95$ Å⁻¹（1×1 斑，谷内）。

**测量什么：** intervalley 散射通道是否被激发（二元有/无）。

**不测量什么：** 散射强度比值；绝对零（"无峰"=测量分辨率内无）。

**常见误用：** 把"无斑"读成"绝对无 intervalley 散射"；把"有斑"读成"完全无保护"。

**与用户目标关系：** TBPM 算 LDOS(r) → 2D FFT → 判斑，可直接对标 Verbakel 2021。

## Metric 4：畴壁通道计数与电导 $4e^2/h$

**人话解释：** gapped 双层畴壁的预期两端口电导（2 模/谷 × 2 自旋 = 4 前进通道）。

**定义：** 每谷每自旋 2 条模（来自 $\Delta N_\nu=2$）→ 两端口 $G=4e^2/h$。

**测量什么：** 畴壁态是否存在、是否弹道。

**不测量什么：** 谷保护（弹道 ≠ 谷保护，E13 明确区分）。

**常见误用：** 用 $4e^2/h$ 当"谷保护已证"的代理指标。

**与用户目标关系：** 输运数值的 baseline 判据（若算得远小于 4e²/h，需解释是谷间散射还是接触/无序效应）。

## Benchmark 1：ZMM 2013 LSW 紧束缚

- 任务：复现 gapped 双层 AB/BA 畴壁每谷 2 条边缘态/自旋。
- 平台：紧束缚（t=2.8 eV, t_⊥=0.4 eV, V=0.5 eV, 200 晶胞超胞）。
- 基线：ZMM 2013 原文（每 K/K′ 谷各 2 条/自旋；Landauer 电导可达 $Ne^2/h$）。
- 指标：边界态数目（每谷每自旋）、色散。
- 可复现状态：参数给全，可作 tbplas 基准。
- 与用户资产关系：tbplas 直接对标。

## Benchmark 2：E9 Huang 2018 mTBG LDOS

- 任务：复现 mTBG 畴壁隙内双线 LDOS 增强 + 高能 ±250 meV 鞍点。
- 平台：连续模型局域带近似 + 线性四面体法（github tflovorn）。
- 基线：E9 SI 参数（w≈0.45 eV、2u≈60 meV、r_DW={0,9.4 nm}、r_AB/BA={±16 nm,0}、鞍点 ±256 meV）。
- 指标：双线形态、鞍点能量、电场开关。
- 可复现状态：参数已给全，tbplas 可对标。

## Benchmark 3：E13 Verbakel 2021 FFT QPI

- 任务：复现"defect-free 网络无 intervalley 斑、加缺陷出现斑"的判据。
- 平台：实空间 LDOS → 2D FFT（TBPM 可算）。
- 基线：三对照（pristine HOPG / H 缺陷 HOPG / TBG 网络）。
- 指标：(√3×√3)R30° 斑有/无。
- 可复现状态：需在 TB 模型中引入原子缺陷 + 计算 LDOS 后 FFT。

## Summary Table / 汇总表

| Metric / Benchmark | Type | 人话解释 | What it tests | Common baseline | Risk | Status |
|---|---|---|---|---|---|---|
| 谷陈数 $N_\nu$ | metric | 单谷几何相位整数 | 畴壁边界模数 | ZMM 2013 $\pm1$ | 与 $\Delta N_\nu$ 混 | source_checked |
| 谷霍尔电导 $\sigma_{xy}^V$ | metric | 谷分辨横向流 | 谷流 | $N_\nu e^2/h$ | 当严格平台 | source_checked |
| intervalley 指纹 | metric | FFT 斑有/无 | 谷保护 | Verbakel 2021 | 当绝对零 | source_checked |
| $4e^2/h$ 通道计数 | metric | 畴壁预期电导 | 存在性/弹道 | 2 模×2 自旋 | 当谷保护代理 | source_checked |
| ZMM 2013 LSW | benchmark | 每谷 2 模复现 | 谷陈数/边界模 | 原文参数 | 谷守恒近似 | 可复现 |
| E9 LDOS | benchmark | mTBG 双线复现 | LDOS/鞍点 | E9 SI 参数 | 局域带近似 | 可复现 |
| E13 FFT QPI | benchmark | intervalley 斑复现 | 谷保护判据 | 三对照 | 需建模缺陷 | 待做 |

*Last updated: 2026-09-02*
