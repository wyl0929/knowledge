<!--
 * @Author       : AI 精读 (paper-reading skill)
 * @Date         : 2026-08-11（初读）→ 2026-08-20（S-REV 机制重写）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T24_hsu2023_prb.md
 * @Description  : T24: Hsu, Loss & Klinovaja 2023 — moiré 量子线网络中一般散射与电子态（相互作用量子线 + 广义 Umklapp；2026-09-08 按 5 块演绎结构重写）
-->

# Paper Review: Hsu, Loss & Klinovaja (2023) — moiré 量子线网络中的一般散射与电子态

| 字段 | 内容 |
|------|------|
| **编号** | T24 |
| **标题** | General scattering and electronic states in a quantum-wire network of moiré systems |
| **作者** | Chen-Hsuan Hsu, Daniel Loss, Jelena Klinovaja |
| **期刊** | Physical Review B 108, L121409 (2023)（Letter） |
| **DOI / arXiv** | 10.1103/PhysRevB.108.L121409 / 2303.00759（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 理论 — 相互作用量子线网络的散射理论与电子态（玻色化/Luttinger 液体，无实验数据） |
| **课题组** | Hsu (Yukawa / Academia Sinica / RIKEN)、Loss & Klinovaja (RIKEN / U. Basel) |
| **PDF / SI** | ✅ `reference/pdfs/Hsu 等 - 2023 - General scattering and electronic states in a quantum-wire network of moiré systems.pdf`（正文 9 页 + Supplemental Material：特定 Hfs 模型、Table S1、QPC 细节） |
| **精读日期** | 2026-08-11（初读）→ 2026-08-20（机制修正）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」五块记（`note/shared/method/theory_paper_reading.md` §3）。本文是**多体白箱**——研究对象是玻色化的相互作用量子线 + 守恒律约束下的一般散射算符，结论是"哪些散射过程能隙化体/留手征边缘模"这类定理式主张，受单粒子假设到 Luttinger 假设限定。

---

## TL;DR

**本文想解决的理论问题**：强关联 moiré 体系（如 TBG）里，畴壁构成的量子线网络能否承载**拓扑相**——即什么样的散射过程能在分数填充处给出"隙化体 + 无隙手征边缘模"？

**主结果**：① 构造守恒律（电荷守恒 Eq. (4) + moiré 周期性允许的**广义 Umklapp** 动量守恒 Eq. (5)）约束下的一般散射算符 $O$（Eq. 3），把散射分成"常规散射"（Eq. 6–7，任意填充都允许）与"moiré Umklapp 散射"（填充条件 $\nu=P/(\sum s_{Rp\sigma})$，Eq. 8）两类 📜Q；② 识别四类 Umklapp 过程 $O_{\rm i}$–$O_{\rm iv}$：$O_{\rm i}$ 单线背散射给出分数电荷 $\pm e/2$；$O_{\rm iv}$ 给出**$n$ 条无隙手征边缘模**（体隙化）+ 分数激发 $\pm 2e/S_{0,c}$ 📜Q；③ Landauer-Büttiker 下得量子化霍尔电阻 $h/(ne^2)$（$n=1,\nu=3/4$ 给 $h/e^2$，与 Ref. [29] 观测一致），并预言 STS 局域 DOS 与 QPC 隧穿的普适标度律（Eq. 14–15）可探测手征边缘模 📜Q。

**结论/意义**：把网络模型从单粒子散射推广到**相互作用量子线**，为 TBG 观测到的量子反常霍尔/Chern 绝缘态（$C=\pm1,\pm2,\pm3$）提供一个"分数填充关联态"的耦合线机制 📜Q。⚠️ 全文是相互作用散射理论（"we construct/identify/demonstrate/expect"），非实验证实。

---

## 1. 模型白箱（玻色化量子线 + 散射算符）

### 1.1 哈密顿量/作用量（玻色化形式）

费米场玻色化（Eq. 1）：

$$\psi_{\ell m\sigma}^{(j)}(x)=\frac{U_{\ell m\sigma}^{(j)}}{\sqrt{2\pi a}}e^{i\ell k_F x}e^{-\frac{i}{\sqrt2}[\ell\phi_{cm}^{(j)}-\theta_{cm}^{(j)}+\ell\sigma\phi_{sm}^{(j)}-\sigma\theta_{sm}^{(j)}]}$$

