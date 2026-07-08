<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-24 13:24:41
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-25 01:50:00
 * @FilePath     : /.agents/home/wyl/project/MG/docs/sigma/plan_vbl_trace.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-24 02:30:00
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-24 02:30:00
 * @FilePath     : /MG/docs/sigma/plan_vbl_trace.md
 * @Description  : Kubo-Bastin 基线偏移 — 系统变量追踪调试计划 (Variable Baseline Localization)
-->

# Kubo-Bastin 基线偏移 — 系统变量追踪计划 (VBL)

> **状态**: 🟢 Phase A–L 全部完成 — 全 9 假说已排除, 根因确认为条件收敛+浮点精度
> **父计划**: `plan_baseline_root_cause.md`（H_A/H_B/H_C 已排除，剩余 H_D 待测）
> **配套任务**: `task_vbl_trace.md` ✅ (2026-06-24 已创建, Phase L 完成)
> **实际执行路径**: AI:0624_1430 (A1-A6) → ... → AI:0625_0744 (Phase J1: H_J 排除) → AI:0625_0818 (Phase K: μ/Γ 均 M 无关) → AI:0625_0838 (Phase L: δμ 随机噪声, Krylov 漂移排除)
> **最后修订**: 2026-06-25 — Phase L 完成: δμ 随机噪声, 振荡对消有效, 条件收敛+浮点精度为最终根因

> **定位**: 在 E1–E3 三个互斥假说全部排除后，切换策略——从"猜假说再验证"转为"逐级追踪数值链路，定位误差首次出现的位置"。本文档规划如何通过在关键节点插桩、保存中间量、离线对比分析，找到基线偏移 S 的**数值源头**。

> **源码基准**: `/home/wyl/tbplas/source/tbplas-cpp-a021ca8/sources/tbpm/`
> **关键文件**: `kubo_bastin.h`（`kbdc_mu_raw` + `cond_from_trace` + `gamma_matrix`）
> **项目路径**: `/home/wyl/project/MG/`
> **环境**: `conda activate tbplas-alpha` + `export TBPLAS_CORE_PATH=...`

---

## 0. 实际执行路径与发现 (2026-06-24)

### Phase A — μ 矩阵正常 ✅

| 任务 | 关键发现 |
|------|---------|
| A1-A2 | M=2048/4096 μ 矩阵生成 (65MB/257MB HDF5, Jobs 286020-286021) |
| A3 | Hermiticity 偏差同级 (mean≈1.2e-3), M4096/M2048 比=1.0× → μ 内积精度正常 |
| A4 | 热图显示带状对角结构, M4096 高阶区无异常亮斑 |
| A5 | 重叠区 norm 比≈1.4×, 高 m 区偏离外推仅 1.49× — 无异常退化 |
| A6 | 截断验证: 从 M=4096 μ 截断后 σ_xy 随 M 增大, 与直接计算趋势一致 |

**结论**: μ 矩阵构建精度正常 → 误差在 Γ·μ 累加阶段

### Phase B — Γ·μ 累加确认为根因 ✅

| 任务 | 关键发现 |
|------|---------|
| B1 | C++ VBL_TRACE 插桩 (集群 gcc 13.1.0 编译, ofstream 文件输出 vbl_sum_M*.log) |
| B2 | 5 M 值全部 ExitCode 0, sum(θ) 数据采集完好 |
| B3 | B=0 零场: σ_xy(B=0)=-482 e²/h 破坏时间反演对称性; sum(θ) B100 vs B0 恒等 (diff=0) |
| B4 | sum(θ) 曲线形状自相似, 幅值随 M 系统性放大 |
| B5 | **∫sum 从 -0.27(M2048)→+484.5(M4096), ~1800× 发散** — 不收敛! |

**结论**: Γ·μ 累加中浮点误差与 M 系统性相关, 是基线偏移的直接驱动

### 技术里程碑

| 里程碑 | 详情 |
|------|------|
| 诊断库编译 | 集群编译 (gcc 13.1.0, GLIBC 2.2.5), 文件输出 vbl_sum_M*.log |
| Job 时间 | M2048: 7:21, M2560: 11:07, M3072: 15:28, M3584: 20:36, M4096: 26:32, B0: 26:34 |
| B0 验证 | σ_xy(B=0) = -482 e²/h (应=0), 时间反演对称性破坏 |
| sum(θ) 恒等 | B100T 和 B0 的 sum(θ) 完全相同 (diff=0), 说明 sum(θ) 本身与 B 场无关 |

### Phase C — Kahan 未根除 (AI:0624_1745)
- C1: 行级 Kahan + OpenMP reduction 编译成功
- C2: M=2048/2560 Kahan 稳定 (σ≈10), M≥3072 偏移复现
- C3: M=4096 Kahan σ=2945 > Standard σ=1060
- **结论**: H_D (浮点累加精度) 证伪

### Phase D — 分块无异常 (AI:0624_1900)
- D1-D3: 256×256 分块, 低阶 69.3%, 高阶仅 2.6%, 无单一块主导
- **结论**: 偏移全域均匀, 非特定 (m,n) 区域发源

### Phase E — 综合判定
| 假说 | 测试 | 结论 |
|------|------|:---:|
| H_A (Chebyshev 范数) | E1 | ❌ |
| H_B (Jackson 核) | E2 | ❌ |
| H_C (谱边缘泄漏) | E3 | ❌ |
| H_D (双精度不足) | VBL Phase C | ❌ (Kahan 未根除) |
| H_D (双精度不足) | VBL Phase I (long double) | ❌ (S_ld=+1060, 仅降 ~3×) |
| H_μ (μ 矩阵异常) | VBL Phase A | ❌ |
| H_block (分块噪声) | VBL Phase D | ❌ |
| H_Γ (Γ·μ 累加) | VBL Phase B | ⚠️ 直接驱动 |

**根因**: Γ·μ 累加中系统性全域浮点误差, 被 θ 积分奇点 (1/sin³θ) 放大
**安全窗口**: M ≤ 2560 (Kahan 可稳定 M=2048/2560)

### Phase F — θ 积分奇点诊断 ✅ H_θ 排除 (AI:0625_0150)

