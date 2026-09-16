<!--
 * @Author       : AI 推导 + 整理 (T0 Snyman 2007 / T01 Martin 2008 / T06 Zhang 2013 / T05 San-Jose 2013 → 我们 DW/cont.py)
 * @Date         : 2026-09-09（初建）→ 2026-09-09（重构为 EFW→LSW→阈值判据→代码 四段式）
 * @Description  : [PHY-2BAND] Bernal 双层 two-component(two-band) 约化 → EFW(质量 kink) → LSW(μ 序参量) → TPH 阈值判据 Eq.(1) → cont.py 实现核对
-->

# [PHY-2BAND] 双层畴壁：EFW → LSW 推广 → U 阈值判据 Eq.(1) → cont.py 实现

> **用途**：一条推导链串起四件事——① Martin 2008 的 EFW 原始模型（质量 kink + 零模衰减）；② Zhang 2013 把模型推广到 LSW（引入堆叠序参量 $\mu$）；③ San-Jose 2013 用它做 TPH 出现的层间势 $U$ 阈值判据 Eq.(1)；④ 我们 `~/project/DW/src/cont.py` 对该模型的 FDM 实现及其问题。
>
> **符号统一**（跨论文对照表，以 SWMcC 标准符号为基准）：
>
> | 物理量（标准符号·标准值） | Martin 2008 | Snyman 2007 | Zhang 2013 | San-Jose 2013 | cont.py |
> |---|---|---|---|---|---|
> | 层内耦合 $\gamma_0$（~3 eV） | （不用，改用 $c$） | $t_\parallel\approx3$ eV | （用 $v$） | （用 $v_F$） | `G0`=2.7 eV |
> | 层间耦合 $\gamma_1$（~0.4 eV） | $t_\perp$（**无数值**） | $t_\perp\approx0.4$ eV | $\gamma_1$（归一化 $\gamma=\gamma_1/\hbar v$） | $\gamma_\perp\approx0.33$ eV | `G1`=0.48 eV |
> | 费米速度 $v_F$（~$10^6$ m/s） | $c$ | $v\approx10^6$ m/s | $v$ | $v_F$ | `vF`=$\hbar v_F$=$\tfrac32$`G0`·`a0`≈0.575 eV·nm |
> | 晶格常数 $a_0$（2.46 Å） | $a$（动量以 $1/a$） | — | — | $a_0$=2.46 Å | `a`=0.246 nm |
> | C-C 键长 $a_{CC}$（1.42 Å） | — | $d\approx1.4$ Å | — | — | `a0`=0.142 nm |
> | 层间偏压（物理 eV） | $V$ | — | $V$（归一化 $\Delta=V/2\hbar v$） | $U$ | `V` |
> | 堆叠序参量 $\mu$ | （无，固定 AB） | — | $\mu$（$+1$=AB,$-1$=BA,$0$=AA） | $\mu$ | `mu` |
> | 层间耦合长度 $l_\perp$（~1.5 nm） | — | $\hbar v/t_\perp\approx11d$ | — | $\hbar v_F/\gamma_\perp\approx7.3a_0$ | 同左 |
>
> **两个关键关系**：
> - **三组别名（同一物理量）**：$c=v_F$、$t_\perp=\gamma_1=\gamma_\perp$、$a=a_0$。Martin 用 $c$（非 $v_F$）、$t_\perp$ 全文无数值；$a$ 是**晶格常数**（2.46 Å）。
> - **$\gamma_0$（层内耦合）Martin/San-Jose 均不显式用**，只通过 $v_F$ 隐式进入：$v_F=\frac{\sqrt3}{2}\frac{\gamma_0a_0}{\hbar}=\frac{3}{2}\frac{\gamma_0a_{CC}}{\hbar}$。
>
> **命名坑**（"$a$/$a_0$"在文献里两种互斥用法，代参前必须按数值区分）：
> - Martin 的 $a$ = San-Jose 的 $a_0$ = cont.py 的 `a` = **晶格常数 2.46 Å**；
> - Snyman 的 $d$ = cont.py 的 `a0` = **C-C 键长 1.42 Å**（⚠️ 名字带 0 却**不是** San-Jose 的 $a_0$）。

---

## 1. Martin 2008：EFW 的原始模型（质量 kink）

> 这一节是整条链的**地基**：Bernal 双层 4×4 哈密顿量 → 2-band 约化 → 反号偏压（EFW）的质量 kink → 零模衰减率的精确解。后续 Zhang（§2）和 San-Jose（§3）都建立在它之上。

### 1.1 4×4 哈密顿量与 2-band 约化（Schrieffer-Wolff）

Martin 2008（T01 Eq.1）的 4×4 哈密顿量（基 $(A_1,B_1,A_2,B_2)$，加层间偏压 $V(x)$，上层 $+V/2$、下层 $-V/2$）：

