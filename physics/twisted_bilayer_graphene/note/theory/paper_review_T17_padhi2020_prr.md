<!--
 * @Author       : AI 精读 (理论论文五块演绎结构)
 * @Date         : 2026-08-06（粗读）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T17_padhi2020_prr.md
 * @Description  : T17: Padhi, Tiwari, Neupert & Ryu 2020 — 转角畴间 moiré 电子的隧穿输运（理论 — 单粒子隧穿 + Landauer-Büttiker 输运签名）
-->

# Paper Review: Padhi, Tiwari, Neupert & Ryu (2020) — 转角畴间 moiré 电子的隧穿输运

| 字段 | 内容 |
|------|------|
| **编号** | T17 |
| **标题** | Transport across twist angle domains in moiré graphene |
| **作者** | Bikash Padhi, Apoorv Tiwari, Titus Neupert, Shinsei Ryu |
| **期刊** | Physical Review Research 2, 033458 (2020) |
| **DOI / arXiv** | 10.1103/PhysRevResearch.2.033458 / arXiv:2005.02406（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 理论 — 单粒子隧穿 + Landauer-Büttiker 输运（连续两带模型 + 转移矩阵 + 散射噪声，无实验数据） |
| **课题组** | Padhi (UIUC) / Tiwari (Princeton+PSI) / Neupert (Univ. Zürich) / Ryu (Univ. Chicago) |
| **PDF / SI PDF** | ✅ `reference/pdfs/Padhi 等 - 2020 - Transport across twist angle domains in moiré graphene.pdf`（正文 16 页 + Appendices A–E：DOS/自伴匹配条件/Snell 定律/转移矩阵/量子噪声） |
| **精读日期** | 2026-08-06（粗读）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」五块记（见 `note/shared/method/theory_paper_reading.md` §3）：**① 模型白箱 → ② 推导链 → ③ 结论清单（分层）→ ④ 假设-结论依赖图 → ⑤ 接口**。理论论文无黑箱、无反推、无可辨识实验（"白箱演绎"而非"黑箱溯因"）。
> **共享知识引用**：通用物理（Landauer-Büttiker 通道计数、Klein 隧穿、van Hove 奇点、WKB）锚点引用 `note/shared/physics/`（[PHY-LB] 等），不复制讲义。

---

## TL;DR

**本文想解决的理论问题**：TBG 器件间相位图差异大，普遍归因于**扭角空间不均匀性**（"twist disorder"）——器件分裂成若干不同转角的大畴（TAD，twist angle domain）。跨这些畴壁的 moiré 电子（低能准粒子）隧穿行为是什么？能否用全局输运量检测/量化局域转角变化？

**主结果**：① 跨畴壁隧穿可理解为畴壁处**有效阶跃势**，高度 $\Delta_{\rm step}=|\varepsilon_{vR}-\varepsilon_{vL}|$ 正比于转角差 📜Q；② 跨转角畴壁处 **Klein 隧穿不可能发生**（与单层石墨烯不同），低能电导被抑制、零偏压下出现随转角差标度的 **sub-meV 电导隙** 📜Q；③ 转角无序下的输运"**有噪声但亚 Poisson**"——微分 Fano 因子在两侧 vHS 能量附近**出现峰**，峰位与峰强即转角无序程度的量度，作者**提出**可作诊断工具 📜Q。

**结论/意义**：把"扭角不均匀性"从定性困扰转化为可用单粒子隧穿理论定量处理的问题，给出隧穿/电导/Fano 三个全局输运签名。⚠️ 全文为理论预言/估算，作者用词 show / find / propose / argue，**非已验证事实**；单粒子框架明确不适用于魔角强关联区。

---

## 1. 模型白箱（理想系统 + 假设清单）

### 1.1 两带有效哈密顿量（每谷）

从低能连续模型（引 de Gail 2011 [34]）约化得到的最低两带有效模型，写在子格 $A$（层 1）与 $B$（层 2）基下：

$$
H_0 = m_0\begin{pmatrix}
0 & (\hat k^\dagger)^2 - (\Delta K^\dagger)^2 \\[2pt]
(\hat k)^2 - \Delta K^2 & 0
\end{pmatrix}
$$

