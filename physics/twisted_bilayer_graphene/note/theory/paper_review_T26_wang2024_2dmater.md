<!--
 * @Author       : AI 精读 (paper-reading skill)
 * @Date         : 2026-08-11（初读）→ 2026-08-20（S-REV 机制重写）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T26_wang2024_2dmater.md
 * @Description  : T26: Wang & Hsu 2024 — TBG 中电控关联畴壁网络（连续模型→屏蔽相互作用→玻色化→相图；2026-09-08 按 5 块演绎结构重写）
-->

# Paper Review: Wang & Hsu (2024) — 电控关联畴壁网络

| 字段 | 内容 |
|------|------|
| **编号** | T26 |
| **标题** | Electrically tunable correlated domain wall network in twisted bilayer graphene |
| **作者** | Hao-Chien Wang, Chen-Hsuan Hsu |
| **期刊** | 2D Materials 11, 035007 (2024)（Open Access） |
| **DOI / arXiv** | 10.1088/2053-1583/ad3b11 / 2311.14384（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 理论 — 电控关联畴壁网络（连续模型 + 屏蔽相互作用 + 玻色化/TLL，无实验数据） |
| **课题组** | Wang & Hsu (Institute of Physics, Academia Sinica) |
| **PDF / SI** | ✅ `reference/pdfs/Wang和Hsu - 2024 - Electrically tunable correlated domain wall network in twisted bilayer graphene.pdf`（正文 20 页 + Appendix A–C） |
| **精读日期** | 2026-08-11（初读）→ 2026-08-20（机制修正）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」五块记。本文是**多体白箱**——研究对象是从连续模型 → 解析电荷密度 → 屏蔽库仑相互作用 → 玻色化（TLL）的关联网络模型；结论是"相互作用强度可电调、相图 DW/SC 竞争"这类预言，受连续模型、平均场、TLL 假设限定。

---

## TL;DR

**本文想解决的理论问题**：TBG 畴壁网络在层间偏压 + 层结构屏蔽效应下，电子-电子相互作用强度如何被**定量确定**（而非 ad hoc 假设），以及这些相互作用能否被**电学调控**以在密度波态与超导之间切换？

**主结果**：① 从连续模型（Eq. 1）算出低能畴壁模的**解析电荷密度分布**（Eq. 4，全局拟合），进而算出畴壁内/畴壁间的**屏蔽库仑相互作用强度** $U_{ee,n}$（Eq. 6）——不预设相互作用形式 📜Q；② 相互作用强度可由**层间偏压 $V_d$、屏蔽长度 $d$（金属栅距离）、介电材料 $\epsilon_r$** 调控，考察范围内增强**超七倍** 📜Q；③ 建立含两分支的玻色化关联网络模型（Eq. 7–12），算局域 DOS（幂律标度）、Anderson 局域化、以及 CDW/SDW/SSC/TSC 关联函数 → **相图显示密度波态与超导间的电学可调性**，强电声耦合出现 Wentzel-Bardeen（WB）奇异性使网络失稳 📜Q。

**结论/意义**：把畴壁网络建立为"**电可调的低维强关联平台**"——关联可在**远离魔角**的小转角（$\theta=0.5°$）出现 📜Q。⚠️ 全文是理论推导/数值估算（"we demonstrate / we establish / our findings suggest"），非实验证实。

---

## 1. 模型白箱（连续模型 + 玻色化网络）

### 1.1 哈密顿量/作用量

**单粒子连续模型**（Eq. 1）：$H_{sp}=H_0+H_{hyb}$，在 $(c_{1A\gamma\sigma},c_{1B\gamma\sigma},c_{2A\gamma\sigma},c_{2B\gamma\sigma})^\intercal$ 基下：

$$H_{sp}=\begin{pmatrix}h_D^{\gamma}(\tfrac\theta2)+V_d & T^\gamma_{hyb}\\[2pt] (T^\gamma_{hyb})^\dagger & h_D^{\gamma}(-\tfrac\theta2)-V_d\end{pmatrix}$$

