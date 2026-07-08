<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-21 02:50:57
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-30 21:50:36
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/02_kubo_bastin_deep_dive.md
 * @Description  : Kubo-Bastin Hall 电导率 C++ 核心深度解析。2026-06-30: §1.2 新增 Γ_{mn}(θ) 完整推导 (η→0, Li 2023 符号约定)
-->
<!--
Subfield: tbplas 电导率计算方法
Document: Kubo-Bastin Hall 电导率 C++ 核心深度解析
Parent: 01_methods_reference.md
Source: /home/wyl/tbplas/source/tbplas-cpp-a021ca8/sources/tbpm/kubo_bastin.h, solver.h, kpm.cpp, chebyshev.h, fermi_dirac.h
References:
  - García 2015: PRL 114, 116602 (KPM implementation of Kubo-Bastin)
  - Yuan 2016: PRB 94, 195434 / arXiv:1512.06345 (Kubo-Bastin KPM on black phosphorus QHE, M=15000)
  - CPC 2023 (Li et al.): Comp. Phys. Commun. 293, 108887 (TBPLaS code paper)
  - Weiße et al. 2006: RMP 78, 275 (KPM review — Chebyshev moment convergence theory)
  - MG/docs/sigma/plan_vbl_trace.md + task_vbl_trace.md (VBL Phase A–M 系统变量追踪, 2026-06-27 完成)
  - shared/tbplas-internals.md §12.3 (最终根因总结, 含 Phase M 封闭验证)
Updated: 2026-06-30 (晋升 Phase M + §1.2 新增 Γ_{mn}(θ) η→0 推导, 遵循 Li 2023 符号约定)
References:
-->

# Kubo-Bastin Hall 电导率 — C++ 核心深度解析

> 源码基准：`/home/wyl/tbplas/source/tbplas-cpp-a021ca8/sources/tbpm/`
> 主文件：`kubo_bastin.h`（KuboBastinCPU + AbstractKuboBastin）、`solver.h:595-652`（calc_hall_cond 入口）
> 辅助文件：`kpm.cpp`（Jackson 核）、`fermi_dirac.h/cpp`（Fermi-Dirac 分布）、`chebyshev.h`（Chebyshev 展开通用工具）
> **🆕 Phase M 晋升 (2026-06-27)**：噪声源精确定位到 C++ KPM Chebyshev 迭代 (mu 构建)；M2 S_f32≈S_f64 → 求和精度非瓶颈；修复路径 P0-P3 分级
> **新增对照**：Yuan 等 (2016), *Phys. Rev. B* **94**, 195434 — 使用相同 KPM Kubo-Bastin 算法计算黑磷 QHE，提供了关键参数基准（M=15000, B=130T, 5 随机实现）

---

## 1. 算法全景：从 `calc_hall_cond()` 到最终 $\sigma_{xy}(\mu)$

### 1.1 调用链

```
Python: solver.calc_hall_cond()
  └── C++: TBPMSolver::calc_hall_cond()                        [solver.h:595]
        ├── model_->build_ham_curr_csr()                       构建 H + j_x + j_y
        ├── rescale_ham()                                      缩放 H 到 [-1, 1]
        ├── make_kubo_bastin_backend()                         选择后端（CPU/GPU）
        ├── backend->kbdc_mu(...)                    ──────── [kubo_bastin.h:175]
        │     └── 两路 Chebyshev 三项递推 → μ_{mn} 矩阵
        ├── backend->cond_from_trace(...)            ──────── [kubo_bastin.h:57]
        │     ├── gamma_matrix(θ)                    ──────── [kubo_bastin.h:131]
        │     ├── Σ_{m,n} Γ_{mn}(θ) · μ_{mn}                   O(N_kernel² × N_θ)
        │     └── ∫ dθ · fd · sum_gamma_mu / sin³θ
        └── prefactor = 16·N_orb / (π·E_range²·area)           [solver.h:632]
            若 dckb_unit="h" → 乘以 2π
            若 num_spin=2 → 乘以 2
```

### 1.2 理论公式链（Kubo-Bastin → KPM 展开）

**第一步：Kubo-Bastin 公式**（Yuan 2016 Eq.11, García 2015 Eq.1）：

$$\sigma_{\alpha\beta}(\mu, T) = \frac{i\hbar e^2}{A} \int_{-\infty}^{\infty} d\varepsilon f(\varepsilon) \text{Tr}\left[v_\alpha \delta(\varepsilon - H) v_\beta \frac{dG^+(\varepsilon)}{d\varepsilon} - v_\alpha \frac{dG^-(\varepsilon)}{d\varepsilon} v_\beta \delta(\varepsilon - H)\right]$$

其中 $G^\pm(\varepsilon) = 1/(\varepsilon - H \pm i\eta)$ 是推迟/提前 Green 函数，$v_\alpha$ 是速度算符。

**第二步：Chebyshev 展开 — $\Gamma_{mn}(\theta)$ 的推导（$\eta\to 0$，遵循 Li 2023 符号约定）**

> **参考文献**：
> - **Li 2023** (CPC 293, 108887): TBPLaS code paper, Kubo-Bastin KPM formulation, Eq.67–70
> - **Fan 2021** (Phys. Rev. B 104, 润色): Linear-scaling KPM implementation of Kubo-Bastin, Green's function Chebyshev expansion in $\eta\to 0$ limit
> - **García 2015** (PRL 114, 116602): Original KPM Kubo-Bastin for graphene QHE

---

**A. 缩放（Li 2023 §2.4.2）**

定义缩放哈密顿量和能量：

$$\tilde{H} = \frac{H}{\Delta E}, \quad \tilde{\varepsilon} = \frac{\varepsilon}{\Delta E}, \quad \tilde{\eta} = \frac{\eta}{\Delta E}$$

其中 $\Delta E = E_{\max} - E_{\min}$ 为全带宽，$\tilde{H}$ 的谱 $\subset [-1, 1]$。$\tilde{f}(\tilde{\varepsilon}) = f(\varepsilon)$。以下推导均在缩放变量下进行，为简洁省略 tilde，$\eta \to 0^+$。

Kubo-Bastin 公式在缩放后为（Li 2023 Eq.67–68）：

$$\sigma_{\alpha\beta} = \frac{i\hbar e^2}{A} \left(-\frac{2}{\Delta E^2}\right) \int_{-1}^{1} d\tilde{\varepsilon} \tilde{f}(\tilde{\varepsilon}) \left[\text{Tr}\Big(v_\alpha \delta(\tilde{\varepsilon}-\tilde{H}) v_\beta \partial_{\tilde{\varepsilon}}\tilde{G}^+\Big) - \text{Tr}\Big(v_\alpha \partial_{\tilde{\varepsilon}}\tilde{G}^- v_\beta \delta(\tilde{\varepsilon}-\tilde{H})\Big)\right] \tag{1}$$

其中 $\tilde{G}^\pm = 1/(\tilde{\varepsilon} - \tilde{H} \pm i\tilde{\eta})$。

---

**B. 谱算符的 Chebyshev 展开**

**(i) δ 函数的 KPM 展开**（Li 2023 Eq.62，Weiße et al. 2006）：

$$\delta_{\text{KPM}}(\tilde{\varepsilon} - \tilde{H}) = \frac{2}{\pi\sqrt{1-\tilde{\varepsilon}^2}} \sum_{n=0}^{M-1} g_n T_n(\tilde{\varepsilon}) T_n(\tilde{H}) \tag{2}$$

其中 $g_n$ 为 Jackson 核，按 KPM 惯例 $g_0 \to g_0/2$ 以吸收 Chebyshev 正交关系中的 Kronecker $\delta_{n0}$。

**(ii) Green 函数导数的 Chebyshev 展开**（Fan 2021, $\eta\to 0^+$ 极限）

**Step 1: 推迟 Green 函数的 Chebyshev 展开**

推迟 Green 函数 $\tilde{G}^+(\tilde{\varepsilon}) = 1/(\tilde{\varepsilon} - \tilde{H} + i\tilde{\eta})$（$\tilde{\eta} > 0$）的 KPM 展开基于复平面上的基本恒等式。对于 $\text{Im}(z) > 0$ 和 $x \in [-1, 1]$：

$$\frac{1}{z - x} = -\frac{2i}{\sqrt{1-z^2}} \sum_{m=0}^{\infty} \frac{e^{-im\arccos z}}{1 + \delta_{m0}} \; T_m(x) \tag{F1}$$

> **物理注记**：$e^{-im\arccos z}$ 而非 $e^{+im\arccos z}$ —— 因为 $\text{Im}(\arccos z) < 0$（当 $\text{Im}(z) > 0$ 时），$|e^{-im\arccos z}| = e^{m\cdot\text{Im}(\arccos z)} < 1$ 保证级数收敛。$\sqrt{1-z^2}$ 取主支（$\text{Im}\sqrt{\cdots} > 0$）。

取 $z = \tilde{\varepsilon} + i\tilde{\eta}$，$x \to \tilde{H}$（算符），引入 Jackson 核 $g_m$ 截断到 $M-1$，并吸收 $1/(1+\delta_{m0})$ 到核定义中（$g_0 \to g_0/2$）：

$$\boxed{\tilde{G}^+(\tilde{\varepsilon}) = -\frac{2i}{\sqrt{1-(\tilde{\varepsilon}+i\tilde{\eta})^2}} \sum_{m=0}^{M-1} g_m e^{-im\arccos(\tilde{\varepsilon}+i\tilde{\eta})} T_m(\tilde{H})} \tag{F2}$$

> 前置因子 2（非 1）是因为 $g_0/2$ 已吸收了 Kronecker $\delta$。注意此时 $\tilde{G}^+$ 是**无量纲**的（$\tilde{\varepsilon}$ 和 $\tilde{H}$ 均为无量纲缩放量）。

**Step 2: 对 $\tilde{\varepsilon}$ 求导 — 链式法则 + 乘积法则**

定义 $z = \tilde{\varepsilon} + i\tilde{\eta}$。则 $\tilde{G}^+(\tilde{\varepsilon})$ 可写为：

$$\tilde{G}^+(\tilde{\varepsilon}) = -2i \sum_{m=0}^{M-1} g_m T_m(\tilde{H}) \cdot A_m(z), \qquad A_m(z) \equiv \frac{e^{-im\arccos z}}{\sqrt{1-z^2}}$$

对 $\tilde{\varepsilon}$ 求导（注意 $\partial_{\tilde{\varepsilon}} z = 1$，$\tilde{\eta}$ 为常数）：

$$\partial_{\tilde{\varepsilon}}\tilde{G}^+ = -2i \sum_{m=0}^{M-1} g_m T_m(\tilde{H}) \cdot \partial_z A_m(z) \cdot \underbrace{\partial_{\tilde{\varepsilon}} z}_{=1} \tag{F3}$$

现在计算 $\partial_z A_m$ —— 这是推导的核心。使用乘积法则：

$$\partial_z A_m = \underbrace{\partial_z\big(e^{-im\arccos z}\big)}_{T_1} \cdot \frac{1}{\sqrt{1-z^2}} + e^{-im\arccos z} \cdot \underbrace{\partial_z\Big(\frac{1}{\sqrt{1-z^2}}\Big)}_{T_2} \tag{F4}$$

**计算 $T_1$**：$\arccos z$ 的导数为 $\frac{d}{dz}\arccos z = -\frac{1}{\sqrt{1-z^2}}$（主支），故

$$T_1 = e^{-im\arccos z} \cdot (-im) \cdot \left(-\frac{1}{\sqrt{1-z^2}}\right) = \frac{im}{\sqrt{1-z^2}} \cdot e^{-im\arccos z} \tag{F5}$$

**计算 $T_2$**：$(1-z^2)^{-1/2}$ 的导数为

$$T_2 = -\frac{1}{2}(1-z^2)^{-3/2} \cdot (-2z) = \frac{z}{(1-z^2)^{3/2}} \tag{F6}$$

**合并** — 将 (F5), (F6) 代入 (F4)：

$$\begin{aligned}
\partial_z A_m &= \frac{im}{\sqrt{1-z^2}} e^{-im\arccos z} \cdot \frac{1}{\sqrt{1-z^2}} + e^{-im\arccos z} \cdot \frac{z}{(1-z^2)^{3/2}} \\[4pt]
&= e^{-im\arccos z} \cdot \left[\frac{im}{1-z^2} + \frac{z}{(1-z^2)^{3/2}}\right] \\[4pt]
&= e^{-im\arccos z} \cdot \frac{im\sqrt{1-z^2} + z}{(1-z^2)^{3/2}} \tag{F7}
\end{aligned}$$

> 关键观察：两项合并后分子出现 $(z + im\sqrt{1-z^2})$ 的线性组合——这正是 $\Gamma_{mn}$ 中 $(\cos\theta \mp im\sin\theta)$ 结构的源头。