📜Q（原文 Eq. (1)）。其中 $m_0\equiv 2v_F^2/15\tilde t_\perp$，$v_F\approx 10^6$ m/s（纯净石墨烯 Dirac 速度）；层间耦合 $t_\perp\approx 0.27$ eV，小角度下近似为常数 $\tilde t_\perp\approx 0.4\,t_\perp$；本文**固定 $m_0=1$**（能量单位归一化）📜Q。$\hat k=\hat k_x+i\hat k_y$，$\hat k_i=-i\partial_i$；MBZ 复动量 $k=k_x+ik_y=|k|e^{i\varphi_k}$，原点在 M 点。$\hat k\leftrightarrow\hat k^\dagger$ 互换给出 $K'$ 谷理论 📜Q。Dirac 点在 $k=\pm\Delta K$，$\Delta K=K_\theta e^{i(\phi+\pi/2)}$；$2K_\theta=2K\sin(\theta/2)$ 为 MBZ 尺寸，$K=4\pi/3a_0$、$a_0\approx 0.25$ nm 📜Q。有限 tilt 角 $\phi$ 的相位在无畴壁时无可观测后果，六重对称使 $|\phi|\le\pi/6$（30°）📜Q。

**能散**（Eq. (2)）：

$$
\varepsilon^2(k)=\varepsilon_v K_\theta^2 + 2\varepsilon_v |k|^2\cos(2\varphi-2\phi)+\varepsilon_v|k|^4
$$

其中 $\varepsilon_v=m_0K_\theta^2=\varepsilon(0)$ 是 M 点对数 van Hove 奇点（vHS）处的鞍点能量 📜Q（见 Eq. (A3)）。

**变量含义表**：

| 符号 | 含义 | 值/定义 |
|---|---|---|
| $\theta$ | 扭角（各畴固定） | 旋钮 |
| $\phi$ | tilt 角（DW 相对 MBZ 的 K-K′ 边的取向） | 旋钮，$\vert\phi\vert\le\pi/6$ |
| $k_y$（或入射角 $\varphi$） | 沿 DW 守恒的动量分量 | 旋钮 |
| $\varepsilon$ | 入射 moiré 电子能量 | 旋钮 |
| $v_F$ | 纯净石墨烯 Dirac 速度 | $\approx 10^6$ m/s |
| $t_\perp,\tilde t_\perp$ | 层间耦合、约化层间耦合 | $\approx 0.27$ eV；$\tilde t_\perp\approx 0.4t_\perp$ |
| $m_0$ | 质量标度 | $2v_F^2/15\tilde t_\perp$，本文取 $=1$ |
| $K_\theta$ | 半 MBZ 尺寸 | $2K_\theta=2K\sin(\theta/2)$ |
| $K,a_0$ | 单层 Dirac 点 / 晶格常数 | $K=4\pi/3a_0$、$a_0\approx 0.25$ nm |
| $\varepsilon_v$ | vHS 鞍点能量（**非能隙**） | $m_0K_\theta^2=\varepsilon(0)$ |
| $a,b,c$ | 1D 本征方程系数 | Eq. (5)，见下 |

### 1.2 参数分册（区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | 两侧扭角 $\theta_L,\theta_R$、两侧 tilt 角 $\phi_L,\phi_R$、守恒动量 $k_y$（或入射角 $\varphi$）、能量 $\varepsilon$（或偏压 $V$） |
| **导出量（由旋钮+常数算出）** | $K_\theta=K\sin(\theta/2)$、$\Delta K=K_\theta e^{i(\phi+\pi/2)}$、$\varepsilon_v=m_0K_\theta^2$、$a,b,c$（Eq. (5)）、波矢 $k_j,\kappa_j$（Eq. (14)）、$\Delta_{\rm step}=\vert\varepsilon_{vR}-\varepsilon_{vL}\vert$ |
| **模型内部量（解的性质）** | 透射/反射系数 $T,R$、传输矩阵 $M$、电导 $G(V)$、Fano 因子 $F(V)$、DOS $\rho(\varepsilon)$ |
| **固定常数** | $v_F\approx10^6$ m/s、$t_\perp\approx0.27$ eV、$a_0\approx0.25$ nm、$K=4\pi/3a_0$、$m_0=1$、简并因子 $g=4$（谷×自旋） |
| **预言量（可检验）** | 零偏 sub-meV 电导隙、$G(V)$ 拐点 $\varepsilon^*=\varepsilon_{vL}+\Delta_{\rm step}$、Fano 峰位/峰强、输运隙 |

> 无"反推量 θ̂"层。**符号防混**：$\varepsilon_v$ 是 vHS 鞍点能量（M 点带底），**不是**畴区能隙；本文 $a_0\approx0.25$ nm 是作者给的单层晶格常数近似（非精确 0.246 nm），照原文保留。

