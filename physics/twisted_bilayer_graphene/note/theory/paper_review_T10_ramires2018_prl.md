<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4) → 2026-09-08 按 5 块演绎结构重写
 * @Date         : 2026-08-06（初读）→ 2026-09-08（5 块重写 + 反向核对）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T10_ramires2018_prl.md
 * @Description  : T10: Ramires & Lado 2018 — 微小角 TBG 电场诱导人工规范场（理论；2026-09-08 按五块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: Ramires & Lado (2018) — 微小角 TBG 中电场可调的人工规范场

| 字段 | 内容 |
|------|------|
| **编号** | T10 |
| **标题** | Electrically tunable gauge fields in tiny-angle twisted bilayer graphene |
| **作者** | A. Ramires, J. L. Lado |
| **期刊** | Physical Review Letters 121, 146801 (2018) |
| **DOI / arXiv** | 10.1103/PhysRevLett.121.146801 / arXiv:1803.04400（v3，2018-09-13，正文来源见下） |
| **类型** | 理论 — 人工规范场/赝朗道能级（解析 2-band 连续模型 + 紧束缚数值，无实验数据） |
| **课题组** | ETH Zurich（Institute for Theoretical Studies / Institute for Theoretical Physics） |
| **PDF** | ✅ `reference/pdfs/Ramires和Lado - 2018 - Electrically Tunable Gauge Fields in Tiny-Angle Twisted Bilayer Graphene.pdf`（⚠️ 该 PDF **仅含 Supplemental Material，8 页**；主文 5 页缺失，本次以 arXiv v3 `1803.04400` 主文补齐，主文内容与已发表 PRL 版本一致） |
| **精读日期** | 2026-08-06（初读）→ 2026-09-08（5 块重写 + 反向核对） |

> **结构说明**：本篇按「理论论文演绎结构」五块记（见 `note/shared/method/theory_paper_reading.md` §3）：**① 模型白箱 → ② 推导链 → ③ 结论清单（分层）→ ④ 假设-结论依赖图 → ⑤ 接口**。理论论文是白箱演绎、无反推、无可辨识实验。
> **全文无 ±**：本文数字均为解析/数值估算，统一 📜Q[~]；📊F 几乎不出现，「推导」等级成为主角。

---

## TL;DR

**本文想解决的理论问题**：微小角（$\alpha\ll1°$）TBG 中，均匀层间偏压 $U$ 能否**不靠应变**、仅靠电场产生一种"人工规范场"，从而可调地生成赝朗道能级（pLL）与强局域平带？

**主结果**：① 解析上把微小角 TBG 的均匀偏压**映射为人工规范场**，其强度 $g_{x,y}\sim U\,\alpha$（正比于偏压×扭角），规范场在 AB/BA 界面处最大、使低能模局域于界面 📜Q；② 数值上（紧束缚 + KPM）证实 $U\neq0$ 在电荷中性点附近产生**离散的 sharp 共振**（= pLL 平带），存在于 $\alpha\lesssim1°$ 的**连续角度区间**（无需魔角精调）📜Q；③ 最低 pLL 在实空间形成**涌现 Kagome 晶格**，每 Moiré 单胞 2 态/格点（6 条无自旋模），作者**提出** TBG 是可调挫败磁性/量子自旋液体的候选平台（suggest / open a new direction）📜Q。

**结论/意义**：首次把 TBG 电场从"开隙工具"升级为"**规范场发生器**"——电控替代应变，且不依赖魔角精调。⚠️ 全文为理论预言/估算（作者用词 show / find / suggest / estimate / open），**非已验证事实**；pLL 的现实实现依赖 $\alpha\approx0.1-0.3°$、$U\approx100-200$ meV 的窗口（见 §5.1）。

---

## 1. 模型白箱（理想系统 + 假设清单）

> 研究对象是**白箱**——作者自写的理想模型。本节写下模型（§1.1）与参数分册（§1.2），列出全部假设（§1.3）。

### 1.1 哈密顿量（每谷、自旋简并）

