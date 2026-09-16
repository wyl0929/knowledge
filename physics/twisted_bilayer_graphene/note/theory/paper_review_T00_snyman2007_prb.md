<!--
 * @Author       : AI 精读 (白箱演绎结构)
 * @Date         : 2026-09-09
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T00_snyman2007_prb.md
 * @Description  : T0: Snyman & Beenakker 2007 PRB — Bernal 双层石墨烯弹道输运 + 散粒噪声（赝扩散 F=1/3 的单层→双层推广；4×4 哈密顿量 + 层间耦合长度 l⊥ 的输运奠基）
-->

# Paper Review: Snyman & Beenakker (2007) — 双层石墨烯弹道输运与赝扩散

| 字段 | 内容 |
|------|------|
| **编号** | T0（谱系奠基；文件/index 用 `T00` 与 T01–T39 排序对齐） |
| **标题** | Ballistic transmission through a graphene bilayer |
| **作者** | I. Snyman, C. W. J. Beenakker |
| **期刊** | Physical Review B 75, 045322 (2007)（received 11 Sep 2006; revised 17 Oct 2006; published 12 Jan 2007） |
| **DOI / arXiv** | 10.1103/PhysRevB.75.045322（正文无 arXiv 号） |
| **类型** | 理论 — 解析 + 数值计算（界面波函数匹配 → Landauer-Büttiker 电导/散粒噪声），无实验数据 |
| **课题组** | Instituut-Lorentz, Universiteit Leiden（Beenakker 组） |
| **PDF / SI** | ✅ `reference/pdfs/Snyman和Beenakker - 2007 - Ballistic transmission through a graphene bilayer.pdf`（6 页，无 SI，含 Appendix A/B） |
| **精读日期** | 2026-09-09 |

> **结构说明**：本篇按「理论论文演绎结构」的五块记（见 `note/shared/method/theory_paper_reading.md` §3）：**① 模型白箱 → ② 推导链 → ③ 结论清单（分层）→ ④ 假设-结论依赖图 → ⑤ 接口**。理论论文无黑箱、无反推、无可辨识实验（"白箱演绎"而非"黑箱溯因"），故不用"四层变量表 + 判别表"这套实验框架词汇。
> **共享知识引用**：通用物理（Landauer-Büttiker 散射图景）见 `note/shared/physics/10_landauer_buttiker.md` `[PHY-LB]`；本文是 Bernal（非扭角）双层，谱系连接见 §7/§9。
> **谱系定位**：本文是 T 系列最早的"双层石墨烯哈密顿量 + 层间耦合长度 + 赝扩散输运"奠基论文——其 4×4 哈密顿量（Eq. 3）、层间耦合长度 $l_\perp=\hbar v/t_\perp$（Eq. 1）、2-band 约化（Eq. B1）是 T01（Martin 2008）、T05（San-Jose & Prada 2013）及整个 EFW/LSW/畴壁网络谱系的**共同构建块**。

---

## TL;DR

**本文想解决的理论问题**：未掺杂（狄拉克点）的 Bernal 双层石墨烯在弹道极限（无杂质、长度 $L\ll W$ 短宽条）下的（时间平均）电流与散粒噪声如何随费米能变化？层间耦合 $t_\perp$ 引入的新长度尺度（层间耦合长度 $l_\perp$）对狄拉克点的赝扩散输运有什么影响？

**主结果**：① 在狄拉克点，双层"如同一对独立的单层并联"（"transmits as two independent monolayers in parallel"）——电流与噪声都是单层的 2 倍，二者之比（Fano 因子）仍取 $F=1/3$，与单层、与扩散金属同值 📜Q；② 赝扩散成立的费米能窗口宽度 $\Delta E_F=2\varepsilon_{res}^{(1)}=2\pi^2\hbar v l_\perp/L^2$（正文引言/结论用量级式 $\Delta E_F\approx\hbar v l_\perp/L^2$），比单层窄一个因子 $l_\perp/L$ 📜Q；③ 与 Katsnelson 的 2-band 结果（$\sigma=G_0/2$、$F=1-2/\pi$，$t_\perp\to\infty$ 极限）对比：本文保留 4-band 有限 $t_\perp$，在 $U_\infty\gg t_\perp$ 极限得 $\sigma=2G_0/\pi$（推导，$\sigma=GL/W$）与 $F=1/3$，两者在 $U_\infty/t_\perp\approx0.2$ 处相交、无平台 📜Q。

**结论/意义**：把 Tworzydło 单层的赝扩散输运（$F=1/3$）**推广到双层**——无杂质、无晶格缺陷仍出现扩散型散粒噪声；但 $l_\perp\approx1.5$ nm 使该共振在 μm 级样品（Novoselov 2006）中不可分辨，需 10–100 nm 级结才能观测（作者 "should make it possible to resolve" = 预言）📜Q。⚠️ 全文为解析/数值结果，作者用词 demonstrate/find/believe/should，**非实验证实**。