> **结论**: H_θ 被排除。θ 积分方案（点数 N_θ、端点截断 δ、Simpson vs 梯形）对基线偏移 S 无任何影响。N_θ≥1024 后 S 收敛到 +600.1 且稳定不变。

**关键数据** (M=4096, m=64, rs=1):

| 实验 | 变体 | σ(0) [e²/h] |
|:---:|------|:---:|
| F1 N_θ=256 | — | −64562 (网格过粗) |
| F1 N_θ=512 | — | +31580 (网格过粗) |
| F1 N_θ=1024 | — | +600.1 |
| F1 N_θ=2048 | — | +600.1 |
| F2 δ=0.01π–0.10π | θ 截断 | 全部 +600.1 |
| F3 trapez/simpson | 积分规则 | 全部 +600.1 |

**推论**: 基线偏移来自 θ 积分之前的 sum(θ) = Σ Γ⊙μ。根因搜索收缩到 **Γ 矩阵构造精度 (Phase G)** 或 **Γ⊙μ 累加**。

#### 假设: H_θ — θ 积分奇点放大大规模累加误差

**机制**: Kubo-Bastin θ 积分使用均匀网格梯形积分:

$$\sigma(E) \propto \int_0^\pi d\theta \cdot \frac{sum(\theta) \cdot f(E,\cos\theta)}{\sin^3\theta}$$

在 θ→0 和 θ→π 处，$\sin^3\theta \to 0$，权重 $1/\sin^3\theta \to \infty$。虽然分子 $sum(\theta)$ 在端点处也趋于零（由 Chebyshev 多项式有界性保证），但数值上 $sum(\theta)$ 在端点附近可能残留微小的浮点舍入噪声。这些噪声被 $1/\sin^3\theta$ 放大 $10^3$–$10^6$ 倍，贡献到最终积分。

**预测** (如果 H_θ 为真):
1. 增大 `dckb_num_integ_steps` 会使 |S| 增大（更多近奇点被采样）— 与观测一致：2048 θ 点下 S 已很大
2. 正则化端点（clamp 或 cut θ∈[δ, π-δ]）会使 |S| 大幅减小
3. 改用非均匀 θ 网格（Gauss-Legendre 或其他避开端点的方案）会减少 S

#### 判别实验设计

| 编号 | 实验 | 参数 | M | 预测 | 优先级 |
|:---:|------|------|:---:|------|:---:|
| **F1** | θ 点数扫描 | dckb_num_integ_steps ∈ {256, 512, 1024, 2048} | 4096 | S 随 N_θ 增大而增大 | 🔴 高 |
| **F2** | θ 端点截断 | 修改 C++ 源码: clamp θ∈[δ, π-δ] (δ=0.01π, 0.05π) | 4096 | S 随 δ 增大而减小 | 🔴 高 |
| **F3** | 梯形 vs 高阶积分 | 对比梯形积分 vs Simpson 规则 | 4096 | Simpson 减小 S | 🟡 中 |

#### 预期结果与分叉

```
F1: S(N_θ) 单调增长?
  ├── YES → H_θ 强烈支持 (奇点效应确认)
  │     └── F2: δ 增大→S 减小? → 确认 → 修复: 正则化 θ 积分
  │
  └── NO → H_θ 被排除
        └── 根因在 prefactor 或更深层 → 重新审查
```

#### C++ 修改计划

在 `cond_from_trace()` 的 θ 积分循环中，将:
```cpp
eng_re = std::cos(theta_array[k]);
div = std::pow(std::sin(theta_array[k]), 3.0);
```
修改为 (F2 端点截断):
```cpp
double theta_k = theta_array[k];
double sin_theta = std::sin(theta_k);
if (sin_theta < delta_cut) sin_theta = delta_cut;  // 或 skip
double div = sin_theta * sin_theta * sin_theta;
eng_re = std::cos(theta_k);
```

#### 估计资源
| 实验 | Jobs | 时间/Job | 总时间 |
|:---:|:---:|:---:|:---:|
| F1 | 4 | ~26 min (M=4096) | ~2h (4 Job 并行) |
| F2 | 8 (4 δ × 2 M) | ~26 min | ~1h (8 Job 并行) |
| F3 | 2 (trapez + simpson) | ~26 min | ~30min (2 Job 并行) |

---

### Phase G — Γ 矩阵精度诊断 (H_Γ) 🔲 🆕

> **新增**: 2026-06-24 — 发现 Gamma 矩阵元素量级 $|\Gamma_{mn}| \sim O(\max(m,n))$，与 μ 矩阵（Jackson 核压制高阶）混合产生 4 个数量级的动态范围。此假说此前未被独立检验。

#### 假设: H_Γ — Gamma 矩阵构造精度是大 M 时的限制因素

**理论分析**: 对角元可简化为:
$$\Gamma_{nn}(\theta) = 2\cos(n\theta)\bigl(\cos\theta\cos n\theta + n\sin\theta\sin n\theta\bigr)$$
当 $\theta \approx \pi/2$ 时 $|\Gamma_{nn}| \approx n|\sin(2n\theta)| \sim O(n)$。在 M=4096 下：
- 低阶区 (m,n < 512): $|\Gamma| \sim O(1)$
- 高阶区 (m,n ~ 4096): $|\Gamma| \sim O(10^3)$
- 极值可达 $|\Gamma_{M,M}| \sim 2M \approx 8192$

**问题**: Γ 矩阵含 $\cos(m\theta)$、$n\sin\theta e^{in\theta}$ 等振荡因子，在 double 精度下对大 m,n 的计算可能损失有效位数。叠加 $\mu_{mn}$ 的 Jackson 核衰减（高阶 μ 为小数的 $O(10^{-4})$），形成 **大数×小数 + 小数×大数** 的混合精度灾难。

**与 H_D 区别**: H_D 是"累加误差"（Kahan 已排除），H_Γ 是"**被累加项本身的构造精度**"——在进入累加循环之前，$\Gamma_{mn} \cdot \mu_{mn}$ 可能已经错了。

#### 判别实验设计