**起点（前提）**：完美 AB 堆叠双层石墨烯在 K 点，把"二聚体"（上层 A 子格 + 下层 B 子格，与另一层强耦合）积分掉后，得到低能 2-band 有效模型（有效自由度 = 上层 B 子格 + 下层 A 子格，二次带接触的 massive chiral 准粒子，ref 47）：

$$
H_0(\mathbf k)=\gamma\,\boldsymbol\sigma\cdot\Gamma_{\mathbf k}+U\sigma_z,\qquad \Gamma_{\mathbf k}=(k_x^2-k_y^2,\ 2k_xk_y)\tag{1}
$$

其中 $\boldsymbol\sigma=(\sigma_x,\sigma_y)$、$\gamma$ 度量逆有效质量、$U$ 为层间偏压强度。本征态 $|\Psi_+(\mathbf k)\rangle=(\gamma k_+^2,\ E-U)/N_0$、$|\Psi_-(\mathbf k)\rangle=(-E+U,\ \gamma k_-^2)/N_0$（$k_\pm=k_x\pm ik_y$），本征能 $E_\pm=\pm E=\pm(U^2+\gamma^2k_p^4)^{1/2}$，$N_0=[(E-U)^2+\gamma^2k_p^4]^{1/2}$。$U\neq0$ 打开**关于零能对称**的能隙 📜Q。

**微小角推广**：AB/BA 界面 + 均匀偏压，**拓扑等价**于"均匀 AB 堆叠 + 交替偏压"（跨 AB/BA 边界交换子格标签，Fig. 1c）📜Q。用空间相关幺正变换 $R(\mathbf r)=I$（AB 区）/$\sigma_x$（BA 区）旋转后，得到**调制偏压** $U(\mathbf r)$ 的有效模型：

$$
H_M(\mathbf r)=\gamma(\boldsymbol\sigma\cdot\Gamma)+U(\mathbf r)\sigma_z,\qquad \Gamma=(\partial_x^2-\partial_y^2,\ \partial_x\partial_y+\partial_y\partial_x)\tag{2}
$$

**广义本征值问题**：因本征态隐含依赖 $U(\mathbf r)$，引入双坐标 $(\mathbf r_0,\mathbf r)$（$\mathbf r_0$ 显式坐标、$\mathbf r$ 经 $U(\mathbf r)$ 的隐含依赖），$\mathbf r_0\to\mathbf r$ 极限回到原问题：

$$
H_G(\mathbf r_0,\mathbf r)=\gamma(\boldsymbol\sigma\cdot\Gamma_0)+\gamma(\boldsymbol\sigma\cdot\Gamma)+U(\mathbf r)\sigma_z\tag{3}
$$

用拟设 $|\Psi(\mathbf r_0,\mathbf r)\rangle=f_+|\Psi_+\rangle+f_-|\Psi_-\rangle$（$f_\pm$ 为待定光滑函数，Eq. 4），取矩阵元后得本征值方程（Eq. 10）：

$$
\begin{pmatrix}E(\mathbf r)&\Pi(\mathbf r)\\ \Pi^*(\mathbf r)&-E(\mathbf r)\end{pmatrix}\begin{pmatrix}f_+\\ f_-\end{pmatrix}=\varepsilon\begin{pmatrix}f_+\\ f_-\end{pmatrix}
$$

$$
\Pi(\mathbf r)=\gamma_x(\mathbf r)\Gamma_x+i\gamma_y(\mathbf r)\Gamma_y+A_x(\mathbf r)\partial_x+A_y(\mathbf r)\partial_y+C(\mathbf r)\tag{11}
$$

其中 $\gamma_{x,y}(\mathbf r)=\gamma v_{x,y}(\mathbf r)$，而

$$
A_x(\mathbf r)=2\gamma a_x\partial_xU+i\gamma a_y\partial_yU,\quad A_y(\mathbf r)=-2\gamma a_x\partial_yU+i\gamma a_y\partial_xU\tag{12}
$$

