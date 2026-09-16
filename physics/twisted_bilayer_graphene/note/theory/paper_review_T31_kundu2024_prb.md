<!--
 * @Author       : AI 精读（白箱演绎结构）
 * @Date         : 2026-08-11（初读）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T31_kundu2024_prb.md
 * @Description  : T31: Kundu & Kundu 2024 PRB — mTBG Josephson 结（2026-09-08 按 5 块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: Kundu & Kundu (2024) — 最小扭角双层石墨烯的 Josephson 结

| 字段 | 内容 |
|------|------|
| **编号** | T31 |
| **标题** | Josephson junction of minimally twisted bilayer graphene |
| **作者** | Ritajit Kundu, Arijit Kundu |
| **期刊** | Physical Review B 110, 085422 (2024)（Received 4 Jun / published 21 Aug 2024）📜Q |
| **DOI / arXiv** | 10.1103/PhysRevB.110.085422 / arXiv:2405.03571（⚠️ arXiv 号外部来源，正文未出现） |
| **类型** | 理论 — mTBG Josephson 结（现象学 Chalker-Coddington 网络模型 + 散射矩阵 + Andreev 束缚态，无实验数据） |
| **课题组** | Arijit Kundu group（IIT Kanpur） |
| **PDF** | ✅ `reference/pdfs/Kundu和Kundu - 2024 - Josephson junction of minimally twisted bilayer graphene.pdf`（正文 15 页 + Appendices A–E） |
| **精读日期** | 2026-08-11（初读）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」的五块记（见 `note/shared/method/theory_paper_reading.md` §3）。理论论文无黑箱、无反推、无可辨识实验，故不用"四层变量表 + 判别表"。
> **共享知识引用**：Chalker-Coddington 网络 / zigzag（ZZ）vs pseudo-Landau-level（PLL）模见 `[PHY-MB]`；valley Chern / 谷守恒见 `[PHY-BERRY]`。⚠️ 本文的 ZZ/PLL 分类直接继承 De Beule 2020（T15）网络模型，§7 显式对标。

---

## TL;DR

**本文想解决的问题**：把 mTBG 的畴壁网络（ZZ / PLL 两种模）接到两块 s 波超导体上构成 Josephson 结，问：畴壁网络的散射参数 $(P_f,\gamma)$ 如何决定 Andreev 束缚态（ABS）谱与 Josephson 电流的周期性（2π vs 4π），以及物理边缘如何改变输运？

**主结果**（全文无实验数据，为散射矩阵 + 数值自洽）：① zigzag 模（$P_f=0,\gamma=0$）→ ABS 线性色散 $\sim(\pi-|\phi|)$、φ=±π 处零能交叉 → **4π 周期锯齿形 Josephson 电流** $J_{st}\sim(2e\Delta/\hbar)\phi$ 📜Q；② pseudo-Landau-level 模（$P_f=0,\gamma=\pi/2$）→ ABS 完美平坦 → **体 Josephson 电流为零**（网络绝缘）📜Q；③ 调 γ 从 0→π/2 使 ABS 两 Dirac 锥合并开隙 → 4π 锯齿 → 2π 正弦 $J_{2\pi}\sim(2e\Delta/\hbar)\sin\phi$；调 $P_f$ 在 γ=0 使 $J_{st}\to J_{4\pi}\sim(2e\Delta/\hbar)\sin(\phi/2)$，转变在 $P_f\approx0.4$ 📜Q；④ **物理边缘**在 PLL 区能中介 4π 周期 Josephson 电流（即便体电流为零），类比磁场下 2DEG 的 skipping orbit 📜Q；⑤ 实验签名：$f_J/2=eV/h$ 偶极 Josephson 辐射、Shapiro 台阶 $V_n=nhf/2e$（仅偶阶）📜Q。