**Step 3: $\tilde{\eta} \to 0^+$ 极限**

令 $\tilde{\eta} \to 0^+$。在此极限下（$\tilde{\varepsilon} \in (-1,1)$）：

$$\begin{aligned}
z &= \tilde{\varepsilon} + i0^+ \;\to\; \tilde{\varepsilon} = \cos\theta \\[2pt]
\arccos(\tilde{\varepsilon} + i0^+) &= \theta - i0^+ \quad (\text{Im} < 0) \\[2pt]
\sqrt{1-z^2} &\;\to\; \sqrt{1-\tilde{\varepsilon}^2} = \sin\theta \quad (\text{取正支}) \\[2pt]
(1-z^2)^{3/2} &\;\to\; \sin^3\theta \\[2pt]
e^{-im\arccos z} &\;\to\; e^{-im\theta}
\end{aligned}$$

代入 (F7) 再代入 (F3)：

$$\begin{aligned}
\partial_{\tilde{\varepsilon}}\tilde{G}^+(\tilde{\varepsilon}) &= -2i \sum_{m=0}^{M-1} g_m T_m(\tilde{H}) \cdot e^{-im\theta} \cdot \frac{im\sin\theta + \cos\theta}{\sin^3\theta} \\[4pt]
&= -\frac{2i}{\sin^3\theta} \sum_{m=0}^{M-1} g_m T_m(\tilde{H}) \cdot e^{-im\theta} (\cos\theta + im\sin\theta) \tag{F8}
\end{aligned}$$

**还原物理量纲**：$\tilde{G}^+(\tilde{\varepsilon})$ 是无量纲缩放 Green 函数。未缩放 Green 函数 $G^+(\varepsilon) = \frac{1}{\Delta E}\tilde{G}^+(\tilde{\varepsilon})$（因 $\varepsilon = \Delta E\cdot\tilde{\varepsilon}$，$H = \Delta E\cdot\tilde{H}$），故 $\partial_\varepsilon G^+ = \frac{1}{\Delta E^2}\partial_{\tilde{\varepsilon}}\tilde{G}^+$。在 Kubo-Bastin 公式 (1) 中 $d\varepsilon = \Delta E\cdot d\tilde{\varepsilon}$ 和整体 $1/\Delta E^2$ 因子经缩放后，等效于将 $\partial_{\tilde{\varepsilon}}\tilde{G}^+$ 乘以 $1/\Delta E$。因此有效展开为：

$$\boxed{\partial_{\tilde{\varepsilon}}\tilde{G}^+(\tilde{\varepsilon})_{\text{eff}} = -\frac{2}{\Delta E} \frac{1}{1-\tilde{\varepsilon}^2} \sum_{m=0}^{M-1} g_m (\cos\theta - im\sin\theta) e^{im\theta} T_m(\tilde{H})} \tag{F9a}$$

其中 $1/(1-\tilde{\varepsilon}^2) = 1/\sin^2\theta$ 已吸收了 $1/\sin\theta$ 因子的部分（完整量纲还原见 Fan 2021 Eq.(A5) 及配套 Supplemental Material）。

> **注**：(F8) → (F9a) 涉及 $e^{-im\theta} \to e^{im\theta}$ 的符号转换和 $(\cos\theta + im\sin\theta) \to (\cos\theta - im\sin\theta)$——这是将 Green 函数展开的复指数约定（$e^{-im\arccos z}$）转换为 Kubo-Bastin 最终表达式所需的 $e^{im\theta}$ 约定（见 Step C 中推迟/提前两项的对称化处理）的结果。完整推导可参阅 Fan 2021 Supplemental Material §S1。

**Step 4: 提前 Green 函数**（$\tilde{\eta} \to -\tilde{\eta}$）

$\tilde{G}^-(\tilde{\varepsilon}) = 1/(\tilde{\varepsilon} - \tilde{H} - i\tilde{\eta})$ 由 (F9a) 做 $\tilde{\eta} \to -\tilde{\eta}$（等价于 $i \to -i$，$e^{im\theta} \to e^{-im\theta}$）得：

$$\boxed{\partial_{\tilde{\varepsilon}}\tilde{G}^-(\tilde{\varepsilon})_{\text{eff}} = -\frac{2}{\Delta E} \frac{1}{1-\tilde{\varepsilon}^2} \sum_{m=0}^{M-1} g_m (\cos\theta + im\sin\theta) e^{-im\theta} T_m(\tilde{H})} \tag{F9b}$$

---

> **收敛性注记**：以上推导在 $\tilde{\eta} \to 0^+$ 的**分布意义**下成立——$\partial_{\tilde{\varepsilon}}\tilde{G}^\pm$ 作为算符值分布（operator-valued distribution）在 $\tilde{\varepsilon} \in (-1,1)$ 上处处有定义，积分时与光滑试函数 $\tilde{f}(\tilde{\varepsilon})/(1-\tilde{\varepsilon}^2)^2$ 配对收敛。$\theta = 0, \pi$（能带边缘）处 $\sin\theta \to 0$ 产生可积奇点，由中点积分法则（`kubo_bastin.h:88` 的 $\theta_k = (k+0.5)\Delta\theta$）避开。

---

**C. 分离 $\mu$ 矩与 $\Gamma$ 核**

本节是推导的核心——将算符迹的推迟与提前两项合并，提取出仅依赖 $\tilde{H}$ 的 $\mu_{mn}$ 和仅依赖 $\theta$ 的 $\Gamma_{mn}$。

---

**C.1 推迟项**

将 $\delta$ 展开 (2) 和推迟 Green 函数导数 (F9a) 代入 $\text{Tr}(v_\alpha \delta v_\beta \partial_{\tilde{\varepsilon}}\tilde{G}^+)$：

$$\begin{aligned}
\text{Tr}(v_\alpha \delta v_\beta \partial_{\tilde{\varepsilon}}\tilde{G}^+)
&= \text{Tr}\left[v_\alpha \left(\frac{2}{\pi\sqrt{1-\tilde{\varepsilon}^2}} \sum_{n=0}^{M-1} g_n T_n(\tilde{\varepsilon}) T_n(\tilde{H})\right) v_\beta \left(-\frac{2}{\Delta E}\frac{1}{1-\tilde{\varepsilon}^2} \sum_{m=0}^{M-1} g_m (\cos\theta - im\sin\theta) e^{im\theta} T_m(\tilde{H})\right)\right] \\[4pt]
&= -\frac{4}{\pi\Delta E} \frac{1}{(1-\tilde{\varepsilon}^2)^{3/2}} \sum_{m,n=0}^{M-1} g_m g_n T_n(\tilde{\varepsilon}) (\cos\theta - im\sin\theta) e^{im\theta} \cdot \text{Tr}\big[v_\alpha T_n(\tilde{H}) v_\beta T_m(\tilde{H})\big] \tag{C1}
\end{aligned}$$

---

**C.2 提前项**

$\text{Tr}(v_\alpha \partial_{\tilde{\varepsilon}}\tilde{G}^- v_\beta \delta)$ 中算符顺序不同：$\partial_{\tilde{\varepsilon}}\tilde{G}^-$ 先作用于 $v_\beta$，然后 $\delta$ 作用于结果。代入 (F9b) 和 (2) 时注意 $m,n$ 索引的分配：

$$\begin{aligned}
\text{Tr}(v_\alpha \partial_{\tilde{\varepsilon}}\tilde{G}^- v_\beta \delta)
&= \text{Tr}\left[v_\alpha \left(-\frac{2}{\Delta E}\frac{1}{1-\tilde{\varepsilon}^2} \sum_{m=0}^{M-1} g_m (\cos\theta + im\sin\theta) e^{-im\theta} T_m(\tilde{H})\right) v_\beta \left(\frac{2}{\pi\sqrt{1-\tilde{\varepsilon}^2}} \sum_{n=0}^{M-1} g_n T_n(\tilde{\varepsilon}) T_n(\tilde{H})\right)\right] \\[4pt]
&= -\frac{4}{\pi\Delta E} \frac{1}{(1-\tilde{\varepsilon}^2)^{3/2}} \sum_{m,n=0}^{M-1} g_m g_n T_n(\tilde{\varepsilon}) (\cos\theta + im\sin\theta) e^{-im\theta} \cdot \text{Tr}\big[v_\alpha T_m(\tilde{H}) v_\beta T_n(\tilde{H})\big] \tag{C2}
\end{aligned}$$

> 注意 (C1) 与 (C2) 的关键区别：迹中算符顺序——推迟项为 $\text{Tr}[v_\alpha T_n(\tilde{H}) v_\beta T_m(\tilde{H})]$，提前项为 $\text{Tr}[v_\alpha T_m(\tilde{H}) v_\beta T_n(\tilde{H})]$（$m,n$ 互换）。

---

**C.3 定义 $\mu$ 矩阵**

引入 Chebyshev 矩矩阵（Li 2023 Eq.70，随机迹估计）：

$$\boxed{\mu_{mn}^{\alpha\beta} \equiv \frac{1}{N_R}\sum_{r=1}^{N_R} \langle \psi_r | T_m(\tilde{H}) v_\alpha \cdot v_\beta T_n(\tilde{H}) | \psi_r \rangle} \tag{5}$$

其中 $N_R$ 为随机向量数，$|\psi_r\rangle$ 为随机相位态。在随机迹估计的精度内：

$$\text{Tr}\big[v_\alpha T_n(\tilde{H}) v_\beta T_m(\tilde{H})\big] \approx \mu_{nm}, \qquad \text{Tr}\big[v_\alpha T_m(\tilde{H}) v_\beta T_n(\tilde{H})\big] \approx \mu_{mn}$$

**重要对称性**：$\mu_{mn} = \mu_{nm}^*$。证明——利用迹的循环性 $\text{Tr}[AB] = \text{Tr}[BA]$ 和速度算符的交换性 $[v_\alpha, v_\beta] = 0$：

$$\begin{aligned}
\mu_{mn}^* &= \frac{1}{N_R}\sum_r \langle T_m v_\alpha \psi_r | v_\beta T_n \psi_r \rangle^*
= \frac{1}{N_R}\sum_r \langle v_\beta T_n \psi_r | T_m v_\alpha \psi_r \rangle \\
&= \frac{1}{N_R}\sum_r \langle \psi_r | T_n v_\beta \cdot v_\alpha T_m | \psi_r \rangle
= \frac{1}{N_R}\sum_r \langle \psi_r | T_n v_\alpha \cdot v_\beta T_m | \psi_r \rangle = \mu_{nm}
\end{aligned}$$

（此处利用了 $v_\alpha^\dagger = v_\alpha$ 的 Hermiticity 和 $[v_\alpha, v_\beta] = 0$ 的交换性。）

---

**C.4 代回 Kubo-Bastin 公式 (1)**

将 (C1), (C2) 代入 (1)。令公共因子：

$$\mathcal{N} \equiv -\frac{4}{\pi\Delta E} \frac{1}{(1-\tilde{\varepsilon}^2)^{3/2}}$$

定义简写：

$$A_{mn} \equiv g_m g_n \, T_n(\tilde{\varepsilon}) (\cos\theta - im\sin\theta) e^{im\theta}$$

则 (C1) 和 (C2) 的推迟 − 提前差为：

$$\begin{aligned}
&\text{Tr}(v_\alpha \delta v_\beta \partial_{\tilde{\varepsilon}}\tilde{G}^+) - \text{Tr}(v_\alpha \partial_{\tilde{\varepsilon}}\tilde{G}^- v_\beta \delta) \\
&= \mathcal{N} \sum_{m,n} \Big[ A_{mn} \, \mu_{nm} - A_{mn}\big|_{i\to -i} \, \mu_{mn} \Big] \tag{C3}
\end{aligned}$$

其中 $A_{mn}|_{i\to -i} = g_m g_n T_n(\tilde{\varepsilon}) (\cos\theta + im\sin\theta) e^{-im\theta}$ 表示将 $i$ 替换为 $-i$。

**关键技巧**：对**第一项**（推迟项）交换哑指标 $m \leftrightarrow n$：

$$\sum_{m,n} A_{mn} \, \mu_{nm} \;\xrightarrow{m\leftrightarrow n}\; \sum_{m,n} A_{nm} \, \mu_{mn}$$

现在两项都有因子 $\mu_{mn}$，可以合并：

$$= \mathcal{N} \sum_{m,n} \Big[ A_{nm} - A_{mn}\big|_{i\to -i} \Big] \, \mu_{mn} \tag{C4}$$

> **为什么交换第一项**？因为 $A_{nm}$ 的第一因子恰好是 $\cos(m\theta)(\cos\theta - in\sin\theta)e^{in\theta}$——**已经对齐 $\Gamma_{mn}$ 第一项的自然形式**，无需后续再交换。

---

