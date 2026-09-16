<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4 → 五块演绎结构重写)
 * @Date         : 2026-08-11（初读）→ 2026-08-20（S-REV 反向核对）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T38_hung2026_arxiv.md
 * @Description  : T38: Hung & Bansil 2026 — 螺旋畴壁环网络重塑超导关联（理论；2026-09-08 按 5 块演绎结构重写）
-->

# Paper Review: Hung & Bansil (2026) — 螺旋畴壁环网络重塑超导关联

| 字段 | 内容 |
|------|------|
| **编号** | T38 |
| **标题** | Helical Domain-Wall-Ring Networks Reshape Superconducting Correlations |
| **作者** | Yi-Chun Hung∗, Arun Bansil† |
| **期刊** | arXiv:2606.23599v1 [cond-mat.mes-hall]（2026-06-22） |
| **DOI / arXiv** | arXiv 2606.23599（预印本，无 DOI） |
| **类型** | 理论 — 相互作用螺旋畴壁环网络的超导关联（RG + 自洽变分） |
| **课题组** | Hung / Bansil（Northeastern U., 物理系 + Quantum Materials and Sensing Institute） |
| **PDF / SI PDF** | ✅ `reference/pdfs/Hung和Bansil - 2026 - Helical Domain-Wall-Ring Networks Reshape Superconducting Correlations.pdf`（正文 5 页 + SI S1–S7：玻色化约定/单粒子隧穿/库仑估计/HLL 动量空间/变分自洽方程/SC 关联函数/补充数值） |
| **精读日期** | 2026-08-11（初读）→ 2026-08-20（S-REV 反向核对）→ 2026-09-08（五块重写） |

> **结构说明**：本篇按「理论论文演绎结构」五块记（见 `note/shared/method/theory_paper_reading.md` §3）。理论论文的研究对象是**白箱**（作者自写的理想模型），结论受假设限定。
> **⚠️ 体系声明**：本文平台是**扭角双层 BiSb**（近期被提议的 moiré 螺旋畴壁网络平台，ref 61），**不是 TBG**。本文"helical"=**自旋-动量锁定**（QSHE 螺旋 Luttinger 液体），**非** TBG 畴壁网络的**谷-动量锁定**（San-Jose/Efimkin 的 helical）。两种"helical"是不同物理，勿跨论文混同（§6 陷阱）。
> **全文无 ±**：本文为纯理论，数字均为解析/数值设定参数，统一 📜Q[~]；📊F 不出现。

---

## TL;DR

**本文想解决的理论问题**：moiré 体系中的**闭合螺旋畴壁环网络**（有限尺寸准 1D 网络）中，约束效应与环几何如何重塑相互作用驱动的超导（SC）关联？——有限尺寸网络能否用"无限长耦合 1D 通道阵列"的截断来理解？

**主结果**：① **无限尺寸理论**（耦合无限长 HLL + RG）：环间 SC-pair 隧穿是 RG 相关的（relevant），通过环间相位锁定增强 SC 关联 📜Q；② **有限尺寸自洽变分理论**：即使在无限尺寸理论预言强耦合 pair 隧穿的区间（θt<θRG），诱导的相位锁定标度 mJ 仍被强烈抑制（m̃J≪1 且随 θt 减小而减小）——源于环几何软模增强的相位涨落 CΘ 📜Q；③ **SC 标度维数 ηSC 随转角减小持续下降、对 pair 隧穿强度不敏感**，与无限尺寸预期**定性失配**（qualitative mismatch）——ηSC 的演化不能仅由相位锁定标度与 θRG 判据推断 📜Q。

**结论/意义**：有限尺寸准 1D 网络**不能**简单当作无限尺寸对应物的截断版本，而可能承载**定性不同的集体行为**——约束效应、网络几何与相互作用在低能交织。⚠️ 全文为理论预言/数值结果，作者用词 show/find/reveal（数学构造），无实验验证。

---

## 1. 模型白箱（理想系统 + 假设清单）

> 研究对象是作者自写的**理想模型**（白箱）：moiré 拓扑畴上的螺旋畴壁环 + 相互作用。本节写**模型**（§1.1–1.2）与**假设清单**（§1.3）。