### 1.3 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **单粒子**（无电子-电子相互作用） | 模型 | 📜Q（作者明确声明 noninteracting，Sec. VI/VII） |
| A2 | **低能两带约化**（消去高能带，含拓扑性质在内被忽略） | 模型 | 📜Q（引 de Gail [34]） |
| A3 | **谷间解耦**（不同谷 $|K-K'|\sim\lambda^{-1}\gg a_0^{-1}$，分开处理单谷） | 模型 | 📜Q（Sec. IV D） |
| A4 | **1D 突变畴壁** + $|\theta_L-\theta_R|<1°$ | 推导 | 📜Q |
| A5 | **有效带参数 $a,b,c$ 取 Eq. (5) 形式**（即 $\varepsilon_v\propto K_\theta^2$、无弛豫/褶皱/相互作用修正） | 模型 | 📜Q（作者 Sec. VII 自述为最需谨慎处） |
| A6 | **弹道/相干输运**（Landauer-Büttiker 适用，杂质极少） | 推导（Sec. VI） | 📜Q |
| A7 | **零温极限**（$V\gg(e\beta)^{-1}$，费米函数→阶跃） | 推导（Eq. (28)） | 📜Q |
| A8 | **两带模型有效域 $2°<\theta\lesssim10°$** | 模型合法域 | 📜Q（Sec. VII 自述） |

> 判别性扫轴：$\theta$ 轴（$\theta_L=1.1°$，$\theta_R=1.2°/1.3°/1.11°/0.7°$）、$\varepsilon$ 轴（跨 vHS）、$k_y$（正入射→斜入射）、$\phi$ 轴（0→30°）📜Q。

---

## 2. 推导链（顺论文演绎顺序）

### 2.0 总览：一条演绎链

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 模型层 | Sec. II | 连续模型 | 两带 $H_0$ + 能散 Eq. (2) | A1–A5 | $2°<\theta\lesssim10°$ |
| 推导层 | Sec. III | $H_0$ + 1D DW | 传输矩阵 $M$、$T,R$（Eq. 12/13） | A4、自伴匹配条件（附录 B） | 突变界面 |
| 推导层 | Sec. IV | $T,R$ | 纵向 DW 正/斜入射、多 DW 共振、平滑 DW | A4 | $|\theta_L-\theta_R|<1°$ |
| 边界层 | Sec. V | tilt 角 | $O(\phi^4)$ 修正 Eq. (27) | 微扰论 | $|\phi|\lesssim30°$ |
| 推导层 | Sec. VI | $T(k_y,\varepsilon)$ | $G(V)$（Eq. 28）、$F(V)$（Eq. 30） | A6、A7 | 弹道零温 |
| 边界层 | 附录 C | 线性低能展开 | 人工石墨烯 Klein 隧穿 + Snell 定律 | 低能 $\varepsilon\ll\varepsilon_v$ | 非 TBG（另速 Dirac 锥） |

### 2.1 模型层：两带模型与能散（Sec. II）

- 输入=TBG 低能连续模型（两层 Dirac + moiré 层间耦合）；输出=两带 $H_0$（Eq. (1)）+ 能散 Eq. (2) 📜Q。
- 关键结构：扭角折进 $\Delta K=K_\theta e^{i(\phi+\pi/2)}$（Dirac 点位于 $k=\pm\Delta K$），**不显式旋转层**；能散含 $\cos(2\varphi-2\phi)$ 项使 M 点成为 $\varepsilon_v$ 的 vHS 📜Q。
- Berry 相位：低能 moiré 电子（近 CNP）相位差 $\eta=\phi+\pi/2+\varphi_q$，闭合轨道得 Berry 相位 $\pi$（对比 MLG $\pi$、BLG $2\pi$）📜Q。

### 2.2 推导层：隧穿计算与转移矩阵（Sec. III）

- **模型化**：1D DW 在 $x=0$，$H_{DW}=H_0(\phi_L,\theta_L)\Theta(-x)+H_0(\phi_R,\theta_R)\Theta(x)$（Eq. (3)）📜Q；$k_y$ 守恒，$k_x\to-i\partial_x$ → 1D 本征方程 $\varepsilon^2=\partial_x^4-a\partial_x^2-ib\partial_x+c$（Eq. (4)），系数
  $$a(\theta,\phi)=2(K_\theta^2\cos2\phi+k_y^2),\quad b(\theta,\phi)=4k_yK_\theta^2\sin2\phi,\quad c(\theta,\phi)=k_y^4+K_\theta^4-2k_y^2K_\theta^2\cos2\phi \tag{5}$$
  📜Q。