**结论/意义**：作者表态 "we theoretically investigate / we show"——首次用网络散射矩阵系统给出 mTBG-JJ 的 ABS/电流相图（$J_{st}/J_{2\pi}/J_{4\pi}$ 三态分类 + 混合区），并把"体/边缘电流分离"引入 mTBG 超导输运。⚠️ 全文为现象学模型 + 数值预言，$P_f,\gamma$ 的微观起源作者明言"remains unknown"。

---

## 1. 模型白箱（理想系统 + 假设清单）

### 1.1 模型：现象学 Chalker-Coddington 网络 + s 波超导结

**网络模型**（引 De Beule 2020 PRL [34]、Vakhtel 2022 [35]）：mTBG（θ ≲ 1°）晶格弛豫形成三角 AB/BA 畴，moiré 长度 $l\sim a_0/\theta$（$a_0=2.46$ Å）；E 场下层间偏压使畴绝缘、谷 Chern 数差 $\Delta C_v=\pm2\,\mathrm{sgn}(U/t_\perp)$ → **每谷每自旋 2 条畴壁模**构成网络链接；AA 区（E 场下仍 gapless）是散射节点 📜Q。

**散射矩阵**：每节点 3 进 3 出通道（每通道含 2 畴壁模/谷/自旋）→ 6×6 酉矩阵。对称性 $C_{3z}$、$C_{2z}T$ 约束（Eqs. (1)–(2)）→ S 取分块形式（Eqs. (3)–(5)），由前向散射振幅 $P_f=P_{f1}+P_{f2}$ 与偏转振幅 $P_d=P_{d1}+P_{d2}$ 参数化 📜Q。酉性 $P_f+2P_d=1$（Eq. (6)）、相位关系 $\cos(\beta-\gamma)=(P_{d2}-P_{d1})/(2\sqrt{P_{f1}P_{d1}})$（Eq. (7)）📜Q。

**对称参数选择**：$P_{f1}=P_{f2}=P_f/2$、$P_{d1}=P_{d2}=(1-P_f)/4$ → $\beta=\gamma+\pi/2$，自由参数缩为 $P_f\in[0,1]$、$\gamma\in[0,\pi/2]$ 📜Q。

**两极限点**：(i) $P_f=0,\gamma=0$ → 三条 120° 旋转独立的 **zigzag（ZZ）模**（弹道）；(ii) $P_f=0,\gamma=\pi/2$ → **pseudo-Landau-level（PLL）模**（循环环，绝缘）📜Q。

**超导结**：左/右 s 波序参量 $\Delta e^{\pm i\phi/2}$；Andreev 反射矩阵 $M_A(\phi)$（Eq. (15)）、α 因子（Eq. (16)）📜Q。仅 retro Andreev 反射（specular 被抑制，引 ref 49）📜Q。横向上周期性边界 → Bloch 动量 k 好量子数，$S^{(n,2)}(k)=U_1(k)S^{(n,1)}U_2(k)$（Eq. (8)）📜Q。

### 1.2 参数分册（区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $P_f\in[0,1]$、$\gamma\in[0,\pi/2]$（网络散射）、超导相位 φ、Bloch 动量 k、结长 N、横宽 Ny、扭角 θ |
| **导出量（由旋钮+常数算出）** | S 矩阵元（$P_{f1}/P_{f2}/P_{d1}/P_{d2}$、β-γ）、$S_{node}(k)$、$S_{bond}(\varepsilon,\phi)$、自由传播相位 $\xi l/\hbar v_F$ |
| **模型内部量（解的性质）** | ABS 谱 $\varepsilon_p(\phi,k)$、Josephson 电流 $J(\phi)$、临界电流 $J_c$ |
| **固定常数** | $a_0=2.46$ Å、$l\sim a_0/\theta$、$\Delta$（超导隙）、$\Delta C_v=\pm2\,\mathrm{sgn}(U/t_\perp)$、$v_F$（DW 模费米速度） |
| **预言量（可检验）** | 4π/2π 周期性、锯齿/正弦电流形、边缘中介电流、$f_J/2$、Shapiro 偶阶台阶 |