---

## 1. 模型白箱（理想系统 + 假设清单）

> 理论论文的研究对象是**白箱**——作者自写的理想模型，无需"反推内部"。本节只做两件事：**写下模型**（§1.1–1.2），**列出它成立的全部假设**（§1.3）。假设清单是本文一切结论的"前提集合"，§4 的依赖图据此展开。

### 1.1 哈密顿量（单谷、单自旋）

写在 $(A_1,B_1,B_2,A_2)$ 基（下标 = 层，$A/B$ = 子格）下的 $4\times4$ 显式矩阵（原文 Eq. (3)）：

$$
H=\begin{pmatrix}
U & v(p_x+ip_y) & t_\perp & 0\\
v(p_x-ip_y) & U & 0 & 0\\
t_\perp & 0 & U & v(p_x-ip_y)\\
0 & 0 & v(p_x+ip_y) & U
\end{pmatrix}\qquad(3)
$$

📜Q（原文 Eq. (3)；`pdftotext -layout` + `-raw` 复核各元素：对角全 $U$、次对角 $(1,2)=(3,4)=v(p_x+ip_y)$、$(2,1)=(4,3)=v(p_x-ip_y)$、层间耦合 $(1,3)=(3,1)=t_\perp$）。$p=-i\hbar\nabla$ 为动量算符。哈密顿量作用在四分量旋量 $(\Psi_{A1},\Psi_{B1},\Psi_{B2},\Psi_{A2})$ 上 📜Q。

- **只含单谷、单自旋**：描述布里渊区中一个 Dirac 点附近的低能激发；"另一个 Dirac 点和自旋自由度对电流与噪声贡献一个 4 重简并因子"（$2$ 谷 $\times2$ 自旋 $=4$，吸收进 $G_0=4e^2/h$）📜Q。
- **仅最近邻跃迁**：层内 $A\leftrightarrow B$，层间仅 $A_1\leftrightarrow B_2$（Bernal 堆叠二聚体；"同子格、不同层的位点不直接相邻"）📜Q。
- **层间耦合来源**：4×4 哈密顿量引自 Refs. 3–5（Wallace 1947 / McCann–Fal'ko 2006 / Nilsson 2006），$t_\perp\approx0.4$ eV 是层间最近邻跃迁 📜Q。

### 1.2 势、能谱与长度尺度

- **静电势剖面**（原文 Eq. (2)）：$U(x)=-U_\infty$（$x<0$ 或 $x>L$，重掺杂接触区）；$U(x)=0$（$0<x<L$，弱掺杂条）。用突变势阶，理由是"任何在小于 $L$ 距离上的平滑在狄拉克点附近（费米波长 $\gtrsim L$）变得无关" 📜Q。两层取**同一静电势** $U$（需顶/底双栅分别调到各自 Dirac 点）📜Q。
- **能谱**（原文 Eq. (4)，取 $\hbar v=1$ 单位，$k=|\mathbf k|$）：四支双曲线
  $$\varepsilon=\pm\tfrac12 t_\perp\pm\sqrt{\tfrac14 t_\perp^2+k^2}\qquad(4a),\qquad
  \varepsilon=\mp\tfrac12 t_\perp\pm\sqrt{\tfrac14 t_\perp^2+k^2}\qquad(4b)$$
  两支低能带在 Dirac 点（$\varepsilon=0,k=0$）相触，两支高能带在 $\pm t_\perp$ 处（Fig. 2）📜Q。
- **层间耦合长度**（原文 Eq. (1)）：
  $$l_\perp=\frac{\hbar v}{t_\perp}=\frac{3t_\parallel}{2t_\perp}\,d\approx11\,d\qquad(1)$$
  用 $v\approx10^6$ m/s、$d\approx1.4$ Å、$t_\parallel\approx3$ eV（层内最近邻跃迁）、$t_\perp\approx0.4$ eV（层间）📜Q；结论处 $l_\perp\approx1.5$ nm 📜Q。$l_\perp$ 比层内原子间距大一个量级；由于 $L\gg l_\perp$，两层强耦合 📜Q。