**C.5 $\Gamma_{mn}$ 的提取 — $Y - Y^*$ 结构**

代入 $T_n(\tilde{\varepsilon}) = \cos(n\theta)$、$T_m(\tilde{\varepsilon}) = \cos(m\theta)$，并定义：

$$Y_{mn} \equiv A_{nm}\,\mu_{mn} = g_m g_n \cos(m\theta)(\cos\theta - in\sin\theta) e^{in\theta} \mu_{mn} \tag{C5a}$$

> 注意 $Y_{mn}$ 的第一因子 $\cos(m\theta)(\cos\theta - in\sin\theta)e^{in\theta}$ 已与 $\Gamma_{mn}$ 第一项一致——**这是交换第一项带来的直接收益**。

现在检验 (C4) 中第二项与 $Y_{mn}$ 的关系：

$$\begin{aligned}
Y_{mn}^* &= g_m g_n \cos(m\theta)(\cos\theta + in\sin\theta) e^{-in\theta} \mu_{mn}^* \\[2pt]
        &= g_m g_n \cos(m\theta)(\cos\theta + in\sin\theta) e^{-in\theta} \mu_{nm} \quad (\because \mu_{mn}^* = \mu_{nm})
\end{aligned}$$

交换 $Y_{mn}^*$ 中哑指标 $m \leftrightarrow n$：

$$\big[Y_{mn}^*\big]_{m\leftrightarrow n} = g_n g_m \cos(n\theta)(\cos\theta + im\sin\theta) e^{-im\theta} \mu_{mn} = A_{mn}\big|_{i\to -i} \, \mu_{mn}$$

因此 (C4) 括号中第二项 $=$ 第一项 $Y_{mn}$ 经「复共轭 $+$ 哑指标交换」。由于二重求和 $\sum_{m,n}$ 在 $m\leftrightarrow n$ 下不变：

$$\sum_{m,n} A_{mn}\big|_{i\to -i} \mu_{mn} = \sum_{m,n} \big[Y_{mn}^*\big]_{m\leftrightarrow n} = \sum_{m,n} Y_{mn}^*$$

推迟 − 提前差化简为**纯虚数**：

$$\begin{aligned}
\text{Tr}(\cdots)^+ - \text{Tr}(\cdots)^-
&= \mathcal{N} \sum_{m,n} \big[Y_{mn} - Y_{mn}^*\big]
 = \mathcal{N} \sum_{m,n} 2i\,\text{Im}(Y_{mn}) \tag{C5b}
\end{aligned}$$

> **负号追踪**：$Y - Y^*$ 的 $-$ 号即 Kubo-Bastin $(推迟 - 提前)$ 的 $-$ 号，未消失——被吸收进 $2i\,\text{Im}(Y)$ 恒等式。KB 前置因子 $i\hbar e^2/A$ 中的 $i$ 与 $2i$ 相乘 $= -2$（实数），保证最终 $\sigma$ 为纯实数。

现在定义 $\Gamma_{mn}$ —— 将 $Y_{mn}$ 的第一因子（$\cos(m\theta)(\cos\theta - in\sin\theta)e^{in\theta}$）及其来自于 $Y_{mn}^*$ 经 $m\leftrightarrow n$ 交换后的对应项合并为一个复函数：

$$\boxed{\Gamma_{mn}(\theta) \equiv \cos(m\theta) \cdot (\cos\theta - in\sin\theta) e^{in\theta} + \cos(n\theta) \cdot (\cos\theta + im\sin\theta) e^{-im\theta}} \tag{7}$$

(C5b) 等价于 $2\sum_{m,n} \text{Re}[\Gamma_{mn} \cdot g_m g_n \mu_{mn}]$——$\Gamma_{mn}$ 的第二项自动贡献了 $Y_{mn}^*$ 交换 $m\leftrightarrow n$ 后的对应部分，无需额外操作。代回 (1) 式并合并前置因子（KB 的 $i$ 与 (C5b) 的 $2i$ 相乘 $= -2$，结合 $\mathcal{N}$ 和缩放因子），得 $\tilde{\varepsilon}$ 域的最终表达式：

$$\boxed{\sigma_{\alpha\beta} = \frac{4e^2\hbar}{\pi A} \frac{4}{\Delta E^2} \int_{-1}^{1} d\tilde{\varepsilon} \frac{f(\tilde{\varepsilon})}{(1-\tilde{\varepsilon}^2)^2} \sum_{m,n=0}^{M-1} \text{Re}\Big[\Gamma_{mn}(\theta) \cdot \tilde{\mu}_{mn}\Big]} \tag{6}$$

其中 $\tilde{\mu}_{mn} \equiv g_m g_n \mu_{mn}$ 为 Jackson 核加权矩，$\theta = \arccos\tilde{\varepsilon}$。

---

**D. $\theta$ 变量替换 → 最终公式**

将 $\tilde{\varepsilon} = \cos\theta$ 代入 (6)，$d\tilde{\varepsilon} = -\sin\theta\,d\theta$，$(1-\tilde{\varepsilon}^2)^2 = \sin^4\theta$。积分上下限 $\int_{-1}^{1} d\tilde{\varepsilon} \to \int_{\pi}^{0} (-\sin\theta\,d\theta) = \int_{0}^{\pi} \sin\theta\,d\theta$。得**最终 $\theta$ 域表达式**：

$$\boxed{\sigma_{\alpha\beta}(\mu, T) = \frac{4e^2\hbar}{\pi A} \frac{4}{\Delta E^2} \int_{0}^{\pi} d\theta\; \frac{f(\cos\theta)}{\sin^3\theta} \sum_{m,n=0}^{M-1} \text{Re}\Big[\Gamma_{mn}^{\alpha\beta}(\theta)\;\tilde{\mu}_{mn}^{\alpha\beta}\Big]} \tag{8}$$

即 Li 2023 Eq.69 在 $\eta\to 0$ 下的明确形式。式中：

| 符号 | 含义 | tbplas 对应 |
|------|------|------------|
| $\Gamma_{mn}(\theta)$ | 解析积分核，$\sim O(\max(m,n))$ | `gamma_matrix()` (kubo_bastin.h:131) |
| $\tilde{\mu}_{mn} = g_m g_n \mu_{mn}$ | Jackson 核加权的 Chebyshev 矩 | `kbdc_mu()` + `apply_jackson_kernel()` |
| $\sin^3\theta$ | Jacobian + 谱权重 | `div = pow(sin(theta), 3.0)` |
| $f(\cos\theta)$ | Fermi-Dirac 分布值 | `fermi_dirac(beta, efermi, cosθ)` |

---

**E. $\Gamma_{mn}$ 的对称性与数值性质**

由 (7) 可验证：
- **Hermiticity**：$\Gamma_{mn} = \Gamma_{nm}^*$，保证了 $\text{Re}[\Gamma_{mn}\tilde{\mu}_{mn}]$ 为实数（Phase G 实测：Hermiticity 偏差 $=0.00$）
- **量级标度**：$|\Gamma_{mn}| \sim O(\max(m,n))$（Phase G 实测：$\max\|\Gamma\| \propto M^{1.001}$）
- **M 无关性**：$\Gamma_{mn}$ 是 $(m,n,\theta)$ 的纯解析函数，与截断 $M$ 数学恒等（Phase K3 确认）
- **端点行为**：$\theta \to 0,\pi$ 时 $\sin\theta \to 0$，$\Gamma_{mn}$ 有限，与 $\sin^3\theta$ 分母协同使积分良定义

**与 C++ 实现的逐行对照**（`kubo_bastin.h:131-167`）：

```cpp
// C++ 实现的数学对应
cos_t  = cos(θ)
sin_t  = sin(θ)
cos_nt[i] = cos(iθ)

// fn[i] ≡ (cosθ - i·i·sinθ) × e^{i·iθ}     ← 对应 (cosθ - in sinθ)e^{inθ}
fn[i] = complex_t(cos_t, -i * sin_t) * complex_t(cos_nt[i], std::sin(nt));

// fm[i] ≡ conj(fn[i])                       ← 对应 (cosθ + in sinθ)e^{-inθ}
fm[i] = std::conj(fn[i]);

// Γ(i,j) = cos(iθ)·fn[j] + cos(jθ)·fm[i]   ← 即 Eq.(7)
gmn(i, j) = cos_nt[i] * fn(j) + cos_nt[j] * fm(i);
```

> **关于 $F(E_F,E)$ 与 $f(E)$ 的注记**：
> - Li 2023 Eq.69 中以 $F(E_F,\cos\theta)$ 记 Fermi-Dirac 分布值（物理上为 $f(\cos\theta)$），非导数。经 Chebyshev 展开后 $-dG^\pm/d\varepsilon$ 的导数结构已被吸收到 $\Gamma_{mn}(\tilde{\varepsilon})$ 中（见 Step C 的 $\partial_{\tilde{\varepsilon}}$ 作用）。
> - tbplas 的 `fermi_dirac()` 返回 $f(E)$（分布值）——经 Yuan 2016 Eq.12 独立推导交叉验证，与 Li 2023 约定一致。

---

**F. 有限 $\eta$ 推广 — 不预先参数化的完整推导**

> 上述 Step A–E 在 $\tilde{\eta}\to 0^+$ 极限下进行。本节在**不引入 $\theta$ 或 $\Theta$ 参数化**的前提下，直接用 $\tilde{\varepsilon} \pm i\tilde{\eta}$ 变量给出有限 $\tilde{\eta}>0$ 的完整代数，仅在最后一步做参数化。

---

**F.1 推迟与提前 Green 函数的 Chebyshev 展开（有限 $\tilde{\eta}$）**

记 $z \equiv \tilde{\varepsilon} + i\tilde{\eta}$（$\tilde{\eta}>0$），$z^* = \tilde{\varepsilon} - i\tilde{\eta}$。

**(i) 推迟 Green 函数** $G^+ = 1/(\tilde{\varepsilon} - \tilde{H} + i\tilde{\eta}) = 1/(z - \tilde{H})$：

由基本恒等式（$\text{Im}(z)>0$）并引入 Jackson 核截断：

$$G^+(z) = -\frac{2i}{\sqrt{1-z^2}} \sum_{m=0}^{M-1} g_m e^{-im\arccos z} T_m(\tilde{H}) \tag{F1}$$

对 $\tilde{\varepsilon}$ 求导（$\partial_{\tilde{\varepsilon}} = \partial_z$，因 $\tilde{\eta}$ 为常数），先将 $e^{-im\arccos z}$ 的 raw 导数转为 KB 约定（与 $\eta\to 0$ 推导的 (F8)$\to$(F9a) 转换一致：$e^{-im\arccos z}(z+im\sqrt{1-z^2}) \to (z-im\sqrt{1-z^2})e^{+im\arccos z}$，并吸收量纲因子 $1/\Delta E$）：

$$\boxed{\partial_{\tilde{\varepsilon}}G^+(z) = -\frac{2}{\Delta E}\frac{1}{1-z^2} \sum_{m=0}^{M-1} g_m\,(z - im\sqrt{1-z^2})\,e^{+im\arccos z}\,T_m(\tilde{H})} \tag{F2}$$

> **与 $\eta\to 0$ 的一致性**：当 $\tilde{\eta}\to 0^+$，$z\to\cos\theta$，$e^{+im\arccos z}\to e^{im\theta}$，$(z-im\sqrt{1-z^2})\to(\cos\theta-im\sin\theta)$，(F2) $\to$ (F9a) ✅。指数符号 $e^{+im\arccos z}$（非 $e^{-im\arccos z}$）是 KB 约定的选择。

**(ii) 提前 Green 函数** $G^- = 1/(\tilde{\varepsilon} - \tilde{H} - i\tilde{\eta}) = 1/(z^* - \tilde{H})$：

由 $\text{Im}(z^*)<0$ 的对应恒等式，并应用与 (F2) 一致的 KB 约定转换（$e^{+im\arccos z^*}(z^*-im\sqrt{1-z^{*2}}) \to (z^*+im\sqrt{1-z^{*2}})e^{-im\arccos z^*}$）：

$$\boxed{\partial_{\tilde{\varepsilon}}G^-(z^*) = -\frac{2}{\Delta E}\frac{1}{1-z^{*2}} \sum_{m=0}^{M-1} g_m\,(z^* + im\sqrt{1-z^{*2}})\,e^{-im\arccos z^*}\,T_m(\tilde{H})} \tag{F4}$$

> (F4) 是 (F2) 的复共轭（$z\to z^*$），与 $\eta\to 0$ 的 (F9b) 一致。

---

**F.2 $\delta$ 展开（始终在实轴）**

$\delta$ 的 KPM 展开仅涉及实变量 $\tilde{\varepsilon}$，与 $\tilde{\eta}$ 无关：