| 编号 | 实验 | 参数 | 预测 | 优先级 |
|:---:|------|------|------|:---:|
| **G1** | Γ 量级分布 | 输出 $\log_{10}\|\Gamma_{mn}\|$ 对 2-3 个 θ 值 | 高阶区 O(M)，低阶区 O(1) | 🔴 高 |
| **G2** | Γ Hermiticity | 检验 $\|\Gamma_{mn} - \Gamma_{nm}^*\|$ | 理论严格成立，偏差反映构造精度 | 🔴 高 |
| **G3** | Γ 范数 vs M | M ∈ {512,1024,2048,4096}，固定 θ=π/4 | O(M) 增长应精确跟踪理论公式 | 🟡 中 |

#### 预期结果与分叉

```
G1: |Γ| 分布符合 O(max(m,n))?
  ├── YES → H_Γ 构造正常
  │     └── 误差在"混叠"阶段 → 需要将 Γ 和 μ 分开分析 (G3)
  │
  └── NO → H_Γ 被确认
        └── 高阶 Γ 元素构造精度不足 → 修复 gamma_matrix() 数值稳定性

G2: Hermiticity 偏差在高阶区放大?
  ├── YES → cos/sin 大角度精度问题 → 需改进 gamma_matrix()
  └── NO → Gamma 构造基本健康
```

#### C++ 修改

在 `cond_from_trace()` 的 `#ifdef TBPLAS_VBL_TRACE` 块中追加:

```cpp
#ifdef TBPLAS_GAMMA_DIAG
// G1: Gamma magnitude heatmap (first 3 θ points)
if (k < 3) {
    std::ofstream gf("gamma_M" + std::to_string(num_kernel) + "_theta" + std::to_string(k) + ".log");
    for (int jj = 0; jj < num_kernel; ++jj) {
        for (int ii = 0; ii < num_kernel; ++ii)
            gf << std::abs(gamma(ii, jj)) << (ii+1<num_kernel?" ":"");
        gf << "\n";
    }
}
// G2: Hermiticity check
double herm_max = 0.0, herm_sum = 0.0;
for (int jj = 0; jj < num_kernel; ++jj)
    for (int ii = 0; ii < num_kernel; ++ii) {
        double d = std::abs(gamma(ii, jj) - std::conj(gamma(jj, ii)));
        if (d > herm_max) herm_max = d;
        herm_sum += d;
    }
std::ofstream gh("gamma_herm_M" + std::to_string(num_kernel) + ".log", std::ios::app);
gh << "theta=" << theta_array[k] << " herm_max=" << herm_max
   << " herm_mean=" << herm_sum/(num_kernel*num_kernel) << std::endl;
#endif
```

#### 估计资源

| 实验 | Jobs | 时间/Job | 总时间 |
|:---:|:---:|:---:|:---:|
| G1/G2 | 1 (M=4096, 3 θ 点, rs=1) | ~26 min | ~30min (含队列) |
| G3 | 4 (M=512,1024,2048,4096) | 2-26 min | ~30min (4 Job 并行) |

#### 与 Phase F 的并发可行性 ✅

Phase G 与 Phase F **可完全同步运行**，无资源冲突：

| 维度 | Phase F | Phase G | 冲突? |
|------|---------|---------|:---:|
| 编译标志 | `TBPLAS_THETA_CUT` / `TBPLAS_SIMPSON` | `TBPLAS_GAMMA_DIAG` (+`TBPLAS_VBL_TRACE`) | ❌ 不同库 |
| 集群节点 | 4 节点/Job | 4 节点/Job | ❌ 独立作业 |
| YAML 配置 | `hall_m64_M4096_vbl_f1/f2/f3_*.yaml` | `hall_m64_M*_vbl_gamma.yaml` | ❌ 不同文件 |
| C++ kubo_bastin.h | 仅在 θ 积分循环（末段） | 在 Γ·μ 求和循环（中段） | ❌ 不同代码块 |
| 数据输出 | `vbl_sum_M*.log` / `hall_*.txt` | `gamma_M*_theta*.log` / `gamma_herm_*.log` | ❌ 不同文件 |

**推荐**: 立即启动 Phase G 编译 + 提交，与 Phase F 并行等待。

---

### Phase I — long double H_D 封闭实验 ✅ H_D 排除 (AI:0625_0630)

> **结论**: H_D (double 精度不足) 被排除。80-bit long double 仅降低偏移 ~3× (S_ld(4096)=+1060 vs S_dbl=+2945)，偏移仍随 M 增长，未根除。

**关键数据** (M=64, rs=1, N_θ=2048):

| M | double (Phase B) | long double | 比值 |
|---|:---:|:---:|:---:|
| 2048 | +10.1 | −5.9 | — |
| 2560 | +10.1 | −3.9 | — |
| 3072 | +150.9 | +44.7 | 30% |
| 3584 | +950.4 | +320.8 | 34% |
| 4096 | +2945.2 | +1060.1 | 36% |

**实现细节**:
- `cond_from_trace()` 中累加变量 `sum`, `dcx`, `sum_gamma_mu`, `theta_array` → `long double`
- `#ifdef TBPLAS_LONG_DOUBLE` 条件编译, 默认 OFF
- 集群 .so 含 38 条 x87 80-bit 指令 (原始: 0)
- Bug 修复: (1) prefix 冲突 → `solver.config.prefix` 用 tag 设唯一值; (2) 缺 mpirun → 添加 `$MPI_PATH/bin/mpirun`

**推论**: 全部 7 假说已排除 (H_A–H_θ)。根因可能在更深层：prefactor 缩放错误 或 `complex<double>` 乘法精度不足。

---

### Phase H — Anderson 无序根因验证 🆕 (2026-06-25)

> **背景**: Phase A–G 全部完成后定位根因: **KPM + δ-函数谱 → μ 不衰减 → S(θ) 正负对消脆弱 → 基线偏移**。预测: 加 Anderson 无序使谱连续 → 偏移消失。

#### 目标

在**完全干净的 C++ 核心**（源码回退 + 集群库重编译安装，移除所有 Phase B–G 诊断插桩及变体安装目录，仅保留 μ save/load）上，通过 Python 官方 API 添加 Anderson 无序，验证基线偏移消失。