### 1.3 参数分册（区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $E_F$（费米能，扫谱）、$U_\infty$（接触区势，Sec. V 扫轴）、$L$（条长）、$k_y$（横向动量） |
| **导出量（由旋钮+常数算出）** | $l_\perp=\hbar v/t_\perp\approx11d$、$k_c=(1/L)\ln[L/2l_\perp+\sqrt{1+L^2/4l_\perp^2}]$、纵向动量 $k_x^{\pm}$、共振位置 $\varepsilon_{res}^{(n)}$ |
| **模型内部量（解的性质）** | 能谱 $\varepsilon(k)$、透射本征值 $T_\pm$、透射矩阵 $t$、电导 $G$、噪声功率 $P$、Fano 因子 $F$ |
| **固定常数** | $v\approx10^6$ m/s、$d\approx1.4$ Å、$t_\parallel\approx3$ eV、$t_\perp\approx0.4$ eV、$G_0=4e^2/h$、$P_0=2e|V|G_0$ |
| **预言量（可检验）** | 狄拉克点 $F=1/3$、$G=2G_0W/(\pi L)$、共振窗口 $\Delta E_F\approx\hbar v l_\perp/L^2$ |

> 无"反推量 θ̂"层——理论论文不反推自数据（见 methodology §4.0）。**符号防混**：$l_\perp$（层间耦合长度 ≈1.5 nm）≠ $t_\perp$（层间跃迁 ≈0.4 eV）；$l_\perp$ 与 $L$（条长）是两个不同长度。

### 1.4 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **弹道**（无杂质、无晶格缺陷，"impurity-free"） | 模型 | 📜Q（摘要/结论） |
| A2 | **短宽几何** $L\ll W$（$y$ 方向边界条件无关，取周期边界 $k_{y,n}=2\pi n/W$） | 模型 | 📜Q |
| A3 | **两层同一静电势** $U$（都调到各自 Dirac 点，需顶/底双栅） | 模型 | 📜Q |
| A4 | **仅最近邻跃迁** | 模型 | 📜Q |
| A5 | **单谷 + 自旋简并**（4 重简并因子并入 $G_0$） | 模型 | 📜Q |
| A6 | **突变势阶**（平滑在 $L$ 尺度上无关） | 模型 | 📜Q |
| A7 | **$U_\infty\gg t_\perp$**（接触区强耦合、接触无关极限，Eq. (15)–(19) 成立域） | 推导 | 📜Q |
| A8 | **低温/小偏压**（Landauer-Büttiker + 散粒噪声定义） | 推导 | 💭I（原文未显式声明温度，但散粒噪声框架隐含） |

> 判别性扫轴：$E_F$ 轴（绕 Dirac 点，Fig. 3/5）、$U_\infty/t_\perp$ 轴（Sec. V，Fig. 6/7）、$k_y$ 轴（Fig. 3/4）📜Q。这些假设在 §4 逐一映射到"失效 → 结论崩塌"。

---

## 2. 推导链（演绎结构：顺论文顺序，每步"输入→输出→所用假设/定理→合法域"）

### 2.0 总览：论文五节是一条演绎链

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | I 引言（继承 Ref. 1） | 单层赝扩散 $F=1/3$ | 本文的对照基准 | Tworzydło 2006 | 单层 |
| 模型层 | II Model | 4×4 哈密顿量 + 参数 | 能谱（4 支）+ $l_\perp$ | A1–A6 | 低能连续、Bernal |
| 推导层 | III–IV Transmission/Results | 界面波函数匹配 → $t$ → $T_\pm$ | $G,P,F$（Eq. 17–19）+ 共振窗口（Eq. 20） | A7（$U_\infty\gg t_\perp$） | 狄拉克点附近 |
| 边界层 | V 接触区势 + App. B | 有限 $U_\infty$、2-band 约化 | 接触无关极限判据 + Katsnelson 对照 | 2-band 近似 | $U_\infty\lesssim t_\perp$、$t_\perp\to\infty$ |

### 2.1 前提定理层：单层赝扩散（继承 Ref. 1，不重推）

Tworzydło 等（Ref. 1）发现：未掺杂单层的 evanescent 模式（衰减 $\propto e^{-L/\xi}$，穿透深度 $\xi$ 上界为宽度 $W$）产生**赝扩散**散粒噪声——Fano 因子 $F=P/2e\bar I=1/3$，与扩散金属同值（而独立电流脉冲 $F=1$）📜Q。这是本文双层计算的对照基准。

### 2.2 模型层：4×4 哈密顿量 → 能谱

输入 4×4 哈密顿量（Eq. 3）+ 势剖面（Eq. 2），输出四支双曲线能谱（Eq. 4，Fig. 2）：两支低能带在 Dirac 点相触、两支高能带在 $\pm t_\perp$。关键新尺度 $l_\perp=\hbar v/t_\perp$（Eq. 1）进入，双层比单层多一个长度尺度 📜Q。

### 2.3 推导层：界面匹配 → 透射本征值 → $G/P/F$

