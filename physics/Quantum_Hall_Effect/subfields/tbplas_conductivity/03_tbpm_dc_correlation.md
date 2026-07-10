<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-07 15:02:52
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-07 15:02:53
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/03_tbpm_dc_correlation.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-07
 * @FilePath     : /home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/03_tbpm_dc_correlation.md
 * @Description  : TBPM DC 关联函数 — C++ 核心深度解析。覆盖完整调用链:
 *                 solver.h → tbpm.h → propagation.h → chebyshev.h → analysis.py
 * @References   :
 *   - TBPLaS CPC 2023 (Li et al.): Comp. Phys. Commun. 293, 108887
 *   - graphene note eqn.381 — DC conductivity formula
 *   - shared/tbplas-internals.md §9.3
 *   - 01_methods_reference.md §3
 *   - 02_kubo_bastin_deep_dive.md (对照 Kubo-Bastin Hall 路径)
 * @Source       : /home/wyl/tbplas/source/tbplas-cpp-a021ca8/sources/tbpm/
 *                 tbpm.h, solver.h, propagation.h, chebyshev.h, config.h
 *                 /home/wyl/tbplas/source/tbplas-py-2.0.1/tbplas/tbpm/
 *                 analysis.py, solver.py, io.py
-->

# TBPM DC 关联函数 — C++ 核心深度解析

> 源码基准：`/home/wyl/tbplas/source/tbplas-cpp-a021ca8/sources/tbpm/`
> 主文件：`tbpm.h`（`TBPMCPU::tbpm_dc_cond()`）、`solver.h`（`TBPMSolver::calc_corr_dc_cond()`）
> 辅助文件：`propagation.h`（`Propagator` + Bessel 表构建）、`chebyshev.h`（三项递推）、`config.h`（参数定义）
> Python 后处理：`analysis.py:352-440`（`Analyzer.calc_dc_cond()`）、`io.py:110-141`（`load_corr_dc_cond()`）

---

## 1. 物理问题与定位

### 1.1 回答什么问题

TBPM DC 关联函数法计算**能量分辨的纵向 DC 电导率** $\sigma_{xx}(E)$ 和 $\sigma_{yy}(E)$：

> "能量为 $E$ 的那些电子态，对直流导电的贡献有多大？"

典型用途：
- 分析能带结构中哪些能量区域是「导电通道」，哪些是「绝缘区」
- 带隙内 $\sigma_{xx}(E) \approx 0$（绝缘），扩展态区域 $\sigma_{xx}(E)$ 取峰值

### 1.2 与其他方法的对比定位

| 方法 | 输出 | 横轴 | 能否直接与 QHE 实验叠图 |
|------|------|------|:---:|
| **TBPM DC 关联函数** (本文) | $\sigma_{xx}(E)$, $\sigma_{yy}(E)$ | 电子能量 $E$ | ❌ |
| **Kubo-Bastin Hall**（`02_kubo_bastin_deep_dive.md`）| $\sigma_{xy}(\mu)$ | 化学势 $\mu$ | ✅ |
| **TBPM AC 关联函数** | $\sigma_{\alpha\beta}(\omega)$ | 频率 $\omega$ | N/A（光谱） |

> ⚠️ **关键限制**：DC 关联函数输出 $\sigma_{xx}(E)$（横轴 = 电子能量 $E$），而 QHE 实验测量 $\sigma_{xx}(V_g)$（横轴 = 栅极电压 $\propto$ 化学势 $\mu$）。两者横轴不同，**不能直接与实验叠图**。若需实验可比的 $\sigma_{xx}(\mu)$，应使用 Kubo-Bastin 方法设 `dckb_component=1`。

### 1.3 方法本质：两步法

1. **C++ 层**：随机波函数传播 → 准本征态投影 → DC 关联函数 $C(E,t)$
2. **Python 层**：关联函数傅里叶积分 + 窗函数 → $\sigma_{xx}(E)$

---

## 2. 数学公式

### 2.1 Kubo-Greenwood 公式的随机波函数形式

直流（$\omega \to 0$）极限下，Kubo 公式的随机波函数实现（CPC 论文 eqn.53 的 DC 极限）：

$$\sigma_{\alpha\alpha}(E) = \frac{N_\text{orb}}{\Omega} \cdot \text{DOS}(E) \cdot \int_0^\infty \text{Re}\big[e^{-iEt}\,C_{\alpha\alpha}(E,t)\big]\,dt$$

其中 DC 关联函数（C++ 实际计算量）：

$$C_{\alpha\alpha}(E,t) = \frac{\langle \exp(-iHt)\,j_\alpha|\psi_0\rangle \;|\; j_\alpha|\psi(E)\rangle}{\big|\langle\psi_0|\psi(E)\rangle\big|}$$

符号说明：
- $|\psi_0\rangle$：随机初始态（复球面均匀分布，Haar 测度）
- $|\psi(E)\rangle$：准本征态（quasi-eigenstate），通过传播子 FFT 构建
- $j_\alpha$：电流算符（$\alpha = x, y$）
- $H$：缩放到 $[-1, 1]$ 的哈密顿量
- $\exp(-iHt)$：时间演化算符（Chebyshev 展开实现）
- $\Omega$：体系面积（2D）或体积（3D）
- $N_\text{orb}$：轨道总数

### 2.2 准本征态的构造