> 无"反推量 θ̂"层——纯理论，参数为现象学散射参数（作者明言 $P_f,\gamma$ 微观起源未知）。**符号防混**：$P_f$（前向散射振幅，标量）≠ $P$（对称性/宇称）；$\gamma$（网络相位参数）≠ 石墨烯 γ1 层间耦合；$\Delta$（超导隙）≠ $\Delta C_v$（谷 Chern 数差）。

### 1.3 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **现象学网络模型有效**：低能物理由 Chalker-Coddington 网络捕捉 | 模型 | 📜Q |
| A2 | **谷守恒**：散射区对原子尺度光滑 → 谷间散射可忽略 | 模型 | 📜Q |
| A3 | **散射矩阵能量无关**：S 与能量无关（网络模型近似） | 模型 | 📜Q |
| A4 | **对称参数选择** $P_{f1}=P_{f2}=P_f/2$、$P_{d1}=P_{d2}=(1-P_f)/4$（主文；Appendix E 放松） | 模型 | 📜Q |
| A5 | **无自旋轨道耦合**：自旋旋转对称、自旋简并（σ0 直积） | 模型 | 📜Q |
| A6 | **长结极限** $L=Nl\gg\xi$（超导相干长度） | 推导 | 📜Q |
| A7 | **无费米子宇称约束**：系统达平衡不受宇称限制（Josephson 电流公式 Eq. (20) 成立前提） | 推导 | 📜Q |
| A8 | **边缘模型**：K 谷模在边缘被完美反射回 K′ 谷（至相位），截断远离节点、ψ1=ψ2=0 | 推导（边缘） | 📜Q |

> 判别性扫轴：$(P_f,\gamma)$ 全平面（Fig. 4(d) 三色相图）、φ、k、结长 Nl（Fig. 4(e)）、$(N_x,N_y)=(3,5)$（边缘）——均为计算扫参。这些假设在 §4 逐一映射到"失效 → 结论崩塌"。

---

## 2. 推导链（演绎结构：顺论文顺序，每步"输入→输出→所用假设/定理→合法域"）

### 2.0 总览

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | Introduction | MTBG 畴壁网络 + ZZ/PLL（refs 33–39） | 网络模型可捕捉低能 | A1、A2 | θ ≲ 1° |
| 模型层 | Sec II | S 矩阵 + 超导结 | 6×6 节点散射 + $M_A$ | A3、A4、A5 | 对称参数 |
| 推导层 | Sec III | ABS 行列式 Eq. (19) + 电流 Eq. (20) | ABS 谱 + Josephson 电流 | A6、A7 | 长结、无宇称约束 |
| 推导层2 | Sec IV | 数值扫描 $(P_f,\gamma)$ | 4π/2π/锯齿三态 + 相图 | — | 数值 |
| 边界层 | Sec V | 开边缘 + K↔K′ 反射 | 边缘中介 4π 电流 | A8 | PLL 区 |

### 2.1 前提定理层（引言）

- mTBG 弛豫形成三角 AB/BA 畴（refs 28,29）；E 场下层间偏压 → 畴绝缘 + 谷 Chern 数 → 畴壁模（refs 30–32）📜Q。
- Chalker-Coddington 网络捕捉低能（ref 33），近期输运研究证实 AB 振荡、zigzag 模（refs 34–39）📜Q。网络参数下：ZZ 模 → 透明（弹道）、PLL 模 → 绝缘 📜Q。

### 2.2 模型层：散射矩阵 + 超导结（Sec II）

- S 矩阵形式（Eqs. (3)–(5)）由 $C_{3z}$、$C_{2z}T$ 对称 + 酉性（$P_f+2P_d=1$）唯一确定 📜Q。
- 对称参数选择 → 仅 $P_f,\gamma$ 两自由参数；$S^{(n,2)}(k)$ 由 Bloch 定理得（Appendix B）📜Q。全网络 $S_{node}(k)=\sigma_0\otimes\oplus S^{(n,m)}(k)$，维数 $D=(2N-1)\times2^3\times6$ 📜Q。
- Andreev 反射 $M_A(\phi)$（Eq. (15)）连接 K↔K′ 谷（电子 K↑ → 空穴 K′↓）；链接自由传播相位 $\xi l/\hbar v_F$ 进 $S_{bond}$ 📜Q。