#### 步骤

| 编号 | 操作 | C++ 改动 | 位置 |
|:---:|------|:---:|------|
| H1 | C++ 源码 + **集群安装** 回退到原始版本 (git checkout + 重编译安装) | ✅ 恢复源码 | 本地 + 集群 |
| H2 | `src/model.py` 添加 `add_anderson_disorder(sample, gamma, seed)` | ❌ 纯 Python | 本地 |
| H3 | AB 单层 M=4096 有/无无序对比 | ❌ | 集群 |
| H4 | ABC 三层 δ=0/δ≠0 有/无无序对比 | ❌ | 集群 |
| H5 | AB 单层 M 扫描 (2048–4096) 无序下 S(M) | ❌ | 集群 |

#### 判别

```
H3: AB M=4096 无序 → σ_xy ≈ +2 e²/h (偏移消失)?
  ├── YES → 根因确认 ✅
  │     └── H4: ABC 符号反转也消失? → 双重确认
  └── NO → 重新考虑根因
```

#### 参考

- García 2015 PRL 114.116602: γ=0.1t, M=6144 无偏移
- Python API: `sample.get_array().orb_eng[i] += disorder`
- 前置: Phase B sum(θ) 分析 + ABC 符号反转 + Phase G Γ 确认



---

### Phase J — Jackson 核 M 依赖性修复 ✅ 已完成, H_J 排除 (2026-06-25)

> **⚠️ 本段假说已被证伪 (2026-06-25)。**
> 证伪实验: J1 统一核截断验证 → S(M) range=309 (统一核) ≈ 320 (标准核)
> 详细: [log AI:0625_0744]
> 以下为历史存档。

> **背景**: 发现 M=4096 的 sum(θ) 在 θ~[0.5, 2.6] 范围内整体偏移，远离端点奇点区。根因收敛到 **Jackson 核的 M 依赖性**——同一 n 在不同 M 下权重不同：$g_n^{(4096)} > g_n^{(2048)}$ for all $n<2048$，导致已有低阶 μ 被系统性放大而非新加高阶项贡献。

#### 假说: H_J — Jackson 核的 M 依赖性导致基线偏移 ❌ 已排除

$$\mu_{mn}^{(M)} = g_m^{(M)} g_n^{(M)} \mu_{mn}^{\text{raw}}$$

对于固定的 $m,n<2048$，$g_n^{(4096)} > g_n^{(2048)}$，因此 $\mu_{mn}^{(4096)} > \mu_{mn}^{(2048)}$，即使 raw μ 完全相同。这解释了 Phase D（分块无异常聚集）和 sum(θ) 整体偏移。

#### 目标

通过 **统一核函数** 消除 M 依赖性，验证基线偏移是否消失。

#### 两种方案

| 方案 | 方法 | 改动 | 风险 |
|------|------|:---:|:---:|
| **J1 (优先)** | 计算一次 μ_raw @ M_max=4096，对每个目标 M' 截断后应用 $g_n^{(M_{\text{max}})}$（统一核） | 仅 Python 脚本 | 🟢 极低 |
| J2 (备选) | 修改 C++ `jackson_kernel()` 为 Lorentz 核 | ~5 行 C++ | 🟡 低 |

**J1 可直接用已有数据**：Phase A 已有 `mu_raw_M4096_m64.h5`，Python 端做截断 + 统一核加权 + re-积分。

#### 判别逻辑

```
J1: M=4096 raw μ, 对 M'=2048/2560/3072/4096 统一用 g^(4096) 核 → S(M') 平坦?
  ├── YES (S≈0 for all M') → 根因确认 ✅ — Jackson 核 M 依赖性
  │     └── J2: Lorentz 核作为永久修复
  └── NO (S 仍随 M 增长) → H_J 排除，根因在其他环节
```

#### 参考

- Jackson 核公式: $g_n^{(M)} = \frac{(M-n+1)\cos\frac{\pi n}{M+1} + \cot\frac{\pi}{M+1}\sin\frac{\pi n}{M+1}}{M+1}$
- Lorentz 核: $g_n = \sinh(\lambda(1-n/M))/\sinh\lambda$（M 无关标度）
- 已有资源: `mu_raw_M4096_m64.h5` (Phase A), `dckb_load_mu_file` + `truncate_mu` (原始功能)


### Phase K — Γ vs μ 变量分离 ✅ 完成 (AI:0625_0818)

> **发现**: μ 和 Γ 各自均无 M 依赖, 但 Jackson 核放大 7.2× 是 sum 膨胀主因
> 详细: [log AI:0625_0818]
> 任务: `task_vbl_trace.md` §Phase K

| 测试 | 结果 | 判定 |
|------|------|:----:|
| K1 μ M 依赖 | sum_A == sum_B (diff ~ 1e-14 relative) | ✅ μ 无 M 依赖 |
| K2 新区/旧区 | 旧区 68% + 新区 32%, 核放大 7.2× | ✅ 旧区主导 |
| K3 Γ M 依赖 | sum_C2 == sum_D2 (diff=0, 数学恒等) | ✅ Γ 无 M 依赖 |

**关键洞察**: Jackson 核 g_n^(M) 随 M 增大而放大同一 n 的权重 → sum 膨胀。但 Phase J 用统一核未根除 → 核差异叠加了累加精度问题。


### Phase L — 高阶项符号结构 ✅ 完成 (AI:0625_0838)

> **假说**: δμ 是系统性偏置 (Krylov 方向漂移) or 随机噪声?
> **结论**: δμ 为随机噪声, Krylov 漂移假说排除
> 详细: [log AI:0625_0838]
> 任务: `task_vbl_trace.md` §Phase L

| 测试 | 结果 | 判定 |
|------|------|:----:|
| L1 μ 符号偏置 | pos_frac=0.4997, 8 blocks <0.001 偏离 | ✅ 随机噪声 |
| L2 新区对消率 | mean R=0.008 (old=new) | ✅ 振荡对消有效 |
| L3 异常行 | 30 top rows, 0 common across θ | ✅ 孤立尖峰 |

