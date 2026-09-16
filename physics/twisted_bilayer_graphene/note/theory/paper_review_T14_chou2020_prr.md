<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4) → 2026-09-08 按 5 块演绎结构重写
 * @Date         : 2026-08-06（初读）→ 2026-09-08（5 块重写 + 反向核对）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T14_chou2020_prr.md
 * @Description  : T14: Chou, Wu & Das Sarma 2020 — mTBG 的 Hofstadter 蝴蝶与 Floquet 拓扑绝缘体（理论；2026-09-08 按五块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: Chou, Wu & Das Sarma (2020) — 最小扭角双层石墨烯中的 Hofstadter 蝴蝶与 Floquet 拓扑绝缘体

| 字段 | 内容 |
|------|------|
| **编号** | T14 |
| **标题** | Hofstadter butterfly and Floquet topological insulators in minimally twisted bilayer graphene |
| **作者** | Yang-Zhi Chou, Fengcheng Wu, Sankar Das Sarma |
| **期刊** | Physical Review Research 2, 033271 (2020) |
| **DOI / arXiv** | 10.1103/PhysRevResearch.2.033271 / arXiv:2004.15022（⚠️ arXiv 号正文未出现，标外部来源） |
| **类型** | 理论 — 网络模型 Hofstadter 谱 + Floquet 拓扑绝缘体（散射矩阵模型，无实验数据） |
| **课题组** | University of Maryland（Condensed Matter Theory Center / JQI） |
| **PDF** | ✅ `reference/pdfs/Chou 等 - 2020 - Hofstadter butterfly and Floquet topological insulators in minimally twisted bilayer graphene.pdf`（正文 9 页 + 3 附录） |
| **精读日期** | 2026-08-06（初读）→ 2026-09-08（5 块重写 + 反向核对） |

> **结构说明**：按「理论论文演绎结构」五块记（`note/shared/method/theory_paper_reading.md` §3）。**全文无 ±**：数字统一 📜Q[~]。

---

## TL;DR

**本文想解决的理论问题**：mTBG 三角网络模型在**外磁场**下的能谱（Hofstadter 蝴蝶）与拓扑性质是什么？能否在**平衡态**固体中实现 Floquet 拓扑绝缘体（FTI）？

**主结果**：① 弱磁场下 Dirac 点在有限场处**重入**（整数/分数 $1/\varphi$ 处），位置敏感依赖前向散射概率 $P_{a\bar a}$ → 可作为确定网络模型参数的实验指纹 📜Q；② 强磁场下左右偏转概率不对称（$\gamma\equiv P_{a\bar b}/P_{a\bar c}\neq1$）→ Dirac 点开隙 → mTBG 实现**零陈数 FTI**：体带陈数为零、但体隙中有手征边缘态穿越 📜Q；③ 拓扑不变量 $\nu=\pm1$（Floquet 缠绕数，非 Chern 数），由 Hofstadter 蝴蝶的非平凡谱流识别 + 显式边缘态计算证实 📜Q。

**结论/意义**：首次在**平衡态固体**（非周期驱动）中预言 FTI 的低能实现；给出"零陈数 + 手征边缘态"的新拓扑判据。⚠️ 全文为理论，作者用词 demonstrate / establish / predict / pave the way；FTI 需强磁场使 C2zT 破缺隙超过热/无序展宽。

---

## 1. 模型白箱（理想系统 + 假设清单）

### 1.1 模型（散射矩阵网络，每谷每自旋）

mTBG 三角网络：每条畴壁链长 $d$（= Moiré 周期），**每自旋每谷 2 条** 1D 通道 📜Q。忽略自旋；K、K′ 谷分别处理（体系在原子尺度光滑）；C2z 联系两谷 → 主要研究 K 谷；进一步假设 K 谷 2 条通道在畴壁与节点**解耦** → 单通道网络模型（ref 16）📜Q。

**散射矩阵**（$3\times3$ 幺正，由 C3z 与 C2zT 对称性决定，Eq. 1）：

$$
\hat S=\begin{pmatrix}\alpha&\zeta&\xi\\ \xi&\alpha&\zeta\\ \zeta&\xi&\alpha\end{pmatrix},\quad
\alpha=\sqrt{P_{a\bar a}},\ \zeta=e^{-i2\pi/3}\sqrt{P_{a\bar c}},\ \xi=e^{-i\pi/3}\sqrt{P_{a\bar b}}
$$