准本征态是能量 $E$ 附近的近似本征态，通过时间演化的傅里叶变换构建：

$$|\psi(E)\rangle = \sum_{t=0}^{N_t-1} w_t^{\text{Hanning}} \cdot \big(e^{+iEt}|\psi_0(t)\rangle + e^{-iEt}|\psi_0(-t)\rangle\big)$$

其中 $|\psi_0(\pm t)\rangle = \exp(\mp iHt)|\psi_0\rangle$，$w_t^{\text{Hanning}}$ 是 Hanning 窗函数。

构造完成后做归一化：$|\psi(E)\rangle \leftarrow |\psi(E)\rangle / \||\psi(E)\rangle\|$。

### 2.3 数值离散化（Python Analyzer 实际执行）

$$\sigma_{xx}(E) = \frac{N_\text{orb}}{\Omega} \cdot \Delta t \cdot \text{DOS}(E) \cdot \sum_{k=0}^{N_t^{dc}-1} w_k^{\text{exp}} \cdot \text{Re}\big[e^{-iE t_k} \cdot C_{xx}(E, t_k)\big]$$

其中：
- $\Delta t = 2\pi / E_\text{range}$（缩放时间步长）
- $t_k = k \cdot \Delta t$
- $w_k^{\text{exp}} = \exp(-2(k/N_t^{dc})^2)$（默认指数窗，`window_exp`）
- $N_t^{dc} =$ `dc_cond_num_time_steps`（默认 1024）

### 2.4 单位分析

| 量 | 单位 | 来源 |
|---|------|------|
| `corr_dc` (C++ 输出) | $e^2/\hbar^2 \cdot (\text{eV})^2 \cdot \text{nm}^2$ | 电流算符 $j_\alpha$ 平方量纲 |
| $\text{DOS}(E)$ | $1/\text{eV}$ | 态密度 |
| $\sigma_{xx}$ | $e^2/\hbar$（2D） | 与 Lindhard 和 Kubo-Bastin 一致 |

验证（2D）：
$$[\sigma] = [N_\text{orb}/\Omega] \cdot [\Delta t] \cdot [\text{DOS}] \cdot [C] = \frac{1}{\text{nm}^2} \cdot \frac{\hbar}{\text{eV}} \cdot \frac{1}{\text{eV}} \cdot \frac{e^2}{\hbar^2}(\text{eV})^2\,\text{nm}^2 = \frac{e^2}{\hbar}$$

---

## 3. C++ 核心实现 — 完整调用链

### 3.1 调用链全景

```
Python: solver.calc_corr_dc_cond()                       [solver.py:207-219]
  └── C++: TBPMSolver::calc_corr_dc_cond()               [solver.h:499-576]
        ├── model_->build_ham_curr_csr()                  构建 H + j_x + j_y
        ├── rescale_ham()                                 缩放 H 到 [-1, 1]
        ├── 确定准本征态能量网格 qe_energies               从 dc_cond_energy_limits 筛选
        ├── backend->tbpm_dc_cond(...)          ──────── [tbpm.h:433-531]
        │     ├── tbpm_qe_dos()                  ──────── [tbpm.h:49-112]
        │     │     ├── Propagator::act()         ──────── [propagation.h:402-407]
        │     │     │     └── cheb_eval_wf()      ──────── [chebyshev.h:53-97]
        │     │     └── FFT 累加 → |ψ(E)⟩ + corr_dos
        │     ├── 投影因子: factor[E] = |⟨ψ₀|ψ(E)⟩|
        │     ├── 电流注入: j_x|ψ₀⟩, j_y|ψ₀⟩, j_x|ψ(E)⟩, j_y|ψ(E)⟩
        │     └── 时间演化 + 关联函数累加
        ├── MPI Allreduce 平均
        └── 保存 corr_dos, corr_dc_xx, corr_dc_yy 到文件

Python: Analyzer.calc_dc_cond()                          [analysis.py:352-440]
  ├── 从 corr_dos FFT → DOS(E)
  ├── get_qe_indices() → 筛选准本征态能量索引
  └── 对每个 E: 傅里叶积分 → σ_{xx}(E), σ_{yy}(E)
```

### 3.2 入口：`TBPMSolver::calc_corr_dc_cond()`（`solver.h:499-576`）

```cpp
void calc_corr_dc_cond()
{
    // 1. 构建 Hamiltonian + 电流算符 CSR 矩阵
    model_->build_ham_curr_csr(indptr_, indices_, ham_,
                                curr_coeff_x_, curr_coeff_y_);
    rescale_ham();

    // 2. 确定准本征态能量网格
    //    从 DOS 全能量网格 (2*num_steps 个点) 中
    //    筛选落在 dc_cond_energy_limits 范围内的能量 → qe_energies
    int num_steps = config.num_time_steps;
    int num_eng = 2 * num_steps;
    double eng_range = get_energy_range();
    Eigen::VectorXd dos_eng(num_eng);
    for (int i = 0; i < num_eng; ++i) {
        dos_eng[i] = rescale_params_.center + 0.5 * eng_range * (i*1.0/num_steps - 1.0);
    }
    // 筛选 → meta.qe_energies（已减 rescale_params_.center）

    // 3. 调用后端计算
    backend->tbpm_dc_cond(h_sparse, curr_x, curr_y, config, meta,
                           corr_dos, corr_dc_xx, corr_dc_yy);

    // 4. MPI 平均 + 保存文件
}
```