- **四阶方程四解**：实数解 $k_x=\pm k_{L,R}$（传播模）、虚数解 $k_x=\pm i\kappa_{L,R}$（衰减模，BLG 特有，MLG 无）📜Q。
- **匹配条件**：$\psi_L(0,y)=\xi\psi_R(0,y)$、$\partial_x\psi_L=\xi\partial_x\psi_R+\zeta\psi_R$（Eq. (9)），$\xi=a_L/a_R$、$\zeta=i\xi(b_R/a_R-b_L/a_L)/2$，由自伴性导出（附录 B）📜Q。
- **结果**：$R=|M_{21}/M_{22}|^2=(k_L-k_R)^2/(k_L+k_R)^2$、$T=1/|M_{22}|^2=4k_Lk_R/(k_L+k_R)^2=1-R$（Eq. (12)(13)）——**与阶跃势隧穿同形** 📜Q。

### 2.3 推导层：纵向 DW（Sec. IV）

- **正入射（$k_y=0$）**：波矢 $k_j^2=-K_{\theta j}^2+\sqrt{\varepsilon^2+4k_y^2K_{\theta j}^2}$ 等在 $\phi=0$ 时（Eq. (14)）📜Q。能谱两侧带底分别为 $\varepsilon_{vL},\varepsilon_{vR}$；$\varepsilon>\max(\varepsilon_{vL},\varepsilon_{vR})$ 时隧穿完美（$T\to1$），$\varepsilon_{vL}<\varepsilon<\varepsilon_{vR}$ 时仅左侧有传播模→全反射。**有效阶跃势高度 $\Delta_{\rm step}=|\varepsilon_{vR}-\varepsilon_{vL}|$** 即隧穿隙，随转角差增大 📜Q。$\theta_R<\theta_L$ 时阶跃势变"下坡"，互换 $k_L\leftrightarrow k_R$ 即可 📜Q。
- **斜入射**：$k_y^2=\sin^2\varphi[-\cos2\varphi\pm\sqrt{\varepsilon^2-\sin^2 2\varphi}]$（Eq. (15)）；$k_y\ne0$ 时隧穿仅当 $\varepsilon>\varepsilon_{vR}-k_y^2$（**阶跃尺寸减小**，斜入射增强隧穿）📜Q。正入射 $T$ 强烈依赖能量（0→1 可调），**不同于 MLG（恒为 1）与 BLG（恒为 0）**——TBG 势垒的独有特征 📜Q。
- **多 DW 共振隧穿**：三畴 $T=1-(K-4k_1k_2^2k_3)/(K+4k_1k_2^2k_3)$，$K=(k_1^2+k_2^2)(k_2^2+k_3^2)+(k_1^2-k_2^2)(k_2^2-k_3^2)\cos(\eta_1-\eta_3)$（Eq. (16)）📜Q。当 $\eta_1=\eta_3$（正入射，或 $\theta_1=\theta_3$）→ $T=4k_1k_3/(k_1+k_3)^2$（Eq. (17)），**与中间畴转角无关**；$n$ 个 DW 归纳为 $T=4k_1k_{n+1}/(k_1+k_{n+1})^2$（Eq. (18)）；$\theta_1=\theta_{n+1}$ → $T=1$（共振隧穿）📜Q。
- **平滑 DW**：宽度 $w\gg\lambda$ 时用 WKB，$T\approx e^{-2\gamma(w)}$、$\gamma(x)=\int_0^x p_+(y)dy$（Eq. (22)）；线性 $\theta(x)$ 时 $\varepsilon_v(x)\approx K^2\bar\theta(\bar\theta+2x\nabla\theta)/4$、$(\bar\theta,w\nabla\theta)=\tfrac12(\theta_R\pm\theta_L)$（Eq. (23)），用 Airy 函数精确解 📜Q。$w k_F\gg1$ 时指数压制隧穿。

### 2.4 边界层：tilt 角（Sec. V）