### 2.3 推导层：ABS 与 Josephson 电流（Sec III）

- $|\varepsilon|<\Delta$ 的模被超导体束缚 → 多重 Andreev 反射 → ABS；条件 $\det[I-S_{node}(k)S_{bond}(\varepsilon,\phi)]=0$（Eq. (19)）📜Q。
- Josephson 电流（Eq. (20)）：Matsubara 频率求和（$T\to0$ 时 $\sum\to\int d\omega$），含准粒子连续谱贡献（引 refs 48,50–53）📜Q。公式成立前提 = 无宇称约束（A7）📜Q。
- 长结：$L=Nl\gg\xi$（A6）📜Q。

### 2.4 推导层2：数值结果（Sec IV）

- **ZZ（$P_f=0,\gamma=0$）**：ABS 近零能线性 $\sim(\pi-|\phi|)$、φ=±π 零能交叉 → **4π 锯齿电流** $J_{st}(\phi)\sim(2e\Delta/\hbar)\phi$（$|\phi|<\pi$，Eq. (21)），φ=±π 处不连续 = 4π 周期性签名 📜Q。
- **γ↑（$P_f=0$）**：ABS 两 Dirac 锥在 k-φ 空间合并开隙（Fig. 3 上排）→ 锯齿 → **2π 正弦** $J_{2\pi}\sim(2e\Delta/\hbar)\sin\phi$（Eq. (22)）；γ=π/2（PLL）→ ABS 完美平坦 → 体电流为零 📜Q。
- **$P_f\uparrow$（γ=0）**：零能 ABS 恒存，$P_f\approx0.4$ 处零能-有限能隙闭合 → 锯齿 → **正弦 4π** $J_{4\pi}\sim(2e\Delta/\hbar)\sin(\phi/2)$（Eq. (23)）📜Q。
- **相图**（Fig. 4(d)）：以 $J_{st}/J_{2\pi}/J_{4\pi}$ 三原色的重心坐标（Eq. (24)）分类全 $(P_f,\gamma)$ 平面 → $J_{st}$（蓝）、$J_{2\pi}$（绿）、$J_{4\pi}$（红）+ 混合区 📜Q。临界电流随结长：4π 区 $J_c\sim1/(Nl)$、2π 区非单调（Fig. 4(e)）📜Q。

### 2.5 边界层：物理边缘（Sec V）

- 开边缘：K 谷模在顶/底边缘被反射回 K′ 谷（Eqs. (27)–(30)），保持时间反演对称；取 ψ1=ψ2=0 📜Q。边缘幅（Fig. 6）证实新 ABS 局域于顶/底边缘 → 确为边缘态 📜Q。
- **PLL 区（$P_f=0.1,\gamma=\pi/2$）**：体电流为零，但边缘产生**两条 gapless 色散 ABS** → **4π 周期边缘 Josephson 电流**（Fig. 5(e)），类比磁场下 2DEG skipping orbit 📜Q。$P_f$ 增大 → 边缘电流增 + 混入 2π 分量 → skewed 📜Q。
- **实验签名**：DC 偏压 → 偶极 Josephson 辐射 $f_J/2=eV/h$（GHz，RF）；微波 → Shapiro 台阶 $V_n=nhf/2e$，4π 电流下**仅偶阶**（缺奇阶）；bolometric 探测（refs 56–59）📜Q。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

### 3.1 定理式主张（散射矩阵对称性论证的产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| S 矩阵形式 | $C_{3z}$、$C_{2z}T$ + 酉性 → Eqs. (3)–(5) 唯一形式 | A3、A5 |
| 酉性约束 | $P_f+2P_d=1$ | 酉性 |
| 对称性对 ABS 的约束 | TRS+PH 对称 → $\varepsilon_p(\phi,k)=\varepsilon_p(-\phi,-k)$、$\varepsilon_p(\phi,k)=-\varepsilon_{-p}(\phi,-k)$ | TRS、PHS |
| 周期-隙对应 | 零能 ABS 交叉 → 4π；gapped ABS → 2π | 散射理论 |