$P_{a\bar a}$ = 前向散射概率，$P_{a\bar b},P_{a\bar c}$ = 偏转散射概率；$P_{a\bar a}+P_{a\bar b}+P_{a\bar c}=1$，相位由幺正性约束 📜Q。**C2zT 要求 $\hat S=\hat S^\dagger$ → $P_{a\bar b}=P_{a\bar c}$**（即 $\gamma\equiv P_{a\bar b}/P_{a\bar c}=1$）📜Q。

**能带方程**（Bloch + 散射，Eq. 2–3）：

$$
e^{iEd/\hbar v}-\hat T^{-1}\hat S\,\hat\psi_{in}=0,\qquad \hat T=\mathrm{diag}[e^{ik\cdot(R_1+R_2)},e^{-ik\cdot R_2},e^{-ik\cdot R_1}]
$$

三角格矢量 $R_1=(\sqrt3d/2,d/2)$、$R_2=(-\sqrt3d/2,d/2)$；$v$ = 畴壁态速度，$E$ = 能量 📜Q。能谱有**能量周期 $2\pi\hbar v/d$**（类 Floquet）→ 无穷多重复能带（连续线性色散近似的结果）📜Q。

**磁场**：相位累积 $\exp(iEd/\hbar v-i\frac{e}{\hbar}A\cdot dr)$，Landau 规范 $A=(0,Bx)$；公度 $eB\sqrt3d^2/h=p/q$（$p,q$ 整数），每三角形磁通 $\varphi=p/(4q)$（Eq. 4）；磁单胞 $R_1=(q\sqrt3d,0)$、$R_2=(0,d)$，$q$ 取素数 $\le37$、$p=0,\dots,4q-1$ 📜Q。

### 1.2 参数分册

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $P_{a\bar a}$（前向散射概率）、$\gamma\equiv P_{a\bar b}/P_{a\bar c}$（偏转不对称，磁场破 C2zT）、磁通 $\varphi=p/(4q)$、$E$（扫谱） |
| **导出量（由旋钮算出）** | 能谱 $E(k)$、Dirac 点位置、谱流 $\nu\equiv n_1-n_0$、Chern 数、能量周期 $2\pi\hbar v/d$ |
| **模型内部量（解的性质）** | Hofstadter 蝴蝶、LL 谱、手征边缘态、Berry 曲率 |
| **固定常数** | $d$（Moiré 周期）、$v$（畴壁态速度）、$e,\hbar$ |
| **预言量（可检验）** | Dirac 点重入指纹、FTI 边缘态级联、$B_0\approx0.49$ T（$\theta=0.1°$） |

> **符号防混**：$\varphi$（每三角形磁通，=p/(4q)）≠ 散射相位（正文也用 $\varphi$ 表相位，注意语境）；$\gamma\equiv P_{a\bar b}/P_{a\bar c}$（偏转比）≠ 光子/其他 $\gamma$；$\nu$（Floquet 缠绕数）≠ LL 填充。**无"反推量"层**。

### 1.3 显式假设清单

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **单通道网络模型**（K 谷 2 通道在畴壁/节点解耦） | 模型 | 📜Q |
| A2 | **两谷在体解耦**（体系原子尺度光滑）；C2z 联系两谷 | 模型 | 📜Q |
| A3 | **连续线性色散近似**（每 1D 畴壁态）→ 无穷多重复带 | 模型 | 📜Q |
| A4 | **C3z + C2zT 决定 $\hat S$ 形式**；C2zT 保持时 $P_{a\bar b}=P_{a\bar c}$ | 模型 | 📜Q |
| A5 | **强场区 $P_{a\bar a}$、$\gamma\neq1$ 不随 B 变** | 推导 | 📜Q |
| A6 | **忽略节点散射的能量依赖**（ref 32 会改拓扑性质） | 模型 | 📜Q |
| A7 | **无自旋**（自旋指标略去） | 模型 | 📜Q |

---

## 2. 推导链（顺论文演绎顺序）

### 2.0 总览

