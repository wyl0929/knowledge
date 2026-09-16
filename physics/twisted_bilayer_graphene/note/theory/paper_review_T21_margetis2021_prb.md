<!--
 * @Author       : AI 精读 (理论论文五块演绎结构)
 * @Date         : 2026-08-06（粗读）→ 2026-08-20（S-REV 修正无源实验引用）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T21_margetis2021_prb.md
 * @Description  : T21: Margetis & Stauber 2021 — 手征双层体系等离激元边缘态理论（理论 — 准静电极限 + Wiener-Hopf 方法）
-->

# Paper Review: Margetis & Stauber (2021) — 手征双层体系的等离激元边缘态理论

| 字段 | 内容 |
|------|------|
| **编号** | T21 |
| **标题** | Theory of plasmonic edge states in chiral bilayer systems |
| **作者** | Dionisios Margetis, Tobias Stauber |
| **期刊** | Physical Review B 104, 115422 (2021) |
| **DOI / arXiv** | 10.1103/PhysRevB.104.115422 / arXiv:2107.05764（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 理论 — 准静电极限等离激元边缘模（积分方程 + Wiener-Hopf 方法），无实验数据 |
| **课题组** | Margetis (Univ. Maryland) / Stauber (ICMM-CSIC Madrid) |
| **PDF / SI PDF** | ✅ `reference/pdfs/Margetis和Stauber - 2021 - Theory of plasmonic edge states in chiral bilayer systems.pdf`（正文 19 页 + Appendices A–F：电场积分方程/准静电近似/Wiener-Hopf/核正则化/积分求值/手征色散微扰） |
| **精读日期** | 2026-08-06（粗读）→ 2026-08-20（S-REV）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」五块记。理论论文无黑箱、无反推、无可辨识实验。
> **共享知识引用**：通用物理（等离激元、Drude 权重、Wiener-Hopf 因子化、s-SNOM）锚点引用 `note/shared/physics/`，不复制讲义。

---

## TL;DR

**本文想解决的理论问题**：手征双层体系（TBG 或类似 moiré 范德华异质结）的**物理边缘**（与无界介质的界面）上，结构手征性（层间耦合 $\sigma_2$）如何改变**等离激元边缘模**的色散？——已知体等离激元色散在非推迟极限**不依赖**手征性，边缘模是否不同？

**主结果**：① 边缘模色散**显式依赖手征响应 $\sigma_2$**，即使非推迟极限（与体等离激元相反）——手征性把光（电偶极）与声（磁偶极）边缘模**耦合**起来 📜Q；② 顺磁区（近中性点，counterflow Drude 权重 $D_0-D_1<0$）光学边缘等离激元由**普适函数** $|\eta_{op}|=\eta_-(s)$ 描述，与单层**磁等离激元**同形——手征性等效于**有效磁场**（可高达 $\sim150$ T），且**总是使边缘模退局域**（不破互易性）📜Q；③ 手征性还打开**近无阻尼的线性色散声学边缘模** $\omega_-=v_S|q|$ 的可能（声速 $v_S$ 强依赖手征性；要求 $v_S>$ 费米速度）📜Q。

**结论/意义**：给出"手征性 → 有效磁场"这一直观对应，连接 TBG 手征等离激元与近场纳米光学（s-SNOM）探测。⚠️ **本文不研究畴壁态、也不声称拓扑保护**——研究对象是**物理边缘**的等离激元，其"局域/近无阻尼"来自手征性（有效磁场）与几何，**非**拓扑保护。全文为解析理论预言，作者用词 predict / believe / may guide。

---

## 1. 模型白箱（理想系统 + 假设清单）

### 1.1 几何与电导率张量