**最终根因画像**: 条件收敛 — Γ~O(n) 增长 + μ 衰减不足 → 绝对和不收敛 → 随机游走累积 ~O(√N·ε) 在 N~1.7×10⁷ 下不可忽略。

**全部 9 假说状态**: H_A❌ H_B❌ H_C❌ H_D❌ H_μ❌ H_Γ❌ H_θ❌ H_J❌ H_bias❌

**建议修复方向**:
1. quad precision (__float128) 关键路径
2. pairwise/tree summation 替代顺序累加
3. 核函数优化 (Lorentz λ>4) 使 μ 更快衰减
4. 实用窗口: M≤2560 + Kahan 编译



---

## 1. 项目概述与物理目标

### 1.1 问题现状

Kubo-Bastin Hall 电导率 $\sigma_{xy}(E)$ 在 $M \gtrsim 2560$ 时出现**相干基线偏移** $S$：

| 特征 | 量值 |
|------|------|
| 偏移形态 | 全能量范围恒加负偏移 |
| 起始阈值 | $M_c \approx 2560$（与超胞尺寸 m 无关）|
| M=4096 时 S | ≈ −991 e²/h |
| 偏移确定性 | 与 rs 无关（非随机迹估计误差）|

**已完成诊断**（`plan_baseline_root_cause.md`）：
- ❌ H_A (Chebyshev 范数膨胀) — E1 证伪：$\|T_n\| \approx 0.707$ 常数
- ❌ H_B (Jackson 核退化) — E2 排除：核起抑制作用
- ❌ H_C (谱边缘泄漏) — E3 排除：S(rescale) 非单调
- 🔲 H_D (浮点精度不足) — E4 待执行

### 1.2 策略转变：假说驱动 → 数据驱动

前三个阶段（H_A/H_B/H_C）采用"提出假说 → 设计判别实验 → 证伪/确认"的 Popper 式方法。三个假说全部排除后，剩余可测试假说仅 H_D（但 H_D 是模糊的"精度不够"，缺乏具体故障定位）。

**新策略**：不再猜测根因，改为沿数值链路逐级插桩，追踪关键中间变量的数值行为。对比 **M=2048（已知正常，S≈0）** 和 **M=4096（已知异常，S≈−991）** 两组的中间量差异，定位误差**首次出现**的计算环节。

### 1.3 数值链路全景

```
Step 0: 随机态 |ψ₀⟩
  │
Step 1: Chebyshev 三项递推 → {T_n(H)|ψ₀⟩}     (✅ E1 已验证稳定性)
  │
Step 2: 内积构建 μ_{mn} = ⟨T_m v_α ψ₀ | v_β T_n ψ₀⟩   ← 🔍 一级怀疑
  │
Step 3: Jackson 核加权 μ'_{mn} = g_m g_n · μ_{mn}        (✅ E2 已验证功能正常)
  │
Step 4: Γ 矩阵求和: sum(θ) = Σ_{m,n} Re[Γ_{mn}(θ)·μ'_{mn}]  ← 🔍 二级怀疑
  │
Step 5: θ 积分: cond[E] = ∫ dθ · sum(θ) · f(E) / sin³θ    ← 🔍 三级怀疑
  │
Step 6: × prefactor → σ_{xy}(E)
```

**核心思路**：每一步都可能引入误差。通过保存每一步的中间量，对照正常组（M=2048）和异常组（M=4096），找到误差放大的环节。

---

## 2. 计算步骤方案

### 阶段流程

```
Phase A: 离线 μ 矩阵诊断（不改 C++ 代码）
  利用已有 dckb_save_mu_file / dckb_load_mu_file 功能
  → 保存 M=2048 和 M=4096 的 raw μ 矩阵
  → Python 离线分析 μ 矩阵结构和 Hermiticity
  → 判定：误差是否在 μ 矩阵层面已出现？

Phase B: sum_gamma_mu(θ) 插桩诊断（C++ 插桩）
  在 cond_from_trace() 中输出 sum_gamma_mu(θ) 序列
  → 对比 M=2048 vs M=4096 的 sum(θ) 曲线
  → 判定：误差是否在 Γ·μ 累加阶段被放大？

Phase C: 累加精度诊断（Kahan 补偿求和）
  在 Γ·μ 和 θ 积分两处改用 Kahan 补偿求和
  → 对比标准累加 vs Kahan 累加
  → 判定：大规模浮点累加是否是根因？

Phase D: 逐项贡献分解
  对每个 (m,n) 项分解其贡献
  → 判定：偏移主要来自哪些 (m,n) 区域？

Phase E: 综合判定与修复
  汇总 A–D 结果，确定根因和修复方案
```

### 阶段依赖关系

```
Phase A (离线 μ 分析) ─── 独立可执行
  │
  ├── μ 矩阵正常? ──→ Phase B (sum 插桩)
  │                     │
  │                     ├── sum 正常? ──→ Phase C (Kahan 累加)
  │                     │                   │
  │                     │                   └── 正常? → Phase E（更下游的问题）
  │                     │
  │                     └── sum 异常? → Phase D (逐项分解)
  │
  └── μ 矩阵异常? ──→ Phase D (逐项分解 μ 矩阵)
                        │
                        └── Phase E（修复 μ 构建精度）
```

---

## 3. 系统架构规划

### 3.1 文件修改清单

| 文件 | 修改类型 | 阶段 | 说明 |
|------|:---:|:---:|------|
| `kubo_bastin.h` | 插桩 | B | `cond_from_trace()` 中输出 `sum_gamma_mu[k]` |
| `kubo_bastin.h` | 修改 | C | Γ·μ 累加改用 Kahan 求和 |
| `kubo_bastin.h` | 修改 | C | θ 积分累加改用 Kahan 求和 |
| `kubo_bastin.h` | 插桩 | D | 输出按 (m,n) 块分解的贡献 |
| `test/analyze_mu_matrix.py` | **新建** | A | μ 矩阵 Hermiticity / 量级分布 / 热图 |
| `test/analyze_sum_gamma_mu.py` | **新建** | B | sum(θ) 序列对比与积分分析 |
| `test/analyze_kahan_compare.py` | **新建** | C | 标准 vs Kahan 累加差异分析 |
| `test/analyze_contrib_decomp.py` | **新建** | D | (m,n) 项贡献分解可视化 |
| `configs/hall_m64_M2048_save_mu.yaml` | **新建** | A | M=2048 raw μ 保存配置 |
| `configs/hall_m64_M4096_save_mu.yaml` | **新建** | A | M=4096 raw μ 保存配置 |
| `configs/hall_m64_M*_load_analyze.yaml` | **新建** | A | 加载 μ 并输出 cond（不重新计算 μ） |