### 1.1 几何与单粒子场（正文 Eq. 1–3）

**畴壁环几何**（Fig. 1）：moiré 图案中的闭合拓扑畴（绿色区）被平庸背景（白色区）包围，畴壁螺旋态约束在包围畴的畴壁上形成**螺旋畴壁环**，尺寸随扭角减小而增大。小扭角极限近似为**圆角六边形**，六条近直段长度 $l_s\approx L/6\approx a_M/\sqrt3$（L=环周长，a_M=moiré 超晶格周期）📜Q。圆角 $l_c\ll L$，只贡献局域修正，低能可忽略 📜Q。

**螺旋畴壁态**（自旋-动量锁定，Eq. 1）：
$$
\psi_R(r)=U_{R,+,↑}(r)e^{ik_F r}+U_{R,-,↓}(r)e^{-ik_F r}
$$
r∈[0,L) 沿畴壁逆时针坐标，k_F 费米动量，R 环中心。环几何要求 $\psi_R(r+L)=\psi_R(r)$。慢变场 U_{R,+,↑}/U_{R,-,↓} 分别对应顺时针/逆时针移动模，**自旋锁定于传播方向**（下文省略自旋指标）📜Q。

**单粒子 Hamiltonian**（Eq. 3）：
$$
H_{0,R}=-i\hbar v_F\sum_{\xi=\pm}\int_0^L dr\, U^\dagger_{R,\xi}(r)\partial_r U_{R,\xi}(r)
$$

### 1.2 相互作用 + 玻色化 + 变分作用量（正文 Eq. 4–21 + SI）

