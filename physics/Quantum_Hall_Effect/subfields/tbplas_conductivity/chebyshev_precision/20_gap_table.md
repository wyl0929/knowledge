<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27 23:50:54
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-27 23:50:59
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/chebyshev_precision/20_gap_table.md
 * @Description  :
-->
<!--
Field: 切比雪夫迭代浮点精度问题
Parent: tbplas_conductivity
Created date: 2026-06-27
-->

# 20 Gap Table / 缺口表

Last updated: 2026-06-27

## 缺口分类标准

| 标签 | 含义 |
|:---:|------|
| **confirmed** | 已被实验或分析明确证实的知识缺口 |
| **suspected** | 有线索但未严格证实的缺口 |
| **weak** | 可能只是误解或定义不清的"假缺口" |
| **not-a-gap** | 已被后续工作填补或证伪 |

---

## 缺口一览

### G-01: C++ 层 quad precision KPM 实现缺失 ⚫ confirmed

| 项目 | 内容 |
|------|------|
| 缺口 | tbplas 的 KPM Chebyshev 迭代仅在 double 精度下实现，无法在 M≥4096 时保持精度 |
| 分类 | **confirmed** |
| 为什么重要 | 这是噪声源所在层级（Phase M2 确认），只有在此层修复才能根治 |
| 最小验证 | 实现 `__float128` 或 `long double` 版 Chebyshev 三项递推，测试 M=4096 下 σ_xy 基线偏移是否消除 |
| 阻塞因素 | 需要修改 C++ 源码；`__float128` 在部分架构上性能未验证；接口兼容性 |
| 相关资产 | tbplas C++ 源码 (`kpm.cpp`), SLURM 集群 |

### G-02: Lorentz 核最优 λ 值未确定 ⚫ confirmed

| 项目 | 内容 |
|------|------|
| 缺口 | Lorentz 核参数 λ 对条件收敛的定量改善尚未系统性扫描 |
| 分类 | **confirmed**（但 gamma_mu_sim T4 正在填补） |
| 为什么重要 | 如果 λ≥4 能在不修改 C++ 的前提下将安全 M 推至 4096，这是最低成本的修复 |
| 最小验证 | gamma_mu_sim T4–T5：扫描 M=64→8192, λ=2,3,4,6,8，拟合 RMS(M,λ) 标度面 |
| 阻塞因素 | T4 扫描正在运行；需要计算资源 |
| 相关资产 | gamma_mu_sim 项目 |

### G-03: 缺乏与其他 KPM 实现的横向对比 ⚫ suspected

| 项目 | 内容 |
|------|------|
| 缺口 | 不知道问题是 tbplas 特有的还是 KPM 方法普遍的 |
| 分类 | **suspected** |
| 为什么重要 | 决定修复策略的普适性和文章的可发表性 |
| 最小验证 | 在至少一个其他 KPM 代码（如 GPAW 的 KPM 模块）中测试 M≥4096 的 Chebyshev 迭代精度 |
| 阻塞因素 | 需要安装和学习其他代码 |
| 相关资产 | 无（需要获取外部代码） |

### G-04: 混合精度方案未探索 ⚫ suspected

| 项目 | 内容 |
|------|------|
| 缺口 | 不知道能否在 Chebyshev 递推中用 quad、在向量-矩阵乘法和累加中用 double |
| 分类 | **suspected** |
| 为什么重要 | 可能找到精度和性能的最优平衡点 |
| 最小验证 | 在 gamma_mu_sim 中模拟混合精度：μ 用 quad 精度生成（模拟 quad KPM），Γ 和求和用 double |
| 阻塞因素 | 需要 gamma_mu_sim 扩展 |
| 相关资产 | gamma_mu_sim 项目 |

### G-05: 缺少对复杂体系（多层转角石墨烯等）M=2560 充分性的定量评估 ⚪ weak

| 项目 | 内容 |
|------|------|
| 缺口 | 当前实用窗口 M≤2560 是基于单层石墨烯 QHE 的结论；对多层转角体系，M=2560 的能量分辨率是否足够解析所有 LL 特征 |
| 分类 | **weak** |
| 为什么重要 | 如果 M=2560 对目标体系不够，实用窗口的约束会更紧 |
| 最小验证 | 对多层体系做 M 收敛性测试（M=1024→2560），看 QHE 平台是否在 M=2560 前收敛 |
| 阻塞因素 | 需要运行多层体系的大规模 Kubo-Bastin 计算 |
| 相关资产 | SLURM 集群, tbplas |

---

## 非缺口（已填补或证伪）

| 项目 | 原状态 | 现状态 | 填补/证伪来源 |
|------|:---:|:---:|------|
| "Chebyshev 正交性是否在大 M 下丧失" | suspected gap | **not-a-gap** | Phase A：正交性保持良好 |
| "Jackson 核是否在高 M 退化" | suspected gap | **not-a-gap** | Phase B：核函数正常 |
| "rescaling 是否导致边缘泄漏" | suspected gap | **not-a-gap** | Phase C：rescale=-1 正确 |
| "Anderson 无序能否修复精度" | suspected gap | **not-a-gap** | Phase H：证伪 |
| "Kahan 求和能否根治" | suspected gap | **not-a-gap** | Phase M2：累加非瓶颈 |
| "δμ 是否有系统性偏差" | suspected gap | **not-a-gap** | Phase L/bias：零均值随机噪声 |

---

## 缺口优先级排序

| 排序 | Gap | 理由 |
|:---:|------|------|
| 🥇 | G-02 Lorentz λ 最优值 | 最低成本、最快产出、正在执行 |
| 🥈 | G-01 C++ quad precision | 根治性方案，但投入大 |
| 🥉 | G-04 混合精度 | 可能找到甜点 |
| 4 | G-03 跨代码对比 | 提升问题普适性 |
| 5 | G-05 复杂体系 M=2560 充分性 | 应用验证 |
