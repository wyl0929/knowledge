<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-08 15:20:56
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-08 15:20:57
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/04_sigma_xx_equivalence.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-08
 * @FilePath     : /home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/04_sigma_xx_equivalence.md
 * @Description  : σ_xx 两条路径等价性证明 — Kubo-Bastin (Chebyshev 能量域) vs TBPM DC 关联函数 (时域)
 * @References   :
 *   - Fan et al. 2021, Physics Reports 903, 1–69 (LSQT review — 统一推导框架)
 *   - 02_kubo_bastin_deep_dive.md (Kubo-Bastin Hall C++ 深度解析)
 *   - 03_tbpm_dc_correlation.md (TBPM DC 关联函数 C++ 深度解析)
 *   - García 2015, PRL 114, 116602 (KPM Kubo-Bastin 原始实现)
 *   - Yuan 2016, PRB 94, 195434 (KPM Kubo-Bastin on black phosphorus)
 *   - Li et al. 2023, CPC 293, 108887 (TBPLaS code paper)
-->

# σ_xx 两条路径等价性证明 — Kubo-Bastin vs TBPM DC 关联函数

> 核心问题：`02_kubo_bastin_deep_dive.md` 中的 Kubo-Bastin 公式和 `03_tbpm_dc_correlation.md` 中的
> Kubo-Greenwood/Chester-Thellung 公式都可以计算 $\sigma_{xx}$。二者等价吗？是否从同一个基本公式推导出来？
>
> **答案：是的，二者完全等价。** 它们都源自同一个基本 Kubo 公式（Kubo-Greenwood 公式，Eq.46 of Fan 2021），
> 区别仅在于对 $\delta(E-\hat{H})$ 算符的**数值表示方式不同**——一个用 Chebyshev 多项式展开（能量域 KPM），
> 一个用 Fourier 积分表示（时域 FTM）。本文给出从基本公式出发的两条完整推导路径，并证明它们的等价性。

---

## 1. 基本公式：Kubo-Greenwood 零温 DC 电导率

### 1.1 从多体 Kubo 到单粒子 Kubo-Bastin

Fan 2021 §2 给出了完整的推导链。出发点是多体 Kubo 公式（Fan 2021 Eq.27–28）：

$$\langle \hat{A} \rangle = \Omega \lim_{\tau_\varphi, \tau \to \infty} \int_0^\tau d\tau' e^{-\tau'/\tau_\varphi} \int_0^\beta d\beta' \times \text{Tr}\left[\hat{\rho}_{\text{eq}} \hat{A}(0) \hat{J}(-\tau' - i\hbar\beta') \right] \cdot \mathbf{E}_0$$

对非相互作用电子，经二次量子化处理和 Green 函数恒等式，得到 **Kubo-Bastin 公式**（Fan 2021 Eq.39）：

$$\boxed{\langle \hat{A}(\mu) \rangle = i\hbar\Omega \int dE' f(E'-\mu) \times \text{Tr}\left[\delta(E'-\hat{H})\hat{A} \frac{dG^+(E')}{dE'} (\hat{\mathbf{J}} \cdot \mathbf{E}_0) - \text{h.c.}\right]} \tag{KB}$$

取 $\hat{A} = \hat{J}_\alpha$（电流密度算符），$\hat{\mathbf{J}} = q\hat{\mathbf{V}}/\Omega$（$q=-e$），得电导率张量：

$$\sigma_{\alpha\beta}(\mu, T) = \frac{i\hbar e^2}{\Omega} \int d\varepsilon f(\varepsilon) \, \text{Tr}\left[v_\alpha \delta(\varepsilon-\hat{H}) v_\beta \frac{dG^+(\varepsilon)}{d\varepsilon} - v_\alpha \frac{dG^-(\varepsilon)}{d\varepsilon} v_\beta \delta(\varepsilon-\hat{H})\right] \tag{1}$$

这与 `02_kubo_bastin_deep_dive.md` §1.2 Eq.(1) 完全一致。

### 1.2 分部积分 → 耗散电导率

对 (1) 做分部积分，利用 $dG^\pm/d\varepsilon$ 的全微分结构，得到**耗散电导率**（Fan 2021 Eq.43）：

$$\sigma_{\alpha\beta}(\mu, T) = -\frac{\hbar e^2}{\Omega} \int dE' \left[-\frac{\partial f(E'-\mu)}{\partial E'}\right] \times \text{Tr}\left[\delta(E'-\hat{H}) v_\alpha \, \text{Im}G^+(E') \, v_\beta\right] \tag{2}$$

> **关键洞察**：$\sigma_{xx}$（纵向耗散电导）来自 Kubo-Bastin 公式的**对称部分**（$v_\alpha$ 与 $v_\beta$ 同方向）。
> Hall 电导 $\sigma_{xy}$ 来自**反对称部分**。tbplas 的 `dckb_component` 参数用于选择提取哪个部分：
> - `dckb_component=1` → 对称部分 → $\sigma_{xx}$
> - `dckb_component=2` → 反对称部分 → $\sigma_{xy}$

### 1.3 零温极限 → Kubo-Greenwood 公式

零温下 $-\partial f/\partial E' = \delta(E' - E)$，代入 (2) 并用恒等式 $\text{Im}G^+(E) = -\pi\delta(E-\hat{H})$，得：