**环内密度-密度**（Eq. 4）：$H_{intra,R}=\int_0^L\int_0^L drdr'\, V(r-r')\rho_R(r)\rho_R(r')$，$\rho_R=\sum_\xi U^\dagger_{R,\xi}U_{R,\xi}$。

**玻色化**（Eq. 5–6）：
$$
H_{HLL}=\sum_R\frac{\hbar u}{2\pi}\int_0^L dr\left[\frac1K(\partial_r\varphi_R)^2+K(\partial_r\vartheta_R)^2\right]
$$
$u=v_F(1+2V_0/\pi\hbar v_F)^{1/2}$、$K=(1+2V_0/\pi\hbar v_F)^{-1/2}$（V₀=V(r) 零动量分量）。

**环间密度-密度**（Eq. 7）：$H_{inter}=\sum_R\sum_{j=0}^5\int\int drdr'\,U(r-r')\rho_R(r)\rho_{R+a_j}(4l_s-r')$，$a_j=a_M(\cos\frac{j\pi}{3}\hat e_x+\sin\frac{j\pi}{3}\hat e_y)$。

**环间 SC-pair 隧穿**（Eq. 8）：
$$
H_T=-J_{SC}\sum_{R}\sum_{j=0}^5\int_{jl_s}^{(j+1)l_s}dr\, U^\dagger_{R+a_j,+}(r')U^\dagger_{R+a_j,-}(r')\,U_{R,-}(r)U_{R,+}(r)+\mathrm{H.c.}
$$
r′=4l_s−r，J_SC>0。**对称性来源**（正文 + SI S2）：相邻畴壁成**ortho-helical 构型**，TRS 只允许带快速振荡相位的单粒子隧穿（低能无关）；二阶效应生成非振荡 pair 隧穿 $J_{SC}\propto t_\perp^2$（t⊥ 单粒子隧穿幅，S8/S9）📜Q。

**两壁无限长极限**（Eq. 9–10）：
$$
H=\sum_{\mu=\pm}\frac{\hbar\tilde u_\mu}{2\pi}\int_0^{l_s}dr\left[\frac1{\tilde K_\mu}(\partial_r\varphi_\mu^{(\infty)})^2+\tilde K_\mu(\partial_r\vartheta_\mu^{(\infty)})^2\right]-\frac{J_{SC}}{(2\pi a)^2}\int_0^{l_s}dr\cos[2\sqrt2\,\vartheta_-^{(\infty)}(r)]
$$
$\tilde u_\pm=v_F(1+\frac{2V_0}{\pi\hbar v_F}\pm\frac{2U_0}{\pi\hbar v_F})^{1/2}$、$\tilde K_\pm=(1+\frac{2V_0}{\pi\hbar v_F}\pm\frac{2U_0}{\pi\hbar v_F})^{-1/2}$（U₀=U(r) 零动量分量）。

**RG 流 + θRG**（Eq. 11）：$d\tilde J_{SC}/dl=2(1-\tilde K_-^{-1})\tilde J_{SC}$（$\tilde J_{SC}\equiv J_{SC}/\hbar u$，l≡ln[a(l)/a(0)]）；由 $l_s\approx L/6\approx a_M/\sqrt3$ 与 $a_M\approx a/[2\sin(\theta_t/2)]$ 得 $\theta_{RG}\simeq2\sin^{-1}\left([\tilde J_{SC}(0)]^{1/[2(1-\tilde K_-^{-1})]}/(2\sqrt3)\right)$。θt<θRG 时 J̃SC 在段内达到强耦合；θt≳θRG 时 RG 流被有限段长截断 📜Q。

**SC 标度维数**（Eq. 12）：SC 不稳定性算符 $O_{SC}(r)=U_{R,+}U_{R,-}-U_{R,-}U_{R,+}\sim e^{i2\vartheta_R(r)}$，$\langle O^\dagger_{SC}(r)O_{SC}(0)\rangle\sim r^{-2\eta_{SC}}$。三个特征标度维数：退耦环 $\eta_{SC}^{(0)}=K^{-1}$；含环间密度-密度 $\eta_{SC}^{(U)}=(\tilde K_+^{-1}+\tilde K_-^{-1})/2$；θt<θRG 时 ϑ− 钉扎 → $\eta_{SC}^{(pin)}=\tilde K_+^{-1}/2$。排序 $\eta_{SC}^{(0)}>\eta_{SC}^{(U)}>\eta_{SC}^{(pin)}$ 📜Q。

**有限尺寸变分理论**（Eq. 13–20）：Gaussian 试探作用量 S₀，变分 Green 函数 G(m_J)，变分质量参数 m_J：$G^{-1}(m_J)=G_{HLL}^{-1}+m_J M$，$\delta[F_0+T\langle S-S_0\rangle_0]/\delta G(m_J)=0$（Eq. 13）。模展开 $\vartheta_R(r,\tau)=\frac1{\sqrt{NL}}\sum_{p=(q,k_n)}\int\frac{d\omega}{2\pi}e^{ip\cdot R-i\omega\tau}\vartheta_p(\omega)$，k_n=2πn/L。$G_{HLL,q}^{-1}(\omega)=\frac1{\pi\hbar u}\omega^2 K B_q^{-1}K+\frac{\hbar u}{\pi}A_q$（Eq. 15）；$[B_q]_{nm}=k_nk_m\left[\frac1K\delta_{nm}-\frac{2U_0}{\pi\hbar u}e^{i\frac{2\pi}{3}(n-m)}\frac{\sin\frac{\pi(n+m)}6}{\pi(n+m)}\sum_{j=0}^5\cos\left(q\cdot a_j-\frac{\pi(n+m)(2j-3)}6\right)\right]$（Eq. 16）——环间密度-密度耦合不同谐波 + moiré 尺度空间调制 📜Q。自洽方程 $m_J=J_{SC}\frac{\sum_q\mathrm{Tr}[M_q\tilde M_q^\dagger(m_J)]}{\sum_q\mathrm{Tr}[M_q M_q^\dagger]}$（Eq. 19）；涨落前因子 $e^{-2C_\Theta(r)}$，$C_\Theta(r)=\langle[\vartheta_{R+a_j}(4l_s-r)-\vartheta_R(r)]^2\rangle_0$（Eq. 20）。

**θU 交叉**（Eq. 21）：$\eta_{SC}(\theta_U)=\eta_{SC}^{(U)}$ 定义特征转角 θU，分隔 $\eta_{SC}>\eta_{SC}^{(U)}$ 与 $\eta_{SC}<\eta_{SC}^{(U)}$ 两区 📜Q。

### 1.3 参数分册（区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | 扭角 θt；环内/环间耦合强度 2V₀/πℏvF、2U₀/πℏvF；裸 pair 隧穿强度 J̃SC(0) |
| **导出量（由旋钮+常数算出）** | l_s≈L/6≈a_M/√3；a_M≈a/[2sin(θt/2)]；u、K、ũ±、K̃±；θRG（Eq. 11）、θU（Eq. 21）；ηSC^(0)/(U)/(pin) |
| **模型内部量（解的性质）** | 变分质量 m_J（相位锁定标度）、m̃J=m_J/m_J^(pin)；SC 标度维数 ηSC；涨落 CΘ(r) |
| **固定/设定参数** | 2V₀/πℏvF=1.18、2U₀/πℏvF=2.08（Fig. 2 主算例）；J̃SC(0)=0.08、θt=3°（SI S2）；ϵeff≈5、ℏvF≈0.5 eV·nm、e²/(4πϵ₀)≈1.44 eV·nm（SI S3） |
| **预言量** | 相位锁定标度被抑制 + ηSC 下降的共存（与无限尺寸失配）→ 可检验的集体行为差异 |

**估算来源（SI S3）**：屏蔽库仑 V₀=(e²/2πϵ₀ϵeff)ln(D_g/w)、U₀=(e²/2πϵ₀ϵeff)ln(D_g/d)（D_g 栅距、w 畴壁横向局域长、d 畴壁间距）；V₀/ℏvF≈1.152 ln(D_g/w)、U₀/ℏvF≈1.152 ln(D_g/d)；5≲D_g/w,D_g/d≲15 → 1.2≲2V₀/πℏvF, 2U₀/πℏvF≲2 → 数值范围 [1.1,2.1] 📜Q[~]。数值：31×31 q 点网格、40 个 r 积分点、收敛判据 10⁻¹⁰ 📜Q。

> **符号防混**：θt（扭角，BiSb moiré）≠ θU/θRG（特征转角判据）；V₀（环内）/U₀（环间）≠ u/ũ±（重整化速度）；K/K̃±（Luttinger 参数）≠ k_F/k_n（费米动量/环谐波动量）；m_J（变分质量）≠ a_M（moiré 周期）。⚠️ "helical" 本文 = 自旋锁定，非 TBG 谷锁定。

### 1.4 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **环=圆角六边形**：6 条直段 l_s≈L/6≈a_M/√3；圆角 l_c≪L 可忽略 | 模型 | 📜Q（正文 + ref 62 脚注） |
| A2 | **螺旋态=自旋-动量锁定 HLL**（QSHE 类），自旋指标省略 | 模型 | 📜Q |
| A3 | **ortho-helical 相邻壁**：TRS 使单粒子隧穿带振荡相位 → 低能无关；二阶生成 pair 隧穿 | 推导 | 📜Q（正文 + SI S2） |
| A4 | **仅 SC 通道**是 TRS 下对称允许的环间隧穿 | 推导 | 📜Q |
| A5 | **Tomonaga-Luttinger（HLL）低能描述** | 模型 | 📜Q |
| A6 | **连续 moiré**：a_M≈a/[2sin(θt/2)]，忽略细致公度条件 | 推导 | 📜Q |
| A7 | **物理耦合区间 d≲w**（有波函数重叠）；d≪w（强杂化、不成 HLL）排除；有限 K̃− 要求 2(U₀−V₀)/πℏvF<1 | 模型 | 📜Q（SI S3） |
| A8 | **屏蔽库仑 + 金属栅**：V₀∝ln(D_g/w)、U₀∝ln(D_g/d) | 模型 | 📜Q（SI S3） |
| A9 | **T→0、Matsubara 频率连续化**；零模被排除（不影响量子涨落） | 推导 | 📜Q |

---

## 2. 推导链（演绎结构：顺论文顺序，每步"输入→输出→所用假设/定理→合法域"）

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 模型层 | Helical domain-wall rings | 螺旋畴壁环 + 单粒子场 | HLL 作用量（Eq. 1–6） | A1/A2/A5 | 小扭角 |
| 推导层① | Inter-ring interactions | 环间相互作用 | SC-pair 隧穿 H_T（Eq. 8） | A3/A4（TRS） | ortho-helical |
| 推导层② | 无限尺寸 RG | 两壁 l_s→∞（Eq. 9–10） | RG 流 + θRG（Eq. 11） | A6 | θt<θRG 强耦合 |
| 推导层③ | 有限尺寸变分 | G_HLL + M + 试探作用量 | 自洽 m_J（Eq. 19）、ηSC、θU（Eq. 21） | A9 | T→0 |
| 结论层 | 数值结果（Fig. 2 + SI S7） | m̃J≪1、ηSC 下降 | 与无限尺寸失配 | — | 参数区间 |

### 2.1 模型层：HLL 作用量（Eq. 1–6）

输入=螺旋畴壁态场（Eq. 1）+ 环内库仑（Eq. 4）；玻色化 → 标准 HLL 作用量（Eq. 5），u、K 由 V₀ 定（Eq. 6）。合法域：小扭角（六边形近似，A1）。

### 2.2 推导层①：环间 SC-pair 隧穿（Eq. 7–8 + SI S2）

单粒子环间隧穿 $H_{Ts}=t_\perp\sum_{\xi=\pm}\sum_{R,j}\int dr\, e^{i\xi(2k_F r-4k_F l_s)}U^\dagger_{R+a_j,\xi}(4l_s-r)U_{R,\xi}(r)+H.c.$（S3）带快速振荡相位 → 一阶平均为零；二阶 cumulant 生成非振荡四费米子项（S6–S8）→ pair 隧穿 $J_{SC}\propto t_\perp^2$（S8）。TRS 下仅 SC 通道对称允许（A4）。合法域：ortho-helical 构型 + r′≃r、τ′≃τ 极限。

### 2.3 推导层②：无限尺寸 RG 与 θRG（Eq. 9–11）

两壁、l_s→∞，用对称/反对称场 φ±、ϑ±（Eq. 9），重整化速度/参数 ũ±、K̃±（Eq. 10）。标准推导 [67] → RG 流 $d\tilde J_{SC}/dl=2(1-\tilde K_-^{-1})\tilde J_{SC}$：当 K̃−>1（U₀>V₀，SI S3）pair 隧穿 relevant → 钉扎 ϑ− → ηSC 降到 ηSC^(pin)。由 l_s 与 a_M 的 θt 依赖 → θRG（Eq. 11）。合法域：无限长近似；θt<θRG 强耦合、θt≳θRG 被有限段长截断。

### 2.4 推导层③：有限尺寸变分（Eq. 13–21）

模展开 + G_HLL,q（Eq. 15）+ Bq（Eq. 16，环间密度-密度耦合不同谐波、moiré 空间调制）→ 变分 Green 函数 G⁻¹=G_HLL⁻¹+(m_J/(2πa)²)Mq（Eq. 17）→ 自洽方程（Eq. 19），涨落前因子 e^{−2CΘ}（Eq. 20）。ηSC 用有限尺寸标度形式 $[L\sin(\pi r/L)/\pi a]^{-2\eta_{SC}}$ 拟合（ref 71）。合法域：T→0、零模排除（A9）。

### 2.5 结论层：数值结果（Fig. 2 + SI S7）

- m̃J 全区间有限但 ≪1，且随 θt 减小而减小（CΘ 增强：moiré 尺度增大产生更多软模 + 环间作用进一步软化）📜Q。**对照**（SI S7-i）：设 CΘ=0 → mJ 增至 ~m_J^(pin)，恢复 CΘ 后骤降 → 涨落强烈抑制 pair 隧穿 📜Q。
- ηSC 对 J̃SC(0) 不敏感、随 θt 减小单调下降；即使 θt<θRG 仍显著 > ηSC^(pin)，并与 ηSC^(U) 交叉于 θU（Eq. 21）📜Q。
- **失配论证**：mJ 强抑制（弱相位锁定）本应在无限尺寸理论中对应 ηSC 增大，但 ηSC 反而下降 → ηSC 演化不能由相位锁定标度与 θRG 推断 📜Q。

---

## 3. 结论清单（分层：定理式主张 / 估算 / 预言）

### 3.1 定理式主张（RG/对称性论证的产物，受假设限定）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| Pair 隧穿 relevant | dJ̃SC/dl=2(1−K̃−⁻¹)J̃SC，K̃−>1 时 relevant | A4/A6/A7 |
| 单粒子隧穿低能无关 | TRS 振荡相位 → 一阶零，二阶生成 pair 隧穿（JSC∝t⊥²） | A3（ortho-helical） |
| 标度维数排序 | ηSC^(0)>ηSC^(U)>ηSC^(pin) | Eq. 12（V₀/U₀ 关系） |

### 3.2 估算（数值设定/经验判据，非严格定理）

| 估算 | 值 | 证据 |
|---|---|---|
| 主算例相互作用 | 2V₀/πℏvF=1.18、2U₀/πℏvF=2.08 | 📜Q[~]（Fig. 2） |
| 物理相互作用区间 | 2V₀/πℏvF、2U₀/πℏvF ∈ [1.1,2.1]（1.2≲…≲2） | 📜Q[~]（SI S3） |
| 库仑估计 | ϵeff≈5、ℏvF≈0.5 eV·nm、e²/4πϵ₀≈1.44 eV·nm、V₀/ℏvF≈1.152 ln(D_g/w) | 📜Q[~]（SI S3） |
| 补充算例 | J̃SC(0)=0.08、θt=3° | 📜Q[~]（SI S7-ii） |
| 数值精度 | 31×31 q 网格、40 积分点、收敛 10⁻¹⁰ | 📜Q[~]（SI S5-3） |

### 3.3 预言/主张（保留作者动词强度）

| 预言 | 作者措辞 | 可检验性 |
|---|---|---|
| 有限尺寸环网络与无限尺寸**定性失配** | "revealing a qualitative mismatch from the infinite-size expectation" 📜Q | 弱——需真实 moiré 体系比对 |
| 环网络可承载"qualitatively distinct collective behavior" | "may instead host qualitatively distinct collective behavior" 📜Q | 弱 |
| 相位锁定强抑制 + ηSC 下降共存的实验后果 | "would be an interesting direction for future study" 📜Q | 未给出具体预言 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

1. **负对照（去掉涨落前因子）**（SI S7-i）：设 CΘ=0 → mJ 增至 ~m_J^(pin)；恢复 CΘ → 骤降。确立"涨落抑制"是主因 📜Q。
2. **参数扫描一致性**（SI S7-ii + Fig. S2/S3）：固定 J̃SC(0)=0.08、θt=3° 扫 (2V₀,2U₀) → 趋势稳健；R² 随 θt 减小增大 → 小转角下标度形式描述更准 📜Q。
3. **无限尺寸↔有限尺寸对照**：m̃J、ηSC 与无限尺寸基准（θRG、ηSC^(pin)）直接对比，暴露失配 📜Q。

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性 |
|---|---|---|---|
| A3 ortho-helical 构型 | 非 ortho 几何 / 单粒子隧穿不被抑制 | SC-pair 隧穿为唯一通道（A4）崩塌 | 致命——pair 隧穿机制的前提 📜Q |
| A6 连续 moiré | 强公度锁定 | θRG（Eq. 11）定量失效 | 中等——作者明说"忽略细致公度条件"📜Q |
| A7 d≲w | d≪w 强杂化（不成 HLL） | HLL 描述本身失效 | 致命——作者明说 d≪w "not physically relevant"📜Q |
| A2 自旋锁定 HLL | 自旋不锁定/自旋翻转 | 螺旋 HLL 图景 | 致命 |
| A5 HLL 低能描述 | 强关联偏离 TLL | RG/变分框架 | 中等 |
| A1 六边形近似 | 大扭角（环小、圆角不可忽略） | 几何模型 | 中等——本文聚焦小扭角 |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性

- 本文**无直接实验预言**（只给"相位锁定强抑制 + ηSC 下降"的定性结论，作者说实验后果是"future study"）📜Q。可检验途径 = 比较不同 moiré 图案（不同扭角）的超导性质，检验 ηSC 对隧穿强度的不敏感性。

### 5.2 设计原则（有限尺寸准 1D 网络的告诫）

"有限尺寸准 1D 网络**不能**总被理解为无限尺寸对应物的截断版本"——研究 moiré 网络集体行为时，须显式纳入**约束效应 + 网络几何**，而非直接用耦合无限长通道阵列 📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- **无**（2026 预印本，无后续）。
- 与 Phase S 的关系：本文平台是 BiSb（自旋 helical），**非 TBG 谷 helical 网络**（T5/T9）。TBG 畴壁网络（量子谷霍尔）在文中仅作为"无限长耦合 1D 通道"的对照例子（refs 13–18）📜Q。本文的"有限尺寸环网络 vs 无限长通道"张力与 Phase S 的"网络 vs 独立 1D 通道"之争（T9/T12/T15/T29）**维度不同**（超导关联 vs 单粒子散射），勿混同 💭I。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 无实验预言 | 实验后果留给 future study | 📜Q |
| 配对对称性未命名 | SC 通道 OSC~e^{i2ϑR} 为对称允许，但本文未命名 s/p/d 波（旧笔记"s 波"为推断 💭I） | 📜Q（grep "s-wave/singlet" 无命中） |
| 平台非 TBG | 是 BiSb（ref 61），畴壁几何参数未从实验提取 | 📜Q |
| 连续 moiré | 忽略细致公度条件 | 📜Q |
| 单粒子隧穿幅 t⊥ 未定量 | "in principle, 可从波函数重叠得到"（S9），未算 | 📜Q |

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）

| 工作 | 关系 |
|------|------|
| Bordoloi-Kaplan-Singh 2026 (ref 61) | **直接引用/动机**——扭角双层 BiSb 的弛豫驱动拓扑畴 + 螺旋畴壁网络平台 📜Q |
| TBG 畴壁网络（Wu-Jian-Xu 2019 ref 13、Chen 2020 ref 14、Wang-Hsu 2024 ref 17 等） | 引用——作为"无限长耦合 1D 通道"的 moiré 网络例子 📜Q |
| QSHE HLL 文献（Kane-Mele 2005、Wu-Bernevig-Zhang 2006 ref 37、Hsu 系列 ref 31/32/50/60） | 引用——螺旋 Luttinger 液体 + Majorana/高阶拓扑的理论基础 📜Q |
| Thakurathi 2017 (ref 67) | 引用——RG 流标准推导来源 📜Q |
| Feynman 1972 / Giamarchi 2003 (refs 69/70) | 引用——变分方法 📜Q |

## 8. 对后续研究的影响

- 把 moiré 畴壁研究从"单粒子拓扑"推进到"**有限尺寸网络的相互作用集体行为**"📜Q。
- 提供"无限尺寸理论 vs 有限尺寸变分"的**对照框架**（θRG 作基准 + m̃J/ηSC 与无限尺寸基准对比）📜Q。
- 确立"约束效应 + 环几何 + 相互作用"三者在低能交织的核心图景 📜Q。

## 9. 理论模型映射（供 TBPM / Kubo 计算对标）

| 映射 | 说明 |
|------|------|
| HLL 作用量 → 1D 玻色化 | 本文是 1D 场论（玻色化 HLL），**非**实空间 TBPM 可直算；TBPM 需从紧束缚 H_TB 提取 t⊥（S9）再输入 HLL 框架 💭I |
| 参数 → 1D 模型 | u、K、ũ±、K̃± 由 V₀/U₀/ℏvF 定（Eq. 6/10）——1D 玻色化计算的输入 📜Q |
| 库仑估计 → 屏蔽模型 | V₀=(e²/2πϵ₀ϵeff)ln(D_g/w) 等（S11）——给定 ϵeff、D_g/w 可估 V₀/U₀ 📜Q |

> 本文无电导/量子化平台讨论，不引入电导数字。与 TBPM 的接口仅在"从畴壁波函数重叠提取单粒子隧穿幅 t⊥"这一层（S9）📜Q。

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：不直接回答——本文无实验表征。仅指出"有限尺寸环网络与无限尺寸通道阵列的集体行为定性不同"，为畴壁网络的超导关联表征提供理论动机 📜Q。
- **Q2（理论如何解释 edge state）**：本文解释的是**自旋 helical 畴壁环网络（BiSb）**的超导关联，非 TBG 谷 helical 畴壁态。对 Q2 的增量 = "有限尺寸准 1D 网络 ≠ 无限长通道截断"这一原则，可迁移到 mTBG 网络关联研究 💭I。
- **Q3（理论↔实验对应）**：无实验对标（平台 BiSb 畴壁几何未从实验提取）；预言方向 = 比较不同转角超导性质检验 ηSC 对隧穿强度不敏感 📜Q。

> **增量价值**：与 T26（Wang-Hsu 2024，电控关联畴壁网络）同属"畴壁 + 关联"新方向，但本文是**自旋 helical（QSHE）环网络 + SC-pair 隧穿 RG/变分**，T26 是 TBG 玻色化 TLL + 屏蔽库仑；两者体系与机制不同。本文对 Phase S 畴壁主线的增量 = "有限尺寸网络几何重塑关联"的方法论告诫。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` → `/tmp/T38.txt`（+`-raw` → `/tmp/T38_raw.txt`），逐项 grep 核对，**全部数字/公式命中原文**：

| 数字/短语 | grep 位置 | 结论 |
|------|------|------|
| 2V₀/πℏvF=1.18、2U₀/πℏvF=2.08 | 正文 Fig. 2 caption 附近 | ✓ 📜Q[~] |
| J̃SC(0)=0.08、θt=3° | SI S7-ii | ✓ |
| ϵeff≈5、ℏvF≈0.5 eV·nm、e²/4πϵ₀≈1.44 eV·nm、1.152 | SI S3 | ✓ |
| 1.2≲…≲2、[1.1,2.1] | SI S3 | ✓ |
| l_s≈L/6≈a_M/√3 | 正文 + Eq. 11 附近 | ✓ |
| 31×31、40 积分点、10⁻¹⁰ | SI S5-3 | ✓ |
| dJ̃SC/dl=2(1−K̃−⁻¹)J̃SC、θRG（Eq. 11）、θU（Eq. 21） | 正文 | ✓ |
| ηSC^(0)>ηSC^(U)>ηSC^(pin)（Eq. 12） | 正文 | ✓ |
| "qualitative mismatch from the infinite-size expectation" | 摘要 | ✓ |
| "ortho-helical configuration" | 正文 | ✓ |
| BiSb 平台（ref 61 Bordoloi-Kaplan-Singh） | 引言 | ✓ |
| JSC∝t⊥²（S8）、t⊥=⟨Ψi|H_TB|Ψj⟩（S9） | SI S2 | ✓ |

⚠️ **确认/降级**：① 旧版 "Little-Parks 振荡" 无源（grep "Little"=0）已删（继承 2026-08-20）；② 旧版 "超导岛 Josephson 阵列"/"frustration" 无源（grep "frustration"=0）已删；③ 旧版 "仅考虑 s 波"——原文未用 s-wave/singlet 命名（grep 0 命中），已降级为"配对对称性未命名"💭I；④ "helical"=自旋-动量锁定（QSHE），**非** TBG 谷锁定——已显式声明防跨论文混同。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-20 | （S-REV）§3 删 "Little-Parks 振荡"（grep "Little"=0）→ 改原文：有限尺寸环 + 约束效应对隧穿强度标度与无限尺寸**定性失配**；§2 删 "超导岛 Josephson 阵列"/"frustration"（grep "frustration"=0）→ 改原文：环间仅 SC-pair 隧穿对称允许（TRS 抑制单粒子）；§3 删 "环几何增强/抑制 Tc" → 改 SC 标度维数对隧穿强度不敏感。依据：appendix_B §B.5#31。 |
| 2026-09-08 | **按五块演绎结构整体重写**（应用户要求）。旧版归档 `archive/paper_review_T38_hung2026_arxiv.backup_20260908.md`。补全：模型白箱（HLL 作用量 Eq. 1–6 + 环间作用 Eq. 7–8 + 变分作用量 Eq. 13–21 + 参数分册 + 9 条假设清单）、推导链 5 层、结论分层、假设-结论依赖图、接口、理论模型映射、Phase S 三问。**显式声明平台=BiSb、helical=自旋锁定（非 TBG 谷锁定）**；"s 波"降级为未命名配对对称性。全部数字 grep 命中。 |