### 3.2 模块职责

| 模块 | 职责 |
|------|------|
| **离线 μ 分析** (`test/analyze_mu_matrix.py`) | 加载 HDF5 中的 μ 矩阵，检查 Hermiticity、量级分布、对角/非对角统计，生成热图和诊断报告 |
| **sum(θ) 诊断** (`test/analyze_sum_gamma_mu.py`) | 解析 C++ stdout 中的 `[VBL_SUM]` 行，绘制 sum(θ) 曲线，对比正常/异常组 |
| **Kahan 对比** (`test/analyze_kahan_compare.py`) | 加载标准累加和 Kahan 累加的 cond 结果，量化差异 |
| **贡献分解** (`test/analyze_contrib_decomp.py`) | 加载 μ 矩阵和 Γ 矩阵，按 (m,n) 块分解贡献，绘制贡献热图 |

### 3.3 安全设计

- **Phase A**: 零 C++ 代码修改，仅使用已有的 `dckb_save_mu_file` / `dckb_load_mu_file` 功能 + Python 离线分析
- **Phase B**: 插桩使用 `#ifdef TBPLAS_VBL_TRACE` 条件编译保护，默认关闭
- **Phase C**: Kahan 修改使用 `#ifdef TBPLAS_KAHAN_SUM` 条件编译，默认关闭
- **Phase D**: 同 Phase B，`#ifdef TBPLAS_VBL_TRACE`
- **所有阶段**: 默认编译（无 `-D` flag）回归安全，不影响正常计算

---

## 4. 接口规范（计划）

### 4.1 C++ 诊断输出格式

**Phase B 插桩** — `cond_from_trace()` 中输出 `sum_gamma_mu`：

```cpp
// 在 sum_gamma_mu[k] 计算完成后，theta 积分循环之前:
#ifdef TBPLAS_VBL_TRACE
std::cout << "[VBL_SUM] M=" << num_kernel << " rs=" << num_samples;
for (int k = 0; k < num_theta; ++k) {
    std::cout << " " << theta_array[k] << ":" << sum_gamma_mu[k];
}
std::cout << std::endl;
#endif
```

输出格式：`[VBL_SUM] M=4096 rs=1 θ1:val1 θ2:val2 ...`

**Phase D 插桩** — 分块贡献：

```cpp
#ifdef TBPLAS_VBL_TRACE
// 每 256×256 块输出一次块贡献总和
int block_size = 256;
for (int jb = 0; jb < num_kernel; jb += block_size) {
    for (int ib = 0; ib < num_kernel; ib += block_size) {
        double block_sum = 0.0;
        for (int j = jb; j < std::min(jb+block_size, num_kernel); ++j)
            for (int i = ib; i < std::min(ib+block_size, num_kernel); ++i)
                block_sum += (gamma(i,j) * mu_avg(i,j)).real();
        std::cout << "[VBL_BLOCK] M=" << num_kernel
                  << " θ=" << theta_array[k]
                  << " ib=" << ib << " jb=" << jb
                  << " sum=" << block_sum << std::endl;
    }
}
#endif
```

### 4.2 Python 分析函数

| 函数 | 计划签名 | 功能说明 |
|------|---------|----------|
| `load_mu_matrix` | `(h5_path: str) -> np.ndarray` | 从 HDF5 加载 μ 矩阵 |
| `check_hermiticity` | `(mu: np.ndarray) -> dict` | 检查 $\|\mu_{mn} - \mu_{nm}^*\|$ 分布 |
| `plot_mu_heatmap` | `(mu: np.ndarray, title: str) -> fig` | 绘制 $\|\mu_{mn}\|$ 热图 |
| `extract_mu_diag_stats` | `(mu: np.ndarray) -> dict` | 对角/非对角/边界统计 |
| `compare_mu_matrices` | `(mu2048, mu4096) -> dict` | M=2048 vs 4096 差异分析 |
| `parse_sum_gamma_mu` | `(log_path: str) -> np.ndarray` | 解析 `[VBL_SUM]` 行 |
| `plot_sum_vs_theta` | `(sum_data: dict) -> fig` | 多 M 值 sum(θ) 对比 |
| `kahan_sum_complex` | `(arr: np.ndarray) -> complex` | Python 端 Kahan 补偿求和（参照验证） |
| `decompose_contrib` | `(mu, gamma, block_size) -> np.ndarray` | 分块贡献矩阵 |

---

## 5. 参数设计表

### 5.1 通用固定参数

```yaml
# 所有 VBL 实验共用
model:
  material: "AB"
  m: 64
  delta: 0.0
  B: 100.0
  gauge: "landau_x"

calc:
  method: "kubo_bastin"
  temperature: 10.0        # K
  dckb_unit: "hbar"
  rescale: -1              # 自动带宽检测
```

### 5.2 阶段专用参数

