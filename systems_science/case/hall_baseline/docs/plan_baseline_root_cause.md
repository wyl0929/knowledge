<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-23 23:50:00
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-23 23:50:00
 * @FilePath     : /MG/docs/sigma/plan_baseline_root_cause.md
 * @Description  : Kubo-Bastin 基线偏移根因诊断 — 三个互斥假说 + 五个判别实验
-->

# Kubo-Bastin 基线偏移 — 根因诊断计划

> **状态**: 🟡 需修订 — H_A 证伪 (E1), H_B 排除 (E2), H_C 排除 (E3), 跳至 E4
> **父计划**: `plan.md` §1.2 (R2 复现目标) ← `plan_m_M_grid.md` (H_η 证伪完成) ← **本文档** (根因诊断)
> **前置**: `archive/baseline_shift_plan.md` (H₀/H₁ 已证伪) + `plan_m_M_grid.md` (双重标度区 + m 非单调交叉已确认)
> **配套任务**: `task_baseline_root_cause.md` (E1–E5 可执行任务单)
> **子计划**: `plan_vbl_trace.md` 🆕 (2026-06-24) — 假说驱动 → 数据驱动：系统变量追踪定位误差源头
> **最后修订**: 2026-06-24 — E3 完成: H_C 排除, 跳至 E4; 新增 VBL 子计划引用

> **定位**: 在 H₀ (误差累积)、H₁ (Krylov 饱和)、H_η (N_bands/M) 全部证伪后，本计划设计三个新的互斥假说和五个判别实验，目标是**确定基线偏移 S 的数值根源**。

> **源码基准**: `/home/wyl/tbplas/source/tbplas-cpp-a021ca8/sources/tbpm/`
> **关键文件**: `kubo_bastin.h` (KuboBastinCPU::kbdc_mu_raw)
> **项目路径**: `/home/wyl/project/MG/`
> **环境**: `conda activate tbplas-alpha` + `export TBPLAS_CORE_PATH=...`

---

## 1. 问题概述与物理动机

### 1.1 核心症状

Kubo-Bastin Hall 电导率 $\sigma_{xy}(E)$ 在 $M \gtrsim 2560$ 时出现整体负偏移 $S$。已知特征：

| 特征 | 详情 |
|------|------|
| **偏移形态** | 全能量范围加恒定负偏移，不破坏 QHE 平台 $\Delta\sigma$ |
| **起始阈值** | $M_c \approx 2560$，三个 $m$ 值 (256/512/1024) 一致 |
| **低 M 区** | $S \propto M^{1.5\sim1.9}$，多项式增长 |
| **高 M 区** | $S \propto \exp(\gamma M)$，$\alpha = d\ln\|S\|/d\ln M = 5\sim8$ |
| **m 依赖** | 非单调 — $M > 3584$ 时 $\|S_{256}\| > \|S_{512}\|$ |
| **NaN 状态** | `rescale: -1` (auto) 下全 M 范围零 NaN |

### 1.2 已知排除的假说

| 假说 | 证伪实验 | 证据 |
|------|---------|:---:|
| H₀: $S\propto M^2$，rs 可抑制 | rs≥2 饱和；M=2048 时 S≈0 | ❌ |
| H₁: Krylov 饱和，$M_c \propto N_{\text{orb}}$ | m=1024 偏移最大 (非 ≈0) | ❌ |
| H_η: $S = f(N_{\text{bands}}/M)$ | 相同 η 不同 m 时 S 截然不同 | ❌ |

### 1.3 战略重要性

基线偏移是当前 **Kubo-Bastin 计算的唯一剩余阻塞**：rescaling NaN 已修复、μ 复用已实现、M 扫描数据充足，但高 M 无法用于物理分析。定位根因后可能通过简单代码修改（如重正交化、精度提升）将可用 M 范围扩展 2-3×。

---

## 2. 候选假说矩阵

三个假说互斥 —— 每个都预测不同的实验签名，最多只有一个可以为真。

### 假说一览

