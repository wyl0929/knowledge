<!--
 * @Author       : AI 精读 (paper-reading skill)
 * @Date         : 2026-08-11（初读）→ 2026-08-20（S-REV 机制重写）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T25_wittig2023_prb.md
 * @Description  : T25: Wittig, Dominguez, De Beule & Recher 2023 — mTBG 中局域态与手征网络耦合（2026-09-08 按 5 块演绎结构重写）
-->

# Paper Review: Wittig, Dominguez, De Beule & Recher (2023) — 局域态耦合到手征模网络

| 字段 | 内容 |
|------|------|
| **编号** | T25 |
| **标题** | Localized states coupled to a network of chiral modes in minimally twisted bilayer graphene |
| **作者** | P. Wittig, F. Dominguez, C. De Beule, P. Recher |
| **期刊** | Physical Review B 108, 085431 (2023) |
| **DOI / arXiv** | 10.1103/PhysRevB.108.085431 / 2303.03901（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 理论 — 局域态 + 手征网络耦合（唯象散射网络模型 + 广义 Weidenmüller 公式，无实验数据） |
| **课题组** | Wittig/Dominguez/Recher (TU Braunschweig)、De Beule (U. Luxembourg / U. Pennsylvania) |
| **PDF / SI** | ✅ `reference/pdfs/Wittig 等 - 2023 - Localized states coupled to a network of chiral modes in minimally twisted bilayer graphene.pdf`（正文 14 页 + Appendix A–C：自洽计算、R/S_D 形式、输运细节） |
| **精读日期** | 2026-08-11（初读）→ 2026-08-20（机制修正）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」五块记。本文是**唯象散射白箱**——研究对象是作者按 $C_3$、$C_2T$ 对称性构造的能量依赖 $S$ 矩阵（含 AA 区域离散能级），结论是"共振附近电导 dip/峰、磁导周期、退相干"这类模型预言。

---

## TL;DR

**本文想解决的理论问题**：mTBG 偏压下手征网络模型与微观计算之间存在一个未补的差距——微观谱在能隙中间出现**局域于 AA 区域的平带**（局域态密度），而既有唯象（能量无关）散射模型没有这些平带。能否把这些局域态纳入唯象 $S$ 矩阵，并算出它们对能谱与磁电导的影响？

**主结果**：① 给 AA 区域加一组**离散能级**（$N$ 个，隧穿幅度 $t_{ij}$），经广义 Weidenmüller 公式（Eq. 6）得到**能量依赖的 $S$ 矩阵**；② 共振附近离散能级与手征 ZZ 模（$\varphi\approx0$）或平带（$\varphi\approx\pi/2$）杂化，产生能谱反交叉、电导 **dip**（$\varphi\approx0$）或 **peak**（$\varphi\approx\pi/2$）📜Q；③ 磁电导周期在共振附近变为 $\Phi/\Phi_0=2$（可绕半个单胞），远离共振为 $\Phi/\Phi_0=1$；弹性 cotunneling 标记路径 → "which path"退相干 → 抑制 AB 共振 📜Q。

**结论/意义**：把"局域态 + 手征网络"耦合纳入统一唯象框架，修正了"网络态全是传播模"的简化图景 📜Q。⚠️ 全文是模型预言（"we model / we have found / we expect"），非实验证实。

---

## 1. 模型白箱（能量依赖 $S$ 矩阵 + 假设清单）

### 1.1 哈密顿量（单 AA 区域）