```yaml
# Phase A: μ 矩阵保存 (M=2048 正常组)
dckb_num_kernel: 2048
num_random_samples: 1
dckb_energies: [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5]  # 7 点即可
dckb_num_integ_steps: 2048
dckb_save_mu_file: "runs/0624/mu_raw_M2048_m64.h5"

# Phase A: μ 矩阵保存 (M=4096 异常组)
dckb_num_kernel: 4096
num_random_samples: 1
dckb_energies: [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5]
dckb_num_integ_steps: 2048
dckb_save_mu_file: "runs/0624/mu_raw_M4096_m64.h5"

# Phase A: μ 矩阵加载分析 (离线, 不改 C++ 代码)
dckb_num_kernel: 2048         # 截断到目标 M
dckb_load_mu_file: "runs/0624/mu_raw_M4096_m64.h5"
dckb_energies: <51 点完整能量网格>
dckb_num_integ_steps: 2048

# Phase B: sum(θ) 插桩
dckb_num_kernel: [256, 512, 1024, 2048, 3072, 4096]
num_random_samples: 1
dckb_energies: [-1.5, 0.0, 1.5]  # 3 点即可，减少积分时间
dckb_num_integ_steps: 2048

# Phase C: Kahan 补偿求和
# 同 Phase B 参数, 但需重新编译 C++ 带 -DTBPLAS_KAHAN_SUM
# 对比: 同一 YAML, 标准编译 vs Kahan 编译

# Phase D: 逐项贡献分解
dckb_num_kernel: 4096
num_random_samples: 1
dckb_energies: [0.0]            # 单能量点, E_F=0
dckb_num_integ_steps: 512       # 减少积分点, 仅诊断用
```

### 5.3 关键对比维度

| 对比维度 | 正常组 | 异常组 | 诊断目的 |
|------|:---:|:---:|------|
| **M** | 2048 | 4096 | 主对比——定位首次出现差异的 M |
| **M 渐变** | 2048, 2560, 3072, 3584, 4096 | — | 追踪 S 的增长起点 |
| **rs** | 1 | 1 | 固定 rs=1，排除随机迹估计变数 |
| **m** | 64 | 64 | 固定 m=64，简化变量 |
| **B** | 0 T | 100 T | B=0 零场检验（时间反演对称性要求 σ_xy≡0） |

---

## 6. 文件结构规划

```
MG/docs/sigma/
├── plan.md                              # 父计划（ABC trilayer QHE）
├── plan_baseline_root_cause.md          # H_A/H_B/H_C 假说诊断计划
├── plan_vbl_trace.md                    # ← 本文档
├── task_baseline_root_cause.md          # E1–E5 任务单
├── task_vbl_trace.md                    # VBL 任务单（待创建）
├── archive/                             # 历史文档
│   ├── baseline_shift_plan.md
│   └── ...
│
MG/
├── configs/
│   ├── hall_m64_M2048_save_mu.yaml      # Phase A 正常组
│   ├── hall_m64_M4096_save_mu.yaml      # Phase A 异常组
│   ├── hall_m64_M2048_load.yaml         # Phase A 加载 M=2048
│   ├── hall_m64_M4096_load.yaml         # Phase A 加载 M=4096
│   ├── hall_m64_M*_vbl.yaml             # Phase B sum(θ) 插桩
│   └── hall_m64_M4096_B0_vbl.yaml       # Phase B 零场检验
│
├── runs/
│   └── 0624/
│       ├── mu_raw_M2048_m64.h5
│       ├── mu_raw_M4096_m64.h5
│       ├── hall_m64_M2048_*.txt
│       ├── hall_m64_M4096_*.txt
│       └── vbl_sum_*.log               # [VBL_SUM] 行日志
│
├── test/
│   ├── analyze_mu_matrix.py             # μ 矩阵离线分析
│   ├── analyze_sum_gamma_mu.py          # sum(θ) 序列分析
│   ├── analyze_kahan_compare.py         # Kahan 累加对比
│   ├── analyze_contrib_decomp.py        # 逐项贡献分解
│   └── analyze_norm_diag.py             # 已有: E1 范数分析
│
└── tbplas source/
    └── sources/tbpm/
        └── kubo_bastin.h                # 插桩目标
```

---

## 7. 数据格式规范

### 7.1 μ 矩阵 HDF5 格式（Phase A）

已有的 `dckb_save_mu_file` 输出格式：

```
/mu_raw       : complex128 [M × M]    — raw μ 矩阵（无 Jackson 核）
/metadata     : int [3]               — [num_kernel, dckb_component, num_samples]
```

Python 加载：
```python
import h5py
with h5py.File("mu_raw_M4096_m64.h5", "r") as f:
    mu = f["mu_raw"][:]          # (M, M) complex128
    meta = f["metadata"][:]      # [M, component, num_samples]
```

### 7.2 sum(θ) 诊断日志格式（Phase B）

C++ stdout 输出：
```
[VBL_SUM] M=4096 rs=1 0.000767:1.234e3 0.002301:-5.678e2 ... \n
```

Python 解析：
```python
# 一行对应一个 (M, rs) 组合
# θ_i:val_i 交替排列，共 num_theta 对
```

### 7.3 分块贡献日志格式（Phase D）

```
[VBL_BLOCK] M=4096 θ=0.000767 ib=0 jb=0 sum=1.234e3
[VBL_BLOCK] M=4096 θ=0.000767 ib=256 jb=0 sum=-5.678e2
...
```

解析后重组为 `(num_blocks, num_blocks)` 贡献矩阵。

### 7.4 输出 cond 文件格式

标准两列 txt（与现有格式兼容）：
```
# energy(eV)  sigma_xy(e^2/h)
-1.500000     -2.341234e+02
-1.440000     -2.331234e+02
...
```

---

## 8. 交付物清单

### Phase A: 离线 μ 矩阵诊断

| 编号 | 任务 | 输入 | 输出 | 耗时 |
|:---:|------|------|------|:---:|
| A1 | 生成 M=2048 μ 矩阵 | `hall_m64_M2048_save_mu.yaml` | `mu_raw_M2048_m64.h5` | ~15min (含队列) |
| A2 | 生成 M=4096 μ 矩阵 | `hall_m64_M4096_save_mu.yaml` | `mu_raw_M4096_m64.h5` | ~30min (含队列) |
| A3 | μ Hermiticity 检验 | A1+A2 的 HDF5 | `mu_hermiticity_report.txt` | ~5min |
| A4 | μ 量级热图 | A1+A2 的 HDF5 | `mu_heatmap_M2048.png`, `mu_heatmap_M4096.png` | ~10min |
| A5 | μ 逐行/列统计 | A1+A2 的 HDF5 | `mu_stats_M2048.txt`, `mu_stats_M4096.txt` | ~10min |
| A6 | load 模式截断验证 | A2 HDF5 + M=2048/2560/3072/3584 load | `cond_M*_from_load.txt` | ~15min (含队列) |