对角块含层间偏压 $2V_d$ 与 Dirac 锥 $h_D^\gamma(\theta)=v_F(p-\hbar K_\gamma)\cdot e^{i\gamma\theta\tau_z/2}\tau^\gamma e^{-i\gamma\theta\tau_z/2}$（Eq. 2）；非对角块为周期 moiré 势（层间杂化）$T^\gamma_{hyb}=\sum_{j=0}^2 e^{i\gamma q_j\cdot r}T^\gamma_j$，$T^\gamma_j=w_{AA}\tau^0+w_{AB}[\tau^x\cos(2j\pi/3)+\gamma\tau^y\sin(2j\pi/3)]$（Eq. 3）📜Q。无量纲参数 $\alpha_{AA}=w_{AA}/(\hbar v_F k_\theta)$、$\alpha_{AB}=w_{AB}/(\hbar v_F k_\theta)$（后者称"有效杂化参数"）📜Q。

**解析电荷密度拟合**（Eq. 4）：$\rho_{2D}(r)=C_0\sum_{j=0}^2\sum_m\sum_\delta R_{2j\pi/3}\rho_{dw}^{\delta,m}(r)$，$\rho_{dw}^{\delta,m}=\rho_\perp^{\delta,m}(x)\rho_\parallel^{\delta,m}(y)\rho_z(z)$，横向/纵向用 Jackiw-Rebbi 型 + 经验正弦函数（参数 $\kappa_\perp,\kappa_\parallel,c_0^\parallel$）📜Q。

**屏蔽库仑**（Eq. 5–6）：三层结构（TBG + 厚度 $d$ 的介电层 + 金属背栅），镜像电荷：介电层 $a_{scn}=(\epsilon_r-1)/(\epsilon_r+1)$ 倍、金属层 $-(1-a_{scn})$ 倍；相互作用 $U_{ee,n}=\tfrac{e^2L_\parallel}{4\pi\epsilon_0}\sum_M\int dr dr' \rho^{\delta,m}(r)\rho^{\delta,m+n}(r')/|r-r'|$（Eq. 6，$M\in\{dw,diel,met\}$）📜Q。

**玻色化网络**（Eq. 7–12）：费米场 $\psi_{\sigma,m}^{(j)}=\sum_{\ell\delta}\psi_{\ell\delta\sigma,m}^{(j)}$ 玻色化（Eq. 7，含 Klein 因子 $U_{\ell\delta\sigma,m}^{(j)}$、截断 $a=\hbar v_{dw}/\Delta_a$、电荷/自旋 $\nu\in\{c,s\}$、对称/反对称分支 $P\in\{s,a\}$）📜Q；对易（Eq. 8）。关联网络 $H_{ee}=\sum_j\sum_{P\in\{s,a\}}(H_{cP}^{(j)}+H_{sP}^{(j)})$（Eq. 9），电荷扇区 $H_{cP}^{(j)}=\sum_m\int\frac{dx}{2\pi}[U_{\phi cP,n}^{(j)}(\partial_x\phi_{cP,m})^2+U_{\theta cP,n}^{(j)}(\partial_x\theta_{cP,m})^2]$（Eq. 9b，$n$ 近邻耦合）、$U_{\phi cs,n}^{(j)}=\hbar v_{dw}\delta_{n0}+\tfrac2\pi(U_{ee,n}^{(j)}+V_{ee,n}^{(j)})$ 等（Eq. 10）📜Q。

