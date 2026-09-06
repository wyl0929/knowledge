<!--
@Author       : Yulong Wang（自推导，AI 转写为 markdown）
@Date         : 2026-09-02
@Description  : [PHY-VC] 谷陈数推导链：两带 Berry 曲率 → 有效哈密顿量 → 单层/AB/ABC/ABA 谷陈数
@Source       : reference/note.tex §1 "Berry curvature & Berry phase in graphene" + §5 "Effective Hamiltonian"
@Note         : 本文是**用户自推导**（非"复现于 ≥2 篇文献"的通用讲义）；源文件保留为 note.tex
-->

# [PHY-VC] 谷陈数推导链（自推导）

Last updated: 2026-09-02

> 本文转写自 `reference/note.tex`（标题 "Note of edge state in tMBG"）中与谷电子学直接相关的 §1（Berry 曲率在石墨烯中的计算）与 §5（有效哈密顿量）。结论是 **chirally-stacked N 层石墨烯的单谷谷陈数 $C_v=N/2$、每谷边界模数 $=N$**，是本 field 谷陈数约定（`11_term_disambiguation.md` §2.2/§7.1）的推导基础。

## 1. 两带模型 Berry 曲率的通用公式

两带模型 $H(\mathbf k)=\mathbf d(\mathbf k)\cdot\boldsymbol\sigma + \Delta(\mathbf k)I$，参数化 $\hat{\mathbf d}=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)$。低能带 Berry 联络 $A_\phi=\tfrac12(1-\cos\theta)$，Berry 曲率：

$$
\Omega(\mathbf k)=\frac{1}{2}\hat{\mathbf d}\cdot\left(\partial_{k_x}\hat{\mathbf d}\times\partial_{k_y}\hat{\mathbf d}\right)
=\frac{1}{2}\frac{\mathbf d\cdot\left(\partial_{k_x}\mathbf d\times\partial_{k_y}\mathbf d\right)}{|\mathbf d|^3}
$$

谷陈数 = 单谷区域 $\Omega$ 的积分（除以 $2\pi$）。下面把所有体系都塞进这个公式。

## 2. 前置：有效哈密顿量（Löwdin 降维，§5）

高低能子空间分块 $H=\begin{pmatrix}H_{ll}&H_{lh}\\H_{hl}&H_{hh}\end{pmatrix}$，在 $E\ll H_{hh}$ 下消除高能子空间：

$$
H_{\mathrm{eff}} = H_{ll} - H_{lh}H_{hh}^{-1}H_{hl}
$$

- **AB 双层**：dimer 位（$\gamma_1$）构成 $H_{hh}$，忽略 $\gamma_3,\gamma_4$ 后得两带有效模型 $H=\begin{pmatrix}\Delta & -\beta(\pi^\dagger)^2\\ -\beta\pi^2 & -\Delta\end{pmatrix}$，$\beta=v_0^2/\gamma_1$。
- **ABC 三层**：只留最近邻 hopping，$H_{\mathrm{eff}}=\begin{pmatrix}\Delta & \frac{v_0^3}{\gamma_1^2}(\pi^\dagger)^3\\ \frac{v_0^3}{\gamma_1^2}\pi^3 & -\Delta\end{pmatrix}$。
- **ABA 三层**：通过基变换 $U$ 把 $6\times6$ 哈密顿量解耦为"单层样"$H_{MLG}$ + "双层样"$H_{BLG}$ 两个块。

## 3. 各体系的谷陈数

| 体系 | $\mathbf d(\mathbf k)$（两带） | Berry 曲率 $\Omega_\xi$ | 单谷谷陈数 $C_v$ |
|---|---|---|---|
| 单层（有质量 Dirac） | $(v_0\xi k_x,\ v_0 k_y,\ m)$ | $\frac12\frac{\xi m v_0^2}{(v_0^2k^2+m^2)^{3/2}}$ | $\frac{\xi}{2}\mathrm{sgn}(m)=\pm\frac12$ |
| AB 双层 | $(-\beta(k_x^2-k_y^2),\ 2\xi\beta k_x k_y,\ \Delta)$ | $-\xi\frac{2\Delta\beta^2 k^2}{(\beta^2k^4+\Delta^2)^{3/2}}$ | $\xi\mu\,\mathrm{sgn}(\Delta)=\pm1$ |
| ABC 三层 | $(A k^3\cos3\theta,\ A k^3\sin3\theta,\ \Delta)$，$A=\frac{v_0^3}{\gamma_1^2}$ | $-\xi\frac{9}{2}\frac{A^2\Delta k^4}{(A^2k^6+\Delta^2)^{3/2}}$ | $\frac32\xi\mu\,\mathrm{sgn}(\Delta)=\pm\frac32$ |
| ABA 三层 | 单层块 + 双层块 | 两块叠加 | 单层 $\frac12\xi\,\mathrm{sgn}(\Delta_2)$ + 双层 $\xi\,\mathrm{sgn}(\Delta_e)$ |

其中 $\xi=\pm1$ 是谷指标（K/K′），$\mu=\pm1$ 是导带/价带指标；$\Delta$ 是层间势差开出的能隙；$v_0=\frac{\sqrt3}{2}\frac{a\gamma_0}{\hbar}$。

## 4. 伪自旋 $J$ 与 Berry 相位

一般 chirally-stacked 体系的有效哈密顿量为 $H_{\mathrm{eff}}=\alpha k^J[\cos(J\theta_k)\sigma_x+\sin(J\theta_k)\sigma_y]$（$J$ 为伪自旋）：

| 体系 | $J$ | Berry 相位 | 单谷谷陈数 $C_v=J/2$ |
|---|---|---|---|
| 单层 | 1 | $\pi$ | $1/2$ |
| AB 双层 | 2 | $2\pi$ | $1$ |
| ABA 三层 | 1 & 2 | $\pi$ & $2\pi$ | $1/2+1$ |
| ABC 三层 | 3 | $3\pi$ | $3/2$ |

## 5. 关键结论（本 field 谷陈数约定的推导基础）

1. **单谷谷陈数 $C_v = J/2 = N/2$**（chirally-stacked N 层），**每谷边界模数 $= N = 2C_v$**。二者差因子 2，正是 `11_term_disambiguation.md` §2.2 定稿里"每谷 ±1 vs 每谷 2 模"关系的推广。
2. **半整数不是严格 Chern 数**：单层 $C_v=1/2$、ABC 三层 $C_v=3/2$ 都是半整数——这就是 ZMM 2013 说"谷陈数在 ABA 三层上无法定义"的原因（严格整数 Chern 数只对偶数层成立）。
3. **双层 $C_v=\pm1$（unit magnitude）**：与 Huang 2018 "quantized at unit magnitude"、ZMM 2013 "$N_\nu=\pm1$"、Verbakel 2021 "$C_v=\pm1$" 三方一致 → 坐实 §2.2 定稿。
4. **`[PHY-BERRY]` 的 "tMBG $C_v=\pm3$" 是每谷边界模数（N=3），不是谷陈数（±3/2）**——需回写 TBG field。

## 6. 与 MVP 的关系

本文的谷陈数公式（单层 ±1/2、AB ±1、ABC ±3/2）是 `23_mvp_experiment_plan.md` 里"单谷谷陈数数值读出"的**解析基线**：数值侧在均匀 gapped 双层上算出的单谷谷陈数应对标 $\pm1$，符号随 $\Delta$ 反号；若扩展到三层，则对标 $\pm3/2$。
