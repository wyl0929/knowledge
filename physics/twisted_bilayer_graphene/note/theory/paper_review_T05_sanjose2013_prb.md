<!--
 * @Author       : AI 精读 (系统辨识式阅读法 → 三层分离整理)
 * @Date         : 2026-08-06（初读）→ 2026-09-02（4 块辨识结构）→ 2026-09-08（S-Q2-T5 执行 + 反向核对）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T05_sanjose2013_prb.md
 * @Description  : T5: San-Jose & Prada 2013 — mTBG 层间偏压下螺旋网络（理论 — 螺旋网络模型奠基；2026-09-08 按 5 块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: San-Jose & Prada (2013) — 层间偏压下扭角双层石墨烯中的螺旋网络

| 字段 | 内容 |
|------|------|
| **编号** | T5 |
| **标题** | Helical networks in twisted bilayer graphene under interlayer bias |
| **作者** | Pablo San-Jose, Elsa Prada |
| **期刊** | Physical Review B 88, 121408(R) (2013) |
| **DOI / arXiv** | 10.1103/PhysRevB.88.121408 / 1304.5344（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 理论 — 螺旋网络模型奠基（连续模型 + 紧束缚模拟，无实验数据） |
| **课题组** | San-Jose (ICMM-CSIC) / Prada (UAM) |
| **PDF / SI PDF** | ✅ `reference/pdfs/San-Jose和Prada - 2013 - Helical networks in twisted bilayer graphene under interlayer bias.pdf`（正文 5 页 + Supplemental Material：DOS-θ 谱与 Kubo 光学电导） |
| **精读日期** | 2026-08-06（初读）→ 2026-09-02（4 块）→ 2026-09-08（S-Q2-T5 + 5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」的五块记（见 `note/shared/method/theory_paper_reading.md` §3）：**① 模型白箱 → ② 推导链 → ③ 结论清单（分层）→ ④ 假设-结论依赖图 → ⑤ 接口**。理论论文无黑箱、无反推、无可辨识实验（是"白箱演绎"而非"黑箱溯因"），故不用"四层变量表 + 判别表"。
> **共享知识引用**：通用物理（Berry/valley Chern、螺旋 vs 手征、Landauer-Büttiker 通道计数、网络 miniband、双栅偏压）已剥离到 `note/shared/physics/`，用锚点 `[PHY-BERRY] [PHY-LB] [PHY-MB] [PHY-GATE]` 引用。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的理论问题**：扭角双层石墨烯（TBG）在均匀层间偏压 $U$ 下，能否**不经应变**、仅靠偏压让 AB/BA 畴壁自发承载拓扑保护的螺旋模，并构成一张可编程的二维导电网络？

**主结果**：① 小角度 + 足够大偏压 → AB/BA 区打开能隙、谷陈数符号相反并被电子耗尽 → 畴壁出现**每谷每自旋 2 条**螺旋模（TPH），构成三角 **Chalker-Coddington 型**离域网络（能窗 $|\varepsilon|<|U|/2$）📜Q；② 网络形成经验判据 Eq. (1)：$z^2(l_\perp/L_M)^2 < U/\gamma_\perp < 1$，据此估算 $U\sim90$ meV 需 $L_M\gtrsim290a_0$（$\theta<0.2°$）、100 nm 周期阈值偏压 $\sim45$ meV 📜Q（作者 "estimate"）；③ 谷混合吸附原子/空位可**阻断单条链接** → 作者**提出**"可编程拓扑纳米电子学"（propose / open the possibility；TB 模拟 Fig. 3 支持）📜Q。

**结论/意义**：首次把畴壁物理从"孤立边缘态"推进到"**连通网络**"范式——mTBG 畴壁网络物理的开创性理论。⚠️ 全文为理论预言/估算，作者用词 propose / find / show / estimate / believe，**非已验证事实**（后续 Efimkin 2018 系统化、Tsim 2020 TZM 部分推翻连通性，见 §5.3/§7）。

---

## 1. 模型白箱（理想系统 + 假设清单）

> 理论论文的研究对象是**白箱**——作者自写的理想模型，无需"反推内部"。本节只做两件事：**写下模型**（§1.1–1.2），**列出它成立的全部假设**（§1.3）。假设清单是本文一切结论的"前提集合"，§4 的依赖图据此展开。

### 1.1 哈密顿量（每谷、自旋简并）

写在 $A,B,A',B'$ 基（$A,B$=下层、$A',B'$=上层，ref 7 符号）下的 $4\times4$ 显式矩阵：

$$
H(\mathbf k,\mathbf r)=
\begin{pmatrix}
U/2 & \hbar v_F\pi_+^\dagger & V^*(\mathbf r) & V^*(\mathbf r-\delta\mathbf r)\\[2pt]
\hbar v_F\pi_+ & U/2 & V^*(\mathbf r+\delta\mathbf r) & V^*(\mathbf r)\\[2pt]
V(\mathbf r) & V(\mathbf r+\delta\mathbf r) & -U/2 & \hbar v_F\pi_-^\dagger\\[2pt]
V(\mathbf r-\delta\mathbf r) & V(\mathbf r) & \hbar v_F\pi_- & -U/2
\end{pmatrix}
$$