（矩阵元 $\langle\Psi_\pm|\sigma|\Psi_\mp\rangle=(v_x,iv_y)$ [Eq. 7]、$\langle\Psi_\pm|\sigma\partial_U|\Psi_\mp\rangle=(a_x,ia_y)$ [Eq. 8]、$\langle\Psi_\pm|\sigma\partial_U^2|\Psi_\mp\rangle=(b_x,ib_y)$ [Eq. 9]，显式在 SM；$v_{x,y},a_{x,y},b_{x,y}$ 的具体积分见 SM Eq. 2/4/7。）

**规范场识别**：做 Peierls 型替换 $\partial_{x,y}\to\partial_{x,y}+g_{x,y}(\mathbf r)$，对比导数项系数，解出人工规范场：

$$
g_x(\mathbf r)=\frac{A_x\gamma_x-iA_y\gamma_y}{2(\gamma_x^2+\gamma_y^2)},\qquad g_y(\mathbf r)=\frac{A_y\gamma_x-iA_x\gamma_y}{2(\gamma_x^2+\gamma_y^2)}\tag{13,14}
$$

**关键标度**：$A_{x,y}\propto\partial U(\mathbf r)$，$U(\mathbf r)\sim U\cos(k_M r)$（$k_M=2\pi/L_M$），故 $g_{x,y}\sim U k_M$；用 $L_M=a/[2\sin(\alpha/2)]$ 得 $g_{x,y}\sim U\alpha$ 📜Q。

**数值哈密顿量**（紧束缚，Eq. 15）：

$$
H=t\sum_{\langle ij\rangle}c_i^\dagger c_j+\sum_{ij}\hat t_\perp(\mathbf r_i,\mathbf r_j)c_i^\dagger c_j+U\sum_i\tau_z^{ii}c_i^\dagger c_i
$$

$\hat t_\perp(\mathbf r_i,\mathbf r_j)=t_\perp[(z_i-z_j)^2/|\mathbf r_i-\mathbf r_j|^2]e^{-\beta(|\mathbf r_i-\mathbf r_j|-d)}$（SM Eq. 41）📜Q。

### 1.2 参数分册（区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $U$（均匀层间偏压）、$\alpha$（扭角，经 Moiré 周期 $L_M$ 进入调制）、$\varepsilon$（能量，扫谱） |
| **导出量（由旋钮+常数算出）** | $g_{x,y}\sim U\alpha$（人工规范场）、$A_{x,y}(\mathbf r)$、$\gamma_{x,y}(\mathbf r)=\gamma v_{x,y}$、$L_M=a/[2\sin(\alpha/2)]$、$k_M=2\pi/L_M$ |
| **模型内部量（解的性质）** | pLL 能谱、pLL 带宽/局域化长度、DOS、谷极化 $\langle V\rangle$、∂E/∂U |
| **固定常数** | $t\approx3$ eV、$t_\perp\approx300$ meV（主文 ref 47）；SM 紧束缚取 $t=-2.7$ eV；$\beta=7a^{-1}$、层间距 $d=3a$、$a$ 碳-碳距离 |
| **预言量（可检验）** | pLL 峰能量（$20-50$ meV）、涌现 Kagome 晶格（2 态/格点、6 无自旋模/MUC）、谷极化 |

> **符号防混**：$\gamma$（逆有效质量系数）≠ $\gamma_{x,y}(\mathbf r)$（含 $v_{x,y}$ 的位置相关耦合）≠ $g_{x,y}$（最终规范场）。**无"反推量"层**（理论论文不反推自数据）。