- $O(\phi_j^4)$ 微扰展开（Eq. (26)），得 $T/T^{(0)}\approx 1+\sqrt{T^{(0)}R^{(0)}}[\phi_R^2\tilde\varepsilon_R-\phi_L^2\tilde\varepsilon_L+\frac{\kappa_L^0-\kappa_R^0}{\kappa_L^0+\kappa_R^0}(\phi_L\tilde\varepsilon_L-\phi_R\tilde\varepsilon_R)^2]+O(\phi_j^3)$（Eq. (27)）📜Q。修正 $\propto\sqrt{T^{(0)}R^{(0)}}$，故**永不显著**（$R^{(0)}$ 在能隙内→0、越过隙→$T^{(0)}\to0$）📜Q；tilt 修正无 $O(\phi_j)$ 项（因 $(\phi_L,\phi_R)\to(-\phi_L,-\phi_R)$ 对称）📜Q。

### 2.5 推导层：输运与噪声（Sec. VI）

- **电导**：Landauer-Büttiker，$dI/dV=G_0W\int\frac{d}{d\varepsilon}f(\varepsilon-eV)d\varepsilon\int\frac{dk_y}{2\pi}T(k_y,\varepsilon)\approx G_0W\int\frac{dk_y}{2\pi}T(k_y,eV)\equiv G(V)$（Eq. (28)），$G_0=ge^2/h$、$g=4$（谷×自旋）、$W$ 样品宽度（$\lambda_F\sim O(100\ \text{nm})$）📜Q。零温极限（A7）。
- **电导特征**：有限偏压下 $G$ 随转角差增大而减小；零偏 $G$ 线性→0（DOS 亦线性）；输运隙随 $\Delta_{\rm step}$ 增大，拐点 $\varepsilon^*=\varepsilon_{vL}+\Delta_{\rm step}$ 表征转角无序强度 📜Q。**conductance minimum 不被扭角无序移动**（因 $k_y\approx K_{\theta L}$ 的零隙粒子在 $\theta_L\ne\theta_R$ 侧变有隙，无法散射过去；常规无序则能移动）📜Q。
- **Fano 因子**：$F(V)=\frac{1}{2e}\frac{dS/dV}{dI/dV}=\frac{G_0}{egG(V)}\int dk_y\,T(k_y,eV)R(k_y,eV)$（Eq. (30)）📜Q。峰出现在 $\varepsilon^*=\varepsilon_{vL}+\Delta_{\rm step}$，峰强随 $\Delta_{\rm step}$ 增大 → **转角无序越大、输运越"噪"** 📜Q。高温极限 $T\approx1$ → $F\to0$；无转角无序时 $F\approx0$ 📜Q。MLG 大纵横比样品的普适最大值 $F=1/3$ 在 TBG **不成立**（因一侧 Dirac 粒子隧穿到另一侧变有隙）📜Q。

### 2.6 边界层：人工石墨烯的 Klein 隧穿与 Snell 定律（附录 C）

- 低能线性化 $H_0$（$\varepsilon\ll\varepsilon_v$）→ 两速 Dirac 模型（Eq. (C1)），$4K_\theta^2$ 扮演"Dirac 速度" 📜Q。
- 动量+能量守恒 → Snell 型定律 $\lambda_L\sin\varphi_L=\lambda_R\sin\varphi_R$（Eq. (C4)），$\lambda_{L,R}=2\pi/3K_{L,R}$ 📜Q；$\theta_R>\theta_L$ 时有临界角 $\varphi_{Lc}=\sin^{-1}(\lambda_R/\lambda_L)$，超过则全反射 📜Q。
- $\varepsilon=0$ 时 $T=1$（Klein 隧穿），$q_y=0$ 时 $T_0^\perp=4\varepsilon_{vL}\varepsilon_{vR}/(\varepsilon_{vL}+\varepsilon_{vR})^2$ 常数；能量修正 $O(\varepsilon^4)$（Eq. (C8)），$T$ 与 $\phi$ 无关 📜Q。**此节明确不适用于 TBG 畴壁**（TBG 中 Dirac 粒子总隧穿到有隙粒子），只适用于冷原子"人工石墨烯"或不同 Dirac 速度界面 📜Q。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

### 3.1 定理式主张（数学/散射论证的产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 阶跃势等价 | 跨畴壁隧穿 $T=4k_Lk_R/(k_L+k_R)^2$（Eq. 13）与阶跃势隧穿同形 | A4 |
| Klein 隧穿缺失 | 跨转角 DW 处 Dirac 粒子无法 Klein 隧穿（一侧总隧穿到有隙态） | A2、A4 |
| 首末转角决定律 | 平行 DW 阵列的正入射隧穿 $T=4k_1k_{n+1}/(k_1+k_{n+1})^2$ 仅由首末转角决定；$\theta_1=\theta_{n+1}\Rightarrow T=1$ | A4、$\eta_1=\eta_3$ |
| 电导极小值不动 | 扭角无序不移动 TBG 的 conductance minimum（常规无序能） | A1–A4、A6 |