### Phase B: sum(θ) 插桩诊断

| 编号 | 任务 | 输入 | 输出 | 耗时 |
|:---:|------|------|------|:---:|
| B1 | C++ 插桩 | `kubo_bastin.h` | 带 `-DTBPLAS_VBL_TRACE` 的编译 | ~5min |
| B2 | M 渐变扫描 (2048–4096, 5 档) | `hall_m64_M*_vbl.yaml` × 5 | `vbl_sum_M*.log` × 5 | ~2.5h (5 Job 并行) |
| B3 | B=0 零场检验 | `hall_m64_M4096_B0_vbl.yaml` | `vbl_sum_M4096_B0.log` | ~30min (含队列) |
| B4 | sum(θ) 曲线对比 | B2 日志 | `sum_vs_theta_all_M.png` | ~5min |
| B5 | sum(θ) 积分收敛分析 | B2 日志 | `sum_integral_vs_M.png` | ~5min |

### Phase C: Kahan 补偿求和

| 编号 | 任务 | 输入 | 输出 | 耗时 |
|:---:|------|------|------|:---:|
| C1 | Kahan 编译 | `kubo_bastin.h` Kahan 修改 | 带 `-DTBPLAS_KAHAN_SUM` 的编译 | ~5min |
| C2 | M 渐变扫描 (Kahan) | 同 B2 YAML, Kahan 编译 | `cond_kahan_M*.txt` | ~2.5h (5 Job 并行) |
| C3 | 标准 vs Kahan 对比 | C2 + Phase A/B 已有数据 | `kahan_vs_standard.png` | ~5min |
| C4 | Python 端 Kahan 验证 | Phase A μ 矩阵 | 独立验证累加精度 | ~10min |

### Phase D: 逐项贡献分解

| 编号 | 任务 | 输入 | 输出 | 耗时 |
|:---:|------|------|------|:---:|
| D1 | 分块贡献输出 | `kubo_bastin.h` 分块插桩 | `vbl_block_M4096.log` | ~30min (含队列) |
| D2 | 贡献热图绘制 | D1 日志 | `block_contrib_heatmap.png` | ~5min |
| D3 | 主要贡献区域识别 | D1 日志 | `block_contrib_report.txt` | ~5min |

### Phase F: θ 积分奇点诊断

| 编号 | 任务 | 输入 | 输出 | 耗时 |
|:---:|------|------|------|:---:|
| F1 | θ 点数扫描 (256–2048) | `hall_m64_M4096_vbl_f1.yaml` × 4 | cond vs N_θ 曲线 | ~2h |
| F2 | θ 端点截断 (δ=0.01π–0.10π) | `hall_m64_M4096_vbl_f2.yaml` × 4 | S vs δ 曲线 | ~1h |
| F3 | 梯形 vs Simpson 对比 | `kubo_bastin.h` simpson 修改 | cond_simpson vs cond_trapez | ~30min |

### Phase H: Anderson 无序根因验证 🆕

| 编号 | 任务 | 输入 | 输出 | 耗时 |
|:---:|------|------|------|:---:|
| H1 | C++ 回退到原始版本 | `kubo_bastin.h` 等 | 干净的 tbplas 编译（仅保留 μ save/load） | ~10min |
| H2 | Python 端加 Anderson 无序 | `src/model.py` | `add_anderson_disorder()` 函数 | ~10min |
| H3 | AB 单层无序验证 | `hall_m64_M4096_disorder.yaml` | σ_xy 曲线（有/无无序对比） | ~30min 集群 |
| H4 | ABC 三层无序验证 | `hall_m64_M4096_ABC_disorder.yaml` × 2 | σ_xy 曲线（δ=0 vs δ≠0，有/无无序） | ~1h 集群 |
| H5 | M 扫描验证 (AB 无序) | `hall_m64_M*_disorder.yaml` × 5 | S(M) 曲线 — 预期偏移消失 | ~2.5h 集群 |

### Phase J: Jackson 核 M 依赖性修复 🆕

| 编号 | 任务 | 输入 | 输出 | 耗时 |
|:---:|------|------|------|:---:|
| J1 | 统一核截断验证 (Python) | `mu_raw_M4096_m64.h5` | S(M') 曲线 (M'=2048/2560/3072/4096) | ~10min 本地 |
| J2 | Lorentz 核 C++ 实现 (备选) | `kpm.cpp` | 带 Lorentz 核的编译 + M 扫描 | ~30min 集群 |

### Phase E: 综合判定

| 编号 | 任务 | 输入 | 输出 | 耗时 |
|:---:|------|------|------|:---:|
| E1 | 汇总诊断结论 | A–D 全部结果 | `vbl_conclusion.md` | ~30min |
| E2 | 确定修复方案 | E1 结论 | 具体修改方案（代码/配置） | ~30min |
| E3 | 更新父计划 | E2 修复方案 | 更新 `plan_baseline_root_cause.md` | ~15min |

---

## 9. 参考文献

| 文献 | 相关内容 |
|------|---------|
| García et al., PRL **114**, 116602 (2015) | KPM Kubo-Bastin 原始实现，M=6144 |
| Yuan et al., PRB **94**, 195434 (2016) | KPM Kubo-Bastin on black phosphorus, M=15000, 5 随机实现 |
| Li et al., Comp. Phys. Commun. **293**, 108887 (2023) | TBPLaS code paper (CPC) |
| Kahan, Commun. ACM **8**, 40 (1965) | Kahan 补偿求和算法 |
| Higham, *Accuracy and Stability of Numerical Algorithms* (2002) | 浮点累加误差分析 |
| `shared/tbplas-internals.md` §12.3 | 基线偏移诊断 E1–E3 结论 |
| `MG/docs/sigma/plan_baseline_root_cause.md` | H_A/H_B/H_C 假说诊断计划 |
| `knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/02_kubo_bastin_deep_dive.md` | Kubo-Bastin 源码深度解析 |
