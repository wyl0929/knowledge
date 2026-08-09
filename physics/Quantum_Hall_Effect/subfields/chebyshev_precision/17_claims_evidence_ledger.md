<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27 23:50:52
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-27 23:50:54
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/chebyshev_precision/17_claims_evidence_ledger.md
 * @Description  :
-->
<!--
Field: 切比雪夫迭代浮点精度问题
Parent: tbplas_conductivity
Created date: 2026-06-27
-->

# 17 Claims Evidence Ledger / 论断-证据台账

Last updated: 2026-06-27

## Gate verdict / 门控结论

- **概念边界状态**：`resolved` — 11_term_disambiguation.md 已完成 6 组概念边界
- **中心论断状态**：`confirmed` — 根因假说（随机游走）通过 Phase M 三通道闭环验证
- **任务可操作化状态**：`operational` — gamma_mu_sim 提供完整的数值验证管线

---

## 排除类论断（Phase A–J, bias）

### CL-X01: Chebyshev 正交性丧失假说 → ❌ 排除

| 项目 | 内容 |
|------|------|
| 论断 | Chebyshev 三项递推在大 M 时丧失正交性，$\langle T_m\|T_n\rangle$ 偏离 $\delta_{mn}$，导致 $\mu_{mn}$ 失真 |
| 假说类型 | mechanism hypothesis |
| 裁决 | **excluded** |
| 排除实验 | Phase A：直接计算 $\langle T_m\|T_n\rangle$ 矩阵，在 M≤4096 下仍接近单位阵 |
| 排除日期 | 2026-06-22 |
| 排除标准 | 如果正交性丧失，非对角线元素应显著偏离 0，但实测 < 10^{-12} |
| 对下游的影响 | 排除此假说意味着修复方向不应是"改进 Chebyshev 递推格式" |

### CL-X02: Jackson 核退化假说 → ❌ 排除

| 项目 | 内容 |
|------|------|
| 论断 | Jackson 核 $g_n(M)$ 在大 M 时数值退化（如末端異常衰减），导致加权出错 |
| 假说类型 | mechanism hypothesis |
| 裁决 | **excluded** |
| 排除实验 | Phase B：直接绘制 $g_n(M)$ 曲线，M=64→4096，核函数行为连续、单调、无异常 |
| 排除日期 | 2026-06-23 |

### CL-X03: 能谱边缘泄漏假说 → ❌ 排除

| 项目 | 内容 |
|------|------|
| 论断 | rescale 设置不当，部分特征值超出 [-1,1] → Chebyshev 域外求值 → 发散或畸变 |
| 假说类型 | mechanism hypothesis |
| 裁决 | **excluded** |
| 排除实验 | Phase C：确认 `rescale=-1` 自动带宽检测正确覆盖全谱 |
| 排除日期 | 2026-06-23 |
| 注意 | 手动设置 rescale=9.0（<< 真实带宽 ~20 eV）确实导致 NaN，但那是另一独立问题 |

### CL-X04: double 精度不足假说 → ❌ 排除（作为单因）

| 项目 | 内容 |
|------|------|
| 论断 | double (53-bit mantissa) 对 KPM 迭代单次运算不够精确 |
| 假说类型 | mechanism hypothesis |
| 裁决 | **excluded**（作为单因） |
| 排除实验 | Phase D：单次 Chebyshev 迭代的相对误差 ~10^{-15}，在合理范围内 |
| 排除日期 | 2026-06-24 |
| 重要澄清 | double 的**累积**效应是根因的一部分，但"单次不够"被排除 |

### CL-X05: θ 积分奇异性假说 → ❌ 排除

| 项目 | 内容 |
|------|------|
| 论断 | $\sin^{-3}\theta$ 因子在 θ→0,π 的奇异性导致数值发散 |
| 假说类型 | mechanism hypothesis |
| 裁决 | **excluded** |
| 排除实验 | Phase θ：奇异性可处理（被 $f(\cos\theta)$ 因子正则化），非基线偏移来源 |
| 排除日期 | 2026-06-24 |

### CL-X06: Γ 矩阵计算精度假说 → ❌ 排除

| 项目 | 内容 |
|------|------|
| 论断 | Γ 矩阵的解析公式在数值求值时精度不足 |
| 假说类型 | mechanism hypothesis |
| 裁决 | **excluded** |
| 排除实验 | Phase Γ：Γ 矩阵可解析计算，与 mpmath 高精度对比一致 |
| 排除日期 | 2026-06-25 |

### CL-X07: μ 矩阵 M 依赖性假说 → ❌ 排除

| 项目 | 内容 |
|------|------|
| 论断 | $\mu_{mn}$ 在 clean 体系下随 M 有系统性变化 |
| 假说类型 | mechanism hypothesis |
| 裁决 | **excluded** |
| 排除实验 | Phase μ：$\mu_{mn}$ 在给定 E0 下由 Chebyshev 多项式确定，与 M 无关 |
| 排除日期 | 2026-06-25 |

### CL-X08: Jackson 核 M 依赖性假说 → ❌ 排除

| 项目 | 内容 |
|------|------|
| 论断 | Jackson 核的归一化或形状随 M 有系统性漂移 |
| 假说类型 | mechanism hypothesis |
| 裁决 | **excluded** |
| 排除实验 | Phase J：核函数随 M 的变化是预期的（更密的采样），非系统性漂移 |
| 排除日期 | 2026-06-25 |

### CL-X09: δμ 系统性偏差假说 → ❌ 排除