| 层 | 论文内容 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 模型层 | 散射矩阵网络 | 畴壁通道 + $\hat S$ | 能带方程 Eq. (3) | A1–A4 | 周期 $2\pi\hbar v/d$ |
| 能带层 | 体带结构 | Eq. (3) | 3 带/周期、Dirac 速度 $v/2$、特殊极限 | A1–A4 | γ=1 泛特征 |
| 磁场层 | Hofstadter 蝴蝶 | Peierls 相位 + 公度通量 | 蝴蝶谱、Dirac 点重入、LL 拟合 | A3、Eq. (4) | $q\le37$ |
| 拓扑层 | FTI + 边缘态 | 谱流 + 条纹几何 | $\nu=\pm1$、手征边缘态、C=0 | A5、A6 | 强场 |

### 2.1 模型层：散射矩阵网络能带

- 单通道模型：电子沿畴壁手征运动、节点散射 $\hat\psi_{out}=\hat S\hat\psi_{in}$；$\hat S$ 由 C3z + C2zT 决定 📜Q。
- Bloch + 散射 → Eq. (3)，能量周期 $2\pi\hbar v/d$（类 Floquet）📜Q。

### 2.2 能带层：体带结构与特殊极限

- C3z + C2zT（γ=1）下泛特征（与 $P_{a\bar a}$ 无关）：(i) 每周期 3 条带；(ii) 每对相邻带经 Γ̄/K̄/K̄′ 之一的高对称动量的 Dirac 锥连接；(iii) Dirac 速度恒为 $v/2$ 📜Q。
- **特殊极限** 📜Q：
  1. $P_{a\bar a}=1$：沿三取向解耦的手征链，谱 = 三支手征色散线性叠加，对磁场不敏感；
  2. $P_{a\bar a}=1/9$、$P_{a\bar b}=P_{a\bar c}=4/9$：近粒子-空穴对称 Dirac 节点，低能性质符合 Dirac 方程（LL 谱）；
  3. $P_{a\bar b}=1$（或 $P_{a\bar c}=1$）：电子绕孤立三角形顺时针（逆时针），整数通量下三支平带，能量 $E=\pm\tfrac13\pi\hbar v/d,\ \pi\hbar v/d$。
- 无 C2zT（γ≠1）：Dirac 节点开直接带隙，但可能因电子口袋未开完整体隙 📜Q。

### 2.3 磁场层：Hofstadter 蝴蝶与 Dirac 点重入

- 公度通量 $\varphi=p/(4q)$，$q$ 素数 ≤37 → 蝴蝶图（Fig. 3）📜Q。
- 弱场 γ≈1：泛 $\varphi$ 分形能隙，$\varphi=1/2$ 例外（类零场、Dirac 锥速度 $v/2$）；$1-\varphi$ 与 $\varphi$ 谱相同（γ=1）📜Q。
- $P_{a\bar a}=1/9$：LL 精确拟合 $E=\pm(v/2)\sqrt{2\hbar eBn}$（$n=0,1,2,\dots$，2D 无质量 Dirac 费米子 LL）；其他 $P_{a\bar a}$ 因粒子-空穴不对称/电子口袋共存而复杂；$P_{a\bar a}=1$ 无 $\varphi$ 依赖 📜Q。
- **Dirac 点重入**：能量 vs $1/\varphi$（Fig. 4），Dirac 节点出现在整数/分数 $1/\varphi$ 处；位置敏感依赖 $P_{a\bar a}$ → 可由输运实验反推 $P_{a\bar a}$ 📜Q。

### 2.4 拓扑层：FTI 与手征边缘态