**关键细节**：
- 准本征态能量网格从 DOS 全能量网格中按 `dc_cond_energy_limits` 筛选，**不是**独立的能量采样
- `qe_energies` 存储的是**缩放后的能量**（已减 `rescale_params_.center`），因为后续 Chebyshev 展开在缩放空间工作
- `corr_dos` 的长度是 `num_steps`（不含 t=0），不是 `num_steps+1` — Python 侧需要 `insert(0, 1.0)`

### 3.3 核心：`TBPMCPU::tbpm_dc_cond()`（`tbpm.h:433-531`）

```cpp
void tbpm_dc_cond(
    const sparse_t& h_sparse,
    const sparse_t& curr_x,    // j_x CSR 矩阵
    const sparse_t& curr_y,    // j_y CSR 矩阵
    const TBPMConfig& config,
    const TBPMMeta& meta,
    Eigen::VectorXcd& corr_dos,
    Eigen::MatrixXcd& corr_dc_xx,   // (num_energies, num_steps_dc)
    Eigen::MatrixXcd& corr_dc_yy)   // (num_energies, num_steps_dc)
{
    // === 初始化 ===
    size_t n_wf = h_sparse.get_dim();
    Eigen::VectorXcd wf0(n_wf);        // |ψ₀⟩
    Eigen::VectorXcd psi0_x(n_wf);     // j_x|ψ₀⟩
    Eigen::VectorXcd psi0_y(n_wf);     // j_y|ψ₀⟩

    size_t num_energies = meta.qe_energies.size();
    std::vector<Eigen::VectorXcd> wf_qe;   // |ψ(E)⟩，后续被 j_x|ψ(E)⟩ 覆盖
    std::vector<Eigen::VectorXcd> psi2_y;  // j_y|ψ(E)⟩
    Eigen::VectorXcd buffer(n_wf);         // j_x|ψ(E)⟩ 临时缓冲

    int num_steps_dos = config.num_time_steps;
    int num_steps_dc  = config.dc_cond_num_time_steps;

    Propagator<sparse_t> propagator(h_sparse, config, meta);
    RandomGenerator rand_gen(config.seed, config.random_method);

    // === 主循环：对每个随机样本 ===
    for (int i_sample = 1; i_sample <= num_samples; ++i_sample) {
        // Step A: 随机初始态
        rand_gen.random_state(wf0, seed_i);

        // Step B: 构造准本征态 |ψ(E)⟩ 和 corr_dos
        //   tbpm_qe_dos() 内部执行:
        //     ① 正/反向传播 |ψ₀(±t)⟩ = exp(∓iHt)|ψ₀⟩ (via Propagator::act)
        //     ② Hanning 窗加权 FFT → |ψ(E)⟩ = Σ_t w_t·(e^{+iEt}|ψ₀(t)⟩+e^{-iEt}|ψ₀(-t)⟩)
        //     ③ 归一化: |ψ(E)⟩ ← |ψ(E)⟩ / ‖|ψ(E)⟩‖
        //     ④ corr_dos[t] = ⟨ψ₀|ψ₀(t)⟩
        tbpm_qe_dos(propagator, config, meta, true, wf0, wf_qe, corr_dos_work);

        // Step C: 投影因子
        for (size_t i_e = 0; i_e < num_energies; ++i_e) {
            factor[i_e] = std::abs(vec_dot(wf0, wf_qe[i_e]));
        }

        // Step D: 电流注入
        //   psi0_x = j_x|ψ₀⟩, psi0_y = j_y|ψ₀⟩
        //   psi2_y[i_e] = j_y|ψ(E_i)⟩
        //   wf_qe[i_e] 被 j_x|ψ(E_i)⟩ 覆盖 (= psi2_x[i_e])
        curr_x.mv(wf0, psi0_x);
        curr_y.mv(wf0, psi0_y);
        for (size_t i_e = 0; i_e < num_energies; ++i_e) {
            curr_y.mv(wf_qe[i_e], psi2_y[i_e]);
            curr_x.mv(wf_qe[i_e], buffer);
            vec_copy(buffer, wf_qe[i_e]);  // wf_qe → psi2_x
        }

        // Step E: t=0 关联函数
        for (size_t i_e = 0; i_e < num_energies; ++i_e) {
            corr_dc_xx(i_e, 0) += vec_dot(psi0_x, psi2_x[i_e]) / factor[i_e];
            corr_dc_yy(i_e, 0) += vec_dot(psi0_y, psi2_y[i_e]) / factor[i_e];
        }

        // Step F: 时间演化 → 各时间步关联函数
        //   i_step 从 2 到 num_steps_dc（对应 j = 1 到 num_steps_dc-1）
        //   NOTE: 最大时间步 = num_steps_dc - 1，与 DOS 路径不同
        for (int i_step = 2; i_step <= num_steps_dc; ++i_step) {
            propagator.act(psi0_x, true);  // psi0_x ← exp(-iHΔt)·j_x|ψ₀⟩
            propagator.act(psi0_y, true);  // psi0_y ← exp(-iHΔt)·j_y|ψ₀⟩
            int j = i_step - 1;
            for (size_t i_e = 0; i_e < num_energies; ++i_e) {
                corr_dc_xx(i_e, j) += vec_dot(psi0_x, psi2_x[i_e]) / factor[i_e];
                corr_dc_yy(i_e, j) += vec_dot(psi0_y, psi2_y[i_e]) / factor[i_e];
            }
        }
    }

    // === 样本平均 ===
    corr_dos  /= static_cast<double>(num_samples);
    corr_dc_xx /= static_cast<double>(num_samples);
    corr_dc_yy /= static_cast<double>(num_samples);
}
```