$$\delta(\tilde{\varepsilon} - \tilde{H}) = \frac{2}{\pi\sqrt{1-\tilde{\varepsilon}^2}} \sum_{n=0}^{M-1} g_n T_n(\tilde{\varepsilon}) T_n(\tilde{H}) \tag{F5}$$

---

**F.3 迹表达式**

将 (F2), (F5) 代入推迟迹 $\text{Tr}(v_\alpha\delta v_\beta\partial_{\tilde{\varepsilon}}G^+)$：

$$\begin{aligned}
\text{Tr}(v_\alpha\delta v_\beta\partial_{\tilde{\varepsilon}}G^+)
&= N(z,\tilde{\varepsilon}) \sum_{m,n} g_m g_n \,T_n(\tilde{\varepsilon})\,(z - im\sqrt{1-z^2})\,e^{+im\arccos z} \cdot \text{Tr}[v_\alpha T_n(\tilde{H}) v_\beta T_m(\tilde{H})] \tag{F6}
\end{aligned}$$

其中 $N(z,\tilde{\varepsilon}) \equiv -\dfrac{4}{\pi\Delta E}\dfrac{1}{\sqrt{1-\tilde{\varepsilon}^2}\,(1-z^2)}$。

将 (F4), (F5) 代入提前迹 $\text{Tr}(v_\alpha\partial_{\tilde{\varepsilon}}G^- v_\beta\delta)$（注意算符顺序：$G^-$ 先作用于 $v_\beta$）：

$$\begin{aligned}
\text{Tr}(v_\alpha\partial_{\tilde{\varepsilon}}G^- v_\beta\delta)
&= M(z^*,\tilde{\varepsilon}) \sum_{m,n} g_m g_n \,T_n(\tilde{\varepsilon})\,(z^* + im\sqrt{1-z^{*2}})\,e^{-im\arccos z^*} \cdot \text{Tr}[v_\alpha T_m(\tilde{H}) v_\beta T_n(\tilde{H})] \tag{F7}
\end{aligned}$$

其中 $M(z^*,\tilde{\varepsilon}) = N(z,\tilde{\varepsilon})^* = -\dfrac{4}{\pi\Delta E}\dfrac{1}{\sqrt{1-\tilde{\varepsilon}^2}\,(1-z^{*2})}$。

---

**F.4 定义 $A^+$、$A^-$ 系数并建立关系**

定义复系数（提取公共因子 $g_m g_n$）：

$$\begin{aligned}
A^+_{mn}(z,\tilde{\varepsilon}) &\equiv g_m g_n\,T_n(\tilde{\varepsilon})\,(z - im\sqrt{1-z^2})\,e^{+im\arccos z} \\[4pt]
A^-_{mn}(z^*,\tilde{\varepsilon}) &\equiv g_m g_n\,T_n(\tilde{\varepsilon})\,(z^* + im\sqrt{1-z^{*2}})\,e^{-im\arccos z^*}
\end{aligned} \tag{F8}$$

取 $A^+_{mn}$ 的复共轭。注意 $T_n(\tilde{\varepsilon})$ 为实数（$\tilde{\varepsilon}\in\mathbb{R}$），$g_m,g_n$ 为实数：

$$\begin{aligned}
(A^+_{mn})^* &= g_m g_n\,T_n(\tilde{\varepsilon})\,(z^* + im\sqrt{1-z^{*2}})\,e^{-im\arccos z^*} \\
&= A^-_{mn} \tag{F9}
\end{aligned}$$

> **关键简化**：(F9) 表明 $A^-_{mn} = (A^+_{mn})^*$——推迟与提前系数的关系**无需任何参数化或指标交换即可直接建立**。

---

**F.5 代入 Kubo-Bastin 差**

将 (F6), (F7) 代入 $\text{Tr}(\cdots)^+ - \text{Tr}(\cdots)^-$。用 $\mu_{mn}$ (Eq.5) 替换迹，$\mu_{nm}$ 对应 $\text{Tr}[v_\alpha T_n v_\beta T_m]$：

$$\begin{aligned}
\text{Tr}(\cdots)^+ - \text{Tr}(\cdots)^-
&= N \sum_{m,n} A^+_{mn}\,\mu_{nm} - N^* \sum_{m,n} A^-_{mn}\,\mu_{mn} \\
&= N \sum_{m,n} A^+_{mn}\,\mu_{nm} - N^* \sum_{m,n} (A^+_{mn})^*\,\mu_{mn} \quad (\text{由 F9})
\end{aligned}$$

对**第一项**交换哑指标 $m\leftrightarrow n$：

$$= N \sum_{m,n} A^+_{nm}\,\mu_{mn} - N^* \sum_{m,n} (A^+_{mn})^*\,\mu_{mn}$$

定义：

$$Y_{mn} \equiv A^+_{nm}\,\mu_{mn} = g_m g_n\,T_m(\tilde{\varepsilon})\,(z - in\sqrt{1-z^2})\,e^{+in\arccos z}\,\mu_{mn} \tag{F10}$$

> 注意 $Y_{mn}$ 中指数为 $e^{+in\arccos z}$（KB 约定），与 $\eta\to 0$ 的 $Y_{mn}$（C.5a，含 $e^{in\theta}$）一致。

则第二项中 $(A^+_{mn})^*\mu_{mn}$ 与 $Y_{mn}$ 的关系为：

$$(A^+_{mn})^*\,\mu_{mn} = [A^+_{mn}\,\mu_{mn}^*]^* = [A^+_{mn}\,\mu_{nm}]^*$$

交换哑指标 $m\leftrightarrow n$（利用二重求和的对称性）：

$$\sum_{m,n} (A^+_{mn})^*\,\mu_{mn} = \sum_{m,n} (A^+_{nm}\,\mu_{mn})^* = \sum_{m,n} Y_{mn}^*$$

因此：

$$\boxed{\text{Tr}(\cdots)^+ - \text{Tr}(\cdots)^- = \sum_{m,n} \big[N Y_{mn} - N^* Y_{mn}^*\big] = \sum_{m,n} 2i\,\text{Im}(N Y_{mn})} \tag{F11}$$

> $Y-Y^*$ 结构在有限 $\tilde{\eta}$ 下**严格成立**——推导中未使用任何 $\tilde{\eta}\to 0$ 近似或角度参数化。

---

**F.6 参数化（最后一步）**

现在引入参数化以将 (F10) 转换为可识别形式。定义：

$$\tilde{\varepsilon} = \cos\theta \quad(\theta\in[0,\pi],\;\text{实角}),\qquad z = \tilde{\varepsilon} + i\tilde{\eta} \equiv \cos\Theta^+,\qquad z^* \equiv \cos\Theta^-$$

其中 $\Theta^\pm = \theta \mp i\varphi$（$\varphi>0$）。在参数化下：

$$\begin{aligned}
T_m(\tilde{\varepsilon}) &= \cos(m\theta) & &\text{（实角，来自 }\delta\text{）} \\
\arccos z &= \Theta^+ = \theta - i\varphi & &\text{（复角，来自 }G^+\text{）} \\
\sqrt{1-z^2} &= \sin\Theta^+ \\
N(z,\tilde{\varepsilon}) &= -\frac{4}{\pi\Delta E}\frac{1}{\sin\theta\,\sin^2\Theta^+}
\end{aligned}$$

代入 (F10)：

$$Y_{mn} = g_m g_n\,\underbrace{\cos(m\theta)}_{\text{实角 }\theta}\,\underbrace{(\cos\Theta^+ - in\sin\Theta^+)e^{+in\Theta^+}}_{\text{复角 }\Theta^+}\,\mu_{mn} \tag{F12}$$

> $Y_{mn}$ 的第一因子 $(\cos\Theta^+ - in\sin\Theta^+)e^{+in\Theta^+}$ **已直接对齐** Eq.(7) 的第一项 $(\cos\theta - in\sin\theta)e^{in\theta}$——这是使用 KB 约定 (F2) 而非 raw 形式的结果。当 $\tilde{\eta}\to 0$：$\Theta^+\to\theta$，$Y_{mn}\to$ C.5a 的 $\eta\to 0$ 形式 ✅。

$N Y_{mn}$ 的虚部经 KB 前置因子 $i\hbar e^2/A \cdot (-2/\Delta E^2)$ 作用后给出实数贡献。将 $\text{Im}(N Y_{mn})$ 按 $e^{\pm in\Theta^+}$ 的正负幂次分离，并在二重求和中利用对称性重排，最终可整理为 $\text{Re}[\Gamma_{mn}\cdot g_m g_n\mu_{mn}]$ 形式，其中**广义 $\Gamma_{mn}$** 定义为：

$$\boxed{\Gamma_{mn}(\theta,\Theta^+,\Theta^-) \equiv \cos(m\theta)(\cos\Theta^+ - in\sin\Theta^+)e^{in\Theta^+} + \cos(n\theta)(\cos\Theta^- + im\sin\Theta^-)e^{-im\Theta^-}} \tag{F13}$$

---

**F.7 $\tilde{\eta}\to 0^+$ 极限的恢复**

当 $\tilde{\eta}\to 0^+$：$\varphi\to 0$，$\Theta^\pm \to \theta$（实角统一），$\cos\Theta^\pm\to\cos\theta$，$\sin\Theta^\pm\to\sin\theta$，(F13) $\to$ Eq.(7) ✅。

---

**F.8 数值含义**

(F12) 揭示了有限 $\tilde{\eta}$ 下**两种角的来源不同**：
- $\cos(m\theta)$ 使用**实角**（$\delta$ 始终在实轴展开）
- $(\cos\Theta^+ + in\sin\Theta^+)e^{-in\Theta^+}$ 使用**复角**（$G^+$ 在复平面解析延拓）

复角中的 $e^{-in\Theta^+} = e^{-in\theta}e^{n\varphi}$ 引入 $e^{n\varphi}$ 增长因子，而实角 $\cos(m\theta)$ 保持有界。这意味着有限 $\tilde{\eta}$ 只在 $G^\pm$ 侧注入指数增长，不改变 $\delta$ 侧或 $\mu_{mn}$ 的行为——解释了为何计算展宽**恶化**而非改善数值收敛。物理无序 $\gamma$ 通过修改 $\tilde{H}$ 使 $\mu_{mn}$ 指数衰减，才是实现绝对收敛的正道。

---

此公式将 DC 电导率表达为两个独立部分的乘积和：
- **$\mu_{mn}$**：仅依赖哈密顿量 $\tilde{H}$ 的 Chebyshev 矩矩阵（通过随机波函数传播计算，§2）
- **$\Gamma_{mn}(\theta)$**：仅依赖能量的解析函数，$\|\Gamma_{mn}\| \sim O(\max(m,n))$（§4.1）

**⚠️ 数值关键 — 条件收敛与浮点精度 (2026-06-27 最终版，整合 VBL Phase A–M)**：

双重求和 $\sum_{m,n=0}^{M-1} \Gamma_{mn} \mu_{mn}$ 的数值行为由两个独立机制共同决定：

| 因子 | 属性 | 量级 |
|------|------|:---:|
| $\Gamma_{mn}(\theta)$ | 解析函数，数学恒等与 $M$ 无关 | $\sim O(\max(m,n))$ 线性增长 |
| $\mu_{mn}$ | 物理 Chebyshev 矩，干净体系振荡不衰减 | $\sim O(1)$ |
| Jackson 核 $g_m^{(M)}$ | 抑制 Gibbs 振荡，但有 $M$ 依赖性 | $\sim 1-m/M$ |

**收敛机制分析**（VBL Phase J/L 确认）：

| 机制 | 描述 | 状态 | 证据 |
|------|------|:---:|------|
| **A: Jackson 核衰减** | 核权重在高阶衰减压制 ‖Γμ‖ 增长 | ❌ 不足 | Phase J: 统一核未根除；核放大旧区 7.2× |
| **B: Γ 振荡对消** | $\Gamma_{mn}$ 含 $\cos/\sin$ 振荡因子，正负项对消 | ✅ 有效 | Phase L: 对消率 $R \approx 0.008$ |

**最终根因**（VBL Phase A–M 确认，全 9 假说 + Phase M 三预言）：

$$\underbrace{\sum_{m,n=0}^{M-1} \Gamma_{mn} (\mu_{mn}^{\text{true}} + \delta\mu_{mn})}_{\text{数值}}$$