- 强场 γ 明显偏离 1，通量 $\varphi\in[N,N+1]$（$N$ 大整数），$P_{a\bar a}$、γ≠1 不随 B 变 📜Q。
- $\varphi=N$ 处 Dirac 锥被 γ≠1 开隙；完整谱隙 = Fig. 1(d) 蓝区（可观隙需超过热/无序展宽 → 需强场）📜Q。
- **谱流**：$\varphi=N\to N+1$ 间第 $n_0$ 隙流到第 $n_1$ 隙（γ>1 时 $n_1=n_0-1$、γ<1 时 $n_1=n_0+1$）；$\nu\equiv n_1-n_0$ 良定义（$n_0,n_1$ 单独不定义，连续近似谱无界）📜Q。
- $P_{a\bar b}=1$（γ→∞）/$P_{a\bar c}=1$（γ=0）极限解析：谱移 $\mp\tfrac13(2\pi\hbar v/d)$ 每单位通量 → $\nu=-1$（$+1$）📜Q。
- **边缘态**（条纹几何，open x̂ + periodic ŷ）：单谷模型"anomalous by construction"（1D 手征态），须两谷同考虑；体两谷解耦、边缘完美谷间 180° 反射（边界 = 平庸绝缘体界面）→ 手征边缘态（Fig. 6b）；每体隙边缘态数目与手征性相同，与 $\nu$ 一致；手征性依赖 $\mathrm{sgn}(\gamma-1)$ 📜Q。
- **Berry 曲率/Chern**（附录 B）：C2zT 保持 → Berry 曲率恒零；整数通量 $\varphi=N$ + γ≠1 → Wilson 环显式算得**每条带 Chern 数为零**（两个 hot spot 反号抵消）📜Q。
- 结论：FTI 的 $n_{edge}$ 由 **Floquet 缠绕数**（非 Chern 数）决定；能谱周期 → **手征边缘态级联**（同手征、同模数）📜Q。

---

## 3. 结论清单（分层）

### 3.1 定理式主张（模型/拓扑论证的产物，依赖 A1–A5）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 能带周期 | 能量周期 $2\pi\hbar v/d$、3 带/周期、Dirac 速度 $v/2$ | A1–A4 |
| FTI 判据 | 零 Chern 数 + 手征边缘态，$\nu=\pm1$ | A5（γ≠1 不随 B 变） |
| 谱流 | $\nu\equiv n_1-n_0$，γ>1 → −1、γ<1 → +1 | A5 |

### 3.2 估算（数值/近似，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| LL 拟合 | $E=\pm(v/2)\sqrt{2\hbar eBn}$（$P_{a\bar a}=1/9$） | 弱场 γ≈1 | 📜Q[~] |
| 平带能量（极限 3） | $\pm\tfrac13\pi\hbar v/d,\ \pi\hbar v/d$ | $P_{a\bar b}=1$/$P_{a\bar c}=1$ | 📜Q[~] |
| 谱移 | $\mp\tfrac13(2\pi\hbar v/d)$ 每单位通量 | 极限 | 📜Q[~] |
| 磁单胞 | $q$ 素数 ≤37、$p=0..4q-1$ | 数值 | 📜Q[~] |
| 实验参数 | $\theta=0.1°$ → $d\approx140$ nm、$B_0\approx0.49$ T | A3 | 📜Q[~] |

### 3.3 预言（可检验性 → §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 平衡态固体实现低能 FTI | "establish / demonstrate / realize" 📜Q | 中——输运（磁阻振荡 + 边缘态） |
| Dirac 点重入指纹 | "should provide fingerprints / could be used to estimate" 📜Q | 中——弱场输运 |
| 手征边缘态级联（同手征同模数） | "predict / smoking-gun evidence" 📜Q | 中——强场边缘输运 |
| 电子排斥自发破 C2zT → 无场 FTI（可能分数化） | "may possibly lead" 📜Q | 弱——需关联研究 |

### 3.4 内部验证（自洽核对）

1. **谱流 ↔ 边缘态互验**：蝴蝶谱流 $\nu$ 与条纹几何边缘态数目/手征一致 📜Q。
2. **Chern 显式计算**：Wilson 环 → 每条带 Chern 数零（两个 hot spot 抵消）→ 证实 FTI（非 Chern 绝缘体）📜Q。
3. **极限解析**：$P_{a\bar b}=1$/$P_{a\bar c}=1$ 谱移解析（$\tfrac13$ 系数）与数值蝴蝶一致 📜Q。
4. **两谷必须同考虑**：单谷"anomalous"，两谷 C2z 对称 → 谱流相同 → $\nu$ 为正确不变量（附录 A）📜Q。