其中 $j\in\{1,2,3\}$ 线列（三组平行线）、$m\in[1,N_\perp]$ 线内指标、$\ell\in\{R\equiv+,L\equiv-\}$ 方向、$\sigma\in\{\uparrow,\downarrow\}$ 自旋、$\xi\in\{c,s\}$ 电荷/自旋扇区；$a$ 短距截断、$k_F$ 费米波矢（所有线相同）。对易关系（Eq. 2）：$[\phi_\xi^{(j)m}(x),\theta_{\xi'}^{(j')m'}(x')]=(i\pi/2)\operatorname{sgn}(x'-x)\delta_{jj'}\delta_{\xi\xi'}\delta_{mm'}$ 📜Q。

未扰哈密顿量 $H_0+H_{fs}$ 描述交叉滑移 Luttinger 液体（csLL）不动点（ref 82）：$H_0$ 动能 + $H_{fs}$ 密度型二次项（marginally relevant 前向散射）📜Q。

**一般散射算符**（Eq. 3）：

$$O_{\{s_{\ell p\sigma}\}}=\prod_{m=1}^{N_\perp}\prod_{p=0}^{3}\prod_{j=1}^{3}\left[\psi_{R(m+p)\uparrow}^{(j)}\right]^{s_{R p\uparrow}^{(j)}}\left[\psi_{L(m+p)\uparrow}^{(j)}\right]^{s_{L p\uparrow}^{(j)}}\left[\psi_{R(m+p)\downarrow}^{(j)}\right]^{s_{R p\downarrow}^{(j)}}\left[\psi_{L(m+p)\downarrow}^{(j)}\right]^{s_{L p\downarrow}^{(j)}}$$

整数集合 $\{s_{\ell p\sigma}\}$ 刻画该算符（负值 = 厄米共轭 $\psi^s\equiv(\psi^\dagger)^{|s|}$，$s<0$）；$s\neq0$ 表示第 $p$ 近邻线参与散射 📜Q。

**约束（守恒律）**：
- 电荷守恒：$\sum_{p,\sigma}(s_{Rp\sigma}+s_{Lp\sigma})=0$（Eq. 4）📜Q；
- 广义动量守恒（moiré 周期势部分弛豫动量）：$k_F\sum_{p,\sigma}(s_{Rp\sigma}-s_{Lp\sigma})=\tfrac{2\pi}{\lambda}\times\text{integer}$（Eq. 5）📜Q。

### 1.2 参数分册

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | 填充因子 $\nu=k_F\lambda/\pi$（由栅压/化学势）、散射算符集合 $\{s_{\ell p\sigma}\}$、相互作用 $U$（$q\sim0$ 密度-密度分量） |
| **导出量** | $\lambda=a_0/[2\sin(\theta/2)]$、线间距 $d=\sqrt3\lambda/2$、$f=-S̄_{0,c}/S_{0,c}$、系数 $S_{p,\xi},S̄_{p,\xi}$（Eq. 10）、标度维数 $\Delta_{iv}$（Eq. 13） |
| **模型内部量（解的性质）** | 边缘模数目 $n$、分数电荷 $e^*/2$（$=\pm e/2$ 或 $\pm2e/S_{0,c}$）、霍尔电阻 $h/(ne^2)$ |
| **固定常数** | $e$、$\hbar$、$v_0$（速度）、$a$（短距截断）；**原文未给数值** $a_0,\theta,U$ |
| **预言量（可检验）** | STS 局域 DOS 标度 $\rho(\epsilon)$（Eq. 14）、QPC 隧穿电流 $I_t$（Eq. 15）、电导修正 $|\delta G|\propto\max(eV,k_BT)^{2f-2}$ |

> 无"反推量"层。**符号防混**：$s_{\ell p\sigma}$（散射算符指数）≠ 标度维数（原文用 $s$ 表 interarray 标度维数阈值）；$f$（=$-S̄_{0,c}/S_{0,c}$）是边缘模标度指数，非填充因子 $\nu$。

### 1.3 显式假设清单

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **Luttinger 液体（相互作用 1D）**——玻色化适用 | 模型 | 📜Q |
| A2 | **交叉滑移 LL 不动点**（$H_0+H_{fs}$）；$H_{fs}$ 具体形式不指定（引 ref 89,95；SI 给示范模型） | 模型 | 📜Q |
| A3 | **短程/有限程相互作用**（$s$ 在 $p$ 大时消失） | 模型 | 📜Q（"one expects s to vanish for large p"） |
| A4 | **$S̄_{p,s}=0$**（自旋扇区 $S̄$ 取零，"operators with nonzero $S̄_{p,s}$ are typically less RG relevant"） | 简化 | 📜Q |
| A5 | **无邻近诱导"外部"配对**（全局电荷/粒子数守恒） | 推导（Eq. 4 前提） | 📜Q |
| A6 | **单粒子近似→相互作用**：本文用 Luttinger 含相互作用（即**含**多体），但**不引入**自旋翻转/谷间散射 | 模型 | 💭I（原文未讨论谷间） |
| A7 | **RG 判据**：intra-array 相关需 $\Delta<2$；interarray 需 $s<1$ | 推导 | 📜Q |