$$H=\begin{pmatrix} -V/2 & v_F\pi^\dagger & 0 & 0\\ v_F\pi & -V/2 & \gamma_\perp & 0\\ 0 & \gamma_\perp & V/2 & v_F\pi^\dagger\\ 0 & 0 & v_F\pi & V/2 \end{pmatrix},\qquad \pi=p_x+ip_y,\ \pi^\dagger=p_x-ip_y$$

**泡利形式**（$\sigma$=子格 A/B、$\tau$=层，$\tau_z=+1$ 顶层；基 $(A_1,B_1,A_2,B_2)$＝(底,顶)）：

$$H=\frac{V}{2}\tau_z+v_F(\sigma_x p_x+\sigma_y p_y)+\frac{\gamma_\perp}{2}(\sigma_x\tau_x-\sigma_y\tau_y)\qquad(\text{Martin 泡利形式})$$

层间耦合 $\gamma_\perp$ 只连二聚对（此处 $B_1\leftrightarrow A_2$，即 $(\gamma_\perp/2)(\sigma_x\tau_x-\sigma_y\tau_y)$ 只留 $A_{\rm top}\leftrightarrow B_{\rm bottom}$）。$|\varepsilon|,|V|\ll\gamma_\perp$ 时用 **Schrieffer-Wolff** 把二聚（高能）子空间积分掉，保留非二聚子空间 $(A_1,B_2)$。分块 $(A_1,B_2\,|\,B_1,A_2)$：

$$H_{LL}=\begin{pmatrix}-V/2 & 0\\ 0 & V/2\end{pmatrix},\quad H_{HH}=\begin{pmatrix}-V/2 & \gamma_\perp\\ \gamma_\perp & V/2\end{pmatrix},\quad T=\begin{pmatrix}v_F\pi^\dagger & 0\\ 0 & v_F\pi\end{pmatrix}$$

$$H_{\rm eff}=H_{LL}-T\,(H_{HH}-\varepsilon)^{-1}T^\dagger\;\xrightarrow{\ \varepsilon\approx0\ }\;H_{LL}-T\,H_{HH}^{-1}T^\dagger$$

代入 $H_{HH}^{-1}\approx\frac{1}{\gamma_\perp^2}\begin{pmatrix}-V/2 & \gamma_\perp\\ \gamma_\perp & V/2\end{pmatrix}$（到 $O(1/\gamma_\perp^2)$），用 $\pi\pi^\dagger=\pi^\dagger\pi=p^2$，得 Martin Eq.2：

$$H_{\rm eff}=\begin{pmatrix}-\frac{V}{2}\big(1-\frac{v_F^2p^2}{\gamma_\perp^2}\big) & -\frac{v_F^2}{\gamma_\perp}\pi^{\dagger2}\\[3pt]-\frac{v_F^2}{\gamma_\perp}\pi^2 & \frac{V}{2}\big(1-\frac{v_F^2p^2}{\gamma_\perp^2}\big)\end{pmatrix}\qquad(\text{T01 Eq.2})$$

首项近似（丢对角 $O(p^2/\gamma_\perp^2)$ 小修正）：

$$H_2=-\frac{v_F^2}{\gamma_\perp}\begin{pmatrix}0 & \pi^{\dagger2}\\ \pi^2 & 0\end{pmatrix}-\frac{V(x)}{2}\begin{pmatrix}1&0\\0&-1\end{pmatrix}\qquad(2)$$

（对角 $(1,1)=-V/2$（层1 $A_1$）、$(2,2)=+V/2$（层2 $B_2$）；符号约定不影响衰减长度，只依赖 $|V|$。）

**泡利形式**（$g\cdot\sigma$，$\sigma$ 作用在 2 分量子空间 $(A_1,B_2)$；由 $\pi^{\dagger2}=(p_x^2-p_y^2)-2ip_xp_y$、$\pi^2=(p_x^2-p_y^2)+2ip_xp_y$ 展开，用分解 $\begin{pmatrix}0&a\\b&0\end{pmatrix}=\tfrac{a+b}{2}\sigma_x+\tfrac{b-a}{2i}\sigma_y$）：