几何（Fig. 1）：两片半无限平板 $\Sigma_1$（$z=0$）、$\Sigma_2$（$z=d$），均占 $x>0$，共面边缘平行 $y$ 轴；浸于均匀无界介质（介电常数 $\varepsilon$、磁导率 $\mu$）📜Q。$y$ 方向平移不变，场取 $e^{iqy}$ 依赖；时间谐波 $e^{-i\omega t}$ 📜Q。

电导率张量 $\underline\sigma$（$4\times4$ 矩阵，频率依赖、各向同性、空间均匀），$2\times2$ 块：

$$
\sigma_{11}=\sigma_{22}=\begin{pmatrix}\sigma_0 & \sigma_B\\ -\sigma_B & \sigma_0\end{pmatrix},\quad
\sigma_{12}=\begin{pmatrix}\sigma_1 & \sigma_2+\sigma_B'\\ -\sigma_2-\sigma_B' & \sigma_1\end{pmatrix},\quad
\sigma_{21}=\begin{pmatrix}\sigma_1 & -\sigma_2+\sigma_B'\\ \sigma_2-\sigma_B' & \sigma_1\end{pmatrix}
$$

📜Q（Eq. 3b–3d）。$\sigma_0,\sigma_1,\sigma_2$ 空间常数，依赖掺杂/扭角/层间距 $d$/频率 $\omega$；**$\sigma_2$ 表手征性**；$\sigma_B,\sigma_B'$ 由垂直磁场引起（弱场下 $\sigma_B=-i(\omega_c/\omega)\sigma_0$、$\sigma_B'=-i(\omega_c/\omega)\sigma_1$，$\omega_c=eB/m$ 回旋频率）📜Q。

**偶极对应**（Fig. 2）：电偶极 $\mathbf p$（两片电流之和）、磁偶极 $\mathbf m=d\,\mathbf e_z\times(\mathbf j_2-\mathbf j_1)/2$（两片电流之差）：