- **离散能级**（Eq. 3，含平均场库仑）：$H_D=\sum_{j=1}^N\varepsilon_j d_j^\dagger d_j+\tfrac{U}{2}\sum_{j,j'}^{j\ne j'}n_j n_{j'}\approx\sum_j\varepsilon_j d_j^\dagger d_j+\tfrac{U}{2}\sum_{j,j'}^{j\ne j'}(\langle n_j\rangle n_{j'}+\langle n_{j'}\rangle n_j)$ 📜Q（$U$=库仑排斥能，平均场近似，占据数涨落小时成立）。
- **隧穿**（Eq. 4）：$H_T=\sum_{i=1}^6\sum_{j=1}^N t_{ij}d_j^\dagger\hat\psi_i(x_{AA})+\text{H.c.}$；$C_3$ 给 $t_{1j}=t_{3j}=t_{5j}$、$t_{2j}=t_{4j}=t_{6j}$；$C_2T$ 给 $t_{1j},t_{2j}$ 实 📜Q。
- **动能**（Eq. 5）：$H_0=\sum_i\int dx_i\,\hat\psi_i^\dagger(-i\hbar v_i)\partial_{x_i}\hat\psi_i$，$|v_i|=v_F$ 📜Q。
- **简化**：取二重简并能级 $N=2$（$\varepsilon_1=\varepsilon_2\equiv\varepsilon$，最近非简并能级间距为最大能标），且每个手征模以相同幅度 $t_D:=t_{i1}=t_{i2}$ 耦合所有离散态 📜Q。

**对称性约束的 $S$ 矩阵**（Eq. 1–2）：$C_3$：$S_K=\begin{pmatrix}s_f&s_l&s_r\\s_r&s_f&s_l\\s_l&s_r&s_f\end{pmatrix}$；$C_2T$：$s_r=(s_l)^t$，$s_f=(s_f)^t$ 📜Q。对谷 $S_{K'}=(S_K)^t$（时间反演）📜Q。

**广义 Weidenmüller 公式**（Eq. 6）：$S(E)=S_0-i\pi\nu(1+i\pi\nu R)W[E-h_D+i\pi\nu W(1+i\pi\nu R)^{-1}W^\dagger]^{-1}W(1+S_0)$，$\nu=1/\pi\hbar v_F$、$R$ 为 $S_0=(1+i\pi\nu R)^{-1}(1-i\pi\nu R)$（Eq. 7）的分解；无偏转时退化为 Mahaux-Weidenmüller 公式 $S_D=1-2i\pi\nu W^\dagger[E-h_D+i\pi\nu WW^\dagger]^{-1}W$（Eq. 8）📜Q。

**偏转过程 $S_0$**（Eq. 9–10，引 refs 32,35）：$s_f$（前向）、$s_r/s_l$（偏转），参数 $P_{f1},P_{f2}$（前向）、$P_{d1},P_{d2}$（偏转）概率 + 相位 $\varphi$；幺正条件 $2(P_{d1}+P_{d2})+P_{f1}+P_{f2}=1$。$\varphi$ 调谐网络从退耦合 ZZ 手征模（$\varphi=0$）到绕 AB/BA 区闭合轨道的平带（$\varphi=\pi/2$）📜Q。本文只考虑偏转：$s_f=0$、$P_{d1}=P_{d2}$（$\chi=\pi/2$）📜Q。

### 1.2 参数分册

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $\varphi$（相位，= 动量差 $\delta q$ 或 AA 散射相位）、$t_D$（隧穿，无量纲 $\tau=t_D\sqrt{l/\hbar v_F}$）、$U$（库仑，取 $U=3.25\hbar v_F/l$）、$\varepsilon$（取 $\varepsilon=\hbar v_F/l$）、$E_F$（费米能，扫谱）、磁场 $B$（$\Phi$） |
| **导出量** | moiré 晶格常数 $l=a/[2\sin(\theta/2)]\approx14(\theta^\circ)^{-1}\,\text{nm}$、能标 $E_l=\hbar v_F/l$、温度标 $T_l=\hbar v_F/(k_B l)$、$\nu=1/\pi\hbar v_F$ |
| **模型内部量（解的性质）** | 网络能带、电导 $G$、磁电导周期、退相干强度 |
| **固定常数** | $G_0=4e^2/h$、$\Phi_0=e/h$（原文写法，磁通量子）、$v_F$（石墨烯费米速度）、$a$（晶格常数，未给数值） |
| **预言量（可检验）** | 共振附近电导 dip/peak、磁电导周期 $\Phi/\Phi_0=1$ vs $2$、AB 共振抑制 |

> 无"反推量"层。**符号防混**：$\varepsilon$（离散能级能量）≠ $\epsilon$（应变，本文无）；$\varphi$（散射相位）≠ 方位角；$U$（库仑）≠ 偏压（本文用"interlayer bias"开隙，无 $U$ 偏压符号）。

### 1.3 显式假设清单

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **唯象散射模型**（$C_3$、$C_2T$ 对称性） | 模型 | 📜Q |
| A2 | **每谷每自旋 2 条手征模**（谷 Chern 数差 $\pm2$，光滑无序无谷间耦合） | 模型前提 | 📜Q |
| A3 | **无自旋相关耦合**（石墨烯 SOC 可忽略）→ 无自旋哈密顿量 | 模型 | 📜Q |
| A4 | **平均场库仑**（占据数涨落小；谷间散射可忽略，只改 $U$） | 推导 | 📜Q |
| A5 | **$N=2$ 二重简并能级 + 单隧穿幅 $t_D$**（最近非简并能级间距最大） | 简化 | 📜Q |
| A6 | **离散能级与外界引线平衡**（设费米能 $E_F$；自洽算 $\langle n_i\rangle$） | 推导 | 📜Q |
| A7 | **纯偏转 $S_0$**（$s_f=0$、$P_{d1}=P_{d2}$） | 简化 | 📜Q |

> 判别性扫轴：$\varphi$（$0\to\pi/2$）、$E_F$（扫谱）、$\tau$（$0,0.1,0.2$）、$\Phi/\Phi_0$（磁通）、温度 $T/T_l$ 📜Q。

---

## 2. 推导链（顺论文顺序）

### 2.0 总览

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 模型层 | Model & Hamiltonian (Sec. II) | 对称性 $C_3,C_2T$ | $S$ 矩阵约束（Eq. 1–2）、$H_D,H_T,H_0$（Eq. 3–5） | A1–A3 | 单谷自旋 |
| 推导层 | Generalized S matrix (Sec. III) | $S_0$ + 离散能级 | 能量依赖 $S(E)$（Eq. 6） | 广义 Weidenmüller | A4–A7 |
| 推导层 | Network energy bands (Sec. IV) | Bloch 定理 | 能谱方程（Eq. 18–19）、$\varphi=\delta ql/2$ | 平移不变 | — |
| 推导层 | Magnetoconductance (Sec. V) | Landauer-Büttiker | $G$（Eq. 23）、dip/peak、周期 | A4 | 宽条带 |
| 边界层 | Decoherence (Sec. V 末) | cotunneling | "which path"退相干（Eq. 26） | 概率干涉 | — |

### 2.1 模型层：对称性 + 哈密顿量

- **输入**：$C_3$、$C_2T$ 对称性 + 手征模。
- **输出**：$S$ 矩阵约束（Eq. 1–2）、$H_D$（Eq. 3）、$H_T$（Eq. 4）、$H_0$（Eq. 5）📜Q。
- **动机**：AA 区域尺寸小（$\sim10$ nm，ref 37）→ 库仑相互作用重要 → 可能库仑阻塞 📜Q。

### 2.2 推导层：能量依赖 $S$ 矩阵

- **输入**：$S_0$（偏转）+ $W$（隧穿耦合）+ $h_D$（Eq. 11：$h_D=\begin{pmatrix}\varepsilon_1+U\langle n_2\rangle&0\\0&\varepsilon_2+U\langle n_1\rangle\end{pmatrix}$）。
- **输出**：广义 Weidenmüller 公式 $S(E)$（Eq. 6）📜Q。无偏转（$R=0$）退化为 Mahaux-Weidenmüller（Eq. 8）📜Q。
- **单隧穿幅极限**：$S_D$ 可写为"三条自由手征模 + 单通道 Efimkin-MacDonald 模型" 📜Q。
- **能量依赖来源**：离散能级位置 $\varepsilon$ 与传播模能量之差 → $S$ 依赖 $E$（对比旧模型能量无关）📜Q。

### 2.3 推导层：网络能带

- **Bloch 定理**：节点在 $m\,l_1+n\,l_2$（$l_{1,2}=l(-1/2,\pm\sqrt3/2)$），散射振幅关系（Eq. 14–17），代入得能谱方程 $[M(k)\otimes1_2]S(E)a_k=e^{-iEl/\hbar v_F}a_k$（Eq. 18）📜Q。
- **$t_D\to0$ 极限**：$S$ 与 $E$ 无关，谱由 $i\log(\xi_j)$ 给，能量周期 $2\pi\hbar v_F/l$ 📜Q；$t_D\ne0$ 时谱高度非线性（Eq. 19），仅在远离共振处恢复周期性 📜Q。
- **$\varphi$ 与 $\delta q$ 等价**：动量差 $\delta q$ 通过 $Z=\exp[i(\delta ql/2)1_3\otimes\sigma_z]$ 进入，$ZS_0(\varphi_0)=MS_0(\varphi_0+\varphi)M^\dagger$ 证明 $\varphi=\delta ql/2$ 📜Q——**两个微观起源**：沿链接累积的动量差 或 AA 区散射相位 📜Q。
- **实验对标**：Ref. [33] 电场开隙 $\sim50$ meV、层间耦合 $\approx0.39$ eV → $\delta q\approx0.17\,\text{nm}^{-1}$；扭角给 $l\approx140$ nm → $\varphi'=\delta ql/2\approx3.89\pi$、$\varphi=4\pi-\varphi'\approx0.34$ → 手征 ZZ 区（弱耦合）📜Q。

### 2.4 推导层：磁电导

- **Landauer-Büttiker**：$G=\tfrac{4e^2}{h}\tfrac{W}{\sqrt3 l}\int dE\,T(E)(-\tfrac{\partial f_0}{\partial E})$（Eq. 23，因子 4 = 自旋×谷）；零温 $G/G_0=\tfrac{W}{\sqrt3 l}T(E_F)$（Eq. 25，$G_0=4e^2/h$）📜Q。Peierls 相位 $\Phi_P=\tfrac{\pi\Phi}{\Phi_0}\tfrac{x}{l/2}+\tfrac12$（Eq. 22，Landau 规范 $A=Bxe_y$，单胞面积 $A=(\sqrt3/2)l^2$）📜Q。
- **$\tau=0$ 复现旧模型**：$\varphi\approx0$ 金属、三族 ZZ 手征模，$\sqrt3 G l/G_0 W=2$；$\varphi=\pi/2$ 电导为零（闭合轨道）📜Q。
- **$\tau\ne0$**：共振附近（$|E_F-\varepsilon|\lesssim|\tau|^2E_l$ 或 $|E_F-\varepsilon-U|$）电导 **dip**（$\varphi\approx0$），**dip 宽度 $\propto|\tau|^2\hbar v_F/l$**（小耦合）📜Q；$\varepsilon+U$ 处 dip 更宽、共振处出 peak 📜Q。
- **磁电导周期**：只耦合平行 ZZ 手征模时 $\Phi/\Phi_0=1$（可绕最小面积 $A$）；所有耦合开放时 $\Phi/\Phi_0=2$（绕半个单胞 $A/2$）📜Q。共振附近 $\Phi/\Phi_0=2$、远离共振 $\Phi\approx\Phi_0$；高温下 $\Phi/\Phi_0=1$ 恢复更快（远离共振）而共振处保持 $\Phi/\Phi_0=2$ 📜Q。Hofstadter 图案（分形）📜Q。

### 2.5 边界层：退相干（cotunneling）

- 最小网络（4 个 AA 区、单胞两条路径），总概率 $P=\sum_j(P_1^j+P_2^j+2\mathrm{Re}\sqrt{P_1^jP_2^j}\langle\chi_1^j|\chi_2^j\rangle e^{-i\Phi/\Phi_0})$（Eq. 26）📜Q。离散能级占据变化 = "标记路径"；弹性标记（$N_p=16$，仅 4 个不标记）抑制 AB 共振 📜Q；非弹性标记受偏压（限于隙内）约束可忽略 📜Q。

---

## 3. 结论清单（分层）

### 3.1 定理式主张（模型/公式产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| $S$ 矩阵约束 | $C_3$（Eq. 1）、$C_2T$（Eq. 2）形式 | A1 |
| 能量依赖 $S$ | 广义 Weidenmüller 公式（Eq. 6） | A4–A7 |
| $\varphi=\delta ql/2$ 等价 | $ZS_0(\varphi_0)=MS_0(\varphi_0+\varphi)M^\dagger$ | A1 |
| 磁电导周期 | 共振附近 $\Phi/\Phi_0=2$、远离 $\Phi/\Phi_0=1$ | A2（ZZ 模） |

### 3.2 估算

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| dip 宽度 | $\propto|\tau|^2\hbar v_F/l$（小耦合） | A4 | 📜Q[~] |
| 实验相位 | $\varphi\approx0.34$（$l\approx140$ nm、$\delta q\approx0.17\,\text{nm}^{-1}$、$\varphi'=3.89\pi$） | Ref. 33 参数 | 📜Q[~] |
| AA 尺寸 | $\sim10$ nm（ref 37） | — | 📜Q[~] |
| 参数值 | $\varepsilon=E_l$、$U=3.25E_l$、$\varepsilon+U=4.25E_l$、$P_{d1}=P_{d2}=1/4$ | 计算取值 | 📜Q[~] |

### 3.3 预言（待实验验证）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 共振附近电导 dip（$\varphi\approx0$）/ peak（$\varphi\approx\pi/2$） | "we have found" 📜Q | 中——两终端磁输运 |
| 磁电导周期 $\Phi/\Phi_0=2$ 揭示局域态 | "contains information" 📜Q | 中——AB 振荡 |
| 弹性 cotunneling 抑制 AB 共振 | "can give rise to … suppressing" 📜Q | 弱——需区分退相干来源 |

### 3.4 内部验证 + "没写什么"

1. **极限对照**：$\tau=0$ 复现旧唯象模型（refs 32,35）📜Q；$t_D\to0$ 恢复能量无关 $S$ 与周期谱 📜Q。
2. **⚠️ 未用"Fano"术语**（grep `Fano`=0）；未给 Fano 线形公式；未讨论量子化电导平台（本文是唯象散射网络，非量子化输运）。

---

## 4. 假设-结论依赖图

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性 |
|---|---|---|---|
| A4 平均场库仑 | 占据数涨落大 / 谷间库仑 | $h_D$ 形式、能量依赖 $S$ 的定量 | 部分——作者指出谷间只改 $U$ |
| A5 $N=2$ + 单隧穿幅 | 真实 AA 更多能级/非均匀耦合 | 具体 dip/峰结构 | 部分——"extension to arbitrary N is straightforward" 📜Q |
| A2 谷守恒 | 谷间散射 | 2 手征模/谷前提失效 | 基础（继承自 San-Jose 图景） |
| A7 纯偏转 | 前向散射 $P_f\ne0$ | $S_0$ 参数化改变 | 简化——本文固定 |
| 单层网络 | 多层畴壁 | 真实 mTBG 修正 | 局限（见 §6） |

---

## 5. 接口（可检验性 / 设计原则 / 后续文献修正）

### 5.1 可检验性

共振附近电导 dip/peak、磁电导周期 $\Phi/\Phi_0=1$↔$2$、AB 共振的退相干抑制、Hofstadter 图案（实验可及磁场）📜Q。

### 5.2 设计原则

用 $\varphi$ 调网络拓扑（ZZ 手征模 ↔ 平带闭合轨道）+ $t_D$ 调局域态耦合 + $U$ 开库仑隙 📜Q（作者 "This parameter tunes the network"）。

### 5.3 后续文献修正（时间倒挂，💭I）

- **T30 Wittig 2024（同组）**：把同一唯象散射方法推广到 Kagome 网络 + Rashba SOC——本文是三角网络的前一环节 💭I。
- ⚠️ 旧 review "解释 E14 Kagome 中心态"为 review 层综合（原文未引 Zheng 2022 / E14），已移出正文（见 §3.4）。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 平均场库仑 | 无法捕捉 cotunneling 改占据数的全部效应 | 📜Q（作者自陈） |
| 无多体（充电能） | 离散能级充电能未超平均场 | 💭I（旧 review 点，原文未定量） |
| 单层网络 | 真实 mTBG 多层畴壁 | 📜Q（引言"single AA region"框架） |
| 有限温展宽未定量 | dip 温度展宽定性讨论 | 📜Q |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| San-Jose & Prada 2013 (ref 19) / Efimkin & MacDonald 2018 (ref 34) / De Beule 2020-2021 (refs 32,35) | 直接继承——唯象散射网络模型与 $S_0$ 参数化 📜Q |
| Tsim 2020 / Hou 2020 (refs 31,32) | 引用——ZZ 手征模（"not forming percolating network"）📜Q |
| 微观计算 (refs 19,37,48) | 引用——AA 局域平带（本文要补的差距）📜Q |
| Ref. 33（Rickhaus 实验） | 引用——$\varphi$ 估算的输入（50 meV gap、0.39 eV 耦合）📜Q |

## 8. 对后续研究的影响

- 把"局域态"作为网络模型的**一等公民**纳入（离散能级 + 能量依赖 $S$ 矩阵），修正"全传播模"图景 📜Q。
- 提供"磁电导周期 $1\to2$"作为局域态耦合的诊断探针 📜Q。
- 为同组 T30（SOC + Kagome）奠定方法基础 💭I。

## 9. 理论模型映射（供计算对标）

| 映射 | 说明 |
|------|------|
| $l\approx14(\theta^\circ)^{-1}$ nm | 扭角→moiré 常数→能标 $E_l=\hbar v_F/l$，TBPM 可复用 |
| $S(E)$（Eq. 6） | 能量依赖散射矩阵 → 可数值递归算 $G$（本文方法） |
| 共振条件 $|E_F-\varepsilon|\lesssim|\tau|^2E_l$ | dip/peak 出现的能量窗 |
| 磁电导周期 | $\Phi/\Phi_0=1$（常规）vs $2$（共振）→ TBPM 磁输运对标 |

## Phase S 目的接口（引用式）

- **Q1（edge state 如何表征）**：本文给**输运特征**——共振附近电导 dip（$\varphi\approx0$）/ peak（$\varphi\approx\pi/2$）、磁电导周期 $\Phi/\Phi_0$ 变化、AB 共振抑制 📜Q。
- **Q2（理论如何解释）**：AA 区域离散能级（局域平带）→ 能量依赖 $S$ 矩阵 → 与手征模共振耦合 → dip/峰 📜Q。
- **Q3（理论↔实验对应）**：$\varphi\approx0.34$ ↔ Ref. 33（Rickhaus）参数；dip/峰 ↔ 非单调电导-栅压曲线；磁电导周期 ↔ AB 测量 📜Q。

> **增量价值**：与 T30 同方法谱系（唯象散射网络）；本文贡献"局域态耦合"这一补丁，是解读"网络态非全传播"的理论入口。不提供量子化电导平台数字。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取到 `/tmp/T25.txt`，grep 核对：**全部数字命中原文**——$l\approx14(\theta^\circ)^{-1}$ nm、$l\approx140$ nm、gap $\sim50$ meV、耦合 $\approx0.39$ eV、$\delta q\approx0.17\,\text{nm}^{-1}$、$\varphi'=3.89\pi$、$\varphi\approx0.34$、$U=3.25\hbar v_F/l$、$\varepsilon+U=4.25E_l$、$G_0=4e^2/h$、$\sqrt3 Gl/G_0W=2$、$P_{d1}=P_{d2}=1/4$、$\sim10$ nm（AA 尺寸）、$N_p=16$、$\Phi/\Phi_0=2$、$T/T_l=0.1$、$\sigma=\hbar v_F/(10l)$。

⚠️ 修正/降级：① arXiv 2303.03901 正文未出现 → 标"外部来源"；② 旧 review "Fano 共振/Fano 线形 $G(E)\propto(q+\epsilon)^2/(1+\epsilon^2)$"原文未用（grep `Fano`=0）→ 已删/降级；③ 旧 review "局域长度 ~3 nm"无源（grep `3 nm`=0）→ 已删；④ 保留 dip 宽度 $\propto|\tau|^2\hbar v_F/l$（原文命中，📜Q）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-11 | 初读（Phase 4 粗读）。 |
| 2026-08-20 | S-REV 机制重写：删"Fano 共振""局域长度 ~3 nm"；改为原文机制（AA 平带局域 DOS + 离散能级 + 能量依赖 S 矩阵 + 平均场库仑）。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（旧版归档 `archive/paper_review_T25_wittig2023_prb.backup_20260908.md`）：补参数分册/假设清单/推导链（Weidenmüller 公式链）/结论分层/假设-结论依赖图/接口；确认"Fano"未用、dip 宽度为 📜Q；补 $\varphi=\delta ql/2$ 推导与实验对标链。 |