$$\boxed{\sigma_{xx}(E) = \frac{\pi\hbar e^2}{\Omega} \, \text{Tr}\left[\delta(E-\hat{H}) \, v_x \, \delta(E-\hat{H}) \, v_x\right]} \tag{KG}$$

这就是 **Kubo-Greenwood 公式**（Fan 2021 Eq.46），是所有后续推导的**共同起点**。

> ⚠️ 注意两个 $\delta(E-\hat{H})$ 的来源不同（Fan 2021 §2.3.1 明确指出）：
> - 第一个来自 $-\partial f/\partial E'$ 的零温极限
> - 第二个来自 $\text{Im}G^+(E)$ 的恒等式
>
> 这一区别在数值实现时至关重要：两个 $\delta$ 可以用**不同的正则化方式**处理，从而衍生出两条路径。

---

## 2. 路径 A：Chebyshev 能量域 → Kubo-Bastin KPM

### 2.1 核心策略

将 Kubo-Greenwood 公式 (KG) 中的**两个** $\delta(E-\hat{H})$ 都用 Chebyshev 多项式展开（KPM）：

$$\delta(\tilde{E} - \tilde{H}) = \frac{2}{\pi\sqrt{1-\tilde{E}^2}} \sum_{n=0}^{M-1} g_n T_n(\tilde{E}) T_n(\tilde{H}) \tag{3}$$

其中 $\tilde{H}$ 为缩放到 $[-1,1]$ 的哈密顿量，$g_n$ 为 Jackson 核。

### 2.2 推导 $\Gamma_{mn} \cdot \mu_{mn}$ 结构

回到 Kubo-Bastin 公式 (1)（而非直接展开 KG），利用 Chebyshev 展开的线性性质：

1. **$\delta$ 展开**：用 (3) 展开 $\delta(\varepsilon-\hat{H})$
2. **$dG^\pm/d\varepsilon$ 展开**：用 Chebyshev 展开 Green 函数导数（详见 `02_kubo_bastin_deep_dive.md` §1.2 的完整推导）
3. **合并推迟与提前项**：利用 $\text{Tr}$ 的循环性和 $Y-Y^*$ 结构，将两项合并
4. **变量替换** $\tilde{\varepsilon} = \cos\theta$：将能量积分转为角度积分

最终得到（Fan 2021 Eq.69 在 $\eta\to 0$ 下的形式，Li 2023 Eq.69）：

$$\boxed{\sigma_{\alpha\beta}(\mu, T) = \frac{4e^2\hbar}{\pi A} \frac{4}{\Delta E^2} \int_0^\pi d\theta \; \frac{f(\cos\theta)}{\sin^3\theta} \sum_{m,n=0}^{M-1} \text{Re}\left[\Gamma_{mn}^{\alpha\beta}(\theta) \cdot \tilde{\mu}_{mn}^{\alpha\beta}\right]} \tag{4}$$

其中：
- $\tilde{\mu}_{mn} = g_m g_n \cdot \mu_{mn}$：Jackson 核加权的 Chebyshev 矩
- $\Gamma_{mn}(\theta) = \cos(m\theta)(\cos\theta - in\sin\theta)e^{in\theta} + \cos(n\theta)(\cos\theta + im\sin\theta)e^{-im\theta}$

### 2.3 提取 $\sigma_{xx}$