### 3.2 估算（数值算例，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 数值参数 | θ=0.1°、N=3、Δ=1 meV、T=0.01Δ | A6 | 📜Q[~] |
| ZZ 电流 | $J_{st}\sim(2e\Delta/\hbar)\phi$（$|\phi|<\pi$） | 零能 ABS | 📜Q[~] |
| 2π 电流 | $J_{2\pi}\sim(2e\Delta/\hbar)\sin\phi$ | gapped ABS | 📜Q[~] |
| 4π 电流 | $J_{4\pi}\sim(2e\Delta/\hbar)\sin(\phi/2)$ | 零能 ABS | 📜Q[~] |
| 锯齿→4π 转变 | $P_f\approx0.4$ | 数值 | 📜Q[~] |
| 边缘算例 | $(N_x,N_y)=(3,5)$ | A8 | 📜Q[~] |

### 3.3 预言（可检验性 → 见 §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| ZZ→4π、PLL→零体电流、参数调 2π/4π/混合 | "we find / we show"（数值）📜Q | 中——超导输运 |
| PLL 区边缘中介 4π 电流 | "edge states can give rise to 4π-periodic response" 📜Q | 中——边缘输运 |
| $f_J/2$、Shapiro 偶阶台阶 | "distinct experimental signatures" 📜Q | 中——RF/微波 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

1. **对称约束核对**：ABS 满足 TRS/PH 对称关系（数值确认）📜Q。
2. **极限对照**：ZZ 锯齿电流、PLL 零电流、4π/2π 周期与已知 long-JJ（ref 54）、QSH 边缘 JJ（ref 50）结果一致 📜Q。
3. **边缘-体一致性**：PLL 区边缘 ABS 的平坦能量 ≠ 体平坦 ABS（Fig. 2(d) vs 5(b)），边缘色散 ABS 的局域性由幅分析（Fig. 6）确认 📜Q。
4. **参数鲁棒性**：非对称参数 $P_{f1}\neq P_{f2}$（Appendix E）结果定性一致 → 对称参数选择（A4）非本质 📜Q。

### 3.5 概念区分（作者论证中的"分类"，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| ZZ vs PLL 模 | $P_f=0,\gamma=0$（三独立 zigzag）vs $P_f=0,\gamma=\pi/2$（循环环）📜Q | 弹道 vs 绝缘 |
| 体 vs 边缘电流 | 周期性边界（体）vs 开边缘（K↔K′ 反射）📜Q | PLL 区体零、边缘 4π |
| 锯齿 vs 正弦 4π | 相位线性（$J\propto\phi$）vs 正弦（$J\propto\sin\phi/2$）📜Q | 由 ABS 色散决定 |
| retro vs specular Andreev | 1D DW 模 → 仅 retro（specular 抑制，ref 49）📜Q | 简化 |

> 注：这些是**概念/图景分类**（taxonomy），不是实验论文那种"数据排除竞争解释"（溯因排除）——理论论文没有后者。

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A1 网络模型有效 | 网络参数微观起源未知、真实弛豫偏离理想三角畴 | 全部 ABS/电流预言 | 作者明言 $P_f,\gamma$ "remains unknown"，定性预言仍稳 📜Q |
| A2 谷守恒 | 原子尺度缺陷谷间散射 | 谷间 Andreev/散射图像 | 未讨论 💭I（对比 T5 显式 weak 保护） |
| A7 无宇称约束 | 宇称守恒（准粒子中毒时间短） | Josephson 电流公式（锯齿电流的 4π） | 作者明言需宇称守恒修正（ref 48）📜Q |
| A8 边缘模型 | 边缘弛豫/几何复杂 | 边缘 4π 电流 | 作者明言需第一性原理定量（尚无文献）📜Q |
| A4 对称参数 | 真实 $P_{f1}\neq P_{f2}$ | 定量细节 | Appendix E 证定性不变 📜Q |
| A6 长结极限 | $L\lesssim\xi$ | 长结电流公式 | 短结是另一极限 📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- **4π/2π 周期 Josephson 电流**：$(P_f,\gamma)$ 调控相图（Fig. 4(d)）📜Q；
- **$f_J/2=eV/h$ 偶极 Josephson 辐射**（RF 技术，ref 56）📜Q；
- **Shapiro 台阶** $V_n=nhf/2e$，4π 下仅偶阶（缺奇阶，refs 57,58）📜Q；
- **bolometric 探测** Josephson 辐射（ref 59）📜Q。