1. **Landauer-Büttiker 公式**（Eq. 5–6）：$G=G_0\operatorname{Tr}tt^\dagger$，$P=P_0\operatorname{Tr}[tt^\dagger(1-tt^\dagger)]$，$F=\operatorname{Tr}[tt^\dagger(1-tt^\dagger)]/\operatorname{Tr}tt^\dagger$，$G_0=4e^2/h$、$P_0=2e|V|G_0$ 📜Q。背景锚点 `[PHY-LB]`。
2. **界面匹配**：在 $x=0,L$ 匹配本征态。与非相对论矩形势垒散射的**两点差异**：① 哈密顿量是一阶微分算符 → 只有波函数（非导数）连续；② 能谱同时含正、负能量本征态 📜Q。纵向动量 $k_x^\pm=\sqrt{(\varepsilon\pm t_\perp/2)^2-t_\perp^2/4-k_y^2}$（Eq. 7，根号取 $[0,\pi)$ 幅角）；每个实 $k_x^+$ 有 2 个传播模式、每个实 $k_x^-$ 再有 2 个 📜Q。
3. **短宽极限 $L\ll W$**：迹→积分 $\operatorname{Tr}(tt^\dagger)^p\to\frac{W}{\pi}\int_0^\infty dk_y\sum_{\sigma=\pm}[T_\sigma(E_F,k_y)]^p$（Eq. 13），$T_\pm$ 是 $tt^\dagger$ 的两个本征值 📜Q。
4. **共振位置**（Eq. 14，由 $k_xL/\pi=n$ 整数估算）：$\varepsilon_{res}^{(n)}(k_y)=\mp\tfrac12 t_\perp\pm\sqrt{\tfrac14 t_\perp^2+(\pi n/L)^2+k_y^2}$ 📜Q。在 $|k_y|\ll1/L$ 与 $|k_y|\gg1/L$ 处与数值吻合好，$|k_yL|\approx1$ 交叉；区域 (c)/(d) 中 $k_x$ 虚 → 透射降为零 📜Q。
5. **狄拉克点精确解**（$\varepsilon=0$，$U_\infty\to\infty$，Eq. 15）：$T_\pm(\varepsilon=0,k_y)=1/\cosh^2[(k_y\mp k_c)L]$，$k_c=\frac1L\ln\!\big[\frac{L}{2l_\perp}+\sqrt{1+\frac{L^2}{4l_\perp^2}}\big]$（Eq. 16）📜Q。计算细节在 Appendix A（8×8 匹配 + $z=e^{k_yL}$ 缩写）。
6. **关键洞察——"位移副本"**：$T_\pm$ 是单层 $T_\text{monolayer}(0,k_y)=1/\cosh^2(k_yL)$（Refs. 1,10）沿 $k_y$ 位移 $\mp k_c$ 的副本（Fig. 4）📜Q。→ 任意形如 $A=\operatorname{Tr}f(tt^\dagger)$ 的可观测量（$f$ 任意函数）在双层都是单层的 2 倍 📜Q。
7. **代入得主结果**（Eq. 17–19）：
   $$G_\text{bilayer}=2G_\text{monolayer}=\frac{2G_0W}{\pi L}\quad(17),\qquad
   P_\text{bilayer}=2P_\text{monolayer}=\frac{4e|V|G_0W}{3\pi L}\quad(18),\qquad
   F_\text{bilayer}=F_\text{monolayer}=\tfrac13\quad(19)$$
   📜Q。离开狄拉克点：法向入射共振 $\varepsilon_{res}^{(n)}(0)=\pm(\pi^2\hbar v l_\perp/L^2)n+O((l_\perp/L)^3)$（Eq. 20），窗口 $\Delta E_F=2\varepsilon_{res}^{(1)}=2\pi^2\hbar v l_\perp/L^2$ 比单层窄 $l_\perp/L$ 倍 📜Q。

### 2.4 边界层：有限 $U_\infty$ 与 2-band 约化