### 3.5 概念区分（分类，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| FTI vs Chern 绝缘体 | 零 Chern 数 + 手征边缘态（Floquet 缠绕数）vs 非零 Chern 📜Q | FTI 是平衡态反常 |
| 弱场 vs 强场 | Dirac 点重入（指纹）vs 开隙 FTI | 两能区两物理 |
| γ=1 vs γ≠1 | C2zT 保持/破缺 | Dirac 锥无隙/开隙 |

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性 |
|---|---|---|---|
| A5（γ≠1、$P_{a\bar a}$ 不随 B 变） | γ 随 B 变化 | FTI 实现条件 | 作者标"γ 随磁场是重要开放问题"📜Q |
| A1（单通道模型） | 2 通道耦合 | 网络模型定量 | 可推广到双通道，定性预言仍适用 📜Q |
| A6（忽略节点能量依赖） | 能量依赖散射 | 拓扑性质被改 | 作者显式忽略（ref 32）📜Q |
| A3（连续线性色散） | 高能截断 | 无穷多带 → 有限带 | 现实 mTBG 有有限重复带 📜Q |
| 强场要求 | 隙 < 热/无序展宽 | 可观 FTI 隙 | 需强场（设计原则）📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（实验靶标）

- 弱场 Dirac 点重入 + 蝴蝶状能谱（磁场依赖输运/谱学）📜Q；
- 强场手征边缘态（级联、同手征同模数）= FTI 的 smoking-gun 📜Q；
- 磁阻振荡（近似磁通周期）+ 霍尔电阻率符号交替（Dirac 点/van Hove 奇点）📜Q（与 ref 14,15 一致）；
- $\theta=0.1°$：$d\approx140$ nm、$B_0\approx0.49$ T（比 graphene/hBN 更低的磁场要求）📜Q。

### 5.2 设计原则

强磁场（C2zT 破缺隙 > 展宽）+ mTBG 大 Moiré 周期（低 $B_0$）→ FTI；弱场 Dirac 点重入 → 定参数 📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- **T15（De Beule 2020, PRL）**：网络散射统一（$\phi=0$=TZM / $\phi=\pi/2$=pLL）——本文单通道 $\hat S$ 的推广。
- **T12（Tsim 2020, TZM）**：AA 节点确定性散射（置换型 $\hat S$）——对本文 C3z 对称 $\hat S$ 的参数化提出更严格的约束。
- **T18（De Beule 2021）**：网络映射为周期驱动（Floquet）系统的显式有效模型。
- **T19（Chou 2021）**：同组后续 CDW + 有限温输运。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 单通道近似 | 2 通道解耦假设 | 📜Q（A1） |
| γ(B) 未知 | γ 随磁场是开放问题 | 📜Q |
| 忽略节点能量依赖 | ref 32 表明会改拓扑 | 📜Q |
| 现实多带 Chern 绝缘体 | mTBG 高能 Chern 带被淹没，低能谱由 FTI 描述 | 📜Q |
| 无相互作用 | 关联可驱动相变（已在讨论中提及） | 📜Q |

## 7. 与其他工作的关系（跨论文对标放这里）

| 工作 | 关系 |
|------|------|
| San-Jose & Prada 2013 (ref 12) / Efimkin & MacDonald 2018 (ref 16) | 引用——网络模型来源（本文 $\hat S$ 在 $P_{a\bar b}=P_{a\bar c}$ 时等价 ref 16）📜Q |
| Rickhaus 2018 (ref 14) / Xu 2019 (ref 15) | 引用——mTBG 畴壁网络输运实验对标 📜Q |
| Rudner 等 (ref 28–30) / Kitagawa 等 (ref 31–33) | 引用——Floquet 拓扑绝缘体概念来源 |
| Hofstadter 1976 / Harper 1955 | 引用——蝴蝶谱祖先 |
| Yoo 2019 (ref 13) | 引用——mTBG 畴壁实验 |

> ⚠️ Phase S 外部对标（**非本文引用**，时间倒挂 💭I）见 §5.3。

## 8. 对后续研究的影响

- 提出**平衡态固体实现 FTI** 的可行路径（零 Chern + 手征边缘态）📜Q。
- 给出网络模型参数的**实验指纹**（Dirac 点重入位置 → $P_{a\bar a}$）📜Q。
- 为 mTBG 磁场物理建立网络模型 → Hofstadter 问题的桥梁 📜Q。

## 9. 理论模型映射（供 TBPM 计算对标）