### 5.2 设计原则（可调 mTBG-JJ 三要素）

$P_f$（前向散射振幅，可由节点周期势降低）+ $\gamma$（网络相位，可由交错磁场调节）+ 边缘构型（PLL 区边缘中介 4π）📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- **De Beule 2020（T15）**：本文网络模型（ZZ/PLL）直接继承其散射统一框架，属其超导推广 💭I。
- **Barrier 2024（Nature 628, 741，实验）**：mTBG 1D 邻近超导的量子霍尔区实验，本文为无磁场区理论对照 💭I。
- 作者指出可推广到 helical trilayer graphene（ref 60）💭I。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 现象学参数无微观起源 | $P_f,\gamma$ 依赖器件工艺/E 场/扭角/衬底，微观未知 | 📜Q（"microscopic origins ... remain unknown"） |
| γ 调控困难 | 需交错磁场保持 TRS，实现难 | 📜Q（"Tuning γ is more challenging"） |
| 边缘几何未定量 | 真实边缘弛豫需第一性原理，尚无文献 | 📜Q |
| 无宇称约束近似 | 宇称守恒时需修正 | 📜Q |

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）

| 工作 | 关系 |
|------|------|
| De Beule 2020 PRL（ref 34）/ Vakhtel 2022（ref 35） | **直接继承**——网络模型 + ZZ/PLL 参数化来源 📜Q |
| Tsim 2020（ref 37）、Fleischmann 2020（ref 36） | 引用——ZZ 模的微观预言 📜Q |
| Huang 2018（ref 28）、Rickhaus 2018（ref 38）、Xu 2019（ref 39） | 引用——mTBG 畴壁网络实验证据 📜Q |
| Beenakker 2013（ref 50）、Ishii 1970（ref 54） | 引用——4π/锯齿 Josephson 电流的已知对照（QSH 边缘 JJ、long metallic JJ）📜Q |
| Barrier 2024（ref 10） | 引用——1D 邻近超导（量子霍尔区）实验背景 📜Q |

> ⚠️ Phase S 外部对标（非本文引用，时间倒挂，💭I）见 §5.3。

## 8. 对后续研究的影响

- 首次用网络散射矩阵系统给出 mTBG-JJ 的 ABS/电流相图（$J_{st}/J_{2\pi}/J_{4\pi}$ 三态 + 混合区）📜Q。
- 把"体-边缘电流分离"引入 mTBG 超导输运（PLL 区体零、边缘 4π）📜Q。
- 与 T36（Du 2025 畴壁工程）共同构成"石墨烯超导畴壁"研究线（T31 网络模型 / T36 紧束缚 kink 态）💭I。

## 9. 理论模型映射（供 TBPM / 计算对标）

| 映射 | 说明 |
|------|------|
| 网络参数 $(P_f,\gamma)$ → 相图 | ZZ（0,0）/ PLL（0,π/2）/ 中间态（Fig. 4(d)）📜Q |
| 散射矩阵 S → 透射计算 | 6×6 节点 S + $S_{node}(k)\otimes\sigma_0$（$D=(2N-1)\times2^3\times6$）📜Q |
| ABS → 输运预言 | $\det[I-S_{node}S_{bond}]=0$ → ABS；Matsubara → $J(\phi)$ 📜Q |
| 边缘 → 构型 | 开顶/底边缘 + K↔K′ 反射（ψ1=ψ2=0）📜Q |
| 4π 周期性 → 实验 | $f_J/2=eV/h$、Shapiro 偶阶台阶 📜Q |