📜Q（原文 Eq. 前矩阵；`pdftotext -raw` 复核各元素与 dagger 位置：$(1,2)=\pi_+^\dagger$、$(2,1)=\pi_+$、$(3,4)=\pi_-^\dagger$、$(4,3)=\pi_-$）。

**逐块结构**：① 左上/右下对角 $2\times2$ 块 = 下层（$A,B$，Dirac 点偏移 $+\Delta K/2$）与上层（$A',B'$，偏移 $-\Delta K/2$）的层内 Dirac 项，各带偏压 $\pm U/2$；② 左下 $2\times2$ 块 $T(\mathbf r)=\begin{pmatrix}V(\mathbf r)&V(\mathbf r+\delta\mathbf r)\\V(\mathbf r-\delta\mathbf r)&V(\mathbf r)\end{pmatrix}$ = 层间耦合（AA 对角项 $V(\mathbf r)$、AB/BA 类次对角项 $V(\mathbf r\pm\delta\mathbf r)$），右上为其厄米共轭 $T^\dagger$。

**变量含义表**：

| 符号 | 含义 | 值/定义 |
|---|---|---|
| $\theta$ | 扭角（$\theta=0$ 即 AA 堆叠） | 旋钮 |
| $U$ | 均匀层间偏压（下层 $+U/2$、上层 $-U/2$） | 旋钮 |
| $A,B,A',B'$ | 下层两子格 $A,B$、上层两子格 $A',B'$ | 基 |
| $\pi_\pm$ | 含 Dirac 点动量偏移的升/降算子 | $k_x+i(k_y\mp\Delta K/2)$ |
| $\Delta K$ | 两层 Dirac 点动量偏移 | $2\lvert K\rvert\sin(\theta/2)$ |
| $K$ | 单层 Dirac 点 | $\lvert K\rvert=4\pi/3a_0$ |
| $a_0$ | 单层 Bravais 晶格常数 | 2.46 Å |
| $L_M$ | Moiré 周期（$\theta<30°$） | $a_0/[2\sin(\theta/2)]$ |
| $V(\mathbf r)$ | 层间耦合的周期调制函数 | $\tfrac13\gamma_\perp\sum_{i=1}^3 e^{ig_i\cdot r}$ |
| $\gamma_\perp$ | 层间耦合强度 | $\approx0.33$ eV |
| $a_{1,2}$ / $g_{1,2}$ | Moiré 晶格矢量 / 倒格矢 | $L_M=\lvert a_{1,2}\rvert$；$g_i\cdot a_j=2\pi\delta_{ij}$，$g_3=0$ |
| $\delta\mathbf r$ | AB/BA 子格中心相对 AA 中心的偏移 | $\pm(a_1-a_2)/3$ |
| $v_F$ | 单层费米速度 | 固定参数 |
| $\varepsilon_M(\theta)$ | 低能能标（两锥在 M 点相交能量，**非能隙**） | $\hbar v_F\Delta K/2\approx88$ meV·θ(deg) |
| $\alpha(\theta)$ | 无量纲耦合参数（分大/小角度两区） | $\gamma_\perp/[6\varepsilon_M(\theta)]$ |

> **结构要点**：① 扭角被折进 $\pi_\pm$ 的动量偏移 $\mp\Delta K/2$（两层 Dirac 锥各移 $\pm\Delta K/2$，整体分离 $\Delta K$），**不显式旋转层**——本文连续模型的简化关键；② $V(\mathbf r)$ 三个谐波（$g_3=0$ 给常数项）在 AA 点（$\mathbf r=0$）相加得 $V=\gamma_\perp$，在 AB/BA 点相位相消使层间退耦 → 开隙结构 📜Q。

### 1.2 参数分册（替代"四层变量表"：区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $\theta$（扭角）、$U$（均匀层间偏压）、$\varepsilon$（能量，扫谱） |
| **导出量（由旋钮+常数算出）** | $L_M=a_0/[2\sin(\theta/2)]$、$\varepsilon_M(\theta)=\hbar v_F\Delta K/2\approx88$ meV·θ(deg)、$\Delta K=2\lvert K\rvert\sin(\theta/2)$、$R=L_M/(2\sqrt3)$、$l_\perp=\hbar v_F/\gamma_\perp\approx7.3a_0$、$\alpha(\theta)$ |
| **模型内部量（解的性质）** | 谷 Chern 数 $C_K$、TPH 模数 $N$、能带 / DOS / 色散、重整化费米速度 $v_F^*$ |
| **固定常数** | $a_0=2.46$ Å、$\lvert K\rvert=4\pi/3a_0$、$\gamma_\perp\approx0.33$ eV、$v_F$ |
| **预言量（可检验）** | sharp 局域共振 DOS 峰、$\sigma_{xx}(\omega)$、Fig. 2/3 空间概率密度图案、链接"开关" |