| 假说 | 机制 | 故障位置 | 故障表现 |
|------|------|---------|---------|
> **⚠️ H_A 已被证伪 (2026-06-23)。**
> 证伪实验: [log AI:0623_2355](../../docs/log.md#ai-0623-2355)
> 以下为历史存档。

| **H_A: 向量范数膨胀** | Chebyshev 三项递推中 $\|T_n\|\psi\rangle\|$ 随 $n$ 指数增长，污染内积 $\mu_{mn} = \langle T_m v_\alpha \psi_0 \| v_\beta T_n \psi_0 \rangle$ | `kubo_bastin.h` 主循环: `alpha_n1 = 2.0 * h_sparse * alpha_n - alpha_n0` | $\|T_n\|\psi\rangle\| \propto \exp(\gamma n)$ for $n > n_c$ |
| **H_B: Jackson 核退化** | $g_n^{(M)}$ 在 $n \approx M$ 时过小 ($\sim 10^{-3}$)，大量近零加权相加产生浮点精度丢失 | `kubo_bastin.h` 累积: `mu(m,n) += factor * kernel(m) * kernel(n) * ...` | 关闭/替换核函数 → S 急剧变化 |
> **⚠️ H_C 已被证伪 (2026-06-24)。**
> 证伪实验: [log AI:0624_0025](../../docs/log.md#ai-0624-0025)
> 以下为历史存档。

| **H_C: 谱边缘泄漏** | 自动带宽检测略微低估带宽 → 部分本征值 $\|\lambda\| \gtrsim 1$ → $T_n(\lambda) \approx \cosh(n\cdot\text{arccosh}(\lambda))$ 指数增长 | `config.h` rescale 参数 → 哈密顿缩放 | 手动增大 `rescale` 20% → $M_c$ 推迟；减小 → $M_c$ 提前 |

### 判别预测表

| 实验 | H_A 预测 | H_B 预测 | H_C 预测 |
|------|--------|--------|--------|
| **E1** (范数诊断) | ❌ **证伪**: $\log_{10}\|T_n\|=-0.15$ (beta) / $-0.47$ (alpha) 全程常数，无增长 | 实际结果: $\|T_n\| \approx 0.707$ 常数，符合 H_B/H_C 预测 | 实际结果: $\|T_n\| \approx 0.707$ 常数 |
| **E2** (无核测试) | N/A (H_A 已排除) | ❌ **排除**: S 增大 3-150×, 核起抑制作用 | 实际: S 增大 → 符合 H_C/H_A? |
| **E3** (rescale 扫描) | $M_c$ 不变（递推不稳定性来自递推自身） | $M_c$ 不变 | $M_c$ 随 rescale 增大而推迟，减小而提前 |
| **E4** (精度对比) | long double → $M_c \gg 4096$ | 变化中等 | long double → $M_c \gg 4096$ |
| **E5** (m 扫描 $n_c$) | $n_c$ 弱依赖 $m$ — 由带宽而非体系大小决定 | — | — |

---

## 3. 判别实验设计

### 3.1 实验优先级与依赖

```
E1 (范数诊断) ─── 决定性证据, 无代码逻辑改动
  │
  ├── H_A 成立? ──→ E5 (m 扫描 n_c), 跳过 E2/E3
  │
  └── H_A 排除? ──→ E2 (无核测试)
                      │
                      ├── H_B 成立? ──→ 修复 Jackson 核实现
                      │
                      └── H_B 排除? ──→ E3 (rescale 扫描) → E4 (精度对比)
```

**E1 优先的原因**：
- 纯诊断（仅加 `printf`），不改计算逻辑，零风险
- 一次运行 (m=256, M=4096, 本地 ~1h) 即可区分 H_A vs H_B/H_C
- 输出 $\|T_n\psi\rangle\|$ 序列本身就极其珍贵 — 无论 H_A 是否成立，都揭示 Chebyshev 向量的实际数值行为

### 3.2 E1: 向量范数诊断

**目的**: 检验 H_A — Chebyshev 向量范数是否指数增长。

**方法**: 在 `kubo_bastin.h` 的 `kbdc_mu_raw()` 外循环末尾插桩：

```cpp
// 在 kbdc_mu_raw() 中，每完成一个 n 的向量迭代后：
if (n % 128 == 0 || n == num_kernel - 1) {  // 每 128 步输出一次，避免 I/O 淹没
    double norm_alpha = alpha_n.norm();       // ||alpha_n|| = ||T_n(H)|alpha_0⟩||
    double norm_beta  = beta_n.norm();        // ||T_n(H)|beta_0⟩||
    std::cout << "[NORM_DIAG] n=" << n
              << " log10|alpha_n|=" << std::log10(std::max(norm_alpha, 1e-300))
              << " log10|beta_n|="  << std::log10(std::max(norm_beta, 1e-300))
              << std::endl;
}
```

> **注意**: `alpha_n = T_n(Ĥ)|v_x ψ_0⟩` 和 `beta_n = T_n(Ĥ)|v_y ψ_0⟩` 是 `kbdc_mu_raw()` 中已有的变量。只需加 `norm()` 调用。
> 相关代码位置: `kubo_bastin.h` ~line 230-280, `alpha_n1 = 2.0 * h_sparse * alpha_n - alpha_n0` 循环体。

**配置**: m=256, M=4096, rs=1 (单样本即可), rescale=-1, B=100T。

**预期运行时间**: 本地单节点 ~1h (M=4096, m=256)。

**成功判据**:

| 观察 | 判断 |
|------|:---:|
| $\log_{10}\|T_n\psi\rangle\|$ 始终 $\in [0, 0.5]$ | H_A **排除** |
| $\log_{10}\|T_n\psi\rangle\|$ 在 $n \approx 2500$ 处突破 1.0，之后线性增长 | H_A **确认** |
| 增长斜率 $\gamma$ 与 $m$ 值有关 | 解释非单调 m 交叉 |

**输出**:
- 终端 stdout: `[NORM_DIAG]` 行序列 (n=0, 128, 256, ..., 4096)
- 后续用 `test/analyze_norm_diag.py` 绘制 $\log_{10}\|T_n\psi\rangle\|$ vs $n$

### 3.3 E2: 无核测试

**目的**: 检验 H_B — Jackson 核是否导致浮点退化。

**方法**: 修改 `kubo_bastin.h` 的 `apply_jackson_kernel()`，注释掉核乘法：

```cpp
// 原始:
mu(m, n) *= kernel(m) * kernel(n);

// E2 测试版:
// mu(m, n) *= kernel(m) * kernel(n);  // 跳过 Jackson 核
// 或替换为 Lorentz 核: kernel_lor[n] = sinh(λ(1 - n/M)) / sinh(λ)
```

> 更简单的方案: 直接在 `kbdc_mu_raw()` 的输出上跳过核调用，仅用 `truncate_mu()` + 直接 `cond_from_trace()`。

**配置**: m=256, M=4096, rs=1, 其余同 E1。对比 M=1024/2048/3072/4096 四个点的 S (无核 vs 有核)。

**预期运行时间**: 本地 ~1.5h (4 M 值 × 截断)。

**成功判据**:

| 观察 | 判断 |
|------|:---:|
| 无核 S 与有核 S 差异 < 10% | H_B **排除** |
| 无核 S 大幅减小 (> 50%) 或消失 | H_B **确认** |
| 无核 S 反而增大 | Jackson 核在起抑制(非退化)作用 |

### 3.4 E3: Rescale 扫描

**目的**: 检验 H_C — 谱边缘泄漏假说。

**方法**: 手动设置 `rescale` 值替代 `rescale: -1` (auto)，在 m=256, M=4096, rs=1 下扫描：

| rescale | 物理含义 | H_C 预测 |
|:---:|------|------|
| auto (-1) | 基准 (带宽约 20 eV → rescale ≈ 10.0) | S ≈ -990 |
| 8.0 | 收缩 20%: $\lambda_{\max} \approx 1.25$ → 大量本征值超 1 | S 急剧增大 |
| 9.0 | 收缩 10%: $\lambda_{\max} \approx 1.11$ | S 明显增大 |
| 11.0 | 扩展 10%: $\lambda_{\max} \approx 0.91$ | S 明显减小 |
| 12.0 | 扩展 20%: $\lambda_{\max} \approx 0.83$ | S 进一步减小 |

> ⚠️ `rescale` 过小 (< ~8.0) 会导致 NaN (已知机制)，但 E3 的目的正是测试 rescale 的精细影响。

**预期运行时间**: 5 个 YAML × ~1h = ~5h (本地串行或集群并行)。

**成功判据**:

| 观察 | 判断 |
|------|:---:|
| 5 个 rescale 值下 S 变化 < 30% | H_C **排除** |
| rescale 增大 → S 单调减小；rescale 减小 → S 单调增大 | H_C **确认** |

### 3.5 E4: 浮点精度对比 (备选)

**目的**: 区分"double 精度不足"与"算法本身发散"。

**方法**: 修改 tbplas CMake 编译选项，启用 `long double` (80-bit x87) 精度，重新编译 `interface_tbpm.so`。对比 double vs long double 的 S(M) 曲线。

> ⚠️ 此实验需重新编译 tbplas C++ 核心，涉及 Eigen 模板的 `long double` 实例化。如果编译失败或性能影响过大 (>3×)，可降级为手动对比 float vs double (仅验证精度趋势)。

**配置**: m=256, M=4096, 其余同 E1。

**预期运行时间**: 编译 ~5min + 运行 ~1h。

**成功判据**:

| 观察 | 判断 |
|------|:---:|
| long double 下 S(4096) 与 double 下差异 < 2× | 精度提升帮助有限 |
| long double 下 S(4096) < 10 (即偏移几乎消失) | **直接修复** — 切换到 long double 编译 |

### 3.6 E5: m 扫描范数发散点 (H_A 确认后)

**目的**: 定量解释 m 非单调交叉行为。

**方法**: E1 的扩展 — 对 m=512、m=1024 各重复范数诊断，提取 $n_c$ (范数开始指数增长的转折点)。

**预期**: $n_c(m=512) > n_c(m=256)$ 且 $n_c(m=1024) > n_c(m=256)$ → 解释为什么 m=512 在高 M 更优 (更大的 m 给了更长的"安全期")，但 m=1024 为什么最终最差 (可能是向量维数大导致累积误差也大)。

---

## 4. 系统架构规划

本计划不涉及新模块，仅对已有文件做最小侵入修改。

| 文件 | 修改 | 说明 |
|------|:---:|------|
| `sources/tbpm/kubo_bastin.h` | 插桩 | E1: `kbdc_mu_raw()` 末尾加范数输出 |
| `sources/tbpm/kubo_bastin.h` | 修改 | E2: 临时注释 `apply_jackson_kernel()` 调用 |
| `configs/hall_m256_M4096_*.yaml` | 新建 | E3: rescale 扫描 5 配置 |
| `configs/hall_m512_M4096_diag.yaml` | 新建 | E5: m=512 范数诊断 |
| `configs/hall_m1024_M4096_diag.yaml` | 新建 | E5: m=1024 范数诊断 |
| `test/analyze_norm_diag.py` | 新建 | 范数输出解析 + 标度拟合 |

### 4.1 接口约定

所有 E1/E5 诊断输出通过 `stdout` 的 `[NORM_DIAG]` 前缀标记，与正常 tbplas 输出隔离。不改变任何 C++ API 或 Python 绑定。

### 4.2 安全设计

- **E1 插桩**: 使用 `#ifdef TBPLAS_NORM_DIAG` 条件编译，默认关闭，不影响正常使用
- **E2 无核**: 单独编译分支或运行时通过 YAML 开关控制
- **E3 rescale**: 仅修改 YAML 配置，零代码改动
- **所有实验**: 不改变已有计算逻辑的数值结果（E1 仅加输出，E2 使用独立编译）

---

## 5. 参数设计

### 5.1 通用固定参数

```yaml
model:
  num: 1            # 单层 graphene (先诊断简单体系)
  stacking: AB
  delta: 0.0
  B_values: [100.0]
  gauge: 0
tbpm:
  rescale: -1       # E3 实验中改为手动值
  ts: 64
  num_spin: 2
  algo: cpu
  temperature: 10.0
hall:
  dckb_component: 2
  dimension: 2
  dckb_energies: {min: -1.5, max: 1.5, num: 301}  # 粗网格即可，仅需 S
```

### 5.2 实验变参

| 实验 | 变参 | 取值 |
|------|------|------|
| E1 | m, M, rs | m=256, M=4096, rs=1 |
| E2 | M, Jackson 核 | M∈{1024,2048,3072,4096}, 核=on/off |
| E3 | rescale | {8.0, 9.0, auto, 11.0, 12.0} |
| E4 | 浮点精度 | double / long double |
| E5 | m | {256, 512, 1024} |

---

## 6. 文件结构

```
MG/
├── configs/
│   ├── hall_m256_M4096_diag.yaml        ← E1 范数诊断
│   ├── hall_m256_M4096_nokernel.yaml    ← E2 无核
│   ├── hall_m256_M4096_rescale_{8,9,11,12}.yaml  ← E3 rescale 扫描
│   ├── hall_m512_M4096_diag.yaml        ← E5
│   └── hall_m1024_M4096_diag.yaml       ← E5
├── test/
│   └── analyze_norm_diag.py             ← 范数输出解析
├── docs/sigma/
│   ├── plan_baseline_root_cause.md      ← 本文档
│   ├── plan_m_M_grid.md                 ← 前置 (H_η 证伪)
│   └── archive/
│       ├── baseline_shift_plan.md       ← 前置 (H₀/H₁ 证伪)
│       └── plan_kb_mu_reuse.md          ← μ 复用实现
└── runs/
    └── 0624/                            ← 诊断实验输出
```

---

## 7. 数据格式

### 7.1 E1 范数诊断输出 (stdout)

```
[NORM_DIAG] n=0 log10|alpha_n|=0.0000 log10|beta_n|=0.0000
[NORM_DIAG] n=128 log10|alpha_n|=0.0231 log10|beta_n|=0.0231
[NORM_DIAG] n=256 log10|alpha_n|=0.0482 log10|beta_n|=0.0483
...
[NORM_DIAG] n=4096 log10|alpha_n|=5.2317 log10|beta_n|=5.2315
```

两列: `n` → `log10|alpha_n|` (×2 组: alpha 和 beta 通道)。

### 7.2 E2/E3 输出

标准 Hall 电导率两列格式 (`eng`, `sigma_xy`)，分析脚本从 $E \approx -1.5$ eV 窗口提取 S。

---

## 8. 交付物清单

| 编号 | 实验 | 交付物 | 预计耗时 | 可并行 |
|:---:|------|------|------|:---:|
| **E1** | 范数诊断 | C++ 插桩 (1 文件) + 1 YAML + 1 次本地运行 + stdout 解析 | ~1h | — |
| **E2** | 无核测试 | 1 代码分支 + 4 YAML + 4 次截断运行 | ~1.5h | ✅ (截断可并行) |
| **E3** | Rescale 扫描 | 4 YAML + 4 次本地/集群运行 | ~4h | ✅ |
| **E4** | 精度对比 | CMake 修改 + 重编译 + 1 YAML + 1 次运行 | ~2h | — |
| **E5** | m 扫描 n_c | 2 YAML + 2 次范数诊断 | ~2h | ✅ |
| **汇总** | 分析制图 | `analyze_norm_diag.py` + `baseline_root_cause_summary.png` | ~0.5h | — |

> **最短关键路径**: E1 (1h) → 判读 → 决定后续实验。若 H_A 确认，跳过 E2/E3，直通 E5。

---

## 9. 成功判据 (终极)

| 判据 | 标准 |
|------|------|
| 根因确认 | 三个假说中恰好一个被保留，其余两个至少有 1 个证伪条件触发 |
| 可复现 | 关键诊断结果在同参数下重复至少 2 次一致 |
| 可修复 | 确认的根因对应一个具体的代码修改方案 (如重正交化 / 核替换 / rescale 修正) |
| 修复验证 | 应用修复后，M=4096 的 S < 5% 物理信号 (即 < ~2 e²/h) |

---

## 参考

- `archive/baseline_shift_plan.md` — H₀/H₁ 测试方案与证伪记录
- `plan_m_M_grid.md` — m×M 网格数据 + 双重标度区发现
- `archive/plan_kb_mu_reuse.md` — μ 复用实现 (提供 HDF5 load 模式用于快速截断)
- `../../shared/tbplas-internals.md` §9.8 — KPM 实践建议 + §12 Chebyshev 三项递推精度分析
- `../../memories/kubo-bastin-convergence.md` — rescale=-1 必须、NaN 根因已修复
- PRL 114, 116602 (2015) — Kubo-Bastin KPM 收敛参数基准 (Weiße et al.)
- `/home/wyl/tbplas/source/tbplas-cpp-a021ca8/sources/tbpm/kubo_bastin.h` — C++ 插桩目标文件
- `/home/wyl/tbplas/source/tbplas-cpp-a021ca8/sources/tbpm/kpm.h` — `jackson_kernel()` 实现