> 判别性扫轴：填充 $\nu$（$P/4$，$P$ 整数）、散射类型（$O_i$–$O_{iv}$）、相互作用 $U$（足够大才 RG 相关）📜Q。

---

## 2. 推导链（顺论文顺序）

### 2.0 总览

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 模型层 | Bosonization | 费米场 $\psi$ | 玻色化 Eq. (1) + 对易 Eq. (2) | A1–A3 | 1D LL |
| 推导层 | General scattering operator | $O$ Eq. (3) + 守恒律 | 两类散射：常规（Eq. 6–7）vs moiré Umklapp（Eq. 8） | A5 | 任意 $\nu$ / 特定 $\nu=P/(\sum s_{Rp\sigma})$ |
| 推导层 | Moiré correlated states | Umklapp 过程 | $O_i$–$O_{iii}$→隙化体+分数电荷 | 玻色化 + sine-Gordon | — |
| 推导层 | Chiral edge modes | $O_{iv}$ | $n$ 条无隙手征边缘模 + $\pm2e/S_{0,c}$ | 手征场变换 Eq. (11) | RG 相关（$U$ 足够大） |
| 边界层 | Experimental signatures | STS/QPC | 标度律 Eq. (14)–(15)、$h/(ne^2)$ | Landauer-Büttiker | 单边缘模 |

### 2.1 模型层：玻色化 + 未扰不动点

- **输入**：费米场 $\psi_{\ell m\sigma}^{(j)}$。
- **输出**：玻色化 Eq. (1)、对易 Eq. (2)、未扰 $H_0+H_{fs}$（csLL 不动点）📜Q。
- **关键论证**：带宽 $W$ 为高能截断；无量纲耦合 $g/W$ 在（准）平带体系中更大 → 高阶散射更显著 📜Q。

### 2.2 推导层：一般散射算符 + 两类散射

- **输入**：$O$（Eq. 3）+ 守恒律。
- **电荷守恒** Eq. (4)：$\sum(s_{Rp\sigma}+s_{Lp\sigma})=0$ 📜Q。
- **动量守恒**：净体系动量差可由"晶格动量" $2\pi/\lambda$ 补偿（moiré 周期势）→ Eq. (5) 📜Q。
- **分类**：
  - **常规散射**（Eq. 6 满足 → Eq. 7 左右手粒子数各自守恒）——任意 $k_F$ 都允许，对应"crystalline states"（ref 89），产生 CDW/超导/Fermi 液体态 📜Q；
  - **moiré Umklapp 散射**（Eq. 6 不满足时仍可行）——用 $\nu=k_F\lambda/\pi$ 得填充条件 $\nu=P/(\sum_{p,\sigma}s_{Rp\sigma})$，$P$ 非零整数（Eq. 8）📜Q。$\nu=1$ ↔ 每 moiré 单胞 4 电子（TBG，ref 81,82）📜Q。

### 2.3 推导层：moiré 关联态（$O_i$–$O_{iii}$）

- 玻色化后 $O=\sum_m\exp[(i/\sqrt2)\sum_p(S_{p,c}\phi_{c(m+p)}+S̄_{p,c}\theta_{c(m+p)}+S_{p,s}\phi_{s(m+p)}+S̄_{p,s}\theta_{s(m+p)})]$（Eq. 9），系数 $S_{p,\xi}=s_{Lp\uparrow}-s_{Rp\uparrow}+\xi(s_{Lp\downarrow}-s_{Rp\downarrow})$、$S̄_{p,\xi}=s_{Lp\uparrow}+s_{Rp\uparrow}+\xi(s_{Lp\downarrow}+s_{Rp\downarrow})$（Eq. 10）📜Q。
- **$O_i$**（单线，$(s_{R0\sigma},s_{L0\sigma})=(2,-2)$，两自旋同）：4 电子在 $k_F$ 背散射到 $-k_F$，总动量差 $8k_F=4\nu\cdot(2\pi/\lambda)$ 由 moiré 势补偿 📜Q。$O_i+O_i^\dagger\propto m\cos(4\sqrt2\,\phi_{cm})$ → RG 相关时隙化所有 $\phi_{cm}$，强耦合极限 $\phi_{cm}$ 钉扎，kink 激发 = $\phi_{cm}$ 变 $\pm\pi/(2\sqrt2)$ 的隧穿 → **分数电荷 $\pm e/2$** 📜Q。
- **$O_{ii}$**（多线 intrawire）、**$O_{iii}$**（interwire 但每线粒子数守恒，$S̄_{p,c}=0$）：同样给出 sine-Gordon 项与关联绝缘态 📜Q。