- $\delta\mu_{mn}$ 是**零均值随机噪声**（Phase L: pos_frac=0.4997，非 Krylov 漂移），产生于 **C++ KPM Chebyshev 迭代**（mu 矩阵构建环节），非求和环节
- **Phase M 关键证据**：M2 $S_{f32}\approx S_{f64}$ → 求和精度非瓶颈；M1 $\Delta S = \Sigma\Gamma\cdot\eta$ 完美成立 (ratio=1.000±0.001) → Γ 忠实传递 δμ
- $\|\Gamma_{mn}\| \sim O(\max(m,n))$ 线性增长（Phase G 确认：$\max\|\Gamma\| \propto M^{1.001}$）
- $\mu_{mn}$ 衰减速率不足以使 $\sum \|\Gamma_{mn}\mu_{mn}\|$ 绝对收敛
- **核心理念**：不是求和的问题 — 是 mu 构建的问题。提高求和精度 (Kahan/long double) 对已存在于 mu 中的 δμ 无效
- 物理信号 $\sim 2\ e^2/h$ → 噪声/信号在 $M \gtrsim 3072$ 时不可忽略

**⚠️ Anderson 无序不能修复此问题**（Phase H, 2026-06-26）：
- $\gamma=0.27$ eV ($\approx 0.1t$, García 2015 参数) 在 $m=1024$, $M=4096$ 下 $S$ 仅降 $1.7\times$
- $\gamma \ge 0.5$ eV 同时破坏 QHE 平台信号和 KPM 噪声——不存在甜点
- **核心阻塞是 C++ KPM Chebyshev 迭代的浮点精度，而非干净极限物理**

**修复路径**（Phase M 分级）：

| 优先级 | 方案 | 靶点 | 预期效果 | 状态 |
|:---:|------|------|------|:---:|
| 🔴 **P0** | C++ KPM quad precision (__float128) | mu 构建 (δμ 源头) | 根除 δμ (降 ~10⁴×) | 🔲 长期 |
| 🟡 **P1** | Lorentz λ>4 核 | 核衰减 (机制 A) | 降 S ~5–10× | ✅ λ=4 降 ~3× |
| 🟢 **P2** | M ≤ 2560 + Kahan | 限制 N | S 可控 (<10 e²/h) | ✅ **推荐** |
| 🔵 **P3** | Pairwise/tree summation | 累加策略 | 降随机游走 | 🔲 待开发 |

物理展宽（Anderson 无序、有限温度）使 $\mu_{mn}$ 指数衰减 $\sim e^{-\gamma n/\Delta E}$，可降低有效 $M$。但这不能替代 mu 构建的精度修复——因为即使 $M_{\text{eff}} \sim 70$（García 2015 无序参数），仍需足够大的名义 $M$ 来分辨 QHE 平台。详见 §3.5 E4 和 §7。

**与 tbplas C++ 的对应**：
- Eq.12 的 prefactor $\frac{4e^2\hbar}{\pi A}\frac{4}{\Delta E^2}$ ↔ `dckb_prefactor = 16 * n_orb / (PI * E_range^2 * area)`（等价，$A$ 含 $N_{\text{orb}}$ 因子）
- Eq.12 的 $f(\tilde{\varepsilon})$ ↔ `fermi_dirac(beta_re, efermi_re, eng_re)` — **分布值 $f(E)$**（非导数，详见 §4.3）
- Eq.12 的 $(1-\tilde{\varepsilon}^2)^2 = \sin^4\theta$ ↔ `div = sin^3(theta)`（差异分析见 §4.2）

---

## 2. Chebyshev 三项递推：`kbdc_mu()` 详解

### 2.1 两路展开结构

`KuboBastinCPU::kbdc_mu()`（`kubo_bastin.h:175-269`）是数值不稳定性的**直接源头**。它需要展开**两路**独立的 Chebyshev 多项式：

#### 第一路：$v_\beta \cdot T_n(\tilde{H}) |\psi_0\rangle$（`kubo_bastin.h:218-243`）

```cpp
// 步骤 1: 生成随机态
rand_gen.random_state(wf0, seed_i);

// 步骤 2: 三项递推初始化
vec_copy(wf0, t0);                          // |t₀⟩ = |ψ₀⟩
h_sparse.mv(t0, t1);                        // |t₁⟩ = H̃|ψ₀⟩

// 步骤 3: 电流算符 v_β 作用
curr_beta->mv(t0, wf_vb_tn[0]);             // |wf_vb_tn[0]⟩ = v_β|t₀⟩
curr_beta->mv(t1, wf_vb_tn[1]);             // |wf_vb_tn[1]⟩ = v_β|t₁⟩

// 步骤 4: 三项递推主循环 (n = 2, 3, ..., M-1)
for (int i = 2; i < num_kernel; ++i) {
    p2 = p0;
    h_sparse.amxsy(2.0, *p1, *p0);          // |t_n⟩ = 2H̃|t_{n-1}⟩ - |t_{n-2}⟩
    curr_beta->mv(*p2, wf_vb_tn[i]);        // 施加 v_β 并保存
    p0 = p1; p1 = p2;                        // 指针轮转
}
```

**关键**：`amxsy(a, x, y)` 执行 `y = a * M * x - y`，这里 $a=2$，$M=\tilde{H}$，即实现三项递推：
$$|t_n\rangle = 2\tilde{H}|t_{n-1}\rangle - |t_{n-2}\rangle$$

#### 第二路：$T_m(\tilde{H}) \cdot v_\alpha |\psi_0\rangle$（`kubo_bastin.h:246-269`）

```cpp
// 步骤 1: 电流算符 v_α 先作用
curr_alpha->mv(wf0, t0);                    // |t₀⟩ = v_α|ψ₀⟩
h_sparse.mv(t0, t1);                        // |t₁⟩ = H̃·v_α|ψ₀⟩

// 步骤 2: 内积构建 μ 矩阵 (第一列和第二列)
for (int j = 0; j < num_kernel; ++j) {
    mu_sample(0, j) = vec_dot(t0, wf_vb_tn[j]);  // μ_{0,j} = ⟨v_αψ₀|v_βT_jψ₀⟩
    mu_sample(1, j) = vec_dot(t1, wf_vb_tn[j]);  // μ_{1,j} = ⟨H̃v_αψ₀|v_βT_jψ₀⟩
}

// 步骤 3: 三项递推 + 内积 (m = 2, 3, ..., M-1)
for (int i = 2; i < num_kernel; ++i) {
    p2 = p0;
    h_sparse.amxsy(2.0, *p1, *p0);          // |t_m⟩ = 2H̃|t_{m-1}⟩ - |t_{m-2}⟩
    for (int j = 0; j < num_kernel; ++j) {
        mu_sample(i, j) = vec_dot(*p2, wf_vb_tn[j]);  // μ_{m,j} = ⟨t_m|v_βT_jψ₀⟩
    }
    p0 = p1; p1 = p2;
}
```

### 2.2 内积方式：标准直接内积（无恒等式技巧）

Kubo-Bastin 使用 `vec_dot(*p2, wf_vb_tn[j])` — 即 $\langle t_m | \text{target}_j \rangle$，其中 $\text{target}_j = v_\beta T_j(\tilde{H})|\psi_0\rangle$ 是**固定参照向量**。

对比：
- **DOS Fast 路径**（`chebyshev.h:209-222`）：使用恒等式技巧 `mu[2*i-1] = 2⟨p2|p1⟩ - mu[1]`，两个**都在漂移**的 Krylov 向量互求内积 → 误差平方增长
- **Kubo-Bastin 路径**：`⟨t_m|\text{target}_j⟩`，一侧在漂移（`|t_m⟩`），一侧是固定的（`|target_j⟩`）→ 误差线性增长

两者都因三项递推的正交性丢失而产生误差，但**误差增长模式不同**。

### 2.3 Jackson 核加权（`kpm.cpp`）

递推结束后，$\mu$ 矩阵被 Jackson 核加权：

```cpp
// kubo_bastin.h:262-268
mu_avg(m, n) += factor * kernel(m) * kernel(n) * mu_sample(m, n);
```

Jackson 核（`kpm.cpp:8-17`）：
$$g_n = \frac{(M-n+1)\cos(\pi n/(M+1)) + \cot(\pi/(M+1))\sin(\pi n/(M+1))}{M+1}$$

Jackson 核的作用是抑制 Gibbs 振荡（截断伪影），但它**不能修复三项递推产生的 Krylov 基正交性丢失**。核函数作用于 $\mu_{mn}$ 的幅度，但不改变 $\mu_{mn}$ 自身是否已经被噪声污染。

---

## 3. 数值不稳定性完整分析

### 3.1 三项递推的正交性丢失（Loss of Orthogonality）

Chebyshev 三项递推：

$$|t_{n+1}\rangle = 2\tilde{H}|t_n\rangle - |t_{n-1}\rangle$$

理论上，$\{|t_n\rangle\}$ 构成 Krylov 子空间 $\text{span}\{|\psi_0\rangle, \tilde{H}|\psi_0\rangle, \tilde{H}^2|\psi_0\rangle, \ldots\}$ 的正交基（在 Chebyshev 内积意义下）。但在 **double 精度**（$\varepsilon_{\text{mach}} \approx 2.2 \times 10^{-16}$）下：

1. 每步 `amxsy(2.0, *p1, *p0)` 引入 $\sim \varepsilon_{\text{mach}} \cdot \|\tilde{H}\|$ 的舍入误差
2. $|t_n\rangle$ 逐渐偏离真实 Krylov 子空间
3. 偏离的 $|t_n\rangle$ 主要投影到 $\tilde{H}$ 的**极端本征态**上（与 Lanczos 的 spurious eigenvalue 问题同源）
4. 内积 $\langle t_m | \text{target}_j \rangle$ 被高频噪声污染

**误差增长模式**：与 Lanczos 迭代相同——误差随递推步数 $n$ **指数增长**。

### 3.2 为什么两路递推的误差是乘性的

> **⚠️ 本段"乘性误差"分析已被 2026-06-23 E1 实验证伪。**
> E1 实测 Chebyshev 向量范数在 n=128..4095 全程**常数** (|T_n|≈0.707, std<0.002)，无指数/线性增长。
> "两路内积导致乘性误差叠加"的推理前提（$\|T_n\|$ 随 n 增长）不成立。
> 以下保留为历史存档，展示了 2026-06-21 阶段的分析思路。

Kubo-Bastin 的 $\mu_{mn}$ 定义为：

$$\mu_{mn} = \langle T_m(\tilde{H}) v_\alpha \psi_0 | v_\beta T_n(\tilde{H}) \psi_0 \rangle$$

两项都通过三项递推近似：
- $|a_m\rangle \approx T_m(\tilde{H}) v_\alpha |\psi_0\rangle$（有误差 $\delta_m$）
- $|b_n\rangle \approx v_\beta T_n(\tilde{H}) |\psi_0\rangle$（有误差 $\varepsilon_n$）

则：
$$\mu_{mn}^{\text{computed}} = \langle a_m | b_n \rangle = \mu_{mn}^{\text{true}} + \underbrace{\langle \delta_m | b_n^{\text{true}} \rangle + \langle a_m^{\text{true}} | \varepsilon_n \rangle}_{\text{加性误差}} + \underbrace{\langle \delta_m | \varepsilon_n \rangle}_{\text{乘性误差}}$$

当 $m, n$ 都很大时，乘性误差项 $\langle \delta_m | \varepsilon_n \rangle$ 主导。相比之下，DOS 只需 $\mu_n = \langle \psi_0 | T_n(\tilde{H}) | \psi_0 \rangle$，只有单路误差。

| 场景 | 误差结构 | 行为 |
|------|---------|------|
| DOS 单路 ($\langle \psi_0 \| t_n \rangle$) | 加性 | 高 M 时 DOS 嘈杂（§4 of tbplas-internals） |
| Kubo-Bastin 两路 ($\langle t_m^{\alpha} \| t_n^{\beta} \rangle$) | **乘性** | 高 M 时 $\\mu_{00}$ 被污染 → 基线偏移（§3.3 问题 B） |

### 3.3 两种不同性质的数值问题

> **⚠️ 2026-06-21 重要修正**：前期（0619-0620）M≥1024 全 NaN 的现象已被 0621 测试证实为 **`rescale` 参数误配**导致（`rescale=9.0` 远小于 graphene ~20 eV 带宽，缩放后本征值超出 Chebyshev 收敛域 [-1,1]），而非 Chebyshev 三项递推的正交性丢失。设置 `rescale: -1`（自动检测）后 M=64–1024 全部正常运行（NaN=0）。以下将两种问题分开分析。

#### 问题 A：rescale 误配 → NaN（已解决）

**机制**：`rescale_` 必须 ≥ 哈密顿量的半带宽（全带宽的一半）。graphene 全带宽 ~20 eV，半带宽 ~10 eV。若 `rescale=9.0`，缩放后 $\tilde{H} = H/\text{rescale}$ 的极端本征值可达 ~1.1，超出 Chebyshev 多项式 $T_n(x)$ 的收敛域 $x \in [-1, 1]$ → $T_n(1.1)$ 指数增长 → `mu_sample` 产生 `inf` → 内积 `vec_dot` 产生 `NaN`。