### 3.2 估算（经验/近似，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 有效阶跃势高度 | $\Delta_{\rm step}=\vert\varepsilon_{vR}-\varepsilon_{vL}\vert$ | A2、A5 | 📜Q[~] |
| 两带模型有效域 | $2°<\theta\lesssim10°$（上界：$\varepsilon_v\ll$ 上带底 $\approx15\tilde t/2$；下界：重整化费米速度非负） | A2 | 📜Q[~] |
| moiré 周期/λF 标度 | $\theta\approx1°$：$\lambda=13$ nm（$\approx50a_0$）、minibandwidth $\sim10$ meV、$\lambda_F\gtrsim12$ nm | 引文+估算 | 📜Q[~] |
| 实验 $\theta$ 梯度 | $\partial_x\theta=(0.02°–0.05°)/\mu m$（≈2–5%/μm，即每 10–15 moiré 周期变 1%） | 引 Uri 2020 | 📜Q[~] |
| MLG 普适 Fano 上限 | $F=1/3$（大纵横比单层） | 引文 | 📜Q[~]（背景，非本文值） |

### 3.3 预言（可检验性 → §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 零偏 sub-meV 电导隙 + $G(V)$ 拐点 $\varepsilon^*$ 表征转角无序 | "show / find"（数学构造）📜Q | 中——偏压电导谱 |
| 微分 Fano 因子峰（峰位 $\varepsilon_{vL}+\Delta_{\rm step}$、峰强∝$\Delta_{\rm step}$）可诊断转角无序 | "propose ... could be used as a concrete tool" 📜Q | 中——散粒噪声测量 |
| 可设计超低电压 [$O(\lesssim1\ \text{meV})$] 开关 | "one can design" 📜Q | 弱——器件蓝图 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

1. **解析↔数值互验**：Eq. (13) 解析 $T$ 与 Fig. 2/3 数值作图一致；正入射阶跃势图景（Fig. 2 top）与 $T$ 曲线（Fig. 2 bottom）对应 📜Q。
2. **极限对照（负对照）**：$\theta_R>\theta_L$（上坡阶跃）vs $\theta_R<\theta_L$（下坡）互换 $k_L\leftrightarrow k_R$，两类曲线互为镜像；MLG（$T=1$）与 BLG（$T=0$）作对照凸显 TBG 特有"0→1 可调" 📜Q。
3. **量级核对**：$\lambda=13$ nm、$\lambda_F\gtrsim12$ nm 用于论证"突变 DW 近似对低能准粒子合理" 📜Q。

### 3.5 概念区分（作者论证中的"分类"）

| 区分 | 依据 | 结论 |
|---|---|---|
| TBG 隧穿 vs MLG/BLG 隧穿 | 正入射 $T$ 能量依赖（0→1 可调 vs 恒 1 vs 恒 0）📜Q | TBG 势垒独有特征 |
| 扭角无序 vs 常规无序 | 是否移动 conductance minimum（否 vs 是）📜Q | 两类无序区分 |
| 上坡 vs 下坡阶跃势 | $\Delta_{\rm step}$ 符号（$\theta_R>\theta_L$ vs $\theta_R<\theta_L$）📜Q | 隧穿不对称 |
| TBG 畴壁 vs 人工石墨烯 | 是否总隧穿到有隙态（是 vs 否）📜Q | Klein/Snell 只适用于后者 |

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A5 有效带参数 $a,b,c$ 取 Eq. (5) | 晶格弛豫/层褶皱/电子相互作用 | $\varepsilon_v$ 值、$\Delta_{\rm step}$、隧穿切换点、电导/Fano 定量 | **作者自认最大脆弱点** → 建议把 $a,b,c$ 当唯象参数 📜Q |
| A2 两带约化 | $\theta$ 出 $2°–10°$ 域（尤其魔角平带） | 整个两带模型失效 | 作者声明强关联（魔角）不适用 📜Q |
| A1 单粒子 | 相互作用（近 vHS DOS 增强） | 电导 $G(V)$、Fano 定量 | 作者声明近魔角不匹配实验 📜Q |
| A4 突变 1D DW | DW 有限宽/有限长（电子可"绕过"） | 完美反射 $R=1$ 难实现、$T=1$ 受修正 | 用平滑 DW WKB（Eq. 22）补盲 📜Q |
| A3 谷间解耦 | umklapp 谷间散射（接近 MBZ 中心） | 单谷隧穿描述失效 | 作者声明避开 MBZ 中心（$\lambda_F$ 最小处）📜Q |
| A7 零温极限 | 有限温 | Fano 峰被抹平、$F$ 变化 | 作者声明 Fano 峰有限温会 smeared 📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- 偏压电导谱：零偏 sub-meV 电导隙 + 拐点 $\varepsilon^*=\varepsilon_{vL}+\Delta_{\rm step}$（Fig. 5a）📜Q；
- 散粒噪声：微分 Fano 因子峰（Fig. 5b，峰位 $\varepsilon^*$、峰强∝$\Delta_{\rm step}$）📜Q；
- 作者主张 Fano 测量比局域成像更简单（"simpler experimental tool ... than more involved local measurements"）📜Q。