### 3.4 准本征态构造：`tbpm_qe_dos()`（`tbpm.h:49-112`）

这是 DC 关联函数最关键的子程序。核心算法：

```
输入: propagator (预构建 Bessel 表), config, wf0 (初始态 |ψ₀⟩)
输出: wfq (准本征态 |ψ(E)⟩，逐能量归一化), corr_dos (DOS 关联函数)

算法:
1. 初始化 wf_t_pos = wf_t_neg = wf0
2. 初始化 wfq[i_e] = wf0 (t=0 贡献)
3. for i_step = 1 to num_steps:
   a. Propagator::act(wf_t_pos, forward=true)   → |ψ₀(+t)⟩ = exp(-iHΔt)·|ψ₀(+t-Δt)⟩
   b. Propagator::act(wf_t_neg, forward=false)  → |ψ₀(-t)⟩ = exp(+iHΔt)·|ψ₀(-t+Δt)⟩
   c. Hanning 窗: window = 0.5*(1+cos(π*i_step/num_steps))
   d. 对每个能量 i_e:
      phase = qe_energies[i_e] * i_step * time_step
      factor = exp(+i*phase) * window   (正时间贡献)
      factor_conj = exp(-i*phase) * window (负时间贡献)
      wfq[i_e] += factor * wf_t_pos + factor_conj * wf_t_neg
   e. corr_dos[i_step-1] += ⟨wf0|wf_t_pos⟩
4. 归一化: 对每个 wfq[i_e], wfq[i_e] /= ||wfq[i_e]||
```

**数学解释**：准本征态是时间演化波函数的能量投影：

$$|\psi(E)\rangle = |\psi_0\rangle + \sum_{t=1}^{N_t-1} w_t^{\text{Hanning}} \cdot \big(e^{+iEt} e^{-iHt} + e^{-iEt} e^{+iHt}\big) |\psi_0\rangle$$

这等效于对传播子做窗口傅里叶变换（Hanning 窗抑制 Gibbs 振荡）。

### 3.5 时间演化：`Propagator::act()`（`propagation.h:402-407`）

```cpp
void act(Eigen::VectorXcd& wf_in, bool forward = true)
{
    const Eigen::VectorXcd* bes = forward ? &bes_forward_ : &bes_backward_;
    cheb_eval_wf(h_sparse_, *bes, wf_in, t0_, t1_, wf_out_);
    vec_copy(wf_out_, wf_in);
}
```

**波函数时间演化的 Chebyshev 实现**：

$$|\psi(t)\rangle = e^{-iHt}|\psi(0)\rangle = \sum_{n=0}^{\infty} c_n(t) \cdot T_n(\tilde{H})|\psi(0)\rangle$$

在缩放空间 $\tilde{H} \in [-1, 1]$：

$$c_n(t) = 2 \cdot (-i)^n \cdot J_n(t \cdot \Delta E / 2) \quad (n \ge 1), \quad c_0 = (-i)^0 \cdot J_0(t \cdot \Delta E / 2)$$

其中 $J_n$ 是第一类 Bessel 函数。Bessel 系数预计算为 `bes_forward_` / `bes_backward_` 向量。

**Chebyshev 三项递推**（`chebyshev.h:53-97`）：

```
|t₀⟩ = H̃|ψ_in⟩
|t₁⟩ = 2H̃|t₀⟩ - |ψ_in⟩
|ψ_out⟩ = coeff[0]·|ψ_in⟩ + coeff[1]·|t₀⟩ + coeff[2]·|t₁⟩
for n = 3; n < num_series; ++n:
    |t₂⟩ = 2H̃|t₁⟩ - |t₀⟩   // 三项递推
    |ψ_out⟩ += coeff[n]·|t₂⟩
    rotate: t₀ ← t₁, t₁ ← t₂
```

**⚠️ 数值稳定性**：
- 普通 `cpu` 算法每步只用 ~4 阶 Chebyshev 矩 → 三项递推步数少，稳定
- `cpu_fast` 算法一次性算所有 Chebyshev 矩，高阶矩噪声可能累积 → **不建议** DC 关联函数使用 `cpu_fast`（与 DOS/LDOS 的结论一致，见 `tbplas-internals.md` §4）
- DC 关联函数**不使用** `cpu_fast` 路径的恒等式技巧（`cheb_eval_mu_dos`），而是逐时间步独立调用 `cheb_eval_wf`，因此 Chebyshev 阶数由 Bessel 级数截断（`bessel_precision`，默认 1e-14）决定，通常仅需 ~10-20 阶，数值稳定

### 3.6 投影因子的作用

$$C(E,t) = \frac{\langle e^{-iHt} j_x \psi_0 | j_x \psi(E) \rangle}{|\langle \psi_0 | \psi(E) \rangle|}$$

除以 $|\langle\psi_0|\psi(E)\rangle|$ 是为了**去除随机初始态在能量 $E$ 上的投影权重差异**。不同随机态 $|\psi_0\rangle$ 在准本征态 $|\psi(E)\rangle$ 上的投影幅度不同，该因子确保关联函数不受初始态随机性的影响。