- **接触无关极限判据**（Sec. V）：$U_\infty\gg t_\perp$ 是"正常金属接触"模型（对各层两个子格等耦合）的合适区 📜Q。$U_\infty>t_\perp$ 时每条 $(\varepsilon,k_y)$ 有 2 个左入射传播模式；$U_\infty<t_\perp$ 时一个模式变 evanescent → 电导/Fano 突变 📜Q。$U_\infty-t_\perp\gtrsim\hbar v/L$ 时几乎到达 $U_\infty\to\infty$ 极限；$U_\infty\lesssim t_\perp$ 时电导更小、Fano 更大；当接触区费米动量 $\sqrt{U_\infty t_\perp}/v$ 降到 $\hbar/L$ 以下时两者都消失（接触耗尽）📜Q。
- **Katsnelson 对照**（Ref. 12）：Katsnelson 在 $\hbar v/L\ll\sqrt{U_\infty t_\perp}\ll t_\perp$ 区得到 $\sigma=G_0/2$、$F=1-2/\pi$ 📜Q。本文曲线与之交点位于 $U_\infty/t_\perp\approx0.2$（Fig. 6/7 参数 $U_\infty=0.2t_\perp$、$L=100l_\perp$）📜Q；交点随 $L$ 增大趋近 $U_\infty=0$、**无平台**，且（App. B）交点不对应 $E_F$ 的极值 → 难以从测量提取 📜Q。
- **4-band vs 2-band（App. B）**：Katsnelson 一开始取 $t_\perp\to\infty$，把 4×4 约化成 2×2 有效哈密顿量（Eq. B1）：
  $$H_\text{eff}=-\frac{v^2}{t_\perp}\begin{pmatrix}0&(p_x-ip_y)^2\\(p_x+ip_y)^2&0\end{pmatrix}+U(x)\begin{pmatrix}1&0\\0&1\end{pmatrix}\qquad(B1)$$
  仅保留 Dirac 点附近两支最低能带（适用 $U_\infty\ll t_\perp$）📜Q。本文用两套哈密顿量在交点参数处重算，结果一致（Fig. 7）→ 与 Katsnelson 的差异**不是**哈密顿量选择导致 📜Q。

  > 此 Eq. (B1)（无偏压 2-band 约化，二次手征项）加层间偏压 $\pm U/2$ 即 Martin 2008 的 two-component 哈密顿量；由此推 kink 零模衰减 $\lambda=\sqrt{U\gamma_\perp}/(2\hbar v_F)$ → T05 San-Jose 的 TPH 网络判据 Eq.(1)。完整推导见 `note/shared/physics/11_bilayer_two_component_kink.md` `[PHY-2BAND]`。作者 "believe" Ref. 12 描述的是 $L/l_\perp\to\infty$ 在 $E_F\equiv0$ 的渐近极限，但该极限下窗口 $\Delta E_F\approx\hbar v l_\perp/L^2\to0$，"seems unobservable" 📜Q。

---

## 3. 结论清单（分层：定理式主张 / 估算 / 预言）

> 理论论文的结论必须按**性质**分层。每条标：**依赖假设** + **可检验性**。保留作者动词强度（demonstrate/find/believe/should）。

### 3.1 定理式主张（解析推导的产物，依赖 A7 $U_\infty\gg t_\perp$）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 狄拉克点透射本征值 | $T_\pm(0,k_y)=1/\cosh^2[(k_y\mp k_c)L]$（$U_\infty\to\infty$ 精确式，Eq. 15） | A1–A7 |
| 位移副本 → 2 倍关系 | 双层 $T_\pm$ = 单层 $T$ 的 $\mp k_c$ 位移副本 → $A=\operatorname{Tr}f(tt^\dagger)$ 双层 $=2\times$ 单层 | A7 |
| $G,P,F$ | $G=2G_0W/(\pi L)$、$P=4e|V|G_0W/(3\pi L)$、$F=1/3$（Eq. 17–19） | A1–A7 |

⚠️ 本文**未**讨论量子化电导平台、**未**引入畴壁/拓扑/谷 Chern 等概念——结论是**体弹道输运**的 $G,P,F$，不是边缘态电导（防跨论文迁移）。

### 3.2 估算（经验/近似判据，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 层间耦合长度 | $l_\perp=\hbar v/t_\perp=(3t_\parallel/2t_\perp)d\approx11d\approx1.5$ nm | 参数值 | 📜Q[~] |
| 共振位置 | $\varepsilon_{res}^{(n)}(k_y)$（Eq. 14，$k_xL/\pi=n$ 整数估算） | 相位条件 | 📜Q[~] |
| 共振窗口（精确） | $\Delta E_F=2\varepsilon_{res}^{(1)}=2\pi^2\hbar v l_\perp/L^2$（Eq. 20 + Sec. IV） | A7 | 📜Q[~] |
| 共振窗口（量级） | $\Delta E_F\approx\hbar v l_\perp/L^2$（引言/结论的量级式） | 同上 | 📜Q[~] |
| 窗口比单层窄 | 因子 $l_\perp/L$ | — | 📜Q |

### 3.3 预言（可检验性 → 见 §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 双层在狄拉克点仍赝扩散（$F=1/3$、$G=2G_0W/\pi L$） | "we have demonstrated / we calculate"（解析+数值构造）📜Q | 中——弹道双层结输运 + 散粒噪声 |
| 10–100 nm 结可分辨 evanescent 共振、观测赝扩散 | "should make it possible to resolve" 📜Q | 中——需短结 |
| Ref. 12（Katsnelson 2-band）是 $L/l_\perp\to\infty$ 渐近极限且不可观测 | "We do believe ... seems unobservable" 📜Q | 弱——渐近极限判定 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

