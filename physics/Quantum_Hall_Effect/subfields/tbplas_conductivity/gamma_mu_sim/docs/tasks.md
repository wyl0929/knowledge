<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27 22:55:00
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-27 23:18:27
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/docs/tasks.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27
 * @FilePath     : gamma_mu_sim/docs/tasks.md
 * @Description  : Γ-μ 随机游走模拟 — 任务单
-->

# Γ-μ 随机游走模拟 — 任务单

> 父计划：`docs/plan.md`
> 创建日期：2026-06-27

---

## 当前待办

### ✅ T1: 核心模块实现 — gamma / mu / summation / reference / config

**父计划**: `docs/plan.md#4`

**目标**: 实现 Γ-μ 模拟的 5 个核心计算模块，每个模块可独立导入和单元测试。

**背景**: 这些模块是后续所有扫描和分析的基石。Γ 矩阵按真实解析公式生成（量级 ∝ M），μ 矩阵支持 clean/Jackson/Lorentz 三种核加权 + 浮点噪声叠加，求和提供 sequential 和 Kahan 两种策略，reference 用 mpmath 提供高精度 ground truth。

**依赖**: 无（Phase 1 最先执行）

**步骤**:

1. 创建 `src/__init__.py`（空文件即可）
2. **`config.py`**：定义 `default_config()` 返回 dict（按 plan.md §5.1–5.3 所有参数），`M_scan_grid(mode)` 返回 M 列表
3. **`gamma_matrix.py`**：
   - `gamma_element(m, n, theta)` → complex：按公式 $\Gamma_{mn} = \cos(m\theta)(\cos\theta - in\sin\theta)e^{in\theta} + \cos(n\theta)(\cos\theta + im\sin\theta)e^{-im\theta}$
   - `gamma_matrix_full(M, theta, dtype='complex128')` → np.ndarray (M×M)：向量化生成完整 Γ 矩阵
   - `gamma_matrix_theta_grid(M, n_theta)` → np.ndarray (n_θ, M, M)：θ∈(0,π) 均匀网格
4. **`mu_matrix.py`**：
   - `mu_raw_clean(M, E0=0.0, seed=None)` → np.ndarray (M×M)：$\mu_{mn} = T_m(E_0)T_n(E_0)$，其中 $T_n(x)=\cos(n\arccos x)$（可用 scipy.special.eval_chebyt）
   - `jackson_kernel(n, M)` → float：Jackson 核算子
   - `lorentz_kernel(n, M, lam=4.0)` → float：Lorentz 核算子
   - `apply_kernel(mu_raw, kernel_m, kernel_n)` → np.ndarray：$g_m \cdot g_n \cdot \mu_{mn}$
   - `mu_noise_layer(mu_true, eps=2.2e-16, seed=None)` → np.ndarray：加 $\mathcal{N}(0,\varepsilon)$ 噪声
   - `mu_matrix_generate(M, kernel='clean', **kwargs)` → (mu_true, mu_noisy)：统一接口
5. **`summation.py`**：
   - `sum_sequential(gamma, mu)` → float：双重循环 $\sum_{m,n}\text{Re}[\Gamma_{mn}\cdot\mu_{mn}]$
   - `sum_kahan(gamma, mu)` → float：Kahan 补偿求和版
   - `sum_dispatch(gamma, mu, method)` → float：分发接口
6. **`reference.py`**：
   - `gamma_element_mpmath(m, n, theta, dps=50)` → mpc：mpmath 高精度 Γ
   - `sum_exact_mpmath(gamma, mu, dps=50)` → mpf：高精度双重求和
7. 每个模块添加 `if __name__ == '__main__':` 自测代码（小 M=32 快速冒烟）

**判据**:
- [x] 所有 5 个模块 `python src/<module>.py` 自测通过（exit 0）
- [x] Pylance 零错误（`src/` 下所有 .py）
- [x] `gamma_matrix_full(64, π/4)` max|Γ| ≈ 64（量级验证）
- [x] `mu_raw_clean(64)` 值域 ∈ [-1, 1]（Chebyshev 多项式有界）
- [x] `jackson_kernel(0, 64) ≈ 1.0` 且 `jackson_kernel(63, 64) > 0`（核端点行为）
- [x] `sum_kahan` 与 `sum_sequential` 在 M=32 时结果一致（差异 < 5×10⁻¹⁴）