### 1.3 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **2-band 低能有效模型**（积分掉二聚体），合法域 $E<U<t_\perp$（能量小于偏压、偏压小于层间耦合） | 模型 | 📜Q |
| A2 | **AB/BA 界面 + 均匀偏压 ≡ 均匀 AB + 交替偏压**（跨界面交换子格标签，幺正旋转） | 模型 | 📜Q |
| A3 | **Bernal 堆叠连续模型**，合法域 $\alpha\ll1°$（AB 区大） | 模型 | 📜Q |
| A4 | **单谷模型**（谷守恒；不混谷） | 模型 | 📜Q |
| A5 | **自旋简并**（自旋指标整体省略） | 模型 | 📜Q |
| A6 | **电场不屏蔽、层不起伏**（"does not take into account screening nor corrugation"） | 数值 | 📜Q |
| A7 | **层间耦合标度 $\alpha\to\alpha/\lambda,\ t_\perp\to\lambda t_\perp$**（合法域 $\alpha\lesssim1°$、$t_\perp<t$），用于用小单胞达微小角 | 数值 | 📜Q |
| A8 | **刚性格子**（无晶格弛豫/原子重构；全文 grep `relax/reconstruct` 零命中） | 数值 | 💭I |

---

## 2. 推导链（顺论文演绎顺序，每步"输入→输出→所用假设/定理→合法域"）

### 2.0 总览：一条演绎链（前提定理 → 模型 → 推导 → 数值边界）

| 层 | 论文内容 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | AB 堆叠 2-band 模型 | 双层石墨烯 + 二聚体 | 二次带接触模型 Eq. (1) | 积分掉二聚体（ref 47） | $E<t_\perp$ |
| 模型层 | 微小角 TBG 调制模型 | Eq. (1) + 交替偏压旋转 | 调制 $U(\mathbf r)$ 模型 Eq. (2) | A2（AB/BA≡交替偏压） | A3（$\alpha\ll1°$） |
| 推导层 | 规范场识别 | Eq. (2) + 双坐标方法 | 规范场 $g_{x,y}$ Eq. (13,14) | A1（双坐标拟设） | $E<U<t_\perp$ |
| 边界层 | 紧束缚 + KPM 验证 | Eq. (15) | pLL 谱 + Kagome + 谷极化 | A4–A8 | $U<t_\perp$、$\alpha\lesssim1°$ |

### 2.1 前提定理层：AB 堆叠 2-band 有效模型

- 完美 AB 堆叠双层石墨烯 K 点，二聚体（上层 A + 下层 B）积分掉 → 有效自由度 = 上层 B + 下层 A，**二次带接触**的 massive chiral 准粒子（ref 47）📜Q。
- 加均匀偏压 $U$ → 两分量获得不同 onsite 能量 → Eq. (1) → 能隙 $E_\pm=\pm(U^2+\gamma^2k_p^4)^{1/2}$ 关于零能对称 📜Q。

### 2.2 模型层：微小角 TBG 的调制偏压模型

- **关键一步**：AB/BA 界面 + 均匀偏压 ≡ 均匀 AB + 交替偏压（子格标签交换，Fig. 1c）📜Q。用 $R(\mathbf r)=I/\sigma_x$ 旋转 → 偏压成为空间调制 $U(\mathbf r)$ → Eq. (2) 📜Q。
- 因本征态隐含依赖 $U(\mathbf r)$，引入双坐标广义本征值问题 Eq. (3)（ref 48,49 方法）📜Q。
- 拟设 $f_+|\Psi_+\rangle+f_-|\Psi_-\rangle$（Eq. 4），取矩阵元（Eq. 7–9）→ 本征值方程 Eq. (10) 📜Q。

### 2.3 推导层：人工规范场 $g_{x,y}\propto\partial U$

- Peierls 型替换 $\partial_{x,y}\to\partial_{x,y}+g_{x,y}$（Eq. 9 起），对比 Eq. (11) 中 $\Pi(\mathbf r)$ 的导数项 → 识别 $A_x=2[\gamma_xg_x+i\gamma_yg_y]$、$A_y=2[\gamma_xg_y+i\gamma_yg_x]$（SM Eq. 26）→ 反解 $g_{x,y}$（Eq. 13,14）📜Q。
- **标度论证**：$U(\mathbf r)\sim U\cos(k_Mr)$ → $A_{x,y}\propto\partial U(\mathbf r)\propto U k_M$ → $g_{x,y}\sim U k_M\sim U\alpha$ 📜Q。
- **位置依赖**：规范场在**偏压导数取极值处**最大 = AB/BA 界面 → 低能模局域于界面 📜Q。
- 对 $U$ 小值，$a_{x,y},v_{x,y}$ 只含 $\propto U$ 的小修正（可忽略），规范场对偏压的主导依赖来自 $A_{x,y}\propto\partial U$ 的显式线性项 📜Q（SM）。
- 同一方法适用 hBN 上单层/三层石墨烯（SM §III，调制子格失衡 $m(\mathbf r)$，规范场 $g=(a/v)(\partial_x m, -\partial_y m)$，SM Eq. 33）📜Q。