> 注意：`factor[i_e]` 取的是**绝对值** `std::abs(vec_dot(wf0, wf_qe[i_e]))`，原因：关联函数 $C(E,t)$ 本身还需要在最后做傅里叶积分时取实部，相位的全局旋转不影响最终物理量。

---

## 4. Python 后处理 — `Analyzer.calc_dc_cond()`

### 4.1 完整流程（`analysis.py:352-440`）

```python
def calc_dc_cond(self, corr_dos, corr_dc,
                 window_dos=window_hanning, window_dc=window_exp):
    # Step 1: 插入 t=0 关联函数值 (1.0)
    corr_dos = np.insert(corr_dos, 0, 1.0)

    # Step 2: 从 corr_dos 计算 DOS(E) — 标准 TBPM DOS 流程
    energies_dos, dos = self.calc_dos(corr_dos, window_dos)
    #   calc_dos 内部:
    #     ① 构造负时间关联函数（利用 C(-t) = C*(t)）
    #     ② IFFT → DOS(E)（未归一化）
    #     ③ 归一化: dos /= sum(dos) * en_step
    #     ④ 乘以自旋简并度

    # Step 3: 获取参数
    tnr_dc = self._info.dc_cond_num_time_steps   # DC 时间步数
    en_range = self._info.energy_range             # 全能量范围 (eV)
    t_step = 2 * pi / en_range                     # 缩放时间步长
    qe_indices = get_qe_indices(self._info, energies_dos)  # 准本征态能量索引

    # Step 4: 对每个准本征态能量做傅里叶积分
    energies = energies_dos[qe_indices]
    dc_prefactor = num_orbitals / lattice_area       # 2D
    # dc_prefactor = num_orbitals / lattice_volume   # 3D
    dc = np.zeros((2, n_energies))

    for i in range(2):         # xx, yy
        for j in range(n_energies):
            en = energies[j]
            dos_val = dos[qe_indices[j]]
            dc_val = 0.0
            for k in range(tnr_dc):
                w = window_dc(k+1, tnr_dc)          # 窗函数
                phi = k * t_step * en
                c_exp = cos(phi) - 1j*sin(phi)
                dc_val += w * (c_exp * corr_dc[i,j,k]).real
            dc[i,j] = dc_prefactor * t_step * dos_val * dc_val

    # Step 5: 自旋修正
    dc *= num_spin
    return energies, dc
```

### 4.2 窗函数

DC 关联函数的傅里叶积分使用 **指数窗**（`window_exp`）：

$$w_k = \exp\!\left[-2\left(\frac{k}{N_t^{dc}}\right)^2\right]$$

与此对比，DOS 计算使用 **Hanning 窗**（`window_hanning`）：

$$w_k = \frac{1}{2}\left[1 + \cos\!\left(\frac{\pi k}{N_t}\right)\right]$$

**为什么使用不同的窗函数？**
- DC 关联函数在长时极限（$t \to \infty$）会因数值噪声偏离真实值，指数窗在 $t \approx N_t^{dc}$ 时接近 0，有效抑制长时噪声
- DOS 关联函数是能量域的 $\delta$-函数卷积，Hanning 窗提供更平滑的展宽

### 4.3 `corr_dos` 的微妙差异

| 来源 | 长度 | t=0 值 |
|------|------|--------|
| `calc_corr_dos()` (独立 DOS) | `num_steps + 1` | `corr_dos[0] = 1.0` |
| `calc_corr_dc_cond()` (附带 DOS) | `num_steps` | **缺失！**需 Python 侧 `insert(0, 1.0)` |

这是 C++ 源码未统一更新的历史遗留问题。`tbpm_dos` 和 `tbpm_ldos` 已更新为 `num_steps + 1` 格式，但 `tbpm_dc_cond` 中附带的 `corr_dos` 仍为 `num_steps` 格式。Python `Analyzer.calc_dc_cond()` 在内部处理了这个差异。

---

## 5. 数据结构与 I/O

### 5.1 输出文件

| 文件 | 维度 | 格式 |
|------|------|------|
| `{prefix}_corr_dc_cond_dos.dat` | `(num_steps, 2)` | 每行: `Re(corr_dos[t])  Im(corr_dos[t])` |
| `{prefix}_corr_dc_cond_xx.dat` | `(num_energies, 2*num_steps_dc)` | 每行: `(Re(C_xx[t₀]), Im(C_xx[t₀])), (Re(C_xx[t₁]), Im(C_xx[t₁])), ...` |
| `{prefix}_corr_dc_cond_yy.dat` | `(num_energies, 2*num_steps_dc)` | 同上，yy 分量 |
| 或 `{prefix}_tbpm.h5` (HDF5) | datasets: `corr_dc_cond.dos`, `corr_dc_cond.xx`, `corr_dc_cond.yy` | HDF5 格式 |

### 5.2 Python 加载（`io.py:110-141`）

```python
corr_dos, corr_dc_cond = load_corr_dc_cond(prefix)
# corr_dos:     (num_steps,) complex128
# corr_dc_cond: (2, num_energies, num_steps_dc) complex128
#              维度0: xx(0), yy(1)
#              维度1: 准本征态能量索引
#              维度2: DC 时间步
```

### 5.3 数据流图