### 1.2 参数分册

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $V_d$（层间偏压）、$d$（屏蔽长度 = 介电层厚度）、$\epsilon_r$（介电常数，材料）、$\alpha_{AB}$（有效杂化，由 $w_{AB}$/压力 与 $\lambda_M$/转角 调）、电声耦合 $v_{ep}$（自由参数，未指定值） |
| **导出量** | $\lambda_M=a_0/(2\sin(\theta/2))$、$q_M=\sqrt3 k_\theta$、$k_\theta=4\pi/(3\lambda_M)$、拟合参数 $\kappa_\perp,\kappa_\parallel,c_0^\parallel$、$U_{ee,n}$、$\Delta_a$（带宽）、$v_{dw}$（畴壁模速度）、局域化长度 $\xi_{loc,m}$ 与温度 $T_{loc,m}$ |
| **模型内部量（解的性质）** | 局域 DOS 指数 $\beta_m$、$\Delta_{\phi cP,m},\Delta_{\theta cP,m}$、关联函数指数、相图（DW/SC/金属/失稳） |
| **固定常数** | $a_0$（晶格常数）、$v_F$、$L_\parallel=0.5\,\mu\text{m}$、$L_z=6.68$ Å、$\epsilon_r=6.93$（hBN）、$w_{AA}/w_{AB}\in[0.2,0.5]$ |
| **预言量（可检验）** | 局域 DOS 幂律（Eq. 14）、Anderson 局域化长度/温度、DW↔SC 电学可调相图、WB 失稳 |

> 无"反推量"层。**符号防混**：$V_d$（偏压）≠ $v_{dw}$（畴壁模速度）≠ $v_{ep}$（电声耦合速度）；$\nu$ 在此处为电荷/自旋扇区指标，**非**填充因子；$\alpha_{AB}$（有效杂化）≠ T22 的应变参数。

### 1.3 显式假设清单

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **连续模型**（BM，平面波基 + 动量截断） | 模型 | 📜Q |
| A2 | **中等弛豫**：$w_{AA}/w_{AB}\in[0.2,0.5]$ | 模型 | 📜Q |
| A3 | **远离魔角小转角** $\theta=0.5°$（$\alpha_{AB}=1.4$，$V_d/\hbar v_F k_\theta=1.5$，参数区 $V_d/\hbar v_F k_\theta\gtrsim\alpha_{AB}>1$） | 模型 | 📜Q |
| A4 | **平均场库仑**（占据数涨落小）；谷间库仑只改 $U$ 可忽略 | 推导 | 📜Q |
| A5 | **镜像电荷近似**（$L_z\ll d$；介电层 $a_{scn}$ 倍 + 金属层 $-(1-a_{scn})$ 倍） | 推导（Eq. 5） | 📜Q |
| A6 | **TLL（玻色化）** | 模型 | 📜Q |
| A7 | **自旋扇区非相互作用**（$K_{ss}=K_{sa}=1$）→ 相图不区分单重态/三重态 | 推导 | 📜Q |
| A8 | **不假设横向平移不变**（有限 $N_\perp=18$ 线） | 模型 | 📜Q |
| A9 | **电声耦合强度为自由参数**（未指定值） | 推导（相图） | 📜Q |

> 判别性扫轴：$V_d$（$1.2\text{–}2\,\hbar v_F k_\theta$ 量级）、$d$（$5,20,60$ nm）、$\epsilon_r$（三种介电材料）、$v_{ep}$（电声耦合）、$\alpha_{AB}\in[1,2]$（$\theta$：$0.35°\lesssim\theta\lesssim0.7°$）📜Q。

---

## 2. 推导链（顺论文顺序）

### 2.0 总览

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 模型层 | Continuum model (Sec. 2) | $H_{sp}$（Eq. 1） | 能带 + 电荷密度 | A1–A3 | 小角度 |
| 推导层 | Charge density (Sec. 3) | 对角化波函数 | 解析 $\rho_{2D}$（Eq. 4）+ $\kappa$ 拟合 | 全局拟合 | $V_d\gtrsim1.2$ |
| 推导层 | Interaction strength (Sec. 4) | $\rho_{2D}$ + 镜像电荷 | $U_{ee,n}$（Eq. 6） | A5 | $L_z\ll d$ |
| 推导层 | Correlated network (Sec. 5) | $U_{ee,n}$ | 玻色化 $H_{ee}$（Eq. 9–12）+ 局域 DOS/局域化（Eq. 13–28） | A6–A8 | TLL |
| 推导层 | Correlation functions & phase diagrams (Sec. 6) | 关联算符 | DW/SC 指数 + 相图（Fig. 14） | A7、A9 | — |

