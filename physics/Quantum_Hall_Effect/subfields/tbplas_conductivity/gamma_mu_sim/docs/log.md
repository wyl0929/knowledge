<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27 23:15:53
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-27 23:15:59
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/docs/log.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27
 * @FilePath     : gamma_mu_sim/docs/log.md
 * @Description  : Γ-μ 随机游走模拟 — 执行日志
-->

# Γ-μ 随机游走模拟 — 执行日志

---

<a id="ai-0628-0000"></a>
## AI: 0628_0000 — T5 核模型对比完成 + T7 可视化与报告完成

**涉及文件**:
- `src/t5_scan.py` — 新建：P1–P3 三核分析 + P4 Lorentz λ 扫描 + 综合排名
- `src/visualize.py` — 新建：8 张发表级图表
- `docs/report.md` — 新建：最终分析报告
- `README.md` — 新建：项目快速启动
- `output/data/P4_lorentz_lambda_scan.csv` — Lorentz λ 扫描 250 行
- `output/data/kernel_ranking.json` — 综合排名
- `output/figures/` — 8 张图表 (main_error_vs_M, scaling_law, gamma_heatmap, mu_heatmap, kernel_profiles, P4_alpha_vs_lambda, P_comprehensive_ranking, comprehensive_summary)
- `02_kubo_bastin_deep_dive.md` §7.7 — 追加 Python 模拟验证小节
- `/memories/kubo-bastin-convergence.md` — 追加验证结论

**变更说明**:

### T5 — 核模型对比
- **P1–P3**: 三核 α≈2.03–2.06（差异 < 3%），jackson 在 M=4096 时 RMS 最低 (1.09e-9)
- **P4 Lorentz λ 扫描**: λ=2,3,4,6,8 × M=64→4096 × 5 trials = 250 次测量，耗时 214s
  - α(λ) 不单调：λ=2 时 α=1.920, λ=4 时 α=2.111, λ=6 时 α=1.891
  - 无"甜点 λ"——所有 λ 均 α≈2，无法实现 α<0.1
  - RMS(M=8192) > RMS(M=4096) → 发散，随机游走不可消除
- **综合排名**: lorentz(λ=2)+sequential 最优 (RMS=9.27e-10)，但与前 5 名差异 < 15%
- **全部 4 条判据未通过**——核加权无法消除随机游走的假设被证伪

### T7 — 可视化与报告
- `visualize.py` 生成 8 张图，全部 exit 0
- `docs/report.md` 含标度指数表、综合排名、物理机制解释、实用建议
- `README.md` 含快速启动命令和目录结构
- 知识晋升：`02_kubo_bastin_deep_dive.md` §7.7 + `/memories/kubo-bastin-convergence.md`

**成功判据验证**:
- [x] visualize.py 所有函数可独立调用
- [x] 主图 error_vs_M 清晰展示 6 线
- [x] docs/report.md 含标度指数表 + 综合排名 + 实用建议
- [x] 02_kubo_bastin_deep_dive.md §7.7 已追加
- [x] README.md 含完整快速启动命令

**T5 判据验证（全部未通过——预期被证伪）**:
- [ ] P3: Lorentz λ=4 RMS(8192)=7.70e-9 > RMS(4096)=1.10e-9 → 发散 ❌
- [ ] P4: α 不随 λ 单调递减, 所有 λ 均 α≈2 → 无甜点 ❌
- [ ] 最优组合: lorentz(λ=2)+sequential, 非 Lorentz+Kahan ❌
- [ ] RMS(M=4096)=9.3e-10 > 1e-13 ❌

> **核心结论**: Lorentz 核无法消除随机游走——α 始终 ≈2。核加权仅改变前因子 β 而非标度指数。与 VBL Phase M 完全一致。

---

<a id="ai-0627-2345"></a>
## AI: 0627_2345 — T4 M 系统性扫描完成 + T3 基础验证完成

**涉及文件**:
- `src/t4_scan.py` — 新建：优化 M 扫描脚本（fsum 参考 + 向量化求和）
- `src/mu_matrix.py` — 修订：修复 scipy eval_chebyt 在 n≥2466 的 NaN（改用 cos(n·π/2) 解析式）
- `output/data/scan_results.csv` — 636 行完整扫描数据
- `output/data/S7_float32_scan.csv` — float32 对照 160 行
- `output/data/scaling_fit.json` — 6 线 α, β, R²
- `output/data/V1_gamma_scaling.csv` — Γ 量级验证
- `output/data/V2_mu_noise_stats.csv` — μ 噪声统计
- `output/data/V3_smallM_consistency.csv` — 小 M 方法一致性
- `output/figures/V1_gamma_scaling.png` — Γ 标度图

**变更说明**:

### T3 — 基础验证
- **V1**: max|Γ| ∝ M^{1.0049}, R²=0.999993 → Γ ∝ M 确认 (a∈[0.98,1.02] ✓)
- **V2**: δμ mean=-7.6e-20 ≈ 0 ✓, std=2.21e-16 ≈ ε ✓; Shapiro-Wilk p≈0 (large-N artifact, 5000/6.5M samples)
- **V3**: 所有 M≤128 时 abs_err < 10·ε·M² ✓; Kahan ≤ sequential 在 M≥128 时成立