```
┌─────────────────────────────────────────────────────────┐
│                    C++ 层                                │
│                                                         │
│  config.dc_cond_energy_limits ──→ qe_energies (N_e个)    │
│  config.num_time_steps        ──→ num_steps_dos    (N_d) │
│  config.dc_cond_num_time_steps ──→ num_steps_dc    (M)   │
│                                                         │
│  输出:                                                   │
│    corr_dos:  (N_d,)       complex                      │
│    corr_dc_xx: (N_e, M)    complex                      │
│    corr_dc_yy: (N_e, M)    complex                      │
└──────────────────────┬──────────────────────────────────┘
                       │ 文件 I/O
┌──────────────────────▼──────────────────────────────────┐
│                   Python 层                              │
│                                                         │
│  load_corr_dc_cond() → corr_dos, corr_dc (2,N_e,M)     │
│  Analyzer.calc_dc_cond():                               │
│    ① corr_dos → FFT → DOS(E)  (2*N_d 个能量点)          │
│    ② get_qe_indices() → 筛选出 N_e 个准本征态能量索引    │
│    ③ 对每个 E_i:                                        │
│       σ(E_i) = prefactor * Δt * DOS(E_i)               │
│               * Σ_k w_k · Re[e^{-iE_i t_k}·C(E_i,t_k)] │
│                                                         │
│  输出:                                                   │
│    energies: (N_e,)     float — 电子能量 (eV)            │
│    dc:       (2, N_e)   float — σ_xx, σ_yy (e²/h)      │
└─────────────────────────────────────────────────────────┘
```

---

## 6. 关键参数表

### 6.1 C++ 配置参数（`config.h`）

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `dc_cond_energy_limits` | `[(-0.5, 0.5)]` | 能量窗口列表 `[(E_min,E_max), ...]` (eV)。准本征态能量从此窗口筛选 |
| `dc_cond_num_time_steps` | 1024 | DC 关联函数时间步数 $M$。控制傅里叶积分的精度和长时噪声 |
| `num_time_steps` | 1024 | DOS/准本征态的时间步数 $N_d$。控制能量分辨率 $\Delta E \approx E_\text{range} / (2N_d)$ |
| `dc_method` | `"cheby_poly"` | 准本征态算法：`"cheby_poly"`（Chebyshev 多项式展开）或 `"block_time"`（分块时间演化） |
| `bessel_precision` | $10^{-14}$ | Bessel 级数截断精度。控制 Chebyshev 展开阶数 |
| `num_random_samples` | 1 | 随机样本数（`rs`）。每个样本使用不同的随机初始态 |
| `seed` | 1337 | 随机种子 |
| `temperature` | 300.0 | 温度 (K)。DC 关联函数法在零温下定义，此参数仅影响 Fermi-Dirac 相关路径 |

### 6.2 Python Analyzer 参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `window_dos` | `window_hanning` | DOS FFT 窗函数 |
| `window_dc` | `window_exp` | DC 关联函数傅里叶积分窗函数 |

### 6.3 参数调优建议

| 场景 | 建议 |
|------|------|
| 提高能量分辨率 | 增大 `num_time_steps`（如 2048 或 4096），注意避免 `cpu_fast` 的 Chebyshev 递推不稳定性 |
| 更精细的能量窗口 | 调整 `dc_cond_energy_limits`，例如 `[(-1.0, -0.5), (0.0, 0.5)]` |
| 减少长时噪声 | 增大 `dc_cond_num_time_steps` 但配合更强的窗函数；或保持默认 1024 |
| 改善随机平均 | 增大 `num_random_samples`（如 4 或 8） |

### 6.4 `num_time_steps` 与 `dc_cond_num_time_steps` 的深度区分

这两个参数虽然都叫"时间步数"，但在 DC 关联函数中控制**完全不同的轴**，且代码中刻意做了区分。

#### 6.4.1 各司其职

```
num_time_steps (N_t)                      dc_cond_num_time_steps (M)
═══════════════════════                    ════════════════════════════
控制：能量轴                                控制：时间轴（关联函数）
用在哪：tbpm_qe_dos() 的循环边界            用在哪：tbpm_dc_cond() 的传播循环
影响：准本征态 |ψ(E)⟩ 的构造质量             影响：C(E,t) 傅里叶积分的截断精度
输出：corr_dos (长度 N_t)                   输出：corr_dc (维度 N_e × M)
```

#### 6.4.2 代码层面的隔离证据

源码中有两处明确注释表明开发者**有意区分**两者：

> `tbpm.h:76` — `// i_step from 1 to num_steps, it is different from DC and AC cond.`

> `tbpm.h:513-514` — `// NOTE: i_step is from 2 to num_steps_dc, i.e. the maximum of num_step is num_steps_dc - 1 NOT num_steps_dc. This is different from DOS.`

两套循环使用不同的变量名（`num_steps` vs `num_steps_dc`），不同的起止索引，不同的 `Propagator` 调用模式——说明它们是两个独立子系统。

#### 6.4.3 各自对结果的影响机制

**`num_time_steps`（能量轴）：**