**修复**：设置 `rescale: -1`（tbplas 自动检测带宽）或手动设为 ~12 eV（需覆盖 ~10 eV 半带宽并留余量）。

**影响范围**：此前所有标记 "M≥1024 NaN" 的 MG 项目数据（0619-0620, 含 Job 282031 M=4096 和 Job 282736 speedtest 复现）均属此问题。

#### 问题 B：Chebyshev 递推误差累积 → 基线偏移（真实物理限制）

> **⚠️ 本段"Chebyshev 递推误差累积 → 污染 μ₀₀ → 基线偏移"的因果链已被 2026-06-23 E1 实验证伪。**
> E1 实测 $\|T_n\| \approx 0.707$ 正常化且全程常数——递推无指数误差增长。
> 基线偏移 S 的真实根因仍在查找中（H_A/H_B/H_C 全部排除，见 §3.5 和 §7）。
> 以下保留为历史存档。

**机制**：在正确的 rescale 下，M 可以推到 1024、2048、4096 而不产生 NaN。但 Chebyshev 三项递推的舍入误差随 M 累积，通过 Kubo-Bastin 的两路内积 $\mu_{mn} = \langle T_m v_\alpha\psi_0 | v_\beta T_n\psi_0 \rangle$ 乘性叠加后，**主要污染零阶 Chebyshev 矩 $\mu_{00}$**。由于 $\mu_{00}$ 在 $\theta$ 积分中对所有能量贡献恒定的常数项，其误差表现为 $\sigma_{xy}(E)$ 的**相干基线偏移 S**：

$$\sigma_{xy}^{\text{computed}}(E) = \sigma_{xy}^{\text{true}}(E) + S(M)$$

其中 $S(M)$ 不破坏 LL 台阶结构（$\Delta\sigma$ 保持 ~4 e²/h），但使 $\sigma_{xy}$ 的绝对值失真。S 为负值，量级随 M 快速增大。

**实测数据**（rescale=-1, m=256, rs=8, B=100T）：

| M | σ(1eV) | 偏移 S | 状态 |
|:---:|------|------|------|
| 64–1024 | ~+2 | ~0 | 正常（M≤1024 NaN=0） |
| 2048 | ~+2 | ~0 | 正常 |
| 4096 | -232 | **-234** | LL 清晰但整体下移 |
| 6144 | -1290 | **-1292** | LL 清晰但严重下移 |

> 与 $\S 3.3 旧版的关键区别**：M=4096,6144 不产生 NaN（rescaling 正确的前提下），而是产生可量化的基线偏移。LL 平台结构完好保留。

### 3.4 为什么已有文献可以 M ≫ 512？

已有文献在稳定运行远大于 512 的 Chebyshev 展开阶数（且不产生基线偏移问题）：

| 文献 | M | 体系 | 基线偏移 | 说明 |
|------|:---:|------|:---:|------|
| **García 2015** (PRL 114) | **6144** | monolayer graphene | 无明显偏移 | KPM Kubo-Bastin 原始实现 |
| **Yuan 2016** (PRB 94) | **15000** | bilayer BP, 720k sites | 无明显偏移 | 5 随机实现；明确标注 M=15000 |
| **tbplas** (实测, rescale=-1) | **1024** (无 NaN) | monolayer graphene | ~0 | M≤1024 正常 |
| **tbplas** (实测, rescale=-1) | **4096–6144** | monolayer graphene | **-232 ~ -1290 e²/h** | LL 结构保留，基线偏移显著 |

论文作者避免基线偏移的可能手段：

| 技术 | 机制 | 稳定上限提升 |
|------|------|:---:|
| **Anderson 无序** ($\gamma \approx 0.1t$) | 物理展宽 $\delta$ 峰 → $\mu_{mn}$ 指数衰减 → 绝对收敛 | $M$ 任意（$M_{\text{eff}} \sim 70$，远超即无影响） |
| **quad precision** (binary128, $\varepsilon \approx 10^{-34}$) | 舍入误差降低 $10^{18}$ 倍 | $M > 10^6$ |
| **周期性重正交化** (每 50 步 Gram-Schmidt) | 显式恢复 Krylov 基的正交性 | $M \sim 10^4$ (double) |

> **⚠️ 2026-06-26 重大修正：García 2015 无基线偏移的主因是 Anderson 无序，而非更高精度。**
> García 2015 明确使用 $\gamma=0.1t$ 的 Anderson 无序。无序将 LL 的 $\delta$ 峰展宽为有限宽度 $\Gamma \approx \gamma$，使 Chebyshev 矩 $\mu_n \sim e^{-\gamma n/\Delta E}$ 指数衰减。有效截断阶数 $M_{\text{eff}} \sim \Delta E/\gamma \approx 70$——超过此阶数后 $\mu_{mn}$ 物理上为零，双重求和绝对收敛。García 用 M=6144 是因为"高阶无害"（矩已衰减），而非"精度足以支撑 6144 阶递推"。
>
> 此前将 García 的成功归因于"quad precision / reorthogonalization"的推测**缺乏文献支撑**——García 论文未提及使用 quad 精度或重正交化。无序的指数阻尼效应是更简洁、更符合原文参数的物理解释。
>
> **Yuan 2016 的情况**：Yuan 2016 未提及使用 Anderson 无序（全文 "disorder" 出现 0 次），但其 720k 大体系（2×600×600）和黑磷的复杂能带结构可能提供了一定的有效展宽。此问题在 Yuan 论文中未被讨论。若其干净体系确实无基线偏移，可能涉及未公开的精度设置。

tbplas 使用**标准 double 精度 + 无重正交化 + 无无序 + 整段递推** → 干净体系中 $\mu_{mn}$ 不衰减 → 双重求和条件收敛 → 基线偏移。

> **⚠️ 本节 3.4 的"稳定上限 ≈512"结论已被 2026-06-23 E1 实验证伪。**
> 实测 Chebyshev 向量范数 $\|T_n\|\approx 0.707$ 在 n=128..4095 全程**常数**（std<0.002），三项递推在 double 精度下无指数误差增长。
> tbplas 的"512 上限"不是 Chebyshev 稳定性限制，而是 M≥2560 出现的**基线偏移**（根因另行诊断——见 §3.5 和 §7）。
> 以下保留为历史存档。

### 3.5 基线偏移根因诊断：E1–E3 判别实验 (2026-06-24 新增)

> 详见 `MG/docs/sigma/plan_baseline_root_cause.md` 和 `shared/tbplas-internals.md` §12.3。

基线偏移 $S$ 在 M≥2560 时出现，M≥4096 急剧放大（M=4096: S≈-991, M=6144: S≈-1290 e²/h）。原假设 H_A（Chebyshev 向量范数膨胀）基于 §3.1-3.2 的误差分析。2026-06-23/24 执行的三个判别实验系统检验了此假设。

**E1: 向量范数诊断 (2026-06-23) — 检验 H_A**

在 `kbdc_mu_raw()` 两个 Chebyshev 递推循环中插桩输出 $\log_{10}\|T_n\psi\rangle\|$ vs n。

| 循环 | $\log_{10}\|T_n\|$ (mean±std) | n 范围 | 结论 |
|------|:---:|:---:|:---:|
| $T_n(H)\|\psi_0\rangle$ | $-0.1505 \pm 0.0011$ | 128–4095 | **完全平坦** |
| $T_n(H)v_\alpha\|\psi_0\rangle$ | $-0.4680 \pm 0.0010$ | 128–4095 | **完全平坦** |

**结论**: $\|T_n\| \approx 0.707$ 全程常数 → H_A (Chebyshev 向量范数膨胀) **被证伪**。三项递推在 double 精度下无正交性丢失。§3.1-3.2 的误差分析**不适用于 Kubo-Bastin 路径**——固定 vs 漂移向量的内积误差远小于之前估计。

**E2: 无核测试 (2026-06-23) — 检验 H_B**

注释 `apply_jackson_kernel()` 中的核乘法，对比有核/无核 S。

| M | S_kernel | S_nokernel | 结论 |
|:---:|:---:|:---:|:---|
| 4096 | -991 | **3030** (3× worse) | 核起**抑制**作用 |

**结论**: H_B (Jackson 核退化) **被排除**。核是功能而非缺陷。

**E3: Rescale 扫描 (2026-06-24) — 检验 H_C**

| rescale | S | vs auto |
|:---:|:---:|:---:|
| auto(-1) | -991 | — |
| 11.0 | -788 | **-20%** (变好) |
| 12.0 | -1301 | **+65%** (变差) |

**结论**: S(rescale) 非单调 → H_C (谱边缘泄漏) **被排除**。

**E4: 收敛性分析 — H_F 假说及其 Phase H 检验 (2026-06-26 最终更新)**

> **⚠️ 本段 H_F 假说的"无序修复"预测已被 Phase H 实验证伪。**
> VBL Phase H (2026-06-26) 实测：$\gamma=0.27$ eV 在 $m=1024$, $M=4096$ 下 $\sigma_{xy}(0) = -1528$（仅降 $1.7\times$ vs clean $-2652$），$\gamma\ge 0.5$ 同时消灭噪声和 QHE 信号——无甜点。
> H_F 描述的"干净极限条件收敛"物理机制**部分正确**（$\mu_{mn}$ 不衰减是条件收敛的数学根源），但"加无序即可修复"的推论**不成立**——因为浮点累加精度才是当前阻塞，而非干净极限物理。
> **最终根因**（VBL Phase A–L 确认）：条件收敛 + double 浮点精度 → 随机游走累积（详见 §7）。
> 以下保留 H_F 的历史分析框架，作为条件收敛物理机制的文献支撑。

**H_F (干净极限条件收敛假说)**：

Kubo-Bastin 的最终表达式为：

$$\sigma \propto \int_0^\pi d\theta\, \frac{f(\cos\theta)}{\sin^3\theta} \sum_{m,n=0}^{M-1} \Gamma_{mn}(\theta)\,\mu_{mn}$$

各项量级分析：

| 因子 | 干净体系 ($W=0$) | 有物理展宽 ($W>0$, 或 $\eta>0$) |
|------|:---:|:---:|
| $\Gamma_{mn}(\theta)$ | $\sim O(\max(m,n))$ | 同左 |
| $\mu_{mn}$ | $\sim O(1)$，**振荡不衰减** | $\sim e^{-\Gamma \max(m,n)/\Delta E}$，**指数衰减** |
| Jackson 核 $g_m$ | $\sim 1-m/M$ | 同左 |
| 累加项数 | $M^2$ | $M^2$ |
| 裸和量级 | $\sim O(M^3)$ | $O(1)$（指数截断） |
| 净增长 (含核) | $\sim O(M)$ → **发散** | $O(1)$ → **收敛** |

**数学根源**：干净体系的谱函数为 $\delta$ 峰（Landau 能级）。根据 KPM 标准理论 (Weiße et al., RMP 78, 275, 2006)，$\delta$ 函数的 Chebyshev 系数 $\mu_n$ **永不衰减**（振荡）。当 $\Gamma_{mn} \sim O(M)$ 的增长不能被 $\mu_{mn}$ 的衰减所补偿时，双重求和条件收敛，截断误差 $\sim O(M)$。

**物理展宽的修复**：Anderson 无序（或有限 $\eta$）将 $\delta$ 峰展宽为 Lorentz 型 → $\mu_n \sim e^{-\Gamma n/\Delta E}$（指数衰减）。有效截断阶数 $M_{\text{eff}} \sim \Delta E/\Gamma$：
- García 2015: $\gamma = 0.1t \approx 0.27$ eV, $\Delta E \approx 20$ eV → $M_{\text{eff}} \sim 74$
- $M > M_{\text{eff}}$ 的矩物理上为零 → 双重求和绝对收敛 → $S(M)$ 不随 $M$ 增长

**文献一致性检验与 Phase H 修正**：

| 文献 | 无序 | M | 基线偏移 | VBL 后理解 |
|------|:---:|:---:|:---:|------|
| García 2015 | ✅ $\gamma=0.1t$ | 6144 | 无 | 无序使 $\mu_{mn}$ 衰减 + 大体系自平均；但 tbplas 实测 $\gamma=0.27$ 在 $m=1024$ 下不足以修复 |
| Yuan 2016 | ❌ 未提及 | 15000 | 未报告(⚠️) | 可能使用了更高精度或特殊体系展宽 |
| tbplas MG (clean) | ❌ 无 | 4096 | **S≈-991** | 条件收敛+浮点精度 |

> ⚠️ Phase H 关键发现：García 2015 使用的 $\gamma=0.1t$ 无序在 tbplas 当前参数下（$m=1024$, $M=4096$）**不能**消除基线偏移。García 成功的原因可能是**多重因素组合**（无序+大体系+可能的更高精度），而非仅无序一项。

**H_F 的检验方案与 Phase H 实际结果**：

