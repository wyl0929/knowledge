<!--
Field: 量子谷霍尔效应与谷电子学（Quantum Valley Hall Effect & Valleytronics）
Mode: full_onboarding
Domain archetype: science_technical
Created date: 2026-09-02
-->

---
document_type: mvp_experiment_plan
schema_version: v1.0-rc2
field: "量子谷霍尔效应与谷电子学（QVH / Valleytronics）"
last_updated: 2026-09-02
---

# 23 最小可行实验计划

Last updated: 2026-09-02

## Gate requirements / 门控要求

已完成 Core Claims Gate 与 Operationalization Gate（`17_claims_evidence_ledger.md`）。本 MVP 对应 P-001 的第一阶段，operational_status = **provisional** → 生成**消歧型 MVP**：先验证"谷分辨读出"这一测量定义与任务可行性，而非证明最终贡献。

## 用人话说这个 MVP

这个 MVP 只回答一个问题：**你的方法栈能不能在均匀 gapped 双层里算出"单谷谷陈数 = ±1"？**

- 结果 A（算出 ±1、符号随 Δ 反号）：谷分辨读出打通，进入 P-001 第二阶段（AB/BA 畴壁每谷 2 模）。
- 结果 B（算出的数不对、或投影不稳定）：测量定义有 bug，先在均匀体系里把谷投影修对，**不进入畴壁/缺陷阶段**。
- 结果 C（投影在均匀体系即失效）：改实空间谷算符/谷极化算符替代，或退回纯 k 空间分类；若 1 个月仍无解，止损改题。

## Operationalization Contract / 任务可操作化契约

### 声称要验证的任务

谷分辨读出能力：能否在紧束缚 + 数值下，把单谷 Berry 曲率积分成单谷谷陈数 $N_\nu=\pm1$。

### 输入对象与允许输入集合

均匀 gapped Bernal 双层石墨烯紧束缚模型：层内最近邻 hopping、层间耦合 $\gamma_1\approx0.4$ eV、垂直场开出的层间势差 $\Delta$（符号可控）。允许输入集合 = {Δ>0, Δ<0} 两个方向 + 若干网格密度。规模 M≤2560、rescale=−1。

### 编码、控制、演化、解码与读出流程

```text
输入：双层 TB 哈密顿量 H(Δ)
  -> 编码：谷投影 P_K / P_K'（k 空间谷窗口 或 实空间谷算符，本 MVP 的核心待验证项）
  -> 演化：对角化（小超胞）得布洛赫波函数
  -> 解码/读出：单谷 Berry 曲率 Ω_ν(q) 离散积分（Fukui-Hatsugai-Suzuki）
  -> 指标计算：N_ν 数值 vs 解析 ±1
  -> 结论：谷分辨读出是否打通
```

### 目标变换

从"双层 TB 能带 + Δ"到"单谷谷陈数 N_ν"。

### 指标定义

- 指标：单谷谷陈数 $N_\nu$（数值）。
- 计算方式：单谷区域 Berry 曲率离散积分（Fukui-Hatsugai-Suzuki 或等价 Wilson loop）。
- 真正测到什么：单谷 Berry 曲率积分是否等于解析 ±1。
- 没测到什么：总 Chern 数（恒 0）；谷保护（本 MVP 不做散射/缺陷）；畴壁边界模（第二阶段）。
- 依赖假设：谷投影在均匀体系良定义（这是本 MVP 要验证的）。

### 失败事件、泄漏、损失与后选择政策

- 谷投影失败/数值不对的算例如实记录，不因"某个网格恰好对"就宣称打通。
- 报告 Δ>0 与 Δ<0 两个符号（$N_\nu$ 应反号），漏报任一符号即失败事件。
- 无后选择：不做"只保留收敛算例"。
- 性能口径：只报 unconditional（全算例、不分后选择）结果；不单独报 conditional（后选择存活算例）结果——两者需区分报告，避免用后选择美化。

### Baseline 公平性

解析基线 $N_\nu=-\nu\,\mathrm{sgn}(\Delta)=\pm1$（ZMM 2013，📜Q）。数值用同一 TB 参数、同一网格；不比"更细网格才算对"。

### 阳性结果能证明什么

谷分辨读出可用；数值上复现单谷谷陈数 = ±1。

### 阳性结果不能证明什么