### 2.4 边界层：紧束缚 + KPM 数值验证（pLL 三判据）

- 紧束缚 Eq. (15) + 核多项式方法（KPM，Chebyshev 展开 $N=10000$ 矩，能量分辨 $10^{-3}-10^{-4}t$，蒙特卡洛 400 k 点）算 DOS 📜Q。
- **pLL 三判据**（SM §V）📜Q：
  1. $\partial E/\partial g>0$（$g=\sqrt{g_x^2+g_y^2}$，能量随规范场增大；$g\sim U$ → $\partial E/\partial U>0$，用 Hellmann-Feynman $\partial E/\partial U=\langle\Psi|\tau_z|\Psi\rangle$，SM Eq. 49）；
  2. 局域化长度随 $U$ 增大而减小（类比磁长度 $l_B\propto1/\sqrt B$；数值上 Γ 点 pLL 能带劈裂随 $U$ 增大趋于零 = 更局域）；
  3. 谷极化（单谷模型的必要条件；用 Haldane 型谷算符，SM Eq. 50–53）。
- **谱演化**：$U=0$ 时魔角 $\alpha\approx1°$ 半填充 DOS 发散、偏离即消失，$\alpha\ll1°$ 态流向零能（复杂背景）；$U\neq0$ 时谱变干净，零能附近低 DOS 平滑背景（= 螺旋网络）+ sharp 共振（= pLL）📜Q（Fig. 2）。大角度（$\alpha\approx1.5°$）偏压只增强 CNP 处 DOS、无新共振；小角度（$\alpha\lesssim1°$）偏压产生**全新 pLL 组**，能量随偏压升高 📜Q。
- **三组态**（Fig. 3）📜Q：AA 态（AA 区局域、三角晶格、对偏压不敏感，$\partial E/\partial U=0$）、螺旋网络态（AB/BA 之间离域、流向 CNP）、pLL（AB/BA 之间局域、形成 **Kagome 晶格**，能量随 $U$ 升高）。晶格常数 = Moiré 长度 $L_M$。
- **能带计数**：Kagome = **2 态/格点 = 6 无自旋模/Moiré 单胞** 📜Q。

---

## 3. 结论清单（分层：定理式主张 / 估算 / 预言）

### 3.1 定理式主张（解析构造的产物，依赖 A1–A3）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 规范场存在性 | 微小角 TBG 均匀偏压可映射为人工规范场 $g_{x,y}$，Eq. (13,14) | A1（2-band）、A2（AB/BA≡交替偏压）、A3（$\alpha\ll1°$） |
| 标度律 | $g_{x,y}\sim U\alpha$（规范场正比于偏压×扭角） | 同上 + 小 $U$ 展开 |
| 空间结构 | 规范场在 AB/BA 界面最大 → 低能模局域于界面 | A2 |

### 3.2 估算（经验/近似，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| pLL 现实窗口 | $\alpha\approx0.1-0.3°$、$U\approx100-200$ meV | A1（$E<U<t_\perp$）、A3 | 📜Q[~]（"we estimate"） |
| pLL 峰能量 | $20-50$ meV（相对 CNP） | 同上 | 📜Q[~] |
| 魔角（背景） | $\alpha\approx1°$（$t_\perp\approx300$ meV 处首个平带） | A7 | 📜Q[~] |
| 微小角可达性 | $\alpha\approx0.1°$ 经 $m_0=70$、$t_\perp=0.4t$ 实现 | A7 | 📜Q[~] |
| Kagome 计数 | 2 态/格点、6 无自旋模/MUC | A4（单谷） | 📜Q[~] |

