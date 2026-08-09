<!--
Field: 切比雪夫迭代浮点精度问题
Parent: tbplas_conductivity
Created date: 2026-06-27
-->

# 22 Project Candidates / 候选项目卡片

Last updated: 2026-06-27

---

## PC-01: gamma_mu_sim — Γ-μ 随机游走完整扫描 🥇 优先

| 维度 | 内容 |
|------|------|
| **一句话** | 在纯 Python 下完成 Γ-μ 双重求和的系统性数值验证，定量确定安全 M 窗口和最优核参数 |
| **对应 gap** | G-02 |
| **当前状态** | 🟡 执行中（T1✓ T2✓ T4 running） |
| **目标** | 扫描 M=64→8192, 3 种核模型 × 2 种求和方法 × float32/64, 拟合标度律 RMS(M, kernel, λ) |
| **Baseline** | sequential + clean (无核) → worst case；mpmath dps=50 ground truth |
| **Metrics** | RMS error vs M, 标度指数 α, Lorentz 核压制比 |
| **Success criteria** | 确定 Lorentz λ 使 M=4096 时 RMS < 10^{-3}（相对物理信号 ~2e²/h）的最低 λ 值 |
| **Stop criteria** | 如果所有核模型在 M=4096 下 RMS > 0.1，则核加权不足以修复，必须走 quad precision 路线 |
| **时间估计** | 1–2 天（代码已就绪） |
| **下一步动作** | 等待 T4 扫描完成 → T5 标度律拟合 → T6 θ 扫描 → T7 报告 |
| **operational_status** | `in_progress` |

### 操作化契约 (Operationalization Contract)

| 要素 | 定义 |
|------|------|
| **输入集合** | M ∈ {64, 96, 128, 192, 256, 384, 512, 768, 1024, 1536, 2048, 2560, 3072, 4096, 6144, 8192}；θ = π/4 (固定)；kernel ∈ {clean, jackson, lorentz_λ2, lorentz_λ4, lorentz_λ6, lorentz_λ8}；trial=1 per (M, kernel) |
| **目标变换** | S = Σ_{m,n} Re[Γ_{mn}] · μ_{mn}；ΔS = |S - S_ref|；S_ref = math.fsum (Shewchuk exact rounding) |
| **编码/读出** | Γ 矩阵按解析公式向量化生成 (complex128)；μ 矩阵按核模型合成 (float64)；乘积用 np.real(Γ).ravel() * μ.ravel() 预计算 |
| **指标定义** | RMS(M) = sqrt(mean(ΔS² across trials))；α = d(log RMS)/d(log M) |
| **失败事件** | S_f32/S_f64 比值异常偏离 1（说明求和层有新问题）；RMS 非单调（说明噪声模型不适用） |
| **后选择政策** | S_ref ≈ 0 的点（信号零点）排除相对误差，仅用绝对误差 |
| **Baseline 公平性** | 所有方法使用相同 Γ 和 μ_true；仅 μ_noisy 的噪声种子不同（但固定种子保证可复现） |
| **阳性结果边界** | Lorentz λ=4 使 M=4096 时 RMS 降低 ≥ 10× vs clean |
| **阴性结果边界** | 所有核模型在 M=4096 时 RMS ≥ 0.5 e²/h（核加权不足以修复） |

---

## PC-02: tbplas C++ Quad Precision KPM 原型 🥈

| 维度 | 内容 |
|------|------|
| **一句话** | 在 tbplas C++ 的 KPM Chebyshev 迭代中引入 quad precision（__float128 或 long double），验证 M=4096 下 σ_xy 基线偏移是否消除 |
| **对应 gap** | G-01 |
| **当前状态** | ⚪ 未开始 |
| **目标** | 最小可行修改：仅修改 `kpm.cpp` 中的 Chebyshev 三项递推内循环，用 quad precision 计算 T_n，其余保持 double |
| **Baseline** | 当前 double 实现，M=4096 时 σ_xy 偏离量子化平台 ~0.5 e²/h |
| **Metrics** | σ_xy(M=4096) vs 量子化平台值 (2, 6, 10 e²/h) 的偏差 |
| **Success criteria** | M=4096 时偏差 < 0.05 e²/h（平台可辨识） |
| **Stop criteria** | 如果 __float128 性能下降 > 10×，则方案不实用，转向混合精度 |
| **时间估计** | 2–3 天 |
| **下一步动作** | 1) 定位 kpm.cpp 中 Chebyshev 递推循环 2) 引入 `__float128` 类型 3) 本地编译测试 4) 集群 M=4096 计算 |
| **operational_status** | `planned` |

### 操作化契约

| 要素 | 定义 |
|------|------|
| **输入集合** | 单层石墨烯, B=10T, M=4096, θ 网格=32, rescale=-1, Jackson 核, rs=1 |
| **目标变换** | σ_xy(M=4096, quad) − σ_xy(M=4096, double) → 量化改善幅度 |
| **编码/读出** | `__float128 T_n, T_{n-1}, T_{n-2}`；结果转回 double 存储 |
| **指标定义** | Δσ = |σ_xy(quad) − σ_xy_plateau| / (e²/h) |
| **失败事件** | 编译失败（__float128 不支持当前工具链）；运行时 NaN（精度混合边界 bug） |
| **后选择政策** | 不适用 |
| **Baseline 公平性** | 除递推精度外，所有参数相同 |
| **阳性结果边界** | Δσ < 0.05 e²/h @ M=4096 |
| **阴性结果边界** | Δσ > 0.1 e²/h @ M=4096（quad 未根治，可能还有其他噪声源） |

---

## PC-03: KPM 浮点精度方法论文章 🥉

| 维度 | 内容 |
|------|------|
| **一句话** | 将 Phase A–M 诊断过程撰写成系统性方法论文章，填补 KPM 文献中浮点精度分析的空白 |
| **对应 gap** | G-03（如扩展跨代码对比） |
| **当前状态** | ⚪ 未开始 |
| **目标** | 可发表的方法论文章（目标期刊：Comp. Phys. Commun. 或 J. Chem. Phys.） |
| **Baseline** | 已完成的 Phase A–M 证据链 + gamma_mu_sim 结果 |
| **Metrics** | 接受/发表 |
| **Success criteria** | 文章清晰呈现"诊断方法论 + 根因机制 + 实用建议"三层结构 |
| **时间估计** | 1–2 周写作 + 补充实验 |
| **阻塞因素** | G-03（如要包含跨代码对比）需先完成 |
| **operational_status** | `planned` |