$$
\mathbf p=-2\frac{\sigma_0+\sigma_1}{i\omega}\mathbf E-2\frac{\sigma_B+\sigma_B'}{i\omega}\mathbf e_z\times\mathbf E+d\sigma_2\mathbf B
$$

📜Q（Eq. 4a；磁偶极 Eq. 4b）。$B=0$ 且 $\sigma_2\ne0$ 即赋予手征等离激元（无需破时间反演）📜Q。

### 1.2 参数分册

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | 波数 $q$（或频率 $\omega$）、层间距 $d$、掺杂/扭角（经 Drude 权重 $D_0,D_1,D_2$）、垂直磁场 $B$（经 $\sigma_B,\sigma_B'$） |
| **导出量（由旋钮+常数算出）** | 组合电导率 $\sigma_S=\sigma_0+\sigma_1$、$\sigma_A=\sigma_0-\sigma_1$、$\sigma_{S/A}^\pm$；Drude 权重 $D_T=2(D_0+D_1)$（总）、$D_0-D_1$（counterflow）；无量纲 $s=2|\zeta|\chi^2|qd|$、$\zeta=D_2^2/(D_0^2-D_1^2)$、$\chi=D_2/D_T$；核 $K,K_\perp$ 与 Fourier 变换 |
| **模型内部量（解的性质）** | 边缘模色散 $\omega_\pm(q)$、准静电势 $\phi_\pm(x)$、截止波数 $q_*$、普适函数 $\eta_-(s)$ |
| **固定常数** | $d$、$\varepsilon,\mu$、$t_e=3$ eV、$\alpha_g\approx2.2$、$a=0.142$ nm、$\gamma=0.577215$ |
| **预言量（可检验）** | 光学边缘模蓝移、声学边缘模线性色散、有效磁场 $\sim150$ T、s-SNOM 信号 |

> 无"反推量 θ̂"层。**符号防混**：$\sigma_2$（手征电导率）≠ 层 2 的电导率；$\sigma_B,\sigma_B'$（磁场项）≠ $\sigma_0,\sigma_1$；$\omega_\pm$（光/声模频率）≠ 附录 $Q_\pm(\xi)$（Wiener-Hopf 分裂函数）；$D_0-D_1$（counterflow Drude 权重）的正负区分顺磁/抗磁。

### 1.3 显式假设清单

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **准静电（非推迟）极限**：$|q|\gg\omega/c$ | 推导 | 📜Q |
| A2 | **局域、各向同性、空间均匀、频率依赖电导率张量**（4×4） | 模型 | 📜Q |
| A3 | **长波极限 $|qd|\ll1$**（Sec. IV 近似） | 推导 | 📜Q |
| A4 | **声速 $>$ 费米速度 $v_F$**（使局域电导率在 Maxwell 方程中可用） | 模型 | 📜Q |
| A5 | **长程静电相互作用保留**（对数奇异核 $K_0$），非指数近似核 | 推导 | 📜Q |
| A6 | **两片对称**（$\sigma_{11}=\sigma_{22}$）；各向同性（非双折射） | 模型 | 📜Q（扩展留后续） |
| A7 | **$P(\xi)$ 在实轴无零点**（Wiener-Hopf 因子化合法，各向同性时绕数 $\nu=0$） | 推导 | 📜Q |

---

## 2. 推导链（顺论文演绎顺序）

### 2.0 总览

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 模型层 | Sec. II | 几何 + 电导率张量 | 标量势积分方程组（Eq. 5/7） | A1、A2、A5、A6 | 非推迟 |
| 推导层 | Sec. III | 积分方程 | 色散关系（Eq. 17a） | Wiener-Hopf（A7） | 各向同性 |
| 推导层 | Sec. IV | 色散关系 | 光/声边缘模近似色散 | A3、A4 | 长波 |

### 2.1 积分方程组（Sec. II）

- 由 2D Poisson 格林函数 $G(x,z)=\tfrac{1}{2\pi}K_0(\tilde q\sqrt{x^2+z^2})$、$\tilde q=q\,\mathrm{sg}(q)=|q|$（Eq. 2）写出静电势（Eq. 1）📜Q。表面电荷密度 $\varrho_j$、连续性方程 $-i\omega\varrho_j+\nabla_\parallel\cdot\mathbf J_j=0$、欧姆定律 $\mathbf J=\underline\sigma\,\mathbf E$（Eq. 3a）📜Q。
- 边缘条件 $\mathbf e_x\cdot\mathbf J_j(0^+)=0$（无电荷累积）→ 对 $x>0$ 的积分方程（Eq. 5）📜Q。
- **对称/反对称模** $\phi_\pm=\phi_1\pm\phi_2$、$K_\pm=K\pm K_\perp$（Eq. 8）→ 解耦积分方程（Eq. 7），**仅当 $\sigma_2\ne0$ 时两模在边界项耦合** 📜Q。$\phi_+$=对称（光）、$\phi_-$=反对称（声）对应体光/声等离激元 📜Q。

### 2.2 色散关系（Sec. III）

- 引入原型积分方程（Eq. 9）→ Fourier 变换 → $P(\xi)\hat\varphi_+(\xi)+\hat\varphi_-(\xi)=\ldots$（Eq. 10a），$P(\xi)=1+\frac{i\omega\mu\sigma}{k_0^2}\beta(\xi)^2\hat K(\xi)$、$\beta(\xi)=\sqrt{\xi^2+q^2}$（Eq. 10b）；核 $\hat K_\pm(\xi)=\frac{1}{2\beta(\xi)}(1\pm e^{-\beta(\xi)d})$ 📜Q。
- **Wiener-Hopf 因子化** $P(\xi)=e^{Q_+(\xi)}e^{Q_-(\xi)}$（Eq. 11）→ 自洽条件（Eq. 14）→ 对 $\phi_S,\phi_A$ 分别代入 → 色散关系：

$$
\big[\sigma_S^-e^{Q_S(q)}+\sigma_S^+\big]\big[\sigma_A^-e^{Q_A(q)}+\sigma_A^+\big]-\sigma_2^2\big[e^{Q_S(q)}-1\big]\big[e^{Q_A(q)}-1\big]=0
$$

📜Q（Eq. 17a），其中 $\sigma_S^\pm=\sigma_0+\sigma_1\pm i\,\mathrm{sg}(q)(\sigma_B+\sigma_B')$、$\sigma_A^\pm=\sigma_0-\sigma_1\pm i\,\mathrm{sg}(q)(\sigma_B-\sigma_B')$，$Q_m(q)=\frac{2q\,\mathrm{sg}(q)}{\pi}\int_0^\infty d\xi\frac{\ln P_m(\xi)}{\xi^2+q^2}$（Eq. 17b）📜Q。

### 2.3 光/声边缘模近似色散（Sec. IV）

- **解耦（$\sigma_2=0$）**：光学边缘等离激元 $e^{Q_S(q)}=-\sigma_S^+/\sigma_S^-$，$|qd|\ll1$ 时 $\eta_{op}=\frac{i\omega\mu(\sigma_0+\sigma_1)}{k_0^2}\tilde q$；$\sigma_B+\sigma_B'=0$ 时 $\eta_{op}=\eta_{op,0}\approx-1.217$ → $\frac{2\omega_+^2\varepsilon}{D_T|q|}=-\frac{1}{\eta_{op,0}}\approx0.822$ 📜Q（Eq. (18a) 附近）。声学边缘模 $\eta_{ac}=\frac{i\omega\mu(\sigma_0-\sigma_1)}{2k_0^2}q^2d\approx-1$ → $\omega_-^2\approx\frac{D_0-D_1}{2\varepsilon}q^2d$（$D_0-D_1<0$ 时不可观测）📜Q。
- **顺磁区（$D_0-D_1<0$）光学模**：$e^{Q_S(q)}\approx-\frac{\sqrt{\pm|D_0-D_1|D_T+2D_2^2}\mp q^2d/(2\omega^2\varepsilon)}{\sqrt{\pm|D_0-D_1|D_T-2D_2^2}\mp q^2d/(2\omega^2\varepsilon)}}$（Eq. 20 附近），归结为普适方程（Eq. 21a）：