对于纵向电导 $\sigma_{xx}$（$\alpha=\beta=x$），取 $\Gamma_{mn}^{xx}$ 的对称部分。tbplas 中通过 `dckb_component=1` 实现。

**数值特点**：
- 双重求和 $\sum_{m,n=0}^{M-1}$：$O(M^2)$ 项
- $\|\Gamma_{mn}\| \sim O(\max(m,n))$ 线性增长
- 干净体系中 $\mu_{mn}$ 振荡不衰减 → **条件收敛**（基线偏移问题，见 `02_kubo_bastin_deep_dive.md` §7）
- 实用窗口：$M \le 2560$

---

## 3. 路径 B：Fourier 时域 → Chester-Thellung → TBPM DC 关联函数

### 3.1 核心策略

将 Kubo-Greenwood 公式 (KG) 中的**一个** $\delta(E-\hat{H})$ 替换为其 Fourier 积分表示（Fan 2021 Eq.49）：

$$\delta(E - \hat{H}) = \lim_{\tau \to \infty} \int_{-\tau}^{\tau} \frac{dt}{2\pi\hbar} \, e^{i(E-\hat{H})t/\hbar} \tag{5}$$

另一个 $\delta$ 保留，用作准本征态的投影。

### 3.2 推导 Chester-Thellung 公式

将 (5) 代入 (KG)，利用恒等式 $\partial f/\partial E = -\partial f/\partial\mu$ 和迹的线性性质，得到**Chester-Thellung 公式**（Fan 2021 Eq.51）：

$$\sigma_{xx}(\mu, T) = \lim_{\tau \to \infty} \frac{e^2}{2\Omega} \int_0^\tau dt \, \text{Tr}\left[\frac{\partial f(\hat{H}-\mu)}{\partial\mu} \{v_x(t), v_x(0)\}\right] \tag{6}$$

其中 $v_x(t) = e^{i\hat{H}t/\hbar} v_x e^{-i\hat{H}t/\hbar}$ 是 Heisenberg 绘景中的速度算符，$\{\cdot,\cdot\}$ 是反对易子。

### 3.3 零温极限 → VAC 形式

零温下 $\partial f/\partial\mu \to \delta(\hat{H}-E)$，定义速度自关联函数（VAC）：

$$C_{vv}(E, t) \equiv \frac{1}{\Omega\rho(E)} \text{Re}\left[\text{Tr}\left(\delta(E-\hat{H}) v_x(t) v_x(0)\right)\right] \tag{7}$$

其中 $\rho(E) = \frac{1}{\Omega}\text{Tr}[\delta(E-\hat{H})]$ 是态密度。电导率化为（Fan 2021 Eq.74）：

$$\boxed{\sigma_{xx}(E) = e^2 \rho(E) \int_0^\infty dt \, C_{vv}(E, t)} \tag{8}$$

### 3.4 TBPM DC 关联函数的实现

TBPM 用随机波函数 $|\psi_0\rangle$ 近似迹，构造准本征态 $|\psi(E)\rangle$：

$$|\psi(E)\rangle = \sum_{t=0}^{N_t-1} w_t^{\text{Hanning}} \left(e^{+iEt} e^{-i\hat{H}t} + e^{-iEt} e^{+i\hat{H}t}\right) |\psi_0\rangle$$

DC 关联函数定义为：

$$C_{xx}(E, t) = \frac{\langle e^{-i\hat{H}t} j_x \psi_0 | j_x \psi(E) \rangle}{|\langle \psi_0 | \psi(E) \rangle|}$$

最终 $\sigma_{xx}$ 通过 Fourier 积分得到（详见 `03_tbpm_dc_correlation.md` §2.3）：

$$\sigma_{xx}(E) = \frac{N_{\text{orb}}}{\Omega} \cdot \Delta t \cdot \text{DOS}(E) \cdot \sum_{k=0}^{N_t^{dc}-1} w_k^{\text{exp}} \cdot \text{Re}\left[e^{-iE t_k} C_{xx}(E, t_k)\right] \tag{9}$$

**数值特点**：
- 时间复杂度 $O(N_t \cdot B \cdot N_{\text{orb}})$，$B \sim 10\text{–}20$（Bessel 截断）
- 低阶 Chebyshev ≈ 10–20 阶 → 数值稳定
- 长时噪声由指数窗 $w_k^{\text{exp}} = e^{-2(k/N_t^{dc})^2}$ 抑制
- 不存在 $\Gamma\cdot\mu$ 随机游走问题（无双重组求和）