### 3.3 预言（可检验性 → §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| $U\neq0$ 在 $\alpha\lesssim1°$ 连续角度区间产生 pLL 平带（无需魔角精调） | "show / we find"（解析+数值构造）📜Q | 中——DOS/输运谱学 |
| 最低 pLL 形成涌现 Kagome 晶格 → 可调挫败磁性/量子自旋液体平台 | "suggest / open a new direction" 📜Q | 弱——需后续强关联研究 |
| 规范场在 AB/BA 界面局域低能模 | "This suggests that low energy modes ... localized" 📜Q | 中——空间 LDOS |
| 单/三层石墨烯+hBN 类似规范场 | "similar results are valid" 📜Q | 中——hBN 平台 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

1. **解析↔数值互验**：$g\sim U\alpha$ 标度 → 数值 pLL 能量随 $U$、$\alpha$ 线性升高（Fig. 3a,b，与真实磁场下单层/AB 双层 LL 谱 [Fig. 3c,d] 对照）📜Q。
2. **标度论证验证**：$t_\perp=0.3t$ 与 $0.4t$ 两套耦合都出现 pLL，验证 $\alpha\to\alpha/\lambda,\ t_\perp\to\lambda t_\perp$ 标度（SM Fig. 1/Fig. 4）📜Q。
3. **谷极化核对**：Haldane 型谷算符证实 pLL 近完美谷极化 → 支撑单谷解析模型 📜Q。

### 3.5 概念区分（分类，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| pLL vs 螺旋网络态 | $\partial E/\partial U$ 符号 + 空间局域（pLL 局域、网络离域）📜Q | 三类态并存（AA/网络/pLL） |
| pLL vs AA 模 | AA 模 bonding-antibonding、$\partial E/\partial U=0$；pLL $\partial E/\partial U>0$ 📜Q | 可由 Eq. (49) 区分 |
| 电控规范场 vs 应变规范场 | 电场可连续调、不需晶格操纵 📜Q | 本文是电控（非应变） |

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性 |
|---|---|---|---|
| A1（$E<U<t_\perp$） | $U\gtrsim t_\perp$ 或高能 | 2-band 模型、Eq. (13,14) 规范场 | Eq. 合法域即结论适用域 📜Q |
| A2（AB/BA≡交替偏压） | 界面非突变 / 含 AA 区 | $U(\mathbf r)$ 调制形式 | smooth 过渡未破坏主结论（定性）📜Q |
| A3（$\alpha\ll1°$） | 大角度（如 $\alpha\approx1.5°$） | pLL 不出现（偏压只增强 CNP DOS）| 负对照验证 📜Q |
| A4（单谷） | 谷间散射 | 谷极化 pLL 图景 | 数值谷算符确认近完美极化 → 风险低 📜Q |
| A6（无屏蔽/无起伏） | 真实屏蔽、层起伏 | 偏压形式、pLL 定量 | 作者声明未考虑 📜Q；属后续修正 💭I |
| A7（层间耦合标度） | $t_\perp\gtrsim t$ | Dirac 锥结构被破坏、标度失效 | 合法域显式声明 📜Q |
| A8（无弛豫） | 晶格弛豫/原子重构 | 网络几何、Kagome 位置 | 未建模（grep 零命中）💭I |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- pLL sharp 共振峰（DOS 谱）＋ 空间局域 LDOS（AB/BA 界面 Kagome 图案）📜Q；
- $\partial E/\partial U$ 标度（pLL 能量随偏压升高，蓝色态 Fig. 2b）📜Q；
- 谷极化（谷算符 / 谷分辨谱学）📜Q；
- 作者指出实验需求已被近期实验（ref 41）"almost already fulfilled"，可通过单器件输运直接表征 pLL 📜Q。