### 5.2 设计原则（超低电压开关蓝图）

转角 DW + 金属接触施加阶跃势 → 超低电压 [$O(\lesssim1$ meV$)$] 开关 📜Q（作者 "one can design"，💭I 蓝图）。

### 5.3 后续文献修正（时间倒挂，💭I）

- 本文是**单粒子、非拓扑**框架，与同批 T18（De Beule Floquet 网络）、T19（Chou 相互作用）形成互补：本文处理**转角畴**（twist-angle DW），后两者处理**堆叠畴**（AB/BA DW，偏压 QVH 网络）——两类"畴壁"不同。
- 与 T20（Kwan 关联畴壁）都处理"转角/衬底变化产生的畴"，但本文单粒子、T20 强关联 HF，物理层次不同 💭I。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 单粒子框架 | 近魔角强关联输运不适用 | 📜Q（作者声明） |
| 两带模型有效域窄 | $2°<\theta\lesssim10°$；魔角/平带被排除 | 📜Q |
| 有效带参数脆弱 | 弛豫/褶皱/相互作用未建模，作者自述为最大不确定性 | 📜Q |
| 未处理相互作用 | 未考虑相互作用对 DW 输运的效应（如超导-正常畴壁） | 📜Q（Sec. VII 展望） |
| 未处理随机多 DW | 单/少 DW 分析，随机分布 DW 网络未处理 | 📜Q（Sec. VII 展望） |
| 非拓扑 | 全文无 Chern/谷陈数/拓扑保护论证，属散射输运框架 | 📜Q（无此类词，正文聚焦隧穿） |

## 7. 与其他工作的关系（跨论文对标放这里）

| 工作 | 关系 |
|------|------|
| de Gail et al. 2011 (ref 34) | **直接引用**——两带有效模型来源（低能连续模型约化）📜Q |
| Uri et al. 2020 Nature 581, 47 (ref 21) | **直接引用**——扭角无序实空间成像（$\partial_x\theta=(0.02°–0.05°)/\mu m$），本文实验动机 📜Q |
| Bistritzer-MacDonald 2011 (ref 24)、Lopes dos Santos 2007/2012 (refs 22,23) | 连续模型谱系 📜Q |
| He/Chu/He 2013 (ref 25)、Katsnelson 2006 (ref 26) | 手征隧穿/Klein 隧穿背景 📜Q |
| San-Jose 2014 (ref 51) | BLG 堆叠畴的类似输运隙 📜Q |
| Tworzydło 2006 (ref 47)、Danneau 2008 (ref 59) | 石墨烯散粒噪声普适 $F=1/3$ 📜Q |

> ⚠️ Phase S 外部对标（**非本文引用**，时间倒挂 💭I）见 §5.3。

## 8. 对后续研究的影响

- 把"扭角不均匀"从定性困扰转化为**单粒子隧穿可定量处理的问题**，给出"有效阶跃势 $\Delta_{\rm step}$"这一核心物理量 📜Q。
- 提供全局输运诊断工具（电导隙 + Fano 峰），可作为实验标定转角无序的候选方案（作者 propose）📜Q。
- 明确"转角畴壁隧穿 ≠ 堆叠畴壁 TPH 网络"——是 mTBG 畴壁物理的**另一条支线**（单粒子散射而非拓扑）💭I。

## 9. 理论模型映射（供 TBPM / NEGF 计算对标）