> 与 TBPM/Kubo 对应：本文是**网络散射矩阵**（非晶格哈密顿），属 mTBG 畴壁网络的最小模型；复现需实现 Chalker-Coddington 网络 + Andreev 边界，非直接 TBPM 可比（供方法对照）💭I。

---

## Phase S 目的接口（引用式，随项目增删）

- **Q1（edge state 如何表征）**：本文是理论，无实验表征；预言 = ABS 谱（线性/平坦/色散）+ Josephson 电流周期（4π/2π）+ 边缘局域幅（Fig. 6）📜Q。
- **Q2（理论如何解释）**：mTBG 畴壁网络 + s 波超导 → 散射矩阵决定 ABS/电流；ZZ→4π、PLL→零体电流、边缘→4π（K↔K′ 反射）📜Q（§2.2–2.5）。
- **Q3（理论↔实验对应）**：$(P_f,\gamma)$ ↔ 器件参数（E 场/扭角/周期势/交错磁场）；$f_J/2$、Shapiro 偶阶台阶 ↔ 超导输运可测 📜Q。

> **增量价值**：Scope Out 定位（Josephson 需独立调研）——仅需知道"存在"；提供 mTBG 超导输运的相图入口 + 与 T36 的分工（网络散射 vs 晶格 kink）。无旧版无源数字需删（旧版较保守）。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取正文到 `/tmp/T31.txt`（945 行），逐项 grep 核对：**全部数字/专名命中原文**——

| 数字/专名 | grep 命中位置 | 结论 |
|------|--------------|------|
| θ=0.1°（6 处）、N=3、Δ=1 meV（6 处）、T=0.01Δ | Fig. 2–5 captions | ✓ 📜Q[~] |
| 4π（42 处）、2π（34 处）、sawtooth | 全文 | ✓ 📜Q |
| $P_f\approx0.4$（3 处） | Sec IV | ✓ 📜Q[~] |
| $P_f+2P_d=1$、6×6、$D=(2N-1)\times2^3\times6$ | Sec II | ✓ 📜Q |
| ΔCv=±2 sgn(U/t⊥)、a0=2.46 Å、l~a0/θ | Sec I/II | ✓ 📜Q |
| $J_{st}\sim(2e\Delta/\hbar)\phi$、$J_{2\pi}$、$J_{4\pi}$（Eqs. 21–23） | Sec IV | ✓ 📜Q |
| $(N_x,N_y)=(3,5)$（2 处）、$f_J/2=eV/h$、$V_n=nhf/2e$ | Sec V/VI | ✓ 📜Q |
| zigzag / pseudo-Landau-level / Chalker-Coddington | 摘要/正文 | ✓ 📜Q |

⚠️ 修正/降级：① arXiv:2405.03571 正文未出现 → 头部表已标"外部来源"。② 未引入量子化电导/临界电流绝对值（本文只给 $J\propto$ 相对形式与 $J_c\sim1/(Nl)$ 标度，无 $I_c$ 绝对数字）——§3.2 已声明。③ 旧版"$I_c\propto$ 畴壁数目"已精化为"临界电流随 $(P_f,\gamma)$ 相图 + $J_c\sim1/(Nl)$ 标度"（原文无 "$I_c\propto N_{DW}$" 表述）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧叙事版归档 `archive/paper_review_T31_kundu2024_prb.backup_20260908.md`。新增：模型白箱（Chalker-Coddington 网络 + 散射矩阵 Eqs.(1)–(8) + 参数分册 + 8 条假设清单）、推导链（前提定理/模型/ABS-电流推导/数值相图/边缘五层）、结论清单（定理/估算/预言分层）、假设-结论依赖图、接口。全部 📜Q 事实与数字无丢失；旧版"$I_c\propto$ 畴壁数目"精化为原文表述。 |