> 无"反推量 θ̂"层——理论论文不反推自数据（见 methodology §4.0）。**符号防混**：$\gamma_\perp$（层间耦合≈0.33 eV）≠ $l_\perp$（层间耦合长度≈7.3$a_0$）；$\varepsilon_M$ 是两 Dirac 锥相交能量，**不是畴区能隙**。

### 1.3 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **谷间解耦（谷守恒）**：连续模型构造上保谷守恒；要求 $U$ 与晶格光滑于 $a_0$ 尺度 | 模型 | 📜Q |
| A2 | **自旋简并**：自旋作为整体 ×2，不进入矩阵 | 模型 | 📜Q |
| A3 | **完美周期 Moiré**（"perfectly periodic model"，作者原话）：无晶格弛豫/原子重构 | 模型 | 📜Q |
| A4 | **单粒子**（无多体/关联） | 模型 | 💭I（原文未讨论关联） |
| A5 | **低能连续描述**（不依赖详细晶格学） | 模型 | 📜Q（refs 40–44） |
| A6 | **两分量近似**（合法域 $U<\gamma_\perp$） | 推导（Eq. (1)） | 📜Q |
| A7 | **一维突变 AB/BA 界面** + 均匀偏压 | 推导（Eq. (1)） | 📜Q |
| A8 | **95% 衰减阈值**（经验选择，非物理必然） | 推导（Eq. (1)） | 📜Q |

> 判别性扫轴：$\theta$ 轴（$4°\to0.2°$）、$U$ 轴（0–180 meV，Fig. 1/2）、$\varepsilon$ 轴（$|\varepsilon|<|U|/2$）📜Q。这些假设在 §4 逐一映射到"失效 → 结论崩塌"。

---

## 2. 推导链（演绎结构：顺论文顺序，每步"输入→输出→所用假设/定理→合法域"）

### 2.0 总览：论文四节是一条演绎链，不是并列四主题

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | Band topology and helical modes | 偏压 AB/BA 堆叠 | 谷陈数反号 → 界面每谷每自旋 2 模 | 体-边对应、谷陈数（引 refs） | 谷守恒（A1） |
| 模型层 | Continuum theory | 4×4 哈密顿量 + 参数 | 大/小角度两区 | A1–A5 | 低能连续 |
| 推导层 | U↔TPH 判据 | 模型 + 一维突变界面 | 判据 Eq. (1) | A6–A8 | $U<\gamma_\perp$ |
| 边界层 | atomic defect 影响 | 谷守恒假设 | 被缺陷打破 → 可编程 | 谷间散射 | — |

### 2.1 前提定理层：能带拓扑与螺旋模（"Band topology and helical modes" 节）

