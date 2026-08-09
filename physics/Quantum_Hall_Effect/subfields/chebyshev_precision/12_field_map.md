<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27 23:48:07
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-27 23:48:11
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/chebyshev_precision/12_field_map.md
 * @Description  :
-->
<!--
Field: 切比雪夫迭代浮点精度问题
Parent: tbplas_conductivity
Created date: 2026-06-27
-->

# 12 Field Map / 问题链与方法谱系

Last updated: 2026-06-27

## 问题在更大链条中的位置

```
凝聚态物理
  └── 拓扑物态
        └── 量子霍尔效应 (QHE)
              └── 数值计算方法
                    ├── 对角化（小体系）
                    ├── TBPM/KPM（大体系）         ← 我们在这里
                    │     ├── DOS 计算
                    │     ├── DC 电导率 (Kubo)
                    │     └── Hall 电导率 (Kubo-Bastin)  ← 本子方向聚焦
                    │           ├── 公式推导与实现
                    │           ├── 收敛性（M, θ 网格, 无序）
                    │           └── 浮点精度 ← 本 field pack 主题
                    └── DMRG / 张量网络（强关联）
```

---

## 核心问题链

```
Q1: Kubo-Bastin 双重求和需要多大 M 才能收敛？
  ├── A1: 理论要求 M ≥ 4096（PRL 114.116602）
  └── 触发 Q2

Q2: 为什么 M ≥ 3072 时 σ_xy 出现基线偏移？
  ├── H_A: Chebyshev 正交性丧失 → ❌ Phase A 排除
  ├── H_B: Jackson 核退化 → ❌ Phase B 排除
  ├── H_C: 能谱边缘泄漏 → ❌ Phase C 排除
  ├── H_D: double 精度单次不够 → ❌ Phase D 排除（累积才是）
  ├── H_θ: θ 积分奇异性 → ❌ Phase θ 排除
  ├── H_Γ: Γ 矩阵计算误差 → ❌ Phase Γ 排除
  ├── H_μ: μ 矩阵 M 依赖性 → ❌ Phase μ 排除
  ├── H_J: Jackson 核 M 依赖性 → ❌ Phase J 排除
  ├── H_bias: δμ 系统性偏差 → ❌ Phase bias 排除
  └── 触发 Q3

Q3: (Phase M) 噪声源在哪里？放大机制是什么？
  ├── M1 ✅: ΔS = ΣΓ·η 线性关系确认（噪声注入模型正确）
  ├── M2 ✅: 求和精度非瓶颈（S_f32≈S_f64），δμ 在 C++ KPM 迭代层
  ├── M3 ✅: 高 |Γ| 项主导 S（Γ 加权确认）
  └── 根因链确立 → 触发 Q4

Q4: 如何修复？
  ├── P0: C++ quad precision KPM 迭代（根治）
  ├── P1: Lorentz 核 λ≥4（压制高索引项）
  ├── P2: 实用窗口 M≤2560（当前最可行）
  └── P3: 探索其他 KPM 库的实现
```

---

## 方法谱系：浮点精度分析

### 诊断方法论

```
诊断层级
├── L0: 现象观测
│   └── σ_xy(M) 基线偏移曲线
├── L1: 假说生成与排除
│   ├── 机制假说（H_A–H_bias, 9 个）
│   └── 判据实验设计（每假说至少一个决定性实验）
├── L2: 数值模拟验证 (gamma_mu_sim)
│   ├── Γ 矩阵合成（解析公式，可控量级）
│   ├── μ 矩阵合成（Chebyshev 矩 + 可控噪声）
│   ├── 求和引擎（sequential / Kahan / 高精度基准）
│   └── 标度律拟合（RMS ∝ M^α）
└── L3: 源码级审计
    ├── tbplas C++ kpm.cpp / kubo_bastin.h 追踪
    └── 浮点运算路径追踪
```

### 数值方法工具箱

| 方法 | 用途 | 在本问题中的应用 |
|------|------|------|
| 假说-排除法 | 系统化根因诊断 | Phase A–M 的 9→1 排除链 |
| 噪声注入验证 | 确认因果关系 | Phase M1: 人工 η → ΔS 线性响应确认 |
| f32/f64 对照 | 区分噪声源层级 | Phase M2: S_f32≈S_f64 → 噪声不在累加层 |
| Γ 加权分析 | 确认放大机制 | Phase M3: 高 |Γ| 项对 S 的贡献占比 |
| 标度律拟合 | 外推误差行为 | RMS ∝ M^α，实测 α≈1 |
| mpmath 高精度基准 | Ground truth | 作为"无误差"参考值 |
| Kahan 补偿求和 | 降低累加舍入 | 与 sequential 对比评估累加层贡献 |
| 核函数压制 | 降低高索引权重 | Jackson / Lorentz 核对条件收敛的改善 |

---

## 核心假设与依赖

| 假设 | 状态 | 验证方式 |
|------|:---:|------|
| Γ 矩阵可由解析公式精确计算 | ✅ confirmed | 与 mpmath 对比一致 |
| μ 矩阵噪声为零均值随机变量 | ✅ confirmed | Phase L: pos_frac=0.4997 |
| 随机游走 RMS ∝ √N·ε·‖Γ‖ | ✅ confirmed | Phase M1: dS_obs/dS_pred=1.000±0.001 |
| 核加权不改变 δμ 本身，只压制 Γ 权重 | ✅ confirmed | Phase B/J |
| C++ 和 Python 的 Chebyshev 迭代噪声行为一致 | ⚠️ plausible | 未直接验证（C++ 无 quad precision 对照） |

---

## 成熟度评估

| 子问题 | 成熟度 | 说明 |
|------|:---:|------|
| 根因确认（δμ × Γ → 条件收敛） | 🟢 成熟 | Phase M 闭环验证完成 |
| 噪声源精确定位（C++ KPM 迭代层） | 🟢 成熟 | M2 确认，排除累加层 |
| 实用窗口（M ≤ 2560） | 🟢 成熟 | 多次独立测试确认 |
| Lorentz 核修复效果 | 🟡 初步 | gamma_mu_sim 正在扫描（T4） |
| Quad precision 修复 | 🔴 未实现 | 需要修改 C++ 源码 |
| 其他 KPM 库对比 | ⚪ 未探索 | 可与 GPAW/Siesta KPM 实现对比 |

---

## 与邻近问题的关系

| 邻近问题 | 关系 | 区分 |
|------|------|------|
| KPM Chebyshev 递推数值稳定性（一般理论） | 强相关 | 一般理论关注 $T_n(x)$ 的正交性丧失（Clenshaw 递推）；本问题关注的是 KPM 特定场景（随机向量 + 稀疏矩阵乘法）的噪声 |
| 大规模矩阵乘法的浮点精度 | 相关 | H·ψ 的稀疏矩阵乘法也产生舍入误差，但量级远小于 Chebyshev 迭代累积 |
| 随机游走与中心极限定理 | 方法论基础 | 双重求和 → 大量独立同分布随机变量之和 → CLT → RMS ∝ √N |