### 2.1 模型层：连续模型 + 偏压

- **输入**：$H_{sp}=H_0+H_{hyb}$（Eq. 1），层间偏压 $2V_d$、Dirac 锥（Eq. 2）、层间杂化 $T^\gamma_{hyb}$（Eq. 3）📜Q。
- **输出**：数值对角化得能带与波函数 → 空间电荷密度（Fig. 2，密度集中在畴壁、AA 区更高）📜Q。
- **关键提取**：从畴壁模色散提取带宽 $\Delta_a$ 与速度 $v_{dw}$（Fig. 4）；$V_d$ 增大 → 带变平、$\Delta_a$ 与 $v_{dw}$ 减小（电可调性）📜Q。

### 2.2 推导层：解析电荷密度（全局拟合）

- **输入**：对角化波函数。
- **输出**：拟合函数 $\rho_{2D}$（Eq. 4），横向 $\rho_\perp^{\delta,m}(x)=e^{-8\kappa_\perp\sin^2(\sqrt3 k_\theta x/4-\sqrt3 m\lambda_M/2)}\Theta(\dots)\Theta(\dots)$、纵向 $\rho_\parallel^{\delta,m}(y)=e^{-8\kappa_\parallel\sin^2[\sqrt3 k_\theta(y-\tfrac m2\lambda_M)/4]}+c_0^\parallel$ 📜Q。$\kappa_\perp,\kappa_\parallel$ 随 $V_d$ **近似线性增大**（更强约束）📜Q。TLL 描述需 $\rho_{2D}(r_{AB})/\rho_{2D}(r_{dw})\ll1$ 即 $e^{-2\kappa_\perp}\ll1$，由 ref 30 简化式得转角 $O(1°)$ 或更小 📜Q。

### 2.3 推导层：屏蔽相互作用强度

- **输入**：$\rho_{2D}$ + 三层结构镜像电荷（Eq. 5：介电层 $-a_{scn}\rho(z\to-z)$、金属层 $-(1-a_{scn})\rho(-z-2d)$，$a_{scn}=(\epsilon_r-1)/(\epsilon_r+1)$）。
- **输出**：$U_{ee,n}$（Eq. 6），intrawire（$n=0$）与 interwire（$n\ne0$，算到第 9 近邻）📜Q。
- **结果**：$U_{ee,0}$ 随 $V_d$ 增大（更强约束）、随 $\epsilon_r$ 增大/距离 $d$ 减小而减小（更强屏蔽）；考察参数区**增强超七倍** 📜Q。interwire 相互作用随线间距指数衰减；$d\sim\sqrt3 n\lambda_M/2$ 时第 $n$ 近邻被严重屏蔽 📜Q。

### 2.4 推导层：玻色化关联网络 + 局域 DOS + Anderson 局域化

- **玻色化**（Eq. 7）→ $H_{ee}$（Eq. 9–12）；每畴壁类比碳纳米管（两 Dirac 锥 → 两分支 $\delta=1,2$），网络 = 耦合纳米管 TLL 介观网络 📜Q。电荷反对称扇区 $U_{ee,n}^{(j)}\approx V_{ee,n}^{(j)}$（数值）→ 近似非相互作用 📜Q。
- **局域 DOS**：$\rho_{dos,m}^{(j)}(E,T)\propto T^{\beta_m^{(j)}}\cosh(E/2k_BT)\,|\Gamma((1+\beta_m^{(j)})/2+iE/2\pi k_BT)|^2$（Eq. 14），$\beta_m^{(j)}=\tfrac18(\Delta_{\phi cs,m}+\Delta_{\theta cs,m}+\Delta_{\phi ca,m}+\Delta_{\theta ca,m}+K_{ss}+K_{sa}+1/K_{ss}+1/K_{sa}-1)$（Eq. 15a）📜Q；低 $T$ 幂律 $\propto|E|^{\beta_m^{(j)}}$ 📜Q。$\Delta$ 偏离 1 越大 → 关联越强（STS 可测）📜Q。
- **Anderson 局域化**：无序关联（Eq. 24，$D_{b,m}^{(j)}=\hbar^2v_F^2/(2\pi\lambda_{mfp})$）→ RG 流（Eq. 27），隙化相条件 $\Delta_{\phi cs,m}+\Delta_{\phi ca,m}<6-K_{ss}-K_{sa}=4$（弱吸引也可局域化）📜Q；局域化长度 $\xi_{loc,m}^{(j)}=a[\pi\hbar^2v_{dw}^2/(2D_{b,m}^{(j)}a)]^{1/[3-(\Delta_{\phi cs,m}+\Delta_{\phi ca,m}+K_{ss}+K_{sa})/2]}$（Eq. 28a）、温度 $k_BT_{loc,m}^{(j)}=\hbar v_{dw}/\xi_{loc,m}^{(j)}$（Eq. 28b）📜Q。典型条件（$\lambda_{mfp}=1\,\mu\text{m}$）下，畴壁**长于 $\sim0.1\,\mu\text{m}$、温度几 K 或以下** → Anderson 绝缘体 📜Q。