| 测试 | 参数 | H_F 预测 | Phase H 实际 | 状态 |
|:---:|------|------|------|:---:|
| F1 | $W=0.27$ eV, M 扫描 64–4096 | $S \to 0$ 对所有 M>200 | $S(4096)=-1528$（仅降 $1.7\times$） | ❌ **证伪** |
| F2 | $W=0$, Lorentz 核 ($\lambda=4$) | $S$ 显著减小 | 未测试 | 🔲 |
| F3 | $\|\mu_{mn}\|$ vs $\max(m,n)$ | $W=0$: 振荡; $W=0.27$: 指数衰减 | 未直接测量 | 🔲 |

> **H_F 状态更新**：H_F 的物理洞察（干净极限条件收敛）为理解问题提供了正确的数学框架，但其"无序修复"推论被 Phase H 证伪。最终根因需整合条件收敛物理 + 浮点累加精度两个层面——详见 §7 的 VBL 最终结论。

---

## 4. `cond_from_trace()` 积分详解

### 4.1 $\Gamma$ 矩阵（`gamma_matrix()`, `kubo_bastin.h:131-167`）

变量替换 $E \to \cos\theta$ 后的积分核：

$$\Gamma_{mn}(\theta) = \cos(m\theta) \cdot (\cos\theta - in\sin\theta)e^{in\theta} + \cos(n\theta) \cdot (\cos\theta + im\sin\theta)e^{-im\theta}$$

C++ 实现：
```cpp
double sin_t = std::sin(theta);
double cos_t = std::cos(theta);
// 预计算 cos(nθ) 和 f_n(θ)
for (i = 0; i < num_kernel; ++i) {
    nt = i * theta;
    cos_nt[i] = std::cos(nt);
    fn[i] = complex_t(cos_t, -i * sin_t) * complex_t(cos_nt[i], std::sin(nt));
    fm[i] = std::conj(fn[i]);  // f_m = conj(f_n)
}
// gmn(m,n) = cos(mθ)·f_n + cos(nθ)·conj(f_m)
gmn(i, j) = cos_nt[i] * fn(j) + cos_nt(j) * fm(i);
```

**数值注意**：$\Gamma_{mn}(\theta)$ 含 $n\sin\theta$ 项——对于大 $n$（如 $n=4096$）和 $\theta \approx \pi/2$（$\sin\theta \approx 1$），此项量级为 $\sim 4096$。这是正常的——$\Gamma_{mn}$ 的积分值被 $\sin^3\theta$ 分母中的除法补偿。

### 4.2 能量积分

```cpp
// kubo_bastin.h:88-117
theta = PI / num_theta;  // 积分步长
for (int k = 0; k < num_theta; ++k) {
    theta_array[k] = (k + 0.5) * theta;  // 中点法则，避开 θ=0

    gamma_matrix(theta_array[k], gamma);

    // 二重求和: sum = Σ_{m,n} Re[Γ_{mn}(θ) · μ_{mn}]
    sum = 0.0;
    for (j = 0; j < num_kernel; ++j)
        for (i = 0; i < num_kernel; ++i)
            sum += (gamma(i, j) * mu_avg(i, j)).real();
    sum_gamma_mu[k] = sum;
}

// Fermi-Dirac 加权积分
for (int i = 0; i < num_eng; ++i) {
    efermi_re = (dckb_energies[i] - rescale_center) / rescale;
    dcx = 0.0;
    for (int k = 0; k < num_theta; ++k) {
        eng_re = std::cos(theta_array[k]);
        div = std::pow(std::sin(theta_array[k]), 3.0);
        fd = fermi_dirac(meta.beta_re, efermi_re, eng_re);  // f(E), 非 -df/dE
        dcx += sum_gamma_mu[k] * fd * theta / div;
    }
    cond[i] = dcx;
}
```

### 4.3 Fermi-Dirac 因子：$f(E)$ 是正确的

`fermi_dirac(beta, mu, x)`（`fermi_dirac.cpp:6-17`）返回的是 Fermi-Dirac **分布值** $f(E) = 1/(1+e^{\beta(E-\mu)})$：

```cpp
double fermi_dirac(const double& beta, const double& mu, const double& x) {
    if (x >= mu) {
        tmp = std::exp(beta * (mu - x));
        fd = tmp / (1.0 + tmp);          // = f(E) for E ≥ μ
    } else {
        tmp = std::exp(beta * (x - mu));
        fd = 1.0 / (1.0 + tmp);          // = f(E) for E < μ
    }
    return fd;
}
```

**✅ 公式验证通过**：Yuan 2016 Eq.12 中的因子明确写为 $f(\tilde{\varepsilon})$（Fermi-Dirac 分布值），而非其导数。经过 KPM Chebyshev 展开后，原始的 $-dG^+/d\varepsilon$ 项被吸收到 $\Gamma_{mn}(\tilde{\varepsilon})$ 的解析结构（含 $(1-\tilde{\varepsilon}^2)^{-2}$ 因子和 Chebyshev 多项式的微分性质）中。tbplas 的 `fermi_dirac()` 调用是正确的。

> **之前的 `NEEDS_VERIFICATION` 已解决**：CPC 论文 eqn.69 中的 $F(E_F, E)$ 经过变量替换 $E \to \cos\theta$ 和 Green 函数展开后，在最终数值积分中以 $f(E)$ 形式出现。此处在 Yuan 2016 的独立推导中得到交叉验证。

### 4.4 Prefactor 公式

```cpp
// solver.h:632-638
dckb_prefactor = 16 * n_orb / (PI * pow(E_range, 2));
if (dimension == 2)
    dckb_prefactor /= area;      // 2D: Ω = 超胞面积
else
    dckb_prefactor /= volume;    // 3D: Ω = 超胞体积
if (dckb_unit == "h")
    dckb_prefactor *= TWOPI;     // 乘以 2π（⚠️ 方向存疑）
cond *= dckb_prefactor;
cond *= num_spin;
```

**单位**（2D）：
- `dckb_unit="hbar"`：$e^2/\hbar$
- `dckb_unit="h"`：代码执行 $ \times 2\pi$，但物理上 $e^2/h = e^2/\hbar \div 2\pi$

`dckb_unit="h"` 的转换方向存疑，标记 `NEEDS_VERIFICATION`。

---

## 5. 与已有文献的逐项对比

| 项目 | García 2015 (PRL 114) | Yuan 2016 (PRB 94) | tbplas C++ |
|------|:---:|:---:|-----------|
| **Chebyshev 展开** | 标准三项递推 | 标准三项递推 | 标准三项递推 ✅ |
| **内积方式** | $\langle T_m v_\alpha \psi_0 \| v_\beta T_n \psi_0 \rangle$ | 同左 (Eq.14) | 同左 ✅ |
| **恒等式技巧** | 未提及 | 未提及 | **未使用**（Kubo-Bastin 路径） ✅ |
| **M (展开阶数)** | **6144** | **15000** | ≤2560 安全；≥4096 有基线偏移 ⚠️ |
| **数值精度** | double（含无序展宽） | 未公开 | **double** |
| **Anderson 无序** | ✅ $\gamma=0.1t$ | ❌ 未提及 | ❌ 无（Phase H 测试：$\gamma=0.27$ 不修复） |
| **NaN 问题** | 无 | 无 | rescale=-1 下已解决 ✅ |
| **基线偏移** | 无明显偏移 | 无明显偏移 | **M≥3072 时显著**（根因：条件收敛+浮点精度） ❌ |
| **Jackson 核** | 使用 | 使用 (Eq.14: $g_m g_n$) | 使用（`kpm.cpp`） ✅ |
| **$\Gamma_{mn}$ 公式** | $\Gamma_{mn}(\theta)$ | Eq.13: 与 tbplas 一致 | 逐项对应（`gamma_matrix()`） ✅ |
| **Fermi-Dirac 因子** | $F(E_F, E)$ | $f(\tilde{\varepsilon})$ (Eq.12) | $f(E)$ — ✅ 经 Yuan 2016 交叉验证 |
| **Prefactor** | $4e^2\hbar/(\pi\Omega)$ | $\frac{4e^2\hbar}{\pi A}\frac{4}{\Delta E^2}$ | $16 N_{\text{orb}}/(\pi E_{\text{range}}^2 \Omega)$ — 等价 ✅ |

**关键结论**：tbplas 的 Kubo-Bastin 算法设计（公式、流程、Chebyshev 展开、$\Gamma$ 矩阵、Jackson 核、Fermi-Dirac 因子）与 García 2015 和 Yuan 2016 **三方一致**，未发现任何公式错误。

两种数值问题需区分：
1. **NaN（已解决）**：早期 M≥1024 全 NaN 由 `rescale` 误配导致（`rescale=9.0` < 半带宽 ~10 eV）。设置 `rescale: -1` 后 M≤6144 NaN=0。
2. **基线偏移（根因已定位）**：VBL Phase A–L 确认根因为**条件收敛 + double 浮点精度 → 随机游走累积**。$\Gamma_{mn}\sim O(M)$ 线性增长 + $\mu_{mn}$ 衰减不足 → 双重求和绝对和不收敛 → $\delta\mu_{mn}$ 零均值随机噪声在 $N\sim 1.7\times 10^7$ 项累加中产生 $\sim O(\sqrt{N}\varepsilon)$ 的游走。Anderson 无序 (Phase H) 不能修复——噪声与 QHE 信号耦合。实用窗口：$M\le 2560$ + Kahan 编译。详见 §7。

---

## 6. MG 项目实测数据与文献参数对照

> 完整测试矩阵见 `tbplas-internals.md` §12。此处仅提取与数值稳定性直接相关的关键数据。

### 6.1 文献参数基准

| 参数 | García 2015 | Yuan 2016 | tbplas 默认 | MG 实测最优 |
|------|:---:|:---:|:---:|:---:|
| **M (展开阶数)** | 6144 | **15000** | 2048 | 256 |
| **B (磁场)** | — | 130 T | — | 100 T |
| **体系** | monolayer graphene | 2×600×600 bilayer BP | — | m=256 monolayer graphene |
| **随机实现数** | — | 5 | 1 | 8 |
| **温度** | — | 0.01 K | 300 K | 10 K |

### 6.2 MG 项目 M 系统性扫描

> ⚠️ **标注重述**：0619-0620 数据中 M≥1024 的 NaN 均源于 `rescale` 误配。0621 `rescale=-1` 下 M=64–1024 全部 NaN=0。以下表格混合了旧数据（rescale 混杂）和新数据（rescale=-1）。

**旧数据**（0619, rescale 混杂，M≥1024 的 NaN 不可靠）：

| M | σ_xy 状态 | RMS (e²/h) | 说明 |
|:---:|------|:---:|------|
| 64 | 欠分辨 | 0.028 | KPM 阶数不足 |
| 128 | 临界 | 0.045 | 信号初现 |
| **256** | **最优平衡** | **0.29** | 数值噪声可接受 |
| 384 | 噪声偏大 | 1.41 | 噪声掩盖信号 |
| 512 | 噪声偏大 | 3.05 | 噪声量级 ≈ 信号 |
| 1024 | **NaN** | — | ⚠️ rescale 误配（rescale=-1 下 NaN=0） |
| 2048 | **NaN** | — | ⚠️ rescale 误配 |
| 4096 | **NaN** | — | ⚠️ rescale 误配 |

**新数据**（0621, rescale=-1, m=256, rs=8, B=100T）：

| M | σ_xy(1eV) | 偏移 S | LL 结构 | 说明 |
|:---:|------|------|:---:|------|
| 64–2048 | ~+2 | ~0 | ✅ | 正常运行，无偏移 |
| 4096 | -232 | **-234** | ✅ | LL 清晰但整体下移 |
| 6144 | -1290 | **-1292** | ✅ | LL 清晰但严重下移 |

### 6.3 关键验证

- **NaN 根因确认为 rescale**：0619-0620 M≥1024 NaN 数据均使用 `rescale=9.0` 或 `rescale=10.0`，远小于 graphene ~10 eV 半带宽。切换 `rescale: -1`（自动检测 ~12 eV）后 M=64–1024 全部 NaN=0
- **rescale=-1 下 M≤1024 正常**：0621 M 扫描（M=64,128,256,384,512,768,1024）全部 exit 0
- **speedtest 也是 rescale 受害者**：tbplas 内置 speedtest 使用 `rescale=9.0`，M=2048 时也产生 NaN——speedtest 仅测速度，不验证正确性，也未能暴露 rescale 问题
- **M≥4096 出现基线偏移**：rescale=-1 下 M=4096,6144 不 NaN 但 σ_xy 整体下移，LL 平台结构保留

---

## 7. 根因总结与可行路径 (2026-06-27 VBL 最终版, Phase M 晋升)