### 2.4 推导层：手征边缘模（$O_{iv}$）

- **$O_{iv}$**：某些线不守恒粒子数（$S̄_{p,c}\neq0$）。取 $S_{n,c}=S_{0,c}$、$S̄_{n,c}=-S̄_{0,c}$，引入手征场 $\tilde\phi_{\ell m}=-\ell\phi_{cm}+f\theta_{cm}$（$f=-S̄_{0,c}/S_{0,c}$），对易式（Eq. 11）📜Q。
- 变换后 $O_{iv}+O_{iv}^\dagger\propto\sum_m\cos[\tfrac{S_{0,c}}{\sqrt2}(\tilde\phi_{L(m+n)}-\tilde\phi_{Rm})]$（Eq. 12）→ **一条边 $n$ 条无隙手征模 $\tilde\phi_{L,1..n}$、对边 $n$ 条右移模** 📜Q；再定义 $\tilde\phi_{m,n}$ 使任意 $m$ 对易 → 内部（体）模被隙化 📜Q。分数激发 $\pm2e/S_{0,c}$ 📜Q。预期形成"手征畴"、畴壁处无隙手征模（局域磁矩触发）📜Q。
- **标度维数**：$\Delta_{iv}=\tfrac12|S_{0,c}S̄_{0,c}|(1+\tfrac{2U}{\hbar v_0})^{-1/2}$（Eq. 13）；RG 相关条件 $\Delta_{iv}<2$ 对足够大 $U$ 满足 📜Q。

### 2.5 边界层：实验签名

- **Landauer-Büttiker**：量子化霍尔电阻 $h/(ne^2)$；$n=1,\nu=3/4$ 给 $h/e^2$（Ref. [29] 观测）📜Q。对应 $C=\pm1,\pm2,\pm3$（= $n$）在 $\nu=\pm3/4,\pm1/2,\pm1/4$ 📜Q。
- **STS 局域 DOS**：$\rho(\epsilon)\propto T^{2/f-1}\cosh[\tfrac{\epsilon}{2k_BT}+\tfrac1{2f}\ln(\tfrac{\epsilon}{2\pi k_BT})]$（Eq. 14）——普适标度曲线；指数**不依赖** $H_{fs}$（手征边缘模的拓扑性质，对比碳纳米管/螺旋液体）📜Q。
- **QPC 隧穿**：interedge 隧穿 $I_t\propto T^{2/f-1}\sinh(\tfrac{eV}{2k_BT})\,|\Gamma(\tfrac1f+\tfrac{ieV}{2\pi k_BT})|^2$（Eq. 15）；backscattering $|\delta G|\propto\max(eV,k_BT)^{2f-2}$ 📜Q。指数依赖 $f$ 但不直接依赖 $\nu$（对比分数量子霍尔态）📜Q。分数电荷可由散粒噪声探测 📜Q。

---

## 3. 结论清单（分层）

### 3.1 定理式主张（守恒律 + 玻色化论证产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 散射二分类 | 常规散射（Eq. 7）↔ moiré Umklapp（Eq. 8，$\nu=P/(\sum s_{Rp\sigma})$） | A5 |
| $O_i$→分数电荷 | $O_i$ 单线背散射 → $\pm e/2$ kink 激发 | A1、A4 |
| $O_{iv}$→手征边缘模 | $n$ 条无隙手征模 + 体隙化 + $\pm2e/S_{0,c}$ | A1、A4、RG |
| 量子化霍尔电阻 | $h/(ne^2)$ | Landauer-Büttiker |
| 拓扑性 | 边缘模标度指数**不依赖 $H_{fs}$** | 手征场构造 |