| 映射 | 说明 |
|------|------|
| $\theta\to\varepsilon_v\to\Delta_{\rm step}$ | 转角差 → vHS 能量差 → 阶跃势高度（Eq. 2 + Sec. IV A）📜Q |
| $H_0$（Eq. 1）→ TBPM | 两带模型是 TBPM/紧束缚的低能对照；可复现 Eq. (2) 能散与 vHS 📜Q |
| $T(k_y,\varepsilon)$ → NEGF/Landauer | Eq. (13)(16)(18)(22) 提供解析透射，可作 NEGF 数值互验锚点 📜Q |
| $G(V)$、$F(V)$ → Kubo/噪声 | Eq. (28)(30) 对应弹道输运电导与散粒噪声，可作计算扩展 💭I（[PHY-LB]） |

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：本文**不处理拓扑边缘态**——它研究**转角畴壁的隧穿/电导/Fano** 签名（零偏电导隙 + Fano 峰），与 AB/BA 畴壁 TPH 网络的 DOS/$\sigma_{xx}$ 签名是**不同对象** 📜Q。
- **Q2（理论如何解释）**：单粒子散射框架——有效阶跃势 $\Delta_{\rm step}=|\varepsilon_{vR}-\varepsilon_{vL}|$ 解释隧穿隙与电导极小值不动 📜Q；对"畴壁态=拓扑通道"图景**无贡献**（非拓扑）💭I。
- **Q3（理论↔实验对应）**：$\theta$ 梯度 ↔ 实验转角无序（Uri 2020）；$G(V)$ 拐点/Fano 峰 ↔ 输运诊断；超低电压开关 ↔ 器件蓝图 📜Q。

> **增量价值**：为"转角畴"（非堆叠畴）输运提供唯象阶跃势框架，与 T18/T19/T20 分工——本文是**单粒子 + 非拓扑 + 转角畴**，T18 是**拓扑网络 + Floquet**、T19 是**相互作用 + 堆叠畴网络**、T20 是**强关联 + 衬底畴壁**。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` + `-raw` 提取到 `/tmp/T17.txt`，逐项 grep 核对：**全部数字命中原文**——

| 数字 | grep 命中位置 | 结论 |
|------|--------------|------|
| $m_0\equiv2v_F^2/15\tilde t_\perp$、$v_F\approx10^6$ m/s、$t_\perp\approx0.27$ eV、$\tilde t_\perp\approx0.4t_\perp$、fix $m_0=1$ | Sec. II | ✓ 📜Q[~] |
| $a_0\approx0.25$ nm、$K=4\pi/3a_0$、$2K_\theta=2K\sin(\theta/2)$ | Sec. II | ✓ |
| $\theta=1.18°$（Fig. 1） | Fig. 1 caption | ✓ |
| $\lambda=13$ nm（≈50$a_0$）、minibandwidth $\sim10$ meV、$\lambda_F\gtrsim12$ nm | Sec. IV D | ✓ |
| $\partial_x\theta=(0.02°–0.05°)/\mu m$ | Sec. IV D | ✓ |
| $2°<\theta\lesssim10°$、$\approx15\tilde t/2$ | Sec. VII | ✓ |
| $F=1/3$（MLG） | Sec. VI | ✓ |
| $(\theta_L,\theta_R)=(1.1°,1.2°)/(1.1°,1.3°)/(1.1°,0.7°)/1.11°$ | Fig. 3/5/6 captions + 正文 | ✓ |
| $g=4$、$G_0=ge^2/h$、$\lambda_F\sim O(100\ \text{nm})$ | Sec. VI | ✓ |
| $|\theta_L-\theta_R|<1°$、$|\phi|\le\pi/6$ | Sec. III / Sec. II | ✓ |

⚠️ 修正/降级：① 本文**不引入量子化电导平台**（如 $4e^2/h$）——全文无此量，已显式声明；② 本文 $a_0\approx0.25$ nm 为作者给的近似值（非标准 0.246 nm），照原文保留；③ arXiv 号正文未出现 → 头部表标"外部来源"。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（粗读版：一句话总结 + 核心贡献 + 关联） |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求；方法论 §4.0 定位：理论论文是"白箱演绎"非"黑箱溯因"）。旧版归档 `archive/paper_review_T17_padhi2020_prr.backup_20260908.md`。补：两带 $H_0$ 显式矩阵、参数分册（删反推量层）、8 条假设清单、推导链（Sec. II→VI + 附录 C）、结论分层、假设-结论依赖图、反向核对 pass。 |
| 2026-09-08 | **降级/删除**：① 旧版 "转角畴壁上出现谷极化 1D 通道，类似 QVH 畴壁" 无源——原文无"谷极化通道/QVH"措辞，本文是非拓扑散射框架，已删除并显式声明"不处理拓扑边缘态"；② 未引入量子化电导。 |