### 5.2 设计原则（"电控规范场"三要素）

$U$ 开隙 + 诱导规范场、$\alpha$ 设 Moiré 周期/规范场强度、pLL 形成 Kagome 挫败晶格 💭I（本文 "show / suggest / open"）。

### 5.3 后续文献修正（时间倒挂，💭I）

- **T14（Chou 2020, PRR）**：同一网络模型在磁场下的 Hofstadter/Floquet 推广——pLL/网络态的磁场版。
- **T12（Tsim 2020, TZM）**：推翻"连通网络"图景（AA 节点确定性散射），对本文"螺旋网络态"谱解释构成部分修正。
- **E14（Zheng 2022 实验）**：Kagome 中心态 = pLL（本文机制）的实验实现/现实修正（重构→三角网络、e-h 不对称）——卡片层对标（见 §7）。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 2-band 模型合法域 | 仅 $E<U<t_\perp$，高能/大偏压失效 | 📜Q |
| 无屏蔽/无起伏 | 电场形式忽略屏蔽与层起伏 | 📜Q |
| 无晶格弛豫 | 弛豫/原子重构未建模（grep 零命中） | 💭I |
| 未给输运定量预言 | 只给 DOS/局域化，未算电导 | 📜Q（无量子化电导讨论） |
| pLL 定量依赖 $t_\perp$ 标度 | 用放大的 $t_\perp$ 达微小角，非真实参数 | 📜Q（A7） |
| 强关联后果未展开 | Kagome→量子自旋液体仅提议 | 📜Q（"suggest"） |

## 7. 与其他工作的关系（跨论文对标放这里）

| 工作 | 关系 |
|------|------|
| San-Jose & Prada 2013 (ref 40, = T5) | 引用——偏压下螺旋网络的先导；本文在其"螺旋网络"基础上**新增 pLL 类局域态** 📜Q |
| Efimkin & MacDonald 2018 | （本文 arXiv v3 未引；概念上网络模型系统理论）💭I |
| Bistritzer & MacDonald 2011 (ref 36) | 引用——魔角 $\alpha\approx1°$ 平带标度 📜Q |
| McCann & Koshino 2013 (ref 47) | 引用——AB 双层 2-band 有效模型来源 📜Q |
| Yankowitz 2012 / Chen 2018 (SM ref 1,2) | 引用——hBN 上单/三层 Moiré 实验动机（SM §III）📜Q |
| Guinea 2010 应变赝磁场 | （概念对照——应变 vs 电控规范场；本文引言讨论 strain gauge fields）📜Q |

> ⚠️ Phase S 外部对标（**非本文引用**，时间倒挂 💭I）见 §5.3；引用关系依据 `cards.md` Q2/Q3 卡片与 `appendix_B_theory.md`。

## 8. 对后续研究的影响

- 把 TBG 电场从"开隙"升级为"**规范场发生器**"——电控规范场成为新范式 📜Q。
- 提供**免精调**的平带/局域态途径（连续角度区间，对比魔角单点）📜Q。
- Kagome 涌现晶格 → 挫败磁性/量子自旋液体平台的候选 📜Q。
- 被 T14（磁场 Hofstadter）与 E14（实验 PLL）继承发展 💭I。

## 9. 理论模型映射（供 TBPM/Kubo 计算对标）

