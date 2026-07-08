<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-16 22:13:57
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-01 12:00
 * @FilePath     : /MG/docs/blue_print.md
 * @Description  : 多层 Graphene 量子霍尔效应 — 总计划 (quantum-kite + tbplas 双轨验证)
-->

# σ — 多层 Graphene 量子霍尔效应：总计划书

> **状态**: � 战略修正 — tbplas Kubo-Bastin 基线偏移根因重新定位: num_integ_steps < num_kernel 导致 Nyquist 混叠 (非 C++ 浮点精度)
> **父计划**: `../../CONTEXT.md`（MG 项目全局上下文）
> **最后修订**: 2026-07-01 14:00 — 🔴 重大修正: VBL Phase A–M "条件收敛+浮点精度"结论被 Nyquist 混叠根因取代
>
> **战略背景**：
> - ~~tbplas Kubo-Bastin Hall 电导率在高 $M$ 下出现基线偏移（VBL Phase A–M 全 9 假说排除，根因：条件收敛 + 浮点精度，详见 `archive/plan_vbl_trace.md`）~~
> - **> ⚠️ 以上结论已被证伪 (2026-07-01)。** 新发现: M_int 扫描 (M×num_integ_steps 全矩阵) 证实基线偏移的真实根因是 `dckb_num_integ_steps` (θ-积分点数) 不足导致的 **Nyquist 混叠**。当 `num_integ_steps < num_kernel` 时，Γ(θ) 矩阵的高频振荡分量 (频率 ∝ M) 被欠采样 → 混叠伪影 → σ_xy 系统性偏差。正确配置 `num_integ_steps ≥ num_kernel` 即可消除。详见 `Phase0_save_load/plan.md` §实际执行路径。
> - 有限 $\eta$ 计算展宽路径理论证伪（`../references/02_kubo_bastin_deep_dive.md` §1.2.F：$e^{n\varphi}$ 指数增长，非衰减）
> - ~~**新策略**：引入 **quantum-kite** 作为独立 Kubo-Bastin 实现 → 交叉验证 tbplas~~
> - **> ⚠️ 战略调整 (2026-07-01)**: quantum-kite 交叉验证不再是必须的阻断步骤。tbplas 基线偏移已通过正确参数 (num_integ_steps ≥ num_kernel) 解决。quantum-kite 保留为独立验证工具 (Phase 1–2 降级为可选对照)

