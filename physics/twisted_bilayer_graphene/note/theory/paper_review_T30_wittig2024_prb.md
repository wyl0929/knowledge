<!--
 * @Author       : AI 精读 (paper-reading skill)
 * @Date         : 2026-08-11（初读）→ 2026-08-20（S-REV 机制重写）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T30_wittig2024_prb.md
 * @Description  : T30: Wittig, Dominguez & Recher 2024 — 谷手征 Kagome 网络中的自旋轨道耦合效应（2026-09-08 按 5 块演绎结构重写）
-->

# Paper Review: Wittig, Dominguez & Recher (2024) — 谷手征 Kagome 网络中的自旋轨道耦合效应

| 字段 | 内容 |
|------|------|
| **编号** | T30 |
| **标题** | Effects of spin-orbit coupling in a valley chiral kagome network |
| **作者** | P. Wittig, F. Dominguez, P. Recher |
| **期刊** | Physical Review B 109, 245429 (2024)（Editors' Suggestion） |
| **DOI / arXiv** | 10.1103/PhysRevB.109.245429 / 2403.10181（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 理论 — 谷手征 Kagome 散射网络 + Rashba 自旋轨道耦合（唯象散射模型 + 石墨烯 Rashba 哈密顿量，无实验数据） |
| **课题组** | Wittig / Dominguez / Recher (TU Braunschweig) |
| **PDF / SI** | ✅ `reference/pdfs/Wittig 等 - 2024 - Effects of spin-orbit coupling in a valley chiral kagome network.pdf`（正文 14 页 + Appendix A–C） |
| **精读日期** | 2026-08-11（初读）→ 2026-08-20（机制修正）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」五块记。本文是**唯象散射白箱**——研究对象是按 $C_3$、$M_xT$ 对称性构造的 Kagome 散射网络 + Rashba SOC 项，结论是"磁电导周期缩减、尖锐共振、电导自旋极化"这类模型预言。⚠️ 原文**只含 Rashba SOC**（无内禀 SOC、无 QSH/$Z_2$）。

---

## TL;DR

**本文想解决的理论问题**：谷手征 Kagome 网络（双对准石墨烯-hBN、周期应变石墨烯中可实现）中，加入 Rashba 自旋轨道耦合（SOC）会如何改变能谱、磁输运与自旋输运？

**主结果**：① 按对称性（$C_3$、$M_xT$）构造 Kagome 散射网络模型，收缩单三角形为能量依赖 $S$ 矩阵 $S_\triangle$（Eq. 7），把 Kagome 网络映射为三角网络 📜Q；② Rashba SOC（$\alpha=\alpha_R l/(\pi\hbar v_F)$，石墨烯/WSe₂ 上 $\alpha_R\approx15$ meV、$l\sim100$ nm、$v_F\approx10^6$ m/s → $\alpha\approx0.7$）导致能带**局域化/扁平化**、磁电导**周期缩减**（$\Phi/\Phi_0=8\to4$，$\alpha=2n+1$ 时）与**尖锐共振** 📜Q；③ 发现电导的**有限自旋极化**（最高 $P\approx0.9$），可用于自旋电子学器件 📜Q。

**结论/意义**：把 SOC 引入谷手征 Kagome 网络，揭示几何 + Rashba 干涉（Aharonov-Casher 类效应）的自旋电子学后果 📜Q。⚠️ 全文是模型预言（"we construct / we identify / we find / could be exploited"），非实验证实。

---

## 1. 模型白箱（Kagome 散射网络 + Rashba 项）

### 1.1 哈密顿量/散射模型

**散射网络**：Kagome 网络由沿六边形/三角形边传播的手征模 + 节点散射构成；保时间反演，对谷手征模反向传播 📜Q。单个三角形的散射（Eq. 1–3）：

$$\begin{pmatrix}b_2\\\beta_2\end{pmatrix}=S_1\begin{pmatrix}a_1\\\alpha_1\end{pmatrix},\quad \begin{pmatrix}b_3\\\beta_3\end{pmatrix}=S_2\begin{pmatrix}a_2\\\alpha_2\end{pmatrix},\quad \begin{pmatrix}b_1\\\beta_1\end{pmatrix}=S_3\begin{pmatrix}a_3\\\alpha_3\end{pmatrix}$$

$C_3$ 与 $M_xT$ 对称性强制 $S_0:=S_1=S_2=S_3$ 且对称（$S_0=S_0^t$），最一般 $2\times2$ 幺正对称矩阵（Eq. 4）：