1. **解析↔数值互验**：共振位置 Eq. (14)（$k_xL/\pi=n$ 估算）与 Fig. 3 灰阶图的共振线在 $|k_y|\ll1/L$、$|k_y|\gg1/L$ 两区"good agreement"，$|k_yL|\approx1$ 交叉 📜Q。
2. **4-band↔2-band 互验**：交点参数处两套哈密顿量结果一致（Fig. 7）→ 差异非哈密顿量选择 📜Q。
3. **极限对照**：有限 $U_\infty$（Fig. 6）在 $U_\infty-t_\perp\gtrsim\hbar v/L$ 收敛到 $U_\infty\to\infty$ 极限；$U_\infty\lesssim t_\perp$ 偏离 📜Q。
4. **与已知结果核对**：平均电流/电导与 Cserti（Ref. 7）一致；与 Koshino-Ando（Ref. 8）、Nilsson（Ref. 9）弱无序结果**不同**（本文弹道，后两者弱无序）📜Q。

### 3.5 概念区分（作者论证中的"分类"）

| 区分 | 依据 | 结论 |
|---|---|---|
| 单层 vs 双层 | 双层多一个长度尺度 $l_\perp$（比 $d$ 大一个量级）📜Q | 狄拉克点同行为、离狄拉克点很不同 |
| 4-band vs 2-band | 有限 $t_\perp$ vs $t_\perp\to\infty$（Eq. B1）📜Q | $U_\infty\lesssim t_\perp$ 才需 2-band |
| 赝扩散 vs 真扩散 | $F=1/3$ 同值，但来源是弹道 evanescent 模式（非杂质散射）📜Q | 无杂质仍有扩散型噪声 |
| 弹道 vs 弱无序 | 本文 impurity-free vs Refs. 8,9 weakly disordered 📜Q | 结果不同（§3.4-4） |

---

## 4. 假设-结论依赖图（含金量所在）

> 理论论文三个月后最可能被引用的是"何时失效"，不是推导本身。本表把 §1.4 的每条假设映射到"失效方式 → 崩塌的结论"。

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A1 弹道（无杂质/缺陷） | 引入杂质散射 | 赝扩散 $F=1/3$ 不再普适（与 Refs. 8,9 弱无序结果不同）📜Q | 结论限弹道；作者已与弱无序文献区分 |
| A7 $U_\infty\gg t_\perp$ | $U_\infty\lesssim t_\perp$ | Eq. (15)–(19) 失效；电导更小、Fano 更大；$U_\infty$ 降至接触耗尽（$\sqrt{U_\infty t_\perp}/v<\hbar/L$）时两者消失 📜Q | 作者在 Sec. V 显式处理有限 $U_\infty$ |
| A3 两层同一势 $U$ | 两层势不相等 | 无法同时调到各自 Dirac 点 → 狄拉克点共振不复现 | 作者声明需顶/底双栅 📜Q |
| A2 短宽 $L\ll W$ | $L\gtrsim W$ | 迹→积分（Eq. 13）失效，$y$ 方向离散性不可忽略 | 作者声明限 $L\ll W$ 📜Q |
| A4 仅最近邻跃迁 | 高阶跃迁 | 4×4 哈密顿量需修正 | 模型层固有近似（Refs. 3–5）📜Q |
| A5 单谷/自旋简并 | 谷间散射、自旋劈裂 | 4 重简并因子不成立 | 低能单谷描述固有（"smooth enough"）💭I |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- 弹道双层结的**最小电导**与 **Fano 因子**：狄拉克点 $G=2G_0W/(\pi L)$（→ $\sigma=2G_0/\pi$，推导）、$F=1/3$ 📜Q。
- **共振窗口** $\Delta E_F\approx\hbar v l_\perp/L^2$ 需 $L\sim10$–100 nm 才能分辨（$l_\perp\approx1.5$ nm 使 μm 级样品不可分辨）📜Q。
- Novoselov 2006（Ref. 11）单/双层 μm 样品**无定性差异**、都显示最小电导 $G_0$——与本文"$\Delta E_F$ 太窄不可分辨"自洽 📜Q。

### 5.2 设计原则（观测赝扩散的几何条件）

短结（$L$ 越小 $\Delta E_F\propto L^{-2}$ 越宽）+ 弹道（无杂质）+ 双栅（两层同调 Dirac 点）+ 大 $U_\infty$（$U_\infty-t_\perp\gtrsim\hbar v/L$）📜Q→💭I。

### 5.3 后续文献修正/承接（时间倒挂，💭I）