不能证明谷霍尔电导严格量子化；不能证明畴壁边界模数（那是第二阶段）；不能证明谷保护。

### 阴性结果意味着什么

谷投影方法或离散积分实现有 bug；先修 bug，不判理论。

operational_status: provisional

## 最小模型 / 核心方程

gapped 双层单谷两带有效模型（ZMM 2013）作为解析锚点：

$$
\Omega_\nu(\mathbf q)=\mp\frac{2\nu\gamma\Delta\, q^2}{(q^4+\gamma^2\Delta^2)^{3/2}},\qquad N_\nu=-\nu\,\mathrm{sgn}(\Delta)=\pm1,\qquad \gamma=\frac{t_\perp}{(\hbar v_F)^2}
$$

数值侧用全双层紧束缚（非两带近似），验证谷投影 + 离散积分能收敛到 ±1。

实验流程：

```text
输入：双层 TB H(Δ>0 与 Δ<0)
  -> 对角化得本征态
  -> 谷投影 → 单谷 Berry 曲率离散积分
  -> 对比基线：解析 ±1
  -> 指标：N_ν 数值
  -> 成功（=±1）或止损判断
```

## 实验计划

### MVP 标题：单谷谷陈数数值读出的消歧实验

### 研究问题：现有 tbplas/Kubo-Bastin 能否（经谷投影改造后）算出单谷谷陈数 ±1？

### 最小可行假设：k 空间谷窗口（或实空间谷算符）能在均匀 gapped 双层上把 Berry 曲率分解到单谷，并积分得 ±1。

### 输入：gapped Bernal 双层 TB（γ₁、Δ、晶胞、k 网格）。

### 需要实现的代码：谷投影（P_K/P_K'）+ 单谷 Berry 曲率离散积分；基于 graphene.py 扩展双层 + Δ。

### 需要的数据：无外部数据（自产 TB 计算）。

### 对比基线：解析 $N_\nu=-\nu\,\mathrm{sgn}(\Delta)=\pm1$。

### 评价指标：$N_\nu$ 数值 vs 解析 ±1；Δ 反号时 $N_\nu$ 反号。

### 预期关键图：单谷 Berry 曲率 $\Omega_\nu(q)$ 在布里渊区的热图（K/K′ 附近正负相反），积分 = ±1。

### 第一周计划（可交给 coding agent 的中文任务单）

1. 读 QHE field `subfields/tbplas_conductivity/kubo_bastin.h` 与 tbplas 源码，确认是否已有动量空间/谷分解接口（对应 C-007 code audit，输出一句话结论）。
2. 用 graphene.py 扩展出 gapped Bernal 双层 TB：层内最近邻 + 层间 $\gamma_1$ + 层间势差 $\Delta$（Δ 可正可负）。
3. 实现 k 空间谷投影：在单谷区域（K 或 K′ 附近）对布洛赫态做窗口投影。
4. 实现单谷 Berry 曲率离散积分（Fukui-Hatsugai-Suzuki），输出 $N_K$、$N_{K'}$。
5. 跑 Δ=+Δ₀ 与 Δ=−Δ₀ 两个算例，核对 $N_K=\mp1$、$N_{K'}=\pm1$。

### 第一个月计划

- 打通后进入 P-001 第二阶段：AB/BA 畴壁超胞，数隙内边界模（每谷每自旋 = 2），对标 ZMM 2013 LSW。
- 若投影不稳定，改实空间谷算符/谷极化算符，重跑 MVP。

### 成功标准：

$N_K$、$N_{K'}$ 数值 = ±1（误差在离散误差内），且 Δ 反号 → 符号反号；两个符号方向都报告。

### 止损标准：

若 1 个月内（含排 bug）谷投影在**均匀体系**仍无法稳定给 ±1，或结论依赖"恰好某网格"，则止损：标 C-007 为 blocked，退回纯 k 空间分类路线，不做无序/畴壁阶段。

### 成功后的下一步

进入 P-001 第二阶段（畴壁边界模 + 单缺陷 FFT 软保护），并回填谷分辨读出为可复用工具（`99_update_log.md` 记录）。

### 失败后的下一步

改题：转向 P-002（三层 C_v 约定核对，纯文献），或与理论合作者确认谷投影先例。

## 实验记录

| 日期 | 动作 | 结果 | 决策 | 下一步 |
|---|---|---|---|---|
|  |  |  | 继续 / 修改 / 停止 |  |