### 2.5 推导层：关联函数 + 相图

- **无电声耦合**（Sec. 6.1）：CDW/SDW 关联函数（Eq. 30）与 SSC/TSC 配对关联（Eq. 32）幂律，指数由表 1 给；纯电子系统**排斥相互作用利于 CDW/SDW**（抑制 SC）📜Q。
- **含电声耦合**（Sec. 6.2）：纵向声学声子 → 速度重整化 $\eta$（Eq. 36,39），降低配对关联指数 → **更强超导倾向** 📜Q；强耦合处 WB 奇异性 $v_{ep}^2=\min_m(c_{ph}u_m)$（Eq. 37 定义处）使模型失稳 📜Q。
- **相图**（Fig. 14）：按主导失稳指数划界——DW 相 / 关联网络（无隙"金属"）相 / SC 相；声子速度足够高时（Fig. 14(c)）低 $V_d$ 处 SC、中 $V_d$ 无隙网络、高 $V_d$ 处 DW；极高（不现实）声速（Fig. 14(d)）SC 区扩大 📜Q。**无平移不变 → 指数跨网络不同 → 预期 crossover 而非尖锐相变** 📜Q。

---

## 3. 结论清单（分层）

### 3.1 定理式主张（模型/公式产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 解析密度 | $\rho_{2D}$（Eq. 4）分离变量形式 | A1–A3、拟合 |
| 相互作用形式 | $U_{ee,n}$（Eq. 6）由密度 + 镜像电荷定 | A5 |
| 局域 DOS 标度 | $\rho_{dos}\propto T^{\beta_m}\cosh(\dots)|\Gamma(\dots)|^2$（Eq. 14） | A6 |
| 局域化判据 | 隙化相 $\Delta_{\phi cs}+\Delta_{\phi ca}<4$（Eq. 27） | RG |

### 3.2 估算

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 相互作用增强 | 超七倍（考察参数区） | A5 | 📜Q[~] |
| 局域化阈值 | 畴壁 $\gtrsim0.1\,\mu\text{m}$、几 K 或以下 | A8、$\lambda_{mfp}=1\,\mu\text{m}$ | 📜Q[~] |
| 拟合有效区 | $V_d\gtrsim1.2\hbar v_F k_\theta$（更低 $V_d$ 拟合差） | A3 | 📜Q[~] |
| 转角范围 | $\alpha_{AB}\in[1,2]\leftrightarrow0.35°\lesssim\theta\lesssim0.7°$ | A3 | 📜Q[~] |
| 参数默认值 | $\theta=0.5°$、$\alpha_{AB}=1.4$、$V_d/\hbar v_Fk_\theta=1.5$、$L_\parallel=0.5\,\mu\text{m}$、$L_z=6.68$ Å、$\epsilon_r=6.93$ | 计算取值 | 📜Q[~] |