| 增大 $N_t$ 的效果 | 机制 |
|:---|:---|
| 能量分辨率提高 | $\Delta E = E_\text{range} / (2N_t)$ ↓，DOS 全网格从 $2N_t$ 个点加密 |
| 准本征态点数增多 | $N_e$ ∝ 落在 `dc_cond_energy_limits` 内的网格点数，$N_t$ 翻倍 ≈ $N_e$ 翻倍 |
| 准本征态 FFT 质量提高 | Hanning 窗加权累加项数 $= N_t$，越多越接近连续傅里叶极限 |
| $\sigma_{xx}(E)$ 曲线更平滑 | 能量轴上采样更密 → 曲线插值更可靠 |
| 计算量线性增长 | $O(N_t \cdot B \cdot N_\text{orb})$，$B \sim 10{-}20$ |
| ⚠️ `cpu_fast` 风险 | 若使用 `cpu_fast`，$N_t$ 大时 Chebyshev 高阶矩噪声累积（但 DC 路径默认 `cpu`，安全） |

**`dc_cond_num_time_steps`（时间轴）：**

| 增大 $M$ 的效果 | 机制 |
|:---|:---|
| 傅里叶积分截断更晚 | $t_{\max} = (M-1) \cdot \Delta t$ ↑，$\Delta t = 2\pi/E_\text{range}$ |
| 能量域旁瓣抑制更好 | 有限时间截断 → 能量域 sinc 卷积 → $M$ 越大卷积核越窄 |
| ⚠️ 长时噪声风险 | 传播子累积误差 $\propto$ 步数，$C(E, t \gg 0)$ 信噪比下降 |
| 窗函数自动缓解 | `window_exp` 在 $k \to M$ 时 $\to 0$，抑制晚期噪声贡献 |
| 计算量线性增长 | $O(M \cdot B \cdot N_\text{orb})$，仅对 2 个波函数（`psi0_x`, `psi0_y`）传播 |

#### 6.4.4 独立性说明

两者**几乎完全解耦**——唯一的共享资源是 `Propagator` 实例（共用同一个缩放 $H$ 和 Bessel 系数），但各自独立调用 `Propagator::act()`，互不干扰。

实用含义：可以自由组合——
- **高能分辨 + 粗时域积分**：大 $N_t$ + 小 $M$（适合需要密集能量采样但不在意长时行为的场景）
- **粗能扫描 + 精细时域积分**：小 $N_t$ + 大 $M$（适合只需少数能量点但要求高精度的场景）
- **同时放大**：$N_t$ 和 $M$ 都大 → 计算时间 = 两者之和（非乘积），仍比 Kubo-Bastin 的 $O(M^2)$ 便宜

#### 6.4.5 对照表

| 维度 | `num_time_steps` ($N_t$) | `dc_cond_num_time_steps` ($M$) |
|------|--------------------------|--------------------------------|
| 默认值 | 1024 | 1024 |
| 循环起止 | `i_step = 1` 到 `N_t` | `i_step = 2` 到 `M` |
| 传播对象 | $\vert\psi_0(\pm t)\rangle$（正反向各一个） | $j_x\vert\psi_0\rangle$, $j_y\vert\psi_0\rangle$（两个） |
| 窗函数 | `window_hanning`（硬编码在 C++ 中） | `window_exp`（Python 侧可替换） |
| 输出维度 | `corr_dos`: `(N_t,)` | `corr_dc`: `(N_e, M)` |
| t=0 的处理 | 不包含（`corr_dos[0]` 对应 $t=\Delta t$） | 包含（`corr_dc[*,0]` 对应 $t=0$，无传播） |
| 过大时的风险 | `cpu_fast` 三项递推不稳定（DC 路径不受影响） | 长时噪声累积（被窗函数抑制） |
| 过小时的后果 | 能量分辨率不足，可能漏掉窄谱特征 | 傅里叶截断过早，$\sigma_{xx}(E)$ 人工展宽 |

---

## 7. 计算复杂度

对每个随机样本：

| 操作 | 复杂度 | 说明 |
|------|--------|------|
| 准本征态构造 | $O(N_d \cdot B \cdot N_\text{orb})$ | $N_d$ = `num_time_steps`，$B$ = Bessel 级数长度 (~10-20)，每步一次 `cheb_eval_wf` |
| 电流注入 | $O(N_e \cdot N_\text{orb})$ | 稀疏矩阵-向量乘法，$N_e$ = `num_energies` |
| DC 关联函数传播 | $O(M \cdot B \cdot N_\text{orb})$ | $M$ = `dc_cond_num_time_steps`，每次只对 2 个波函数传播 |
| 内积 | $O(M \cdot N_e \cdot N_\text{orb})$ | 每个时间步、每个能量做 2 次 `vec_dot` |

总复杂度 ≈ $O\big(N_d \cdot B \cdot N_\text{orb} + M \cdot N_e \cdot N_\text{orb}\big)$

与 Kubo-Bastin 的 $O(M^2 \cdot N_\text{orb} \cdot N_\theta)$ 相比，DC 关联函数法在大的 $M$（Chebyshev 阶数）时**明显更便宜**，因为它不需要 $\Gamma_{mn}(\theta)$ 矩阵的 $O(M^2)$ 双重求和。

---

## 8. 与 Kubo-Bastin Hall 方法的核心差异