| 映射 | 说明 |
|------|------|
| $\alpha\to L_M\to$ 网络几何 | 扭角→Moiré 周期 $L_M=a/[2\sin(\alpha/2)]$→AB/BA/AA 图案 📜Q |
| $U\to$ 规范场/开隙 | 均匀偏压→$g_{x,y}\sim U\alpha$ + AB/BA 开隙，合法域 $E<U<t_\perp$ 📜Q |
| pLL 三判据 | $\partial E/\partial U>0$、局域化、谷极化 → TBPM 可复现的 DOS/LDOS 判据 📜Q |
| Kagome 计数 | 2 态/格点、6 无自旋模/MUC → TB 紧束缚对角化可核对 📜Q |
| 谷算符 | Haldane 型谷算符（SM Eq. 50–53）→ 谷分辨计算对标 📜Q |

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：本文给出**理论预言**靶标——pLL 局域态 vs 螺旋网络离域态的区分（$\partial E/\partial U$ 符号 + 空间 LDOS + Kagome 图案）📜Q；后续 STM（E14）按此解读。
- **Q2（理论如何解释）**：微小角 TBG 偏压→人工规范场 $g\sim U\alpha$→pLL 局域平带 + 螺旋网络共存；三判据（能量/局域化/谷极化）定量化 📜Q。⚠️ "连通网络"后被 TZM 部分修正（§5.3）。
- **Q3（理论↔实验对应）**：$U$ ↔ 偏压（$100-200$ meV）、$\alpha$ ↔ 扭角（$0.1-0.3°$）、pLL 峰（$20-50$ meV）↔ 谱学/输运、Kagome ↔ 空间 LDOS 📜Q。

> **增量价值**：与 T5（San-Jose 网络奠基）分工——本文是**规范场视角 + pLL 局域态 + Kagome**，T5 是网络判据 + 可编程开关；比 T14 多了"电控规范场"的解析起源，少了磁场 Hofstadter 推广。report/appendix 可用本文三处数字（均 📜Q，已核对）：$g\sim U\alpha$、pLL 窗口 $\alpha\approx0.1-0.3°/U\approx100-200$ meV、$20-50$ meV 峰位。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取 arXiv v3 主文 + 提供 PDF（SI）到 `/tmp`，逐项 grep 核对：

| 数字/公式 | grep 命中位置 | 结论 |
|------|--------------|------|
| $t\approx3$ eV、$t_\perp\approx300$ meV | 主文 "t ≈ 3 eV and t⊥ ≈ 300 meV" | ✓ 📜Q[~] |
| SM $t=-2.7$ eV | SM Eq. 55 "t = −2.7 eV" | ✓ 📜Q[~]（SM 紧束缚值，与主文 ≈3 eV 并存） |
| $\beta=7a^{-1}$、$d=3a$ | SM §IV B | ✓ |
| $g_{x,y}\sim U\alpha$ | 主文 "gx,y(r) ∼ U α" | ✓ |
| pLL 窗口 $\alpha\approx0.1-0.3°$、$U\approx100-200$ meV、$20-50$ meV | 主文末段 "we estimate" | ✓ 📜Q[~] |
| 魔角 $\alpha\approx1°$、$m_0=70$（59644 sites）、$t_\perp=0.4t$、$m_0=75$ | 主文 Fig. 2/3 + SM Fig. 4 | ✓ |
| $E<U<t_\perp$、$U<t_\perp$ | 主文 "E < U < t⊥" | ✓ |
| 2 态/格点、6 无自旋模/MUC | 主文 "2 states per site (6 spinless modes per Moiré unit cell)" | ✓ |
| $N=10000$ 矩、400 k 点、$10^{-3}-10^{-4}t$ | SM §IV D | ✓ |
| Eq. (1)–(15) 编号 | 主文 | ✓ |

⚠️ 修正/降级：① **PDF 仅含 SI**（8 页），主文以 arXiv:1803.04400v3 补齐（内容与 PRL 一致），头部表已标注；② 旧 review 无无源数字（未见 t⊥≈0.4 eV 等脑补值），但结构为叙事体，本次整体重写；③ 未引入量子化电导（本文未出现该量）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（research_onboarding Phase 4），叙事体 8 节。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求；理论论文"白箱演绎"）。旧叙事体归档 `archive/paper_review_T10_ramires2018_prl.backup_20260908.md`。 |
| 2026-09-08 | **QC 修正**：① 发现提供 PDF 仅含 SI（8 页），主文以 arXiv v3 补齐并标注头部；② 全文数字重 grep 全命中；③ 补充 Eq. (1)–(15) 完整推导链 + 参数分册 + 8 条假设清单 + 假设-结论依赖图。 |