| 映射 | 说明 |
|------|------|
| 散射矩阵 $\hat S$ | Eq. (1)：$\alpha=\sqrt{P_{a\bar a}}$、$\zeta=e^{-i2\pi/3}\sqrt{P_{a\bar c}}$、$\xi=e^{-i\pi/3}\sqrt{P_{a\bar b}}$ 📜Q |
| 能带方程 | $e^{iEd/\hbar v}-\hat T^{-1}\hat S=0$、$\hat T$ 平移算子 📜Q |
| 磁场 | Peierls 相位、$\varphi=p/(4q)$、磁单胞 $R_1=(q\sqrt3d,0)$ 📜Q |
| 特殊极限 | $P_{a\bar a}=1$（链）、$1/9$（Dirac）、$P_{a\bar b}=1$/$P_{a\bar c}=1$（平带）📜Q |
| 拓扑不变量 | $\nu\equiv n_1-n_0$（谱流）、Chern 数 = 0（Wilson 环）📜Q |

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：强场下 FTI 手征边缘态（条纹几何，同手征同模数级联）↔ 输运 smoking-gun；弱场 Dirac 点重入 ↔ 磁阻振荡/霍尔符号交替 📜Q。
- **Q2（理论如何解释）**：网络模型 $\hat S$ + 磁场 → Hofstadter 蝴蝶 → γ≠1 破 C2zT → 零 Chern FTI（Floquet 缠绕数 $\nu$）📜Q。
- **Q3（理论↔实验对应）**：$\varphi$ ↔ $B$（$B_0\approx0.49$ T @ θ=0.1°）、Dirac 点位置 ↔ $P_{a\bar a}$ 指纹、边缘态级联 ↔ 强场输运 📜Q。

> **增量价值**：与 T5（San-Jose 网络概念）/T9（Efimkin 网络能带）分工——本文是**网络模型的磁场推广**（Hofstadter + FTI），贡献"平衡态 FTI"预言与 Dirac 点重入指纹。report 可用数字（均 📜Q）：$\nu=\pm1$、Dirac 速度 $v/2$、能量周期 $2\pi\hbar v/d$、$d\approx140$ nm、$B_0\approx0.49$ T、$P_{a\bar a}=1/9$。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` + `-raw` 提取正文到 `/tmp/T14.txt`、`/tmp/T14_raw.txt`，逐项 grep 核对：

| 数字/公式 | grep 命中位置 | 结论 |
|------|--------------|------|
| $P_{a\bar a}=1/9$、$P_{a\bar b}=P_{a\bar c}=4/9$ | raw §III（OCR "-layout" 破碎为 "19/49"，-raw 复核为 1/9、4/9） | ✓ 📜Q[~] |
| γ≡Pab̄/Pac̄、γ=1（C2zT）、γ=0.53、γ=1.9 | 正文 Fig. 2/6/9 | ✓ |
| Dirac 速度 $v/2$ | 正文 "always v/2" | ✓ |
| 能量周期 $2\pi\hbar v/d$ | 正文 | ✓ |
| LL $E=\pm(v/2)\sqrt{2\hbar eBn}$ | 正文 §IV | ✓ |
| 平带 $\pm\tfrac13\pi\hbar v/d,\ \pi\hbar v/d$ | 正文 §III | ✓ |
| $\varphi=p/(4q)$、$q\le37$ 素数、$p=0..4q-1$ | 正文 §IV + 附录 A | ✓ |
| 谱移 $\mp\tfrac13(2\pi\hbar v/d)$、$\nu=-1/1$ | 正文 §V + 附录 A | ✓ |
| $d\approx140$ nm、$B_0\approx0.49$ T（θ=0.1°） | 正文 §VI | ✓ |
| $\nu=\pm1$（FTI±） | Fig. 1(d) caption | ✓ |

⚠️ 修正/降级：① **OCR 分数破碎**（陷阱⑤）：-layout 把 "1/9"→"19"、"4/9"→"49"，用 `-raw` 复核确认 $P_{a\bar a}=1/9$、$P_{a\bar b}=P_{a\bar c}=4/9$；② 旧 review 无无源数字，但"零陈数 FTI"表述需保留"零 Chern + 手征边缘态"完整判据（已补）；③ 全文数字重 grep 全命中。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（research_onboarding Phase 4），叙事体。 |
| 2026-09-08 | **按 5 块演绎结构整体重写**。旧叙事体归档 `archive/paper_review_T14_chou2020_prr.backup_20260908.md`。 |
| 2026-09-08 | **QC 修正**：① OCR 分数破碎（1/9、4/9）用 -raw 复核确认；② 补参数分册 + 7 条假设清单 + 假设-结论依赖图；③ 全文数字重 grep 全命中。 |