### T4 — M 系统性扫描
- **6 线完整**: {clean,jackson,lorentz} × {sequential,kahan}, M=64→8192, 636 行
- **关键发现 — α ≈ 2.08 (非预期 1.0)**: Γ 元素 ∝ M，使得随机游走 RMS ∝ √(M²) × M·ε = M²·ε，即 α≈2
- **Kahan 无显著改善** (α 几乎相同): 噪声源自 δμ 而非求和舍入，与 VBL Phase M 诊断一致
- **三核 α 几乎相同** (~2.08): 核加权不改变主导的 M² 标度
- **float32 vs float64**: clean+seq M=1024 时 RMS=0.48 vs 5.6e-11 (~10¹⁰× 退化)
- **NaN 修复**: scipy eval_chebyt 在 n≥2466 时产生 NaN；改用 cos(n·π/2) 解析式（E0=0 时精确稳定）

**成功判据验证**:
- [x] T3: V1 a=1.0049∈[0.98,1.02] ✓; V2 mean≈0, std≈ε ✓; V3 阈值内 ✓
- [x] T4: 636 行完整，α≈2.08 全 6 线确认，float32 退化 10¹⁰× ✓
- [x] Pylance 零语法错误（mu_matrix.py 修改后）

**备注**:
- α≈2 是正确预期（非失败）: 先前的 α≈1 预期忽略了 Γ 元素随 M 线性增长
- 三核 α 无差异表明现有核模型（Jackson/Lorentz λ=4）不足以抑制 δμ 随机游走——需更强阻尼（λ≥8）或更高精度 μ 计算
- 见 STATUS.md 更新: plan §8.2 预期 α 值需修订

---

<a id="ai-0627-2315"></a>
## AI: 0627_2315 — T2 流水线与分析模块实现完成

**涉及文件**:
- `src/analysis.py` — 新建：rms_error, fit_scaling_law, n_trials_statistics, convergence_diagnostic
- `src/main.py` — 新建：run_single, run_M_scan, main() CLI 入口
- `output/data/scan_results.csv` — 冒烟测试输出（30 行）

**变更说明**:
- 实现 analysis.py：标度律拟合（np.polyfit log-log 线性回归）、RMS 统计、收敛诊断
- 实现 main.py：完整 M 扫描流水线，支持 --config / --small / --tiny 等 CLI 参数，KeyboardInterrupt 安全保存，tqdm 进度条
- 端到端冒烟测试通过（M=16→64, clean+sequential, 2 trials, 5θ）

**成功判据验证**:
- [x] `python src/main.py --tiny` exit 0
- [x] CSV 含全部预期列
- [x] fit_scaling_law 已知数据 α=2.0000, R²=1.000000
- [x] 冒烟测试 RMS 从 M=16(1.5e-14)→M=64(1.3e-13)，单调增长 ✓
- [x] Pylance 零语法错误

**备注**:
- mpmath 参考值用 mu_true（干净 μ），区别测量用 mu_noisy（含噪声），正确解耦噪声累积与核模型
- 相对误差在 S_ref≈0 时发散大——属正常（信号零点附近），不影响绝对误差分析

---

<a id="ai-0627-2300"></a>
## AI: 0627_2300 — T1 核心模块（5 modules）实现完成

**涉及文件**:
- `src/__init__.py` — 新建
- `src/config.py` — 新建：default_config, M_scan_grid
- `src/gamma_matrix.py` — 新建：gamma_element, gamma_matrix_full, gamma_matrix_theta_grid
- `src/mu_matrix.py` — 新建：mu_raw_clean, jackson_kernel(_vector), lorentz_kernel(_vector), apply_kernel, mu_noise_layer, mu_matrix_generate
- `src/summation.py` — 新建：sum_sequential, sum_kahan, sum_dispatch
- `src/reference.py` — 新建：gamma_element_mpmath, sum_exact_mpmath

**变更说明**:
- Γ 矩阵严格按 tbplas kubo_bastin.h:131-167 C++ 公式实现（向量化 outer product）
- Jackson 核匹配 kpm.cpp:8-17 实现，含 cot(π/(M+1)) 项
- Lorentz 核按标准定义 sinh(λ(1-n/M))/sinh(λ)
- μ 噪声层使用 np.random.RandomState 独立种子保证可复现
- 每个模块含 __main__ 自测代码

**成功判据验证**:
- [x] 5 模块全部 self-test exit 0
- [x] Pylance 零语法错误
- [x] max|Γ(64, π/4)| = ~45（量级 ~M·sinθ ≈ 45，符合预期）
- [x] mu_raw_clean(64) 值域 ∈ [-1, 1]
- [x] Jackson g_0≈1.0, g_63≈7.2e-5 > 0
- [x] sum_kahan vs sum_sequential |diff| < 5e-14 at M=32

**备注**:
- Gamma 矩阵量级 ≈ M·sinθ（非精确 M），θ=π/4 时 sinθ≈0.707，故 max|Γ| ≈ 0.707M
- Sequential vs Kahan 差异 ~1.4e-14 at M=32（~7·ε_mach），与 √N·ε 预测吻合