- **偏压开隙 + 谷 Chern 数**：Bernal 型（AB/BA）堆叠加偏压 $U$ 在各谷打开能隙；$U<\gamma_\perp$ 时单谷（非量子化）谷 Chern 数近似量子化 $C_K=-C_{K'}\approx\text{sign}(U)$ 📜Q。AB 与 BA 堆叠互为镜像，谷 Chern 数相反：$C_K^{AB}(\varepsilon)=-C_K^{BA}(\varepsilon)$ 📜Q。
- **畴壁 TPH 模**：$U$（因而 $C_K$）空间反号的界面，或 AB→BA 平滑过渡，各产生**每谷每自旋 2 条** TPH 模 📜Q。体-边对应 $N=|C_2-C_1|\mod2$；本文 $\mod2$ 缺省（$N=2$）因只考虑谷守恒扰动 → "weak" 拓扑保护 📜Q。
- **helical 定义**：helical vs chiral = 有/无时间反演不变性（ref 4）📜Q；石墨烯双层螺旋模 = 传播方向与谷量子数**固定锁定**（ref 15）📜Q。每条链接两谷承载相反方向电流（Fig. 2 白箭头）📜Q；"helicity 通过动量散射抑制耗散" 📜Q。
- 背景锚点：Bernal 双层加偏压开隙的实验上限 250 meV（refs 10,11，Mak 2009 / Zhang 2009）📜Q——"偏压可调隙"的实验动机，非本文扭角体系数值。

### 2.2 模型层：连续模型两区（"Continuum theory" 节）

- **大角度（$\theta\gtrsim1°$，$\alpha\ll1$）**：可微扰处理。van Hove 奇点 $\varepsilon_{vH}\approx\varepsilon_M(1-2\alpha)$（Fig. 1(b) 中峰位 $\sim0.6\varepsilon_M$ 📜Q[~]）、$v_F^*\approx v_F(1-9\alpha^2)$ 📜Q。加偏压仅把两 Dirac 锥平移 $\pm U/2$（本征态分层局域）→ $|\varepsilon|<|U|/2$ 内 DOS 平坦（类 AA 堆叠双锥），**不形成网络**（Fig. 1，$\theta=4°$ 算例，$L_M\approx14.3a_0$）📜Q。
- **小角度（复杂区）**：$U=0$ 时二次 van Hove 奇点随 $\theta$ 减小下移，逐个 morph 成准平坦 miniband + 费米速度消失，发生在魔角 $\theta_i$，最高 $\theta_1\approx1.05°$（$L_M\approx52a_0$）📜Q；简单图景止于 $\theta\sim0.35°$，其下 $U=0$ 谱复杂、态离域，仅剩一个 AA 局域态钉在 $\varepsilon\sim0.17\varepsilon_M$ 📜Q。**加偏压后谱简化**：AB/BA 区开隙、谷陈数反号，偏压高于阈值且角度足够小 → AB/BA 电子耗尽 → 态被强约束离开耗尽区，出现 sharp 局域共振谱 + 弱平滑背景（= 离域 TPH 网络态）📜Q（Fig. 2，$L_M=290a_0$、$\theta\approx0.2°$）。

### 2.3 推导层：网络形成判据 Eq. (1)（U↔TPH 关系）

**经验判据**（作者 "One can approximately quantify this condition"）——简化为突变 AB/BA 界面 + 均匀偏压，用两分量近似（$U<\gamma_\perp$ 有效），界面模 $\sim e^{-\lambda|x|}$ 衰减（$\lambda=\sqrt{U\gamma_\perp}/(2\hbar v_F)$，引 ref 12），要求界面模在 $R=L_M/(2\sqrt3)$ 内衰减 ≥95% → 判据：

$$z^2\left(\frac{l_\perp}{L_M(\theta)}\right)^2 < \frac{U}{\gamma_\perp} < 1,\qquad |\varepsilon|<\frac{|U|}{2}\quad(1)$$

其中 $z\equiv-4\sqrt3\ln0.05=20.76$、$l_\perp=\hbar v_F/\gamma_\perp\approx7.3a_0$ 📜Q。判据三要素：**小 $\theta$（大 $L_M$）+ 大 $U$ + $|\varepsilon|<|U|/2$** 📜Q。

> **Eq. (1) 推导链（逐层"输入→输出→公式+合法域"）**：
> 1. **模型化**：二维网络 → **一维突变 AB/BA 界面**（两侧谷陈数反号）+ **均匀偏压 $U$** 📜Q。
> 2. **两分量近似**：4×4 → 低能 2 分量子空间（合法域 $U<\gamma_\perp$）——即 ref 12（Martin 2008）把 BLG 约化到 $(A_1,B_2)$ 二次色散模型的同一约化 📜Q。
> 3. **界面模衰减**：$\sim e^{-\lambda|x|}$，$\lambda=\sqrt{U\gamma_\perp}/(2\hbar v_F)$，取自 ref 12 的 kink 零模衰减长度 $\xi\sim a/\sqrt{\varphi_0}$（$\varphi_0=Vt_\perp a^2/(2c^2)$；本文取 $\lambda$ 为其倒数并换成 $U,\gamma_\perp,v_F$ 符号）📜Q[推导]。
> 4. **95% 衰减判据**：$R=L_M/(2\sqrt3)$ 内衰减 ≥95% → $e^{-\lambda R}\le0.05$ → $\lambda R=-\ln0.05$ 📜Q。
> 5. **代入得 Eq. (1)**：$\lambda R=\dfrac{\sqrt{U\gamma_\perp}}{2\hbar v_F}\cdot\dfrac{L_M}{2\sqrt3}=-\ln0.05$，用 $l_\perp=\hbar v_F/\gamma_\perp$ 消去 $\hbar v_F$ 得 $\sqrt{U/\gamma_\perp}=z\,l_\perp/L_M$ → 下界；上界 $U/\gamma_\perp<1$ 即两分量近似合法域 📜Q[推导]。
> 6. **自洽核对（$\hbar$ 反推）**：原文 OCR 为 $\lambda=\sqrt{U\gamma_\perp}/(2v_F)$（无 $\hbar$），代入步骤 5 会差一个 $\hbar$ → **自洽形式必须含 $\hbar$**（同一页 $l_\perp=\hbar v_F/\gamma_\perp$ 的 $\hbar$ 却保留，属排版/提取问题，非作者约定）📜Q[推导]。

> **完整推导**（Schrieffer-Wolff 投影 + kink 零模精确解 $\lambda=\sqrt{U\gamma_\perp}/(2\hbar v_F)$ + Eq.(1) 全部代数，跨 T0/T01/T05 三篇）见 `note/shared/physics/11_bilayer_two_component_kink.md` `[PHY-2BAND]`。

- **阈值估算**（作者 "This analysis suggests ... for a realistic value of $U\sim90$ meV, the network requires $L_M\gtrsim290a_0$ ($\theta<0.2°$)"，即 Fig. 2 取值）📜Q；Fig. 2(a) 虚线框标出该角度下满足判据的 $(U,\varepsilon)$ 区，与螺旋网络区（sharp DOS 峰 + 弱平滑背景）**大致吻合** 📜Q（"roughly correlates"）。
- **与实验周期对标**：Alden 等已成像堆叠孤子、最大典型周期近 $1\,\mu$m 且可移动 📜Q；"用 $\sim100$ nm Moiré 周期（如该实验），我们**估算**阈值偏压 $\sim45$ meV" 📜Q（作者 "estimate"）。

### 2.4 边界层：谷守恒假设的失效与可编程性（"atomic defect" 段）

- **机制**：螺旋通道保护是**弱**保护，可被局域谷间散射破坏；空位/小吸附原子是高效谷散射体 📜Q。单个氢吸附原子可**完全阻断**一条网络链接 📜Q。
  - **为什么单个缺陷即可关断（机制链）**：螺旋模 = 谷-动量锁定（传播方向↔谷锁定，ref 15）📜Q → **背散射（动量反转）≡ 谷间散射**；保护成立的唯一前提是谷守恒——smooth 扰动（长波长）不混合谷 → 无耗散 📜Q（"as long as disorder does not mix valleys"），而原子尺度缺陷（空位/氢吸附原子）是高效谷散射体（尖锐势含大动量分量、足以桥接两谷动量差 $2|K|$ 💭I）→ 破坏谷-动量锁定 → 链接 1D 螺旋色散开隙 → 透射关断 📜Q。保护只是"弱"（$\mod2$ 缺省，无 mod 2 不变量兜底），故**单个**谷散射中心即可关断一条链接（对比 Z₂ 边态需磁性杂质/边-边耦合才能破坏）💭I。
- **TB 模拟验证**（Fig. 3）：在扭角双层完整晶格上做紧束缚模拟（连续模型谷守恒，不适合此类模拟）📜Q；每 Moiré 单胞同套缺陷，发现**任何带单个原子缺陷的链接在特定能窗内被高效阻断**（反向谷的子带交叉处，链接 1D 螺旋色散开隙）📜Q。
- **作者提出**（propose / could be used to）：可控沉积吸附原子可"at will"改写网络连通性 → 定制无耗散拓扑电路、拓扑纳米电子学 📜Q；前提是把不想要的吸附原子退火去除 📜Q。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

> 理论论文的结论必须按**性质**分层，而非平铺——"定理式主张"受假设限定、"估算"是经验判据、"预言"是待验证。每条标：**依赖假设** + **可检验性**。

### 3.1 定理式主张（数学/拓扑论证的产物，依赖 A1 谷守恒）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 谷 Chern 数 | $C_K=-C_{K'}\approx\text{sign}(U)$（$U<\gamma_\perp$）、$C_K^{AB}=-C_K^{BA}$ | A1（谷守恒） |
| TPH 模数 | 每谷每自旋 2 条；$N=|C_2-C_1|\mod2$，本文 $\mod2$ 缺省（$N=2$）→ "weak" 保护 | A1 |

⚠️ 本文**未**讨论量子化电导（如 $4e^2/h$）——网络的可测签名是 DOS 与 $\sigma_{xx}(\omega)$，不引入电导平台数字（防跨论文迁移）。

### 3.2 估算（经验/近似，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 网络形成判据 | Eq. (1)：$z^2(l_\perp/L_M)^2<U/\gamma_\perp<1$，$|\varepsilon|<|U|/2$ | A6（两分量）、A7（突变界面）、A8（95%） | 📜Q[~] |
| $U\sim90$ meV 所需周期 | $L_M\gtrsim290a_0$（$\theta<0.2°$） | 同上 | 📜Q[~] |
| 100 nm 周期阈值偏压 | $\sim45$ meV | 同上（对标 Alden 周期） | 📜Q[~]（"we estimate"） |
| 魔角 $\theta_1$ | $\approx1.05°$（$L_M\approx52a_0$） | 低能连续（A5） | 📜Q[~] |
| 大角度定量 | $\varepsilon_{vH}\approx\varepsilon_M(1-2\alpha)$、$v_F^*\approx v_F(1-9\alpha^2)$、峰位 $\sim0.6\varepsilon_M$ | 微扰论 $\alpha\ll1$ | 📜Q[~] |

### 3.3 预言（可检验性 → 见 §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 偏压下畴壁螺旋模构成连通网络（Chalker-Coddington 型） | "We show / we find"（数学构造）📜Q | 中——空间密度图案 + DOS |
| 可控沉积吸附原子改写连通性 → 定制拓扑电路 | "propose / could be used to / open the possibility" 📜Q | 中——后续实验（缺陷工程） |
| 理想平台（"we believe ... ideal platform"） | 谨慎表态 📜Q | 弱——定性判断 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

理论论文没有数据可辨识性，但有**一致性核对**，本文两处：

1. **解析↔数值互验**：Eq. (1) 阈值线（Fig. 2(a) 虚线）与 DOS 谱 sharp 峰→平滑背景的"螺旋网络区"**大致吻合**（作者 "roughly correlates"）📜Q——判据与对角化结果自洽。
2. **极限对照（负对照）**：$\theta=4°$ 大角度算例——同一旋钮 $U$ 下仅平移 Dirac 锥、无网络 📜Q，验证"网络是小角度特有"（类比实验论文的负对照）。
3. **量级核对**：界面模衰减 $\lambda$ 与 ref 12 Martin 2008 的 kink 零模衰减长度 $\xi\sim a/\sqrt{\varphi_0}$ 量级一致（因子 $\sqrt2$ 属 "of the order of"）📜Q[推导]。

### 3.5 概念区分（作者论证中的"分类"，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| 螺旋 vs 手征 | 有/无时间反演不变性（ref 4）📜Q；本文体系 TRS 保持 | 本文是螺旋（谷-动量锁定，ref 15） |
| 弱保护 vs 强保护 | $\mod2$ 缺省（$N=2$）因仅考虑谷守恒扰动 📜Q | 本文是弱（谷保护）保护 |
| 平台 TBG vs h-BN | h-BN 晶格失配无法任意增大 Moiré 周期 📜Q | 扭角双层（可调 $\theta$）作平台 |
| 网络态 vs 局域共振态 | 偏共振能区 DOS 弱且无特征 vs 共振处 sharp 峰（Fig. 2）📜Q | 两者**并存**：离域网络 + 局域共振 |

> 注：这些是**概念/图景分类**（taxonomy），不是实验论文那种"数据排除竞争解释"（溯因排除）——理论论文没有后者。

---

## 4. 假设-结论依赖图（含金量所在）

> 理论论文三个月后最可能被引用的是"何时失效"，不是推导本身。本表把 §1.3 的每条假设映射到"失效方式 → 崩塌的结论 → 是否致命"。

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A1 谷守恒 | 原子尺度缺陷/谷间散射 | $C_K$ 量子化、TPH 无耗散 | **弱保护** → 单链接可关断；作者反用为"开关"特性 📜Q |
| A3 完美周期（无弛豫） | 弹性畸变 / 原子重构 | 网络几何、Eq. (1) 判据 | smooth 畸变**不致命反而增强**（扩大耗尽区）📜Q；原子重构（AA 收缩/AB 扩大锐化）**未建模**（全文 grep `relax/reconstruct` 零命中），属后续文献 💭I |
| A6 两分量近似 | $U\ge\gamma_\perp$ | Eq. (1) 下界失效 | Eq. (1) 上界 $U/\gamma_\perp<1$ 就是合法域 📜Q |
| A4 单粒子 | 魔角平带关联态 | 网络图景 | 未处理（$\theta_1\approx1.05°$ 处平带）💭I |
| A1（连续模型谷守恒） | 吸附原子处局域电子结构 | 连续模型本身 | 作者换 TB 模拟补盲 📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- DOS 谱：弱平滑背景（= 离域网络）+ sharp 峰（= 局域共振）📜Q；
- 光学电导 $\sigma_{xx}(\omega)$（Kubo，细节见 SI）📜Q；
- 空间概率密度图案：Fig. 2 三角网络 + 白箭头（谷电流方向）📜Q。
- 后续实验（Huang 2018 STM 双线、Rickhaus 2018 输运）按此靶标解读（§7）。

### 5.2 设计原则（"可编程拓扑电路"三要素）

$\theta$ 设连通几何 + $U$ 开隙/耗尽 + 吸附原子作开关 💭I（本文 "propose / could be used to"）。

### 5.3 后续文献修正（时间倒挂，💭I）

- **Efimkin & MacDonald 2018（T9）**：本文网络范式的系统化/严格化（$S$ 矩阵）。
- **Tsim 2020（T12, TZM）**：推翻"连通网络"——AA 节点确定性散射、不渗流；**部分修正本文网络图景**。
- **Hou 2024（T29, NQCP）**：裁决为独立 1D 通道 + 近量子化平台。
- **De Beule 2020（T15）**：散射统一（$\phi=0$=TZM / $\phi=\pi/2$=pLL 两极限）。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 弱拓扑保护 | 谷守恒破坏即失效——原子尺度缺陷/强谷间散射敏感 | 📜Q（"weak" protection） |
| 理想周期 Moiré（无弛豫） | 弛豫/原子重构未建模（grep `relax/reconstruct` 零命中）；smooth 畸变仅定性论证不破坏 | 📜Q（"perfectly periodic model"）+ 💭I |
| 连续模型盲区 | 谷守恒构造，无法描述吸附原子处局域电子结构（故用 TB） | 📜Q |
| 设计原则而非定量预言 | 网络导电性/电路性能未定量；σxx(ω) 细节在 SI 未展开 | 📜Q→💭I |
| 未处理多体/魔角 | 魔角 $\theta_1\approx1.05°$ 处平带（关联态）未纳入 | 💭I（原文未讨论关联） |

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）

| 工作 | 关系 |
|------|------|
| Alden et al. 2013, PNAS 110, 11256 (ref 6) | **直接引用**——堆叠孤子实验成像（最大周期近 1 μm、可移动），本文以此为实验动机与周期对标 📜Q |
| Martin 2008 (ref 12) / Nunez 2011 (ref 13) / Qiao 2011 (ref 14) | 引用——偏压反号界面的畴壁 TPH 先驱（"每谷每自旋 2 模"，refs 12–15；ref 15 为 helical 定义脚注）📜Q |
| Wright & Hyart 2011 (ref 17) / Vaezi 2013 (ref 18) / Zhang 2013 (ref 19) | 引用——AB→BA 平滑过渡（"applying a different strain to each layer"，ref 18）与谷陈数拓扑荷分类（refs 19,39）；本文的"网络"是这些孤立畴壁的推广 📜Q |
| Chalker & Coddington 1988 (ref 21) | 引用——网络模型的类比来源 📜Q |
| Tudorovskiy & Katsnelson 2012 (ref 20) | 引用——zero mass lines / 谷电流涡旋 📜Q |
| h-BN 上石墨烯 (refs 27–30) | 引用——机制也出现但晶格失配限制 Moiré 周期，网络不能完全发展 📜Q |

> ⚠️ Phase S 外部对标（**非本文引用**，时间倒挂，💭I）见 §5.3；引用关系依据 `cards.md` Q2 卡片与 `appendix_B_theory.md` §B.2。

## 8. 对后续研究的影响

- 把畴壁物理从"孤立 1D 边缘态"推进到"**连通 2D 网络**"范式——"网络"成为 mTBG 畴壁物理的核心语言 📜Q。
- 提出"可编程拓扑电路"三要素（$\theta$ 设几何 + $U$ 开隙/耗尽 + 吸附原子开关）💭I（本文 "propose / could be used to"）。
- 可测签名（DOS 峰 + $\sigma_{xx}(\omega)$）为后续 STM/输运实验提供理论靶标 📜Q。
- 留下"连通性是否成立"的核心张力——被 TZM (T12) 挑战、被 NQCP (T29) 裁决为"独立通道 + 近量子化"（§5.3）💭I。

## 9. 理论模型映射（供 TBPM / Kubo 计算对标）

| 映射 | 说明 |
|------|------|
| $\theta\to L_M\to A$ | 扭角→Moiré 周期 $L_M=a_0/[2\sin(\theta/2)]$→三角畴面积 $A=\frac{\sqrt3}{4}L_M^2$（超晶格单胞一半）📜Q→💭I |
| $U\to\delta$ | 均匀偏压→AB/BA 区局域能隙（耗尽条件），能窗 $|\varepsilon|<|U|/2$ 📜Q |
| Eq. (1) → 相图 | $z^2(l_\perp/L_M)^2<U/\gamma_\perp<1$ 给出 TBPM/Kubo 可扫的 $(\theta,U)$ 网络相图边界 📜Q |
| 通道数 $N=2$/谷/自旋 → 电导 | 若做 Landauer/Fisher-Lee 透射计算，通道数决定弹道电导上限（本文**未**算量子化电导，属计算扩展）💭I（[PHY-LB]） |
| DOS 峰 + 网络态空间图案 | 本文可算量；对应 TBPM 的 LDOS/DoS 与 Kubo 的 $\sigma_{xx}(\omega)$ 📜Q |

> 与 TBPM/Kubo 对应：本文连续模型 + TB 是 TBPM/Kubo 的直接上游（同一 $V(r)=\tfrac13\gamma_\perp\sum e^{ig_i\cdot r}$ 层间耦合）；复现"网络 vs 局域共振"需同时算 DOS 与空间 LDOS 图案，纯体 $\sigma_{xx}$ 只给背景 💭I。

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：本文给出**理论预言**的表征靶标——DOS 谱（弱平滑背景 = 离域网络 + sharp 峰 = 局域共振）、$\sigma_{xx}(\omega)$、空间密度图案（Fig. 2 三角网络白箭头 = 谷电流）📜Q；后续实验（Huang 2018、Rickhaus 2018）按此靶标解读（§7）。
- **Q2（理论如何解释）**：螺旋网络奠基——偏压下 AB/BA 谷陈数反号 + 耗尽 → 畴壁每谷每自旋 2 条螺旋模 → 连通网络；判据 Eq. (1) 定量化（小 θ + 大 U + $|\varepsilon|<|U|/2$）📜Q。⚠️ 连通性后被 TZM 部分修正（§5.3）。
- **Q3（理论↔实验对应）**：$\theta\to L_M$ ↔ 实验周期；$U$ ↔ 阈值偏压（100 nm ↔ ~45 meV）↔ Alden 周期；吸附原子开关 ↔ 可编程器件蓝图；DOS/σxx ↔ 谱学可观测量 📜Q。

> **增量价值**：与 T9（Efimkin 系统理论）分工——本文是**概念奠基 + 经验判据 Eq. (1) + 可编程性预言**，T9 是 $S$ 矩阵严格化；report/appendix_B 用本文 $\varepsilon_M\approx88$ meV·θ(deg)、$L_M=290a_0$、100 nm↔45 meV 三处数字（均 📜Q，已核对）。比 T9 多的 = 网络形成判据与可编程开关概念；少的 = 无 $S$ 矩阵/网络能带定量。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取正文到 `/tmp/T05.txt`，逐项 grep 核对：**全部数字命中原文**——

| 数字 | grep 命中位置 | 结论 |
|------|--------------|------|
| 88 meV·θ(deg) | "≈ 88 meV × θ (deg) for small angles"（Continuum theory 节）| ✓ 📜Q[~] |
| L_M = a0/[2sin(θ/2)]、a0=2.46 Å | Continuum theory 节 | ✓ |
| L_M = 290a0（θ≈0.2°）| Fig. 2 caption | ✓ |
| U∼90 meV → L_M≳290a0（θ<0.2°）| 正文 "for a realistic value of U∼90 meV" | ✓ |
| 100 nm → ∼45 meV | 正文 "we estimate a threshold interlayer bias of ∼45 meV" | ✓ |
| γ⊥≈0.33 eV、l⊥≈7.3a0、z=20.76 | Continuum theory 节 / Eq. (1) 附近 | ✓ |
| θ1≈1.05°、L_M≈52a0、θ∼0.35°、0.17ε_M | Continuum theory 节 | ✓ |
| θ=4°、L_M≈14.3a0 | Fig. 1 caption | ✓ |
| 250 meV（Bernal 开隙，背景）| 引言 | ✓ |
| 近 1 μm（Alden 孤子）| conclusion 段 | ✓ |
| C_K=−C_K′≈sign(U)、C_K^AB=−C_K^BA、N=2 mod2 缺省 | Band topology 节 | ✓ |
| 每谷每自旋 2 条 TPH、单氢吸附原子阻断链接 | Band topology 节 / Fig. 3 段 | ✓ |

⚠️ 修正/降级：① 界面模 $\lambda=\sqrt{U\gamma_\perp}/(2\hbar v_F)$——原文 OCR 为 $\sqrt{U\gamma_\perp}/(2v_F)$ 无 $\hbar$ 且根号位移，由 Eq. (1) 的 $z^2$ 因子与 $\lambda R=-\ln0.05$ 反推自洽确认须含 $\hbar$。② arXiv 号 1304.5344 正文未出现 → 头部表已标"外部来源"。③ 未引入 $4e^2/h$（本文未出现该量）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-19 | （appendix_B §B.5 #10）T5 数字核对通过：$E_M\approx88$ meV·θ(deg) ✓、100 nm 周期阈值 ≈45 meV ✓、$L_M=290a_0$（θ≈0.2°）✓（均 📜Q）。旧 review 无独立更正日志，本条为历史基线。 |
| 2026-09-02 | **按 4 块辨识结构整体重写**：旧 5 节叙事 → 4 块架构（TL;DR + 四层变量表 + 判别表置顶 + 数据/提取链）。 |
| 2026-09-02 | **新增/修正**：① 补判据 Eq. (1) 完整式；② 精确化界面模衰减 $\lambda$（引 ref 12）；③ 补大角度定量（$\varepsilon_{vH}\approx\varepsilon_M(1-2\alpha)$ 等）；④ 判据表 + [前提与限定] 块（M 边界声明）；⑤ arXiv 号标外部来源；⑥ 全文统一 📜Q[~] 标注。 |
| 2026-09-02 | **降级/删除**：① 未发现无源/过强论断；② 未引入 $4e^2/h$；③ 跨论文对标移出正文并标 💭I 时间倒挂。 |
| 2026-09-08 | **S-Q2-T5 执行**（阅读复盘见 `note/shared/method/theory_paper_reading_case_T05.md`）：22 项数字/公式重 grep 全命中；补 $\alpha(\theta)=\gamma_\perp/[6\varepsilon_M(\theta)]$（OCR 分数破碎 "16 γ⊥"，-raw 复核）、$\sim0.6\varepsilon_M$、$L_M$ 适用域 $\theta<30°$、§7 引文分组订正。 |
| 2026-09-08 | **§3.1 展开为显式矩阵 + 变量表**（应用户要求整理 Continuum theory 模型）；**Eq. (1) 推导链 + λ 的 $\hbar$ 修正**（追溯 ref 12 Martin 2008：4-band → $(A_1,B_2)$ 二次色散 → 准经典 $H_{qc}$ → step-kink 衰减 $\xi\sim a/\sqrt{\varphi_0}$）。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求；方法论 §4.0 定位：理论论文是"白箱演绎"非"黑箱溯因"）。旧 4 块版归档 `archive/paper_review_T05_sanjose2013_prb.backup_20260908.md`。四层变量表 → 参数分册（删反推量层）；判别表 → 拆为"内部验证（§3.4）+ 概念区分（§3.5）"；[前提与限定] → 显式假设清单（§1.3）+ 假设-结论依赖图（§4）；新增 §5 接口。全部 📜Q 事实与数字无丢失。 |