| 项目 | 内容 |
|------|------|
| 论断 | $\delta\mu_{mn}$ 有非零均值（系统性 Krylov 漂移），导致累加后定向偏移 |
| 假说类型 | mechanism hypothesis |
| 裁决 | **excluded** |
| 排除实验 | Phase bias/L：pos_frac = 0.4997（零均值），无 Krylov 漂移 |
| 排除日期 | 2026-06-26 |

---

## 确认类论断（Phase M）

### CL-C01: 噪声注入线性关系 → ✅ 确认

| 项目 | 内容 |
|------|------|
| 论断 | ΔS = ΣΓ·η 的线性关系成立，噪声 × Γ → 求和偏移的因果链完整 |
| 证据类型 | 直接数值实验 |
| 证据强度 | **confirmed** |
| 证据来源 | Phase M1：dS_obs/dS_pred = 1.000 ± 0.001, RMS ∝ σ^0.999 |
| 验证日期 | 2026-06-27 |
| 对下游判断的影响 | 确认 Γ 加权是噪声放大的核心机制 |

### CL-C02: 噪声源在 C++ KPM 迭代层 → ✅ 确认

| 项目 | 内容 |
|------|------|
| 论断 | δμ 噪声在 mu 矩阵构建过程（C++ KPM Chebyshev 迭代）中产生，而非后续累加 |
| 证据类型 | 对比实验 |
| 证据强度 | **confirmed** |
| 证据来源 | Phase M2：S_f32 ≈ S_f64，求和精度非瓶颈 |
| 验证日期 | 2026-06-27 |
| 对下游判断的影响 | 修复必须触及 C++ KPM 迭代层，Python 层后处理无效 |

### CL-C03: Γ 加权主导噪声 → ✅ 确认

| 项目 | 内容 |
|------|------|
| 论断 | 高 |Γ| 项（大 m,n 索引）对 S 的噪声贡献占主导 |
| 证据类型 | 分解分析 |
| 证据强度 | **confirmed** |
| 证据来源 | Phase M3：高 |Γ| 区域的噪声贡献远超低 |Γ| 区域 |
| 验证日期 | 2026-06-27 |
| 对下游判断的影响 | 核加权通过压制高索引项可部分缓解 |

### CL-C04: 条件收敛（非发散） → ✅ 确认

| 项目 | 内容 |
|------|------|
| 论断 | S(M) 是条件收敛的随机游走，不是发散级数；求和顺序影响结果 |
| 证据类型 | 求和策略对比 |
| 证据强度 | **confirmed** |
| 证据来源 | Phase L：Sequential vs Kahan 差异随 M 增大；S(M) 围绕真值随机游走 |
| 验证日期 | 2026-06-25 |
| 对下游判断的影响 | 将问题定性为"发散"会误导修复方向 |

---

## 推测类论断

### CL-S01: 其他 KPM 实现可能也有类似问题

| 项目 | 内容 |
|------|------|
| 论断 | GPAW、Siesta、pybinding 等代码的 KPM Chebyshev 迭代在 double 精度下也可能有类似的浮点累积问题 |
| 证据类型 | 类比推理 |
| 证据强度 | **suspected**（未经直接验证） |
| 验证需求 | 需要在至少一个其他 KPM 代码中复现 M≥4096 的基线偏移 |
| 如果证实 | 问题是 KPM 社区的普遍盲点，方法论文章的重要性显著提升 |
| 如果证伪 | 问题是 tbplas 特有的实现细节（如稀疏矩阵乘法实现），可针对性修复 |

### CL-S02: Quad precision 可以根治但性能代价可接受

| 项目 | 内容 |
|------|------|
| 论断 | C++ KPM 迭代改用 __float128 可以将噪声降低 ~10^{-34}，使 M≥4096 可用，且性能下降在 2–4× 内 |
| 证据类型 | 外推估算 |
| 证据强度 | **suspected**（未经实现验证） |
| 验证需求 | 需要在 tbplas 中实现 quad precision KPM 并测试 M=4096 |
| 已知限制 | __float128 是软件模拟，在某些架构上可能极慢；需要性能实测 |

### CL-S03: Lorentz λ=4 可将安全 M 推到 4096

| 项目 | 内容 |
|------|------|
| 论断 | Lorentz 核 λ≥4 的指数衰减足以压制高索引 Γ 贡献，使 M≤4096 的基线偏移降至可接受水平 |
| 证据类型 | gamma_mu_sim 模拟外推 |
| 证据强度 | **suspected**（T4 扫描进行中，结果待确认） |
| 验证需求 | T4 扫描完成 + T5 标度律拟合 |
| 如果证实 | 不用修改 C++ 即可安全使用 M≤4096 |

---

## 操作性建议

### CL-R01: 生产环境推荐配置

| 项目 | 内容 |
|------|------|
| 建议 | Kubo-Bastin 生产计算使用 M≤2560 + rescale=-1 + Jackson 核 |
| 证据基础 | Phase A–M 全链路 |
| 建议强度 | **strong recommendation** |
| 例外 | 如果需要 M≥3072，必须使用 Lorentz λ≥4 或 quad precision 并验证 |

### CL-R02: 不推荐 Anderson 无序作为精度修复

| 项目 | 内容 |
|------|------|
| 建议 | 不要用 Anderson 无序来"展宽"以降低 M 需求 |
| 证据基础 | Phase H：γ=0.27 eV 无效，γ≥0.5 破坏 QHE 信号 |
| 建议强度 | **strong recommendation** |