### 3.3 预言（待实验验证）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 相互作用强度电可调（偏压/屏蔽/介电） | "we demonstrate" 📜Q | 中——可对比 Ref. [113] 屏蔽距离实验 |
| 局域 DOS 幂律标度（STS） | "serves as spectroscopic features … can be verified" 📜Q | 中——STS |
| Anderson 局域化（中等无序） | "potential Anderson localization" 📜Q | 中——输运 |
| DW↔SC 电学可调相图 | "these diagrams illustrate electrical tunability" 📜Q | 弱——相图依赖自由参数 |
| WB 奇异性（强电声） | "we identify" 📜Q | 弱——需强耦合 |

### 3.4 内部验证 + "没写什么"

1. **极限对照**：电荷反对称扇区近似非相互作用（$U_{ee,n}\approx V_{ee,n}$ 数值）📜Q；纯电子排斥 → DW（与 1D TLL 定性一致）📜Q。
2. **⚠️ 未做**：不引入 $T_c\sim10$–50 K（无源）；不引入 "$K<1$ 吸引 / $K>1$ 排斥"判据；不引入量子化电导平台；电声耦合强度是自由参数（作者明言未指定值）。

---

## 4. 假设-结论依赖图

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性 |
|---|---|---|---|
| A3 远离魔角小转角 | 到魔角（化学势效应不可忽略） | 解析密度/相互作用定量 | 边界——作者限定 |
| A5 镜像电荷近似 | $L_z\not\ll d$（薄介电） | $U_{ee,n}$ 定量 | 部分 |
| A4 平均场库仑 | 占据数涨落大 | $h_D$、能量依赖 $S$ 的定量 | 部分 |
| A7 自旋扇区非相互作用 | 邻近诱导 SOC/自旋相关作用 | 相图不区分单重态/三重态失效 | 边界——作者指出可 enrich |
| A9 电声自由参数 | 实际耦合未知 | SC 相边界、WB 位置 | 关键——相图定量依赖 |
| A8 有限 $N_\perp$ | 无横向平移不变 | 指数跨网络不同 → crossover 非尖锐相变 | 已被作者纳入 |

---

## 5. 接口（可检验性 / 设计原则 / 后续文献修正）

### 5.1 可检验性

STS 局域 DOS 幂律（Eq. 14）、Anderson 局域化长度/温度、DW↔SC 相图、介电材料/屏蔽距离依赖（对标 Ref. [113] 屏蔽实验）📜Q。

### 5.2 设计原则

偏压 $V_d$ 设约束强度 + 屏蔽长度 $d$/介电材料设相互作用 + 转角/压力设 $\alpha_{AB}$；三旋钮协同电调关联相 📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- **T24 Hsu 2023（同组前作）**：本文把 $U$ 从"自由参数"升级为"由连续模型 + 屏蔽算出"——同组方法递进 💭I。
- **Chou 2019 / Chen 2020 / Chou 2021（refs 67,68,72 等）**：本文明确"不预设相互作用形式"以区别于这些前作 📜Q。
- ⚠️ 旧 review "Tc~10–50 K""CDW 开隙→电阻陡增""1D→2D 维度渡越"均无源 → 已删。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 电声耦合为自由参数 | 值未指定 | 📜Q |
| 平均场库仑 | 无法捕捉 cotunneling 改占据 | 📜Q（作者自陈） |
| 自旋扇区非相互作用 | 相图不区分单重态/三重态 | 📜Q |
| 低 $V_d$ 拟合差 | $V_d\lesssim1.2$ 约束弱，拟合不准 | 📜Q |
| 单畴壁指数定相图 | 因无平移不变，实际是 crossover | 📜Q |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| Bistritzer-MacDonald 2007 (ref 26) / San-Jose & Prada 2013 (ref 30) / Efimkin 2018 (ref 32) | 引用——连续模型与畴壁网络基础 📜Q |
| Wu 2019 (ref 21) / Chou 2019 (ref 67) / Chen 2020 (ref 68) / Chou 2021 (ref 72) | 引用——前作网络模型（本文不预设相互作用形式以区别）📜Q |
| Emery 2000 / Vishwanath 2001 / Mukhopadhyay 2001 (refs 5–8) | 引用——sTLL/csTLL 起源 📜Q |
| Ref. [113]（屏蔽距离实验） | 引用——相互作用电调的实验动机 📜Q |
| Georgoulea 2022 (ref 51) | 引用——异质应变能隙/堆叠能量（方法）📜Q |