> **定位**：本文档为 Hall 电导率方向的**总计划**，聚焦大方向与阶段划分。
> 各阶段的详细实现方案拆分到子计划（`plan_*.md`），本文仅维护顶层路线图和阶段间接口。
> **目标论文**：
>   - [G1] García et al., PRL **114**, 116602 (2015) — monolayer graphene QHE (KPM Kubo-Bastin, M=6144)
>   - [P1] L. Zhang et al., Nature Physics **7**, 953–957 (2011) — ABC trilayer QHE 实验 ($l=3$ chirality)
>   - [P2] F. Zhang, Tilahun, MacDonald, PRB **85**, 165139 (2012) — ABC trilayer N=0 LL 理论 (Hund's rules)
> **最终目标**：ABA/ABC stacking domain wall 上的量子输运（$\sigma_{xy}$, $\sigma_{xx}$）

---

## 0. 总体路线图（6 阶段）

```
Phase 0: tbplas-exp save/load 一致性校准 🆕
  ├── 0.1 确认 tbplas-exp 的 save/load mu 管线完整性
  ├── 0.2 同参数下 save 模式 vs load 模式 σ_xy(E) 对比
  └── 0.3 验证: 两模式 σ_xy(E) 在 M≤2560 安全窗口内恒等 (diff < 1e-10)
  ⏱ 预计: 0.5 天

Phase 1: quantum-kite 安装 + σ_xy 实现
  ├── 1.1 编译安装 quantum-kite (C++/Python)
  ├── 1.2 构建 monolayer graphene 模型 (与 tbplas 相同 TB 参数)
  ├── 1.3 实现 DC conductivity → σ_xy 计算
  └── 1.4 验证: B=0 时 σ_xy=0, B≠0 时有 QHE 信号
  ⏱ 预计: 1–2 周

Phase 2: quantum-kite ↔ tbplas 交叉验证
  ├── 2.1 相同体系 (monolayer, m=64, B=100T) 双代码独立计算
  ├── 2.2 对比 μ 矩阵 / Γ 核 / sum(θ) / σ_xy(E) 各级中间量
  │      └── tbplas 侧使用 Phase 0 校准后的 save/load 管线提供 μ 矩阵
  ├── 2.3 定位 tbplas 偏离 quantum-kite 的具体环节
  └── 2.4 判定: tbplas 代码 bug vs 算法极限
  ⏱ 预计: 1 周

Phase 3: 复现 García 2015 — monolayer graphene QHE
  ├── 3.1 quantum-kite 主算 + tbplas 对照 (M≤2560 安全窗口)
  ├── 3.2 验证 σ_xy = ±2, ±6, ±10 e²/h 平台序列
  ├── 3.3 建立参数基准 (M, rs, T, B 范围)
  └── 3.4 输出: monolayer QHE 标准参考数据
  ⏱ 预计: 1 周

Phase 4: 复现 Zhang 2011 — ABC trilayer graphene QHE
  ├── 4.1 quantum-kite 主算 (ABC trilayer, 多 B 值)
  ├── 4.2 验证 J=3 chirality 标志: ν = ±6, ±10, ±14 平台
  ├── 4.3 Landau 扇图 + σ_xx SdH 振荡
  └── 4.4 输出: trilayer QHE 复现数据 → 与实验对比
  ⏱ 预计: 2 周

Phase 5: ABA/ABC domain wall 输运
  ├── 5.1 构建 stacking domain wall 超胞
  ├── 5.2 计算 domain wall 上的 σ_xy, σ_xx
  └── 5.3 分析 domain wall 态的拓扑输运贡献
  ⏱ 预计: 2–3 周
```

> **依赖关系**：Phase 0 → Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 严格串行。
> Phase 0 确保 tbplas 的 mu save/load 管线在进入量子-kite 交叉验证前已经过自洽校准。
> 每个 Phase 完成的标志：输出数据 + 与参考文献的定量对比。
> 子计划索引：
> - Phase 0 详细方案 → `Phase0_save_load/plan.md` ✅ (2026-07-01 已创建)
> - Phase 1–2 详细方案 → `sigma/plan_quantum_kite.md` ✅ (2026-06-30 已创建)
> - Phase 3 详细方案 → 🆕 `sigma/plan_garcia2015.md`（待创建）
> - Phase 4 详细方案 → 🆕 `sigma/plan_zhang2011.md`（待创建）
> - Phase 5 详细方案 → 🆕 `sigma/plan_domain_wall.md`（待创建）
> - tbplas 基线偏移诊断 → `sigma/archive/plan_vbl_trace.md` ✅ (Phase A–M 完成)
> - 有限 η 理论分析 → `sigma/plan_eta_kubo_bastin.md` 🟡 (理论证伪, 路径废弃)

---

## 0.1 🆕 Phase 0: tbplas-exp save/load 一致性校准

> **动机**：Phase 2 的双代码交叉验证需要 tbplas 侧提供 $\mu$ 矩阵用于与 quantum-kite 逐级对比。
> tbplas-exp 已移植了 mu save/load 功能（`dckb_save_mu_file` / `dckb_load_mu_file`），
> 但在投入交叉验证之前，必须确认 save→load 往返不引入额外误差。

### 目标

验证 tbplas-exp 的 save 模式（计算 + 保存 $\mu$ 到 HDF5）和 load 模式（从 HDF5 加载 $\mu$ 后直接积分）在 $M \le 2560$ 安全窗口内产生**恒等**的 $\sigma_{xy}(E)$。

### 判别标准

| 测试 | 判据 |
|------|------|
| save vs load $\sigma_{xy}(E)$ 全谱 | $\max\|\sigma_{xy}^{\text{save}} - \sigma_{xy}^{\text{load}}\| < 10^{-10}\ e^2/h$ |
| M 扫描 (64/256/512/1024/2048) | 所有 M 下两模式恒等 |
| 多 B 值抽样 (B=0, 50T, 100T) | B=0 时 $\sigma_{xy}\equiv 0$（时间反演对称性），B≠0 时两模式一致 |

### 与后续 Phase 的接口

- **输出到 Phase 2**：经校准的 tbplas $\mu$ 矩阵（HDF5 格式），可被 quantum-kite 侧读取对比
- **输出到 Phase 3**：确认 tbplas 在 $M \le 2560$ 窗口内可信任，作为 García 2015 复现的对照引擎

### 子计划

> 详细实现方案见 [`Phase0_save_load/plan.md`](Phase0_save_load/plan.md) ✅ (2026-07-01 已创建).

---

## 1. 项目概述与物理目标

> ⚠️ **历史存档标记**：以下 §1.1–§1.3 为原计划（2026-06-16）的物理背景，基于「直接用 tbplas 复现」的假设。
> 当前战略已调整为 quantum-kite + tbplas 双轨（见 §0 路线图）。
> 物理图景和研究目标不变，但实现路径已更新。

### 1.1 物理图景

ABC (rhombohedral) 三层石墨烯在垂直磁场下展现独特的量子霍尔效应：
- 低能有效模型为 **pseudospin J=3** 的 chirality（单层 J=1，双层 J=2）
- 朗道能级结构包含 12 重简并的 N=0 LL（来自 3 轨道(n=0,1,2) × 2 自旋 × 2 谷；相互作用下通过 Hund's rules 逐级解除简并）
- LL 能量标度 $E_n \propto B^{3/2}$（J=3 chirality 特征；单层 $\propto B^{1/2}$，双层 $\propto B^{1}$）
- 零磁场下有非零 valley Chern number $C_v = \pm 3/2 \cdot \mathrm{sgn}(\Delta)$（位移场 $\Delta$ 打开能隙时）
- Landau 扇图：$\sigma_{xy}$ 台阶出现在 $\nu = \pm 6, \pm 10, \pm 14, \dots$（Zhang 2011, J=3 chirality 的标志性序列）
- N=0 Landau 能级 12 重简并通过 Hund's rules 逐级解除：自旋极化 → 谷极化 → 层极化（Zhang 2012）

### 1.2 复现目标

| 编号 | 来源论文 | 复现内容 | 验证指标 |
|------|---------|---------|---------|
| **R1** | Zhang 2012 | $B=0$ ABC trilayer 能带结构 + Berry curvature / valley Chern | $C_v = \pm 3/2 \cdot \mathrm{sgn}(\Delta)$，验证 J=3 chirality |
| **R2** | Zhang 2011 | $\sigma_{xy}$ vs $V_g$ 在不同 $B$ 下的台阶（实验 Fig.2） | 平台量子化 $\nu = \pm 6, \pm 10, \pm 14, \dots e^2/h$ |
| **R3** | Zhang 2011 | Landau 扇图：$\sigma_{xy}$ 在 $(n, B)$ 平面的颜色图（实验 Fig.3） | 扇图发散结构，$\nu=6$ 台阶最宽 |
| **R4** | Zhang 2012 | N=0 LL 在磁场下的单粒子简并结构（DOS 峰值计数） | N=0 LL 12 重简并（3 轨道 × 2 自旋 × 2 谷）；相互作用驱动的 Hund's rules 劈裂（spin→valley→layer）超出 TBPM 单粒子能力，仅作定性讨论 |
| **R5** | Zhang 2011 | $\sigma_{xx}$ 的 SdH 振荡，Berry phase $3\pi$ 验证 | SdH 振荡周期和相位，与 J=3 一致 |
| **R6** | Zhang 2011 | 低 $B$ 下 cyclotron mass 随 $n$ 发散行为 | $m^* \propto n^{-1/2}$（J=3 色散的标志，$m^* \propto 1/p \propto \varepsilon^{-1/3} \propto n^{-1/2}$） |

### 1.3 与最终目标的关系

```
Phase 1 (本计划): ABC trilayer 单畴 σ_xy, σ_xx 复现
  → 验证 tbplas + Peierls + Kubo-Bastin 工作流
  → 建立参数基准（B, T, m, N_kernel 等）
  → 确认代码能复现已知实验结果

Phase 2 (后续): ABA trilayer 单畴计算
  → 对比 ABA vs ABC 的 QHE 差异（ABA 是半金属，无 gap）
  → 理解 stacking 对输运的影响

Phase 3 (最终): ABA/ABC domain wall 输运
  → 构建含 stacking domain wall 的超胞
  → 计算 domain wall 上的 σ_xy, σ_xx
  → 分析 domain wall 态的拓扑输运贡献
```

---

## 2. 代码资产与工具链

> ⚠️ **路径调整 (2026-07-01, 14:00 再次修正)**：基线偏移根因重新定位为 `num_integ_steps` 欠采样 (Nyquist 混叠)。
> tbplas 恢复为主计算引擎，quantum-kite 降级为可选对照。原 tbplas 资产清单完全适用。

### 2.0 🆕 工具链总览 (2026-07-01 修正)

| 工具 | 角色 | 状态 |
|------|------|:---:|
| **tbplas** (exp) | 🥇 **主计算引擎** — Kubo-Bastin DC conductivity → $\sigma_{xy}$ (M ≤ 4096, int ≥ M) | ✅ 已校准 |
| **quantum-kite** | 🥈 **可选对照** — 独立 Kubo-Bastin 实现，验证用 | 🟡 可选 |
| **MG/src** (model/calc/io_vis) | 🔧 **模型构建 + 数据管线** — 统一的 TB 模型和 I/O | ✅ 已部署 |
| **h3clogin 集群** | 💻 **计算资源** — SLURM 批量提交 | ✅ 已配置 |

### 2.1 🆕 quantum-kite 预期能力

| 能力 | 说明 |
|------|------|
| Kubo-Bastin DC conductivity | $\sigma_{xy}$ 和 $\sigma_{xx}$，与 tbplas 同算法但独立实现 |
| Chebyshev 展开 | 预期使用稳定的 KPM 实现（García 2015 合作组代码） |
| 磁场 (Peierls) | 需确认 quantum-kite 对磁场的支持方式 |
| Python 接口 | 需确认是否提供 Python 绑定或需通过 C++ 调用 |

### 2.2 可直接复用的 MG 模块 (tbplas 侧)

| 模块 | 文件 | 已有能力 | 本次使用 |
|------|------|---------|---------|
| 模型构建 | `src/model.py` | `build_trilayer_graphene("ABC", delta=D)` + `calc_hop`/`extend_hop` | ✅ 直接用 |
| 扩胞 | `src/model.py` | `expand_cell(prim_cell, m)` | ✅ 直接用 |
| 磁场 | `src/model.py` | `apply_magnetic_field(sample, B, gauge)` | ✅ 直接用 |
| Hall 计算 | `src/calc.py` | `calc_hall_cond_tbpm(sample, cfg)` → Kubo-Bastin | ✅ 直接用 |
| DC 计算 | `src/calc.py` | `calc_dc_cond_tbpm(sample, cfg)` → TBPM DC 关联 | ✅ 直接用 |
| Berry 计算 | `src/calc.py` | `calc_berry_curvature(prim_cell, cfg)` → Kubo 公式 | ✅ 零场验证用 |
| Valley Chern | `src/calc.py` | `calc_valley_chern(kpt_cart, omega_xy, b1, b2, cfg)` | ✅ 零场验证用 |
| TBPM 配置 | `src/calc.py` | `config_tbpm_solver(solver, cfg)` | ✅ 直接用 |
| 主调度 | `src/main.py` | `_run_hall()`, `_run_dc()` 已支持 B 扫描 | ✅ 直接用 |
| IO/绘图 | `src/io_vis.py` | `save_conductivity()`, `plot_conductivity()` | ✅ 直接用 |

### 2.2 需要新增或修改的部分

| 需求 | 位置 | 说明 |
|------|------|------|
| $\sigma_{xy}$ vs $n$ 映射 | 新建 `src/sigma_utils.py` | $E_F \to n$：从 DOS 积分得到载流子浓度 $n(E_F) = \int_{E_0}^{E_F} \rho(E) dE$ |
| Landau 扇图绘图 | 新增 `src/io_vis.py` 函数 | `plot_landau_fan(B_list, n_list, sigma_xy)` |
| Zhang 2011 专用 YAML | 新建 `configs/sigma_zhang2011.yaml` | 实验复现：B=2-45T 扫描 + E_F→n 映射参数 |
| Zhang 2012 专用 YAML | 新建 `configs/sigma_zhang2012.yaml` | 理论验证：Berry curvature + valley Chern |
| 批量运行脚本 | 新建 `slurm/sigma_batch.sh` | 自动提交多个 B 组合 |
| 收敛性测试配置 | 新建 `configs/sigma_converge.yaml` | m 扫描 + dckb 参数扫描 |

---

## 2.6 实际执行路径（2026-06-21 补充, 2026-07-01 更新）

> 原计划 §3 假设可直接在 ABC trilayer 上开始 QHE 计算。
> 实际执行中，在 monolayer graphene 上先完成了以下前置验证
> （详见 `../log.md` AI:0618–0621 系列条目）：

| 步骤 | 内容 | 核心产出 | log 条目 |
|------|------|---------|----------|
| T9 参数扫描 | B/m/rs/N_k/N_θ/E 全维度 29 YAML | monolayer 参数基准 | AI:0619_2330 |
| NaN 根因诊断 | rescale=9.0 误配 → 修复为 rescale=-1 | rescale=-1 是安全默认值 | AI:0620_2230 |
| M 扫描 | M=64–1024 ×7 | M=256 最优，M≤1024 无 NaN | AI:0621_0324 |
| 🆕 **M_int 扫描 (2026-07-01)** | M × num_integ_steps (512–4096) 全矩阵 (m=512, rescale=20) | **基线偏移根因重新定位**: Nyquist 混叠 (num_integ_steps < num_kernel), 非浮点精度。int/M ≥ 1.0 安全, < 0.5 灾难性 | log AI:0701_Mint |
| 基线偏移 | M≥4096 常数偏移 (非 NaN) | → ~~VBL Phase A–M 全 9 假说排除, 根因: 条件收敛+浮点精度~~ **> ⚠️ 已证伪 (2026-07-01)** — 真正根因为 num_integ_steps 欠采样 | AI:0624–0627 (历史存档) |
| ABC M=4096 | ABC trilayer Hall M=4096_m256_B100 | rescale=-1 零 NaN, 但基线偏移严重 ($\sigma_{xy}$ 全正 48–513, 无台阶) | AI:0623_2020 |
| 有限 η 理论证伪 | 严格推导 (02_kubo_bastin_deep_dive.md §1.2.F) | 有限 η 在 G⁺ 侧引入 $e^{n\varphi}$ 指数增长 → 计算展宽恶化收敛 | AI:0630_2200 |
| 🆕 战略转向 | tbplas 阻塞确认 → 引入 quantum-kite | 新路线图 §0；tbplas 保留为 $M\le 2560$ 对照工具 | 2026-07-01 |

> **对后续的影响**：
> - 🔴 **基线偏移已解决 (2026-07-01)**: 正确配置 `num_integ_steps ≥ num_kernel` 即可消除。tbplas 在 $M \le 4096$ 下可正常使用（需 int ≥ M）。
> - 🟡 **quantum-kite 降级为可选对照**: Phase 1–2 不再是阻断步骤，保留为独立验证工具。
> - 🟢 **Phase 3 (García 2015 复现) 可直接在 tbplas 上推进**: M=4096 需 int=4096（或更高）。
> - 原 §3 的详细步骤方案可直接复用（tbplas 独用），无需替换为 quantum-kite。

---

## 3. 计算步骤方案（原 tbplas 路线 — 历史存档）

> ⚠️ **路径调整 (2026-07-01)**：以下 §3.1–§3.5 为原计划的详细步骤（基于 tbplas 独用假设）。
> 当前战略见 §0 新路线图。本节保留作为 **Phase 4 (ABC trilayer QHE)** 的步骤模板——
> 将 "tbpm" 替换为 "quantum-kite" 后大部分步骤仍然适用。
> 新的 Phase 1–3 详细方案将在 `plan_quantum_kite.md` 和 `plan_garcia2015.md` 中展开。

### 3.1 Phase 0（原）：零场验证 — Zhang 2012 理论基线（R1）

**目的**：在加磁场之前，确认 ABC trilayer 的 TB 模型正确，验证 J=3 chirality。

```
步骤 0.1: 能带计算 + 低能色散
  输入: prim_cell (ABC, delta=0)
  方法: calc_band_diag() → k_path Γ-M-K-Γ
  验证: K 点附近低能色散 ≈ E ∝ k³（J=3），非单层 ∝k 也非双层 ∝k²

步骤 0.2: Berry curvature + Valley Chern
  输入: prim_cell (ABC, delta=0.016, 0.030 eV)
  方法: calc_berry_curvature(Nk=2001) + calc_valley_chern()
  验证: C_v ≈ ±3/2 × sgn(Δ)，对比 tbplas-internals.md §8.11
  验证: dimer 带 C₁+C₂ ≈ 0，低能带 C₃ ≈ ±1.5

步骤 0.3: DOS 验证 (diag)
  输入: prim_cell (ABC, delta=0, 0.03 eV)
  方法: calc_dos_diag(Nk=201) → 确认能隙宽度和 van Hove 奇点
  验证: delta=0 时费米能级 DOS=0（半金属），delta≠0 时能隙打开
```

### 3.2 Phase 1：σ_xy Hall 电导率 — Zhang 2011 实验复现（R2-R3）

**目的**：复现 ABC trilayer 标志性的 ±6, ±10, ±14 e²/h 量子化平台。

```
步骤 1.1: m 收敛性测试
  B = 18 T 固定（Zhang 2011 Fig.2 主数据），m = 128, 256, 512
  跑 calc_hall_cond_tbpm()
  判断: σ_xy 平台位置不随 m 漂移

步骤 1.2: dckb_num_kernel 收敛性测试
  B = 18 T, m = 256, dckb_num_kernel = 1024, 2048, 4096
  判断: 噪声 vs 精度平衡

步骤 1.3: B 场扫描（无位移场）
  B = 10, 18, 30, 45 T（Zhang 2011 实验参数；B<10T 时 LL 分辨率不足，仅定性探索）
  delta = 0
  输出: σ_xy(E_F) × 4 条曲线
  验证: J=3 标志性序列 ν = ±6, ±10, ±14, ±18, ...
  注意: 单粒子图像下第一个平台就是 ν=±6（N=0 LL 含 12 重简并）；ν=±2,±4 需相互作用解除简并后才出现，TBPM 单粒子计算无法复现

步骤 1.4: 位移场影响
  B = 18 T
  delta = 0, 0.01, 0.03, 0.05 eV
  输出: σ_xy(E_F, delta) 曲线
  验证: 位移场打开能隙 → 中性点 σ_xy=0 平台出现

步骤 1.5: Landau 能级提取
  从 DOS(E, B) 的峰值提取 LL 能量
  绘制 LL energy vs B^(3/2)（J=3 LL 色散：ε ∝ p³ → Onsager 量子化 ε_n ∝ B^(3/2)）
  验证: 对比 J=1 (∝ B^(1/2)) 和 J=2 (∝ B) 确认 chirality
```

### 3.3 Phase 2：σ_xx SdH 振荡 + Berry phase 验证（R5-R6）

**目的**：复现 SdH 振荡，从中提取 Berry phase 3π。

```
步骤 2.1: DC 电导率收敛测试
  B = 10 T, m = 256
  dc_cond_num_time_steps = 512, 1024, 2048

步骤 2.2: σ_xx(E) 计算
  B = 5, 10, 18 T
  输出: σ_xx(E) 曲线
  验证: SdH 振荡周期 ∝ 1/B，相移对应 Berry phase 3π
  注意: TBPM DC 路径（calc_corr_dc_cond）不使用 Fermi-Dirac 算符，temperature 参数对 σ_xx 无效（tbplas-internals §11.4）；SdH 锐利度由 dc_cond_num_time_steps 和 rs 控制

步骤 2.3: σ_xy + σ_xx 联合图
  同 B 值，叠加 σ_xy 平台和 σ_xx 峰
  验证: σ_xx 峰在 σ_xy 平台过渡处

步骤 2.4: Cyclotron mass 验证
  从 TBPM 计算 m* = (ħ²/2π)·dA/dE（通过 LL 间距）
  验证: m* ∝ n^(-1/2)（J=3 色散的标志；ε ∝ p³ → m* = p/(∂ε/∂p) ∝ 1/p ∝ n^(-1/2)，对比 Zhang 2011 Fig.4）
```

### 3.4 Phase 3：E_F → n 映射 + Landau 扇图（R3）

**目的**：将理论 σ_xy(E_F) 转为实验可比的 σ_xy(n)，绘制 Landau 扇图。

```
步骤 3.1: DOS 积分 → n(E_F)
  优先用 calc_dos_diag(prim_cell, Nk=401) 得到 ρ(E)（确定性、高精度）
  n(E_F) = (4 / A_uc) · ∫_{E_Dirac}^{E_F} ρ(E) dE（因子 4 = 自旋×谷简并，A_uc ≈ 5.24 nm²）
  实现: src/sigma_utils.py → ef_to_density()
  注: Diag DOS 无随机噪声，可做极精细能量网格，精确映射 n(E_F)

步骤 3.2: σ_xy vs n
  映射 σ_xy(E_F) → σ_xy(n)
  输出: σ_xy(n) × 6 条 B 曲线
  横轴 n (10¹² cm⁻²)

步骤 3.3: Landau 扇图
  B = 2-45 T（密扫描，~10 个值）
  每条 B 曲线的 σ_xy 映射到 n 轴
  绘制 (n, B) 平面 σ_xy 颜色填充图
  验证: ν=6 台阶自低 B 起始终最宽（J=3 特征），对比 Zhang 2011 Fig.3
```

### 3.5 Phase 4：N=0 LL 单粒子结构验证 + 规范不变性（R4）

**目的**：验证 ABC trilayer 在磁场下的单粒子 LL 结构。Zhang 2012 预测的 Hund's rules 劈裂（spin→valley→layer）是 Coulomb 相互作用效应，**TBPM 单粒子计算无法复现**。本 Phase 聚焦单粒子可验证的内容：

1. N=0 LL 12 重简并（在 DOS 上体现为 12 个子峰结构，取决于磁场强度）
2. 规范不变性（同一物理量在不同 gauge 下必须一致）
3. 零场 Chern number ↔ B 场 σ_xy 的对应关系（带隙内量子化值一致）

```
步骤 4.1: 规范不变性检查
  同 B 下 gauge=0 和 gauge=1 的 σ_xy 和 DOS 一致

步骤 4.2: Chern number ↔ σ_xy 交叉验证
  Berry (diag, 零场) → C_v = ±3/2
  Kubo-Bastin (tbpm, B 场) → σ_xy 量子化值
  验证: 带隙内 σ_xy = C_v × e²/h

步骤 4.3: 与 Zhang 2011 实验数据定量比较
  数字化 Zhang 2011 Fig.2 (σ_xy vs V_g at B=18T) → 叠加对比
  σ_xy 平台位置偏差 < 10%
```

---

## 4. 系统架构规划（原 tbplas 路线 — 历史存档）

> ⚠️ 以下 §4–§10 为原计划的详细架构/接口/参数/文件结构/数据格式/交付物/风险/参考文献，
> 基于 tbplas 独用假设。Phase 4 复用前需将 `calc_hall_cond_tbpm` 替换为 quantum-kite 对应接口。
> 新的 quantum-kite 架构规划见 `plan_quantum_kite.md`（待创建）。

### 4.1 模块划分

```
MG/src/
├── main.py              [已有] 主调度，无需修改
├── model.py             [已有] 模型构建，无需修改
├── calc.py              [已有] 物理计算，无需修改
├── io_vis.py            [修改] 新增 plot_landau_fan()
├── sigma_utils.py       [新建] E_F↔n 映射 + 扇图数据准备
└── in.MG                [已有] LAMMPS 输入
```

### 4.2 新增模块职责

| 模块 | 职责 |
|------|------|
| `sigma_utils.py` | (1) `ef_to_density(energies, dos, E_Dirac)` → 从 DOS 积分得 n(E_F)；(2) `build_landau_fan_data(B_list, data_dir)` → 聚合所有 B 值的 σ_xy(n) 数据；(3) `plot_landau_fan(ax, B_list, n_grid, sigma_xy_2d)` → 扇图 |
| `io_vis.py`（新增函数） | `plot_conductivity_vs_n(n, sigma, prefix, B)` — σ_xy vs n 版本；`plot_sdH_combined(eng, sigma_xx, sigma_xy, prefix, B)` — σ_xx + σ_xy 叠加 |
| `configs/sigma_zhang2011.yaml` | Zhang 2011 实验复现参数 — B=2-45T 扫描 |
| `configs/sigma_zhang2012.yaml` | Zhang 2012 理论验证参数 — Berry curvature + valley Chern |
| `configs/sigma_converge.yaml` | 收敛性测试（m / kernel 扫描） |

---

## 5. 接口规范（计划）

### 5.1 `sigma_utils.py` 计划接口

| 函数 | 计划签名 | 功能说明 |
|------|---------|----------|
| `ef_to_density` | `(energies: np.ndarray, dos: np.ndarray, E_Dirac: float=0.0, area_per_uc: float=5.24) -> tuple[np.ndarray, np.ndarray]` | 从 DOS 积分得载流子浓度 vs 能量；返回 `(energies, n_cm2)`，浓度单位 cm⁻² |
| `remap_sigma_vs_n` | `(eng: np.ndarray, sigma: np.ndarray, eng_dos: np.ndarray, dos: np.ndarray, E_Dirac: float) -> tuple[np.ndarray, np.ndarray]` | 将 σ(E_F) 重新映射到 σ(n)；返回 `(n_values, sigma_vs_n)` |
| `build_landau_fan` | `(B_list: list[float], data_dir: str, cfg: dict) -> tuple[np.ndarray, np.ndarray, np.ndarray]` | 聚合所有 B 值的 σ_xy(n)；返回 `(B_grid, n_grid, sigma_xy_2d)` |
| `extract_landau_levels` | `(energies: np.ndarray, dos: np.ndarray, min_peak_height: float) -> np.ndarray` | 从 DOS 提取朗道能级位置；返回 LL 能量列表 |

### 5.2 `io_vis.py` 新增函数计划签名

| 函数 | 计划签名 | 功能说明 |
|------|---------|----------|
| `plot_conductivity_vs_n` | `(n_cm2: np.ndarray, sigma: np.ndarray, prefix: str, B: float, ylabel: str)` | 横轴为载流子浓度 cm⁻² 的电导率图 |
| `plot_landau_fan` | `(B_list: list, n_list: np.ndarray, sigma_2d: np.ndarray, prefix: str)` | 绘制 (n, B) 平面的 σ_xy 颜色填充图 |
| `plot_sdH_combined` | `(eng: np.ndarray, sigma_xx: np.ndarray, sigma_xy: np.ndarray, prefix: str, B: float)` | σ_xx(左轴) + σ_xy(右轴) 叠加图 |

---

## 6. 参数设计表

### 6.1 Zhang 2011 实验复现参数 (`sigma_zhang2011.yaml`)

```yaml
calc_type: "hall"               # 或 "dc" for SdH
solver_type: "tbpm"

model:
  num: 3
  stacking: "ABC"
  delta: 0.0                    # 主扫描: 0, 0.01, 0.03, 0.05 (位移场影响)
  B_values: [18.0]              # Fig.2 主数据 B=18T; 扫描: 2, 5, 10, 18, 30, 45
  gauge: 0

tbpm:
  rescale: 10.0
  rescale_center: 0.0           # ABC 三层半金属，费米能级在 0
  m: 256                        # 收敛后确认用 256 或升至 512
  rs: 1
  ts: 5000
  num_spin: 2
  algo: "cpu_fast"
  temperature: 1.0              # ⚠️ 低温解析 QHE 平台（默认 300K 会抹平 LL 结构）

hall:
  dckb_component: 2             # XY = Hall
  dimension: 2
  dckb_unit: "h"                # ⚠️ 输出 e²/h（默认 "hbar" → e²/ħ，差 2π 倍！）
  dckb_energies:
    min: -0.3                   # 覆盖中性点附近
    max: 0.3
    num: 401                    # 密网格分辨 J=3 chirality 台阶
  dckb_num_kernel: 2048
  dckb_num_integ_steps: 2048

dc:
  dc_cond_energy_limits: [[-0.5, 0.5]]
  dc_cond_num_time_steps: 1024  # DC 关联时间步数（需在 config_tbpm_solver 接入）

# 额外: DOS 计算参数（用于 E_F → n 映射）
dos_for_n_mapping:
  calc_type: "dos"
  solver_type: "diag"
  dos:
    Nk: 201
    energy_range: [-0.5, 0.5]
    energy_points: 1001
    sigma: 0.002
```

### 6.2 Zhang 2012 理论验证参数 (`sigma_zhang2012.yaml`)

```yaml
calc_type: "berry"              # 零场 Berry curvature + valley Chern
solver_type: "diag"

model:
  num: 3
  stacking: "ABC"
  delta: 0.016                  # 验证不同 delta 下的 C_v

berry:
  Nk: 2001
  bz_size: [2, 2, 1]
  method: "kubo"
  num_occ: 3                    # 3 条占据带
  K_frac: [0.6667, 0.3333, 0.0]
  ham_deriv_analytical: false
  ham_deriv_delta: 1.0e-6
```

### 6.3 收敛性测试参数 (`sigma_converge.yaml`)

```yaml
# m 扫描: m = [128, 256, 512]
# dckb_num_kernel 扫描: [1024, 2048, 4096]
# 固定: B=10 T, delta=0, stacking=ABC
# 判据: σ_xy 平台位置偏差 < 5% 认为收敛
```

### 6.4 关键参数选择依据

| 参数 | 推荐值 | 物理/数值依据 |
|------|--------|--------------|
| `m` | 256 | $B=10$T 时 m=256 含 ~800$\Phi_0$（tbplas-internals §10.4），LL 已可分辨；$B<5$T 时需 512+ |
| `ts` | 5000 | tbplas-internals §4：cpu_fast 下 ts > 4096 递推不稳定，5000 是安全上限 |
| `dckb_num_kernel` | 2048 | tbplas-internals §9.2 默认值；**注意** KPM Chebyshev 递推不稳定性随 kernel 阶数增加，不建议超过 4096 |
| `rescale` | 10.0 | 半带宽 ~6 eV（3 层 × 2 eV/层），10 > 6 安全 |
| `rescale_center` | 0.0 | ABC 三层无 gap 时费米能级在 0 |
| `num_spin` | 2 | 包含自旋简并 |
| `temperature` | **1.0 K** | ⚠️ 仅影响 Hall（Kubo-Bastin 中 Fermi-Dirac 展宽）；DC（`calc_corr_dc_cond`）**不受 temperature 影响**（tbplas-internals §11.4），σ_xx 锐利度由 `dc_cond_num_time_steps` 和 `rs` 控制 |
| `dckb_unit` | **"h"** | ⚠️ 必须显式设 e²/h；默认 "hbar" 输出 e²/ħ，与实验值差 2π ≈ 6.28 倍 |
| `dc_cond_num_time_steps` | 1024 | DC 关联时间步数，需在 `config_tbpm_solver` 中接入 `solver.config.dc_cond_num_time_steps` |

### 6.5 ⚠️ 运行前必须修复的代码缺陷

| 缺陷 | 文件 | 修复方案 |
|------|------|---------|
| **多 B 扫描磁场相位叠加** | `src/main.py:_run_hall`, `_run_dc` | B 循环内每次重新 `sample = expand_cell(prim_cell, m)` 再 `apply_magnetic_field`；当前代码对同一个 sample 重复叠加 Peierls 相位 |
| **dckb_unit 未传入 solver** | `src/calc.py:config_tbpm_solver` | 添加 `solver.config.dckb_unit = hall_cfg.get("dckb_unit", "h")` |
| **temperature 未传入 solver** | `src/calc.py:config_tbpm_solver` | 添加 `solver.config.temperature = tbpm_cfg.get("temperature", 1.0)` |
| **dc_cond_num_time_steps 未接入** | `src/calc.py:config_tbpm_solver` | 添加 `solver.config.dc_cond_num_time_steps = dc_cfg.get("dc_cond_num_time_steps", 1024)` |

---

## 7. 文件结构规划

```
MG/
├── configs/
│   ├── config.yaml                    [已有] 主配置
│   ├── sigma_zhang2011.yaml           [新建] Zhang 2011 实验复现参数
│   ├── sigma_zhang2012.yaml           [新建] Zhang 2012 理论验证参数
│   └── sigma_converge.yaml            [新建] 收敛性测试参数
├── src/
│   ├── sigma_utils.py                 [新建] E_F↔n 映射 + 扇图工具
│   └── io_vis.py                      [修改] 新增 3 个绘图函数
├── slurm/
│   └── sigma_batch.sh                 [新建] B/D 批量提交脚本
├── docs/
│   └── sigma/
│       ├── plan.md                    [本文档]
│       └── log.md                     [新建] 运行日志
├── runs/
│   └── sigma/                         [新建] 本次复现输出目录
│       ├── converge/                  m / kernel 收敛测试输出
│       ├── zhang2011/                 按 B 值分子目录
│       └── zhang2012/                 按 δ 值分子目录
└── figures/
    └── sigma/                         [新建] 复现图
```

---

## 8. 数据格式规范

### 8.1 电导率输出文件命名

```
sigma/{paper}/{stacking}_d{delta}_B{B}_{type}.txt

示例:
  sigma/zhang2011/ABC_d0.000_B18_hall.txt
  sigma/zhang2011/ABC_d0.030_B18_hall.txt
  sigma/zhang2011/ABC_d0.000_B12_dc.txt
  sigma/zhang2012/ABC_d0.016_berry.txt
```

### 8.2 文件列结构

```
# hall 输出 (2 列，空格分隔):
# E_F(eV)  sigma_xy(e²/h)
-0.300000  0.001234
-0.297000  0.001456
...

# dc 输出 (2 列):
# E(eV)  sigma_xx(e²/h)
-0.500000  0.000123
...

# DOS 输出 (2 列):
# E(eV)  DOS(1/eV)
-0.500000  0.001234
...

# n(E_F) 映射输出 (2 列):
# n(cm⁻²)  sigma_xy(e²/h)
-5.00e12  0.001234
...
```

### 8.3 图片输出

```
sigma/zhang2011/hall_ABC_d{delta}_B{B}.png
sigma/zhang2011/dc_ABC_d{delta}_B{B}.png
sigma/zhang2011/landau_fan_ABC.png
sigma/zhang2011/sdH_combined_ABC_B{B}.png
sigma/zhang2012/berry_ABC_d{delta}.png
```

---

## 9. 交付物清单

### 9.1 收敛性测试

| 编号 | 测试内容 | 参数 | 判据 |
|------|---------|------|------|
| C1 | m 收敛 | m=128,256,512; B=10T; D=0 | $\sigma_{xy}$ 平台位置偏差 < 5% |
| C2 | kernel 收敛 | dckb_num_kernel=1024,2048,4096 | 噪声 vs 精度平衡 |
| C3 | gauge 不变性 | gauge=0,1; 同 B,D | $\sigma_{xy}$ 和 DOS 一致 |

### 9.2 Zhang 2011 实验复现 (P1)

| 编号 | 计算内容 | B (T) | δ (eV) | 预期输出 |
|------|---------|-------|--------|---------|
| Z1 | 零场能带 + k³ 色散 | 0 | 0 | K 点 E ∝ k³（J=3 chirality 验证） |
| Z2 | σ_xy vs E_F (多 B) | 10,18,30,45 | 0 | 台阶 ν=±6,±10,±14,... |
| Z3 | σ_xy vs n (多 B) | 同上 | 0 | σ_xy(n) × 4 条 |
| Z4 | Landau 扇图 | 10-45 (密扫描) | 0 | (n,B) 平面 σ_xy 颜色图 |
| Z5 | σ_xx SdH | 10,18,30 | 0 | σ_xx(E) 振荡 → Berry phase 3π |
| Z6 | σ_xx + σ_xy 叠加 | 18 | 0 | 峰-平台对应，验证 J=3 chirality |
| Z7 | LL 能量 vs B^(3/2) | 10-45 | 0 | LL ∝ B^(3/2)，对比 J=1 ∝ B^(1/2), J=2 ∝ B¹ |
| Z8 | 与 Zhang 2011 Fig.2 定性比较 | 18 | 0 | 平台序列一致，台阶宽度定性吻合 |

### 9.3 Zhang 2012 理论验证 (P2)

| 编号 | 计算内容 | B (T) | δ (eV) | 预期输出 |
|------|---------|-------|--------|---------|
| ZT1 | 零场 Berry + Valley Chern | 0 | 0.016, 0.030 | $C_v = \pm 3/2 \cdot \mathrm{sgn}(\Delta)$ |
| ZT2 | 零场 LL 简并度 | 10,18,30 | 0 | N=0 LL 12 重简并（DOS 峰值计数） |
| ZT3 | 位移场下的能隙 | 0 | 0.01, 0.03, 0.05 | 能隙 ∝ Δ，验证层间偏压效果 |
| ZT4 | Dimer 带抵消验证 | 0 | 0.016 | $C_1+C_2 \approx 0$, $C_3 \approx \pm 1.5$（§8.11）|

---

## 10. 风险与缓解措施

| 风险 | 概率 | 影响 | 缓解措施 |
|------|:---:|------|---------|
| TBPM cpu_fast Chebyshev 递推不稳定导致 σ_xy 噪声大 | 中 | σ_xy 平台模糊 | ① 降 `dckb_num_kernel` 至 1024–2048（KPM Chebyshev 不稳定，非 ts）② 改用 `algo:cpu` ③ 增大 `dckb_num_integ_steps` |
| 低 B (< 10 T) 时 LL 分辨率不足 | 高 | 平台不可见 | ① 增大 m 到 512 ② 降 temperature 可锐化 Hall 平台（仅影响 Kubo-Bastin，不影响 DOS/DC）③ 承认 TBPM 对 <10T 的局限 |
| σ_xx DC 关联函数噪声大 | 中 | SdH 振荡模糊 | ① 增大 `dc_cond_num_time_steps` ② 增大 `rs` 多样本平均 |
| E_F → n 映射精度不够 | 低 | σ_xy(n) 横轴偏差 | ① 优先用 diag DOS（确定性、无噪声）② 验证 n=0 处 electron-hole 对称性 |
| 计算时间过长（m=512 + ts=5000） | 中 | 迭代变慢 | ① 先用 m=128 快速扫描 ② 只在关键参数用 m=512 ③ 所有生产级计算提交集群 h3clogin |

---

## 11. 参考文献

| 编号 | 引用 | 用途 |
|------|------|------|
| [G1] | J. H. García, L. Covaci, T. G. Rappoport, *Real-space calculation of the conductivity tensor for disordered topological matter*, Phys. Rev. Lett. **114**, 116602 (2015). | ⭐ **Phase 3 核心复现目标**：monolayer graphene QHE, KPM Kubo-Bastin, M=6144 |
| [G2] | **quantum-kite** — [https://github.com/quantum-kite](https://github.com/quantum-kite) | 🆕 **Phase 1–5 主计算引擎**：García 合作组的开源 KPM Kubo-Bastin 实现 |
| [P1] | L. Zhang, Y. Zhang, J. Camacho, M. Khodas, I. A. Zaliznyak, *The experimental observation of quantum Hall effect of l=3 chiral charge carriers in trilayer graphene*, Nature Physics **7**, 953–957 (2011). | ⭐ **Phase 4 核心复现目标**：ABC trilayer QHE, $\nu=\pm 6,\pm 10,\pm 14$, Landau 扇图 |
| [P2] | F. Zhang, D. Tilahun, A. H. MacDonald, *Hund's Rules for the N=0 Landau Levels of Trilayer Graphene*, Phys. Rev. B **85**, 165139 (2012). | Phase 4 理论验证：ABC trilayer N=0 LL 12 重简并 + Hund's rules |
| [R1] | M. Koshino & E. McCann, *Landau level spectra and the quantum Hall effect of multilayer graphene*, Phys. Rev. B **83**, 165443 (2011) | ABC trilayer k·p 有效模型 LL 能量公式 |
| [R2] | A. Kumar et al., *Integer Quantum Hall Effect in Trilayer Graphene*, Phys. Rev. Lett. **107**, 126806 (2011) | ABA + ABC trilayer IQHE 对比 |
| [R3] | `../references/02_kubo_bastin_deep_dive.md` | Kubo-Bastin C++ 核心深度解析（含有限 η 严格推导 §1.2.F + VBL Phase A–M 根因 §7） |
| [R4] | `shared/tbplas-internals.md` §8–§12 | tbplas Berry / Conductivity / Peierls / 基线偏移根因 |
| [R5] | `archive/plan_vbl_trace.md` | VBL Phase A–M 全 9 假说诊断（已完成, 根因确认） |
| [R6] | `plan_eta_kubo_bastin.md` | 有限 η Kubo-Bastin 计划（理论证伪, 路径废弃） |