### 3.2 估算

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 分数电荷 | $\pm e/2$（$O_i$）、$\pm2e/S_{0,c}$（$O_{iv}$） | A1 | 📜Q[~] |
| 标度维数 | $\Delta_{iv}=\tfrac12|S_{0,c}S̄_{0,c}|(1+2U/\hbar v_0)^{-1/2}$ | RG | 📜Q[~] |
| RG 相关条件 | $\Delta_{iv}<2$（intra-array）、$s<1$（interarray） | RG | 📜Q[~] |

### 3.3 预言（待实验验证）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| STS 局域 DOS 普适标度曲线（Eq. 14） | "can be characterized" / "we demonstrate" 📜Q | 中——STS |
| QPC 隧穿电流（Eq. 15）、$|\delta G|$ 幂律 | "we consider" / "concrete predictions" 📜Q | 中——QPC 输运 |
| 分数电荷散粒噪声 | "can be used to detect" 📜Q | 中——噪声测量 |
| 分数 QAH 态、parafermion 平台 | "can reveal … provide a platform" 📜Q | 弱——远景 |

### 3.4 内部验证 + "没写什么"

1. **实验对标（自洽核对）**：$h/e^2$（$n=1,\nu=3/4$）"as observed in Ref. [29]" 📜Q；$C=\pm1,\pm2,\pm3$ 序列与 Refs. [30–32] 对应 📜Q。
2. **⚠️ 未做**：不引入 $4e^2/h$（本文是相互作用关联态，量子化值 $h/(ne^2)$，$n$=边缘模数）；不引入具体 $T_c$、具体 $\theta$ 数值、$a_0$ 数值。

---

## 4. 假设-结论依赖图

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性 |
|---|---|---|---|
| A1 Luttinger 液体 | 温度高/耦合弱到偏离 LL | 玻色化推导、分数电荷、手征边缘模 | 基础——整个框架 |
| A5 无外部配对 | 邻近诱导配对 | 电荷守恒 Eq. (4) 失效 → 散射分类改变 | 边界——作者限定 |
| A4 $S̄_{p,s}=0$ | 保留自旋扇区 $S̄$ | 结论定性不变（作者说非零 $S̄_{p,s}$ 更不相关） | 轻微 |
| RG（$U$ 足够大） | 相互作用弱 | $\Delta_{iv}<2$ 不满足 → 手征模不出现 | 关键——相存在条件 |
| 单边缘模（STS/QPC 简化） | 多边缘模 | Eq. (14)–(15) 需推广 | 简化——作者注明（SM） |

---

## 5. 接口（可检验性 / 设计原则 / 后续文献修正）

### 5.1 可检验性

STS 局域 DOS 普适标度曲线（Eq. 14）、QPC 隧穿电流与电导修正幂律（Eq. 15）、分数电荷散粒噪声 📜Q。

### 5.2 设计原则

moiré 周期势把动量守恒放宽为"晶格动量"守恒 → 广义 Umklapp 在特定分数填充生效；网络可在"更宽条件"下形成（谱隙可通过衬底/异质堆叠空间依赖地打开，非仅偏压）📜Q（作者 "we expect that the network can form under broader conditions"）。

### 5.3 后续文献修正（时间倒挂，💭I）

- **Chou 2019（ref 81）、Chen 2020（ref 82）、Wu 2019（ref 80）**：本文扩展的耦合线网络模型（前驱，作者自己引用）📜Q。
- **T26 Wang & Hsu 2024**：同一 Hsu 课题组的后续——把相互作用强度从"自由参数"改为**由连续模型+屏蔽效应算出**（本文 $U$ 是自由参数）💭I。
- ⚠️ 旧 review "统一 T9/T12/T15/T29 数学语言""θ=0/π/2 连接"均为 review 层无源综合，已删（原文未作此宣称）。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| $H_{fs}$ 不指定 | 前向散射具体形式依赖模型（SI 给示范） | 📜Q |
| 无谷间/自旋翻转散射 | 未讨论谷自由度对散射分类的修正 | 💭I |
| 畴形成需能量 | 手征畴壁形成需（无序诱导的）局域磁矩，有限温度下熵驱动 | 📜Q（"costs energy"） |
| 边缘模指数依赖 $f$ 非 $\nu$ | 与 FQH 不同，需微观模型输入 $S_{0,c},S̄_{0,c}$ | 📜Q |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| Wu 2019 (ref 80) / Chou 2019 (ref 81) / Chen 2020 (ref 82) / Chou 2021 (ref 83) / Lee 2021 (ref 84) | 直接扩展的网络模型（前驱）📜Q |
| Emery 2000 / Vishwanath 2001 / Mukhopadhyay 2001 (refs 85–88) | 引用——csLL/sTLL 起源（铜酸盐）📜Q |
| 耦合线 QH 态 (refs 89–99) | 引用——耦合线构造方法来源 📜Q |
| Serlin 2020 (ref 29) / Nuckolls 2020 (ref 30) / Choi 2021 (ref 31) / Das 2021 (ref 32) | 引用——Chern 绝缘体观测（实验对标）📜Q |