- **T01 Martin 2008**：同一 4×4 Bernal 哈密顿量 + $t_\perp$，但把静电势从"均匀/突变势阶"改为"符号反转偏压 kink"，约化到 2-band 二次色散用于畴壁零模——本文的 Eq. (B1) 就是 Martin 2008 的 2-band 约化的先行者。
- **T05 San-Jose & Prada 2013**：直接沿用 $l_\perp=\hbar v/\gamma_\perp$（$\gamma_\perp\equiv t_\perp$）作层间耦合长度，用于 mTBG 畴壁网络判据 Eq. (1)。
- **Tworzydło 2006（Ref. 1）**：本文的单层对照与直接前驱。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 弹道假设 | 无杂质/缺陷；弱无序结果不同（Refs. 8,9） | 📜Q |
| 突变势阶 | 平滑势仅"在 Dirac 点附近无关"论证，未定量 | 📜Q |
| 两层同一势 | 需顶/底双栅，实际势不相等（Refs. 13,14） | 📜Q |
| 温度/退相干 | 未显式讨论温度；散粒噪声为低温框架 | 💭I |
| $t_\perp$ 数值不确定 | "此 $\gamma_1$ 值是石墨的值；双层的值尚不知道"（footnote 6） | 📜Q |
| Katsnelson 渐近极限 | 窗口 $\to0$ "seems unobservable"，只能作极限论证 | 📜Q |

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）

| 工作 | 关系 |
|------|------|
| Tworzydło et al. PRL 96, 246802 (2006) (Ref. 1) | **直接前驱**——单层赝扩散 $F=1/3$，本文的双层对照基准 📜Q |
| McCann & Fal'ko PRL 96, 086805 (2006) (Ref. 4)；Nilsson et al. PRB 73, 214418 (2006) (Ref. 5) | **哈密顿量来源**——4×4 双层哈密顿量（Eq. 3）与 $l_\perp$ 引自 Refs. 3–5 📜Q |
| Cserti cond-mat/0608219 (Ref. 7) | 平均电流/电导**一致** 📜Q |
| Koshino & Ando PRB 73, 245403 (2006) (Ref. 8)；Nilsson cond-mat/0604106 (Ref. 9) | 弱无序结果**不同**（本文弹道）📜Q |
| Katsnelson EPJB 52, 151 (2006) (Ref. 12) | 2-band 结果（$\sigma=G_0/2$、$F=1-2/\pi$）=$L/l_\perp\to\infty$ 渐近极限；本文 4-band 与之在 $U_\infty/t_\perp\approx0.2$ 相交、无平台 📜Q |
| Novoselov et al. Nat. Phys. 2, 177 (2006) (Ref. 11) | 实验——单/双层最小电导 $G_0$ 无定性差异，与本文"μm 不可分辨"自洽 📜Q |

> ⚠️ Phase S 外部对标（**非本文引用**，时间倒挂，💭I）：T01 Martin 2008、T05 San-Jose 见 §5.3；本文是 Bernal（非扭角）双层，与 mTBG 畴壁网络的连接是"共享哈密顿量 + $l_\perp$ 构建块"，不是直接对象同一。

## 8. 对后续研究的影响

- 把赝扩散输运（$F=1/3$）从单层**推广到双层**，确立"无杂质仍扩散型噪声"的普适图景 📜Q。
- 固化**层间耦合长度 $l_\perp=\hbar v/t_\perp$** 为双层石墨烯的基本尺度，被 T01/T05 等沿用 📜Q→💭I。
- 提供 **2-band 约化**（Eq. B1）作为 $t_\perp\to\infty$ 极限的标准参考（App. B）📜Q。
- 给出可检验预言（10–100 nm 结分辨共振），为后续短结实验提供靶标 📜Q。

## 9. 理论模型映射（供计算对标）

| 映射 | 说明 |
|------|------|
| 4×4 哈密顿量（Eq. 3）→ 紧束缚 | Bernal 堆叠双层紧束缚模型的连续低能形式（$A_1\leftrightarrow B_2$ 二聚耦合 $t_\perp$）；与 T01/T05 的 4×4 哈密顿量**同源不同基**（基序 $A_1,B_1,B_2,A_2$）📜Q |
| $l_\perp=\hbar v/t_\perp$ → 长度标度 | 层间耦合长度的定义，$t_\perp\approx0.4$ eV → $l_\perp\approx1.5$ nm 📜Q |
| Eq. (B1) → 2-band 约化 | $H_\text{eff}=-(v^2/t_\perp)\begin{pmatrix}0&(p_x-ip_y)^2\\(p_x+ip_y)^2&0\end{pmatrix}+U$，二次色散低能带 📜Q |
| $T_\pm=1/\cosh^2[(k_y\mp k_c)L]$ → 透射 | Dirac 点 $U_\infty\to\infty$ 透射本征值，可作 Landauer/Fisher-Lee 计算的解析基准 📜Q |
| $F=1/3$、$G=2G_0W/(\pi L)$ → 输运 | 弹道双层赝扩散的定量预言，供散粒噪声计算对标 📜Q |