---

## 4. 等价性证明

### 4.1 共同起源

两条路径都从 **Kubo-Greenwood 公式 (KG)** 出发：

$$\sigma_{xx}(E) = \frac{\pi\hbar e^2}{\Omega} \, \text{Tr}\left[\delta(E-\hat{H}) \, v_x \, \delta(E-\hat{H}) \, v_x\right]$$

| 路径 | 对 $\delta_1$ 的处理 | 对 $\delta_2$ 的处理 | 数值域 |
|------|---------------------|---------------------|--------|
| **A: Kubo-Bastin KPM** | Chebyshev 展开 (3) | Chebyshev 展开 ($dG^+/d\varepsilon$) | 能量域 $\theta \in [0,\pi]$ |
| **B: TBPM DC 关联** | Fourier 积分 (5) | KPM/准本征态投影 | 时域 $t \in [0, T_{\max}]$ |

### 4.2 数学等价性：KPM ≡ FTM 在 $\delta(E-\hat{H})$ 的表示

两种方法的核心区别仅在于对 $\delta(E-\hat{H})$ 的数值近似方式。Fan 2021 §3.4 明确讨论了这两种方法：

**KPM（路径 A）**：
$$\delta(\tilde{E} - \tilde{H}) \approx \frac{2}{\pi\sqrt{1-\tilde{E}^2}} \sum_{m=0}^{M-1} g_m T_m(\tilde{E}) T_m(\tilde{H})$$
- 截断阶数 $M$ → 能量分辨率 $\delta E \sim \pi\Delta E / M$
- Jackson 核 $g_m$ 抑制 Gibbs 振荡

**FTM（路径 B 的基础）**：
$$\delta(E - \hat{H}) \approx \frac{\Delta\tau}{2\pi\hbar} \sum_{m=-M}^{M} w_m e^{i(E-\hat{H})m\Delta\tau/\hbar}$$
- 时间步数 $M$ → 能量分辨率 $\delta E \sim \Delta E / M$
- Hann 窗 $w_m$ 抑制 Gibbs 振荡

**在 $M \to \infty$ 极限下，两种表示都精确收敛到 $\delta(E-\hat{H})$。** 这是等价性的数学基础。

### 4.3 数值等价性：从 KG 公式的代换出发

将 KPM 展开 (3) 同时代入 KG 公式的两个 $\delta$：

$$\begin{aligned}
\sigma_{xx}^{\text{KPM}}(E) &\propto \sum_{m,n} g_m g_n T_m(\tilde{E}) T_n(\tilde{E}) \cdot \text{Tr}[T_m(\tilde{H}) v_x T_n(\tilde{H}) v_x] \\
&= \sum_{m,n} \text{Re}[\Gamma_{mn}(\theta) \cdot \tilde{\mu}_{mn}] \quad \text{(路径 A)}
\end{aligned}$$

将 Fourier 表示 (5) 代入 KG 公式的**一个** $\delta$（另一个保留为精确 $\delta$）：

$$\begin{aligned}
\sigma_{xx}^{\text{FTM}}(E) &\propto \int dt \, e^{iEt} \cdot \text{Tr}[\delta(E-\hat{H}) v_x(t) v_x(0)] \\
&= \int dt \, e^{iEt} \, C_{xx}(E,t) \quad \text{(路径 B)}
\end{aligned}$$

将路径 B 的 Fourier 积分展开为对 $t$ 的离散求和，并利用 $\delta(E-\hat{H})$ 的 KPM 展开构造准本征态，可以直接恢复路径 A 的 $\Gamma\cdot\mu$ 结构——两条路径在**有限截断下**也可以通过变换相互转化（见附录 A）。

### 4.4 物理等价性：都是耗散电导率 $\sigma_{xx}$

两条路径计算的都是**同一个物理量**——纵向耗散 DC 电导率 $\sigma_{xx}$：
- 都在零温（$T=0$）极限下定义
- 都描述电子在能量 $E$ 处的导电能力
- 都不包含 Hall 分量（$\sigma_{xy}$ 需取反对称部分）
- 都满足 Einstein 关系 $\sigma_{xx} = e^2 \rho(E) D(E)$