## 8. 对后续研究的影响

- 提供"**从单粒子连续模型定量算相互作用强度**"的系统方法，摆脱耦合线模型的 ad hoc 假设 📜Q。
- 确立畴壁网络为"电可调低维强关联平台"——关联不必在魔角 📜Q。
- 留下"电声耦合值 + 自旋相关相互作用"两个开放输入，供后续 enrich 相图 💭I。

## 9. 理论模型映射（供计算对标）

| 映射 | 说明 |
|------|------|
| 连续模型（Eq. 1） | TBPM/TB 可直接复现能带、电荷密度、$\Delta_a$、$v_{dw}$ |
| $\rho_{2D}$（Eq. 4） | 解析密度 → 供相互作用积分复用 |
| $U_{ee,n}$（Eq. 6） | 屏蔽库仑强度 → 供玻色化相图输入 |
| 局域 DOS 指数 $\beta_m$ | STS 幂律 → 实验对标量 |

## Phase S 目的接口（引用式）

- **Q1（edge state 如何表征）**：本文给**谱学 + 输运特征**——局域 DOS 幂律（Eq. 14）、Anderson 局域化长度/温度、关联函数指数 📜Q。
- **Q2（理论如何解释）**：连续模型 → 屏蔽相互作用 → 玻色化 → 关联相（DW/SC）竞争，强度可电调 📜Q。
- **Q3（理论↔实验对应）**：$V_d$/屏蔽距离 ↔ Ref. [113] 实验；STS 幂律 ↔ 局域谱学；介电材料 ↔ 器件设计 📜Q。

> **增量价值**：超出 TBPM 单粒子框架（本文是关联/多体）。价值在于"关联修正方向"——若 TBPM 单粒子结果与实验有定性差异，本文提供关联机制入口。不提供 $T_c$/电导平台数字。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取到 `/tmp/T26.txt`，grep 核对：**全部数字命中原文**——$\theta=0.5°$、$\alpha_{AB}=1.4$、$V_d/\hbar v_F k_\theta=1.5$、$w_{AA}/w_{AB}\in[0.2,0.5]$、$\alpha_{AB}\in[1,2]\leftrightarrow0.35°\lesssim\theta\lesssim0.7°$、$L_\parallel=0.5\,\mu\text{m}$、$L_z=6.68$ Å、$\epsilon_r=6.93$、$N_\perp=18$、第 9 近邻、七倍、$\lambda_{mfp}=1\,\mu\text{m}$、$\sim0.1\,\mu\text{m}$、$d=5/20/60$ nm、$c_{ph}=10v_F$、$V_d\gtrsim1.2$。

⚠️ 修正/降级：① arXiv 2311.14384 正文未出现 → 标"外部来源"；② 旧 review "$K<1$ 吸引/$K>1$ 排斥""$T_c\sim10$–50 K""CDW 开隙→电阻陡增""1D→2D 维度渡越"原文均无（grep `10 K`=0、`50 K`=0）→ 已删；③ 电声耦合强度为自由参数（作者明言未指定）→ 相图定量是"预言"非"事实"。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-11 | 初读（Phase 4 粗读）。 |
| 2026-08-20 | S-REV 机制重写：删旧版"$K<1$/$K>1$""CDW 开隙→电阻陡增""$T_c\sim10$–50 K""1D→2D 渡越"（无源）；改为原文（连续模型+屏蔽→玻色化→相图 DW/SC）。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（旧版归档 `archive/paper_review_T26_wang2024_2dmater.backup_20260908.md`）：补参数分册/假设清单/推导链（连续模型→密度拟合→屏蔽作用→玻色化→局域化→相图）/结论分层/假设-结论依赖图/接口；补 Eq. (1)–(28) 关键式与七倍/0.1 µm/18 线等数字；电声耦合标"自由参数"。 |