---

## Phase S 目的接口（引用式，随项目增删）

> 本文**不直接回答** Q1/Q2/Q3（edge state 表征/解释/映射）——研究对象是 Bernal 双层的**体弹道输运**，不是畴壁/边缘态。其角色是"**哈密顿量祖先**"：为 T 系列提供共用构建块。

- **Q2（理论如何解释）——间接**：本文的 4×4 Bernal 哈密顿量（Eq. 3）、层间耦合长度 $l_\perp=\hbar v/t_\perp$（Eq. 1）、2-band 约化（Eq. B1）是 EFW（T01）/LSW/畴壁网络（T05）理论的共同起点 📜Q；T05 的判据 Eq. (1) 直接借用 $l_\perp=\hbar v/\gamma_\perp$。
- **Q3（理论↔实验映射）——间接**：本文与 Novoselov 2006（Ref. 11）的"最小电导 $G_0$"实验对照，给出"μm 样品不可分辨、需 10–100 nm"的定标 📜Q。
- **增量价值**：比 T01/T05 多的 = 弹道体输运的 $G,P,F$ 定量结果（$F=1/3$、$2G_0W/\pi L$）+ $l_\perp$ 的原始定义 + 2-band 约化先行者；少的 = 无畴壁/拓扑/谷概念。三个月后最可能被引用的 = $l_\perp=\hbar v/t_\perp$ 定义与 Eq. (B1) 2-band 约化。

## 反向核对 pass (2026-09-09)

`pdftotext -layout` + `-raw` 提取正文到 `/tmp/snyman2007.txt`、`/tmp/snyman2007_raw.txt`，逐项 grep 核对：**全部数字命中原文**——

| 数字/公式 | grep 命中位置 | 结论 |
|-----------|--------------|------|
| $l_\perp=\hbar v/t_\perp=(3t_\parallel/2t_\perp)d\approx11d$ | Eq. (1) | ✓ 📜Q[~] |
| $v\approx10^6$ m/s、$d\approx1.4$ Å、$t_\parallel\approx3$ eV、$t_\perp\approx0.4$ eV | Eq. (1) 段 | ✓ 📜Q[~] |
| $l_\perp\approx1.5$ nm | 结论段 | ✓ 📜Q[~] |
| $F=1/3$、$G=2G_0W/(\pi L)$、$P=4e|V|G_0W/(3\pi L)$ | Eq. (17–19) | ✓ 📜Q |
| $G_0=4e^2/h$、$P_0=2e|V|G_0$ | Eq. (5) 段 | ✓ 📜Q |
| $T_\pm=1/\cosh^2[(k_y\mp k_c)L]$、$k_c$ 公式 | Eq. (15–16) | ✓ 📜Q |
| $\varepsilon_{res}^{(n)}(0)=\pm(\pi^2\hbar v l_\perp/L^2)n+O((l_\perp/L)^3)$ | Eq. (20) | ✓ 📜Q |
| $\Delta E_F=2\varepsilon_{res}^{(1)}=2\pi^2\hbar v l_\perp/L^2$ | Sec. IV | ✓ 📜Q |
| $\Delta E_F\approx\hbar v l_\perp/L^2$（量级式） | 引言 + 结论 | ✓ 📜Q |
| Katsnelson $\sigma=G_0/2$、$F=1-2/\pi$ | Sec. V | ✓ 📜Q |
| 交点 $U_\infty=0.2t_\perp$、$L=100l_\perp$ | Fig. 7 caption | ✓ 📜Q |
| Heff（Eq. B1）2-band 约化 | App. B | ✓ 📜Q |

⚠️ 修正/降级：① 电导率 $\sigma=2G_0/\pi$ 原文未显式写出——由 $\sigma=GL/W$（Fig. 5 caption）+ $G=2G_0W/(\pi L)$（Eq. 17）合成，标 [推导]；② $t_\perp$ 数值带 footnote 6 限定（"石墨的 $\gamma_1$ 值；双层的值尚不知道"），已记入 §6；③ 正文无 arXiv 号 → 头部表不写 arXiv。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-09-09 | **初读 + 按五块演绎结构建档**（作为谱系奠基 T0）：块1 模型白箱（4×4 哈密顿量 + $l_\perp$ + 8 条假设清单）→ 块2 推导链（前提定理/模型/推导/边界四层）→ 块3 结论清单（定理/估算/预言分层）→ 块4 假设-结论依赖图 → 块5 接口。全部 📜Q 数字/公式 `-layout`+`-raw` 双提取 grep 命中；$\sigma=2G_0/\pi$ 标 [推导]；$t_\perp$ footnote 限定记入局限。 |