> ⚠️ **路径 A 在 tbplas 中的实际使用**：`02_kubo_bastin_deep_dive.md` 主要分析 $\sigma_{xy}$（Hall），
> 但 `calc_hall_cond()` 通过 `dckb_component` 参数同样可以计算 $\sigma_{xx}$。见 `solver.h` 中的
> `dckb_component` 设置。

---

## 5. 两条路径的对比总结

| 维度 | 路径 A: Kubo-Bastin KPM | 路径 B: TBPM DC 关联函数 |
|------|------------------------|--------------------------|
| **基本公式** | Kubo-Bastin → $\Gamma_{mn}\cdot\mu_{mn}$ | Chester-Thellung → VAC |
| **数值域** | 能量/角度域 $\theta \in [0,\pi]$ | 时域 $t \in [0, T_{\max}]$ |
| **核心计算** | Chebyshev 矩矩阵 $\mu_{mn}$（二重求和） | 波函数时间演化 + FFT |
| **截断参数** | $M$（Chebyshev 阶数） | $N_t$（时间步数） |
| **复杂度** | $O(M^2 \cdot N_{\text{orb}} \cdot N_\theta)$ | $O(N_t \cdot B \cdot N_{\text{orb}})$ |
| **数值稳定性** | ⚠️ $M \gtrsim 2560$ 条件收敛（$\Gamma\cdot\mu$ 随机游走） | ✅ 良好（低阶 Chebyshev $B \sim 10\text{–}20$） |
| **窗函数** | Jackson 核 $g_m$（抑制 Gibbs） | 指数窗 $e^{-2(k/N_t)^2}$（抑制长时噪声） |
| **能量分辨率** | $\delta E \sim \pi\Delta E / M$ | $\delta E \sim \Delta E / (2N_t)$ |
| **横轴** | 化学势 $\mu$ / 能量 $E$ | 电子能量 $E$ |
| **适用场景** | $\sigma_{xy}$ (Hall) QHE 平台扫描 | $\sigma_{xx}$ 导电通道能量分辨 |
| **tbplas 入口** | `calc_hall_cond(dckb_component=1)` | `calc_corr_dc_cond()` |

### 5.1 为什么 tbplas 中两条路径并存

两条路径各有优势，服务于不同的研究目标：

- **Kubo-Bastin（路径 A）**是计算 $\sigma_{xy}$（Hall 电导）的**唯一**选择——TBPM DC 关联函数不能算 $\sigma_{xy}$。$\sigma_{xy}$ 来自 Kubo-Bastin 公式的反对称部分（推迟 − 提前），涉及 $v_x$ 和 $v_y$ 的交叉关联。这是 tbplas 中 Kubo-Bastin 路径的主要价值。

- **TBPM DC 关联函数（路径 B）**是计算 $\sigma_{xx}$ 的**推荐**选择——时间复杂度 $O(N_t B N_{\text{orb}})$ 远优于 Kubo-Bastin 的 $O(M^2 N_{\text{orb}} N_\theta)$，且不存在高 $M$ 时的 $\Gamma\cdot\mu$ 随机游走问题。

- 如果只需要 $\sigma_{xx}(E)$，**没有理由使用 Kubo-Bastin 路径**（除非需要有限温度展宽，见 §6.2）。

---

## 6. 常见疑问澄清

### 6.1 "DC 关联函数不能算 $\sigma_{xx}(\mu)$？"

部分正确。TBPM DC 关联函数的输出是 $\sigma_{xx}(E)$（横轴 = 电子能量 $E$），而非 $\sigma_{xx}(\mu)$（横轴 = 化学势 $\mu$）。但 $T=0$ 时 $\mu = E$，两者等价。有限温度下可以用 Fermi-Dirac 卷积从 $\sigma_{xx}(E)$ 得到 $\sigma_{xx}(\mu, T)$：

$$\sigma_{xx}(\mu, T) = \int dE \left[-\frac{\partial f(E-\mu)}{\partial E}\right] \sigma_{xx}(E)$$

### 6.2 "Kubo-Bastin 可以算 $\sigma_{xx}$ 但文档主要讲 $\sigma_{xy}$？"

是的。`02_kubo_bastin_deep_dive.md` 的 §1.2 给出了通用公式 $\sigma_{\alpha\beta}$，$\alpha=\beta=x$ 即得 $\sigma_{xx}$。
tbplas 中设置 `dckb_component=1` 即可。但文档聚焦 $\sigma_{xy}$，因为：
1. $\sigma_{xy}$ 是 Kubo-Bastin 的**独特能力**（TBPM DC 关联函数做不到）
2. $\sigma_{xx}$ 已有更高效的 TBPM DC 关联函数路径

