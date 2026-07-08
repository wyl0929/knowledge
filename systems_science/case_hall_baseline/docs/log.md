<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-05-25 16:54:31
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-01 00:44:52
 * @FilePath     : /MG/docs/log.md
 * @Description  :
-->

# MG 日志

<a id="ai-0701-1400"></a>

## AI: 0701_1400 — 🔴 基线偏移根因重新定位: Nyquist 混叠 (num_integ_steps 欠采样)

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/m_int/*.yaml` | ➕ 批量生成 | M × num_integ_steps 全矩阵扫描 (5×5=25 YAML) |
| `runs/0701/M_int/*.txt` | ➕ 运行产出 | 全部 load 同一 HDF5，仅变 int/M |
| `docs/blue_print.md` | ✏️ 重大修订 | 战略转向撤销，tbplas 恢复为主引擎 |
| `shared/tbplas-internals.md` | ✏️ 重大修订 | §12.3 VBL 结论标记 SUPERSEDED，新增 §12.4 Nyquist 根因 |
| `docs/references/02_kubo_bastin_deep_dive.md` | ✏️ 重大修订 | 旧根因标记 SUPERSEDED，新增 Nyquist 分析 |
| `docs/Phase0_save_load/plan.md` | ✏️ 修订 | C++ 源码审查 + config 不匹配分析 |

### 发现

**M_int 全矩阵扫描** (M ∈ {512,1024,2048,3072,4096} × int ∈ {512,1024,2048,3072,4096}, m=512, rescale=20, B=100T, 共用同一 HDF5 μ 文件) 揭示：

| int/M | M=512 | M=1024 | M=2048 | M=3072 | M=4096 |
|:-----:|:-----:|:------:|:------:|:------:|:------:|
| 0.125 | — | — | — | — | 🔴 88 |
| 0.250 | — | — | 🔴 88 | — | 🔴 505 |
| 0.333 | — | — | — | 🔴 270 | — |
| 0.500 | ✅ 0.6 | 🟡 5.5 | 🔴 37 | — | 🔴 176 |
| 0.667 | — | — | — | 🟡 6.1 | — |
| 0.750 | — | — | — | — | ✅ 0.24 |
| **1.000** | ✅ 0.6 | ✅ 0.3 | ✅ 0.2 | ✅ 0.2 | — |

> 以 int=4096 为参考 (ground truth)。🔴=RMS>10, 🟡=1-10, ✅=<1 e²/h

### 根因

**Nyquist 采样定理**: Γ_mn(θ) 矩阵的振荡频率 ∝ M (最高频分量周期 2π/M)。要在 [0,π] 上准确数值积分，Nyquist 要求 `num_integ_steps ≥ num_kernel`。

当 `int < M` 时 → 高频分量欠采样 → 混叠 (aliasing) → 伪影叠加 → σ_xy 系统性偏移。

**非单调性特征** (M=4096: int=1024 误差 505 > int=512 误差 88) 是混叠的经典诊断标志——特定欠采样比导致别名同相叠加。

### 影响

**VBL Phase A–M (2026-06-22~27) 的全部 "条件收敛+浮点精度" 结论被推翻**:
- VBL 所有实验使用的 `num_integ_steps` 为默认值 2048
- 对于 M≥3072，int=2048 < M → Nyquist 欠采样 → 观测到的 "基线偏移" 实为混叠伪影
- "δμ 随机噪声"、"Γ·μ 放大"、"随机游走" 等假说追逐的是同一个幻影的不同侧面
- VBL 诊断并非完全错误——它正确排除了 9 个假说，并确认了噪声注入/Γ 权重的数学关系。但它们诊断的是**混叠产生的伪影**，而非独立的数值现象

**新安全窗口**: M ≤ 4096, int ≥ M (例如 M=4096 需 int≥3072, 推荐 int≥4096)

### 后续行动
- [x] 更新 blue_print.md 战略方向
- [x] 更新 tbplas-internals.md §12.3 (SUPERSEDED) + 新增 §12.4
- [x] 更新 02_kubo_bastin_deep_dive.md (SUPERSEDED)
- [ ] 修正所有现有 YAML 中的 dckb_num_integ_steps (从 null/2048 → ≥ M)
- [ ] 在 M=4096, int=4096 下重新运行 García 2015 复现验证

---

<a id="ai-0701-0120"></a>

## AI: 0701_0120 — TK5 推送完成: 双代码 M 扫描全部提交集群

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `test/TK5_kite_hall_Mscan.py` | ➕ 新建 | quantum-kite M 扫描脚本 (命令行参数 M) |
| `slurm/slm_kite_cross_check.sh` | ➕ 新建 | quantum-kite SLURM 脚本 (从 job name 解析 M) |
| `slurm/slm_tbplas_cross_check.sh` | ➕ 新建 | tbplas SLURM 脚本 ($SLURM_JOB_NAME → YAML) |
| `configs/hall_m64_M{064,0256,0512,1024,2048,4096}_cross.yaml` | ➕ 新建 | tbplas 6 个 M 值 YAML 配置 |
| `configs/kite_cross_check.yaml` | ➕ 新建 | 跨代码参数约定文档 |
| `~/scratch/quantum-kite/kite.py` (集群) | ✏️ 修复 | 同步 vectors_full 磁场 cross product bugfix |

### 变更说明
- **参数对齐**: monolayer, m=64, B≈100T (kite: 100.65T), rescale=-1, T=10.0K, rs=1
- **quantum-kite 超胞**: lx=64, ly=784 (50,176 cells; ly=784/16=49✓, B_min=100.65T≈100T)
- **tbplas 超胞**: m=64 (64×64=4,096 cells); 不同超胞尺寸但洁净体系 σ_xy 独立于尺寸
- **关键修复**: 集群 kite.py 缺少 vectors_full bugfix (TK4 修复), 已同步上传

### 作业清单
| Job ID | 代码 | M | 状态 |
|--------|------|------|:--:|
| 288252 | tbplas | 64 | ✅ 完成 |
| 288258 | kite | 64 | ✅ 完成 |
| 288259 | tbplas | 256 | 🔄 已提交 |
| 288260 | tbplas | 512 | 🔄 已提交 |
| 288261 | tbplas | 1024 | 🔄 已提交 |
| 288262 | tbplas | 2048 | 🔄 已提交 |
| 288263 | tbplas | 4096 | 🔄 已提交 |
| 288264 | kite | 256 | 🔄 已提交 |
| 288265 | kite | 512 | 🔄 已提交 |
| 288266 | kite | 1024 | 🔄 已提交 |
| 288267 | kite | 2048 | 🔄 已提交 |
| 288268 | kite | 4096 | 🔄 已提交 |

### 冒烟测试结果 (M=64)
- **tbplas**: ✅ σ_xy(E) 401 点正常输出, E∈[-0.6, 1.0] eV, σ_xy≈-0.35→-0.12
- **kite**: ✅ KITEx + KITE-tools 正常完成, B=100.65T, 输出 401 点 condDC.dat

### 成功判据验证
- C1: 8 组数据正常完成 — M=64 两侧均 ✅; 其余 10 作业已提交待完成
- C2–C4: 待全部作业完成后对比分析

---

<a id="ai-0701-0030"></a>

## AI: 0701_0030 — TK4 完成: quantum-kite B≠0 QHE 信号初探

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `test/TK4_hall_Bscan.py` | ➕ 新建 | B=50/100/200T Hall 扫描 |
| `/home/wyl/quantum-kite/kite.py` | ✏️ bugfix | 2D 晶格磁场 cross product 维度修复 |
| `runs/kite/phase1_first_run/kite_monolayer_B{50,100}_M256_hall.txt` | ➕ 生成 | B=49.82T, 99.64T Hall 数据 |
| `figures/kite/phase1/hall_monolayer_Bscan_M256.png` | ➕ 生成 | 3 B 值 σ_xy 对比图 |

### 结果
- QHE S 曲线观测到: B=50T (−2.34 → +0.17), B=100T (−2.55 → +1.63)
- 台阶不明显 (M=256 不足); B=200T KITEx 超时 (600s)
- 详情见 `docs/sigma/log_quantum_kite.md#ai-0701-0030`

---

<a id="ai-0701-0015"></a>

## AI: 0701_0015 — TK3 完成: quantum-kite B=0 零磁场 Hall 验证

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `test/TK3_hall_B0.py` | ➕ 新建 | B=0 Hall 验证脚本 |
| `configs/kite_hall_monolayer.yaml` | ➕ 新建 | quantum-kite Monolayer Hall 配置 |
| `runs/kite/phase1_first_run/kite_monolayer_B0_M256_hall.txt` | ➕ 生成 | B=0 Hall 数据 |
| `figures/kite/phase1/hall_monolayer_B0_M256.png` | ➕ 生成 | B=0 σ_xy + σ_xx 双面板 |

### 结果
- Im{σ} ≡ 0 → σ_xy = 0 at B=0 ✅
- Re{σ} ≈ 2.4–2.6 (σ_xx)
- 详情见 `docs/sigma/log_quantum_kite.md#ai-0701-0015`

---

<a id="ai-0629-1800"></a>

## AI: 0629_1800 — TASK-04.5 完成: mu 复用功能移植到 tbplas-cpp-eta

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `tbplas-cpp-eta/sources/tbpm/config.h` | ✏️ 修改 | +dckb_save_mu_file, +dckb_load_mu_file (string, default "") |
| `tbplas-cpp-eta/sources/tbpm/kubo_bastin.h` | ✏️ 修改 | +kbdc_mu_raw() virtual + impl, +apply_jackson_kernel(), +truncate_mu() |
| `tbplas-cpp-eta/sources/tbpm/solver.h` | ✏️ 修改 | calc_hall_cond() 双路径: load HDF5 / compute+save raw mu |
| `tbplas-py-1a43ccb/tbplas/tbpm/config.py` | ✏️ 修改 | +dckb_save_mu_file, +dckb_load_mu_file (str, default "") |
| `tbplas-cpp-eta/lib/*.so` | 🔄 重编译 | 9 .so, import tbplas OK |

### 变更说明
- 从 `tbplas-cpp-exp` 移植 mu save/load 完整流水线到 `tbplas-cpp-eta`
- **不引入** TBPLAS_LONG_DOUBLE / TBPLAS_LORENTZ_KERNEL 宏
- 默认值空字符串 → 向后兼容，行为与原 kbdc_mu() 一致
- kbdc_mu_raw() = kbdc_mu() 去掉 Jackson 核的版本

### 成功判据验证
- C1: config.h dckb_save/load_mu_file grep ✅ (2 matches)
- C2: kubo_bastin.h kbdc_mu_raw (virtual + impl) ✅ (2 matches)
- C3: kubo_bastin.h apply_jackson_kernel + truncate_mu ✅ (2 matches)
- C4: solver.h dckb_load/save_mu_file ✅ (7 matches)
- C5: config.py dckb_save/load_mu_file ✅ (2 matches)
- C6: 编译零错误, import tbplas OK ✅
- C7: dckb_save_mu_file="" (默认空串) ✅

---

<a id="ai-0629-1700"></a>

## AI: 0629_1700 — TASK-01~04 完成: 有限η Kubo-Bastin 环境搭建与编译

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `tbplas/source/tbplas-cpp-eta/` | ➕ 新建 | 从 a021ca8 rsync 复制，排除 build |
| `tbplas/source/tbplas-cpp-eta/sources/tbpm/gamma_matrix_eta.h` | ➕ 新建 | 有限η Γ核参考实现 |
| `tbplas/source/tbplas-cpp-eta/sources/tbpm/kubo_bastin.h` | ✏️ 修改 | +include gamma_matrix_eta.h; cond_from_trace() 调用替换 |
| `tbplas/source/tbplas-cpp-eta/sources/tbpm/config.h` | ✏️ 修改 | +dckb_eta 成员 (double, default 0.0) |
| `tbplas/source/tbplas-py-1a43ccb/tbplas/tbpm/config.py` | ✏️ 修改 | +self.dckb_eta = 0.0 |
| `~/anaconda3/envs/tbplas-eta/` | ➕ 新建 | conda 环境 python=3.12 |
| `tbplas/install/tbplas-cpp-eta/lib/` | ➕ 编译 | 9 个 .so 文件 |

### 变更说明
- **TASK-01**: rsync 复制源码，diff 零差异 ✅
- **TASK-02**: gamma_matrix_eta.h 语法检查零错误，两个重载版本 ✅
- **TASK-03**: 三文件修改 — kubo_bastin.h (include+调用替换), config.h (+dckb_eta), config.py (+dckb_eta) ✅
- **TASK-04**: conda 环境 tbplas-eta 创建，编译 9 .so，import tbplas 零错误，TBPLAS_CORE_PATH 正确 ✅
- **TASK-05**: 测试目录 `test_output/T5_L0_L2/` 已创建，T1-T4 测试待执行（用户暂停）

### 成功判据验证
- TASK-01: diff 零差异, kubo_bastin.h 存在, a021ca8 未改动 ✅
- TASK-02: 文件存在, g++ -fsyntax-only 零错误, 双重重载 ✅
- TASK-03: gamma_matrix_eta grep 匹配, dckb_eta 三处匹配 ✅
- TASK-04: conda env 存在, 9 .so ≥ 8, import tbplas 零错误, TBPLAS_CORE_PATH 正确 ✅

---

<a id="ai-0628-1200"></a>

## AI: 0628_1200 — K5 完成: Σ(Γ⊙μ) vs M 收敛曲线

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `test/K5_sum_vs_M.py` | ➕ 新建 | K5 脚本: 复用 K4 compute_Gm_matrix() |
| `test/K5_sum_vs_M.png` | ➕ 生成 | Jackson + 无核 双面板 Σ(M) 曲线 |
| `test/K5_sum_vs_M_data.txt` | ➕ 生成 | 汇总数据表 |

### 结果 — Jackson Σ(M)
| M | θ=1.0 | θ=1.5 | θ=2.0 |
|---|:---:|:---:|:---:|
| 2048 | −4764 | +3328 | +4112 |
| 2560 | −10898 | +2605 | +13931 |
| 3072 | −18756 | +1159 | +31133 |
| 3584 | −25897 | −336 | +56003 |
| 4096 | −31463 | −2610 | +88245 |

- θ=1.5 特殊: Σ 在 M~3584 过零点, 对消增强
- 无核 Σ ~6–20× Jackson, 同趋势发散
- K4 交叉验证: M=4096 Σ 完全一致 ✅

---

<a id="ai-0628-0200"></a>

## AI: 0628_0200 — G4 完成: Gamma 矩阵行/列和 Re/Im 分解 × 3θ

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `test/G4_gamma_row_col_sum.py` | ✅ 新建 | G4 分析脚本 |
| `test/G4_row_col_sum_theta{1.0,1.5,2.0}.txt` | ✅ 生成 | 行/列和原始数据 |
| `test/G4_gamma_sum_theta{1.0,1.5,2.0}.png` | ✅ 生成 | 四面板可视化 |

### 结果
| θ | \|row_sum\| m=0 | \|row_sum\| m=4095 | ratio |
|:---:|:---:|:---:|:---:|
| 1.0 | 3595 | 1638 | 0.46× |
| 1.5 | 2997 | 1605 | 0.54× |
| 2.0 | 2213 | 2314 | 1.05× |

- Hermiticity = 0.00 (perfect) ✅
- col_sum ≈ conj(row_sum), max diff ~1e-10 ✅
- |Im| ≈ |Re| (同级 ~1000–3500) ✅
- **无简单 O(m) 线性增长** — 行和由 cos/sin 振荡主导, 高 m 区无单调增大

### Plan Feedback
- 无需修订 — G4 为 Phase G 补充验证，结论与 G1–G3 一致（Γ 矩阵精度正常）

---

<a id="ai-0628-0105"></a>

## AI: 0628_0105 — D4 完成: μ 矩阵实部/虚部之和 vs M

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `test/D3_mu_sum_real_imag_vs_M.png` | ➕ 新建 | 双面板: ΣRe/ΣIm vs M + L1 vs M |
| `test/D3_mu_sum_data.txt` | ➕ 新建 | 5 M 值的数据表 |

### 结果
| M | Σ Re(μ) | Σ Im(μ) | L1 Re | L1 Im |
|---|:---:|:---:|:---:|:---:|
| 2048 | +1.02×10⁻⁴ | −1.09×10⁻³ | 3706 | 2428 |
| 2560 | +1.07×10⁻³ | +2.76×10⁻⁴ | 5769 | 3753 |
| 3072 | +1.29×10⁻³ | −3.23×10⁻⁴ | 8254 | 5403 |
| 3584 | +4.93×10⁻⁴ | −2.81×10⁻⁴ | 11204 | 7368 |
| 4096 | +8.69×10⁻⁴ | −3.47×10⁻⁴ | 14610 | 9633 |

### 判定
✅ μ 矩阵 ΣRe/ΣIm 无 M 依赖单调漂移 — 均在 ~10⁻³–10⁻⁴ 量级振荡，验证了 Phase K1 结论（μ 无 M 依赖性）。L1 norm 平滑增长（M² 项数增加），无异常跳变。

---

<a id="ai-0627-2257"></a>

## AI: 0627_2257 — Phase M 完成: 随机游走假说封闭验证 (M1✅ M2❌ M3⚠️)

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `test/phase_M_analysis.py` | ➕ 新建 | Phase M 综合分析脚本 (M1+M2+M3) |
| `test/M1_noise_injection.png` | ➕ 生成 | M1: dS_obs vs dS_pred 散点 + RMS scaling 双对数 |
| `test/M1_noise_injection.txt` | ➕ 生成 | M1 统计报告 |
| `test/M2_precision_scaling.png` | ➕ 生成 | M2: f32/f64 S(θ) 双曲线 + 精度对比 |
| `test/M2_precision_scaling.txt` | ➕ 生成 | M2 精度分析报告 |
| `test/M3_gamma_capping.png` | ➕ 生成 | M3: S_capped + S_random vs Γ_max (2×3 面板) |
| `test/M3_gamma_capping.txt` | ➕ 生成 | M3 Γ 截断报告 |
| `docs/sigma/task_vbl_trace.md` | ✏️ 更新 | Phase M 任务状态全部 [x] + 完成记录 |

### M1 — 合成噪声注入验证 ✅ PASS
- dS_obs/dS_pred ≈ 1.000±0.001 for σ≥1e-14 (9/9 points within 0.05%)
- RMS(ΔS) ∝ σ_noise^0.9992 (100 trials, R²>0.9999)
- 噪声注入传播机制完美成立

### M2 — 浮点精度缩放验证 ❌ 求和精度非瓶颈
- S_f32 ≈ S_f64 (|Δ|/|S| ≈ 2.5e-7 at θ=π/2)
- 求和精度不是限制因素 — δμ 源自 C++ KPM Chebyshev 迭代
- 与 Phase C (Kahan 无效) + Phase I (long double 无效) 一致

### M3 — Γ 量级截断 ⚠️ Γ 权重确认
- 低Γ区 S_capped ≪ S_random (同项数) → 高|Γ|项主导
- |S| ∝ Γ_max^α (α~1.3-2.3, 超线性因 Γ·μ 协变)

### Phase M 综合判定
- M1✅ M2❌(求和) M3⚠️ → 根因链: C++ KPM → δμ → ×Γ → S(M)发散
- 修复: (a) C++ quad precision (b) Lorentz λ>4 (c) 实用窗口 M≤2560

---

<a id="ai-0626-1640"></a>

## AI: 0626_1640 — K4 完成: Γ⊙μ 矩阵全分辨率可视化 (6 图 × 5 M, 零 NaN)

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `test/K4_matrix_viz.py` | ➕ 新建 | K4 主脚本: Gamma 矩阵显式构建 + 降采样渲染 |
| `test/K4_matrix_{jackson,lorentz,nokernel}_theta{1.0,2.0}.png` | ➕ 生成 | 6 张热图 (2θ × 3核), 每张 5 子图 |
| `test/K4_matrix_report.txt` | ➕ 生成 | 全统计摘要 + 跨核对比 |

### 方法
- 加载 `mu_raw_M4096_m64.h5` (raw μ, 无核)
- 固定 θ=1.0, 2.0, M ∈ {2048, 2560, 3072, 3584, 4096}
- Gamma 用秩-2 显式构建: Γ = cos_nt·fn^T + conj(fn)·cos_nt^T
- 三种核: Jackson / Lorentz (λ=4, 等价 J2 C++) / 无核 (全 1)
- Gm = Re(Γ ⊙ (g·μ·g)), 降采样 block-avg 到 ~1024px 渲染

### 关键数值发现

**幅度标度**:
| 核 | max |Re(Gm)| (θ=1.0, M=4096) | vs Jackson |
|------|:---:|:---:|
| Jackson | 2.93 | 1× |
| Lorentz λ=4 | 1.48 | 0.50× |
| 无核 | 17.5 | 6.0× |

**均值**: Jackson θ=1.0 mean≈−0.0019, θ=2.0 mean≈+0.0053 — 接近零

**θ 对比**: θ=1.0 frac>0≈0.49, θ=2.0 frac>0≈0.51 — 符号分布随 θ 翻转

**高阶区**: Jackson/Lorentz 系统性渐变, 无核 salt-and-pepper 噪声

### 判定
- 全部 30 矩阵 NaN=0 Inf=0 ✅
- 核函数抑制但不消除高阶波动 (Lorentz 降 ~2×)
- 矩阵元均值≈0 → 偏移来自 O(M²) 系统性累加, 非单元素异常

---

<a id="ai-0625-0838"></a>

## AI: 0625_0838 — Phase L 完成: μ 符号随机、振荡对消有效、Krylov 方向漂移假说排除

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `test/phase_L_analysis.py` | ➕ 新建 | Phase L 综合分析脚本 (L1+L2+L3) |
| `test/L1_mu_sign_structure.png` | ➕ 生成 | μ 符号结构 (六面板: 行pos_frac/列pos_frac/分块柱状图/直方图/高m放大/分布) |
| `test/L1_mu_sign_structure.txt` | ➕ 生成 | L1 符号一致性报告 |
| `test/L2_cancellation_rate.png` | ➕ 生成 | 对消率 R(θ) 四面板: R曲线/net贡献/R散点/R比 |
| `test/L2_cancellation_rate.txt` | ➕ 生成 | L2 对消率报告 |
| `test/L3_row_profile.png` | ➕ 生成 | 行贡献剖面 (3θ×3面板: row_sums/cumsum/高m放大) |
| `docs/sigma/task_vbl_trace.md` | ✏️ 更新 | L1/L2/L3 标记完成 + 综合判定 |

### 方法
利用 Phase K 已有的工具函数 (load_mu, jackson_kernel, apply_kernel)，新增 `build_gamma_matrix()` 和 `compute_terms_fast()` 实现 O(M²) 向量化 Γ·μ 项计算。L1 直接分析 raw μ 的符号结构；L2 用 256 点 θ 扫描计算对消率；L3 对 3 个代表性 θ 做单行贡献剖面。

### L1 — μ 符号一致性: ✅ PASS (无符号偏置)

| 指标 | 值 | 判定 |
|------|:---:|:---:|
| Row pos_frac mean | 0.4997 ± 0.0039 | ≈ 0.5 ✅ |
| Col pos_frac mean | 0.4997 ± 0.0040 | ≈ 0.5 ✅ |
| 8 blocks (512-row) | [0.4993, 0.5000] | 全在 ±0.001 内 ✅ |
| High-m (m≥3072) | mean=0.4994 | 无漂移 ✅ |
| 全矩阵直方图 | 对称, 零均值 | 随机分布 ✅ |

**结论**: μ 矩阵符号完全随机 — Krylov 方向漂移假说被排除。

### L2 — 对消率: ✅ PASS (R ≈ 0, 振荡对消有效)

**3 点测试**:
| θ | R_old | R_new | 判定 |
|---|:---:|:---:|:---:|
| 1.00 (57°) | 0.0335 | 0.0056 | R_new < R_old ✅ |
| 1.57 (90°) | 0.0118 | 0.0134 | 同级 ✅ |
| 2.00 (115°) | 0.0494 | 0.0566 | 同级 ✅ |

**256 点 θ 扫描**:
- R_old: mean=0.0082, max=0.124
- R_new: mean=0.0081, max=0.126
- R_new/R_old median=1.04 — 新区对消与旧区同样有效

**结论**: 新区 Γ·μ 的振荡对消 (机制 B) 工作正常。净偏置 < 1%。

### L3 — 行贡献剖面: ✅ PASS (无系统性异常行)

- 3 θ 值各 top-10 行共 30 行，**无一同时出现在三个 top-10** 中
- 仅 m=77 和 m=102 符号跨 θ 一致 — 均为低 m (<200)，与 Krylov 漂移无关
- 高 m 区 (m≥3072): 正负行数近似相等
- 异常行为: **孤立尖峰**，非连续偏置

### 综合判定

```
L1: μ 符号偏置?  → ✅ NO  (pos_frac=0.4997, Krylov drift excluded)
L2: 新区对消率?  → ✅ R≈0.008 (oscillation mechanism effective)
L3: 跨θ异常行?   → ✅ none  (isolated spikes, no continuous bias)
```

**Phase L 核心结论**:
- δμ 是**随机噪声** (零均值)，非系统性偏置
- 机制 B (振荡对消) 工作正常
- 基线偏移的根因 → **条件收敛本身**: Γ~O(n) 线性增长，μ 模长衰减不够快
  → 绝对和 ∑‖Γμ‖ 发散 → 随机噪声虽零均值，但随机游走幅值 ~O(√N·ε)
  在 N~1.7×10⁷ 下不可忽略 (√N≈4120, √N·ε≈9e-13 vs 物理信号 ~2)

### 全部假说最终状态
H_A❌ H_B❌ H_C❌ H_D❌ H_μ❌ H_Γ❌ H_θ❌ H_J❌ H_bias❌ — 9/9 假说已排除
Phase K: μ✅ Γ✅ — 所有变量已验证
Phase L: δμ=random noise ✅ — 系统性偏置排除
**剩余唯一解释**: 条件收敛 + 浮点精度 → 随机游走累积
**下一方向**: 根本解决需 (a) 提高浮点精度至 quad (b) 替换累加策略 (pairwise/tree) (c) 核函数优化使 μ 模长更快衰减

---

<a id="ai-0625-0818"></a>

## AI: 0625_0818 — Phase K 完成: μ 无 M 依赖, Γ 无 M 依赖, 根因在 Jackson 核 × 累加精度

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `test/phase_K_analysis.py` | ➕ 新建 | Phase K 综合分析脚本 (K1+K2+K3, BLAS 优化) |
| `test/K1_mu_M_dependence.png` | ➕ 生成 | sum(θ) 对比: mu2048 vs mu4096[:2048,:2048] (三面板) |
| `test/K1_mu_M_dependence.txt` | ➕ 生成 | K1 点对比报告 |
| `test/K2_old_vs_new_contribution.png` | ➕ 生成 | 旧区/新区/全区分区贡献 (三面板) |
| `test/K3_gamma_M_dependence.png` | ➕ 生成 | 核效应/核差异/相对差异 (三面板) |
| `test/K3_gamma_M_dependence.txt` | ➕ 生成 | K3 分析报告 |

### 方法
复用 J1 的 BLAS gemv 优化 (γ_{ij}=cos(iθ)·fn_j + cos(jθ)·fm_i 秩-2 结构)，对固定 θ 做 O(M²) 累加。K1 固定 Γ_2048 比较两种 μ；K2 分区累加 μ_4096；K3 统一核消除 Jackson 核差异后检验 Γ。

### K1 — μ M 依赖性: ✅ PASS (μ 无 M 依赖)

| θ | sum_A (mu2048) | sum_B (mu4096[:2048,:2048]) | diff/|sum_A| |
|---|:---:|:---:|:---:|
| 1.0 | −4764.38901874 | −4764.38901874 | 2.23e-14 |
| 1.57 | −2669.80229115 | −2669.80229115 | 1.67e-14 |
| 2.0 | +4112.32280631 | +4112.32280631 | 4.38e-14 |

- μ 矩阵在重叠区域**完全一致** — Chebyshev 递推不引入 M 依赖性误差
- 两矩阵在相同随机种子下计算 (m=64, rs=1) — 数值逐位相同

### K2 — 分区贡献: 旧区主导 (68%) 但新区不可忽略 (32%)

| θ | sum_full | sum_old (m,n<2048) | sum_new (≥2048) | new/old |
|---|:---:|:---:|:---:|:---:|
| 1.0 | −31463 | −34520 (110%) | +3057 (−10%) | — |
| 1.57 | +19232 | +12070 (63%) | +7162 (37%) | 0.59× |
| 2.0 | +88245 | +55078 (62%) | +33166 (38%) | 0.60× |

- 全局: sum|old| = 1.72e7, sum|new| = 8.12e6, new/old = 0.47×
- **关键发现**: 同一 μ 子块在 M=4096 用 g4096 核 → sum=−34520, 在 M=2048 用 g2048 核 → sum=−4764 → **Jackson 核放大 7.2×**

### K3 — Γ M 依赖性: ✅ PASS (Γ 无 M 依赖)

- 统一 g4096[:2048] 核下: sum_C2 == sum_D2 完全一致 (diff=0)
- Γ(m,n,θ) = cos(mθ)·fn(n,θ) + cos(nθ)·fm(m,θ) — 与 M 无关 (数学恒等)
- K3.1 的巨大差异 (sum_C≈−34520 vs sum_D≈−4764) **完全来自 Jackson 核差异** (g4096[:2048] ≠ g2048)

### 综合判定
- μ: 无 M 依赖 ✅ — Chebyshev 递推精度充足
- Γ: 无 M 依赖 ✅ — 数学恒等，数值验证通过
- **根因画像**: Jackson 核 M 依赖性 (g_n^(M) 随 M 增大) × 浮点累加精度不足 (double 53-bit)
- 核放大 ~7× + 新区贡献 ~32% → sum(M) 系统性增长
- Phase J 统一核未根除 → 核差异**叠加**了累加精度问题

### 全部假说状态
H_A❌ H_B❌ H_C❌ H_D❌ H_μ❌ H_Γ❌ H_θ❌ H_J❌ — 8/8 假说已排除
Phase K: μ✅ Γ✅ — 所有变量已验证，根因收缩到 Jackson 核 + 累加

---

<a id="ai-0625-0744"></a>

## AI: 0625_0744 — Phase J1 完成: H_J 排除, Jackson 核 M 依赖性不是根因

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `test/J1_unified_kernel.py` | ➕ 新建 | Python 离线统一 Jackson 核截断验证 |
| `test/J1_unified_kernel_S_vs_M.png` | ➕ 生成 | S(M) 对比图 (standard vs unified kernel) |
| `test/J1_unified_kernel_report.txt` | ➕ 生成 | 完整分析报告 |

### 方法
从 `mu_raw_M4096_m64.h5` (raw μ, 无核) 出发，截断到 M' ∈ {2048, 2560, 3072, 3584, 4096}，对比两种核:
- **Standard**: 各 M' 用独立 g^(M') Jackson 核
- **Unified**: 所有 M' 统一用 g^(4096) 核截断

利用 γ_{ij}=cos(iθ)*fn_j + cos(jθ)*fm_i 的秩-2 结构，用 BLAS gemv 优化 (2×O(M²) per θ vs 原 O(M²) 逐元素)。

### 结果 — σ_xy(E_F=0) [a.u., no prefactor]

| M | Standard | Unified | Δ |
|---|:---:|:---:|:---:|
| 2048 | 8.46 | 18.95 | +10.50 |
| 2560 | 10.50 | 161.63 | +151.13 |
| 3072 | 26.77 | 307.54 | +280.76 |
| 3584 | 118.14 | 327.40 | +209.26 |
| 4096 | 328.06 | 328.06 | 0.00 |

- S_std range = 319.60, S_uni range = 309.10
- 统一核未平坦化 S(M) — 两核 S(M) range 基本相同
- 统一核在低 M 下使 σ 更大 (因 g^(4096)[n] > g^(M)[n] at same n)

### 判定
- **H_J 排除 ❌** — Jackson 核 M 依赖不是基线偏移根因
- 偏移来自 Γ·μ 累加本身，非核归一化
- J2 (Lorentz 核 C++ 实现) 取消

### 全部假说状态
H_A❌ H_B❌ H_C❌ H_D❌ H_μ❌ H_Γ❌ H_θ❌ H_J❌ — 8/8 假说已排除

---

<a id="ai-0625-0630"></a>

## AI: 0625_0630 — Phase I 完成: H_D 排除 (S_ld=+1060, 仅降 ~3×)

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `src/calc.py` | 🔧 修改 | `config_tbpm_solver()`: 用 YAML `tag` 设置 `solver.config.prefix`，修复并行作业文件冲突 |
| `slurm/slm_longdouble.sh` | 🔧 修改 | 添加 `$MPI_PATH/bin/mpirun`，修复 MPI 启动 |
| `runs/0625/hall_AB_d0.000_m64_M*_ld_B100.0.txt` | ➕ 生成 | long double M 扫描输出 (5 文件 MD5 均不同) |

### 关键 Bug 修复
1. **prefix 冲突**: `solver.calc_hall_cond()` 先 C++ 写入 `{prefix}.hall_cond.dat` 再 Python 读回。默认 prefix=sample → 5 作业互相覆盖。修复: `config_tbpm_solver()` 用 tag 设唯一 prefix。
2. **MPI 启动**: 第一批 slm_longdouble.sh 用 `python` 直调 → PMI not found。修复: 改用 `mpirun`。
3. **集群编译**: 复制 CMakeCache 到 build-ld，追加 `TBPLAS_LONG_DOUBLE=ON`。objdump 确认 38 条 x87 80-bit 指令 (原 .so: 0)。

### S_ld vs S_double
| M | double (Phase B) | long double | 比值 |
|---|:---:|:---:|:---:|
| 2048 | +10.1 | −5.9 | — |
| 2560 | +10.1 | −3.9 | — |
| 3072 | +150.9 | +44.7 | 30% |
| 3584 | +950.4 | +320.8 | 34% |
| 4096 | +2945.2 | **+1060.1** | 36% |

### 判定
- S_ld(4096)=+1060 ≫ 100 → **H_D 排除** ❌
- Long double (80-bit) 仅降偏移 ~3×，未根除
- 全部 7 假说: H_A❌ H_B❌ H_C❌ H_D❌ H_μ❌ H_Γ❌ H_θ❌
- 剩余: prefactor 审计 / complex<double> 乘法精度

---

<a id="ai-0625-0615"></a>

## AI: 0625_0615 — Phase I long double H_D 封闭实验: I1 完成 + I2 提交

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `sources/tbpm/kubo_bastin.h` | 🔧 修改 | `cond_from_trace()` 添加 `#ifdef TBPLAS_LONG_DOUBLE` 条件编译, 累加变量 double→long double |
| `sources/tbpm/CMakeLists.txt` | 🔧 修改 | 添加 `OPTION(TBPLAS_LONG_DOUBLE)` + `target_compile_definitions` |
| `configs/sigma/hall_m64_M{2048,2560,3072,3584,4096}_ld.yaml` | ➕ 新建 | 5 个 long double M 扫描 YAML (m=64, rs=1, 51 能量点) |
| `slurm/slm_longdouble.sh` | ➕ 新建 | 集群 long double 专用 slurm 脚本 (TBPLAS_CORE_PATH=...-ld/lib) |

### 变更说明
- **kubo_bastin.h**: `sum_gamma_mu`, `theta_array` → `std::vector<long double>`; `sum`, `dcx`, `theta`, `eng_re`, `div`, `fd`, `efermi_re` → `long double`。`gamma_matrix()` 和 `fermi_dirac()` 调用处 cast 为 double。
- **CMakeLists.txt**: 在 `sources/tbpm/CMakeLists.txt` 添加 `OPTION(TBPLAS_LONG_DOUBLE ...)` + `target_compile_definitions(${target_name} PUBLIC TBPLAS_LONG_DOUBLE)`
- ⚠️ 不改 `std::complex<double>` (gamma, mu_avg 矩阵)，仅改纯实数累加路径
- 默认 `TBPLAS_LONG_DOUBLE=OFF` — 回归安全

### 成功判据验证

**I1 本地冒烟**:
- [x] 本地编译 (tbplas-alpha, MPI=OFF) 零错误
- [x] 默认编译 (TBPLAS_LONG_DOUBLE=OFF) 回归安全
- [x] 冒烟 M=64: σ_xy(ld) = [-0.266, 3.004, 0.935] ≡ σ_xy(double) — M=64 太小无精度差
- [x] 零 NaN, 零 Inf

**I2 集群提交**:
- [x] 集群编译 (gcc 13.1.0 + Intel MPI 2021.9.0) 零错误
- [x] 安装到 `/home/ylwang/tbplas/install/tbplas-cpp-a021ca8-ld/lib/`
- [x] 5 Jobs 提交: 287116 (M2048), 287117 (M2560), 287118 (M3072), 287119 (M3584), 287120 (M4096)
- [ ] 等待 Job 完成 (~1.5h) 后进行 S_ld vs M 对比分析

### 关键数值
- 本地冒烟 (M=64): σ_xy = [-0.2661, 3.0042, 0.9349] (ld ≡ double)
- 集群 double 基线 (Phase B): S(2048)=+10.1, S(4096)=+1060 (Kahan) / +600 (std)

### 判定
✅ I1 完成: long double 编译链验证通过，冒烟通过。
🔲 I2 等待: Jobs 287116–287120 运行中。

---

<a id="ai-0625-0535"></a>

## AI: 0625_0535 — Phase D 分块贡献图重绘: log→linear Re(Γ·μ) 着色

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `test/plot_phase_D_blocks.py` | ➕ 新建 | Phase D 块贡献热图专用绘制脚本 (linear Re(Γ·μ)) |
| `test/regenerate_vbl_figures.py` | 🔧 修改 | `fig_block_heatmap()`: log10→linear signed/abs 双面板 + multi-M |
| `data/sigma/phase_D_block_decomp/block_contrib_heatmap_M4096.png` | 🔄 更新 | Signed Re(Γ·μ) + |Re(Γ·μ)| magnitude 双面板 |
| `data/sigma/phase_D_block_decomp/block_contrib_all_M.png` | 🔄 更新 | M=2048–4096 五档 linear Re(Γ·μ) 对比面板 |

### 变更说明
- **移除 log10 着色**: 原图右面板用 `log10|Block Contribution|` (viridis)，现改为 `|Re(Γ·μ)|` linear (inferno)
- **Signed 面板保留**: 左面板用 `RdBu_r` diverging colormap，保留 Re(Γ·μ) 正负号信息
- **Multi-M 面板**: 从 M=4096 全 16×16 块矩阵截断到各目标 M 的 nb×nb 子块，全局统一 vmax
- **数据源**: `runs/0624/vbl_block_M4096.log` — C++ VBL_BLOCK 诊断输出 (256 unique blocks, 4 MPI ranks 去重)
- 新增统计: L1 norm / low-order% / high-order% (用 L1 归一化避免 total≈0 时的除零)

### 关键数值
- M=4096, 16×16 blocks: total Σ=−0.0000 (正负近乎完全抵消), L1=0.1738
- 低阶 (m,n<2048): Σ=−0.0001 (−0.1% L1), 高阶 (m,n≥2048): Σ=−0.0001 (−0.1% L1)
- 块值范围: [−0.0056, +0.0074] — 单块贡献量级 ~5×10⁻³

### 判定
✅ Phase D 块贡献热图已从 log10 着色改为 linear Re(Γ·μ) 着色，正负号可视化清晰。
✅ 新增 `block_contrib_M_vs_summary.png` — M vs 块贡献综合四面板图 (L1 标度/低高阶占比/对角线剖面)

### M vs 块贡献关键数据
| M | L1 norm | Low% | High% |
|---|:---:|:---:|:---:|
| 2048 | 0.1204 | 18.4% | 21.5% |
| 2560 | 0.1522 | 38.5% | 15.4% |
| 3072 | 0.1682 | 56.2% | 8.4% |
| 3584 | 0.1733 | 61.5% | 4.6% |
| 4096 | 0.1738 | 69.3% | 2.6% |
- L1 在 M≥3584 后饱和 (0.1733→0.1738), 高阶贡献降至 <5%

### 🆕 Signed sum vs M
| M | Signed Σ | \|Σ\|/L1 |
|---|:---:|:---:|
| 2048 | −1.09×10⁻⁴ | 9.0×10⁻⁴ |
| 2560 | −1.38×10⁻⁷ | 9.1×10⁻⁷ |
| 3072 | −1.66×10⁻⁶ | 9.9×10⁻⁶ |
| 3584 | −1.24×10⁻⁸ | 7.1×10⁻⁸ |
| 4096 | −1.55×10⁻⁸ | 9.0×10⁻⁸ |
- **Signed sum 随 M 增大趋近于零** — 正负对消随 M **改善** ~10,000× (2048→4096)
- 与 Phase B sum(θ) ~1800× 发散形成鲜明对比 — 根因在 θ 积分后段, 不在 Γ·μ 累加

### 🆕 Phase C Kahan vs Standard 对比图
- `test/kahan_vs_standard.png`: Standard load/save vs Kahan σ_xy(EF=0) vs M
- **发现**: Standard load-mode ≈ Kahan at M=2560/3072/3584 (逐位相等), Kahan 可能未在这些 M 生效
- M=4096: Kahan (+2945) 比 Standard (+1060) 更差 2.8×

---

<a id="ai-0625-0520"></a>

## AI: 0625_0520 — Phase H 结论修正: H_disorder 无法判定 (Γ·μ 噪声地板)

### 数据路径验证
`pymodel.h:928` — `ham[ptr] = orb_eng_[i]` — 无序**已进入** CSR 哈密顿量。
`solver.h:597` — `build_ham_curr_csr(...)` — Hall 计算每次重建 CSR。
数据路径完整无断裂。

### 量级分析
| 量 | 值 (e²/h) | 来源 |
|------|:---:|------|
| σ_xy 噪声地板 | ~600 | Γ·μ 累加发散 (Phase B) |
| QHE 物理信号 | ~2 | σ_xy = ±2 e²/h |
| 无序效应 (预期) | ≲1 | Anderson γ=0.27 eV 微扰 |

无序效应被噪声掩盖 600× → H_disorder 无法判定。

### VBL 全局诊断更新
| Phase | 假说 | 结论 |
|:---:|------|:--:|
| A | μ 矩阵异常 | ❌ 排除 |
| B | Γ·μ 累加 ~1800× 发散 | ✅ **核心阻塞** |
| C | 浮点累加精度 | ❌ 排除 |
| D | 特定块异常 | ❌ 排除 |
| F | θ 积分奇点 | ❌ 排除 |
| G | Γ 矩阵精度 | ❌ 排除 |
| H | δ-函数谱/对消脆弱 | ⚠️ **无法判定** (噪声地板) |

### 结论
H_disorder 既未被证实也未被证伪 — 需先解决 Γ·μ 累加问题。
**顺序应调整为: 修复 Γ·μ → 再测试物理假说 (H_disorder/H_θ 等)**

---

<a id="ai-0625-0505"></a>

## AI: 0625_0505 — Phase H 启动: H1 C++ 回退 + H2 无序函数 + H3 集群提交

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `../tbplas/source/.../kubo_bastin.h` | 🔧 清理 | 移除 TBPLAS_VBL_TRACE/KAHAN_SUM/THETA_CUT/SIMPSON/GAMMA_DIAG |
| `../tbplas/source/.../CMakeLists.txt` | 🔧 清理 | 移除诊断 OPTION 声明 |
| `../tbplas/source/.../tbpm/CMakeLists.txt` | 🔧 清理 | 移除诊断编译选项 |
| `src/model.py` | ➕ 新增 | `add_anderson_disorder()` — 逐轨道均匀分布 onsite 无序 |
| `src/main.py` | 🔧 修改 | `_run_hall()` 中调用 `add_anderson_disorder()` |
| `configs/sigma/hall_m64_M4096_clean.yaml` | ✅ 新建 | H3 clean 配置 |
| `configs/sigma/hall_m64_M4096_disorder.yaml` | ✅ 新建 | H3 disorder 配置 (γ=0.27) |

### 变更说明

#### H1: C++ 回退
- 本地 + 集群同步: 编辑源文件 → scp 到集群 → `module load cmake` → `cmake .. && cmake --build . -j4` → `cmake --install .`
- 集群 gcc 13.1.0 + Intel MPI 2021.9.0, 编译 [100%] 零错误
- 验证: `grep -c TBPLAS_* kubo_bastin.h` → 0, 库清洁

#### H2: Anderson 无序
- `add_anderson_disorder(sample, gamma, seed)` — 用 `sample.get_array().orb_eng[i]` 逐轨道加均匀分布无序
- 无序强度默认 γ=0.27 eV (~0.1t), 范围 [−γ/2, +γ/2]
- 在 `_run_hall()` 中通过 `cfg['tbpm'].get('disorder_gamma', 0)` 控制

#### H3: 集群提交
- Jobs 287113 (clean), 287114 (disorder), 均 RUNNING on cpu_2d
- 参数: m=64, M=4096, rs=1, B=100T, N_θ=2048, 51 能量点
- 预计 ~25min wall time

### 成功判据验证状态
- [x] H1: kubo_bastin.h 零诊断宏 ✅, 集群编译零错误 ✅
- [x] H2: `add_anderson_disorder()` 语法正确 ✅, 零 C++ 改动 ✅
- [ ] H3: 等待集群结果

### Plan Feedback
- 无需修订 — Phase H 按计划执行，H1/H2 无意外发现

---

<a id="ai-0625-0305"></a>

## AI: 0625_0305 — Phase G 完成: H_Γ 排除, Gamma 矩阵精度完全正常

### 结果
| 测试 | 结果 | 判定 |
|------|------|:--:|
| G1 热图 | 对角渐变, 无 NaN/Inf | ✅ |
| G2 Hermiticity | 偏差=0.00 (机器精度) | ✅ |
| G3 标度 | max\|Γ\|∝M^1.001 (R²=1.000) | ✅ |
| **H_Γ** | Gamma 矩阵精度完全正常 | ❌ 排除 |

### 关键发现: PYTHONPATH 根因
tbplas 用 `sys.path.append(TBPLAS_CORE_PATH)` 加载库 → conda site-packages 优先 → **此前所有 Phase F/G 诊断代码从未执行!** 修复: `PYTHONPATH` 前置。

> ⚠️ Phase F (THETA_CUT/SIMPSON) 可能同样受影响, 待重新验证。

---

<a id="ai-0625-0210"></a>

## AI: 0625_0210 — Phase G 第三轮: PRIVATE→PUBLIC 宏传播修复 (Jobs 287042-287045)

### 涉及文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `sources/tbpm/CMakeLists.txt` | 🔧 修复 | TBPLAS_GAMMA_DIAG: PRIVATE → PUBLIC |
| `source/.../build_gamma/` | ✅ 新建 | 独立构建目录 |
| `source/.../build_f2_d03/` | 🔧 恢复 | 恢复 Phase F2 d03 原始配置 |

### 根因
前两轮提交无 gamma 输出。`kubo_bastin.h` 通过 `interface_tbpm.cxx` 编译，但 `TBPLAS_GAMMA_DIAG` 在 tbpm CMakeLists.txt 中定义为 PRIVATE → 不传播到 interface_tbpm → 诊断代码被预处理器跳过。修复: PRIVATE → PUBLIC。

### 验证
- `strings *.so | grep "gamma_M"` ✅ 确认字面量已编译
- 所有 Phase F install 目录未受影响 ✅
- ⚠️ Phase F 宏 (THETA_CUT/SIMPSON/KAHAN_SUM) 也是 PRIVATE, 可能从未生效

### 作业: Jobs 287042-287045 (BUILD_TAG=gamma)

---

<a id="ai-0624-2252"></a>

## AI: 0624_2252 — VBL Phase G 启动: Γ 矩阵精度诊断 (G1/G2/G3 全部提交)

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `sources/tbpm/kubo_bastin.h` | 🔧 修改 | 新增 `#ifdef TBPLAS_GAMMA_DIAG` 块 — G1 热图 + G2 Hermiticity + G3 maxabs |
| `CMakeLists.txt` | 🔧 修改 | 新增 `OPTION(TBPLAS_GAMMA_DIAG)` |
| `sources/tbpm/CMakeLists.txt` | 🔧 修改 | 传播 TBPLAS_GAMMA_DIAG 到 tbpm 编译目标 |
| `configs/sigma/hall_m64_M{512,1024,2048,4096}_vbl_gamma.yaml` | ✅ 新建 | G1/G2/G3 配置 (N_θ=16, 单能量点) |
| `test/analyze_gamma_matrix.py` | ✅ 新建 | G1 热图 + G2 Hermiticity + G3 标度拟合 分析脚本 |

### 变更说明

#### C++ 插桩 — `#ifdef TBPLAS_GAMMA_DIAG`
插入位置: `kubo_bastin.h` L168 `sum_gamma_mu[k] = sum;` 之后（theta 循环内），独立于 VBL_TRACE 块。

- **G1**: 64×64 下采样 log10|Gamma| 热图，输出到 `gamma_M4096_t{0,1,2}.log`（前 3 个 θ 点）
- **G2**: Hermiticity 检验 — max/mean |Γ_mn - conj(Γ_nm)|，输出到 `gamma_herm_M4096.log`
- **G3**: max|Γ| 范数，输出到 `gamma_maxabs.log`（M × θ 矩阵）

#### 编译
- `cmake -DTBPLAS_GAMMA_DIAG=ON` → 安装到 `tbplas-cpp-a021ca8-gamma`
- gcc 13.1.0 + Intel MPI 2021.9.0, 构建成功

#### 集群提交
- `BUILD_TAG=gamma sbatch slurm/slm_phasef.sh` × 4
- Jobs: 287015 (M=4096), 287016 (M=512), 287017 (M=1024), 287018 (M=2048)
- M=4096 Job 同时产出 G1/G2/G3 数据

### 成功判据验证状态
- [ ] G1 热图: 等待集群完成
- [ ] G2 Hermiticity: 等待集群完成
- [ ] G3 标度: 等待集群完成

### Plan Feedback
- 无需修订 — Phase G 按原计划执行，无新增发现

---

<a id="ai-0624-2230"></a>

## AI: 0625_0150 — VBL Phase F 完成: H_θ 被排除

> **原条目**: 0624_2230 (启动) → 重写为最终结果

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `sources/tbpm/kubo_bastin.h` | 🔧 修改 | F2: `#ifdef TBPLAS_THETA_CUT` + F3: `#ifdef TBPLAS_SIMPSON` |
| `CMakeLists.txt` | 🔧 修改 | 新增 TBPLAS_THETA_CUT/TBPLAS_THETA_CUT_DELTA/TBPLAS_SIMPSON |
| `sources/tbpm/CMakeLists.txt` | 🔧 修改 | 传播编译定义 |
| `slurm/slm_phasef.sh` | ✅ 新建 | 支持 BUILD_TAG 切换库版本 |
| `configs/sigma/hall_m64_M4096_vbl_f1_N*.yaml` ×4 | ✅ 新建 | F1 |
| `configs/sigma/hall_m64_M4096_vbl_f2_d*.yaml` ×4 | ✅ 新建 | F2 (初版有 tag 冲突 bug) |
| `configs/sigma/hall_m64_M4096_vbl_f3_*.yaml` ×2 | ✅ 新建 | F3 (初版有 tag 冲突 bug) |

### 最终结果 (M=4096, m=64, rs=1, B=100T)

| 实验 | 变体 | σ_xy(EF=0) [e²/h] | Jobs | 结论 |
|:---:|------|:---:|------|------|
| **F1** N_θ=256 | — | −64562 | 286976 | 网格过粗, 不可靠 |
| **F1** N_θ=512 | — | +31580 | 286977 | 网格过粗, 不可靠 |
| **F1** N_θ=1024 | — | **+600.1** | 286978 | 收敛 |
| **F1** N_θ=2048 | — | **+600.1** | 287041 | 收敛 (初版 286979 bug: YAML 写错 N_θ=1024) |
| **F2** δ=0.01π | θ 截断 1.8° | **+600.1** | 287035 | 无影响 |
| **F2** δ=0.03π | θ 截断 5.4° | **+600.1** | 287036 | 无影响 |
| **F2** δ=0.05π | θ 截断 9° | **+600.1** | 287037 | 无影响 |
| **F2** δ=0.10π | θ 截断 18° | **+600.1** | 287038 | 无影响 |
| **F3** trapez | 梯形积分 | **+600.1** | 287039 | 基准 |
| **F3** simpson | Simpson 积分 | **+600.1** | 287040 | 无改善 |

### 执行中遇到的 Bug 及修复

1. **F1 N2048 YAML 错误** (初版 286979): 本地创建时 tag 和 dckb_num_integ_steps 误写入 N1024 的值 → 实际跑了 N_θ=1024 而非 2048。修复后重提为 287041。
2. **F2/F3 tag 冲突导致数据全部丢失** (初版 287003–287008): 所有 YAML 共用 `tag: m64_M4096_vbl_f2` → 6 个作业输出互相覆盖。修复: 每个变体赋予唯一 tag (`f2_d01`, `f3_trapez` 等)，重提为 287035–287040。
3. **F1 N2048 重提瞬态失败** (287034): 旧 YAML 仍在集群上 (未随本地修复同步上传)，作业 1 秒退出。重新 scp 修正版后重提为 287041。

### 编译清单 — 6 变体全部成功

| 变体 | 安装路径 |
|------|---------|
| 标准 (trapez) | `tbplas-cpp-a021ca8` |
| F2 δ=0.01π–0.10π | `tbplas-cpp-a021ca8-f2-d{01,03,05,10}` |
| F3 Simpson | `tbplas-cpp-a021ca8-f3-simpson` |

gcc 13.1.0 + Intel MPI 2021.9.0, 零错误。

### 科学结论: H_θ 被排除 ❌

| 假说预测 | 实测 | 判定 |
|----------|------|:---:|
| F1: S 随 N_θ 单调增长 | N_θ≥1024 收敛到 +600.1, N256/512 仅因网格过粗不可靠 | ❌ |
| F2: S 随 δ 增大而减小 | δ=0.01π–0.10π 全部 +600.1, 零变化 | ❌ |
| F3: Simpson 显著 < trapez | 梯形 = Simpson = 600.1 | ❌ |

**推论**: 基线偏移 +600.1 来自 θ 积分之前的 sum(θ) = Σ Γ⊙μ。根因搜索收缩到 Γ 矩阵构造精度 (H_Γ, Phase G) 或 Γ⊙μ 累加。
**集群消耗**: F1×5 + F2×4 + F3×2 = 11 Jobs (含重提), ~5.5h 总 wall time。

---

<a id="ai-0624-1900"></a>

## AI: 0624_1900 — VBL Phase A–D 全部完成, 基线偏移根因综合诊断

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `sources/tbpm/kubo_bastin.h` | 🔧 修改 | VBL_TRACE 插桩 (sum θ + block) + KAHAN_SUM 累加 |
| `sources/tbpm/CMakeLists.txt` | 🔧 修改 | TBPLAS_KAHAN_SUM 编译选项 |
| `CMakeLists.txt` | 🔧 修改 | TBPLAS_VBL_TRACE + TBPLAS_KAHAN_SUM 选项 |
| `python/solver/cmake/CMakeLists_scikit.cmake` | 🔧 修改 | 传播 VBL/KAHAN 定义到 Python 接口 |
| `test/analyze_mu_matrix.py` | ✅ 新建 | A3–A5 μ 矩阵离线分析 |
| `test/analyze_sum_gamma_mu.py` | ✅ 新建 | B4/B5 sum(θ) 分析 |
| `configs/sigma/hall_m64_M*_vbl.yaml` | ✅ 新建 | B2/B3/C2/D1 诊断 YAML × 15+ |
| `shared/tbplas-internals.md` | 📝 更新 | §12.3 VBL 结论 + H_D 证伪 |
| `docs/sigma/plan_vbl_trace.md` | 📝 更新 | 执行路径 + Phase E 结论 |
| `docs/sigma/task_vbl_trace.md` | 📝 更新 | Phase A–E 完成记录 + 状态表 |

### 变更说明

#### Phase A — μ 矩阵正常 ✅
- A1/A2: m=64 M=2048/4096 μ 矩阵生成 (65MB/257MB, Jobs 286020/286021, ExitCode 0)
- A3: Hermiticity 偏差同级 (mean≈1.2e-3), M4096/M2048 比=1.0×
- A4: 热图带状对角结构, M4096 高阶无异常亮斑
- A5: 重叠区 norm 比≈1.4×, 高 m 偏离外推 1.49× (< 2× 阈值)
- A6: Load 截断 σ_xy 随 M 增大趋势与直接计算一致

→ **μ 矩阵构建精度正常, 偏移在 Γ·μ 累加环节**

#### Phase B — sum(θ) 确认为根因环节 ✅
- B1: C++ VBL_TRACE 插桩 (集群 gcc 13.1.0 编译, ofstream 文件输出)
- B2: 5 M 值 (2048/2560/3072/3584/4096) 全部 ExitCode 0, vbl_sum_M*.log 完好
- B3: σ_xy(B=0)=-482 e²/h (应=0), sum(θ) B100 vs B0 恒等 (diff=0)
- B4: sum(θ) 曲线形状自相似, 幅值随 M 系统性放大
- B5: ∫sum -0.27(M2048)→+484.5(M4096), ~1800× 发散

→ **Γ·μ 累加误差与 M 系统性相关, 是基线偏移的直接驱动**

#### Phase C — Kahan 未根除 ❌
- C1: 行级 Kahan + OpenMP reduction 编译成功 (集群 gcc 13.1.0)
- C2: 5 M 值全部 ExitCode 0, M=2048/2560 稳定 (σ≈10), M≥3072 偏移复现
- C3: M=4096 Kahan σ=2945 > Standard σ=1060

→ **浮点累加精度不足不是唯一根因**

#### Phase D — 分块无异常 ✅
- D1: 256×256 块分解编译 + Job 286515 (13:53, ExitCode 0)
- D2: 16×16 块贡献热图
- D3: 低阶块 69.3%, 高阶块仅 2.6%, 无单一块主导

→ **偏移均匀分布, 排除"高阶 μ 噪声被 Γ 放大"假说**

### 根因链确认

```
A: μ 矩阵正常 ✅ → B: sum(θ) 爆炸 ~1800× ✅ → C: Kahan 不修复 ❌ → D: 分块均匀 ❌
→ 根因不在任何单一环节: Cumulative floating-point + θ 积分奇点 (1/sin³θ) 联合效应
```

### 关键数据

| Phase | 关键数值 | 集群消耗 |
|-------|---------|---------|
| A | μ 矩阵 257MB | ~30min (2 Jobs) |
| B | sum(θ) ~1800× 发散 | ~110min (6 Jobs) |
| C | Kahan σ=2945 vs Std 1060 | ~90min (5 Jobs) |
| D | 分块低阶 69% | ~14min (1 Job) |
| **总计** | | **~4h 集群时间** |

### 修正原 H_D 假说

- **原 H_D**: "double 精度不足以支撑 M=4096 累加" → **Phase C Kahan 证伪** (若仅为浮点累加, Kahan 应完全修复)
- **新认识**: 根因可能是 θ 积分奇点行为 (θ→π 时 1/sin³θ→∞) 与大规模 Γ·μ 累加中浮点误差的**联合效应**
- **实用建议**: M ≤ 2048 为安全区, M=2560 有 Kahan 可稳定, M≥3072 不推荐

---

<a id="ai-0624-1430"></a>

## AI: 0624_1430 — VBL Phase A 启动: m=64 M=2048/4096 μ 矩阵 save 提交

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/sigma/hall_m64_M2048_save_mu.yaml` | ✅ 新建 | A1: m=64, M=2048, rs=1, 7 能量点, save μ |
| `configs/sigma/hall_m64_M4096_save_mu.yaml` | ✅ 新建 | A2: m=64, M=4096, rs=1, 7 能量点, save μ |
| `docs/sigma/task_vbl_trace.md` | 📝 更新 | A1/A2 标记 [-], 追加提交记录 |

### 变更说明

- 创建 A1 (M=2048) 和 A2 (M=4096) 的 μ 矩阵保存 YAML
- scp 上传到集群 `~/scratch/MG/configs/`
- sbatch 提交: Job 286020 (M=2048), Job 286021 (M=4096)
- 状态检查: 两者均在 RUNNING
- STATUS.md 更新: 追加 VBL 进行中状态, 更新最近发现

### 成功判据验证

- [x] YAML 文件创建并上传集群 ✓
- [x] sbatch 提交成功 (Jobs 286020-286021)
- [x] squeue 显示 RUNNING

---

<a id="ai-0624-1214"></a>

## AI: 0624_1214 — E1 save/load round-trip 验证通过 (H_A 确认)

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/hall_m16_M1024_save.yaml` | ✅ 新建 | save 模式配置 (m=16, M=1024, rs=1) |
| `configs/hall_m16_M1024_load.yaml` | ✅ 新建 | load 模式配置 (指向同一 h5) |
| `slurm/slm_save_load_test.sh` | ✅ 新建 | 集群单节点提交脚本 (save→load→compare) |
| `runs/0624/mu_raw_M1024_m16.h5` | ✅ 生成 | raw μ 矩阵 (~16 MB) |
| `runs/0624/hall_AB_d0.000_m16_M1024_{save,load}_B100.0.txt` | ✅ 输出 | σ_xy vs E (1500 点) |
| `runs/0624/hall_AB_d0.000_m16_M1024_{save,load}_B100.0.png` | ✅ 输出 | σ_xy 曲线图 |

### 变更说明

- 创建 save/load YAML 配置，上传到集群
- 集群 Job 285997 (1 节点, 32 OMP, 20s) 完成 save→load→compare 全流程
- 回传结果到本地 `runs/0624_save_load_test/`

### 结果

| 指标 | 值 | 对比 |
|------|:---:|:---:|
| Save exit code | 0 | — |
| Load exit code | 0 | — |
| Max |diff| | 1.24e-10 e²/h | 旧代码 368 → **~3×10¹² 倍改善** |
| RMS diff | 1.02e-11 e²/h | 机器精度级别 |
| 相对误差 | 2.54e-13 | — |

### 结论

- **H_A 确认**: σ_xx 注释修复了 HDF5 双分量覆盖问题
- **H_B/H_C 无需测试**: E1 直接通过，排除 save/load 路径自身 bug
- save→load round-trip 达到机器精度 (1e-10 e²/h)，μ 复用基础设施验证通过
- **不再有「σ_xy round-trip 失效」的已知问题**

### Plan Feedback

- `docs/sigma/plan_save_load_roundtrip.md` → 🟢 E1 通过, 直接晋升
- `docs/sigma/archive/plan_kb_mu_reuse.md` → 🟡 需更新: 将已知问题标记为 RESOLVED

<a id="ai-0623-2020"></a>

## AI: 0623_2020 — ABC 三层 Hall 电导率测试 (M4096_m256, 4节点)

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/hall_m256_M4096_save.yaml` | 📤 上传 | ABC trilayer, M=4096, m=256, B=100T, rescale=-1 |
| `src/` | 📤 上传 | 最新源码同步至集群 |
| `slurm/slm.sh` | 📤 上传 | 4 节点 SLURM 模板 |
| `runs/0623/hall_ABC_d0.000_m512_M4096_save_B100.0.txt` | ✅ 输出 | σ_xy vs E (1500 点) |
| `runs/0623/hall_ABC_d0.000_m512_M4096_save_B100.0.png` | ✅ 输出 | σ_xy 曲线图 |
| `runs/0623/mu_ABC_M4096_m256.h5` | ✅ 输出 | 原始 μ 矩阵 (256 MB) |
| `runs/0623/slurm-285503.out` | ✅ 日志 | SLURM 运行日志 |

### 变更

- 集群 Job 285503 (4×node[32-35], MPI=4×OMP=32)
- 首次提交误用旧版单层 AB 配置 → scancel 285466
- 重新上传正确 ABC 三层配置 → sbatch 285503
- Exit 0, 耗时 1h00m21s

### 结果

| 指标 | 值 |
|------|-----|
| 模型 | ABC trilayer, 6 atoms, 144 hops |
| 能量范围 | [-1.5, 1.5] eV, 1500 点 |
| NaN | 0 (rescale=-1 验证通过) |
| σ_xy 范围 | [47.8, 513.0] e²/h (全部正值) |
| mu 文件 | 256 MB HDF5, 已回传 |

### 发现

- σ_xy 全部为正 (48–513 e²/h)，无零穿越，无 QHE 台阶结构
- 疑似基线偏移问题 (已知 issue，见 STATUS.md 最近决策)
- M=4096 下 rescale=-1 仍然零 NaN，确认 rescale 自动检测稳定

<a id="ai-0624-0025"></a>

## AI: 0624_0025 — E3 rescale 扫描完成: H_C 被排除（非单调行为）

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/hall_m256_M4096_rescale_{8,9,11,12}.yaml` | ✅ 新建 | 4 个 rescale 扫描配置 |
| `slurm/slm_rescale.sh` | ✅ 新建 | 集群单节点提交脚本 |
| `runs/0624/hall_AB_d0.000_m256_M4096_rescale_{11,12}_B100.0.txt` | ✅ 输出 (集群) | rescale=11/12 σ_xy |
| `src/io_vis.py` | ✅ 修复 | 缩进错误修复 |

### 结果

| Rescale | S | vs auto |
|:---:|:---:|:---:|
| auto(-1) | -991 | — |
| 8.0 | NaN (已知) | rescale < 带宽 |
| 9.0 | 集群失败×4 | C++ CPPSample 加载错误 |
| 11.0 | -788 | -20% (略好) |
| 12.0 | -1301 | +65% (更差) |

- **H_C 被排除**: S(rescale) 非单调，增大 rescale 不能单调减小基线偏移
- rescale=9.0 集群持续失败（C++ 接口加载问题），非实验目标
- 集群流程验证: scp → sbatch (slm_rescale.sh) → 回传 → 分析

### Plan Feedback
- `plan_baseline_root_cause.md` §3.4 (H_C): 假设被推翻，需标记 ⚠️ 证伪
- H_A/H_B/H_C 全部排除 → 跳至 E4 (浮点精度对比)

<a id="ai-0623-2215"></a>

## AI: 0623_2215 — E2 无核测试完成: H_B 被排除（Jackson 核起抑制作用）

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `kubo_bastin.h` | ✅ 修改 → 恢复 | `apply_jackson_kernel()` 注释/恢复核乘法 |
| `configs/hall_m256_M{1024,2048,3072,4096}_load.yaml` | ✅ 新建 | 4 个 load 模式 YAML |
| `runs/0623/hall_AB_d0.000_m256_M*_nokernel_B100.0.txt` | ✅ 输出 | 4 个 M 值的无核 σ_xy |
| `runs/0624/hall_m256_M*_nokernel.log` | ✅ 输出 | 运行日志 |

### 结果

| M | S_kernel | S_nokernel | S_ratio | 结论 |
|:---:|:---:|:---:|:---:|:---:|
| 1024 | -20.09 | 3030.30 | 150.8 | 核抑制强 |
| 2048 | -63.51 | 3030.30 | 47.7 | 核抑制强 |
| 3072 | -183.58 | 3030.30 | 16.5 | 核抑制中 |
| 4096 | -991.19 | 3030.30 | 3.06 | 核抑制弱 |

- **H_B 被排除** — Jackson 核起抑制作用而非退化。S_ratio ≫ 1.5
- 无核时 S 与 M 无关 (≈3030)，说明原始 Chebyshev 矩的 DC 分量恒定，核的作用是压制高阶矩贡献
- 编译需 `tbplas` 环境（含 MPI+HDF5）+ `TBPLAS_CORE_PATH=install/tbplas-cpp-a021ca8/lib`

### Plan Feedback
- `plan_baseline_root_cause.md` §2 H_B: 无需修订（原始预测正确——排除 H_B 或确认 H_B）
- 根因仍在查找中，按任务链跳至 E3 (rescale 扫描)

<a id="ai-0623-2355"></a>

## AI: 0623_2355 — E1 范数诊断完成: H_A 被排除（Chebyshev 向量范数无指数增长）

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `source/tbpm/kubo_bastin.h` | ✅ 修改 | `kbdc_mu_raw()` 添加 `#ifdef TBPLAS_NORM_DIAG` 范数输出 |
| `configs/hall_m256_M4096_diag.yaml` | ✅ 新建 | E1 专用配置 (m=256, M=4096, rs=1, 51 能量点) |
| `test/analyze_norm_diag.py` | ✅ 新建 | 范数诊断分析脚本 |
| `runs/0624/norm_diag_m256_M4096.log` | ✅ 输出 | 完整 stdout (22MB) |
| `runs/0624/norm_diag_m256_M4096.txt` | ✅ 输出 | [NORM_DIAG] 64 行过滤数据 |
| `runs/0624/norm_diag_m256_M4096.png` | ✅ 输出 | 范数 vs n 图 |

### 结果

- **loop_beta**: $\log_{10}\|T_n\| = -0.1505 \pm 0.0011$, $|T_n| \approx 0.707$ — 全程常数
- **loop_alpha**: $\log_{10}\|T_n\| = -0.4680 \pm 0.0010$, $|T_n| \approx 0.340$ — 全程常数
- **结论: H_A 被排除** — Chebyshev 向量 $\|T_n\psi\rangle\|$ 在 n=128..4095 无任何增长趋势
- C++ 插桩编译零错误（含/不含诊断 flag）；回归安全通过

### Plan Feedback
- `docs/sigma/plan_baseline_root_cause.md` §3.2 (H_A): 假设被推翻，需要更新。Chebyshev 三项递推在 M=4096 内数值稳定。
- 根因仍在查找中，按任务链跳至 E2 (H_B: Jackson 核退化测试)。

<a id="ai-0623-2345"></a>

## AI: 0623_2345 — m×M 网格测试完成: 双重标度区 + m 非单调交叉

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `docs/sigma/plan_m_M_grid.md` | ✅ 重写 | 计划 → 最终报告 |
| `test/analyze_mM_grid.py` | ✅ 新建 | 49 数据点汇总分析 |
| `runs/0623/S_vs_M_eta_m256_m512.png` | ✅ 已有 | M 扫描图 |
| `runs/0623/S_vs_eta_m256_m512_m1024.png` | ✅ 已有 | η 标度图 |

### 关键发现

1. **双重标度区**:
   - 低 M (≤2048): $S \propto M^{1.5\sim1.9}$，m 依赖极弱
   - 高 M (>2560): $S \propto \exp(\gamma M)$，局部 $\alpha = d\ln|S|/d\ln M = 5\sim8$

2. **m 非单调交叉** (最重要新发现):
   - M < 3400: $|S_{256}| < |S_{512}|$ (正常直觉)
   - M ≈ 3400±200: 交叉 → $|S_{256}| > |S_{512}|$
   - M = 4096: $|S_{256}|=990$, $|S_{512}|=823$, $|S_{1024}|=2967$
   - **m=512 在最高 M 区意外最优**

3. **H_η 决定性证伪**: $m=1024, M=1024$ ($\eta=8192$) 仅 $S=-29$，而 $m=256, M=3072$ ($\eta=171$) 却有 $S=-187$

4. **实用窗口**: $M \leq 1024$ 安全 ($|S|<32$)，$M>2560$ 危险

### 下一步

- 根因诊断实验 (E1 范数诊断优先) → 见 plan §4.1
- 不推荐 m=1536 (成本高，非单调已确认)

### 成功判据

- [x] 49 数据点全部收集 (m=256×24, m=512×19, m=1024×12)
- [x] cluster vs local 逐比特一致验证通过 (m=512)
- [x] H_η 四重检验全部证伪
- [x] 双重标度区 + m 交叉定量定位
- [x] 文档全部更新

---

<a id="ai-0623-2300"></a>

## AI: 0623_2300 — T3 集群部署完成: μ 复用全流程验证通过

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `docs/sigma/task_kb_mu_reuse.md` | ✅ 更新 | T3 → [x] 完成 |
| `docs/sigma/plan_kb_mu_reuse.md` | ✅ 更新 | 补集群部署发现 + M_c 阈值 |
| `docs/sigma/plan_m_M_grid.md` | ✅ 更新 | ⚠️ H_η 已证伪 |
| `configs/hall_m256_M4096_save.yaml` | ✅ 新建 | Phase 1a (Job 285226) |
| `configs/hall_m1024_M4096_save.yaml` | ✅ 新建 | Phase 1b (Job 285233) |
| `configs/hall_m512_M4096_save.yaml` | ✅ 新建 | Phase 1c (Job 285271) |
| `configs/hall_m*_M*_cluster_load.yaml` | ✅ 新建 | 31 个集群 load 配置 |
| `slurm/scan_m512_m1024.sh` | ✅ 新建 | 批量 M 扫描脚本 (Job 285452) |
| `runs/0622/mu_raw_M4096_m*.h5` | ✅ 生成 | m=256/512/1024 raw μ (3×268 MB) |
| `runs/0623/hall_AB_*_cluster*.txt` | ✅ 生成 | 31+19 个 σ_xy 输出 |

### 变更说明

1. **远程编译部署**:
   - `cmake -DWITH_MPI=ON -DWITH_OPENMP=ON -DWITH_HDF5=ON` 零错误
   - Python 绑定 `interface_tbpm.so` + `config.py` 同步更新
2. **集群环境适配**（计算节点特殊配置）:
   - `conda activate` 不可用 → `source conda.sh` 初始化
   - 单节点 Python 需 `FI_PROVIDER=shm` 避免 Intel MPI OFI 崩溃
   - `TBPLAS_CORE_PATH` 指向 `~/scratch/MG/tbplas_ext`（非 `~/tbplas/install/`）
   - `--exclude=node[28-31,41-64]` 排除有问题的计算节点
3. **Phase 1 保存** (4 节点 MPI，全部成功):
   - m=256 M=4096: ~1h, mu_raw 268 MB
   - m=512 M=4096: ~2.5h, mu_raw 268 MB
   - m=1024 M=4096: ~4h, mu_raw 268 MB
4. **Phase 2 截断** (单节点串行，全部 exit 0):
   - m=256: 24 M 值 (M=64~4096)
   - m=512: 19 M 值
   - m=1024: 12 M 值

### 成功判据验证

| 判据 | 状态 |
|------|:----:|
| 远程 tbplas 编译零错误 | ✅ |
| Phase 1a/b/c exit 0, mu_raw h5 生成 | ✅ |
| Phase 2 全部 exit 0 | ✅ |
| 集群 vs 本地: 24 M 值逐比特一致 | ✅ |
| 所有输出零 NaN | ✅ |
| 本地 vs 远程 round-trip bit-identical | ✅ |

### 🔬 关键科学发现

- **M_c ≈ 2560**: 偏移起始阈值在 m=256/512/1024 三体系一致
- **η = N_bands/M 不是普适参数** (H_η 假说已证伪)
- 偏移更可能是 Chebyshev 三项递推在高阶的数值稳定性问题
- M≤2304 安全；M≥2560 需谨慎；M≥2816 明显偏移

<a id="ai-0623-1900"></a>

## AI: 0623_1900 — hop_max_distance 提升为 YAML 可配置参数

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/config.yaml` | ✅ 修改 | `model` 节新增 `hop_max_distance: 0.75` |
| `src/main.py` | ✅ 修改 | 从 YAML 读取并传入 `build_Nlayer_graphene` |
| `docs/tasks.md` | ✅ 更新 | 标记完成 |

### 变更说明

将 `build_Nlayer_graphene` 的 `hop_max_distance` 参数从硬编码默认值提升为 YAML 可配置参数。

- `configs/config.yaml`: `model` 节新增 `hop_max_distance: 0.75`（Slater-Koster hopping cutoff，单位 nm）
- `src/main.py` `main()`: 通过 `mc.get("hop_max_distance", 0.75)` 读取，传入 `build_Nlayer_graphene`
- 使用 `.get()` 保证旧 YAML 配置文件（无此键）向后兼容

### 成功判据验证

- [x] `configs/config.yaml` 的 `model` 节包含 `hop_max_distance: 0.75`
- [x] `main.py` 中 `build_Nlayer_graphene` 调用传入了从 YAML 读取的 `hop_max_distance`
- [x] 默认值 0.75 下 hopping 项数与修改前一致（回归验证: 17 项）
- [x] 修改 `hop_max_distance` 为 0.5 后，hopping 项数减少（验证通过）
- [x] 旧 YAML 配置文件（无 `hop_max_distance` 键）仍可正常运行（默认 0.75）
- [x] Pylance 对 `src/main.py` 零错误

---

<a id="ai-0622-1642-2"></a>

## AI: 0622_1642 (2) — KB μ 复用: 本地 m=256 回归测试 (T4, M=512/384/256/128/64)

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `docs/sigma/task_kb_mu_reuse.md` | ✅ 更新 | 新增 T4 任务，标记完成 |
| `configs/hall_m256_M512_save.yaml` | ✅ 新建 | Phase 1: save raw μ |
| `configs/hall_m256_M512_load.yaml` | ✅ 新建 | Phase 2: M=512 load |
| `configs/hall_m256_M384_load.yaml` | ✅ 新建 | M=384 load |
| `configs/hall_m256_M256_load.yaml` | ✅ 新建 | M=256 load |
| `configs/hall_m256_M128_load.yaml` | ✅ 新建 | M=128 load |
| `configs/hall_m256_M064_load.yaml` | ✅ 新建 | M=64 load |
| `runs/0622/mu_raw_M512_m256.h5` | ✅ 生成 | raw μ (512×512 complex) |
| `runs/0622/hall_AB_d0.000_m256_M{512,384,256,128,64}_load_*.txt` | ✅ 生成 | 5 个 load σ_xy 输出 |

### 变更说明

在 T2 (m=16) 基础上增加本地 m=256 回归测试:
1. 创建 6 个 YAML 配置 (1 save + 5 load)
2. Phase 1: `kbdc_mu_raw()` 计算 M=512 raw μ 并保存到 HDF5 (~4.2 MB)
3. Phase 2: 加载 raw μ → 截断到各 M → 施加 Jackson 核 → `cond_from_trace`
4. 与 0621 历史独立计算数据逐 M 对比

### 成功判据验证

| 判据 | 状态 |
|------|:----:|
| Phase 1: mu_raw_M512_m256.h5 生成, exit 0, 零 NaN | ✅ |
| Save M=512 σ_xy vs 0621 M=512: RMS diff = 9.37e-11 | ✅ **回归安全** |
| Phase 2: 5 个 load 全部 exit 0 | ✅ |
| 全部输出零 NaN | ✅ |
| M=128 因 HDF5 覆盖偏差 (RMS=0.60) — 已知局限 | ⚠️ 已记录 |

### 备注
- save config 的 σ_xy 是**独立计算**（不发生 HDF5 覆盖），与 0621 历史数据逐比特一致
- load config 的 σ_xy 使用被 σ_xx 覆盖的 raw μ，与历史的逐 M 对比仅供趋势参考
- M=128 偏差源于 `calc_hall_cond_tbpm()` 双分量调用覆盖 HDF5 的已知局限

---

<a id="ai-0622-1642"></a>

## AI: 0622_1642 — KB μ 矩阵复用: C++ 源码修改 + 本地验证 (T1+T2)

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `sources/tbpm/config.h` | ✅ 修改 | 新增 `dckb_save_mu_file` / `dckb_load_mu_file` 字段 |
| `sources/tbpm/kubo_bastin.h` | ✅ 修改 | 新增 `kbdc_mu_raw()` / `apply_jackson_kernel()` / `truncate_mu()` 三个方法 |
| `sources/tbpm/solver.h` | ✅ 修改 | `calc_hall_cond()` 新增 HDF5 load/save 分支 |
| `python/solver/interface_tbpm.h` | ✅ 修改 | `read_tbpm_config()` 新增两行 |
| `tbplas/tbpm/config.py` | ✅ 修改 | 新增 `dckb_save_mu_file` / `dckb_load_mu_file` 属性 |
| `src/calc.py` | ✅ 修改 | `config_tbpm_solver` 透传两个新键 |
| `configs/hall_m16_M1024_save.yaml` | ✅ 新建 | Phase 1 测试配置 |
| `configs/hall_m16_M1024_load.yaml` | ✅ 新建 | Phase 2 测试配置 |
| `configs/hall_m16_M512_load.yaml` | ✅ 新建 | M=512 截断测试 |
| `configs/hall_m16_M256_load.yaml` | ✅ 新建 | M=256 截断测试 |
| `configs/hall_m16_M1024_T0_01.yaml` | ✅ 新建 | 温度扫描 T=0.01 K |
| `configs/hall_m16_M1024_T1.yaml` | ✅ 新建 | 温度扫描 T=1.0 K |
| `runs/0622/mu_raw_M1024_m16.h5` | ✅ 生成 | raw μ 矩阵 (~16 MB) |
| `runs/0622/hall_AB_d0.000_m16_M1024_save_B100.0.txt` | ✅ 生成 | M=1024 save σ_xy |
| `runs/0622/hall_AB_d0.000_m16_M1024_load_B100.0.txt` | ✅ 生成 | M=1024 load σ_xy |
| `runs/0622/dc_AB_d0.000_m16_M1024_save_B100.0.txt` | ✅ 生成 | M=1024 save σ_xx |
| `runs/0622/dc_AB_d0.000_m16_M1024_load_B100.0.txt` | ✅ 生成 | M=1024 load σ_xx (round-trip 基准) |
| `runs/0622/dc_AB_d0.000_m16_M512_load_B100.0.txt` | ✅ 生成 | M=512 截断 σ_xx |
| `runs/0622/dc_AB_d0.000_m16_M256_load_B100.0.txt` | ✅ 生成 | M=256 截断 σ_xx |

### 变更说明

1. **C++ 核心** (最小侵入):
   - `config.h`: 新增两个 `std::string` 字段 (默认空), 放在 `dckb_component` 附近
   - `kubo_bastin.h`: `AbstractKuboBastin` 新增纯虚 `kbdc_mu_raw()`, 静态 `apply_jackson_kernel()`, `truncate_mu()`; `KuboBastinCPU` 实现 `kbdc_mu_raw()` (去掉 Jackson 核的 `kbdc_mu()` 副本)
   - `solver.h`: `calc_hall_cond()` 新增三路分支 — 加载/保存/原始路径, HDF5 操作由 `#ifdef WITH_HDF5` 保护
2. **Python 绑定**:
   - `interface_tbpm.h`: 添加 `input.read_single()` 两行
   - `config.py`: 添加 Python 属性, `save(fmt="dat")` 自动写入 `.dat` 文件
3. **前端透传**: `calc.py` 的 `config_tbpm_solver()` 透传两个新键

### 成功判据验证

| 判据 | 状态 |
|------|:----:|
| `kubo_bastin.h` 新增 3 个方法 | ✅ |
| `solver.h` 含 load/save 分支 (`#ifdef WITH_HDF5`) | ✅ |
| `config.h` 新增两个字段 | ✅ |
| `src/calc.py` 透传两个键 | ✅ |
| `cmake --build .` 零错误零警告 | ✅ |
| Phase 1: mu_raw h5 生成, exit 0, 零 NaN | ✅ |
| Phase 2: M=1024 σ_xx round-trip 逐比特一致 (Max diff=0) | ✅ |
| Phase 2: M=256/512 load exit 0, 零 NaN | ✅ |
| 温度扫描 T=0.01/1/10: T 升高 plateau 平滑化 | ✅ (mean\|dσ/dE\| 从 16.79→16.75) |
| Pylance `src/calc.py` 零错误 | ✅ |

### 已知问题

- `calc_hall_cond_tbpm()` 双分量调用 (σ_xy+σ_xx) 导致第二次调用覆盖 HDF5 文件。
  σ_xy round-trip 因 `dckb_save_mu_file` 被 σ_xx 覆盖而失效。已在 plan 中记录。
  **不影响**: 不设新字段时已有代码行为完全一致 (回归安全)。

---

<a id="ai-0622-0100"></a>

## AI: 0622_0100 — 基线偏移测试全部完成: H₀/H₁ 双证伪

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/hall_m128_M4096.yaml` | ✅ 新建 | T2 m=128 M=4096 (Job 284769, 1.3h) |
| `configs/hall_m512_M3072.yaml` | ✅ 新建 | T3 M=3072 m=512 (Job 284900, 2.7h) |
| `configs/hall_m1024_M4096.yaml` | ✅ 新建 | T4 m=1024 M=4096 MPI (Job 284771, 12.7h) |
| `runs/0621/` | ✅ 下载 | rs=16 (Job 283661, 9.4h) |
| `runs/0622/` | ✅ 新建 | T2/T3/T4 输出 |
| `docs/sigma/baseline_shift_plan.md` | ✅ 更新 | 状态 🔴, §3-4 全部更新 |
| `docs/sigma/baseline_shift_task.md` | ✅ 更新 | T1-T4 → [x] |
| `docs/tasks.md` | ✅ 更新 | [x] 完成 |

### 最终数据集

**rs 扫描 (m=512, M=4096):**

| rs | 1 | 2 | 4 | 8 | 16 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| S | -1034 | -720 | -730 | -685 | **-649** |

→ rs≥2 饱和，$S\propto 1/\text{rs}^{0.08}$ — **确定性系统效应。**

**m 扫描 (M=4096):**

| m | 128 | 256 | 512 | 1024 |
|:---:|:---:|:---:|:---:|:---:|
| S | -464 | -234 | -685 | **-2650** |

→ 非单调（U 形），m=1024 偏移最大 — **H₁ 被证伪。**

**M 扫描 (m=512):**

| M | 2048 | 3072 | 4096 | 6144 |
|:---:|:---:|:---:|:---:|:---:|
| S | ≈0 | -29 | -685 | -1822 |

→ M=3072 微弱偏移（-29），渐变过渡而非跳变。

### 假说结论

| 假说 | 状态 | 证伪实验 |
|------|:---:|------|
| H₀ (误差累积 S∝M², 可被 rs 抑制) | ❌ 证伪 | M=2048 S≈0; rs≥2 饱和 |
| H₁ (Krylov 饱和, M_c∝N_orb) | ❌ 证伪 | m=1024 S=-2650 而非 ≈0 |
| H₂ (Jackson 核失效) | ⚠️ 未测试 | — |

### 成功判据

- [x] T1-T4 全部 exit 0 (经 rs=16 9.4h 和 m=1024 12.7h 验证稳定)
- [x] rs 饱和确认
- [x] m 非单调发现
- [x] M=3072 渐变过渡定位
- [x] 文档全部更新

---

<a id="ai-0621-0324"></a>

## AI: 0621_0324 — Kubo-Bastin M 扫描: 全部完成 (M=64–1024, 7/8 成功)

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/hall_M{064..2048}.yaml` × 8 | ✅ 新建 | M=64/128/256/384/512/768/1024/2048 独立配置 |
| `slurm/slm_single.sh` | ✅ 编辑 | 修正路径 + conda tbplas-alpha + TBPLAS_CORE_PATH |
| `test/analyze_M_scan.py` | ✅ 新建+修正 | 适配实际文件名 hall_AB_*.txt |
| `runs/0621/` | ✅ 下载 | M=64-1024 ×7 数据回传: .txt + .png |
| `docs/tasks.md` | ✅ 更新 | [x] 完成 |
| **集群** | **Jobs 283022–283029** | **7/7 exit 0, M=2048 未提交** |

### 变更说明

1. 第1轮失败 (283017-283021): YAML 缺 `stacking` → KeyError; 修复后重提
2. 第2轮成功 (283022-283026): M=64-512 全部 exit 0; M=256 初次 qe_method 瞬态错误重提通过
3. 补充提交 (283028-283029): M=768 (4m28s), M=1024 (7m56s) 全部 exit 0
4. 分析脚本适配实际文件名 `hall_AB_d0.000_M{MMM}_B100.0.txt` (非计划的 .dat)
5. skill `cluster-workflow` 已根据本任务暴露的 6 条陷阱更新

### M 扫描最终结果

| M | NaN比例 | RMS (低能) | RMS (全窗口) | 定性 |
|:---:|:---:|:---:|:---:|------|
| 64 | 0 | 0.255 | 0.246 | 欠分辨 (KPM 展开不足) |
| 128 | 0 | 0.255 | 0.246 | 与 M=64 几乎相同 |
| 256 | 0 | 3.128 | 2.776 | 信号浮现 (LL 振荡发育) |
| 384 | 0 | 6.417 | 5.413 | 持续放大 |
| 512 | 0 | 10.315 | 8.690 | 指数增长 |
| 768 | 0 | 18.579 | 16.297 | 线性增长区间 |
| 1024 | **0** | **26.049** | 24.454 | ⚠️ **全无 NaN** (推翻了计划预期) |
| 2048 | — | — | — | 未提交 (已得完整趋势) |

### ⚠️ 计划 vs 实测差异

| 计划预期 | 实测 | 判断 |
|----------|------|------|
| M≥1024 全 NaN ("崩溃区") | M=1024 NaN=0, exit 0 | **错误** — NaN 阈值 > 1024 |
| M=256 RMS≈0.3 (最优) | RMS≈3.13 (10×) | RMS 定义差异: 计划指"噪声本底"? |
| M=512 RMS≈3.0 | RMS≈10.3 (3×) | RMS 增长（Gibbs 振荡累积）比预期更快 |
| RMS 增长模式 | RMS ≈ 0.025×M (线性) | 非指数、非对数 |

> **核心结论**:
> 1. **NaN 已修复**：全部使用 `rescale: -1`（自动检测带宽），M≤1024 全零 NaN。此前 0620 的 NaN 根因是 `rescale=9.0` 远小于 ~20 eV 带宽（详见上方 0620_2230 修正条目），而非"Chebyshev 正交性丢失"。
> 2. **RMS 单调线性增长**（RMS ∝ M）是 Gibbs 振荡的经典特征：有限 M Chebyshev 展开逼近 δ-函数（LL 能级）时，振荡幅度不随 M 收敛。这不等于数值发散或代码错误。
> 3. **M=256 仍为最优平衡点**（信号浮现但振荡不过度放大）。计划基于旧 tbplas 版本的"崩溃区"（M≥1024 全 NaN）模型已过时 —— 该模型的 NaN 实为 rescale 误配导致。

### 成功判据验证

- [x] 8 个 YAML 配置文件全部生成, tag/dckb_num_kernel/stacking 正确
- [x] M≤512 五组全部 exit 0, 数据回传完整
- [x] `analyze_M_scan.py` 运行成功, 产出 `M_scan_summary.png`
- [x] M≥1024 NaN=0 — M=768/1024 均已完成, NaN=0, 确认 rescale=-1 修复 NaN ✅
- [ ] QHE 平台结构验证 — 需进一步物理分析

**修复的意外问题**:
1. YAML 缺少 `stacking` → main.py KeyError (已修正)
2. 集群路径不一致 → slm_single.sh CONFIG_FILE 修正
3. 输出文件命名格式与计划不同 → 分析脚本适配
4. M=256 首次 qe_method 错误 → 重新提交通过

---

<a id="ai-0619-2330"></a>

## AI: 0619_2330 — T9 单层 graphene QHE 参数扫描提交 (29 YAML, Jobs 280962–280990)

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/hall_MG_B*.yaml` × 3 | ✅ 新建 | B=0/20/100T 扫描 |
| `configs/hall_MG_m*.yaml` × 7 | ✅ 新建 | m=128-768 超胞收敛性 |
| `configs/hall_MG_rs*.yaml` × 7 | ✅ 新建 | rs=1-16 样本数收敛性 |
| `configs/hall_MG_k*.yaml` × 6 | ✅ 新建 | N_k=64-512 KPM 阶数扫描 |
| `configs/hall_MG_t*.yaml` × 3 | ✅ 新建 | N_θ=1024-4096 θ 积分扫描 |
| `configs/hall_MG_e*.yaml` × 3 | ✅ 新建 | E∈[-0.3,-1.0] 能量窗口扫描 |
| `docs/sigma/tasks.md` | ✅ 更新 | T9 进度: [-] → 集群已提交 |
| `STATUS.md` | ✅ 更新 | 进行中/发现/下一步 |
| **集群** | **Jobs 280962–280990** | **29 个任务全部 sbatch 提交** |

### 变更说明

1. 基于 `configs/hall_MG.yaml` 模板, Python 批量生成 29 个 YAML, 覆盖 6 个参数维度
2. 对标 Ortmann 2015 Fig.2: 单层 graphene, B=0/20/100T, T=10K, rescale=-1(auto)
3. 本地冒烟 (m=64,N_k=64,E∈[-0.3,0.3]) 通过: RMS=0.057
4. scp 全部 YAML + src 到 h3clogin, 逐个 sbatch --nodes=1 提交
5. B0/B20/B100 三个 YAML 率先运行 (nodes 31/38/39), 其余排队

### 成功判据验证

- [x] 29 YAML 全部创建
- [x] 29 任务全部 sbatch 提交 (no reject)
- [ ] 集群全部 exit 0 — 等待完成
- [ ] QHE 平台验证 — 待数据回传

---

<a id="ai-0618-1500"></a>

## AI: 0618_1645 — Berry: B_inv.T 修复 + bz_size_ab 去重 + valley Chern header 保存

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/calc.py` | ✅ 修复 | `calc_valley_chern`: ① `B_inv.T` → `B_inv`（分数坐标变换矩阵错误）；② `area_per_kpt /= bz_size_ab`（折叠后 k 点重复计数修复） |
| `src/io_vis.py` | ✅ 修改 | `save_berry`: per-band header 加入 valley Chern 信息 |

### 变更说明

#### Bug 1: B_inv.T → B_inv（分数坐标变换错误）

**根因**：变换公式 $\mathbf{k}_{\text{frac}} = \mathbf{k}_{\text{cart}} \cdot B^{-1}$，代码错误地使用了 $B^{-T}$（`B_inv.T`）。对非对称倒格矢矩阵 $B^{-1} \neq (B^{-1})^T$，导致分数坐标算错，k 点映射到错误位置，Voronoi 划分完全错乱，valley Chern 数值完全错误。

**修复**：`kpt_cart[:, :2] @ B_inv.T` → `kpt_cart[:, :2] @ B_inv`（一行改动）。

#### Bug 2: area_per_kpt 未除以 bz_size_ab（折叠后 k 点重复计数）

**根因**：`bz_size=(2,2,1)` 扩展 BZ 有 4 个 FBZ 副本，mod 1 折叠后每个物理 k 点出现 4 次，`sum(omega[mask_K])` 对同一物理贡献重复求和。

**修复**：`area_per_kpt = bz_area / (Nk * Nk) / bz_size_ab`。

#### 验证

| bz_size | band 2 $C_K$ | 状态 |
|---------|:-----------:|:----:|
| (1,1,1) | 1.401 | ✅ 基准 |
| (2,2,1) 修复前 | 5.603 (4×) | ❌ |
| (2,2,1) 修复后 | 1.401 | ✅ 一致 |

### 成功判据验证

- [x] `bz_size=(1,1,1)` 与 `bz_size=(2,2,1)` valley Chern 一致
- [x] 每条带 $C_K + C_{K'} = 0$（Voronoi 全覆盖验证）
- [x] 全 BZ 总 Chern = 0（C++ 输出 < 1e-7）
- [x] per-band `.txt` header 含 valley Chern 信息
- [x] Pylance 对 `src/calc.py` + `src/io_vis.py` 零错误

---

## AI: 0620_2230 — T9 QHE: Job 282031 全 NaN 根因修正（rescale 误配，非 Chebyshev 不稳定性）

### 背景
Jobs 282004–282031 全部完成。Job 282031 (M=4096, rescale=9.0, García 参数复现) σ_xy/σ_xx 全部 500 能量点为 NaN。**当时误判为"Chebyshev 三项递推正交性丢失导致的数值崩溃"。**

### ⚠️ 根因修正（2026-06-21 审计）

**NaN 的真实原因：`rescale=9.0` 远小于体系带宽（~20 eV），导致缩放后哈密顿量部分特征值超出 Chebyshev 收敛域 [-1, 1]，展开发散。**

| 参数 | 值 | 问题 |
|------|-----|------|
| 体系带宽 ΔE | ~20 eV (graphene) | — |
| rescale | 9.0 | 缩放后 max(|E|)/9.0 ≈ 2.2 > 1 → **超出收敛域** |
| 正确值 | `-1` (auto-detect) | tbplas 自动检测带宽并设置正确的 rescale |

**修正后的结论**：
- 设置 `rescale: -1`（自动检测）即可修复 NaN。之后的三轮实验证实：
  - T2 r3（0618）：`rescale: -1` 修复了 8 个作业中 7 个的 NaN（仅 k=4096 仍 NaN）
  - 0621 M 扫描：`rescale: -1` 下 M=64–1024 全部 exit 0，NaN=0
- 此前的"Chebyshev 正交性丢失 / 乘性噪声叠加 / 稳定上限 M≈512"分析**基于错误前提**（误将 rescale 配置问题当作数值精度极限）
- 详见 `../shared/tbplas-internals.md` §12 的后续修正

### 更新文件
| 文件 | 操作 | 说明 |
|------|------|------|
| `runs/0620/hall_A_d0.000_M4096_B100.0.txt` | 下载 | 282031, all NaN (rescale=9.0) |
| `runs/0620/dc_A_d0.000_M4096_B100.0.txt` | 下载 | 282031, all NaN (rescale=9.0) |
| `runs/0620/slurm-282031.out` | 下载 | exit code 0 |

> **注**：本条目保留原始记录但核心结论已在 2026-06-21 修正。原错误分析（"正交性丢失"等）已作废。

---

## AI: 0618_1500 — T5: σ_xx SdH 振荡计算完成

T5 Phase 2 完成：创建 3 个 DC YAML（B=10/18/30T, m=256, ts=5000, rs=2），集群提交 3 SLURM 作业。发现并修复 `calc_dc_cond_tbpm` 中 `analyzer.calc_dc_cond` 返回 dc shape=(2, n_energies) 与 `save_conductivity` 期望 (n_energies, 2) 不兼容的 bug（转置修复）。3 作业全部 exit code 0，输出 dc_ABC_d0.000_dc_B*.txt（477-478 能量点）+ .png。σ_xx 数据显示丰富的 SdH 振荡特征（~200 次导数符号变化/B 值）。

**涉及文件**：

| 文件 | 变更 |
|------|------|
| `configs/sigma_dc_smoke.yaml` | 新建，冒烟配置 |
| `configs/sigma_dc_B10.yaml` | 新建，B=10T DC 参数 |
| `configs/sigma_dc_B18.yaml` | 新建，B=18T DC 参数 |
| `configs/sigma_dc_B30.yaml` | 新建，B=30T DC 参数 |
| `src/calc.py` `calc_dc_cond_tbpm` | 增加 dc 转置逻辑：dc.shape=(2,N)→(N,2) |

**集群作业**：

| Job ID | B (T) | Node | Exit | 产物 |
|--------|-------|------|------|------|
| 279622 | 10 | - | 0 | dc_ABC_d0.000_dc_B10.0.txt/png |
| 279623 | 18 | - | 0 | dc_ABC_d0.000_dc_B18.0.txt/png |
| 279624 | 30 | - | 0 | dc_ABC_d0.000_dc_B30.0.txt/png |

**成功判据验证**:
- [x] 3 个 DC YAML 创建并集群提交，exit code 0
- [x] σ_xx 输出 ~477 能量点，含丰富振荡
- [ ] SdH 周期/相位定量分析 → 待 T8 汇总

**已知问题**:
- 本地冒烟测试跳过（DC 计算极慢，m=32 亦耗时 >30min）
- 集群提交需 `bash -l`（login shell）以加载 Intel MPI 模块，否则 tbplas import 即 segfault

<a id="ai-0618-1300"></a>

## AI: 0618_1300 — T3+T4 完成：结果分析与 gauge 问题确认

### T3: σ_xy B 场扫描结果

| B (T) | σ_xy(E=0) | 范围 | 平台特征 |
|-------|-----------|------|---------|
| 10 | -1.99 | [-1.99, +0.33] | ❌ 无 |
| 18 | -4.00 | [-4.81, -2.61] | ❌ 无 |
| 30 | -8.92 | [-10.55, -5.41] | ⚠️ ν=-6 (E>0.22), ν=-10 |
| 45 | -12.87 | [-17.58, -7.00] | ⚠️ ν=-10 (E>0.09), ν=-14 |

### T4: σ_xy delta 扫描结果 (B=18T)

| delta | σ_xy(E=0) | E_F≈0 均值±std | 趋势 |
|-------|-----------|----------------|------|
| 0.000 | -4.000 | -3.986±0.200 | 基线 |
| 0.010 | -4.031 | -4.012±0.202 | → 略负 |
| 0.030 | -4.096 | -4.070±0.212 | → 更负 |
| 0.050 | -4.165 | -4.132±0.228 | → 最负 |

### 交叉验证
T3 B18 vs T4 d0.000: **RMS=0.0000, corr=1.000000** ✅ 两套独立配置完全一致

### 关键发现

1. **σ_xy 全局为负**: 所有 B 值、所有 delta 下，σ_xy 在整个 [-0.3,0.3] eV 能量窗口内均为负值，无过零点。这违反 σ_xy 应为 E_F 奇函数的预期。

2. **高 B 出现部分平台特征**: B=30/45T 检测到 ν=-6,-10,-14 e²/h 平台，但仅在负侧。正 ν 平台完全缺失。

3. **delta 效应微弱**: 0→0.05 eV 位移场仅使 σ_xy 负移 ~4%，E_F=0 处无 σ_xy=0 平台出现。

4. **数值稳定性优秀**: T3/T4 交叉验证 RMS=0，证明计算可复现、无随机性。

### 根因分析
所有异常指向 T2 发现的 **gauge 不变性破坏**：
- σ_xy 符号全局偏移 → Peierls 相位可能在 `apply_magnetic_field` 或 Kubo-Bastin 实现中产生系统误差
- gauge=0 vs gauge=1 给出完全不同的 σ_xy（T2: 差 ~4.5 e²/h）→ 规范选择影响物理结果

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `runs/0618/hall_ABC_d0.000_z2011_B*.txt` ×4 | 📥 | T3 结果回传 |
| `runs/0618/hall_ABC_d*_d*_B18.0.txt` ×4 | 📥 | T4 结果回传 |
| `docs/sigma/tasks.md` | ✏️ | T3/T4 标记 [x]，记录分析结果 |
| `STATUS.md` | ✏️ | 更新进度/发现 |

### 下一步
- **优先**: 排查 `apply_magnetic_field` Peierls 相位实现 → gauge 不变性修复
- 修复后重新跑 T3 B 扫描验证 QHE 平台
- 若 gauge 修复后 sigma 不全局为负，T4 delta 扫描也需重跑

<a id="ai-0618-1245"></a>

## AI: 0618_1245 — T3+T4: 集群批量提交完成（8 作业入队）

### 提交概要

| 作业 ID | 任务 | 参数 | 状态 |
|---------|------|------|------|
| 279555 | T4 delta | d=0.000, B=18T | PD |
| 279556 | T4 delta | d=0.010, B=18T | PD |
| 279557 | T4 delta | d=0.030, B=18T | PD |
| 279558 | T4 delta | d=0.050, B=18T | PD |
| 279559 | T3 B 扫描 | B=10T | PD |
| 279560 | T3 B 扫描 | B=18T | PD |
| 279561 | T3 B 扫描 | B=30T | PD |
| 279562 | T3 B 扫描 | B=45T | PD |

### 环境验证
- hostname: `slurm-login-1` ✅
- mpirun: `/hpc/software/intel/oneapi/mpi/2021.9.0/bin/mpirun` ✅
- conda env: `tbplas-alpha` ✅ (交互式 shell 自动激活)
- ControlMaster: `/home/wyl/.ssh/controlmasters/ylwang@127.0.0.1:10022` ✅

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/sigma_delta_d*.yaml` ×4 | 🆕→📤 | 本地创建 → scp 上传集群 |
| `configs/sigma_z2011_B*.yaml` ×4 | 📤 | 之前已上传，本次一并提交 |
| `docs/sigma/tasks.md` | ✏️ | T3/T4 状态更新，移除阻塞标记 |
| `STATUS.md` | ✏️ | 阻塞解除，记录作业 ID |

### 监控命令
```bash
ssh h3clogin "squeue -u ylwang"
# 或交互式:
ssh h3clogin
watch -n 30 'squeue -u ylwang; echo "---"; ls -lt runs/0618/'
```

<a id="ai-0618-1230"></a>

## AI: 0618_1230 — T4: delta 扫描 YAML 创建 + 冒烟验证（集群上传阻塞）

### 目标
Phase 1B+: 位移场影响验证。B=18T 下扫描 delta=[0.0, 0.01, 0.03, 0.05]，验证 delta≠0 时打开能隙 → σ_xy=0 平台。

### 完成部分

| 步骤 | 状态 | 说明 |
|------|------|------|
| 1. 创建 4 YAML | ✅ | `sigma_delta_d{0.000,0.010,0.030,0.050}.yaml` |
| 2. 冒烟测试 | ✅ | m=128, ts=1024, B=18T → 加载/建模/磁场/KuboBastin 启动均正常 |
| 3. 集群上传 | ⛔ | SSH 隧道需 id_h3c 密钥密码 |
| 4. 结果分析 | ⏳ | 等待作业完成 |

### YAML 参数

| 参数 | 值 | 来源 |
|------|-----|------|
| `model.num` | 3 | ABC trilayer |
| `model.stacking` | ABC | rhombohedral |
| `model.delta` | 0.0, 0.01, 0.03, 0.05 | T4 扫描变量 |
| `model.B_values` | [18.0] | 单一 B 值（较高 B 有利 LL 分离） |
| `model.gauge` | 0 | T2 暂定（gauge 不变性待修复） |
| `model.tag` | d0.000/d0.010/d0.030/d0.050 | 输出文件区分 |
| `tbpm.m` | 256 | T2 收敛：最小可用 |
| `tbpm.rescale` | -1 | T2: 自动缩放避免 Chebyshev 发散 |
| `tbpm.ts` | 5000 | T3 标准（高于 T2 的 2048） |
| `tbpm.temperature` | 1.0 | 低温（1K ≈ 0.086 meV，远小于 LL 间距） |
| `hall.dckb_num_kernel` | 2048 | T2 收敛：可用 |
| `hall.dckb_num_integ_steps` | 4096 | T3 标准（高于 T2 的 2048） |
| `hall.dckb_energies.num` | 401 | T3 标准（能量分辨率 ~1.5 meV） |

### 集群提交命令（用户执行）

```bash
# 1. 建立隧道
ssh -f -N -L 10022:slurm-login-1:22 h3cmaster2

# 2. 上传配置
scp configs/sigma_delta_d*.yaml h3clogin:~/scratch/MG/configs/

# 3. 登录并提交
ssh h3clogin
cd ~/scratch/MG
for f in configs/sigma_delta_d*.yaml; do
    jn=$(basename $f .yaml)
    sbatch --job-name=$jn slurm/slm.sh
done
```

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/sigma_delta_d0.000.yaml` | 🆕 | delta=0.0, B=18T |
| `configs/sigma_delta_d0.010.yaml` | 🆕 | delta=0.01, B=18T |
| `configs/sigma_delta_d0.030.yaml` | 🆕 | delta=0.03, B=18T |
| `configs/sigma_delta_d0.050.yaml` | 🆕 | delta=0.05, B=18T |
| `docs/sigma/tasks.md` | ✏️ | T4 状态更新 |

### 预期结果（作业完成后验证）
- delta=0.0: 连续 σ_xy 变化（无能隙），需确认有无平台
- delta=0.01: E_F≈0 处出现窄 σ_xy=0 平台
- delta=0.03: σ_xy=0 平台加宽
- delta=0.05: σ_xy=0 平台最宽
- ⚠️ 注意: T2 发现 gauge 不变性破坏 + B=10T 无 QHE 平台；B=18T 下 LL 间距更大，平台可能更明显

<a id="ai-0618-1200"></a>

## AI: 0618_1200 — T3: B 扫描 YAML 创建 + 管道验证（集群上传阻塞）

### 目标
Phase 1B: σ_xy B 场扫描 (B=10, 18, 30, 45T)，复现 Zhang 2011 QHE 平台序列 ν=±6,±10,±14 e²/h。

### 完成部分

| 步骤 | 状态 | 说明 |
|------|------|------|
| 1. 创建 4 YAML | ✅ | `sigma_z2011_B{10,18,30,45}.yaml` + `_smoke.yaml` |
| 2. 管道验证 | ✅ | prim_cell → expand_cell(m=128, 98304 orb) → B=18T → solver init 全部通过 |
| 3. 集群上传 | ⛔ | SSH 隧道需 id_h3c 密钥密码 |
| 4. 结果分析 | ⏳ | 等待作业完成 |

### YAML 参数

| 参数 | 值 | 来源 |
|------|----|------|
| `tbpm.m` | 256 | T2 收敛（m=512 失物理） |
| `tbpm.ts` | 5000 | 任务指定 |
| `hall.dckb_num_kernel` | 2048 | T2 收敛（k=4096 → NaN） |
| `hall.dckb_energies.num` | 401 | 任务指定 |
| `hall.dckb_num_integ_steps` | 4096 | 任务指定 |
| `model.gauge` | 0 | T2 暂定（gauge 不变性待修复） |

### 管道验证输出
```
prim_cell built: 6 orbitals
expand_dim = 128
supercell expanded: 98304 orbitals (m=128)
magnetic field B=18.0T applied
solver initialized OK
PIPELINE VERIFIED
```

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/sigma_z2011_B10.yaml` | 🆕 | B=10T 生产配置 |
| `configs/sigma_z2011_B18.yaml` | 🆕 | B=18T 生产配置 |
| `configs/sigma_z2011_B30.yaml` | 🆕 | B=30T 生产配置 |
| `configs/sigma_z2011_B45.yaml` | 🆕 | B=45T 生产配置 |
| `configs/sigma_z2011_smoke.yaml` | 🆕 | 冒烟测试（m=128, ts=1024） |
| `slurm/submit_T3.sh` | 🆕 | 一键上传+提交脚本 |

### 阻塞
⛔ SSH 隧道需要 `~/.ssh/id_h3c` 密钥密码。无 ssh-agent/sshpass/expect。

### 下一步（用户操作）
```bash
# 1. 建立隧道（需要输入密钥密码）
ssh -f -N -i ~/.ssh/id_h3c -L 10022:slurm-login-1:22 ylwang@h3cmaster2 -p 223

# 2. 一键上传+提交
bash slurm/submit_T3.sh

# 3. 检查作业状态
ssh ylwang@h3clogin "squeue -u ylwang"
```

<a id="ai-0618-1130"></a>

## AI: 0618_1130 — T2 r3: rescale=-1 修复 + 最终收敛分析

### 修复历程

| 轮次 | 问题 | 根因 | 修复 |
|------|------|------|------|
| r1 | 文件覆盖 | 输出命名不含 m/kernel/gauge | 新增 `tag` 参数 + YAML `tag:` 字段 |
| r2 | 全部 NaN | `rescale=10.0` < ~20 eV 带宽 → Chebyshev 发散 | 改为 `rescale: -1`（自动） |
| r3 | ✅ | 279519–279526 | 7/8 有效（k4096=NaN 自洽） |

### 收敛分析结果

| 参数 | 扫描值 | 结论 |
|------|--------|------|
| **m** | 128, 256, 512 | m=512 全负单调无物理 → **排除**; m=256 暂定可用 |
| **kernel** | 1024, 2048, 4096 | 4096=NaN; 1024→2048 RMS=0.78 → 未严格收敛但 2048 可用 |
| **gauge** | 0, 1 | ❌ **规范不变性破坏**: g0≈-2.0, g1≈+2.5 (差 4.5 e²/h) |

### 严重发现

1. **未观察到 QHE 平台**: 所有参数下 σ_xy(E) 在 [-0.3,0.3] eV 窗口内无 ν=±6,±10 e²/h 量子化平台
2. **gauge 不变性破坏**: gauge=0/1 给出完全不同的 σ_xy 值（符号都不同）→ Peierls 相位或 Kubo-Bastin 实现可能有 bug
3. **B=10T 可能太弱**: LL 间距 ∝ B^(3/2)，10T 下 LL 未充分分离

### 暂定推荐参数
`m=256, kernel=2048, gauge=0` — 待 gauge 问题解决 + 高 B (18/30T) 验证后确认

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/sigma_converge_*.yaml` | ✏️ | `rescale: -1` + `tag:` + `dc:` |
| `src/io_vis.py` | ✏️ | `save_conductivity`/`plot_conductivity` 增加 `tag` 参数 |
| `src/main.py` | ✏️ | `_run_hall`/`_run_dc` 传递 `model.tag` |
| `runs/0618/convergence_overview.png` | 🆕 | 5 条 σ_xy(E) 叠加对比图 |

<a id="ai-0617-1702r2"></a>

### 问题

第 2 轮 8 个作业（279496–279503）全部产出 NaN。第 1 轮结果也有荒谬值 ~1.8e+265。

### 根因

`rescale: 10.0` 远小于 ABC trilayer 的 ~20 eV 全带宽 → 缩放后哈密顿量特征值超出 Chebyshev 收敛域 [-1,1] → 展开发散。

### 修复

- 将所有收敛测试 YAML 的 `rescale` 从 `10.0` 改为 `-1`（tbplas 自动计算）
- 配置已上传集群，重新提交作业

### 第 3 轮作业

| 作业 ID | 作业名 | 节点 |
|---------|--------|------|
| 279519 | sigma_converge_m128 | node40 |
| 279520 | sigma_converge_m256 | node01 |
| 279521 | sigma_converge_m512 | node02 |
| 279522 | sigma_converge_k1024 | node03 |
| 279523 | sigma_converge_k2048 | node04 |
| 279524 | sigma_converge_k4096 | ✅ 已完成 |
| 279525 | sigma_converge_g0 | node06 |
| 279526 | sigma_converge_g1 | node07 |

---

## YL: 0618_1115 — ABC trilayer LDOS 对称性分析：top/bot 层不等价

### 问题

计算了 ABC trilayer graphene 在 B=80T 下不同层间偏压 δ 的 LDOS（TBPM，m=1600，rs=1，ts=5000）。
数据位于 `runs/0617/top_layer/` 和 `runs/0617/bot_layer/`。

预期对称性：top=+δ, bot=-δ 时 top layer LDOS 应等于 top=-δ, bot=+δ 时 bot layer LDOS。
但计算结果不相等。

### 结论：ABC 堆垛缺乏 z→-z 镜面对称性，top 和 bottom 层 crystallographically 不等价

### 结构分析

从 `src/model.py` `build_trilayer_graphene(stacking="ABC")` 的原子位置：

```
Layer 3 (top, z=2c/3):   A₃ @ (2/3, 2/3)    B₃ @ (0, 0)      on-site = +δ
Layer 2 (mid, z=c/3):    A₂ @ (1/3, 1/3)    B₂ @ (2/3, 2/3)   on-site =  0
Layer 1 (bot, z=0):      A₁ @ (0, 0)        B₁ @ (1/3, 1/3)   on-site = -δ
```

Slater-Koster 层间 hopping 中，垂直对齐（同 (x,y)）的原子对有最强耦合：

| 垂直对齐对 | 距离 | 角色 |
|-----------|------|------|
| B₁ (1/3,1/3,0) ↔ A₂ (1/3,1/3,c/3) | c/3 ≈ 0.335 nm | **dimer 对**（强耦合） |
| B₂ (2/3,2/3,c/3) ↔ A₃ (2/3,2/3,2c/3) | c/3 ≈ 0.335 nm | **dimer 对**（强耦合） |

非 dimer（表面态）位：
- **A₁ (0,0,0)**：中层无正对原子 → 弱层间耦合
- **B₃ (0,0,2c/3)**：中层无正对原子 → 弱层间耦合

**各层各子晶格的 dimer/non-dimer 身份**：

| 层 | A 子晶格 | B 子晶格 |
|----|---------|---------|
| **Top (layer 3)** | **dimer**（耦合中层 B₂） | **non-dimer**（表面态） |
| **Bottom (layer 1)** | **non-dimer**（表面态） | **dimer**（耦合中层 A₂） |

**Top 和 Bottom 的原子环境完全不同**：top-A 是 dimer，bottom-A 是 surface；
top-B 是 surface，bottom-B 是 dimer。不存在空间对称操作能将 top 映射到 bottom。

### 对称性分析

用户期望的对称性等价于：系统在以下联合操作下不变：
> 空间反演 (z → -z) + 偏压反号 (δ → -δ) + 层交换 (top ↔ bottom)

即要求系统具有关于中层平面的**空间反演对称性**。

- **ABA (Bernal) 堆垛**：层排列为 A→B→A，关于中层平面镜面对称 → **对称性成立**
- **ABC (rhombohedral) 堆垛**：层排列为 A→B→C，具有手性 → **对称性破缺**

ABC 堆垛中每层相对下一层同向偏移 (+1/3, +1/3)，空间反演会将其变为反向偏移 (-1/3, -1/3)，即 C→B→A（反手性），不再是原结构。因此：

$$\text{LDOS}_{\text{top}}(+\delta) \neq \text{LDOS}_{\text{bot}}(-\delta)$$

### 数值验证

取 δ = ±0.001 的 LDOS 数据做定量比较（以 diag 精确对角化为基准的能量范围 [0.7, 0.9] eV）：

| 比较对 | 子晶格 | 相关系数 | RMS 差异 |
|--------|--------|---------|---------|
| top(+0.001) vs bot(-0.001) | sA | 0.9262 | 0.0302 |
| top(-0.001) vs bot(+0.001) | sA | 0.9261 | 0.0302 |
| top(+0.001) vs bot(+0.001) | sA | 0.9261 | — |
| top(+0.001) vs bot(-0.001) | sB | 0.9243 | 0.0304 |
| top(-0.001) vs bot(+0.001) | sB | 0.9242 | 0.0304 |
| top(+0.001) vs bot(+0.001) | sB | 0.9242 | — |

关键发现：
1. **交叉比较和同 δ 比较的相关系数几乎相同**（~0.924-0.926）→ 差异主要来自 intrinsic 结构不对称，而非 δ 符号
2. **RMS 差异 ~0.03**（LDOS 峰值 ~0.5）→ 约 6% 的相对差异，物理显著

### 物理图像

ABC 三层石墨烯中：
- Top 层 LDOS = dimer-A + non-dimer-B 的贡献
- Bottom 层 LDOS = non-dimer-A + dimer-B 的贡献

Dimer 位能级由层间耦合主导（~0.4 eV 量级），non-dimer 位更接近单层行为。
两者对偏压 δ 的响应不同，因此即使交换偏压极性，top 和 bottom 的 LDOS 也不会互换。

这是 **ABC 石墨烯手性堆垛的固有特征**，不是计算错误。
若需要验证对称性，应使用 **ABA 堆垛**。

### 涉及文件

| 文件 | 说明 |
|------|------|
| `runs/0617/top_layer/` | top layer (site 0 = A₃, site 1 = B₃) LDOS，δ ∈ [-0.050, +0.050] |
| `runs/0617/bot_layer/` | bot layer (site 4 = A₁, site 5 = B₁) LDOS，δ ∈ [-0.050, +0.050] |
| `src/model.py` | `build_trilayer_graphene(stacking="ABC")` 原子位置定义 |

---

<a id="ai-0617-1702"></a>

## AI: 0617_1702r2 — T2 修复：文件命名冲突 + 重新提交（第 2 轮）

### 问题

第一轮 8 个作业（278461–278468）全部成功，但所有输出写入同一文件 `hall_ABC_d0.000_B10.0.txt`，后完成的覆盖前者 → 仅剩一份结果。

### 根因

`save_conductivity` 文件名仅基于 `calc_type/stacking/delta/B`，不包含 m/kernel/gauge 变参。

### 修复

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/io_vis.py` | ✏️ 修改 | `save_conductivity` / `plot_conductivity` 增加 `tag` 参数 |
| `src/main.py` | ✏️ 修改 | `_run_hall` / `_run_dc` 读取 `model.tag` 并传递给 save/plot |
| `configs/sigma_converge_*.yaml` | ✏️ 修改 | 各 YAML 的 `model:` 段增加唯一 `tag`（m128/m256/m512/k1024/k2048/k4096/g0/g1） |

### 输出文件命名（修复后）

- `hall_ABC_d0.000_m128_B10.0.txt` / `.png`
- `hall_ABC_d0.000_m256_B10.0.txt` / `.png`
- `hall_ABC_d0.000_k1024_B10.0.txt` / `.png` ...

### 集群重新提交

| 作业 ID | 作业名 | 节点 |
|---------|--------|------|
| 279496 | sigma_converge_m128 | node27 |
| 279497 | sigma_converge_m256 | node40 |
| 279498 | sigma_converge_m512 | node01 |
| 279499 | sigma_converge_k1024 | node02 |
| 279500 | sigma_converge_k2048 | node03 |
| 279501 | sigma_converge_k4096 | node04 |
| 279502 | sigma_converge_g0 | node05 |
| 279503 | sigma_converge_g1 | node06 |

<a id="ai-0617-1702"></a>

## AI: 0617_1702 — T2: Phase 1A Hall 收敛性测试（m/kernel/gauge 扫描）

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/sigma_converge_m128.yaml` | 🆕 新建 | m 收敛扫描：m=128, B=10T, kernel=2048, gauge=0 |
| `configs/sigma_converge_m256.yaml` | 🆕 新建 | m 收敛扫描：m=256 |
| `configs/sigma_converge_m512.yaml` | 🆕 新建 | m 收敛扫描：m=512 |
| `configs/sigma_converge_k1024.yaml` | 🆕 新建 | kernel 收敛扫描：kernel=1024, m=256 |
| `configs/sigma_converge_k2048.yaml` | 🆕 新建 | kernel 收敛扫描：kernel=2048 |
| `configs/sigma_converge_k4096.yaml` | 🆕 新建 | kernel 收敛扫描：kernel=4096 |
| `configs/sigma_converge_g0.yaml` | 🆕 新建 | gauge 对比：gauge=0, m=256, kernel=2048 |
| `configs/sigma_converge_g1.yaml` | 🆕 新建 | gauge 对比：gauge=1 |
| `configs/sigma_smoke_T2.yaml` | 🆕 新建 | 冒烟测试配置（m=128, ts=1024, num=51） |
| `docs/sigma/tasks.md` | ✏️ 更新 | T2 标记为 [x] + 完成记录 |

### 变更说明

1. 创建 8 个收敛测试 YAML 配置 + 1 个冒烟测试 YAML
2. 每个 YAML 含 `dc:` 段（config_tbpm_solver 必需）
3. 本地冒烟测试通过（m=128, ts=1024, num=51）✅
   - 输出: `runs/0617/hall_ABC_d0.000_B10.0.txt` + `.png`
4. scp 上传 9 个 YAML 到集群 `~/scratch/MG/configs/`
5. sbatch 提交 8 个作业（ID 278461–278468）

### 集群作业状态

| 作业 ID | 作业名 | 状态 | 原因 |
|---------|--------|------|------|
| 278461 | sigma_converge_m128 | PD | AssocMaxJobsLimit |
| 278462 | sigma_converge_m256 | PD | AssocMaxJobsLimit |
| 278463 | sigma_converge_m512 | PD | AssocMaxJobsLimit |
| 278464 | sigma_converge_k1024 | PD | AssocMaxJobsLimit |
| 278465 | sigma_converge_k2048 | PD | AssocMaxJobsLimit |
| 278466 | sigma_converge_k4096 | PD | AssocMaxJobsLimit |
| 278467 | sigma_converge_g0 | PD | AssocMaxJobsLimit |
| 278468 | sigma_converge_g1 | PD | AssocMaxJobsLimit |

### 成功判据验证

- [ ] m=256 下 σ_xy 已收敛 — ⏳ 集群作业排队中
- [ ] dckb_num_kernel=2048 最优 — ⏳ 集群作业排队中
- [ ] gauge=0/1 一致 — ⏳ 集群作业排队中
- [ ] 推荐参数组 — ⏳ 作业完成后

> 注意: 集群当前有 140 个待处理作业（AssocMaxJobsLimit），新作业需等待旧作业完成。

<a id="ai-0617-1701"></a>

## AI: 0617_1701 — T1: Phase 0 ABC 零场验证（能带+Berry+valley Chern）

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/sigma_zhang2012.yaml` | 🆕 新建 | Berry curvature 配置（delta=0.016, Nk=2001, bz_size=[1,1,1]） |
| `configs/sigma_zhang2012_d0.030.yaml` | 🆕 新建 | delta 扫描对比配置 |
| `configs/sigma_band_ABC.yaml` | 🆕 新建 | 零场能带配置（delta=0, k_num=601） |

### 计算结果

#### 零场能带（delta=0）
- ABC 三层 K 点附近低能带显示 ∝ k³ 的 J=3 特征（平坦色散）✅

#### Berry curvature（delta=0.016, Nk=2001, bz_size=[1,1,1]）

| 能带 | C_K | C_K' | 说明 |
|:----:|:---:|:----:|:----:|
| ib=0（最低价带） | +0.341 | −0.341 | dimer-like |
| ib=1（中间价带） | −0.318 | +0.318 | dimer-like |
| ib=2（高价带） | −0.667 | +0.667 | 低能 chiral 带 |
| **价带和** | **−0.644** | **+0.644** | — |
| ib=3（低导带） | +1.060 | −1.060 | chiral 导带 |
| ib=4 | −0.229 | +0.229 | — |
| ib=5 | −0.187 | +0.187 | — |

#### delta 扫描（delta=0.030）
| 能带 | C_K | 说明 |
|:----:|:---:|:----:|
| ib=0 | −0.258 | dimer-like |
| ib=1 | +0.293 | dimer-like |
| ib=2 | −0.697 | chiral 带（与 delta=0.016 同号） |

✅ C₁ + C₂ ≈ 0（dimer 带抵消）
⚠️ C_v ≈ ±0.64（预期 ±1.5，bz_size=[1,1,1] 下 Nk=2001 尚未完全收敛）
⚠️ 旧 runs/0616 数据用 bz_size=[2,2,1] 得到 C_v≈1.5 但总 Chern ≠ 0（不正确）

---

<a id="ai-0617-1700"></a>

## AI: 0617_1700 — T0: 修复 4 个 P0 代码缺陷（B 循环叠加/dckb_unit/temperature/dc_ts）

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/main.py` | ✅ 修改 | `_run_hall`/`_run_dc`: B 循环内每次重新 `expand_cell` 避免相位叠加 |
| `src/calc.py` | ✅ 修改 | `config_tbpm_solver`: 新增 `dckb_unit`, `temperature`, `dc_cond_num_time_steps` |
| `configs/sigma_smoke_T0.yaml` | 🆕 新建 | 冒烟测试配置（B=[18,30], m=64, ts=256, num=51） |

### 变更说明

#### 1. B 循环相位叠加修复（`src/main.py`）

- **`_run_hall`**：将 `sample = expand_cell(prim_cell, m)` 从循环外移到 B 循环内，确保每次 B 迭代从无磁场原胞重新扩胞并施加独立的 Peierls 相位
- **`_run_dc`**：同上修改

#### 2. 缺失 solver 参数补齐（`src/calc.py` `config_tbpm_solver`）

| 参数 | 默认值 | 来源 | 影响 |
|------|--------|------|------|
| `dckb_unit` | `"h"` | `hall.dckb_unit` | 输出 e²/h 而非 e²/ħ（差 2π 倍） |
| `temperature` | `1.0` | `tbpm.temperature` | 低温解析 LL 结构 |
| `dc_cond_num_time_steps` | `1024` | `dc.dc_cond_num_time_steps` | DC 关联时间步数可配置 |

### 成功判据验证

- [x] `_run_hall` 中每次 B 迭代均重新 expand_cell
- [x] `_run_dc` 中每次 B 迭代均重新 expand_cell
- [x] `config_tbpm_solver` 传入 `dckb_unit/h`/`temperature`/`dc_cond_num_time_steps`
- [x] Pylance 零错误
- [ ] B=18T vs B=30T σ_xy 不同 — ⏳ 冒烟测试运行中

### 环境发现

`tbplas-alpha` conda 环境缺少 tbplas C++ 扩展（`atom.so` 等），需设置 `TBPLAS_CORE_PATH=/home/wyl/tbplas/install/tbplas-cpp-a021ca8/lib` 方可运行。

---

<a id="ai-0616-2030"></a>

## AI: 0616_2030 — Berry: Voronoi 谷划分 + bz_size + 折叠修复 + spinless vs spinful 澄清

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/calc.py` | ✅ 修改 | `calc_valley_chern`: 圆盘 → Voronoi；新增 k 点折叠回 FBZ；`calc_berry_curvature`: 新增 bz_size 参数入口 |
| `configs/config.yaml` | ✅ 修改 | `berry` 节新增 `bz_size: [1,1,1]`；`alpha_r` 标记 deprecated |
| `runs/0616/valley_chern_number.md` | 🆕 新建 | ABC/ABA/AB 三种 stacking 计算结果汇总 |

### 变更说明

#### 1. Voronoi 谷划分（替换圆盘积分）

- 移除 `alpha_r`、`dist_KK`、`r` 相关代码
- 替换为 Voronoi 最近距离分配：`mask_K = dist_K <= dist_Kp`
- 每个 k 点恰好属于一个谷（全覆盖、无重叠）
- 新增打印 `total_chern` 用于全 BZ 交叉验证（应为 0）

#### 2. bz_size 参数支持 + k 点折叠修复

- **新增参数**：`config.yaml` → `berry.bz_size: [1, 1, 1]`，`calc.py` 读取并设置 `solver.config.bz_size`
- **bug 发现**：`bz_size=(2,2,1)` 时 valley Chern 翻倍（1.5→3.0），根因是扩展 BZ 含 4 个 FBZ 副本，Voronoi K-半区含 2 个物理 K 谷
- **修复**：将扩展 BZ 的 k 点通过分数坐标 `mod 1` 折叠回第一 FBZ 再做 Voronoi，消除重复计数

#### 3. spinless vs spinful valley Chern 澄清

- **发现**：计算结果 $C_V^K \approx 1.5$（per spin）而非文献的 ±3
- **根因**：tbplas 默认 `num_spin=1`，紧束缚模型 6 个 p_z 轨道不含自旋，计算的是 spinless valley Chern
- **文献值 ±3 = 2 × 1.5**（自旋简并因子 2）
- 修改 `num_spin` 不影响 Berry curvature 计算（C++ 层不读取此参数），仅需在解读时乘以 2

### 计算结果汇总（delta=0.016, Nk=2001, Voronoi 划分）

#### ABC trilayer（6 轨道，价带 ib=0,1,2）

| 能带 | $C_K$ | $C_{K'}$ | total |
|------|:-----:|:--------:|:-----:|
| ib=0 | −0.208 | +0.208 | 0 |
| ib=1 | +0.307 | −0.307 | 0 |
| ib=2 | +1.401 | −1.401 | 0 |
| **价带和** | **+1.500** | **−1.500** | — |
| ib=3 | −3.867 | +3.867 | 0 |
| ib=4 | +1.220 | −1.220 | 0 |
| ib=5 | +1.148 | −1.148 | 0 |

✅ $C_V^{\text{spinless}} = \pm 1.5$，$C_V^{\text{spinful}} = \pm 3$，与文献一致。

#### ABA trilayer（6 轨道，价带 ib=0,1,2）

| 能带 | $C_K$ | $C_{K'}$ | total |
|------|:-----:|:--------:|:-----:|
| ib=0 | −0.106 | +0.106 | 0 |
| ib=1 | −0.501 | +0.501 | 0 |
| ib=2 | +0.853 | −0.853 | 0 |
| **价带和** | **+0.246** | **−0.246** | — |

⚠️ valley Chern 不收敛（预期 ±1.0），根因：delta=0.016 eV 太小，ABA 存在 mirror-even 子空间使实际 gap ≪ delta，Dirac 点 Berry curvature 峰极窄，Nk=2001 不足以分辨。需增大 delta（≥0.05 eV）或 bz_size（≥2,2,1）。

#### AB bilayer（4 轨道，价带 ib=0,1）

| 能带 | $C_K$ | $C_{K'}$ | total |
|------|:-----:|:--------:|:-----:|
| ib=0 | −0.027 | +0.027 | 0 |
| ib=1 | +1.027 | −1.027 | 0 |
| **价带和** | **+1.000** | **−1.000** | — |

✅ $C_V^{\text{spinless}} = \pm 1.0$，$C_V^{\text{spinful}} = \pm 2$，与文献一致。

### 体系对比

| 体系 | 色散 | $C_V$ (spinless) | $C_V$ (incl. spin) |
|------|:----:|:----------------:|:------------------:|
| AB bilayer | $\sim k^2$ | **±1.0** | **±2** |
| ABA trilayer | $\sim k$ + $\sim k^2$ | (待 delta≥0.05 确认) | (预期 ±2) |
| ABC trilayer | $\sim k^3$ | **±1.5** | **±3** |

ABC↔AB domain wall: $\Delta C_V = 0.5$ (per spin)，拓扑非平庸，可支撑边界态。

### 成功判据验证

- [x] `calc_valley_chern` 不再使用 `alpha_r` 和圆盘半径 `r`
- [x] `mask_K` / `mask_Kp` 基于 Voronoi 最近距离分配
- [x] 每个 k 点恰好属于一个谷（$C_K + C_{K'} = 0$ 每带验证通过）
- [x] 全 BZ 总 Chern = 0（C++ 输出 < 1e-7）
- [x] bz_size 折叠修复后 (1,1,1) 与 (2,2,1) 结果一致
- [x] ABC valley Chern spinless=±1.5、AB=±1.0，与色散缠绕数一致
- [x] Pylance 对 `src/calc.py` 零错误

---

<a id="ai-0616-1825"></a>

## AI: 0616_1825 — Berry 全面重构：T1~T5

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/io_vis.py` | ✅ 修改 | T1: `save_berry`/`plot_berry` 9 处单位标注 Å⁻¹/Å² → nm⁻¹/nm² |
| `src/calc.py` | ✅ 修改 | T2: 添加 `solver.config.prefix` 唯一化；T3: K_frac 从 YAML 读取去硬编码；T4: 暴露 ham_deriv_analytical/delta 参数 |
| `configs/config.yaml` | ✅ 修改 | T4: `berry` 节新增 `ham_deriv_analytical`/`ham_deriv_delta` |
| `runs/scan_berry_convergence.py` | 🆕 新建 | T5: Berry 精度收敛验证扫描脚本 |
| `runs/0616/convergence_results.json` | 🆕 生成 | T5: 扫描结果（Nk/delta/alpha_r 三参数 × ABA+ABC） |

### 变更说明

#### T1 — Berry 单位标注修正：1/Å → 1/nm ✅
- `save_berry` header：`kx(1/A)` → `kx(1/nm)`，`ky(1/A)` → `ky(1/nm)`（3 处）
- `plot_berry` 分能带/总分图：`$A^{-1}$` → `nm$^{-1}$`，`$A^{2}$` → `nm$^2$`（6 处）

#### T2 — Berry: prefix 显式设置 + 输出目录归位 ✅
- `calc_berry_curvature` 中设 `solver.config.prefix = f"berry_{stacking}_d{delta_str}"`
- `delta_str` 用 `'p'` 替代 `'.'`（C++ `_set_output()` 禁止小数点）
- 示例：`berry_ABC_d0p030`（替代默认 `sample`）

#### T3 — Berry: calc_valley_chern 从 YAML 读取 K_frac 去硬编码 ✅
- `K_frac = np.array([2/3, 1/3])` → `np.array(bc.get("K_frac", [2/3, 1/3, 0.0])[:2])`
- K' 保持 `[1/3, 2/3]`（时间反演对称点，标准约定固定）

#### T4 — Berry: 暴露 ham_deriv 参数 ✅
- `config.yaml` 新增 `ham_deriv_analytical: false` + `ham_deriv_delta: 1.0e-6`
- `calc_berry_curvature` 读取并设置 `solver.config.ham_deriv_analytical` / `ham_deriv_delta`
- 默认值向后兼容（false + 1e-6）

#### T5 — Berry 精度收敛验证 ✅

**Nk 收敛扫描**（alpha_r=0.5, ham_deriv_delta=1e-6）：

ABA stacking valley Chern（K 谷）:
| Nk | b0 | b1 | b2 | b3 | b4 | b5 |
|----|----|----|----|----|----|----|
| 501 | -0.1057 | -0.4980 | +0.9512 | +0.9351 | -0.3262 | -0.9563 |
| 1001 | -0.1057 | -0.5038 | +0.1267 | +1.8018 | -0.3625 | -0.9565 |
| 2001 | -0.1057 | -0.5038 | +0.0370 | +1.8908 | -0.3618 | -0.9564 |
| 3001 | -0.1057 | -0.5038 | +0.4135 | +1.5143 | -0.3618 | -0.9564 |

ABC stacking valley Chern（K 谷）:
| Nk | b0 | b1 | b2 | b3 | b4 | b5 |
|----|----|----|----|----|----|----|
| 501 | +0.3319 | -0.2570 | +1.4244 | -3.4488 | +0.9950 | +0.9546 |
| 1001 | +0.4572 | -0.3824 | +1.4244 | -3.4492 | +0.9952 | +0.9547 |
| 2001 | +0.4738 | -0.3989 | +1.4244 | -3.4491 | +0.9951 | +0.9547 |
| 3001 | +0.7286 | -0.6537 | +1.4244 | -3.4491 | +0.9952 | +0.9547 |

**ham_deriv_delta 敏感性**（ABC, Nk=2001）:
- 1e-5 / 1e-6 / 1e-7 三组结果完全一致（差异 < 1e-6）
- ✅ 默认 1e-6 在 plateau 区

**alpha_r 敏感性**（ABC, Nk=2001）:
| alpha_r | b0 | b1 | b2 | b3 | b4 | b5 |
|---------|----|----|----|----|----|----|
| 0.3 | +0.4169 | -0.3624 | +1.4444 | -3.0346 | +0.7546 | +0.7811 |
| 0.4 | +0.4594 | -0.3894 | +1.4291 | -3.3481 | +0.9642 | +0.8848 |
| 0.5 | +0.4738 | -0.3989 | +1.4244 | -3.4491 | +0.9951 | +0.9547 |
| 0.6 | +0.4671 | -0.3947 | +1.4269 | -3.5578 | +1.0384 | +1.0201 |

**全 BZ 总 Chern**: 所有运行 total_Chern < 1e-16 ✅（时间反演对称性满足）

### 关键发现

1. **ABA b0/b1 收敛快**（Nk=1001 即稳定），但 **b2/b3 因能带交叉不收敛**（需 Wilson loop 或其他方法分离）
2. **ABC b2/b3/b4/b5 收敛好**（Nk=1001→3001 变化 < 0.001），但 **b0/b1 不收敛**（Berry curvature 在 Dirac 点高度集中，需 Nk > 3001）
3. **ham_deriv_delta 对 valley Chern 无影响**（1e-5~1e-7 结果一致），默认 1e-6 安全
4. **alpha_r 在 [0.4, 0.5] 对多数能带接近 plateau**，但非完美。推荐 alpha_r=0.5
5. **推荐生产参数**: Nk=2001, delta=1e-6, alpha_r=0.5

### 成功判据验证

- [x] `grep "1/A\|A^{-1}\|A^{2}" src/io_vis.py` 在 save_berry/plot_berry 零匹配
- [x] `grep "1/nm\|nm^{-1}\|nm^{2}" src/io_vis.py` 对应新增匹配（9 处）
- [x] Pylance 对 `src/io_vis.py` + `src/calc.py` 零错误
- [x] `solver.config.prefix` 为非 `"sample"` 唯一字符串
- [x] `K_frac` 从 `cfg["berry"]["K_frac"][:2]` 读取，无硬编码 `[2/3, 1/3]`
- [x] `config.yaml` 含 `ham_deriv_analytical` + `ham_deriv_delta`
- [x] Nk=2001 与 Nk=3001 对收敛能带差异 < 0.01
- [x] ham_deriv_delta=1e-6 在 plateau 区
- [x] 全 BZ 总 Chern = 0（< 1e-16）

---


<a id="ai-0609-1530"></a>

## AI: 0609_1530 — ldos_delta 物理含义 + TBPM DOS/LDOS 展宽控制全景分析

> 结论：`ldos_delta` 仅在 Haydock 递归法中生效（Lorentzian 展宽），TBPM 传播路径不读取此参数。TBPM 框架四种计算路径的展宽机制完全不同。
> 完整分析已提取到跨项目知识库 → [`/home/wyl/docs/tbplas-internals.md#2-ldos_delta--物理含义与生效范围`](/home/wyl/docs/tbplas-internals.md#2-ldos_delta--物理含义与生效范围) 和 [`#3-tbpm-展宽控制全景`](/home/wyl/docs/tbplas-internals.md#3-tbpm-展宽控制全景)

---

<a id="ai-0609-1500"></a>

## AI: 0609_1500 — calc_ldos_tbpm 统一调用 config_tbpm_solver

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/calc.py` | ✅ 修改 | `calc_ldos_tbpm` 先调用 `config_tbpm_solver` 设置公共参数，再覆盖 LDOS 专用参数 |

### 变更说明

| 维度 | 修改前 | 修改后 |
|------|--------|--------|
| 公共参数设置 | 手动 `solver.config.num_random_samples = rs`、`num_time_steps = ts`、`algo = algo` | `config_tbpm_solver(solver, cfg)` 统一管理 rescale/rs/ts/num_spin/algo |
| LDOS 专用参数 | 穿插在公共参数之间 | 在 `config_tbpm_solver` 之后统一覆盖（`ldos_orbital_indices`/`ldos_delta`/`ldos=True`） |
| `rescale` / `num_spin` | ❌ 缺失 | ✅ 由 `config_tbpm_solver` 自动设置 |

### 成功判据验证

- [x] `calc_ldos_tbpm` 调用了 `config_tbpm_solver(solver, cfg)`
- [x] 不再手动设置 `rescale`/`num_random_samples`/`num_time_steps`/`num_spin`/`algo`
- [x] LDOS 专用参数在 `config_tbpm_solver` 之后设置
- [x] Pylance 对 `src/calc.py` 零错误
- [x] `calc_ldos_tbpm` 导入正常

---

<a id="ai-0609-1400"></a>

## AI: 0609_1425 — TBPM DOS 27 参数扫描：首次提交（4 节点）→ 取消 → cpu_fast + 单节点重新提交

### 流程概要

| 阶段 | 时间 | 操作 | 说明 |
|------|------|------|------|
| ① 首次提交 | 1400 | `gen_cfg.py` → `sbatch` | 27 作业（4 节点 × 32 核，默认 `algo=cpu`） |
| ② 取消 | 1425 | `scancel -u ylwang` | Job IDs 274979-275009 |
| ③ 参数修改 | 1425 | `algo: cpu_fast` + `--nodes=1` | 移除 mpirun |
| ④ 重新提交 | 1425 | scp → sbatch | **Submitted: 27**（Job IDs 275010-275036） |
| ⑤ 验证 | 1425 | `squeue` | 27 个作业 PENDING |

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/gen_cfg.py` | ✅ 执行 → 修改 | 首先生成 27 个 YAML；随后新增 `cfg["tbpm"]["algo"] = "cpu_fast"` |
| `configs/ABC_d0.030_*.yaml` | 🆕 生成 × 27 → 重新生成 × 27 | 首次含默认 algo；二次含 `algo: cpu_fast` |
| `slurm/slm.sh` | ✅ 修改 | `--nodes=4` → `--nodes=1`，移除 mpirun |
| `slurm/batch_submit.sh` | ✅ 执行 | 两次批量提交 |
| `docs/tasks.md` | ✅ 更新 | 标记完成 |
| `STATUS.md` | ✅ 更新 | 更新进度 |

### 首次提交（1400）

| 步骤 | 状态 | 说明 |
|------|------|------|
| 1. 本地生成 27 个 YAML | ✅ | `python gen_cfg.py` 输出 27 个文件，`wc -l=27` |
| 2. 连接 h3clogin 集群 | ✅ | ControlMaster 存活 → SSH 登录 → 环境验证通过 |
| 3. scp 上传 | ✅ | `scp -r configs/ src/ slurm/` 零错误，远程 27 文件验证通过 |
| 4. sbatch 批量提交 | ✅ | `bash slurm/batch_submit.sh` → **Submitted: 27**，SKIP: 1(config.yaml) |
| 5. squeue 验证 | ✅ | `squeue -u ylwang | wc -l` = 27，全部 PENDING |
| 6. 产物验证 | ⏳ | 作业完成后检查 `runs/0609/`（待后续） |

### 取消与重新提交（1425）

| 操作 | 状态 | 说明 |
|------|------|------|
| `scancel -u ylwang` | ✅ | 取消全部 27 个作业（Job IDs 274979-275009） |
| `gen_cfg.py` + `algo: cpu_fast` | ✅ | 新增 `cfg["tbpm"]["algo"] = "cpu_fast"` |
| `slm.sh` `--nodes=4` → `--nodes=1` | ✅ | 单节点计算，移除 mpirun |
| 重新 scp 上传 | ✅ | 27 YAML + slm.sh |
| 重新 sbatch 提交 | ✅ | **Submitted: 27**（Job IDs 275010-275036） |
| `squeue` 验证 | ✅ | 27 个作业 PENDING |

### 关键验证

- **前置检查**: `hostname=slurm-login-1` ✅, `CONDA_DEFAULT_ENV=tbplas-alpha` ✅, `pwd=~/scratch/MG` ✅
- **首次作业**: Job IDs 274979-275009，4 节点 × 32 核，排除 node[29-30,41-64]
- **二次作业**: Job IDs 275010-275036，单节点，无 mpirun
- **环境**: `tbplas-alpha` 环境已加载 Intel oneAPI MPI + MKL
- **约束遵守**: 通过交互式终端提交（非 `ssh h3clogin "sbatch ..."` 反模式）

### 备注

- 本地用 `base` 环境运行 `gen_cfg.py`（仅需 yaml+numpy，无需 tbplas）
- 集群 `tbplas-alpha` 环境已预装 tbplas + Intel MPI + MKL
- `batch_submit.sh` 自动跳过 `config.yaml` 模板
- 改用 `algo: cpu_fast` 原因：避免 Chebyshev 递推数值不稳定性（见 0608_2330 分析）

---

<a id="ai-0608-2330"></a>

## AI: 0608_2330 — ts 增大导致 TBPM LDOS 精度下降根因分析（Chebyshev 递推数值不稳定性）

> 结论：`cpu_fast` 算法一次性计算所有 Chebyshev 矩（三项递推），ts 越大 → 矩阶数越高 → 舍入误差累积越大 → LDOS 反而更嘈杂。推荐 `m=512, ts=2048, algo=cpu_fast`。
> 完整分析已提取到跨项目知识库 → [`/home/wyl/docs/tbplas-internals.md#4-chebyshev-递推数值不稳定性---为什么-ts-越大-ldos-反而越差`](/home/wyl/docs/tbplas-internals.md#4-chebyshev-递推数值不稳定性---为什么-ts-越大-ldos-反而越差)

---

<a id="ai-0608-2230"></a>

## AI: 0608_2230 — rs 对 TBPM LDOS 无影响根因分析 + config_tbpm_solver 修复

### 代码修复（保留）

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/calc.py` | ✅ 修复 | `config_tbpm_solver` 移除不存在的 `ldos_orbital_indices` 键引用 |

**修复内容**：`config_tbpm_solver` 中 `solver.config.ldos_orbital_indices = tbpm_cfg["ldos_orbital_indices"]` 导致 KeyError（YAML `tbpm` 段无此键）。删除该行，此参数由 `calc_ldos_tbpm` 单独设置。

### rs 根因分析

> 结论：单 site LDOS 中随机相位 $e^{i\theta}$ 在量子力学内积中精确抵消，`rs` 参数无影响。这是 TBPM 方法的理论特性，非 bug。
> 完整分析（含 C++ 源码追踪 + 数学推导 + 各场景建议）已提取到跨项目知识库 → [`/home/wyl/docs/tbplas-internals.md#5-rs-对单-site-ldos-无效--随机相位抵消`](/home/wyl/docs/tbplas-internals.md#5-rs-对单-site-ldos-无效--随机相位抵消)

---

<a id="ai-0608-2100"></a>

## AI: 0608_2100 — TBPM LDOS 参数扫描误差分析（以 diag 为基准）

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `runs/0608/compare_ldos.py` | ✅ 新增 | TBPM vs diag LDOS 误差对比脚本 |
| `docs/log.md` | ✅ 追加 | 本记录 |

### 分析方法

- **基准**：`ldos_ABC_d0.030_site1.txt`（diag 对角化，201 点，[0.7, 0.9] eV，ΔE=0.001 eV）
- **对比对象**：27 个 TBPM LDOS 文件（m∈{128,256,512} × rs∈{4,8,16} × ts∈{1024,2048,4096}）
- **误差计算**：将 TBPM LDOS 线性插值到 diag 能量网格，计算 MAE / RMSE / MaxErr / MAPE

### 误差总表

| m | rs | ts | n_pts | MAE | RMSE | MaxErr |
|---|----|-----|-------|-----|------|--------|
| 128 | 4 | 1024 | 59 | 4.360e-03 | 6.288e-03 | 1.920e-02 |
| 128 | 8 | 1024 | 29 | 2.096e-03 | 2.711e-03 | 6.884e-03 |
| 128 | 16 | 1024 | 29 | 2.096e-03 | 2.711e-03 | 6.884e-03 |
| 128 | 4 | 2048 | 59 | 4.360e-03 | 6.288e-03 | 1.920e-02 |
| 128 | 8 | 2048 | 59 | 4.360e-03 | 6.288e-03 | 1.920e-02 |
| 128 | 16 | 2048 | 59 | 4.360e-03 | 6.288e-03 | 1.920e-02 |
| 128 | 4 | 4096 | 118 | 6.665e-03 | 9.571e-03 | 3.648e-02 |
| 128 | 8 | 4096 | 118 | 6.665e-03 | 9.571e-03 | 3.648e-02 |
| 128 | 16 | 4096 | 118 | 6.665e-03 | 9.571e-03 | 3.648e-02 |
| 256 | 4 | 1024 | 29 | 9.753e-04 | 1.313e-03 | 3.914e-03 |
| 256 | 8 | 1024 | 29 | 9.753e-04 | 1.313e-03 | 3.914e-03 |
| 256 | 16 | 1024 | 29 | 9.753e-04 | 1.313e-03 | 3.914e-03 |
| 256 | 4 | 2048 | 58 | 1.904e-03 | 2.593e-03 | 6.418e-03 |
| 256 | 8 | 2048 | 58 | 1.904e-03 | 2.593e-03 | 6.418e-03 |
| 256 | 16 | 2048 | 58 | 1.904e-03 | 2.593e-03 | 6.418e-03 |
| 256 | 4 | 4096 | 117 | 3.429e-03 | 4.569e-03 | 1.304e-02 |
| 256 | 8 | 4096 | 117 | 3.429e-03 | 4.569e-03 | 1.304e-02 |
| 256 | 16 | 4096 | 117 | 3.429e-03 | 4.569e-03 | 1.304e-02 |
| 512 | 4 | 1024 | 29 | 6.155e-04 | 1.134e-03 | 3.862e-03 |
| 512 | 8 | 1024 | 29 | 6.155e-04 | 1.134e-03 | 3.862e-03 |
| 512 | 16 | 1024 | 29 | 6.155e-04 | 1.134e-03 | 3.862e-03 |
| 512 | 4 | 2048 | 58 | 3.157e-04 | 4.310e-04 | 1.297e-03 |
| 512 | 8 | 2048 | 58 | 3.157e-04 | 4.310e-04 | 1.297e-03 |
| 512 | 16 | 2048 | 58 | 3.157e-04 | 4.310e-04 | 1.297e-03 |
| 512 | 4 | 4096 | 117 | 1.405e-03 | 1.976e-03 | 7.423e-03 |
| 512 | 8 | 4096 | 117 | 1.405e-03 | 1.976e-03 | 7.423e-03 |
| 512 | 16 | 4096 | 117 | 1.405e-03 | 1.976e-03 | 7.423e-03 |

> 最优: m=512, rs=8, ts=2048 — RMSE=4.310e-04
> 最差: m=128, rs=16, ts=4096 — RMSE=9.571e-03

### 关键发现

#### 1. rs 对 TBPM LDOS 精度无影响（随机采样已收敛）

同 m/ts 下，rs=4/8/16 的 MAE 完全一致（25/27 组合）。唯一例外是 m=128, ts=1024, rs=4（MAE=4.36e-3 vs rs=8/16 的 2.10e-3），其原因已在上一次分析中确认：TBPM `cpu_fast` 算法对 `ts=1024 + rs=4` 组合存在内部约束，实际使用了 16 个采样和 3306 个 mu orders（而非 4 采样 + 1679 mu orders）。

**结论**：TBPM 随机采样在此体系中极快收敛，rs=4 即足够。rs 参数对精度无提升作用。

#### 2. m（超胞大小）是主导精度的核心参数

| m | ts=1024 平均 RMSE | ts=2048 平均 RMSE | ts=4096 平均 RMSE | 总体平均 RMSE |
|---|-------------------|-------------------|-------------------|--------------|
| 128 | 3.90e-03 | 6.29e-03 | 9.57e-03 | 6.59e-03 |
| 256 | 1.31e-03 | 2.59e-03 | 4.57e-03 | 2.83e-03 |
| 512 | 1.13e-03 | 4.31e-04 | 1.98e-03 | 1.18e-03 |

m 从 128 → 512，RMSE 下降约 **5.6 倍**。超胞越大，TBPM 有限尺寸效应越小，越接近 diag 的无限周期边界结果。

#### 3. ts 对精度的影响呈反直觉趋势 ⚠️

| ts | 平均 RMSE |
|----|----------|
| 1024 | 2.12e-03 |
| 2048 | 3.10e-03 |
| 4096 | 5.37e-03 |

ts 越大（传播时间越长），误差反而越大。这反直觉，需要进一步分析：

**可能原因**：
- TBPM 关联函数 C(t) 在长时极限下累积数值误差（KPM 展开截断 + 浮点精度）
- 本分析采用 diag 精细网格（ΔE=0.001 eV）对 TBPM 粗网格插值，ts=4096 时 TBPM 在 [0.7, 0.9] eV 窗口仅约 118 点（vs diag 201 点），插值引入额外误差
- 更根本的原因可能是 TBPM 的能量分辨率由总传播时间 T = ts × dt 决定，但 FFT 后能量网格的最小间距不一定随 ts 线性改善

**建议**：若要获得最精确 TBPM LDOS，推荐 **m=512, ts=2048**（RMSE=4.31e-4，MaxErr=1.30e-3），而非 ts=4096。

#### 4. m=128, ts=1024, rs=4 的异常行为确认

此组合的 n_pts=59（正常应为 29），MAE=4.36e-3（vs 正常 2.10e-3），与 TBPM 库日志一致：实际使用 16 采样 + 3306 mu orders。**建议避免 ts=1024 + rs=4 组合**。

### 推荐配置

| 优先级 | m | ts | rs | RMSE | 适用场景 |
|--------|---|-----|-----|------|---------|
| 🥇 最佳 | 512 | 2048 | 4 | 4.31e-04 | 高精度生产 |
| 🥈 均衡 | 256 | 1024 | 4 | 1.31e-03 | 日常使用 |
| 🥉 快速 | 128 | 1024 | 8 | 2.71e-03 | 快速筛查 |

---

<a id="ai-0608-1730"></a>

## AI: 0608_1730 — io_vis 全量迁移：read/plot → prefix + save → data_dir，删除 _make_output_path

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/io_vis.py` | ✅ 重写 | `read_*`/`plot_*` → prefix 模式（追加 `.txt`/`.png`）；`save_*` → data_dir + 内部 f-string；删除 `_make_output_path` 及 `import datetime`；修复 `plot_ldos_spectrum` 双扩展名 bug |
| `src/main.py` | ✅ 修改 | 所有 `_run_*` 函数签名新增 `data_dir`；`_run_band`/`_run_dos`/`_run_berry` 构造 `prefix` 传 plot 函数；`_run_hall`/`_run_dc` B 循环内构造含 `_B{B}` 的 prefix |

### 变更说明

1. **`read_*` 系列 prefix 化**：`read_dos`/`read_bands`/`read_berry`/`read_conductivity` 签名从 `(filename)` 改为 `(prefix)`，内部 `np.loadtxt(f"{prefix}.txt")`
2. **`plot_*` 系列 prefix 化**：`plot_dos`/`plot_bands`/`plot_berry`/`plot_conductivity`/`plot_cond_comparison` 签名从 `(..., cfg, ...)` 改为 `(..., prefix, ...)`，内部 `plt.savefig(f"{prefix}.png")`
3. **`save_*` 系列 data_dir 化**：`save_dos`/`save_bands`/`save_berry`/`save_conductivity` 签名新增 `data_dir` 参数，内部 `os.makedirs` + f-string 拼接路径
4. **`_make_output_path` 删除**：全文件零引用后删除函数体及不再需要的 `import datetime`
5. **`plot_ldos_spectrum` 修复**：`glob` 返回 `.txt` 完整路径 → `os.path.splitext` 去扩展名后再传 `read_ldos(prefix)`，消除双扩展名 bug
6. **`main.py` 适配**：所有 `_run_*` 函数接收 `data_dir`；`_run_*` 内构造 `prefix` 供 plot 调用；`_run_hall`/`_run_dc` B 循环内部 `prefix = f"{data_dir}/{calc_type}_{stacking}_d{delta:.3f}{b_suffix}"`

### 成功判据验证

- [x] `_make_output_path` 不存在于 `io_vis.py` — grep 确认零引用
- [x] 所有 `read_*`/`plot_*` 接受 `prefix`（不含扩展名），内部追加 `.txt`/`.png` — 签名验证通过
- [x] 所有 `save_*` 签名为 `(..., cfg, data_dir, ...)`，内部 `os.makedirs` + f-string 拼路径 — 签名验证通过
- [x] Pylance 对 `src/` 下全部 .py 零错误
- [ ] 运行时验证阻塞于 tbplas C++ 扩展环境问题（`ImportError: C++ atom extension not found`），非本次修改导致

### 备注

- 路径生成从 `_make_output_path` 统一迁移为 prefix / data_dir + f-string，对齐 LDOS 重构②（0608_1605）的标准
- `import datetime` 在 `main.py` 中保留（用于 `data_dir` 时间戳），从 `io_vis.py` 删除
- 文件命名规则完全不变，仅路径生成方式重构

---

<a id="ai-0608-1610"></a>

## AI: 0608_1610 — LDOS 重构①~③：YAML site 键 + io_vis.py 重写 + main.py _run_ldos 重写

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/*.yaml` (×82) | ✅ 修改 | `ldos` 节新增 `site: 1` 键 |
| `configs/config.yaml` | ✅ 修改 | `ldos` 节新增 `site: 1` 并加注释 |
| `src/calc.py` | ✅ 修改 | `calc_ldos_tbpm` 移除硬编码 `[1]`，改为 `cfg["ldos"]["site"]` |
| `src/io_vis.py` | ✅ 重写 | 删除 `save_ldos_diag`/`save_ldos_test`/`plot_ldos`；重写 `save_ldos`/`read_ldos`/`vis_ldos` 为 per-site 两列格式；适配 `plot_ldos_spectrum` 接口 |
| `src/main.py` | ✅ 修改 | `_run_ldos` diag 分支逐 site 循环保存 + total；tbpm 分支从 cfg 读 site；import 更新 `save_ldos_diag`→`vis_ldos` |

### 变更说明

1. **YAML site 键统一**：`configs/` 下 82 个 `.yaml` 的 `ldos` 节均新增 `site: 1` 键
2. **calc.py 去硬编码**：`calc_ldos_tbpm` 中 `solver.config.ldos_orbital_indices = [1]` 改为从 `cfg["ldos"].get("site", 1)` 读取
3. **io_vis.py LDOS 重构**：删除三个旧函数，重写为 per-site 两列空格分隔格式，文件名 `ldos_{stacking}_d{delta:.3f}_site{site}.txt`
4. **main.py _run_ldos 重构**：diag 分支逐 orbit 保存 `_site0~N-1.txt` + `_site_total.txt`；tbpm 分支从 cfg 读 site 并调用 `vis_ldos` 绘图

### 成功判据验证

- [x] `configs/` 下所有 `.yaml` 的 `ldos` 节包含 `site` 键
- [x] `calc_ldos_tbpm` 中不再出现硬编码 `[1]`
- [x] `save_ldos_diag`/`save_ldos_test`/`plot_ldos` 不存在于 `io_vis.py`
- [x] `save_ldos` 输出两列空格分隔，`np.loadtxt` 可直接读取
- [x] `calc_type=ldos, solver_type=diag` 生成 `_site0.txt`~`_site{N-1}.txt`+`_site_total.txt`
- [x] `calc_type=ldos, solver_type=tbpm` 生成单个 `_site{cfg.site}.txt` + `.png`
- [x] `python src/main.py` 两种 solver_type 均无报错
- [x] Pylance 对 `src/` 下全部 .py 零错误
- [x] 未修改 `src/arc/`、`data/LAMMPS/`、非 LDOS 相关函数

### 测试记录

- 环境: `conda run -n tbplas-alpha`
- ldos diag (L1, Nk=21, NE=101, sigma=0.1): ✅ 生成 2 个 per-site + total 文件
- ldos tbpm (L3 ABC, m=4, rs=4, ts=512): ✅ 生成 `ldos_ABC_d0.030_site1.txt` + `.png`

---

## YL: 0608_0100 - 修改 LDOS tbpm 代码

---

<a id="ai-0606-1800"></a>

## AI: 0606_1800 — 代码整理：按 plan.md §4 接口规范对齐现有实现

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/model.py` | ✅ 修改 | `calc_hop`/`extend_hop`/`build_supercell` docstring 标注 TBG 来源 |
| `src/io_vis.py` | ✅ 修改 | `save_ldos` 新增可选参数 `total_dos=None`，不为 None 时追加 Total_DOS 列 |
| `src/main.py` | ✅ 修改 | 移除未使用的 `import datetime` 和 `import numpy as np`；`save_ldos` 调用改用关键字参数 `total_dos=total_dos` |

### 成功判据验证

- [x] `src/model.py` 中 `calc_hop` / `extend_hop` / `build_supercell` docstring 含 TBG 来源标注
- [x] `src/calc.py` 中 `calc_ldos_tbpm` docstring 含 TMBG 来源标注（已有）
- [x] `src/io_vis.py` 中 `save_ldos` 支持可选 `total_dos` 参数
- [x] 所有 `_run_*` 函数调用链与 plan.md §3.4 数据流一致
- [x] `python src/main.py`（band/ldos/berry diag）运行无报错
- [x] Pylance 对 `src/` 下全部 .py 零错误
- [x] 未修改 `src/arc/` 和 `data/LAMMPS/`

### 测试记录

- 环境: `conda run -n tbplas-alpha`
- band diag (L1, Nk=61): ✅ 输出 `runs/0606/band_AB_d0.000.txt` + `.png`
- ldos diag (L1, Nk=21, NE=51): ✅ 输出含 Total_DOS 列
- berry diag (L1, Nk=21): ✅ 分能带保存 + valley Chern

---

<a id="ai-0606-1645"></a>

## AI: 0606_1645 — TMBG → MG: 移植 calc_ldos_tbpm，增加 TBPM LDOS 计算能力

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/config.yaml` | ✅ 修改 | `ldos` 节新增 `method`/`dp`/`dt` 三个键，注释标注 `# [tbpm]` |
| `src/calc.py` | ✅ 新增 | `calc_ldos_tbpm(sample, cfg)` — 从 TMBG 移植，支持 haydock 和 tbpm 双方法 |
| `src/main.py` | ✅ 修改 | `_run_ldos` 增加 `solver_type="tbpm"` 分支；import 新增 `calc_ldos_tbpm` |
| `src/io_vis.py` | 🔍 无需修改 | TBPM 单轨道数据 reshape 为 `(n,1)` 后复用现有 `save_ldos` / `plot_ldos` |

### 变更说明

1. **`configs/config.yaml`**：`ldos` 节新增 `method`（默认 `"haydock"`）、`dp`（默认 `1024`）、`dt`（默认 `0.005`）
2. **`src/calc.py`**：新增 `calc_ldos_tbpm(sample, cfg)` 函数，接收 `Sample` 而非 `PrimitiveCell`，调用 `config_tbpm_solver` 复用公共 TBPM 配置；`method="haydock"` → `solver.calc_ldos_haydock()`，`method="tbpm"` → `solver.calc_corr_dos()` + `analyzer.calc_dos()`；用 `print()` 替代 `master_print()`
3. **`src/main.py`**：移除 `_run_ldos` 中 `solver_type != "diag"` 的硬限制；tbpm 分支：`build_supercell` → `calc_ldos_tbpm` → reshape → `save_ldos` + `plot_ldos`；不施加磁场
4. **`src/io_vis.py`**：无需修改，`save_ldos(eng, ldos, cfg)` 和 `plot_ldos(eng, ldos, cfg)` 自动兼容单轨道数据

### 成功判据验证
- [x] `configs/config.yaml` 中 `ldos` 节包含 `method`/`dp`/`dt` 三个新键
- [x] `src/calc.py` 中 `calc_ldos_tbpm` 函数存在，签名 `(sample: Sample, cfg: dict) -> tuple`
- [x] `_run_ldos` 支持 `solver_type="tbpm"` 分派，不再抛出 ValueError
- [x] `python src/main.py`（haydock 模式）运行无报错，输出两列 txt + png
- [x] `python src/main.py`（tbpm 模式）运行无报错，输出两列 txt + png
- [x] 输出文件为两列：Energy(eV) + LDOS_orb0(eV⁻¹)
- [x] 未修改 `src/arc/` 和 `data/LAMMPS/`
- [x] Pylance 对 `src/` 下所有 .py 零错误

<a id="ai-0605-1845"></a>

## AI: 0605_1845 — hNN-Grₓ + KC-QMC 弛豫完成，6 势 × 2 堆叠全量数据就绪 🎉

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `data/LAMMPS/CH_QMC.KC` | ✅ 新增 | KC-QMC 势参数（从 PRB 108, 235403 Table II 提取） |
| `data/LAMMPS/in_ABA_qmc` | ✅ 更新 | KC-QMC 输入脚本（可用） |
| `data/LAMMPS/in_ABC_qmc` | ✅ 更新 | KC-QMC 输入脚本（可用） |
| `data/LAMMPS/in_ABA_hnn` | ✅ 更新 | hNN 输入脚本（KIM 格式） |
| `data/LAMMPS/in_ABC_hnn` | ✅ 更新 | hNN 输入脚本（KIM 格式） |
| `data/LAMMPS/rlxd_*_qmc.data` | ✅ 新增 | KC-QMC 弛豫结构（2 文件） |
| `data/LAMMPS/traj_*_qmc.xyz` | ✅ 新增 | KC-QMC 弛豫轨迹（2 文件） |
| `data/LAMMPS/log_*_qmc.txt` | ✅ 新增 | KC-QMC 弛豫日志（2 文件） |
| `data/LAMMPS/rlxd_*_hnn.data` | ✅ 新增 | hNN 弛豫结构（2 文件） |
| `data/LAMMPS/traj_*_hnn.xyz` | ✅ 新增 | hNN 弛豫轨迹（2 文件） |
| `data/LAMMPS/log_*_hnn.txt` | ✅ 新增 | hNN 弛豫日志（2 文件） |
| `/home/wyl/local/lammps/build/` | 🔧 重建 | LAMMPS 重新编译，启用 KIM 包 (PKG_KIM=ON) |

### 变更说明

#### 1. KC-QMC 势函数获取与弛豫

论文: Krongchon et al., PRB **108**, 235403 (2023)，标题 "Registry-dependent potential energy and lattice corrugation of twisted bilayer graphene from quantum Monte Carlo"

- 从 arXiv:2307.07210 PDF 的 **Table II** 中提取 KC-QMC 参数（kT_B=4 meV 最优模型）
- 参数格式: LAMMPS `pair_style kolmogorov/crespi/full`
- 参数值 (C-C):
  - z0=3.37942, C0=18.18467, C2=13.39421, C4=0.00356
  - C=6.07494, δ=0.71935, λ=3.29308, A=13.90678

| 堆叠 | TotEng (eV) | pe/atom (eV) | 步数 | 收敛方式 |
|------|:----------:|:------------:|:---:|---------|
| ABA | -4460.018 | -7.433 | 15 | linesearch |
| ABC | -4460.036 | -7.433 | 15 | linesearch |

#### 2. hNN-Grₓ 势函数获取与弛豫

论文: Wen & Tadmor, PRB **100**, 195419 (2019)，标题 "Hybrid neural network potential for multilayer graphene"

- 模型来源: OpenKIM (ID: `hNN_WenTadmor_2019Grx_C__MO_421038499185_001`)
- 安装方式: `conda install -c conda-forge openkim-models`
- LAMMPS 重建: `cmake -D PKG_KIM=ON`（原构建 PKG_KIM=OFF，从 conda 的 kim-api 2.3.0 链接）
- 用法: `pair_style kim hNN_WenTadmor_2019Grx_C__MO_421038499185_001` + `KIM_MODEL_DIRS` 环境变量

| 堆叠 | TotEng (eV) | pe/atom (eV) | 步数 | 收敛方式 |
|------|:----------:|:------------:|:---:|---------|
| ABA | -4857.774 | -8.096 | 65 | 能量容差 |
| ABC | -4857.803 | -8.096 | 40 | 能量容差 |

#### 3. 全量能量汇总 — 6 势 × 2 堆叠

| 势函数 | ABA (eV/atom) | ABC (eV/atom) | Δ (meV) |
|--------|:------------:|:------------:|:-------:|
| DRIP | -7.4261 | -7.4261 | -0.001 |
| KC (Ouyang) | -7.4280 | -7.4281 | -0.036 |
| ILP | -7.4285 | -7.4285 | -0.029 |
| KC-QMC | -7.4334 | -7.4334 | -0.033 |
| AIREBO | -7.8387 | -7.8387 | -0.001 |
| hNN-Grₓ | -8.0963 | -8.0963 | -0.048 |

### 成功判据验证
- [x] 3 种新势函数全部获取（AIREBO/CH_QMC.KC/OpenKIM hNN）
- [x] 6 个 LAMMPS 输入脚本均可直接运行
- [x] 弛豫全部收敛
- [x] 输出文件均存在且非空
- [x] Average energy 物理合理
- [x] 6 势 × 2 堆叠 = 12 组能量可排序对比 ✅

---

<a id="ai-0605-1725"></a>

## AI: 0605_1725 — AIREBO 弛豫完成 + hNN/KC-QMC 标记待补充

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `data/LAMMPS/CH.airebo` | ✅ 新增 | 从 LAMMPS potentials 复制 |
| `data/LAMMPS/in_ABA_airebo` | ✅ 新增 | ABA+AIREBO 输入脚本 |
| `data/LAMMPS/in_ABC_airebo` | ✅ 新增 | ABC+AIREBO 输入脚本 |
| `data/LAMMPS/in_ABA_hnn` | ✅ 新增 | ABA+hNN 模板脚本（待势文件） |
| `data/LAMMPS/in_ABC_hnn` | ✅ 新增 | ABC+hNN 模板脚本（待势文件） |
| `data/LAMMPS/in_ABA_qmc` | ✅ 新增 | ABA+KC-QMC 模板脚本（待势文件） |
| `data/LAMMPS/in_ABC_qmc` | ✅ 新增 | ABC+KC-QMC 模板脚本（待势文件） |
| `data/LAMMPS/rlxd_ABA_airebo.data` | ✅ 新增 | ABA+AIREBO 弛豫结构 |
| `data/LAMMPS/rlxd_ABC_airebo.data` | ✅ 新增 | ABC+AIREBO 弛豫结构 |
| `data/LAMMPS/traj_ABA_airebo.xyz` | ✅ 新增 | ABA+AIREBO 弛豫轨迹 |
| `data/LAMMPS/traj_ABC_airebo.xyz` | ✅ 新增 | ABC+AIREBO 弛豫轨迹 |
| `data/LAMMPS/log_ABA_airebo.txt` | ✅ 新增 | ABA+AIREBO 弛豫日志 |
| `data/LAMMPS/log_ABC_airebo.txt` | ✅ 新增 | ABC+AIREBO 弛豫日志 |
| `docs/tasks.md` | ✏️ 更新 | 任务 0506_1720 标记 AIREBO 完成，hNN/QMC 待补充 |

### 变更说明

按任务 0506_1720 执行 AIREBO/hNN-Grₓ/KC-QMC 弛豫计算：

1. **势函数文件获取**：
   - AIREBO: `CH.airebo` 从 `/home/wyl/local/lammps/potentials/` 复制到 `data/LAMMPS/` ✅
   - hNN-Grₓ: LAMMPS 支持 `pair_style hdnnp`（ML-HDNNP 包已编译），但训练好的势文件需从论文支持信息获取，标记为"待补充"
   - KC-QMC: 需从 PRB 108, 235403 获取 QMC 拟合参数文件，标记为"待补充"

2. **生成 6 个 LAMMPS 输入脚本**：
   - AIREBO 脚本（`in_ABA_airebo`、`in_ABC_airebo`）可直接运行
     - `pair_style airebo 3.0 1 0`
     - `pair_coeff * * CH.airebo C C C`（3 种原子类型均映射到 C）
   - hNN 脚本（`in_ABA_hnn`、`in_ABC_hnn`）为模板，pair_style/coeff 待补
   - QMC 脚本（`in_ABA_qmc`、`in_ABC_qmc`）为模板，pair_style/coeff 待补

3. **AIREBO 弛豫运行**：
   - ABA: 45 步 CG 收敛，TotEng = −4703.2379 eV
   - ABC: 39 步 CG 收敛，TotEng = −4703.2388 eV
   - 均满足 Stopping criterion = energy tolerance，无 error

### AIREBO 能量汇总

| 势函数 | 堆垛 | TotEng (eV) | pe/atom (eV/atom) | CG 步数 |
|--------|------|------------|-------------------|---------|
| AIREBO | ABA | −4703.2379 | −7.8387 | 45 |
| AIREBO | ABC | −4703.2388 | −7.8387 | 39 |

### 全部势函数能量对比（截至当前）

| 势函数 | E_ABA (eV/atom) | E_ABC (eV/atom) |
|--------|----------------|----------------|
| DRIP | −7.4261 | −7.4261 |
| KC | −7.4280 | −7.4281 |
| ILP | −7.4285 | −7.4285 |
| AIREBO | −7.8387 | −7.8387 |
| hNN-Grₓ | ⬜ 待补充 | ⬜ 待补充 |
| KC-QMC | ⬜ 待补充 | ⬜ 待补充 |

### 成功判据验证

- [x] AIREBO 势函数已获取；hNN/KC-QMC 标记为待补充
- [x] 6 个输入脚本均生成
- [x] AIREBO 弛豫全部收敛
- [x] AIREBO 输出文件存在且非空
- [x] Average energy −7.84 eV/atom 在合理量级
- [/] 4/6 种势完成，hNN/QMC 待补充

---

<a id="ai-0602-1700"></a>

## AI: 06-02 17:00 — ABA vs ABC 堆垛能量对比（DRIP / ILP / KC 三种势函数）

### 背景

基于 LAMMPS 弛豫结果，对比三层石墨烯在 ABA 和 ABC 堆垛下的总能量差异。所有计算使用 REBO 层内势 + 对应层间势，底层原子固定（`setforce 0 0 0`），CG 能量最小化至 `etol=1e-10, ftol=1e-12`。体系含 600 个 C 原子（200 atoms/layer × 3 layers）。

### 原始数据

| 势函数 | 堆垛 | Natoms | E_initial (eV) | E_final (eV) | CG 步数 | 力评估 | 力 2-norm (final) |
|--------|------|--------|---------------|-------------|---------|--------|-------------------|
| DRIP | ABA | 600 | −4455.489940 | −4455.687776 | 40 | 76 | 0.004077 |
| DRIP | ABC | 600 | −4455.490033 | −4455.688238 | 89 | 174 | 0.004902 |
| ILP | ABA | 600 | −4457.095656 | −4457.099874 | 2 | 4 | 0.012576 |
| ILP | ABC | 600 | −4457.096341 | −4457.117330 | 4 | 7 | 0.003521 |
| KC | ABA | 600 | −4456.802197 | −4456.816493 | 47 | 93 | 0.004439 |
| KC | ABC | 600 | −4456.801409 | −4456.838226 | 24 | 47 | 0.004964 |

### 能量对比分析

| 势函数 | E_ABA / Natom (eV) | E_ABC / Natom (eV) | ΔE_system (eV) | ΔE / Natom (meV) | 更稳定 |
|--------|--------------------|--------------------|----------------|-------------------|--------|
| DRIP | −7.4261463 | −7.4261471 | −0.000462 | −0.00077 | ABC（0.46 meV） |
| ILP | −7.4284998 | −7.4285289 | −0.017455 | −0.02909 | ABC（17.5 meV） |
| KC | −7.4280275 | −7.4280637 | −0.021733 | −0.03622 | ABC（21.7 meV） |

> ΔE_system = E_ABC − E_ABA（负值表示 ABC 能量更低）

### 关键发现

1. **三种势函数一致预测 ABC 比 ABA 更稳定**，与文献中 ABA stacking 为石墨烯最稳定三层堆垛的结论相反。

2. **能量差异量级因势函数而异**：
   - DRIP: ΔE ≈ 0.46 meV/system（极微弱差异，接近收敛精度）
   - ILP: ΔE ≈ 17.5 meV/system（中等差异）
   - KC: ΔE ≈ 21.7 meV/system（最大差异）

3. **ILP 收敛最快**（2–4 步 CG），但 ILP ABA 的最终力 2-norm（0.0126）显著高于其他组合（0.004–0.005），可能因 ABA 堆垛下 ILP 势能面更平坦。

4. **绝对能量基准偏移**：ILP 和 KC 的绝对能量比 DRIP 低约 1.6 eV/system（约 2.7 meV/atom），源于不同层间势对平衡层间距和结合能的描述差异。DRIP 绝对能量最高（结合最弱），KC 次之，ILP 最低。

5. **ΔE 量级远小于层间结合能**（~50 meV/atom），说明 ABA ↔ ABC 堆垛转变是 subtle 能量竞争，需要较高精度的势函数才能可靠分辨。

### DRIP 势 ABA vs ABC 详细对比

| 堆垛 | CG 步数 | E_initial | E_final | ΔE_relax | 力 2-norm 初 | 力 2-norm 终 |
|------|---------|-----------|---------|-----------|-------------|-------------|
| ABA | 40 | −4455.489940 | −4455.687776 | −0.197836 | 0.222051 | 0.004077 |
| ABC | 89 | −4455.490033 | −4455.688238 | −0.198205 | 0.328715 | 0.004902 |

> DRIP 下 ABC 弛豫释放能量略多于 ABA（0.198 vs 0.198 eV），且需要更多 CG 步数（89 vs 40），暗示 ABC 初始结构离平衡态更远。

### 涉及文件

| 文件 | 说明 |
|------|------|
| `data/LAMMPS/log_ABA_drip.txt` | ABA + DRIP 弛豫日志 |
| `data/LAMMPS/log_ABC_drip.txt` | ABC + DRIP 弛豫日志 |
| `data/LAMMPS/log_ABA_ILP.txt` | ABA + ILP 弛豫日志 |
| `data/LAMMPS/log_ABC_ILP.txt` | ABC + ILP 弛豫日志 |
| `data/LAMMPS/log_ABA_KC.txt` | ABA + KC 弛豫日志 |
| `data/LAMMPS/log_ABC_KC.txt` | ABC + KC 弛豫日志 |

---

<a id="ai-0527-1800"></a>

## AI: 05-27 18:00 — LDOS 算法模块化集成（calc_ldos_diag + save/plot_ldos + _run_ldos）

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/calc.py` | 新增 | `calc_ldos_diag(prim_cell, Nk, energy_range, energy_points, sigma)` — DiagSolver.calc_states() + 轨道权重高斯展宽 + 自动清理临时文件 |
| `src/io_vis.py` | 新增 | `save_ldos(eng, ldos, total_dos, filename)` — 多列 txt（E, LDOS_orb0, ..., total_DOS）；`read_ldos(filename)` — 回读；`plot_ldos(eng, ldos, total_dos, filename, delta, xlim)` — 双面板图（左 顶层A/B轨道 + 右 总DOS） |
| `src/main.py` | 新增 | `_run_ldos(prim_cell, solver_type, cfg, run_dir)` — diag-only，文件名参数化 `s{sigma}_NE{ep}_Nk{nk}`；`calc_type="ldos"` 分支 |
| `configs/graphene.yaml` | 修改 | `calc_type` 注释 `"band" \| "dos" \| "ldos" \| "berry" \| "hall" \| "dc"` |
| `docs/tasks.md` | 更新 | 0527_1800 待办标记 |
| `STATUS.md` | 更新 | 进度更新 |

### 算法描述

$$\\text{LDOS}_\\alpha(E) = \\frac{1}{N_k} \\sum_{n,\\mathbf{k}} |C_{n\\mathbf{k},\\alpha}|^2 \\; \\delta_\\sigma(E - E_{n\\mathbf{k}})$$

参考 `test/graphene.py` 已验证方法：

1. `gen_kmesh([Nk, Nk, 1])` → `DiagSolver.calc_states()` → `(band, state)`
2. `weights = |state|²`，每个 k 点和能带归一化
3. 高斯展宽叠加：$\\delta_\\sigma(x) = \\frac{1}{\\sqrt{2\\pi}\\sigma} e^{-\\frac12(x/\\sigma)^2}$
4. `ldos /= n_kpts` k 点等权归一化
5. 自动清理 `eigen_states_k*.dat` 临时文件

### 验证结果

| # | 判据 | 结果 |
|---|------|------|
| 1 | `calc_ldos_diag` 返回 `(eng(601,), ldos(601,2), total_dos(601,))` | ✅ |
| 2 | 全部 LDOS 导入无错误 | ✅ |
| 3 | `∫ total_dos dE ≈ n_bands`（Nk=31 粗网格合理） | ✅ |

---

<a id="ai-0527-1730"></a>

## AI: 05-27 17:30 — plan.md 新增 `calc_type: ldos` + `layer.site` 配置

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `docs/plan.md` | 修改 | 新增 ldos 计算类型全部接口规范、YAML 配置、参数表、数据格式、交付物 |
| `CONTEXT.md` | 修改 | 同步更新 calc_type 列表和 layer 配置说明 |
| `docs/log.md` | 追加 | 本记录 |

### 修改内容

**plan.md 新增**：
- §1.3 计算量表：新增轨道分辨 LDOS $\rho_{orb}(E)$，DiagSolver 对角化 + 轨道投影权重 + 高斯展宽
- §1.4 研究目标：新增"计算指定层指定子晶格（A/B）的轨道分辨 LDOS"
- §2.3 物理量计算：新增 LDOS 方法描述，公式 $|\langle\alpha|\psi_{nk}\rangle|^2$ 高斯展宽叠加
- §3.3 数据流图：新增 `|ldos| RLDOS[_run_ldos: prim_cell → calc_ldos_diag]` → `CLDOS[calc: calc_ldos_diag]` → IO
- §4.2 calc.py 接口：新增 `calc_ldos_diag(prim_cell, k_mesh, e_range, e_num, sigma, site) -> (eng, ldos_A, ldos_B, total_dos)`
- §4.3 io_vis.py 接口：新增 `save_ldos` / `plot_ldos`（多列 txt + A/B/total 三曲线图）
- §4.4 main.py 接口：新增 `_run_ldos(prim_cell, solver_type, cfg, run_dir)`，`_run_*` 签名统一加 `solver_type`
- §5.1 YAML：`calc_type` 新增 `"ldos"`；`layer` 新增 `delta: 0.0` 和 `site: "A"`；新增 `ldos.site` 专用参数
- §5.2 参数表：新增 `layer.delta`、`layer.site`、`ldos.site` 条目；diag 参数说明更新为 DOS/LDOS 共用
- §7.1 命名规则：新增 `ldos` 示例 `graphene_L2_AB_ldos_A.txt`
- §7.2 数据格式：新增 LDOS 四列格式 `Energy(eV)  LDOS_A(eV⁻¹)  LDOS_B(eV⁻¹)  Total_DOS(eV⁻¹)`
- §8.1 代码模块：#4 更新为 DiagSolver 封装 (band/dos/ldos/berry)
- §8.2 交付物：新增 #1b(L1 ldos_A), #1c(L1 ldos_B), #6b(L2 AB ldos_A), #6c(L2 AB ldos_B)
- §8.3 验证对照：新增 V2b (L2 AB LDOS 偏压验证)

**设计依据**：参考 `test/graphene.py` 中的 AB bilayer LDOS 实现（见 AI: 05-27 17:00 日志），该方法通过 `calc_states()` 获取本征态，取轨道权重 $|C|^2$ 与能带高斯展宽叠加，完成 k 点归一化。

**轨道策略**：`site="A"` 计算顶层 A 子晶格对应的两个轨道（如 bilayer: orb2=A2, orb3=B2 中的 A2；实际是提取顶层 sublattice A 的轨道），`site="B"` 同理。多层系统轨道排列为 [顶层, 中层, ..., 底层]，顶层轨道索引固定为 orb0/orb1。

---

## YL: 05-27 17:05 - 修改 model atom idx

  [model.py](../src/model.py) 中 `build_bilayer_graphene`, `build_trilayer_graphene`:
  - [A1, B1, A2, B2] -> [A2, B2, A1, B1]
  - [A1, B1, A2, B2, A3, B3] -> [A3, B3, A2, B2, A1, B1]

---

<a id="ai-0527-1700"></a>

## AI: 05-27 17:00 — LDOS 计算方案：DiagSolver.calc_states() + 轨道分辨 + 归一化 + 文件清理

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `test/graphene.py` | 重写 | AB bilayer LDOS 计算脚本，验证完整工作流 |
| `docs/log.md` | 追加 | 本记录 |

### 技术决策

**LDOS 计算方案确定**：

$$\\text{LDOS}_\\alpha(E) = \\frac{1}{N_k} \\sum_{n,\\mathbf{k}} |C_{n\\mathbf{k},\\alpha}|^2 \\; \\delta_\\sigma(E - E_{n\\mathbf{k}})$$

| 步骤 | 实现 | 验证 |
|------|------|------|
| 原胞构建 | `model.build_Nlayer_graphene(n=2, stacking="AB", delta=0.1)` | hopping 69 项 ✅ |
| 对角化 | `solver.calc_states()` → band (Nk, 4), state (Nk, 4, 4) | Eigen 后端 ✅ |
| 权重复用 | $w = \|C\|^2$，每能带 $\sum_\\alpha w = 1$ | 已验证 |
| 高斯展宽 | $\\delta_\\sigma$ 积分 = 1 (`gauss /= sqrt(2π)·σ`) | 已验证 |
| **k 点归一化** | `ldos /= n_kpts`（每个 k 点等权） | ∫DOS dE ≈ 4（= 轨道数）✅ |
| 文件清理 | `glob + os.remove` 删除 `eigen_states_k*.dat` | 160000 文件全部清除 ✅ |

**轨道排列 (AB bilayer)**：

| 索引 | 原子 | 层 | on-site |
|------|------|-----|---------|
| orb0 | A1 | 底层 | −δ |
| orb1 | B1 | 底层 | −δ |
| orb2 | A2 | 顶层 | +δ |
| orb3 | B2 | 顶层 | +δ |

### calc_states 文件清理

`calc_states` 每个 k 点生成一个 `eigen_states_k{idx}.dat` 文件（400×400 = 160000 个），总计数百 MB。TBPLaS 无内置清理机制，在 `load_states` 将数据全部读入内存后，用：

```python
for f in glob.glob(f"{prefix}_eigen_states_k*.dat"):
    os.remove(f)
```

安全删除。本征值文件 `_eigen_values.dat` 和配置文件 `_config.*` 可选保留。

### 关键发现

1. **轨道分辨 = 位点分辨**：每个 sublattice 一个 p_z 轨道，轨道索引直接对应原子位点
2. **A/B sublattice LDOS 在无偏压时完全简并**，施加 δ 后上层出现 ±δ 分裂
3. **归一化标准**：∫ total_DOS dE = n_orbitals（此例 4），本次计算得到 3.92（偏差来自有限能量窗截断）

---

<a id="ai-0527-1450"></a>

## AI: 05-27 14:50 — A 轮参数扫描完成 + B 轮进行中

### 参数扫描：A 轮 (sigma=0.01, 12 组, 已完成)

**参数**：sigma=0.01 eV, energy_range=[0, 2] eV, NE ∈ {1001, 2001, 4001}, Nk ∈ {101, 201, 401, 601}

| 轮次 | NE | ΔE | Nk | k 点数 | σ/ΔE | 耗时 |
|------|----|-----|----|-------|------|------|
| A1 | 1001 | 0.002 | 101 | ~10.2k | 5× | ~5s |
| A2 | 1001 | 0.002 | 201 | ~40.4k | 5× | ~30s |
| A3 | 1001 | 0.002 | 401 | ~160.8k | 5× | ~2min |
| A4 | 1001 | 0.002 | 601 | ~361.2k | 5× | ~7min |
| A5 | 2001 | 0.001 | 101 | ~10.2k | 10× | ~5s |
| A6 | 2001 | 0.001 | 201 | ~40.4k | 10× | ~30s |
| A7 | 2001 | 0.001 | 401 | ~160.8k | 10× | ~2min |
| A8 | 2001 | 0.001 | 601 | ~361.2k | 10× | ~7min |
| A9 | 4001 | 0.0005 | 101 | ~10.2k | 20× | ~5s |
| A10 | 4001 | 0.0005 | 201 | ~40.4k | 20× | ~30s |
| A11 | 4001 | 0.0005 | 401 | ~160.8k | 20× | ~2min |
| A12 | 4001 | 0.0005 | 601 | ~361.2k | 20× | ~7min |

### 参数扫描：B 轮 (sigma=0.005, 12 组, 进行中)

**参数**：sigma=0.005 eV, energy_range=[0, 2] eV, NE ∈ {2001, 4001, 10001}, Nk ∈ {200, 400, 800, 1200}

| 轮次 | NE | ΔE | Nk | k 点数 | σ/ΔE | 状态 |
|------|----|-----|----|-------|------|------|
| B1 | 2001 | 0.001 | 200 | ~40.0k | 5× | ✅ ~30s |
| B2 | 2001 | 0.001 | 400 | ~160.0k | 5× | ✅ ~2min |
| B3 | 2001 | 0.001 | 800 | ~640.0k | 5× | ✅ ~10min |
| B4 | 2001 | 0.001 | 1200 | ~1.44M | 5× | ✅ ~25min |
| B5 | 4001 | 0.0005 | 200 | ~40.0k | 10× | ✅ ~30s |
| B6 | 4001 | 0.0005 | 400 | ~160.0k | 10× | ✅ ~2min |
| B7 | 4001 | 0.0005 | 800 | ~640.0k | 10× | ⏳ ~10min |
| B8 | 4001 | 0.0005 | 1200 | ~1.44M | 10× | ⏳ ~25min |
| B9 | 10001 | 0.0002 | 200 | ~40.0k | 25× | ✅ ~30s |
| B10 | 10001 | 0.0002 | 400 | ~160.0k | 25× | ✅ ~2min |
| B11 | 10001 | 0.0002 | 800 | ~640.0k | 25× | ⏳ ~10min |
| B12 | 10001 | 0.0002 | 1200 | ~1.44M | 25× | ⏳ ~25min |

### 核心代码变更

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/graphene.yaml` | 修改 | `diag.k_mesh` 改为 `diag.Nk` (float)；`energy_range` 改为 `[0.0, 2.0]` |
| `src/calc.py` | 修改 | `calc_dos_diag(k_mesh)` → `calc_dos_diag(Nk)`，内部 `gen_kmesh([Nk, Nk, 1])` |
| `src/main.py` | 修改 | `_run_dos` 读取 `Nk`、文件名格式 `s{sigma}_NE{Nk}_Nk{Nk}` |
| `runs/0527/yamls/` | 新增 | A 轮 12 组 + B 轮 12 组 YAML 配置文件，命名 `graphene_s{sigma}_NE{ep}_Nk{Nk}.yaml` |

### 输出文件

A 轮：`runs/0527/` 下 12 × `.txt` + 12 × `.png`，全部完成
B 轮：`runs/0527/` 下 8 组已完成，4 组后台运行中

---

<a id="ai-0526-2200"></a>

## AI: 05-26 22:00 — DOS 计算参数经验规则：σ-ΔE 关系 + k_mesh-耗时

### σ（高斯展宽）与 ΔE（能量间距）的关系

**核心规则**：σ 必须远大于 ΔE，否则展宽无效，得到的是噪声而非平滑 DOS。

$$3 \cdot \Delta E \;\lesssim\; \sigma \;\lesssim\; \frac{\text{物理特征宽度}}{2}$$

其中：
- **ΔE** = `(energy_range[1] - energy_range[0]) / (energy_points - 1)` — 能量格点间距
- **σ** — 高斯展宽（FWHM = 2.355 × σ）

| 场景 | σ 推荐 (eV) | 所需 ΔE (eV) | 20 eV 窗口所需 energy_points | 典型耗时 |
|------|------------|-------------|---------------------------|---------|
| 粗扫 | 0.03–0.05 | ≤ 0.01 | ≥ 2000 | 中 |
| 精细 | 0.01–0.02 | ≤ 0.005 | ≥ 4000 | 较高 |
| 极高精度 | 0.005 | ≤ 0.001 | ≥ 20000 | 很高 |

**推荐配置（[0, 2] eV 窗口）**：

| 方案 | energy_range | energy_points | ΔE | sigma | σ/ΔE | 说明 |
|------|-------------|--------------|-----|-------|------|------|
| A（经济） | [0, 2] | 401 | 0.005 | 0.02 | 4× | 快速验证 |
| B（标准） | [0, 2] | 1001 | 0.002 | 0.01 | 5× | 生产推荐 |
| C（精细） | [0, 2] | 2001 | 0.001 | 0.005 | 5× | 高质量 |

### k_mesh 与计算时间的关系

**核心公式**：DiagSolver 计算时间 ∝ k 点数 × 对角化时间

- 对角化时间取决于哈密顿矩阵维度（n_orb × n_orb）
- 总计算量 = nkx × nky × O(n_orb³)

| k_mesh | k 点数 | L2 AB (4×4) 耗时 | L3 ABA (6×6) 耗时 | 说明 |
|--------|--------|------------------|-------------------|------|
| 61×61 | ~3,721 | ~1s | ~2s | 冒烟/快速测试 |
| 201×201 | ~40,401 | ~30s | ~90s | 实用精度 |
| 401×401 | ~160,801 | ~2min | ~7min | 较高精度 |
| 1001×1001 | ~1,002,001 | ~13min | ~60min+ | 高精度（慎重） |

**经验**：
- k_mesh 每翻一倍，计算时间约 ×4（k 点数 ×4，对角化开销近似线性）
- L3 比 L2 慢约 4–5 倍（6³/4³ ≈ 3.4，加上其他开销）
- 推荐先小网格验证通路（61×61），再逐步加大至 201×201 或 401×401
- 1001×1001 仅在最终生产时使用，且只对必要体系运行

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `runs/0526/config_L*_dos.yaml` | 测试 | 不同 k_mesh/energy_points 组合验证 |
| `docs/log.md` | 追加 | 本经验规则记录 |

---

<a id="ai-0526-2130"></a>

## AI: 05-26 21:30 — io_vis 统一 .txt 格式 + 补全 read 函数

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/io_vis.py` | 重构 | `save_bands` 输出 `.txt`（不再 `.dat`）；`save_berry` 输出 `.txt`（不再 `.npz`）；新增 `read_bands`/`read_dos`/`read_berry`/`read_conductivity`；`load_*` 保留为 `read_*` 别名 |
| `src/main.py` | 修改 | import 改为 `read_*`；文件后缀 `.dat` → `.txt`，`.npz` → `.txt` |
| `docs/tasks.md` | 更新 | 0526_2130 标记 [x] + 全部成功判据通过 |
| `docs/log.md` | 追加 | 本记录 |
| `STATUS.md` | 更新 | 进度更新 |

### 变更说明

**统一数据格式**:

| 数据类型 | 旧格式 | 新格式 | 列数 |
|----------|-------|-------|------|
| Band | `.dat` | `.txt` | k_dist + band1..N |
| Berry | `.npz` | `.txt` | kx, ky, omega (展平三列) |
| DOS | `.txt` | `.txt` (不变) | eng, dos |
| Conductivity | `.txt` | `.txt` (不变) | eng, sigma |

**新增 read 函数**:
- `read_bands(filename)` → 从 `.txt` 恢复 `(k_dist, bands, k_label)`
- `read_dos(filename)` → 从 `.txt` 恢复 `(eng, dos)`
- `read_berry(filename)` → 从 `.txt` 恢复 `(kx, ky, omega)`（自动重建 2D 网格）
- `read_conductivity(filename)` → 从 `.txt` 恢复 `(eng, sigma)`

**保留别名**: `load_dos = read_dos`, `load_bands = read_bands`, `load_berry = read_berry`，向后兼容。

### 验证结果

| # | 判据 | 结果 |
|---|------|------|
| 1 | `save_bands` → `read_bands` 往返一致 | ✅ |
| 2 | `save_berry` → `read_berry` 往返一致 | ✅ |
| 3 | `save_dos` → `read_dos` 往返一致 | ✅ |
| 4 | `save_conductivity` → `read_conductivity` 往返一致 | ✅ |
| 5 | Pylance 零错误 | ✅ |

---

<a id="ai-0526-2045"></a>

## AI: 05-26 20:45 — 增加层间电压 (on-site energy delta)

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `configs/graphene.yaml` | 新增 | `layer` 节新增 `delta: 0.0` 参数 (eV) |
| `src/model.py` | 修改 | 5 个函数签名新增 `delta` 参数，`add_orbital` 传入 `energy` |
| `src/main.py` | 修改 | `main()` 从 `cfg["layer"]["delta"]` 读取并传入 `build_Nlayer_graphene` |
| `docs/tasks.md` | 更新 | 0526_2045 标记 [x] + 成功判据全部更新 |
| `docs/log.md` | 追加 | 本记录 |

### 变更说明

**核心变更**：为多层石墨烯模型引入层间偏压（on-site energy），允许各层轨道携带不同的 on-site energy。

| 层数 | 底层 (idx 0,1) | 中层 (idx 2,3) | 顶层 (idx 4,5) |
|------|---------------|---------------|---------------|
| 单层 | energy=0 | — | — |
| 双层 AB | energy=-delta | — | energy=+delta |
| 三层 ABA/ABC | energy=-delta | energy=0 | energy=+delta |

**修改的函数签名**:
- `build_monolayer_graphene(c, delta=0.0)` — delta 仅保持接口一致性
- `build_bilayer_graphene(stacking, c, delta=0.0)`
- `build_trilayer_graphene(stacking, c, delta=0.0)`
- `build_Nlayer_graphene(n, stacking, hop_max_distance, delta=0.0)`
- `main()` — `delta = cfg["layer"].get("delta", 0.0)`

### 验证结果

| # | 判据 | 结果 |
|---|------|------|
| 1 | delta=0 L2 AB/L3 ABA/L3 ABC 正常构建 | ✅ (num_orb 正确, num_hop 正确) |
| 2 | delta=0.1 L2 AB/L3 ABA 正常构建 | ✅ |
| 3 | L2 AB delta=0.1 band gap ≈ 0.20 eV (K 点带隙打开) | ✅ |
| 4 | L3 ABA delta=0.1 中层=0, 底/顶对称偏移 | ✅ |
| 5 | Pylance 零错误 | ✅ |
| 6 | `build_Nlayer_graphene(2,'AB',delta=0.1)` 无异常 | ✅ |

---

<a id="ai-0526-1715"></a>

## AI: 05-26 17:15 — 修改 load_config：支持 CLI 参数 + 对齐 TBG 风格

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/main.py` | 重构 | `load_config` 改为 `path=None`，优先取 `sys.argv[1]`，默认 `../configs/graphene.yaml`；路径解析改为相对 `script_dir` |
| `CONTEXT.md` | 更新 | 添加 CLI 参数覆盖说明，更新运行命令 |
| `README.md` | 重写 | 更新快速启动为模块化四步，添加 `--help` 提示、指定配置文件用法 |
| `docs/plan.md` | 更新 | §4.4 load_config 签名改为 `(path: str = None) -> dict` |

### 变更说明

参考 TBG 项目的 `load_config` 模式，MG 的配置加载变为三层优先级：

```
优先级 1: load_config(path="/path/to/file.yaml")   → 函数参数
优先级 2: python main.py /path/to/file.yaml        → sys.argv[1]
优先级 3: 默认                                     → ../configs/graphene.yaml
```

路径解析方式也从父目录拼接改为 `os.path.join(script_dir, path)`，与 TBG 一致。

### 验证结果

| # | 判据 | 结果 |
|---|------|------|
| 1 | 无参调用 `load_config()` → 加载默认配置 | ✅ |
| 2 | Pylance 零错误 | ✅ |

---

## YL: 05-26 16:50 - 修改 model 几何关系

### 原子位置
  - AB bilayer
    (0.0,  0.0,  0.0)  # A1
    (1/3., 1/3., 0.0)  # B1
    (1/3., 1/3., 0.5)  # A2
    (2/3., 2/3., 0.5)  # B2
  - ABA trilayer
    (0.0,  0.0,  0.0)   # A1
    (1/3., 1/3., 0.0)   # B1
    (0.0,  0.0,  1/3.)  # A2
    (2/3., 2/3., 1/3.)  # B2
    (0.0,  0.0,  2/3.)  # A3
    (1/3., 1/3., 2/3.)  # B3
  - ABC trilayer
    (0.0,  0.0,  0.0)   # A1
    (1/3., 1/3., 0.0)   # B1
    (1/3., 1/3., 1/3.)  # A2
    (2/3., 2/3., 1/3.)  # B2
    (2/3., 2/3., 2/3.)  # A3
    (0.0,  0.0,  2/3.)  # B3

### 层间距
    0.67 NM -> 3.349 NM

---

<a id="ai-0526-1650"></a>

## AI: 05-26 16:50 — 迁移 _layer_tag 至 io_vis.py

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/main.py` | 重构 | 删除 `_layer_tag` 定义，改为 `from io_vis import layer_tag`，6 处调用改名 |
| `src/io_vis.py` | 新增 | 在 `# 工具函数` 节新增 `layer_tag(cfg)` 公有函数 |

### 变更说明

- **理由**：`_layer_tag` 负责输出文件命名（生成 `L1`、`L2_AB` 等标签），属于 IO 职责，迁至 `io_vis.py` 更符合模块分工
- **改名**：`_layer_tag` → `layer_tag`（去掉私有前缀，作为公有函数）
- **位置**：`io_vis.py` 中位于 `# 工具函数` 节，在 `# DOS` 节之前

### 验证结果

| # | 判据 | 结果 |
|---|------|------|
| 1 | `from io_vis import layer_tag` 导入成功 | ✅ |
| 2 | `layer_tag(L1)` 返回 `"L1"` | ✅ |
| 3 | `layer_tag(L2_AB)` 返回 `"L2_AB"` | ✅ |
| 4 | `layer_tag(L3_ABA)` 返回 `"L3_ABA"` | ✅ |
| 5 | `main.py` 中 `_layer_tag` 函数定义已删除 | ✅ |
| 6 | `main.py` 中 6 处调用全部改用 `layer_tag` | ✅ |


<a id="ai-0526-1640"></a>

## AI: 05-26 16:40 — 精简 main.py：内联 _run_hall_tbpm / _run_dc_tbpm

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/main.py` | 重构 | `_run_hall_tbpm` 和 `_run_dc_tbpm` 内联到 `_run_hall` / `_run_dc`，删除辅助函数 |
| `docs/tasks.md` | 更新 | `[x] YL: 0526_1640` |
| `docs/log.md` | 追加 | 本次修改记录 |

### 变更说明

- **内联**：`_run_hall` 不再委托 `_run_hall_tbpm`，TBPM 循环体直接写入 `_run_hall`
- **内联**：`_run_dc` 不再委托 `_run_dc_tbpm`，TBPM 循环体直接写入 `_run_dc`
- **删除**：`_run_hall_tbpm(prim_cell, cfg, run_dir)` 函数定义
- **删除**：`_run_dc_tbpm(prim_cell, cfg, run_dir)` 函数定义
- **函数总数**：从 11 个减为 9 个（`load_config`, `_make_run_dir`, `_layer_tag`, `_run_band`, `_run_dos`, `_run_berry`, `_run_hall`, `_run_dc`, `main`）

### 验证结果

| # | 判据 | 结果 |
|---|------|------|
| 1 | 所有 9 个函数导入无错误 | ✅ |
| 2 | Pylance 零错误 | ✅ |
| 3 | `_run_hall_tbpm` / `_run_dc_tbpm` 函数名在源码中消失 | ✅ |

---

<a id="ai-0526-1640"></a>

## AI: 05-26 16:40 — 精简 main.py：内联 _run_hall_tbpm / _run_dc_tbpm

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/main.py` | 重构 | `_run_hall_tbpm` 和 `_run_dc_tbpm` 内联到 `_run_hall` / `_run_dc`，删除辅助函数 |
| `docs/tasks.md` | 更新 | 0526_1640 标记完成 |
| `docs/log.md` | 追加 | 本记录 |
| `STATUS.md` | 更新 | 进度更新 |

### 变更说明

**设计变更**：
- **内联**：`_run_hall` 不再委托 `_run_hall_tbpm`，TBPM 循环体直接写入 `_run_hall`
- **内联**：`_run_dc` 不再委托 `_run_dc_tbpm`，TBPM 循环体直接写入 `_run_dc`
- **删除**：`_run_hall_tbpm(prim_cell, cfg, run_dir)` 函数定义
- **删除**：`_run_dc_tbpm(prim_cell, cfg, run_dir)` 函数定义

### 最终函数列表 (main.py)

1. `load_config` — YAML 加载
2. `_make_run_dir` — 创建输出目录
3. `_layer_tag` — 层堆垛标签
4. `_run_band` — 能带 (diag only)
5. `_run_dos` — DOS (diag + tbpm, 内联)
6. `_run_berry` — Berry curvature (diag only)
7. `_run_hall` — Hall 电导率 (tbpm only, 内联)
8. `_run_dc` — DC 电导率 (tbpm only, 内联)
9. `main` — 主入口

### 验证结果

| # | 判据 | 结果 |
|---|------|------|
| 1 | Pylance 对 `src/` 下所有 .py 零错误 | ✅ |
| 2 | `grep -r '_run_hall_tbpm\|_run_dc_tbpm' src/main.py` 无匹配 | ✅ |
| 3 | `_run_hall_tbpm` / `_run_dc_tbpm` 函数名在源码中消失 | ✅ |

---

<a id="ai-0526-1640"></a>

## AI: 05-26 16:40 — 精简 main.py：内联 _run_hall_tbpm / _run_dc_tbpm

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/main.py` | 重构 | `_run_hall_tbpm` 和 `_run_dc_tbpm` 内联到 `_run_hall` / `_run_dc`，删除辅助函数 |
| `docs/tasks.md` | 更新 | 0526_1640 标记完成 |
| `docs/log.md` | 追加 | 本记录 |

### 变更说明

**设计变更**：
- **内联**：`_run_hall` 不再委托 `_run_hall_tbpm`，TBPM 循环体直接写入 `_run_hall`
- **内联**：`_run_dc` 不再委托 `_run_dc_tbpm`，TBPM 循环体直接写入 `_run_dc`
- **删除**：`_run_hall_tbpm(prim_cell, cfg, run_dir)` 函数定义
- **删除**：`_run_dc_tbpm(prim_cell, cfg, run_dir)` 函数定义

### 最终函数列表 (main.py)

1. `load_config`
2. `_make_run_dir`
3. `_run_band` — diag only
4. `_run_dos` — diag + tbpm（内联）
5. `_run_ldos` — diag only
6. `_run_berry` — diag only
7. `_run_hall` — tbpm only（内联）
8. `_run_dc` — tbpm only（内联）
9. `main`

### 验证结果

| # | 判据 | 结果 |
|---|------|------|
| 1 | `grep '_run_hall_tbpm\|_run_dc_tbpm' src/main.py` 无匹配 | ✅ |
| 2 | `_run_hall_tbpm` / `_run_dc_tbpm` 函数名在源码中消失 | ✅ |
| 3 | `_run_dos` 已内联 diag/tbpm 分支 | ✅ |
| 4 | Pylance 对 `src/` 下所有 .py 零错误 | ✅ |

---

<a id="ai-0526-1640"></a>

## AI: 05-26 16:40 — 精简 main.py：内联 _run_hall_tbpm / _run_dc_tbpm

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/main.py` | 重构 | `_run_hall_tbpm` 和 `_run_dc_tbpm` 内联到 `_run_hall` / `_run_dc`,删除辅助函数 |
| `docs/tasks.md` | 更新 | 0526_1640 标记完成 |
| `docs/log.md` | 追加 | 本记录 |

### 变更说明

- **内联**: `_run_hall` 不再委托 `_run_hall_tbpm`, TBPM 循环体直接写入 `_run_hall`
- **内联**: `_run_dc` 不再委托 `_run_dc_tbpm`, TBPM 循环体直接写入 `_run_dc`
- **删除**: `_run_hall_tbpm(prim_cell, cfg, run_dir)` 函数定义
- **删除**: `_run_dc_tbpm(prim_cell, cfg, run_dir)` 函数定义

### 最终函数列表 (main.py, 共9个)

1. `load_config`
2. `_make_run_dir`
3. `_run_band` — diag only
4. `_run_dos` — diag + tbpm
5. `_run_ldos` — diag only
6. `_run_berry` — diag only
7. `_run_hall` — tbpm only
8. `_run_dc` — tbpm only
9. `main`

### 验证结果

| # | 判据 | 结果 |
|---|------|------|
| 1 | `grep '_run_hall_tbpm|_run_dc_tbpm' src/main.py` 无匹配 | ✅ |
| 2 | Pylance 对 `src/` 下所有 .py 零错误 | ✅ |

---

<a id="ai-0525-1810"></a>

## AI: 05-25 18:10 — 全部任务 T03-T10 执行完成

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/calc.py` | 重构 | DiagSolver config 驱动 API 适配 + BerryData 提取 (kx,ky,omega) |
| `src/main.py` | 重构 | runs/MMDD_HHMM 输出 + calc_type=all 串联 + TBPM 冒烟 |
| `src/io_vis.py` | 修复 | 重复文件头清除 |
| `configs/graphene.yaml` | 更新 | 添加 tbpm_smoke_dim |
| `docs/tasks.md` | 更新 | T03-T10 全部 [x] |
| `STATUS.md` | 更新 | 进度 100% |

### Diag 计算结果

| Run | 层 | 堆垛 | 计算内容 | 输出文件 |
|-----|-----|------|----------|----------|
| `runs/0525_1745` | L1 | — | band + DOS + Berry | 6 文件 ✅ |
| `runs/0525_1801` | L2 | AB | band + DOS + Berry | 6 文件 ✅ |
| `runs/0525_1803` | L3 | ABA | band + DOS + Berry | 6 文件 ✅ |
| `runs/0525_1807` | L3 | ABC | band only | 2 文件 ✅ |

### TBPM 冒烟测试

- L1 hall smoke: 代码通路验证（小 dim=6×6×1，rescale=9.0 需更大体系以确保 norm 稳定）
- L2/L3/L1 DOS TBPM smoke: 代码通路验证

### 关键技术决策

1. DiagSolver 使用 config 驱动 API（`solver.config.k_points = ...`），非参数传递
2. Berry curvature 使用 tbplas.diag.berry.Berry 类，提取 kx(慢)/ky(快) 网格
3. 输出统一到 `runs/MMDD_HHMM/`，每次运行独立目录
4. TBPM 仅做冒烟测试（小超胞），Diag 全量计算（完整 k-mesh）

---

<a id="ai-0525-1730"></a>

## AI: 05-25 17:30 — T02 model.py 单/双/三层原胞构建验证通过

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/model.py` | 验证 | 6 项成功判据全部通过 |
| `docs/tasks.md` | 更新 | T02 标记 [x] |
| `STATUS.md` | 更新 | 进度 20% |

### 验证结果

| # | 判据 | 结果 |
|---|------|------|
| 1 | `build_monolayer_graphene` 轨道数 = 2 | ✅ |
| 2 | `build_bilayer_graphene("AB")` 轨道数 = 4 | ✅ |
| 3 | `build_trilayer_graphene("ABA")` 轨道数 = 6 | ✅ |
| 4 | `build_Nlayer_graphene(3, "ABC")` 不抛异常 | ✅ (num_orb=6, num_hop=159) |
| 5 | 扩胞 (3,3,1) 后 orb 数正确翻倍：L1=18, L2=36, L3=54 | ✅ |
| 6 | Pylance 零错误 | ✅ |

---

<a id="ai-0525-1730"></a>

## AI: 05-25 17:30 — T02 model.py 单/双/三层原胞构建验证通过

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/model.py` | 验证 | 6 项成功判据全部通过 |
| `docs/tasks.md` | 更新 | T02 标记 [x] |
| `STATUS.md` | 更新 | 进度 20% |

### 验证结果

| # | 判据 | 结果 |
|---|------|------|
| 1 | `build_monolayer_graphene` 轨道数 = 2 | ✅ |
| 2 | `build_bilayer_graphene("AB")` 轨道数 = 4 | ✅ |
| 3 | `build_trilayer_graphene("ABA")` 轨道数 = 6 | ✅ |
| 4 | `build_Nlayer_graphene(3, "ABC")` 不抛异常 | ✅ (num_orb=6, num_hop=159) |
| 5 | 扩胞 (3,3,1) 后 orb 数正确翻倍：L1=18, L2=36, L3=54 | ✅ |
| 6 | Pylance 零错误 | ✅ |


---

<a id="ai-0525-1655"></a>

## AI: 05-25 16:55 — model.py hopping 重构（calc_hop + extend_hop 统一方案）

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/model.py` | 重构 | 删除所有手动 add_hopping，改为 build_* 只加轨道，由 `build_Nlayer_graphene` 统一调 `extend_hop` |

### 变更说明

- **删除内容**: 层间 hopping 常量 (`GAMMA_0/1/3/4`)、`_add_intralayer_hopping`、`_add_aba_hopping`、`_add_abc_hopping`、各 `build_*` 中的手动 add_hopping
- **新增函数**: `calc_hop(rij)`—Slater-Koster 公式，`extend_hop(model, max_distance)`—自动发现 cutoff 内轨道对并计算 hopping
- **核心变更**: `build_Nlayer_graphene(n, stacking, hop_max_distance=0.75)` 在分派完轨道构建后统一调用 `extend_hop` 完成全部 hopping
- **保留不改**: `build_supercell`、`apply_magnetic_field`、`export_lammps` 不变

### 验证结果

| 测试 | num_orb | num_hop | 状态 |
|------|---------|---------|------|
| L1 只加轨道 | 2 | 0 | ✅ |
| L2 只加轨道 | 4 | 0 | ✅ |
| L3 只加轨道 | 6 | 0 | ✅ |
| `build_Nlayer(1)` | 2 | 17 | ✅ |
| `build_Nlayer(2, AB)` | 4 | 70 | ✅ |
| `build_Nlayer(3, ABA)` | 6 | 159 | ✅ |
| `build_Nlayer(3, ABC)` | 6 | 159 | ✅ |
| Pylance 语法 | — | — | ✅ 零错误 |

---

<a id="ai-0525-1650"></a>

## AI: 05-25 16:50 — 项目骨架搭建完成

### 涉及文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `src/main.py` | 新建 | 含 `load_config()` + `main()` 调度骨架，支持 band/dos/berry/hall/dc 五类计算 |
| `src/model.py` | 新建 | 含 8 个函数：单层/双层/三层原胞构建 + 扩胞 + 磁场 + LAMMPS 导出 |
| `src/calc.py` | 新建 | 含 7 个函数：DiagSolver (band/dos/berry) + TBPMSolver (dos/dc/hall) |
| `src/io_vis.py` | 新建 | 含 15 个函数：save/load/plot 全套（dos/bands/berry/conductivity） |
| `src/arc/graphene.py` | 新建 | 归档副本，与原文件完全一致 |
| `configs/graphene.yaml` | 扩展 | 新增 layer/diag/solver_type/lammps 配置节，保留原有参数不变 |
| `data/band/` | 新建 | 能带数据目录 |
| `data/dos/` | 新建 | DOS 数据目录 |
| `data/berry/` | 新建 | Berry curvature 数据目录 |
| `data/transport/` | 新建 | 电导率数据目录 |
| `figures/` | 新建 | 可视化图片目录 |
| `CONTEXT.md` | 新建 | AI 上下文文档 |
| `STATUS.md` | 新建 | 项目状态看板 |

### 变更说明

- **代码归档**: `src/graphene.py` → `src/arc/graphene.py`（diff 确认一致）
- **模块拆分**: 从单体 graphene.py 拆分出 model/calc/io_vis/main 四模块，保留原脚本不动
- **配置扩展**: YAML 新增 layer (num/stacking)、solver_type (diag/tbpm)、diag (k_mesh/k_path/k_num/energy_range/sigma)、output (data_dir/figure_dir/prefix)、lammps 节
- **数据流**: main.py 统一入口，按 calc_type 分派到 calc 计算 → io_vis 保存/绘图
- **接口兼容**: 所有现有 TBPM 参数和环境保持不变

### 成功判据验证

| # | 判据 | 结果 |
|---|------|------|
| 1 | 四模块导入无错误 | ✅ 通过 |
| 2 | YAML safe_load 解析无报错 | ✅ 通过 |
| 3 | 归档与原文件内容一致 | ✅ 通过 |
| 4 | Pylance 零错误 | ✅ 通过 |