$$
\frac{2}{\pi}\int_0^\infty d\xi\frac{\ln(|\eta_{op}|\tilde\beta(\xi)-1)}{\tilde\beta(\xi)^2}\approx\ln\frac{1-s|\eta_{op}|}{1+s|\eta_{op}|},\qquad s=s(q)=2|\zeta|\chi^2|qd|
$$

📜Q（Eq. 21a，$\tilde\beta(\xi)=\sqrt{1+\xi^2}$、$\zeta=D_2^2/(D_0^2-D_1^2)$、$\chi=D_2/D_T$）。**与单层磁等离激元同形**（$\mathrm{sg}(q)\omega_c<0$，Eq. 19）→ $|\eta_{op}|=\eta_-(s)$（Fig. 3 普适函数），$\frac{2\omega_+^2\varepsilon}{D_T|q|}=[\eta_-(2|\zeta|\chi^2|qd|)]^{-1}$（Eq. 21b）📜Q。
- **局域条件**：$0\le s(q)<s^*\approx0.525$ → $0\le|q|<|q_*|$、$|q_*|\approx0.138(|\zeta|\chi^2)^{-1}d^{-1}$、截止频率 $\omega_{+,*}=D_T|q_*|/(2\varepsilon)\sim|\chi|^{-1}$ 📜Q。$|\zeta|\chi^2$ 越小，局域 $q$ 范围越宽（Fig. 4）📜Q。
- **蓝移**：小 $s(q)\lesssim0.2$ 时 $\frac{2\omega_+^2\varepsilon}{D_T|q|}\approx|\eta_{op,0}|^{-1}(1+C_0's(q))$（Eq. 22），$C_0'=\pi\sqrt{\eta_{op,0}^2-1}/[|\eta_{op,0}|\arccos(\eta_{op,0}^{-1})]$（$D_0-D_1<0$）→ **无阻尼光学边缘模被蓝移** 📜Q。
- **声学模**：$\frac{2\omega_-^2\varepsilon}{(D_0-D_1)q^2d}\approx\frac{1-\zeta^2}{1+2\,\mathrm{sgn}(\zeta)s(q)^2}$（Eq. 23）；几何修正（Eq. 24）📜Q。顺磁区（$\zeta<0$）若 $s(q)\gg1$、$\zeta^2>1$，$\omega_-$ 变实、$\omega_-\sim|q|$ → **线性色散声学边缘模 $\omega_-=v_S|q|$**（$v_S$ 强依赖手征性）📜Q。$s(q)\gg1$、$\zeta^2\gg1$ 时 $\omega_-$ 纯虚、模不存在（近转变能 $E_{Ft}$）📜Q。

### 2.4 有效磁场对应（Sec. IV B）

- 令 TBG 的 $s=2|\zeta|\chi^2|qd|$ 等于单层的 $s=2\omega_c^2\varepsilon/(D_T|q|)$ → $\frac{\hbar\omega_c}{t_e}=s\sqrt{3\pi}\tilde D_T\alpha_g qa$，$t_e=3$ eV、$\alpha_g=\frac{e^2}{4\pi\varepsilon\hbar v_F}\approx2.2$（石墨烯精细结构常数）、$\hbar v_F=3at_e/2$、$a=0.142$ nm 📜Q。$s=s^*$、典型 $qa=0.01$、$\tilde D_T\approx0.01$ → **有效磁场 $B\approx150$ T**（与应变诱导磁场同量级）📜Q。
- 注意：此对应**不破互易性**（与真实磁场不同），手征耦合总是倾向使单层边缘模退局域 📜Q。

---

## 3. 结论清单（分层）

### 3.1 定理式主张（解析/复分析论证的产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 边缘模依赖手征性 | 非推迟极限下边缘模色散显式依赖 $\sigma_2$（体等离激元不依赖） | A1、A2 |
| 光/声模耦合机制 | $\sigma_2\ne0$ 时对称/反对称模经边界项耦合（电/磁偶极垂直、非共线） | A1、A2 |
| 色散关系 | Eq. (17a)（$\sigma_2=0$ 时解耦为单层磁等离激元型 Eq. (19)） | A7 |
| 普适函数对应 | 顺磁区光学边缘模 = 单层磁等离激元（$\mathrm{sg}(q)\omega_c<0$），$|\eta_{op}|=\eta_-(s)$ | A3 |

### 3.2 估算（经验/近似，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 非手征光边缘模常数 | $\eta_{op,0}\approx-1.217$、$\frac{2\omega_+^2\varepsilon}{D_T|q|}\approx0.822$ | A3 | 📜Q[~] |
| 局域阈值 | $s^*\approx0.525$ | A3 | 📜Q[~] |
| 截止波数 | $|q_*|\approx0.138(|\zeta|\chi^2)^{-1}d^{-1}$ | A3 | 📜Q[~] |
| 有效磁场 | $B\approx150$ T（$s=s^*$、$qa=0.01$、$\tilde D_T\approx0.01$） | 对应 | 📜Q[~] |
| 蓝移 | $2\omega_+^2\varepsilon/(D_T|q|)\approx|\eta_{op,0}|^{-1}(1+C_0's(q))$（$s\lesssim0.2$） | 微扰 | 📜Q[~] |

### 3.3 预言（可检验性 → §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 光学边缘模蓝移（手征性） | "show / demonstrated"（解析）📜Q | 中——s-SNOM 近场谱 |
| 声学边缘模线性色散 $\omega_-=v_S|q|$ | "opens up the possibility" 📜Q | 弱——需强手征 $v_S>v_F$ |
| 结果可指导近场纳米显微 | "may guide future near-field nanoscopy" 📜Q | 弱——方法论 |
| 可实验检验 | "we believe ... can possibly be tested" 📜Q | 弱 |

### 3.4 内部验证（自洽核对）

1. **奇异核↔正则化核互验**：色散关系在奇异核（附录 C）与正则化核（附录 D）下同形，正则化核 $b\to0$ 恢复奇异核结果 📜Q。
2. **零手征极限对照**：$\sigma_2=0$ 时 Eq. (17a) 约化为单层各向同性系统的边缘模色散（Eq. 19，与 refs 61/62 单层磁等离激元一致）📜Q。
3. **绕数核对**：各向同性下 Wiener-Hopf 绕数 $\nu=0$，保证因子化合法（各向异性时 $\nu$ 可非零）📜Q。

### 3.5 概念区分（分类）

| 区分 | 依据 | 结论 |
|---|---|---|
| 光（电偶极）vs 声（磁偶极）边缘模 | 对称/反对称组合 $\phi_\pm$，两片电流同相/反相 📜Q | 耦合仅由 $\sigma_2$ |
| 顺磁 vs 抗磁 | counterflow Drude 权重 $D_0-D_1\lessgtr0$（$E_F\lessgtr E_{Ft}$）📜Q | 光/声模行为不同 |
| 边缘模 vs 体模 | 体色散非推迟极限不依赖手征性，边缘模依赖 📜Q | 本文核心对照 |
| 手征边缘模 vs 拓扑保护边缘态 | 手征（结构手性 $\sigma_2$）≠ 拓扑保护（本文无拓扑论证）📜Q | 见 §6/§5.3 |

---

## 4. 假设-结论依赖图

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A2 局域电导率 | 声速 $<$ 费米速度（非局域修正重要） | 局域电导率模型失效 | 作者声明 A4 为应用前提 📜Q |
| A1 非推迟极限 | $|q|\lesssim\omega/c$（推迟区） | 手征效应消失（推迟区色散不依赖手征性） | 引言声明（引 ref 56）📜Q |
| A3 $|qd|\ll1$ | 短波 | Eq. (21b)(23) 近似失效 | Sec. IV 前提 📜Q |
| A6 各向同性 | 双折射/各向异性 | 色散关系改变（各向异性扩展另文） | 作者声明扩展留后续 📜Q |
| A7 $P(\xi)$ 无实零点 | 各向异性（绕数 $\nu\ne0$） | Wiener-Hopf 因子化需修正 | 附录 C 声明 📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- 光学边缘等离激元色散（蓝移）→ s-SNOM / 红外近场成像（石墨烯与 TBG 均可用）📜Q；
- 声学边缘模线性色散 $\omega_-=v_S|q|$ → 近场谱（强手征条件下）📜Q。

### 5.2 设计原则（手征性作"旋钮"）

手征性 $\sigma_2$（经 $\chi=D_2/D_T$）调谐边缘模色散/局域/阻尼——为等离激元器件提供额外调谐自由度 📜Q（作者 "adding a knob for tuning their dispersion by chirality"）。

### 5.3 后续文献修正（时间倒挂，💭I）

- **旧版 review/card 的框架性错误已修正**：本文**不研究畴壁上的 THS**（正文仅把"弛豫诱导畴壁作等离激元周期势""拓扑保护畴壁态手征等离激元"列为背景引文 ref 46/47，非本文对象），也**不声称拓扑保护**——边缘模"局域/近无阻尼"来自手征性（有效磁场）+ 几何。见 §6。
- 本文的"各向异性扩展"引 ref 82（另文），与 T17 的 tilt 各向异性等构成后续支线 💭I。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| **非拓扑保护** | 边缘模"局域/近无阻尼"来自手征性，**非**拓扑保护；本文无背散射免疫/拓扑论证 | 📜Q（全文无此类论证；旧版"对背散射免疫/继承拓扑保护"系无源） |
| **非畴壁态** | 研究对象是**物理边缘**（与介质的界面），非 AB/BA 畴壁态 | 📜Q（Fig. 1 几何 + 摘要 "interface"） |
| 局域电导率近似 | 需声速 $>$ 费米速度；非局域修正未处理 | 📜Q |
| 各向异性未处理 | 双折射扩展另文 | 📜Q |
| 中性点/转变能 | $D_0-D_1=0$（$E_F=E_{Ft}$）需正则化核、本文省略 | 📜Q |
| 屏蔽相互作用 | 本文主用长程对数核；屏蔽情形的定量映射（$q_*$、有效磁场）依赖细节 | 📜Q |

## 7. 与其他工作的关系（跨论文对标）

| 工作 | 关系 |
|------|------|
| Stauber 2014 (ref 39)、Stauber-Gómez-Santos 等 (refs 33,34,53) | **直接引用**——TBG 体等离激元、手征电导率张量 $\sigma_2$ 的来源 📜Q |
| Fetter 1985/1986 单层边缘磁等离激元 (refs 60–63) | 单层磁等离激元的对应参照（本文普适函数 $\eta_-(s)$ 的来源）📜Q |
| Volkov-Mikhailov 1988 (ref 66) | 单层边缘模 Wiener-Hopf 先驱 📜Q |
| Fei 2012 (ref 35)、Chen 2012 (ref 36) | s-SNOM 实验（单层石墨烯边缘模）📜Q |
| Ju 2015 / Jiang 2017 | ⚠️ **原文引用列表无此两篇**（旧版 card 误引），实际引 Sunku/Ni 2020 等 📜Q（已登记） |

> ⚠️ Phase S 外部对标（**非本文引用**，时间倒挂 💭I）见 §5.3。

## 8. 对后续研究的影响

- 建立"手征性 ↔ 有效磁场"对应，连接结构手征性与边缘磁等离激元物理 📜Q。
- 为 TBG/范德华异质结的近场纳米光学（s-SNOM）提供可测靶标 📜Q。
- 提出各向异性、非局域电导率、屏蔽相互作用的扩展方向 📜Q。

## 9. 理论模型映射（供计算对标）

| 映射 | 说明 |
|------|------|
| $\underline\sigma$（Eq. 3b–3d）→ 介电函数 | 4×4 电导率张量是 TBPM/Kubo 介电函数计算的可对标对象 📜Q |
| 色散关系 Eq. (17a) → 数值求根 | 光/声边缘模色散可数值解 📜Q |
| $\eta_-(s)$ → 普适函数 | 供 s-SNOM 色散提取对标 📜Q |
| 有效磁场 $\frac{\hbar\omega_c}{t_e}=s\sqrt{3\pi}\tilde D_T\alpha_g qa$ | 供"手征性→磁场"定量换算 📜Q |

---

## Phase S 目的接口（引用式）

- **Q1（edge state 如何表征）**：本文给出**等离激元**（集体激发）边缘态的表征靶标——边缘模色散（光学蓝移、声学线性 $\omega_-=v_S|q|$）→ s-SNOM 近场谱；**非**单粒子拓扑边缘态 📜Q。
- **Q2（理论如何解释）**：手征电导率 $\sigma_2$ 在非推迟极限耦合光/声边缘模、改色散，等效于有效磁场（$\sim150$ T）——**非拓扑保护**解释 📜Q。
- **Q3（理论↔实验对应）**：$\omega_\pm(q)$ ↔ s-SNOM/红外近场成像；$\chi=D_2/D_T$ ↔ 手征性（扭角/掺杂）；$B\approx150$ T ↔ 有效磁场标度 📜Q。

> **增量价值**：与 T05/T09/T12/T15/T18（单粒子拓扑/散射网络）**不同层**——本文是**集体激发（等离激元）**的边缘态理论；比前者多 = 光/声边缘等离激元色散 + 手征性→有效磁场对应；少 = 无任何单粒子拓扑/畴壁论证（非同类对象）。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` + `-raw` 提取到 `/tmp/T21.txt`，逐项 grep 核对：**全部数字命中原文**——

| 数字 | grep 命中位置 | 结论 |
|------|--------------|------|
| $\theta_m\approx1.08°$ | 引言 | ✓ 📜Q |
| $\eta_{op,0}\approx-1.217$、$\frac{2\omega_+^2\varepsilon}{D_T|q|}\approx0.822$ | Sec. IV A | ✓ |
| $s^*\approx0.525$ | Fig. 3 / Sec. IV B | ✓ |
| $|q_*|\approx0.138(|\zeta|\chi^2)^{-1}d^{-1}$ | Sec. IV B | ✓ |
| $B\approx150$ T | Sec. IV B | ✓ |
| $t_e=3$ eV、$\alpha_g\approx2.2$、$a=0.142$ nm、$\hbar v_F=3at_e/2$ | Sec. IV B | ✓ |
| $qa=0.01$、$\tilde D_T\approx0.01$ | Sec. IV B | ✓ |
| $\gamma=0.577215$（Euler 常数） | 附录 E | ✓ |
| $\sigma_{11}=\sigma_{22}=[\ldots]$、$\sigma_{12}/\sigma_{21}$（Eq. 3b–3d） | Sec. II | ✓ |
| 色散关系 Eq. (17a) 结构 | Sec. III B | ✓ |
| $\omega_-^2\approx\frac{D_0-D_1}{2\varepsilon}q^2d$、$\frac{2\omega_-^2\varepsilon}{(D_0-D_1)q^2d}\approx\frac{1-\zeta^2}{1+2\,\mathrm{sgn}(\zeta)s(q)^2}$（Eq. 23） | Sec. IV | ✓ |

⚠️ 修正/降级：① 旧版"畴壁上的等离激元边缘态 + THS 继承拓扑保护"**框架性错误**——本文对象是**物理边缘**的等离激元（非畴壁 THS），"局域/近无阻尼"来自手征性（有效磁场）**非拓扑保护**，已全面改写；② 旧版"用 RPA 介电函数 + 流体力学方法"无源——实际是**Wiener-Hopf 方法 + 4×4 电导率张量**，已改；③ 旧版"色散 $\omega\propto\sqrt q$"仅部分正确——光边缘模 $\omega_+\propto\sqrt{|q|}$ 之外，**关键新结果是声学边缘模线性 $\omega_-=v_S|q|$**，已补；④ 已确认"Ju 2015/Jiang 2017 不在引用列表"（旧 card 误引，本文无此表述，仅登记）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（粗读版） |
| 2026-08-20 | **S-REV 修正**："为 Ju 2015 和 Jiang 2017 的等离激元实验提供理论框架"确认不存于本 review（原文引用列表无 Ju 2015/Jiang 2017，实际引 Sunku/Ni 2020 等）。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧版归档 `archive/paper_review_T21_margetis2021_prb.backup_20260908.md`。补：4×4 电导率张量显式式、参数分册、7 条假设清单、推导链（Sec. II→IV）、结论分层、假设-结论依赖图、反向核对 pass。 |
| 2026-09-08 | **框架性修正 + 降级/删除**：① "畴壁 THS + 拓扑保护" → "物理边缘等离激元 + 手征性（非拓扑）"（旧版框架错误）；② "RPA 介电函数 + 流体力学" → "Wiener-Hopf + 电导率张量"（无源方法描述）；③ 补声学线性色散 $\omega_-=v_S|q|$（旧版漏掉的关键新结果）；④ 删除"对背散射免疫"（无源）。 |