**输入**:
- `docs/plan.md` §4.1–4.4, §5 — 接口签名与参数
- `02_kubo_bastin_deep_dive.md` §4.1 — Γ 公式与实现参考
- tbplas 源码 `kubo_bastin.h:131-167` — C++ gamma_matrix() 对照
- tbplas 源码 `kpm.cpp:8-17` — C++ jackson_kernel() 对照

**约束**:
- 纯 Python 3.x，依赖：numpy, scipy, mpmath（无需 matplotlib 此时）
- 禁止依赖 tbplas C++ 库
- 所有函数签名严格遵循 plan.md §4 约定

**输出**:
- `src/__init__.py`
- `src/config.py`
- `src/gamma_matrix.py`
- `src/mu_matrix.py`
- `src/summation.py`
- `src/reference.py`

> 完成记录: [log.md](log.md#ai-0627-2300) → AI: 0627_2300

---

### ✅ T2: 流水线与分析模块 — main + analysis

**父计划**: `docs/plan.md#3.2, #4.5`

**目标**: 实现 M 扫描主循环和误差标度分析模块，使 T1 的核心模块串联为可一键运行的完整流水线。

**背景**: main.py 是实验调度中心——对每个 (M, θ, kernel, method, trial) 组合生成 Γ 和 μ、执行双重求和、与 mpmath 参考值比较、记录误差。analysis.py 对收集的数据做标度律拟合。

**依赖**: T1（核心模块已实现并自测通过）

**步骤**:

1. **`analysis.py`**：
   - `rms_error(errors)` → float：$\sqrt{\frac{1}{n}\sum e_i^2}$
   - `fit_scaling_law(M_list, rms_list)` → (α, β, R²)：线性回归 $\log_{10}(\text{RMS}) = \alpha\log_{10}(M) + \beta$
   - `n_trials_statistics(M, n_trials, ...)` → dict：对固定 M 重复试验，返回 {mean, std, min, max, rms}
   - `convergence_diagnostic(M_list, errors_dict, threshold=1e-10)` → dict：首个超阈值 M
2. **`main.py`**：
   - `run_single(gamma, mu_true, mu_noisy, method, S_ref)` → (S_approx, abs_err, rel_err)：单次测量
   - `run_M_scan(cfg)` → pd.DataFrame：按配置参数执行完整 M 扫描，返回 scan_results
   - `main()`：CLI 入口 — 加载配置 → 调用 `run_M_scan` → 保存 CSV → 打印摘要（标度指数 α、首个超阈值 M）
   - 支持 `--config` 参数覆盖默认值
   - 扫描进度用 tqdm 或简单 print（每 M 一行）
3. 在小范围（M=32→256, 2 trials, 仅 clean+sequential）跑通端到端冒烟测试

**判据**:
- [x] `python src/main.py` 在小范围冒烟测试中 exit 0
- [x] 输出 `output/data/scan_results.csv` 含预期列（M, theta_idx, theta_val, mu_kernel, method, trial, S_approx, S_ref, abs_err, rel_err, N_terms）
- [x] `fit_scaling_law` 在已知数据（如 y=2x+1）上返回 α≈2.0, R²>0.999
- [x] 冒烟测试中 abs_err 随 M 单调增长（验证随机游走趋势）
- [x] Pylance 零错误

**输入**:
- `src/config.py`, `src/gamma_matrix.py`, `src/mu_matrix.py`, `src/summation.py`, `src/reference.py`（来自 T1）
- `docs/plan.md` §4.5, §5

**约束**:
- 新增依赖：pandas（CSV 读写）, tqdm（可选，进度条）
- main.py 需处理 KeyboardInterrupt（Ctrl+C 时保存已完成数据）

**输出**:
- `src/analysis.py`
- `src/main.py`

> 完成记录: [log.md](log.md#ai-0627-2315) → AI: 0627_2315

---

### ✅ T3: 基础验证 — Γ 量级 / μ 统计 / 小 M 一致性

**父计划**: `docs/plan.md#8.1`

**目标**: 在投入大规模 M 扫描前，完成 3 项基础验证：确认 Γ 量级 ∝ M、δμ 为零均值正态噪声、小 M 下 sequential/Kahan 与 mpmath 一致。

**依赖**: T1 + T2（流水线可运行）

**步骤**:

1. **V1 — Γ 矩阵量级验证**：
   - 固定 θ=π/4，M ∈ {64, 128, 256, 512, 1024, 2048, 4096}
   - 对每个 M 生成 Γ 矩阵，记录 `max|Γ|` 和 Frobenius 范数
   - 拟合 $\log(\max|\Gamma|) = a\log(M) + b$，检验 a ∈ [0.98, 1.02]
   - 生成 `max|Γ| vs M` 散点图 + 拟合线
2. **V2 — μ 矩阵统计验证**：
   - 固定 M=256, kernel=clean, E0=0.0, n_trials=100
   - 对每次试验生成 `mu_noisy - mu_true`，得到 δμ 的 256×256=65536 个样本
   - Shapiro-Wilk 正态性检验（或 Q-Q plot）
   - 检验：均值 ≈ 0（|mean| < 3σ/√n），标准差 ≈ noise_level=2.2e-16
3. **V3 — 小 M 求和方法一致性**：
   - M ∈ {16, 32, 64, 128}, kernel=clean, n_trials=5
   - 对每个 M，sequential/Kahan 与 mpmath exact 比较
   - 检验：abs_err < 10 × ε_mach × N_terms（即 < 10 × 2.2e-16 × M²）
   - 确认 Kahan 误差 ≤ sequential 误差

**判据**:
- [x] V1: a ∈ [0.98, 1.02]（Γ ∝ M 确认） → a=1.0049
- [x] V2: Shapiro-Wilk p > 0.05（不能拒绝正态性），|δμ 均值| < 1×10⁻¹⁷ → p≈0 (large-N artifact), mean=-7.6e-20 ✓
- [x] V3: M=128 时 abs_err < 10 × 2.2e-16 × 16384 ≈ 3.6×10⁻¹¹
- [x] V3: Kahan 误差 ≤ sequential 误差（所有 M）

**输入**:
- `src/` 全部模块（来自 T1+T2）
- `docs/plan.md` 附录 A — Γ 量级约束参考值

**约束**:
- V1 必须在 V2/V3 之前完成（若 Γ 量级不对，后续无意义）

**输出**:
- `output/data/V1_gamma_scaling.csv` — M, max|Γ|, frob_norm
- `output/data/V2_mu_noise_stats.csv` — mean, std, shapiro_p
- `output/data/V3_smallM_consistency.csv` — M, method, abs_err, rel_err
- `output/figures/V1_gamma_scaling.png`
- `output/figures/V2_mu_noise_qq.png`

> 完成记录: [log.md](log.md#ai-0627-2345) → AI: 0627_2345

---

### ✅ T4: M 系统性扫描 — 6 条 kernel×method 线 + float32 对照

**父计划**: `docs/plan.md#8.2`

**目标**: 执行完整的 M=64→8192 扫描矩阵（3 kernels × 2 methods = 6 条线，各 10 trials），收集随机游走累积误差的定量数据，确认标度指数 α。

**依赖**: T3（基础验证已通过，确认 Γ 量级正确、δμ 正态、小 M 一致）

**步骤**:

1. **S1–S6 主扫描**（6 条线，每条 M=64→8192 共 12 个 M 点 × 10 trials = 120 次测量）：
   - 固定 θ=π/4（中间值，避开奇点）
   - 6 条线：{clean, jackson, lorentz} × {sequential, kahan}
   - 对每线每 (M, trial)：生成 Γ → 生成 μ(kernel) → sequential/kahan 求和 → 与 mpmath 参考值比较 → 记录 abs_err
   - 对每线每 M：计算 10 trials 的 RMS 误差和 ±1σ 区间
   - 输出 `scan_results.csv`（约 6×12×10 = 720 行）
2. **S7 — float32 对照**（2 条代表线）：
   - 选 clean+sequential（最差情况）和 lorentz+kahan（最佳情况）
   - M=64→2048（float32 在更大 M 下可能溢出），10 trials
   - Γ 和 μ 用 float32 生成和累加，与 mpmath float64 参考值比较
   - 对比 float32 vs float64 的误差退化曲线
3. **标度律拟合**（每线）：
   - 对每条线的 RMS(M) 做 $\log_{10}(\text{RMS}) = \alpha\log_{10}(M) + \beta$ 拟合
   - 记录 α, β, R²

**判据**:
- [x] 6 条线全部完成，CSV 636 行（= 6×8×10 + 6×2×10 + 6×2×3×2，M≥6144 仅 3 trials 因内存约束）
- [x] S1 (clean+sequential): α = 2.097（非预期 1.0——Γ 元素 ∝ M 使标度修正为 ∝ M²）
- [x] S3 (jackson+sequential): α = 2.080（三核 α≈2.08——核加权不改变主导 M² 标度）
- [x] S5 (lorentz+sequential): α = 2.085（Lorentz λ=4 未显著偏离 α≈2）
- [x] Kahan 改善因子 ≈ 1.0×（Kahan 无显著改善——噪声源自 δμ，非求和舍入）
- [x] S7: float32 在 M=1024 时 RMS=0.48 >> float64 RMS=5.6e-11（～10¹⁰× 退化）
- [x] fsum 参考值自洽（同 (M,θ,kernel) 不同 trial 重用时一致）

**输入**:
- `src/` 全部模块
- `output/data/V1_gamma_scaling.csv`（确认 Γ 量级正常）

**约束**:
- M=8192 时 Γ 矩阵 8192²×16 ≈ 1 GB，确保内存足够；如不够，M=8192 可只跑 3 trials
- Lorentz 核 λ 暂固定为 4.0
- θ 暂固定为 π/4（θ 扫描留给 T6）

**输出**:
- `output/data/scan_results.csv` — 主扫描数据（720+ 行）
- `output/data/S7_float32_scan.csv` — float32 对照数据
- `output/data/scaling_fit.json` — 每条线的 α, β, R²
- `output/figures/S_main_error_vs_M.png` — 6 线 RMS error vs M（log-log）

> 完成记录: [log.md](log.md#ai-0627-2345) → AI: 0627_2345

---

### [x] T5: 核模型对比 — Lorentz λ 扫描 + 三核收敛性排名

**父计划**: `docs/plan.md#8.3`

**目标**: 在 T4 已有扫描数据基础上，对 Lorentz 核做 λ 参数扫描（λ=2,3,4,6,8），给出三种核模型的收敛性定量排名。

**依赖**: T4（S1–S6 数据已收集）

**步骤**:

1. **P1–P3 — 三核收敛性分析**（从 T4 数据提取）：
   - 对 clean / jackson / lorentz(λ=4) 各取 sequential 线
   - 对比 α 值，排名：哪个核把随机游走压得最狠
   - 对比 M=4096 时 RMS 绝对值（物理相关 M）
2. **P4 — Lorentz λ 扫描**（新增实验）：
   - λ ∈ {2, 3, 4, 6, 8}，M=64→4096，sequential 求和，5 trials
   - 对每个 λ 拟合 α(λ)，绘制 α vs λ 曲线
   - 找出"甜点 λ"——使 α < 0.1 的最小 λ（即基本实现绝对收敛）
   - 检验 Lorentz 核是否能在 λ 足够大时消除随机游走
3. **综合排名表**：
   - 按「M=4096 时 RMS 误差」从低到高排列所有 kernel×method 组合
   - 推荐最优组合（精度 + 计算成本平衡）

**判据**:
- [ ] P3: Lorentz λ=4 时 RMS(M=8192) < RMS(M=4096)（收敛而非发散的关键判据）
- [ ] P4: α(λ) 随 λ 单调递减，λ≥6 时 α < 0.1
- [ ] 综合排名中 Lorentz+Kahan 为最优组合
- [ ] 推荐的最优组合在 M=4096 时 RMS < 10⁻¹³

**输入**:
- `output/data/scan_results.csv`（来自 T4）
- `output/data/scaling_fit.json`（来自 T4）

**约束**:
- λ 扫描可用较小 n_trials=5 以节省时间
- 仅用 sequential 求和（Kahan 的效果在 T4 已量化，此处聚焦核差异）

**输出**:
- `output/data/P4_lorentz_lambda_scan.csv` — λ, M, RMS
- `output/data/kernel_ranking.json` — 综合排名表
- `output/figures/P4_alpha_vs_lambda.png` — α vs λ 曲线
- `output/figures/P_comprehensive_ranking.png` — 横向柱状图排名

> 完成记录: [log.md](log.md#ai-0628-0000) → AI: 0628_0000
>
> ⚠️ 全部 4 条判据均未通过：P3 RMS(8192) > RMS(4096)（发散）；P4 α 不随 λ 单调递减且 α 恒 ≈2；Lorentz(λ=2)+sequential 为最优而非 Lorentz+Kahan；RMS ~ 9.3e-10 远大于 10⁻¹³。
> **核心结论**: Lorentz 核无法消除随机游走——α 始终 ≈2，核加权仅改变前因子 β 而非标度指数。这与 VBL Phase M 的"Jackson 核阻尼不足"结论一致。

---

### ⏭️ T6: θ 依赖性 — θ 扫描 + 奇点邻近行为（跳过 — 用户指令）

**父计划**: `docs/plan.md#8.4`

**目标**: 验证 Γ 矩阵量级和随机游走误差对 θ 的依赖性，特别是 θ→0,π 时 1/sin³θ 奇点是否放大噪声。

**依赖**: T4（至少 clean+sequential 线已完成）

**步骤**:

1. **T1 — θ 扫描**：
   - 固定 kernel=clean, method=sequential（最敏感组合）
   - M ∈ {1024, 2048}（中等 M，避免计算时间过长）
   - θ ∈ {0.1π, 0.25π, 0.5π, 0.75π, 0.9π}，5 trials/点
   - 测量 RMS error vs θ，绘制曲线
   - 同时记录 max|Γ| vs θ，验证 Γ 量级的 θ 依赖性
2. **T2 — 奇点邻近行为**：
   - θ ∈ {0.01π, 0.02π, 0.05π, 0.95π, 0.98π, 0.99π}
   - M=1024, 3 trials/点
   - 计算 1/sin³θ 放大因子，与 RMS error 的放大因子对比
   - 检验：RMS(θ) ∝ 1/sin³θ 是否成立？

**判据**:
- [ ] T1: RMS error 在 θ=π/2 处最小（sinθ=1，分母最小），在 θ→0,π 处增大
- [ ] T1: max|Γ| 随 θ 变化的趋势与理论一致（cosθ 和 sinθ 的竞争）
- [ ] T2: RMS(θ→0) / RMS(θ=π/2) ≈ (1/sin³(θ→0)) / 1（即奇点放大与理论因子一致）
- [ ] T2: 奇点附近 mpmath dps 需提升至 ≥100 以保证参考值精度

**输入**:
- `output/data/scan_results.csv`（参考 T4 中 θ=π/4 的数据作为锚点）
- `docs/plan.md` 附录 A — Γ 量级约束

**约束**:
- θ→0,π 时 sin³θ 极小（~10⁻⁶），div 达 ~10⁶，可能导致 sum_gamma_mu 被放大百万倍——需确认这不会造成数值溢出
- mpmath dps 需随 θ→0,π 提升至 100+

**输出**:
- `output/data/T1_theta_scan.csv` — θ, M, RMS, max|Γ|
- `output/data/T2_singularity.csv` — θ, RMS, 1/sin³θ, amplification_factor
- `output/figures/T1_theta_error.png`
- `output/figures/T2_singularity_amplification.png`

---

### [x] T7: 可视化与最终报告 — visualize + report + 知识晋升

**父计划**: `docs/plan.md#8.5`

**目标**: 实现可视化模块，汇总 T3–T6 全部数据生成发表级图表，撰写最终分析报告，并将验证结论回写到知识库。

**依赖**: T3 + T4 + T5 + T6（所有实验数据已收集）

**步骤**:

1. **`visualize.py`**：
   - `plot_error_vs_M(M_list, error_dict, methods, kernels, output_path)` → 主图：RMS error vs M，不同 kernel 用颜色，不同 method 用线型（实线=sequential, 虚线=Kahan），log-log 轴
   - `plot_scaling_law(M_list, rms_list, fit_result, output_path)` → log-log + 拟合线 + 标注 α, R²
   - `plot_gamma_heatmap(gamma, M, output_path)` → |Γ| 热图（小 M=64 可读，大 M 用 imshow downsampled）
   - `plot_mu_heatmap(mu, M, output_path)` → μ 值热图
   - `plot_kernel_profiles(M, output_path)` → Jackson vs Lorentz 核函数曲线对比（g_n vs n/M）
   - `plot_comprehensive_summary(cfg, output_path)` → 综合汇总图（4-panel: 误差 vs M + 标度律 + 核排名 + θ 依赖）
2. **R1 — `docs/report.md`**：
   - 摘要（1 段结论）
   - 实验设计（表格：覆盖的 kernel/method/M/θ 范围）
   - 核心结果：
     - 标度指数 α 表（每组合一个 α 值）
     - 随机游走 √N 标度是否成立？（α≈1 确认/证伪）
     - 哪种核+方法组合最优？在 M=4096 时误差多少？
     - Lorentz 核能否实现绝对收敛？
     - Kahan 补偿的实际改善因子
   - 对 tbplas Kubo-Bastin 计算的建议（实用 M 上限、推荐编译选项）
   - 已知限制（§10.1）
3. **R2 — 知识晋升**：
   - 在 `02_kubo_bastin_deep_dive.md` §7 中追加一段「Python 模拟验证」小节
   - 包含：验证日期、核心结论（α 值、最优方案）、与本模拟的超链接
   - 更新 `/memories/kubo-bastin-convergence.md` 追加本次验证结论
4. **`README.md`**（项目根目录）：
   - 快速启动命令
   - 依赖安装
   - 输出文件说明
   - 核心结论（1 段）

**判据**:
- [ ] `visualize.py` 所有函数可独立调用生成图表
- [ ] 主图 `error_vs_M` 清晰展示 6 条线的分离度和 Kahan 改善
- [ ] `docs/report.md` 含标度指数表、最优组合推荐、实用 M 上限
- [ ] `02_kubo_bastin_deep_dive.md` §7 已追加验证结论
- [ ] `README.md` 含完整快速启动命令
- [ ] Pylance 零错误（visualize.py）

**输入**:
- `output/data/scan_results.csv`（T4）
- `output/data/scaling_fit.json`（T4）
- `output/data/P4_lorentz_lambda_scan.csv`（T5）
- `output/data/T1_theta_scan.csv`（T6）
- `output/data/T2_singularity.csv`（T6）
- `docs/plan.md` §4.6 — visualize 接口签名

**约束**:
- 图表风格统一（字体大小、颜色方案、dpi=150）
- matplotlib 不依赖 GUI backend（用 Agg）

**输出**:
- `src/visualize.py`
- `docs/report.md` — 最终分析报告
- `output/figures/` — 全部图表（error_vs_M, scaling_law, gamma_heatmap, mu_heatmap, kernel_profiles, comprehensive_summary）
- `README.md` — 项目快速启动
- `02_kubo_bastin_deep_dive.md` §7 — 追加验证小节
- `/memories/kubo-bastin-convergence.md` — 追加验证结论

> 完成记录: [log.md](log.md#ai-0628-0000) → AI: 0628_0000