| 维度 | TBPM DC 关联函数 | Kubo-Bastin Hall |
|------|-----------------|------------------|
| **物理量** | $\sigma_{xx}(E), \sigma_{yy}(E)$ | $\sigma_{xy}(\mu)$ |
| **自变量** | 电子能量 $E$ | 化学势 $\mu$ |
| **温度** | 零温（$T=0$）| 有限温（Fermi-Dirac 展宽）|
| **核心计算** | 波函数时间演化 + FFT | Chebyshev 矩 $\mu_{mn}$ 矩阵 |
| **复杂度** | $O(N_d \cdot B \cdot N_\text{orb})$ | $O(M^2 \cdot N_\text{orb} \cdot N_\theta)$ |
| **Chebyshev 阶数** | $\sim$10-20（Bessel 截断） | $\sim$1000-6000（KPM 收敛要求） |
| **数值稳定性** | 良好（低阶 Chebyshev） | 存在 $\Gamma \cdot \mu$ 随机游走问题（$M \gtrsim 2560$） |
| **与实验对比** | ❌ 横轴不同 | ✅ 可直接叠图 |
| **适用场景** | 导电通道能量分辨分析 | QHE 平台、$\sigma_{xy}(\mu)$ 扫描 |

### 8.1 何时使用 DC 关联函数而非 Kubo-Bastin

- 需要分析**哪些能量范围的电子态贡献导电**，而不关心化学势扫描
- 体系很大，Kubo-Bastin 的 $O(M^2)$ 计算量不可接受
- 关注 $\sigma_{xx}$（纵向电导）而非 $\sigma_{xy}$（Hall 电导）
- **不要**用它来生成与 QHE 实验对比的 $\sigma_{xx}(\mu)$ 曲线

---

## 9. 已知限制与注意事项

### 9.1 物理限制

1. **零温公式**：DC 关联函数法在 $T=0$ 极限下定义，不包含温度展宽效应。如需有限温结果，应使用 Kubo-Bastin 方法。
2. **能量分辨限制**：$\Delta E \approx E_\text{range} / (2N_d) \approx 17\text{eV}/(2 \times 1024) \approx 8\text{meV}$（graphene），不足以分辨极窄的能级。
3. **无 Hall 分量**：DC 关联函数法只计算纵向分量 $\sigma_{xx}, \sigma_{yy}$，不提供 $\sigma_{xy}$。Hall 电导率需用 Kubo-Bastin。

### 9.2 数值限制

1. **投影因子为零的风险**：当 $E$ 远离体系能谱时，$\langle\psi_0|\psi(E)\rangle \approx 0$，DC 关联函数发散。`dc_cond_energy_limits` 应设置在态密度非零的区域内。
2. **随机样本数**：单样本（`rs=1`）的统计噪声较大，建议 $rs \ge 4$ 进行随机平均。
3. **长时噪声**：$t \gg 0$ 时关联函数因数值误差偏离真实值。指数窗 `window_exp` 部分缓解此问题。

### 9.3 代码注意事项

1. **`corr_dos` 长度不一致**：`calc_corr_dc_cond()` 返回的长度为 `num_steps`（不含 t=0），而 `calc_corr_dos()` 返回 `num_steps+1`。`Analyzer.calc_dc_cond()` 内部已处理——但如果手动分析，需 `insert(0, 1.0)`。
2. **`dc_method="cheby_poly"` vs `"block_time"`**：默认 `"cheby_poly"` 是稳定选择。`"block_time"` 是早期实现，测试较少。
3. **缩放能量的处理**：C++ 内部所有计算在缩放空间进行（$\tilde{H} \in [-1, 1]$），`meta.qe_energies` 已减 `rescale_params_.center`。Python 侧的 `energies` 是物理能量。

---

## 10. 相关文件索引

| 文件 | 内容 |
|------|------|
| `01_methods_reference.md` §3 | TBPM DC 关联函数方法概述 |
| `02_kubo_bastin_deep_dive.md` | Kubo-Bastin Hall 电导率深度解析（对照阅读） |
| `shared/tbplas-internals.md` §9.3 | DC 关联函数全景 + 参数表 |
| `shared/tbplas-internals.md` §3 | TBPM 展宽控制全景 |
| `shared/tbplas-internals.md` §4 | Chebyshev 递推数值不稳定性 |
| `shared/tbplas-internals.md` §5 | `rs` 对单 site LDOS 无效原理 |
| `shared/tbplas-internals.md` §6 | 随机数生成机制 |
| `/home/wyl/tbplas/source/tbplas-cpp-a021ca8/sources/tbpm/tbpm.h` | `tbpm_dc_cond()`, `tbpm_qe_dos()` C++ 源码 |
| `/home/wyl/tbplas/source/tbplas-cpp-a021ca8/sources/tbpm/solver.h` | `calc_corr_dc_cond()` C++ 包装 |
| `/home/wyl/tbplas/source/tbplas-cpp-a021ca8/sources/tbpm/propagation.h` | `Propagator`, Bessel 表构建 |
| `/home/wyl/tbplas/source/tbplas-cpp-a021ca8/sources/tbpm/chebyshev.h` | `cheb_eval_wf()` 三项递推 |
| `/home/wyl/tbplas/source/tbplas-py-2.0.1/tbplas/tbpm/analysis.py` | `Analyzer.calc_dc_cond()` Python 后处理 |
| `/home/wyl/tbplas/source/tbplas-py-2.0.1/tbplas/tbpm/io.py` | `load_corr_dc_cond()` 数据加载 |
| `/home/wyl/tbplas/source/tbplas-py-2.0.1/tbplas/tbpm/solver.py` | `TBPMSolver.calc_corr_dc_cond()` Python 包装 |