$$H_2=-\frac{V(x)}{2}\sigma_z-\frac{v_F^2}{\gamma_\perp}(p_x^2-p_y^2)\sigma_x-\frac{2v_F^2}{\gamma_\perp}p_xp_y\,\sigma_y\qquad(2')$$

即 $g=(-(v_F^2/\gamma_\perp)(p_x^2-p_y^2),\ -2(v_F^2/\gamma_\perp)p_xp_y,\ -V/2)$，**$g_z=-V/2$ 即质量（幅度 $V/2$）**。这正是 Martin 2008 准经典 $H_{\rm qc}=-\varphi\sigma_z-(p_x^2-p_y^2)\sigma_x-2p_xp_y\sigma_y$ 的物理对应（**$\sigma_y$ 项为负号**，与 Eq.(2) 非对角 $-\pi^{\dagger2},-\pi^2$ 一致）。

> **无偏压极限 = Snyman 2007 Eq.B1**（T0）：对角为常数 $U$、无隙、保留同一二次手征项 $-(v_F^2/\gamma_\perp)\pi^{\dagger2}$。这是 T0 与 T01 的实质连接点 📜Q。

### 1.2 能谱与"质量" $m=V/2$

均匀 $V$ 下，$H_2$ 本征值（用 $\pi^2\pi^{\dagger2}=p^4$）：

$$E^2=\frac{V^2}{4}+\frac{v_F^4 p^4}{\gamma_\perp^2}\qquad(\text{T01 Eq.3 的 }V<t_\perp\text{ 简化式})$$

$p=0$ 处能隙 $=|V|$，即"质量" $m=V/2$（$\sigma_z$ 项系数）。**二次色散 + 偏压开隙 = BLG 手征准粒子（非 Dirac 费米子）** 📜Q。

### 1.3 Martin Eq.4 的数值解推导（u/v、step kink、α/β）

Martin 2008 的准经典哈密顿量（Eq.4，$\sigma_y$ 项为**负号**）：

$$H_{qc}=-\varphi(x)\sigma_z-(p_x^2-p_y^2)\sigma_x-2p_xp_y\,\sigma_y\equiv\mathbf g(\mathbf p,x)\cdot\boldsymbol\sigma,\qquad \varphi(x)=\frac{V(x)t_\perp a^2}{2c^2}$$

（动量以 $1/a$ 为单位，自然单位 $\hbar=1$。）

**u、v 是什么**：$H_{qc}$ 作用在约化后的 2 分量子空间 $(A_1,B_2)$ 上（原文 "The remaining components ... have predominantly **A1 and B2** character" 📜Q）。$u=\psi_{A_1}$、$v=\psi_{B_2}$ 是非二聚子格的振幅；完整 4 分量 $\Psi\approx(u,\ \cdot,\ \cdot,\ v)$，二聚子格 $B_1,A_2$ 已被 Schrieffer-Wolff 积分掉（幅度 $O(vp/t_\perp)$ 小）。概率密度 $|\Psi|^2=u^2+v^2$（Martin Fig.2 caption）📜Q。

**Eq.5/6 的由来**：把 $H_{qc}$ 写成 2×2 显式矩阵（非对角 $-\pi^{\dagger2},-\pi^2$，$\pi=p_x+ip_y$），作用在 $(u,v)^T$ 上，$p_x\to-i\partial_x$：

$$H_{qc}=\begin{pmatrix}-\varphi & -\pi^{\dagger2}\\ -\pi^2 & +\varphi\end{pmatrix}\;\Rightarrow\;
\begin{cases}
-\varphi u+(\partial_x+p_y)^2 v=\varepsilon u & (\text{Martin Eq.5})\\
+\varphi v+(\partial_x-p_y)^2 u=\varepsilon v & (\text{Martin Eq.6})
\end{cases}$$

（用了 $-\pi^{\dagger2}=-[(p_x-ip_y)^2]$ 且 $p_x=-i\partial_x$：$-\pi^{\dagger2}\to+(\partial_x+p_y)^2$，$-\pi^2\to+(\partial_x-p_y)^2$。）

**Step kink + α/β**：取阶跃 kink $\varphi(x)=\varphi_0\,\mathrm{sgn}\,x$，$\varphi_0$ = 无量纲 kink 幅度（= 无量纲能隙）。两侧 $\varphi$ 常数，解 $\psi\propto e^{-\lambda x}$，隙内态（$|\varepsilon|<\varphi_0$）：

$$\lambda=\alpha\pm i\beta\qquad(\text{Martin Eq.7})$$

由体能谱 $\varepsilon^2=\varphi_0^2+p^4$（$p^2=p_x^2+p_y^2$）代入 $p_x^2=-\lambda^2$：

$$\varepsilon^2=\varphi_0^2+(p_y^2-\lambda^2)^2\ \Rightarrow\ \lambda^2=p_y^2\pm i\sqrt{\varphi_0^2-\varepsilon^2}$$

令 $\lambda=\alpha+i\beta$：$\mathrm{Re}\,\lambda^2=\alpha^2-\beta^2=p_y^2$、$|\lambda^2|=\alpha^2+\beta^2=\sqrt{p_y^4+\varphi_0^2-\varepsilon^2}$，相加/相减：

$$\alpha(\beta)=2^{-1/2}\Big[\sqrt{p_y^4+\varphi_0^2-\varepsilon^2}\ \pm\ p_y^2\Big]^{1/2}\qquad(\text{Martin Eq.7 显式})$$

$\alpha$ = 横向衰减率（$e^{-\alpha x}$）、$\beta$ = 沿法向的轻微振荡（对应 Fig.2 "slightly oscillatory and decaying" 📜Q）。

**色散与零能解**：$x=0$ 匹配（波函数及一阶导连续，二阶/三阶导由 Eq.5 跳跃，Martin Eqs.9–12）→ 4×4 行列式方程（Eq.13）→ 零能附近色散（Eqs.14/15），零能解在

$$p_0=-\frac{\sqrt{\varphi_0}}{2^{3/4}}\qquad(\varphi_0>0)$$

即每谷每自旋 2 条零模（两支反向、两谷反向）。

### 1.4 Martin 的衰减长度讨论（$\xi\sim a/\sqrt{\varphi_0}$）

Martin 原文（Eq.15 之后的散文，非编号公式）明确给出衰减长度量级：

> "the decay length of the wave function of the topologically confined states **is of the order of $a/\sqrt{\varphi_0}$** at low energies. ... For kinks wider than $a/\sqrt{\varphi_0}$ one expects quantitative deviations..." 📜Q

代入 $\varphi_0=V_0t_\perp a^2/(2c^2)$（恢复 $\hbar$：$\varphi_0=V_0\gamma_\perp a_0^2/(2\hbar^2v_F^2)$）：

$$\xi\sim\frac{a_0}{\sqrt{\varphi_0}}=\frac{a_0}{\sqrt{V_0\gamma_\perp a_0^2/(2\hbar^2v_F^2)}}=\frac{\sqrt2\,\hbar v_F}{\sqrt{V_0\gamma_\perp}}$$

**精确版**（§1.3 的 $p_y=0,\ \varepsilon=0$ 特例，即 San-Jose 引用的形式）：零模衰减率

$$\lambda=\frac{\sqrt{V_0\gamma_\perp}}{2\hbar v_F},\qquad\text{衰减长度}\ \frac1\lambda=\frac{2\hbar v_F}{\sqrt{V_0\gamma_\perp}}$$

与 $\xi\sim a_0/\sqrt{\varphi_0}$ 差 **$\sqrt2$ 因子**——属 Martin "of the order of" 的范畴 📜Q[推导]。San-Jose 2013 取精确首项 $\lambda=\sqrt{U\gamma_\perp}/(2\hbar v_F)$（引 Martin 为 ref 12，§3 用）。

**一致性论证**（Martin 原意）：$V<t_\perp$ 时 $\xi\sim a/\sqrt{\varphi_0}\gtrsim a$，零模空间展宽 ≳ 晶格常数 → 长波展开 Eq.(4) 自洽；"kinks wider than $a/\sqrt{\varphi_0}$ → quantitative deviations" 只改色散细节、不改零模数目（拓扑）📜Q。

> **$\hbar$ 说明**：Martin 用自然单位 $\hbar=1$（故 $\varphi=Vt_\perp a^2/(2c^2)$ 无量纲）；本笔记恢复 $\hbar$（$\varphi_0=V_0\gamma_\perp a_0^2/(2\hbar^2v_F^2)$）以便与 San-Jose 的 $\lambda$ 对接。San-Jose 正文 OCR 丢 $\hbar$（写成 $\sqrt{U\gamma_\perp}/2v_F$），自洽形式必须含 $\hbar$ 📜Q[推导]。

---

## 2. Zhang 2013：对 LSW 的推广（μ 序参量）

> 这一节回答"EFW 模型能否直接用于 mTBG 的 LSW"。结论：**4 带哈密顿量层面能直接沿用（拓扑等价），但 Martin 的 2 带约化不能原样搬过去**——因为 EFW 变号的是"质量"、LSW 变号的是"手征性/动能项"。

### 2.1 问题的提出

Martin 2008 的墙是 **EFW**（电场畴壁，$V(x)$ 反号）；mTBG 里的墙是 **LSW**（层堆叠畴壁，AB↔BA）。二者物理起源不同，能否用同一模型？Zhang 2013 给出了系统回答。

### 2.2 μ 序参量与推广 4-band $H_{LSW}$

Zhang 2013 引入**堆叠序参量 $\mu$**（registry 指标），把 AB/BA 统一进一个 4 带哈密顿量（Zhang Eq.[3]）：

$$H_{LSW}=\Delta\tau_z+\nu q_x\sigma_x+q_y\sigma_y+\frac{\gamma}{2}(\sigma_x\tau_x-\mu\,\sigma_y\tau_y)\qquad(\text{Zhang Eq.[3]})$$

**显式 4×4 矩阵**（基 $(A_T,B_T,A_B,B_B)$；逐项代入 $\tau_z=\mathrm{diag}(1,1,-1,-1)$、$\sigma_x,\sigma_y$ 层内、$\sigma_x\tau_x,\sigma_y\tau_y$ 层间）：

$$H_{LSW}=\begin{pmatrix}
\Delta & \nu q_x-iq_y & 0 & \frac{\gamma}{2}(1+\mu)\\[3pt]
\nu q_x+iq_y & \Delta & \frac{\gamma}{2}(1-\mu) & 0\\[3pt]
0 & \frac{\gamma}{2}(1-\mu) & -\Delta & \nu q_x-iq_y\\[3pt]
\frac{\gamma}{2}(1+\mu) & 0 & \nu q_x+iq_y & -\Delta
\end{pmatrix}\qquad(\text{Zhang Eq.[3] 显式})$$

（验算：$\mu=+1$ → 只留 $(1,4),(4,1)=\gamma$ 即 $A_T\leftrightarrow B_B$；$\mu=-1$ → 只留 $(2,3),(3,2)=\gamma$ 即 $B_T\leftrightarrow A_B$；$\mu=0$ → 两对子格等强度 $\gamma/2$。）

层间耦合项 $\frac{\gamma}{2}(\sigma_x\tau_x-\mu\sigma_y\tau_y)$ 中，$\mu$ 编码"哪对子格被连接"：

- $\mu=+1$（AB）：只留 $A_T\leftrightarrow B_B$ 二聚（"top A hybridizes bottom B" 📜Q）；
- $\mu=-1$（BA）：只留 $B_T\leftrightarrow A_B$ 二聚；
- $\mu=0$（AA）：两对子格等强度耦合。

（Zhang 的 $\Delta=V/2\hbar v$、$\gamma=\gamma_1/\hbar v$ 是归一化量；物理对应 $V$、$\gamma_\perp$。）

### 2.3 2-band 约化里的 μ：进动能项，不进质量项（关键）

把 $H_{LSW}$ 再约化到 2 带（$\gamma\gg\Delta$），Zhang 明确写出广义 $g_\nu(q)$（Zhang Eq.[1] 推广）：

$$g_\nu(q)=\left(-\frac{q_x^2-q_y^2}{\gamma},\ \frac{2\mu\nu\,q_xq_y}{\gamma},\ \Delta\right)$$

**显式 2×2 矩阵**（$\tilde H_\nu=g_\nu(q)\cdot\tilde\sigma$，$\tilde\sigma$ 作用在 2 分量子空间；用 $g_x\mp ig_y=-\dfrac{(q_x\pm i\mu\nu q_y)^2}{\gamma}$）：

$$\tilde H_\nu=\begin{pmatrix}
\Delta & -\dfrac{(q_x+i\mu\nu q_y)^2}{\gamma}\\[4pt]
-\dfrac{(q_x-i\mu\nu q_y)^2}{\gamma} & -\Delta
\end{pmatrix}\qquad(\text{Zhang 2 带显式})$$

三个分量：$g_x=-(q_x^2-q_y^2)/\gamma$（无 $\mu$）、$g_y=2\mu\nu q_xq_y/\gamma$（**$\mu$ 在此**）、$g_z=\Delta$（**质量 = 纯偏压，无 $\mu$**）。

**结论**：在 2 带模型里，$\mu$ 进的是**动能项 $g_y$**（$\sigma_y$ 分量，即二次手征项），**不是质量项 $g_z=\Delta$**。所以 LSW 在 2 带模型里**不是质量 kink**，而是 $g_y$ 随 $\mu$ 反号的"手征性 kink"。这是 Martin 的 2 带模型不能原样搬去 LSW 的根本原因 📜Q。

### 2.4 三个关键差异（EFW vs LSW）

| 差异 | EFW（Martin） | LSW（mTBG） | Zhang 依据 |
|---|---|---|---|
| ① 变号的量 | 质量 $\Delta\sigma_z$（偏压 $V$） | 手征性 $g_y\propto\mu$（堆叠） | §2.3，Zhang Eq.[1] 推广 |
| ② 低能子空间 | 固定 $(B_1,A_2)$ | 跨墙**切换** $(B_T,A_B)\leftrightarrow(A_T,B_B)$ | "switches the orbitals that span its low-energy subspace" 📜Q |
| ③ μ 过 0 | （无 AA） | 必经 $\mu=0$（AA），有限动量能隙闭合 $q_x=\pm\sqrt{\Delta^2+\gamma^2/4}$ | Zhang Fig.1 相图 📜Q |

② 的后果：Zhang 明言 "**In the LSW case, unlike the EFW case, analyzing the continuity of wave functions across the interface requires consideration of all four bands**" 📜Q——2 带模型两侧基不同，必须退回 4 带（或显式跟踪基旋转）。③ 的后果：mTBG 的 AB→BA 墙**不是 gapped–gapped 突变界面**，而是穿过金属性 AA（$\mu=0$）点的光滑过渡（San-Jose 同说 "an AA bilayer is a good metal for any reasonable interlayer bias" 📜Q）。

### 2.5 拓扑等价 Eq.[9] 与结论

尽管有上述差异，Zhang 2013 证明两者**拓扑等价**（Zhang Eq.[9]）：

$$H_{LSW}(-\Delta,\mu)=\tau_x\,H_{LSW}(\Delta,-\mu)\,\tau_x$$

即 **$\Delta$ 反号 ⟺ $\mu$ 反号 + 基变换 $\tau_x$**。因此 EFW 与 LSW 的谷 Chern 数变化相同 $\Delta N_\nu=2\nu$，都束缚每谷一对同向传播手征模（Zhang Fig.3 上排两条谱重合）📜Q。

**结论**：
1. **4 带层面**：模型直接沿用，序参量从 $\Delta$ 换成 $\mu$（或两者组合）。
2. **2 带层面**：不能直接沿用，需三处修改——质量项 $\Delta$ 保持均匀、$\mu$ 进动能项、2×2 基跨墙旋转（即用 4 带匹配）。
3. 附加：LSW 晶格计算每谷 **3 条**（非 2 条）无隙模（第三条来自断裂层悬键，连续模型漏掉）；谷间散射可使模数 0–4 浮动 📜Q。

---

## 3. San-Jose 2013：用该模型做 U 阈值判断（Eq.(1)）

> San-Jose 2013 把 §1 的 EFW 质量-kink 衰减率 $\lambda$ **套到 LSW 上**，用几何 + 95% 判据组装成 TPH 网络出现的层间势阈值 Eq.(1)。本节给出完整代数（= 原文一句 "One can approximately quantify this condition" 的展开）。

### 3.1 关键近似：把 EFW 衰减率 λ 套到 LSW

San-Jose 原文："Using the two-component approximation (valid for $U<\gamma_\perp$), an interface mode decays like $\sim e^{-\lambda|x|}$ with $\lambda=\sqrt{U\gamma_\perp}/2\hbar v_F$"（引 Martin 2008 为 ref 12）📜Q。即直接沿用 §1.4 的精确版 $\lambda=\sqrt{U\gamma_\perp}/(2\hbar v_F)$（= §1.3 α/β 的 $p_y=0,\varepsilon=0$ 特例）。

> **越界使用的性质**（联系 §2）：严格说这是把"质量 kink 衰减率"偷换成"手征性 kink 衰减率"。其物理合法性来自一个事实——**AB/BA 区各自的能隙由同一偏压 $U$ 打开、幅度 $|U|$ 相同**，所以界面模衰减尺度只由 $|U|$ 和 $\gamma_\perp$ 决定，与"反号的是 $\Delta$ 还是 $\mu$"无关。故 Eq.(1) 是可靠的经验判据（San-Jose 自标 "approximately quantify"），非严格推导。

### 3.2 几何 + 95% 判据

要求界面模在 Moiré BA 畴半径 $R=L_M/(2\sqrt3)$ 内振幅衰减 $\ge95\%$（"half the distance between the AB and BA region centers" 📜Q）：

$$e^{-\lambda R}\le0.05\ \Leftrightarrow\ \lambda R\ge-\ln0.05$$

$$\lambda R=\frac{\sqrt{U\gamma_\perp}}{2\hbar v_F}\cdot\frac{L_M}{2\sqrt3}=\frac{\sqrt{U\gamma_\perp}\,L_M}{4\sqrt3\,\hbar v_F}\ge-\ln0.05$$

### 3.3 用 $l_\perp$ 消去 $\hbar v_F$ → Eq.(1)

层间耦合长度（Snyman Eq.1 / San-Jose）：$l_\perp=\hbar v_F/\gamma_\perp\approx7.3\,a_0$。代入 $\hbar v_F=l_\perp\gamma_\perp$：

$$\frac{\sqrt{U\gamma_\perp}\,L_M}{4\sqrt3\,l_\perp\gamma_\perp}\ge-\ln0.05\ \Rightarrow\ \frac{\sqrt{U/\gamma_\perp}\,L_M}{4\sqrt3\,l_\perp}\ge-\ln0.05$$

$$\sqrt{\frac{U}{\gamma_\perp}}\ge\underbrace{-4\sqrt3\ln0.05}_{=z=20.76}\cdot\frac{l_\perp}{L_M}\ \Rightarrow\ z^2\left(\frac{l_\perp}{L_M}\right)^2<\frac{U}{\gamma_\perp}$$

加上界 $U/\gamma_\perp<1$（two-component 合法域）+ 能窗 $|\varepsilon|<|U|/2$（AB/BA 区能隙 $|U|$），得 **Eq.(1)**：

$$z^2\left(\frac{l_\perp}{L_M(\theta)}\right)^2<\frac{U}{\gamma_\perp}<1,\qquad |\varepsilon|<\frac{|U|}{2}\qquad(1)$$

### 3.4 数值核对

下界反解 $L_M>z\,l_\perp\sqrt{\gamma_\perp/U}=20.76\times7.3a_0\times\sqrt{\gamma_\perp/U}$。取 $\gamma_\perp=0.33$ eV、$U=90$ meV：$\sqrt{\gamma_\perp/U}=1.91$，得

$$L_M>290\,a_0\ \Rightarrow\ \theta<0.20^\circ$$

**完全复现** San-Jose 的 "$U\sim90$ meV → $L_M\gtrsim290a_0$ ($\theta<0.2^\circ$)" 📜Q[~]。（sympy 验算 $z=20.755$、$L_M=290.1a_0$、$\theta=0.197^\circ$。）

> **物理读法**：TPH 网络需要"大偏压 + 小角度"——大 $U$ 抬 $\lambda$（衰减快）、小 $\theta$ 抬 $L_M$（畴区 $R$ 大），二者都让 $\lambda R\gg1$，畴壁模被充分局域、不渗入体区，网络才 "fully develop"（San-Jose 引言 "requires large bias and small angles" 📜Q）。

---

## 4. 我们的 cont.py：代码实现及存在的问题

> 核对对象：`~/project/DW/src/cont.py`（`build_4band_H`）与 `configs/cont_4band.yaml`。结论：4-band 是 Zhang Eq.[3] 的 FDM 实现，EFW/LSW/comp 三剖面正确；但有一个 ν 符号约定问题值得留意。

### 4.1 定位

`build_4band_H`（基 $(A_b,B_b,A_t,B_t)$，底在前）实现了 Zhang Eq.[3] 的四项：

$$H=\underbrace{\nu q_x\sigma_x+q_y\sigma_y}_{\text{层内 Dirac}}+\underbrace{\frac{\gamma_1}{2}(\sigma_x\tau_x-\mu\sigma_y\tau_y)}_{\text{层间耦合}}+\underbrace{\Delta\sigma_0\tau_z}_{\text{偏压}}$$

代码用 `G0,G1` 为层内/层间跃迁，`pi_x ∝ νσ_x`（x 差分）、`pi_y = σ_y`（y）、`M_const + μ·M_mu`（层间）、`M_V = (1/2)diag(-1,-1,+1,+1)`（偏压）。

### 4.2 逐项核对

| 项 | Zhang Eq.[3] | cont.py | 判定 |
|---|---|---|---|
| 基 | $(A_T,B_T,A_B,B_B)$ | $(A_b,B_b,A_t,B_t)$（底前，置换） | ✅ 等价 |
| 偏压 | $\Delta\sigma_0\tau_z$（顶 $+V/2$、底 $-V/2$） | `M_V=(1/2)diag(-1,-1,+1,+1)` | ✅ 一致 |
| 层间耦合 | $(\gamma/2)(\sigma_x\tau_x-\mu\sigma_y\tau_y)$ | `M_const + μ·M_mu` | ✅ 一致（μ 约定见下） |
| 层内 Dirac | $\nu q_x\sigma_x+q_y\sigma_y$ | `pi_x∝νσ_x`、`pi_y∝σ_y` | ⚠️ 结构对、ν 符号反（问题①） |

**μ 约定逐项验算**：代码 $H_{int}=(G1/2)[(1-\mu)(A_b\!\leftrightarrow\!B_t)+(1+\mu)(B_b\!\leftrightarrow\!A_t)]$，故 $\mu=+1$ → 只留 $B_b\leftrightarrow A_t$（底 B–顶 A 二聚）＝ Zhang 的 AB；$\mu=-1$ → 只留 $A_b\leftrightarrow B_t$＝ BA；$\mu=0$ → 两对子格等耦合＝ AA 线。**与 Zhang 一致** ✅。配置 `mu0: 1` + LSW 剖面 `mu = -mu0·tanh(x/dL)` 正是 AB→BA 光滑过渡。

### 4.3 剖面函数（`_dw_profile`）——三种墙正确

| `dw_type` | $V(x)$ | $\mu(x)$ | 对应 |
|---|---|---|---|
| `EFW` | $V\tanh(x/dL)$ | $\mu=\text{const}$ | **Martin 2008**（偏压反号 kink，§1） |
| `LSW` | $V=\text{const}$ | $-\mu_0\tanh(x/dL)$ | **Zhang 2013**（堆叠反号，§2） |
| `comp` | $V\tanh$ | $-\mu_0\tanh$ | Zhang 2013 补偿墙（$\Delta N_\nu=0$） |

### 4.4 计算流程与方法（不是 KPM）

`main()` → `build_4band_H`（或 6band）→ `calc_diag`。五步：

1. **FDM 离散**：k·p 哈密顿量在 $x$ 方向有限差分，$x$ 取 $N_x$ 格点（`Nx=101`），得 $(N_{\rm int}\times4)^2$ 稀疏矩阵；并分解 $H(k_y)=H_0+k_y H_{ky}$（$k_y$ 只线性进入一次）。
2. **逐 $k_y$ 对角化**：`eigsh(H, k=Nb, sigma=1e-8, which='LM')` —— scipy **shift-invert Lanczos/Arnoldi**，取最靠近 $E\approx0$ 的 `Nb=100` 个本征值 + 本征矢（**低能窗口**，带隙/边界态都在 $E=0$ 附近）。
3. **DOS**：对每个本征值 $E_0$ 叠加洛伦兹 $\frac1\pi\frac{\eta}{(E-E_0)^2+\eta^2}$（$\eta=0.001$ eV）。
4. **LDOS**：本征矢平方（空间概率）$\times$ 洛伦兹权重累加。
5. **$k_y$ 积分**：`dky/2π` 归一化；`ProcessPoolExecutor` 多进程并行，子进程从磁盘 `.npz` 加载共享 $H_0/H_{ky}$。

| | cont.py（实际） | KPM |
|---|---|---|
| 求谱方式 | 直接对角化 `eigsh` | 切比雪夫展开，**不对角化** |
| DOS 构造 | 本征值 + 洛伦兹展宽 | Chebyshev 矩 + Jackson 核 |
| 需要本征矢 | 需要（算 LDOS 用 $\|\psi\|^2$） | 不需要（随机向量 trace） |
| 瓶颈 | 每个 $k_y$ 一次 eigsh | 矩阵-向量乘迭代 |

> **不是 KPM**：KPM 的核心是"Chebyshev 展开谱函数、不做对角化"；cont.py 恰好相反——每个 $k_y$ 显式对角化再洛伦兹展宽。KPM 类方法在项目的 **TBPM 入口**（`main.py`+`model.py`+`calc.py`，`tbplas` 紧束缚传播 / Haydock 递归），不在 cont.py。

### 4.5 输出结果与现状

`main()` 末尾保存三样（`io_vis.py` 定义格式，输出到 `runs/{MMDD}/`）：

| 输出 | 文件 | 内容 |
|---|---|---|
| 能带色散 | `band_{dw_type}.txt` | 第 1 列 $k_y$ + 后续列各能带（`Nb=100` 条） |
| 态密度 | `dos_{dw_type}.txt` | 第 1 列 $E$ + DOS |
| 局域态密度 | `ldos_{dw_type}.npz` | $x$ 格点、$E$、LDOS 二维矩阵 |

按 `dw_type`（EFW / LSW / comp / DW / 均匀 AB）各存一套。**物理现状**（WRAPUP ⑤⑦）：
- ✅ 4band：层间偏压 $V$ 打开能隙、$x=0$ 处可见**畴壁边界态色散**（subgap 态）；
- ⚠️ 4band LDOS 在 $E=0$ 处集中于畴壁区但空间分布较均匀（非强局域边缘态）；`Nx=101` 精度不足（未达生产级 ≥1001）；
- 🔴 6band：ABA/ABC DW 畴壁态不明显、与实验不符 → 项目整体 **BLOCKED**（重启条件：用 TBPM 交叉验证连续模型）。

### 4.6 发现的问题（按重要性排序）

| # | 级别 | 问题 | 说明/影响 |
|---|---|---|---|
| ① | 🟡 | **ν 符号约定翻转** | 代码 `pi_x = -1j·ν·vF/(2h)·σ_x` 离散化后 $H_x=+i\nu v_F\sigma_x\partial_x$，而标准/Zhang 的 $\nu q_x\sigma_x$（$q_x=-i\partial_x$）是 $-i\nu v_F\sigma_x\partial_x$。差一个负号 ⟺ **代码 `nu=+1` 实为标准 K′ 谷**。谱/能隙/模数/DOS 不受影响（对 ν 对称）；但边界手征模**传播方向**（$E(k_y)$ 斜率符号）会与 Zhang Fig.2/3 的 K 谷相反。config 注释 `nu: 1 # (K=1, K'=-1)` 目前**误导**。 |
| ② | 🟢 | `G1=0.48` eV | 参数选择。Snyman/Martin 用 $t_\perp=0.4$ eV、Zhang 数值例 $\gamma_1=0.3$；0.48 是石墨常用值，跨文献对标时注意。 |
| ③ | 🟢 | 重复 print | `build_4band_H`/`build_6band_H` 连续两行 `print(f"G0: {G0}")`（155–156、232–233），第二行应为 `G1`。纯 cosmetic。 |
| ④ | 🟢 | `build_2band_H` 死代码 | 2-band 阶段遗留（即 §1 的 Martin 2-band），`main()` 只调 4/6-band，不被调用。 |
| ⑤ | 🟢 | `dw_type=='DW'` 含义不清 | `mu = mu0·0.5`（μ=0.5 均匀中间堆叠），非畴壁亦非标准堆叠，疑似测试占位。 |
| ⑥ | 🔵 | 6band 层间耦合不对称 | `M_const` 底层–中层带 $1/2$、中层–顶层带 $1$，对 ABA/ABC 可疑；但三层超出本锚点范围（WRAPUP 已标 BLOCKED），暂不动。 |

> **一个值得点出的确认**：代码是 **4-band**（非 Martin 的 2-band 约化），故算 EFW 时不受 $V\ll\gamma_\perp$ 限制，且正确回避了 §2.4 的"LSW 需 4 带匹配"问题——把 EFW（质量 kink）与 LSW（手征性 kink）统一在同一个 $H_{LSW}(\mu)$ 框架里（Zhang Eq.[3]/[9] 的拓扑等价）。

---

## 附：与相邻锚点的关系

- `[PHY-BERRY]`（`04_berry_vs_ab_phase.md`）：谷 Chern 数反号给 TPH 模"存在性"（拓扑），本文 Eq.(1) 给其"充分局域/耗尽"的**能量-几何判据**——两者互补（一个答"为什么有"，一个答"何时 fully develop"）。
- `[PHY-LB]`（`10_landauer_buttiker.md`）：TPH 网络一旦形成，其电导/透射用 Landauer-Büttiker 计通道——本文不涉及通道计数。

*创建: 2026-09-09 | 重构: 2026-09-09（EFW→LSW→阈值判据→代码 四段式）| 推导核对: λ 根式、z=20.76、L_M≈290a₀/θ≈0.2° 均 sympy 验算；cont.py 的 μ 约定逐项手算*