$$S_0=\begin{pmatrix}e^{i\phi}\sqrt{P_R} & i\sqrt{1-P_R}\\[2pt] i\sqrt{1-P_R} & e^{-i\phi}\sqrt{P_R}\end{pmatrix}$$

$P_R=1-P_L$ 为向右散射概率、$\phi$ 为内外散射相位差。预期 $P_R>P_L$（几何强迫 60° 右出射 vs 120° 左出射重叠更大）；强局域极限 $P_R\approx P_L\approx0.5$ 📜Q。动力学相位 $\alpha_i=\exp[i\pi\xi/2]\beta_i$（Eq. 5，$\xi=El/(\pi\hbar v_F)$，链长 $l/2$）📜Q。收缩单三角形得能量依赖总 $S_\triangle$（Eq. 6–7）📜Q。对谷 $S_\triangle^{K'}=(S_\triangle^K)^t$ 📜Q。

**Rashba SOC**：低能 K/K′ 谷石墨烯哈密顿量（Eq. 18–20）：

$$H=H_0+H_R,\qquad H_0=\hbar v_F(\tau k_x\sigma_x+k_y\sigma_y),\qquad H_R=\alpha_R(\tau\sigma_x s_y-\sigma_y s_x)$$

（$s_i$ 自旋、$\sigma_i$ 子格 Pauli 矩阵，$\tau=\pm1$ 谷，$\alpha_R$ SOC 常数）。改写为自旋依赖动量平移 $H=\hbar v_F\,\sigma\cdot(k+s\times\alpha_R)$（Eq. 21，$\alpha_R=(0,0,\alpha_R/\hbar v_F)^t$）📜Q。类比磁场 Peierls 相位，动量平移 → 几何相位（Eq. 22–23）$A(\theta)=\exp[i\pi\alpha(s_x\sin\theta-s_y\cos\theta)/2]$（Eq. 24，$\alpha=\alpha_R l/(\pi\hbar v_F)$）📜Q。传播矩阵 $M(\theta)=\exp[i\pi s_0\xi/2]A(\theta)$（Eq. 28，$s_0$ 自旋恒等）📜Q。

**自旋化网络**：$S_\sigma=\operatorname{diag}(S_{0,\sigma},S_{0,\sigma},S_{0,\sigma})$（Eq. 30，节点 $S$ 自旋无关 $S_{0,\sigma}=S_0$）；Bloch 定理得 $M(k)S a_k=D(\alpha,\xi)^{-1}a_k$（Eq. 35）、$\det[M(k)S-D(\alpha,\xi)^{-1}]=0$（Eq. 36）📜Q。

### 1.2 参数分册

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $P_R$（右散射概率）、$\phi$（散射相位）、$\alpha$（无量纲 Rashba，$\alpha=\alpha_R l/(\pi\hbar v_F)$）、$E_F$（扫谱）、磁场 $\Phi$ |
| **导出量** | 能标 $E_l=\pi\hbar v_F/l$、温度标 $T_l=\pi\hbar v_F/(k_B l)$、面积 $A=\sqrt3 l^2/2$（$A_\text{hex}=3\sqrt3 l^2/8$、$A_\triangle=\sqrt3 l^2/16$） |
| **模型内部量（解的性质）** | 网络能带、电导 $G$、磁电导周期、自旋极化 $P$ |
| **固定常数** | $G_0=e^2/h$（Kagome 单谷单模，**非** $4e^2/h$）、$\alpha_R\approx15$ meV（WSe₂ 上）、$l\sim100$ nm、$v_F\approx10^6$ m/s |
| **预言量（可检验）** | 磁电导周期 $\Phi/\Phi_0=8\to4$、尖锐共振、自旋极化 $P$ |

> 无"反推量"层。**符号防混**：$\alpha$（无量纲 Rashba）≠ $\alpha_R$（Rashba 常数，meV）；$\phi$（散射相位）≠ 应变角；$G_0=e^2/h$（本文 Kagome）≠ T25 的 $G_0=4e^2/h$（三角 mTBG 双谷双自旋）。

### 1.3 显式假设清单

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **唯象散射模型**（$C_3$、$M_xT$ 对称性） | 模型 | 📜Q |
| A2 | **单谷单条手征模**（Kagome 网络，对比 mTBG 三角网络的 2 模） | 模型前提 | 📜Q |
| A3 | **节点 $S$ 自旋无关**（$S_{0,\sigma}=S_0$） | 模型 | 📜Q |
| A4 | **低能石墨烯 Dirac 描述 + Rashba**（Eq. 18–20） | 模型 | 📜Q |
| A5 | **仅 Rashba SOC**（无内禀 SOC；石墨烯 SOC 本身 μeV 量级，靠 TMD 邻近增强到 meV） | 模型 | 📜Q |
| A6 | **自旋轨道耦合为几何相位**（动量平移 $s\times\alpha_R$ 类比 Peierls 相位） | 推导 | 📜Q |

> 判别性扫轴：$P_R$（$0\to1$）、$\phi$（$[-\pi/3,\pi/3]$）、$\alpha$（$0,0.2,1$）、$\Phi/\Phi_0$、温度 $T/T_l$ 📜Q。

---

## 2. 推导链（顺论文顺序）

### 2.0 总览

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 模型层 | Kagome scattering network (Sec. II) | $C_3,M_xT$ | $S_0$（Eq. 4）、$S_\triangle$（Eq. 7） | A1–A2 | 单谷 |
| 推导层 | 无 SOC 网络 (Sec. III) | Bloch 定理 | 能带（Eq. 11–14）、电导（Eq. 15–17） | A1 | — |
| 推导层 | Rashba SOC (Sec. IV) | $H=H_0+H_R$ | 几何相位（Eq. 22–24）、自旋化 $S$（Eq. 34–36） | A4–A6 | 低能 |
| 推导层 | 磁电导 + 共振 | $M(\theta)$ | 周期 $8\to4$（Eq. 39）、共振（Eq. 40） | A6 | $\alpha=2n+1$ |
| 推导层 | 自旋极化 (Sec. IV C) | 自旋分辨透射 | $P_x,P_y,P_z,P$（Eq. 50–52） | A3 | — |

### 2.1 模型层：Kagome 网络 → 三角网络

- **输入**：$C_3$、$M_xT$ 对称性。
- **输出**：$S_0$（Eq. 4，最一般 $2\times2$ 幺正对称矩阵）、单三角形总 $S_\triangle$（Eq. 7，能量依赖，因收缩的链上动力学相位）📜Q。
- **映射**：收缩单三角形为散射节点 → Kagome 网络映射为三角网络（类比 mTBG 偏压三角网络）📜Q。

### 2.2 推导层：无 SOC 能谱与磁电导

- **能带**：Bloch 定理 + $M(k)S_\triangle a_k=e^{-i\pi\xi/2}a_k$（Eq. 10）→ $\det[M(k)S_\triangle-e^{-i\pi\xi/2}1_3]=0$（Eq. 11）→ $f(k_x,k_y)=\cos(3\pi\xi/2)$（Eq. 12），$f=\sqrt{P_RP_R}\cos(3\phi)-(1-P_R)\cos(k_xl/2-\phi)-2(1-P_R)\cos(\tfrac{k_xl}{2}+\phi)\cos(\tfrac{\sqrt3 k_yl}{2})$（Eq. 13）📜Q。解 $\xi_\pm=E_\pm l/(\pi\hbar v_F)=\pm\tfrac2{3\pi}\arccos f$（Eq. 14）；基本域 $\xi\in[-2/3,2/3]$、$\phi\in[-\pi/3,\pi/3]$ 📜Q。
- **能隙闭合**：$P_R\to1(0)$ 出平带（电子绕单三角形/六边形闭合轨道）；$\Gamma$ 点 $P_R=1/4$ 闭合（$\phi=0$），一般 $P_R=1/[4\cos^2\phi]$；$K(K')$ 点 $P_R=1/[4\cos^2(\phi\pm2\pi/3)]$；$P_R=1/3$ 且 $\phi=\pm\pi/6$ 时同时闭合 📜Q。
- **电导**：$G=G_0\tfrac{W}{\sqrt{3l/2}}\int dE\,T(E)(-\partial f_0/\partial E)$（Eq. 15）、零温 $G=G_0\tfrac{W}{\sqrt{3l/2}}T(E_F)$（Eq. 16），$G_0=e^2/h$ 📜Q。$P_R=0.5$ 电导最大；$P_R=1/3,\phi=\pi/6$ 处周期缩到 $2/3E_l$ 且共振峰更高（Eq. 17 解析 $T$）📜Q。磁导：Peierls 相位 $\propto\Phi=BA$；$\Phi/\Phi_0=8$ 周期（可绕单三角形面积 $A_\triangle=A/8$）📜Q。

### 2.3 推导层：Rashba SOC 的几何相位

- **输入**：$H=\hbar v_F\,\sigma\cdot(k+s\times\alpha_R)$（Eq. 21）。
- **输出**：动量平移 → 几何相位 $A(\theta)=\exp[i\pi\alpha(s_x\sin\theta-s_y\cos\theta)/2]$（Eq. 24）→ 传播矩阵 $M(\theta)=\exp[i\pi s_0\xi/2]A(\theta)$（Eq. 28）📜Q。
- **估算**：石墨烯/WSe₂ $\alpha_R\approx15$ meV（ref 59）、$l\sim100$ nm、$v_F\approx10^6$ m/s → $\alpha\approx0.7$ 📜Q。
- **自旋化网络**：$D(\alpha,\xi)=\operatorname{diag}[M(-\pi/3),M(2\pi/3),M(\pi),M(0),M(\pi/3),M(-2\pi/3)]$（Eq. 34）→ 能带方程 $\det[M(k)S-D(\alpha,\xi)^{-1}]=0$（Eq. 36）📜Q。SOC 使能带自旋-动量劈裂 + 扁平化（局域化效应）📜Q。

### 2.4 推导层：磁电导周期缩减 + 尖锐共振

- **周期减半条件**：节点间传播自旋旋转 $180°$ 时有效周期翻倍，发生在 $M(\theta)$ 完全非对角，即 $\alpha=2n+1$（Eq. 39，$n\in\mathbb Z$）📜Q。此时磁电导周期 $\Phi/\Phi_0=8\to4$（绕单三角形路径不再贡献），对应 **Aharonov-Casher 效应**（非 Abel 相位场）📜Q。
- **共振条件**：除 Eq. (39) 外还需 $\tfrac32\xi_F\pi-\tfrac{\pi}{4}\tfrac{\Phi}{\Phi_0}=(2m+1)\tfrac\pi2$（Eq. 40）→ $\Phi/\Phi_0$ 整数时出现**尖锐电导峰** 📜Q。由单三角形绕行传播子 $P_1,P_2$ 求和 $\sum_n P_j^n=(1-P_j)^{-1}$（Eq. 41）发散解释；满足 Eq. (39)(40) 时解析 $T=\tfrac{1250+2P_R\{475+P_R[147+2P_R(13+P_R)]\}}{[25+P_R(9+P_R)]^2}$（Eq. 42）📜Q。

### 2.5 推导层：自旋极化

- 自旋分辨透射 $T_{n\sigma,m\sigma'}^\nu$；时间反演给 $T_{n\sigma,m\sigma'}^K(\Phi)=T_{m\sigma',n\sigma}^K(-\Phi)$（Eq. 45）、互易关系 $G_{RL}(\Phi)=G_{LR}(-\Phi)$（Eq. 48）📜Q。
- 自旋极化定义（Eq. 50–52）：$P_x+iP_y=\tfrac2T\sum_{\nu}\sum_{i,j,\sigma'}t_{i\downarrow,j\sigma'}^\nu t_{i\uparrow,j\sigma'}^{\nu*}$、$P_z=\tfrac1T\sum_\nu(T_{\uparrow\uparrow}^\nu+T_{\uparrow\downarrow}^\nu-T_{\downarrow\downarrow}^\nu-T_{\downarrow\uparrow}^\nu)$、$P=\sqrt{P_x^2+P_y^2+P_z^2}$ 📜Q。$\alpha\to0$ 恢复无自旋极限 $P=0$；对称性 $P_{x,y}(\alpha)=-P_{x,y}(-\alpha)$、$P_z(\alpha)=P_z(-\alpha)$（Eq. 53）📜Q。**数值上 $P$ 最高 $\approx0.9$**，随各参数噪声式变化，$\Phi/\Phi_0=8$ 周期 📜Q。

---

## 3. 结论清单（分层）

### 3.1 定理式主张（模型/对称性产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| $S_0$ 形式 | $2\times2$ 幺正对称矩阵（Eq. 4） | A1 |
| 能隙闭合条件 | $P_R=1/[4\cos^2\phi]$（$\Gamma$）、$1/[4\cos^2(\phi\pm2\pi/3)]$（$K,K'$）、$P_R=1/3,\phi=\pm\pi/6$ 同时 | A1 |
| 周期减半 | $\alpha=2n+1$ → $\Phi/\Phi_0=8\to4$ | A6 |
| 互易关系 | $G_{RL}(\Phi)=G_{LR}(-\Phi)$ | 时间反演 |

### 3.2 估算

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 无量纲 SOC | $\alpha\approx0.7$（$\alpha_R\approx15$ meV、$l\sim100$ nm、$v_F\approx10^6$ m/s） | A4 | 📜Q[~] |
| 磁电导周期 | $\Phi/\Phi_0=8$（$\alpha=0$）、$4$（$\alpha=1$） | A6 | 📜Q[~] |
| 自旋极化 | 最高 $P\approx0.9$ | A3 | 📜Q[~]（数值，读图 [读图]） |
| 共振解析透射 | $T=\tfrac{1250+2P_R\{475+P_R[147+2P_R(13+P_R)]\}}{[25+P_R(9+P_R)]^2}$ | Eq. 39+40 | 📜Q[~] |

### 3.3 预言（待实验验证）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| SOC 局域化效应（能带扁平 + 电导下降） | "we find" 📜Q | 中——磁输运 |
| 几何相关尖锐共振（自旋翻转节点间） | "we find" 📜Q | 中——电导峰 |
| 磁电导周期缩减 $8\to4$ | "the periodicity … is reduced to" 📜Q | 中——AB/AC 振荡 |
| 有限电导自旋极化（spintronics） | "could be exploited" 📜Q | 弱——自旋分辨探测 |

### 3.4 内部验证 + "没写什么"

1. **极限对照**：$\alpha\to0$ 恢复无 SOC 结果（周期 $8\Phi_0$、$P=0$）📜Q；$P_R\to1(0)$ 平带与能带闭合位置互验 📜Q。
2. **⚠️ 未用**：无内禀 SOC、无 QSH/$Z_2$、无自旋 Chern 数（grep `QSH`=0、`intrinsic`=0）；旧 review 这些表述无源已删。

---

## 4. 假设-结论依赖图

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性 |
|---|---|---|---|
| A5 仅 Rashba | 引入内禀/谷-Zeeman SOC | 周期减半条件、共振谱、自旋极化结构改变 | 边界——作者限定 |
| A6 几何相位近似 | 高阶 SOC / 大 $\alpha$ | $M(\theta)$ 形式、Eq. 39 精确性 | 部分 |
| A2 单谷单模 | 变成三角网络（双模） | $G_0=e^2/h$ → $4e^2/h$；能带/周期改 | 边界（Kagome 特有） |
| A3 节点自旋无关 | 节点自旋相关散射 | 自旋极化 $P$ 定量 | 简化 |
| A1 唯象模型 | 微观谱偏离 | 能带定量 | 基础 |

---

## 5. 接口（可检验性 / 设计原则 / 后续文献修正）

### 5.1 可检验性

磁电导周期（$\Phi/\Phi_0=8\to4$）、尖锐共振峰、自旋极化 $P$、Hofstadter 图案随 $\alpha$ 畸变 📜Q。作者建议：周期应变场石墨烯 + WSe₂ 衬底（诱导 SOC）体系可同时观测 AB 共振与 SOC 效应 📜Q。

### 5.2 设计原则

Kagome 几何（60° vs 120° 重叠不对称 → $P_R>P_L$）+ Rashba 强度 $\alpha$ 作自旋电子学旋钮；$\alpha=2n+1$ 共振点是设计目标 📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- **T25 Wittig 2023（同组）**：本文的方法前身（三角网络 + 能量依赖 $S$），本文推广到 Kagome + SOC 💭I。
- ⚠️ 旧 review "与 Barrier 2024 (E16) 互补""实现拓扑超导路线"为 review 层综合（原文未提 Barrier）→ 已移出正文。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| SOC 强度由衬底决定 | 实验上不可独立调控 | 📜Q（"one could increase it through proximity to a substrate"） |
| 仅单粒子 SOC | 多体效应（自旋液体等）未涉及 | 💭I（原文未讨论） |
| 节点 $S$ 自旋无关 | 简化假设 | 📜Q |
| 真实 mTBG 无序掩盖 | SOC 效应可能被无序淹没 | 💭I（review 层，原文未定量） |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| San-Jose & Prada 2013 (ref 15) / Efimkin 2018 (ref 16) / De Beule 2020-2021 (refs 41–43) | 引用——三角手征网络散射模型方法来源 📜Q |
| 双对准石墨烯-hBN (refs 37,38)、周期应变石墨烯 (ref 39) | 引用——Kagome 网络的实验/理论实现体系 📜Q |
| Chalker-Coddington 1988 (ref 40) | 引用——散射网络模型类比来源 📜Q |
| 石墨烯/WSe₂ Rashba 测量 (ref 59) | 引用——$\alpha_R\approx15$ meV 来源 📜Q |

## 8. 对后续研究的影响

- 把唯象散射网络方法从三角推广到 **Kagome 几何 + 自旋**，扩展方法工具箱 📜Q。
- 揭示"几何 + Rashba → 非 Abel 相位干涉（Aharonov-Casher）"的自旋电子学通道 📜Q。
- 提供 $P$ 最高 $\approx0.9$ 的自旋极化定量预言，供自旋分辨输运对标 📜Q。

## 9. 理论模型映射（供计算对标）

| 映射 | 说明 |
|------|------|
| Kagome 几何 → $S_\triangle$ | 单三角形收缩为能量依赖节点（Eq. 7），TBPM/TB 网络模型可复用 |
| Rashba $\alpha$ → 几何相位 | $\alpha=\alpha_R l/(\pi\hbar v_F)$，SOC 作自旋依赖 Peierls 相位 |
| 周期 $8\to4$ | 磁导周期是 $\alpha=2n+1$ 的诊断量 |
| 自旋极化 $P$ | 自旋分辨透射 → 自旋电子学器件设计指标 |

## Phase S 目的接口（引用式）

- **Q1（edge state 如何表征）**：本文给**输运 + 自旋特征**——磁电导周期缩减（$8\to4$）、尖锐共振、有限自旋极化 $P$ 📜Q。
- **Q2（理论如何解释）**：Rashba SOC → 自旋依赖动量平移 → 几何相位 → 非 Abel 干涉 → 局域化 + 周期缩减 + 自旋极化 📜Q。
- **Q3（理论↔实验对应）**：$\alpha_R\approx15$ meV（WSe₂）↔ 周期应变石墨烯/WSe₂ 器件；磁电导周期与共振 ↔ AB 输运；$P$ ↔ 自旋分辨测量 📜Q。

> **增量价值**：与 T25 同方法谱系；本文贡献"Kagome + SOC"推广。$G_0=e^2/h$（Kagome 单谷单模）区别于 T25 的 $4e^2/h$，注意不可混用。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取到 `/tmp/T30.txt`，grep 核对：**全部数字命中原文**——$\alpha_R\approx15$ meV、$l\sim100$ nm、$v_F\approx10^6$ m/s、$\alpha\approx0.7$、$G_0=e^2/h$、$\Phi/\Phi_0=8$（$\alpha=0$）、$4$（$\alpha=1$）、$P\approx0.9$、$P_R=1/4$、$1/[4\cos^2\phi]$、$P_R=1/3,\phi=\pm\pi/6$、$A=\sqrt3l^2/2$、$A_\triangle=\sqrt3l^2/16$、$A_\text{hex}=3\sqrt3l^2/8$。

⚠️ 修正/降级：① arXiv 2403.10181 正文未出现 → 标"外部来源"；② 旧 review "QSH 绝缘体/$Z_2$=1/自旋-谷锁定/$\lambda_I\sim1$–5 meV/自旋 Chern 数/$\lambda_I$-$\lambda_R$ 相图"原文均无（grep `QSH`=0、`intrinsic`=0）→ 已删；③ $P\approx0.9$ 为数值图读出 → 标 [读图]；④ 未引入 $4e^2/h$（本文 $G_0=e^2/h$）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-11 | 初读（Phase 4 粗读）。 |
| 2026-08-20 | S-REV 机制重写：删旧版"QSH 绝缘体/自旋-谷锁定/λ_I~1–5 meV/自旋 Chern 数"（无源）；改为原文（仅 Rashba SOC → 磁电导周期缩减 + 尖锐共振 + 电导自旋极化）；补 $\alpha_R\approx15$ meV。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（旧版归档 `archive/paper_review_T30_wittig2024_prb.backup_20260908.md`）：补参数分册/假设清单/推导链（Kagome→三角映射、Rashba 几何相位、周期减半 Eq. 39）/结论分层/假设-结论依赖图/接口；明确 $G_0=e^2/h$（非 $4e^2/h$）；$P\approx0.9$ 标 [读图]。 |