## 8. 对后续研究的影响

- 提供**守恒律约束下的一般散射算符**框架，把耦合线网络从"具体模型"提升为"分类工具" 📜Q。
- 把 moiré 网络的拓扑相（手征边缘模 + 分数激发）落到相互作用（Luttinger）层面，连接"分数 QAH"与耦合线构造 📜Q。
- 留下"相互作用强度 $U$ 从何而来"的开放问题——由 T26（同组后续）补上 💭I。

## 9. 理论模型映射（供计算对标）

| 映射 | 说明 |
|------|------|
| $\nu=k_F\lambda/\pi$ | 填充因子（$\nu=1$ ↔ 4 电子/单胞）→ TBPM/TB 可扫的填充 |
| 散射算符 $\{s_{\ell p\sigma}\}$ | 分类（常规 vs Umklapp）→ 可作相图标签 |
| 分数电荷 $\pm e/2,\pm2e/S_{0,c}$ | 可由散粒噪声/输运对标 |
| 手征边缘模数 $n$ ↔ $C$ | 本文 $n$ = 边缘模数，对应实验 Chern 数序列 📜Q |

## Phase S 目的接口（引用式）

- **Q1（edge state 如何表征）**：本文给**可测签名**——STS 局域 DOS 普适标度曲线（Eq. 14）、QPC 隧穿幂律（Eq. 15）、分数电荷散粒噪声、量子化霍尔电阻 $h/(ne^2)$ 📜Q。
- **Q2（理论如何解释）**：广义 Umklapp 散射（moiré 周期势 → 晶格动量守恒）→ 分数填充处关联态；$O_{iv}$ → 隙化体 + $n$ 条无隙手征边缘模 📜Q。
- **Q3（理论↔实验对应）**：$h/e^2$ ↔ Serlin 2020；$C=\pm1,\pm2,\pm3$ 序列 ↔ Refs. 30–32；STS/QPC 标度 ↔ 未来谱学/输运 📜Q。

> **增量价值**：与 T26 分工——本文是**散射分类 + 边缘模机制**（$U$ 为自由参数），T26 是**从连续模型算 $U$**。本文可直接供"耦合线相图"对标，不提供具体 $T_c$/电导平台数值（无 $4e^2/h$）。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取到 `/tmp/T24.txt`，grep 核对：**全部数字命中原文**——$\pm e/2$、$\pm2e/S_{0,c}$、$h/(ne^2)$、$h/e^2$（$n=1,\nu=3/4$）、$C=\pm1,\pm2,\pm3$（$\nu=\pm3/4,\pm1/2,\pm1/4$）、$\nu=P/4$、$\lambda=a_0/[2\sin(\theta/2)]$、$d=\sqrt3\lambda/2$、$\Delta_{iv}<2$、$s<1$、Eq. (14)(15) 形式。

⚠️ 修正/降级：① arXiv 2303.00759 正文未出现 → 标"外部来源"；② 旧 review "$S(\theta)$ 参数化、θ=0/π/2 连接 T9/T12、Peierls 磁场调控、节点缺陷局域化"原文均无 → 已删（保留在更正日志历史）；③ 本文是**相互作用**（Luttinger）框架，非单粒子 $S$ 矩阵散射——旧表述"每条畴壁=量子线、AA 节点=S 矩阵"的"单粒子散射"定性不准确；④ 未引入 $4e^2/h$（量子化值是 $h/(ne^2)$）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-11 | 初读（Phase 4 粗读）。 |
| 2026-08-20 | S-REV 机制重写：删旧版"$S(\theta)$ 参数化、θ=0/π/2 连接 T9/T12、Peierls 磁场调控、节点缺陷局域化"（无源）；改为原文机制（相互作用量子线 + 广义 Umklapp 散射算符 → 分数填充关联态）。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（旧版归档 `archive/paper_review_T24_hsu2023_prb.backup_20260908.md`）：补参数分册/假设清单/推导链/结论分层/假设-结论依赖图/接口；明确"相互作用"定性；显式声明不引入 $4e^2/h$；补 Eq. (1)–(15) 关键式与分数电荷/边缘模机制链。 |