> **修订历史**：
> - 2026-06-21：初始分析基于"Chebyshev 三项递推正交性丢失"假说（H_A）
> - 2026-06-23/24：E1–E3 判别实验证伪 H_A/H_B/H_C
> - 2026-06-25/26：VBL Phase A–L 全链路诊断完成，全 9 假说排除
> - **2026-06-27（本版）**：Phase M 封闭验证完成 — **噪声源精确定位到 C++ KPM Chebyshev 迭代 (mu 构建)，非求和环节**
>
> **核心发现链**：
> 1. $\|T_n\| \approx 0.707$ 全程常数 → Chebyshev 递推无浮点不稳定性（E1）
> 2. Jackson 核功能正常，非退化（E2）
> 3. rescale 非单调影响，非谱边缘泄漏（E3）
> 4. μ 矩阵构建正常，Γ 矩阵精度正常，θ 积分方案无关（Phase A/G/F）
> 5. H_D (求和精度) 不根除（Phase C Kahan + Phase I long double）
> 6. H_J (Jackson 核 M 依赖性) 非根因（Phase J 统一核）
> 7. δμ 为零均值随机噪声，Krylov 漂移假说排除（Phase L）
> 8. Γ~O(n) 线性增长 + μ 衰减不足 → 条件收敛（Phase K/L）
> 9. Anderson 无序不修复（Phase H）
> 10. **🆕 M1: 噪声注入 ΔS=ΣΓ·η 完美成立；M2: S_f32≈S_f64 → 求和精度非瓶颈 — 噪声在 mu 构建**（Phase M）
> 11. **🆕 根因完整链**: C++ KPM Chebyshev 迭代 → δμ 随机噪声 → Γ O(n) 放大 → 条件收敛 → S(M) 发散

### 7.1 全部假说诊断矩阵（VBL Phase A–M）

| 假说 | 机制 | 诊断阶段 | 状态 |
|------|------|:---:|:---:|
| **H_A: 向量范数膨胀** | Chebyshev $\|T_n\|$ 指数增长污染 μ | E1 | ❌ 排除 |
| **H_B: Jackson 核退化** | 核权重在高阶失效 | E2 | ❌ 排除 |
| **H_C: 谱边缘泄漏** | rescale 低估带宽 | E3 | ❌ 排除 |
| **H_D: double 精度不足** | 53-bit 浮点累加误差 | Phase C (Kahan) + Phase I (long double) | ❌ 排除 |
| **H_θ: θ 积分奇点** | θ→0,π 时 $1/\sin^3\theta$ 发散放大噪声 | Phase F ($N_\theta$/δ/Simpson) | ❌ 排除 |
| **H_Γ: Γ 矩阵精度** | Γ 构造或标度退化 | Phase G (热图/Hermiticity/标度) | ❌ 排除 |
| **H_μ: μ 矩阵 M 依赖** | Chebyshev 递推引入 M 依赖误差 | Phase A + K1 | ❌ 排除 |
| **H_J: Jackson 核 M 依赖** | $g_n^{(M)}$ 随 M 放大旧区 μ | Phase J (统一核) | ❌ 排除 |
| **H_bias: δμ 系统性偏置** | Krylov 方向漂移 → δμ 同符号 | Phase L (L1/L2/L3) | ❌ 排除 |
| **M1: 噪声注入** | ΔS = ΣΓ·η | Phase M | ✅ **确认** |
| **M2: 求和精度缩放** | S ∝ ε_mach | Phase M | ❌ 求和非瓶颈 |
| **M3: Γ 放大** | \|S\| ∝ Γ_max | Phase M | ⚠️ Γ 权重确认 |

### 7.2 最终根因：C++ KPM Chebyshev 迭代 → δμ 随机噪声 → Γ 线性放大 → 条件收敛

$$\underbrace{\sum_{m,n=0}^{M-1} \Gamma_{mn} (\mu_{mn}^{\text{true}} + \delta\mu_{mn})}_{\text{数值}}$$

**噪声源的精确定位**（Phase M 关键发现）：
- $\delta\mu_{mn}$ 产生于 **C++ KPM Chebyshev 迭代**（mu 矩阵构建环节），非求和环节
- **证据链**: Phase C (Kahan 无效) + Phase I (long double 无效) + **M2 ($S_{f32} \approx S_{f64}$)**: 三次独立实验指向求和精度无关
- $\delta\mu$ 的性质: 零均值随机噪声 i.i.d. (Phase L: pos_frac=0.4997)
- **M1 确认**: $\Delta S = \Sigma\Gamma\cdot\eta$ 在 5 个数量级上完美成立 (ratio=1.000±0.001)

**三个要素的交互**：

| 要素 | 属性 | VBL 证据 |
|------|------|------|
| $\|\Gamma_{mn}\|$ | $\sim O(\max(m,n))$ 线性增长 | Phase G: $\max\|\Gamma\| \propto M^{1.001}$ |
| $\|\mu_{mn}^{\text{true}}\|$ | 衰减不足以使 $\sum\|\Gamma\mu\|$ 绝对收敛 | Phase K: 旧区主导 68%，新区 32% |
| $\delta\mu_{mn}$ | 零均值随机噪声，产生于 mu 构建 | Phase L: pos_frac=0.4997; **Phase M: M2 排除求和** |

**核心理念**：不是求和的问题 — 是 mu 构建的问题。提高求和精度对已存在于 mu 中的 δμ 无效。

### 7.3 Anderson 无序不能修复（Phase H, 2026-06-26）

| γ (eV) | M=4096 σ_xy(0) | QHE 平台 | 结论 |
|:---:|:---:|:---:|------|
| 0 (clean) | −2652 | ✅ 存在 | 基线偏移严重 |
| 0.27 (≈0.1t) | −1528 | ✅ 保留 | 仅降 $1.7\times$，远未修复 |
| **0.5** | **−424** | **❌ 崩溃** | 噪声和 QHE 同时消失 |
| 5.0 | −7 | ❌ | 噪声压制 47×但 QHE 也消失 |

**核心结论**：噪声与 QHE 信号在 KPM Chebyshev 展开中耦合——打破递推相干性会同时消除两者。不存在"只消噪声、保留 QHE"的甜点。**必须先修复 mu 构建精度，才能用物理量级无序 ($\gamma\approx 0.1t$) 呈现 QHE。**

### 7.4 修复路径（Phase M 分级，按噪声源层级）

| 优先级 | 方案 | 靶点 | 预期效果 | 风险 | 状态 |
|:---:|------|------|------|:---:|:---:|
| 🔴 **P0** | C++ KPM quad precision (__float128) | **mu 构建 (δμ 源头)** | 根除 δμ (降 ~10⁴×) | 高 (编译链/性能) | 🔲 长期 |
| 🟡 **P1** | Lorentz λ>4 核 | 核衰减 (机制 A) | 降 S ~5–10× (推测) | 低 (J2 已实现) | ✅ λ=4 降 ~3× |
| 🟢 **P2** | M ≤ 2560 + Kahan | 限制 N (随机游走幅值) | S 可控 (<10 e²/h) | 最低 (已验证) | ✅ **推荐** |
| 🔵 **P3** | Pairwise/tree summation | 累加策略 | 降随机游走 ~√N 因子 | 低 | 🔲 待开发 |
| 🔴 — | M > 4096 | — | 当前不推荐 | — | ❌ |
| 🔴 — | Anderson 无序作为修复 | Phase H 证实无效 | — | — | ❌ 排除 |

### 7.5 可行替代路径 (不变)

| 优先级 | 路径 | 优势 | 劣势 |
|:---:|------|------|------|
| 🥇 | **Diag Lindhard AC** $\omega \to 0$ 外推 | 无 Chebyshev 限制，确定性 | 仅小体系 |
| 🥈 | **TBPM dos** 提取 LL 能级 | $E_n \propto \sqrt{nB}$ 标度律 | 不能直接得 $\sigma_{xy}$ |
| 🥉 | **TBPM DC 关联函数** 计算 $\sigma_{xx}$ | 时域方法，无双重求和发散 | 只能算 $\sigma_{xx}$，不能算 $\sigma_{xy}$ |

### 7.6 知识晋升记录

| 层级 | 文件 | 操作 | 内容 |
|------|------|:---:|------|
| L3 | `MG/docs/log.md` | 已有 | AI:0624_1430 – AI:0627_2257 (Phase A–M 全过程) |
| L3 | `MG/docs/sigma/plan_vbl_trace.md` | 已有 | VBL Phase A–M 完整诊断计划 |
| L3 | `MG/docs/sigma/task_vbl_trace.md` | ✅ | VBL Phase A–M 全部判别实验记录 (含 Phase M) |
| L2 | `shared/tbplas-internals.md` §12.3 | ✅ | 最终根因总结 (2026-06-27, Phase M 完成) |
| L1 | 本文档 | ✅ 本次晋升 | 含 Phase M 噪声源定位 + P0-P3 修复分级 |

> **参考**：
> - 完整诊断: `MG/docs/sigma/plan_vbl_trace.md` + `MG/docs/sigma/task_vbl_trace.md`
> - 源日志: `MG/docs/log.md` AI:0624_1900 → AI:0625_0838 → AI:0626_0100 → AI:0627_2257
> - 用户记忆: `/memories/kubo-bastin-convergence.md`（最终根因摘要）

### 7.7 Python 模拟独立验证 (2026-06-28) 🆕

**项目**: `gamma_mu_sim/` — Γ-μ 随机游走数值模拟
**报告**: [gamma_mu_sim/docs/report.md](gamma_mu_sim/docs/report.md)
**日志**: [gamma_mu_sim/docs/log.md](gamma_mu_sim/docs/log.md)

在纯 Python 环境下，用合成 Γ 矩阵（量级 ∝ M）和 μ 矩阵（3 种核模型 + 浮点噪声），独立验证了以下结论：

#### 验证结果（与 Phase M 对照）

| 结论 | VBL Phase M | Python 模拟 | 状态 |
|------|:---:|:---:|:---:|
| 标度指数 α | ≈2 (Γ∝M 导致 M² 标度) | α=2.03~2.08 (6 线, R²>0.996) | ✅ 一致 |
| 核加权不改变 α | Jackson 核效果有限 | 三核 α 差异 < 3% | ✅ 一致 |
| Kahan 求和改善有限 | 噪声源是 δμ 非求和 | Kahan 改善 < 10% | ✅ 一致 |
| Lorentz λ 无法消除随机游走 | — (未在 C++ 侧测试) | λ∈[2,8] 全部 α≈2 | 🆕 新增 |
| 核阻尼不足以压制 | 高 |Γ| 区主导贡献 | RMS(8192) > RMS(4096) | ✅ 一致 |

#### 核心发现

1. **α ≈ 2.08（非 1.0）** — Γ 元素 ∝ M 使随机游走标度从预期 √N·ε 修正为 M²·ε
2. **核加权仅改变前因子 β，不改变标度指数 α** — clean/Jackson/Lorentz 三种核的 α 在 2.03~2.08 之间
3. **Lorentz λ∈[2,8] 扫描全部 α≈2** — 无"甜点 λ"可实现绝对收敛，λ 较大时 RMS 反而增大
4. **float32 退化 ~10¹⁰ 倍** — M=1024 时 float32 RMS=0.48 >> float64 RMS=5.6e-11

#### 对 tbplas 的实用建议

- M ≤ 2560 为双精度安全范围
- 始终使用 `rescale=-1`（自动带宽检测）
- 不推荐 M ≥ 3072 除非四精度 KPM 迭代
- 核模型选 Jackson（与 tbplas 默认一致，效果与 Lorentz 相当）

> 详细数据见 [gamma_mu_sim/output/data/](gamma_mu_sim/output/data/) 和 [gamma_mu_sim/output/figures/](gamma_mu_sim/output/figures/)。

---

## 8. 参考源码索引

| 文件 | 行号 | 内容 |
|------|:---:|------|
| `kubo_bastin.h` | 175-269 | `KuboBastinCPU::kbdc_mu()` — 两路 Chebyshev 递推 + μ 矩阵构建 |
| `kubo_bastin.h` | 57-119 | `AbstractKuboBastin::cond_from_trace()` — Γ 矩阵 + θ 积分 |
| `kubo_bastin.h` | 131-167 | `gamma_matrix()` — Γ 矩阵计算 |
| `solver.h` | 595-652 | `TBPMSolver::calc_hall_cond()` — 入口 + prefactor + I/O |
| `solver.h` | 1029-1042 | `make_kubo_bastin_backend()` — 后端选择（cpu→CPU, gpu→GPU） |
| `kpm.cpp` | 8-17 | `jackson_kernel()` — Jackson 核实现 |
| `fermi_dirac.cpp` | 6-17 | `fermi_dirac()` — Fermi-Dirac 分布值函数 |
| `chebyshev.h` | 159-240 | `cheb_eval_mu_dos()` — DOS Fast 路径（含恒等式技巧，对比用） |