### 6.3 "两条路径在数值上会给出完全相同的结果吗？"

在 $M \to \infty$（路径 A）和 $N_t \to \infty$（路径 B）的极限下，是的。在有限截断下：
- 能量分辨率不同：$\delta E_{\text{KPM}} \sim \pi\Delta E/M$，$\delta E_{\text{FTM}} \sim \Delta E/(2N_t)$
- 窗函数/核函数形状不同：Jackson vs 指数窗
- 数值噪声特征不同：$\Gamma\cdot\mu$ 随机游走 vs 长时关联函数噪声

因此在有限截断下结果会有细微差异，但核心物理特征（峰位、带隙、相对幅度）应该一致。

---

## 7. 参考文献精确对照

| 公式 | Fan 2021 | 本文档 | `02_kubo_bastin` | `03_tbpm_dc` |
|------|:---:|:---:|:---:|:---:|
| 多体 Kubo | Eq.27–28 | — | — | — |
| 单粒子 Kubo-Bastin | Eq.39 | Eq.(1) | §1.2 Eq.(1) | — |
| 耗散电导率 | Eq.43 | Eq.(2) | — | — |
| 零温 Kubo-Greenwood | **Eq.46** | Eq.(KG) | — | §2.1 |
| Chester-Thellung (VAC) | Eq.51 | Eq.(6) | — | — |
| VAC 零温形式 | Eq.74 | Eq.(8) | — | — |
| MSD 形式 | Eq.75 | — | — | — |
| KPM $\delta$ 展开 | Eq.127–128 | Eq.(3) | §1.2 Eq.(2) | — |
| FTM $\delta$ 展开 | Eq.121 | Eq.(5) | — | — |
| $\Gamma_{mn}$ 公式 | — | Eq.(4) | §1.2 Eq.(7) | — |
| DC 关联函数 | — | Eq.(9) | — | §2.3 |

---

## 附录 A：从 VAC 恢复 $\Gamma\cdot\mu$ 结构（形式推导）

将 VAC 表达式 (8) 中的 $v_x(t) = e^{i\hat{H}t/\hbar} v_x e^{-i\hat{H}t/\hbar}$ 展开为 Chebyshev 多项式：

$$e^{-i\hat{H}t/\hbar} = \sum_{m=0}^\infty c_m(t) T_m(\tilde{H}), \quad c_m(t) = (2-\delta_{m0})(-i)^m J_m(\omega_0 t)$$

代入 $C_{vv}(E,t)$ 的定义 (7)：

$$\begin{aligned}
C_{vv}(E,t) &\propto \text{Re} \sum_{m,n} c_m^*(t) c_n(t) \cdot \text{Tr}[\delta(E-\hat{H}) T_m(\tilde{H}) v_x T_n(\tilde{H}) v_x] \\
&= \text{Re} \sum_{m,n} c_m^*(t) c_n(t) \cdot \mu_{mn}^{xx}(E)
\end{aligned}$$

其中 $\mu_{mn}^{xx}(E) \equiv \text{Tr}[\delta(E-\hat{H}) T_m(\tilde{H}) v_x T_n(\tilde{H}) v_x]$ 是能量分辨的 Chebyshev 矩。

再对 $t$ 积分（利用 Bessel 函数的正交关系 $\int_0^\infty dt J_m(t)J_n(t) e^{i\omega t}$），恢复 $\Gamma$ 核的结构。这证明了路径 B 可以通过 Fourier 变换转化为路径 A 的 $\Gamma\cdot\mu$ 形式——两条路径在数学上是**严格等价的**。

---

> *“It is important to point out that the two seemingly equivalent Dirac delta functions in the Kubo–Greenwood formula have different origins... Therefore, in order to use the Kubo–Greenwood formula for dissipative conductivity in numerical calculations, a regularization of one of the Dirac delta functions should be performed.”*
> — Fan et al., Physics Reports 903, 1–69 (2021), §2.3.1
>
> 正是这两个 $\delta$ 的不同正则化方式，催生了 Chebyshev KPM 和时域 FTM 两条数值路径。
> 它们从同一个公式出发，走向不同的数值实现，最终在精确极限下回归同一个物理量 $\sigma_{xx}(E)$。
