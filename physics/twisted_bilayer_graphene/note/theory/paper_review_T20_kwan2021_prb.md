<!--
 * @Author       : AI 精读 (理论论文五块演绎结构)
 * @Date         : 2026-08-06（粗读）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T20_kwan2021_prb.md
 * @Description  : T20: Kwan et al. 2021 — TBG Chern 绝缘区（ν=+3 QAHE）中的畴壁竞争（理论 — 有效场论 + Hartree-Fock 数值）
-->

# Paper Review: Kwan, Wagner, Chakraborty, Simon & Parameswaran (2021) — TBG Chern 绝缘区的畴壁竞争

| 字段 | 内容 |
|------|------|
| **编号** | T20 |
| **标题** | Domain wall competition in the Chern insulating regime of twisted bilayer graphene |
| **作者** | Yves H. Kwan, Glenn Wagner, Nilotpal Chakraborty, Steven H. Simon, S. A. Parameswaran |
| **期刊** | Physical Review B 104, 115404 (2021) |
| **DOI / arXiv** | 10.1103/PhysRevB.104.115404（⚠️ arXiv 号正文未出现） |
| **类型** | 理论 — 有效场论（Ginzburg-Landau/CP³ NLSM）+ 自洽 Hartree-Fock 数值（无实验数据） |
| **课题组** | Kwan / Wagner / Chakraborty / Simon / Parameswaran (Rudolf Peierls Centre, Oxford) |
| **PDF / SI PDF** | ✅ `reference/pdfs/Kwan 等 - 2021 - Domain wall competition in the Chern insulating regime of twisted bilayer graphene.pdf`（正文 15 页 + Appendices A–K：CM/FHS/HF 方程/HFWQ/NLSM/DW 标度/能量分解/交织壁相图/谱函数/DW 细节/有限温相变） |
| **精读日期** | 2026-08-06（粗读）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」五块记。理论论文无黑箱、无反推、无可辨识实验。
> **共享知识引用**：通用物理（QAHE、量子霍尔铁磁体、NLSM、Hartree-Fock）锚点引用 `note/shared/physics/`，不复制讲义。

---

## TL;DR

**本文想解决的理论问题**：魔角 TBG 在 $\nu=+3$ 观测到稳健的量子化反常霍尔效应（QAHE），归因于 hBN 衬底稳定、自发破缺时间反演的**谷+自旋极化 Chern 绝缘基态**（$C=\pm1$）。当衬底耦合空间不均匀时，器件会分裂成量子数（Chern 数、谷极化）不同的大畴；这些畴之间的**畴壁类型、性质与能量选择机制**是什么？

**主结果**：① 识别**三种畴壁**——**Chern 壁**（Chern 数翻转、谷不变：$(m_z,n_z)\to(-1,1)$，锐利、承载**手征共传播边缘模**）、**谷壁**（谷翻转、Chern 不变：$(m_z,n_z)\to(1,-1)$，纹理化、承载**非手征对向传播模**）、**交织壁**（Chern 与谷同时翻转：$(m_z,n_z)\to(-1,-1)$，被 moiré 晶格钉扎的**亚稳**态）📜Q；② Chern 壁/谷壁的能量竞争由**衬底梯度 $\Delta_{\rm max}/w$** 与扭角调谐——小梯度→谷壁有利（更多纹理化降低交换能）、小角度→Chern 壁有利；谷壁宽度标度 $\xi\sim a_M[\rho_v/(a_M\Delta_{\rm max}/w)]^{1/3}$（指数 $-1/3$，与 Ginzburg-Landau 一致），Chern 壁锐利且衬底无关 📜Q；③ 渗流的 Chern/交织壁网络会**破坏宏观 QAH 响应**（类加倍 Chalker-Coddington 网络），谷壁主导则得"轨道铁磁、谷无序"的 QH 随机场顺磁体 → 为"为何部分 $\nu=+3$ 样品有 QAHE 而另一些没有"提供候选解释 📜Q。

**结论/意义**：把 QAHE 的畴壁物理从"单个边缘态"推进到"畴壁类型学 + 能量竞争"层面，且**明确区分**于 mTBG 偏压下 AB/BA 畴壁的螺旋态（二者是不同体系）。⚠️ 全文为理论 + HF 数值，作者用词 propose / suggest / expect，**非已验证事实**。

---

## 1. 模型白箱（理想系统 + 假设清单）

### 1.1 有效场论（Ginzburg-Landau 自由能）

对自旋全极化、hBN 对齐 TBG 的平带，用子格 $(A,B)$ × 谷 $(K,\bar K)$ 标记；泡利矩阵 $\sigma_\mu$（子格）、$\tau_\mu$（谷）。子格势 $\propto\sigma_z$ 破 $C_{2z}$、给两谷相反 Chern 数 $C=\sigma_z\tau_z$ 📜Q。畴壁物理用 $Z_2$ 序参量 $m_z\sim\langle\sigma_z\tau_z\rangle$（局域 Chern 数）与 O(3) 序参量 $n$（谷极化，$n_z\sim\langle\tau_z\rangle$、$n_\mu\sim\langle\sigma_x\tau_\mu\rangle_{\mu=x,y}$）描述：

$$
f\sim \rho_s(\nabla m_z)^2+\frac{(m_z^2-1)^2}{\beta^2 a_M^2}+\rho_v(\nabla n)^2-2\frac{\Delta(\mathbf r)}{a_M^2}m_z n_z
$$

📜Q（Eq. (1)）。$\rho_s,\rho_v$ 刚度（量级相近）、$\beta$ 各向异性参数（$O(1)$）、$\Delta(\mathbf r)$ 衬底势（子格劈裂，缓变于 $a_M$、保近似 $U(1)_v$ 谷对称）📜Q。此自由能是更完整 CP³ NLSM（附录 E）的近似 📜Q。衬底势被唯象建模为缓变子格劈裂 $\Delta(\mathbf r)$（可换号），捕获 hBN 的 $C_{2z}$ 破缺效应 📜Q。

### 1.2 参数分册

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | 衬底势 $\Delta(\mathbf r)$（幅 $\Delta_{\rm max}$、宽度 $w$）、扭角 $\theta$、填充 $\nu$（固定 $+3$） |
| **导出量（由旋钮+常数算出）** | 衬底梯度 $\Delta_{\rm max}/w$、DW 宽度 $\xi$、DW 张力 $\sigma=(E_{\rm Chern}-E_{\rm valley})/(2a_M N_2)$、能差 $E_{\rm Chern}-E_{\rm valley}$ |
| **模型内部量（解的性质）** | 序参量轮廓 $(m_z,n_z)$、三类 DW 的能量、手征/非手征边缘模、谱函数 $A(\omega,r)$、相图 |
| **固定常数** | $w_{AA}=0.08$ eV、$w_{AB}=0.11$ eV、$d=40$ nm、$\epsilon_r=9.5$、$v_0\approx9\times10^5$ m/s、$a_M\sim14$ nm、$a=1.42$ Å、$k_D=4\pi/3\sqrt3 a$ |
| **预言量（可检验）** | 手征 DW 网络 vs 谷 DW 网络的可区分 STM 信号、DW 张力→居里温度 |

> 无"反推量 θ̂"层。**符号防混**：$m_z$（Z₂ Chern 序参量）≠ 磁化；$n_z$（谷极化）≠ 电子密度；$C=\sigma_z\tau_z$（Chern 数，两谷反号）；$\Delta(\mathbf r)$（衬底子格劈裂）≠ 超导能隙。

### 1.3 显式假设清单

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **全自旋极化**（$\nu=+3$ 下 7 条填充带，$m_z$ 描述） | 模型 | 📜Q |
| A2 | **完美子格极化仅在 chiral 极限出现，但标签可推广** | 模型 | 📜Q（作者自述） |
| A3 | **衬底势缓变**（保近似 $U(1)_v$ 谷对称） | 模型 | 📜Q |
| A4 | **忽略谷间散射**（$\theta\lesssim1$ 时被抑制） | 模型 | 📜Q |
| A5 | **中心带-远带能隙大** → 固定 Hilbert 空间（FHS）投影到中心带合法 | 数值 | 📜Q（>99% 重叠验证） |
| A6 | **双栅屏蔽库仑** $V(q)=\frac{2\pi e^2}{\epsilon_r q}\tanh qd$，$d=40$ nm、$\epsilon_r=9.5$ | 数值 | 📜Q |
| A7 | **HF 近似**（忽略超越 HF 的 RPA 修正；不同双计数扣除方案会移动定量相界） | 数值 | 📜Q（作者自述） |
| A8 | **一维调制衬底**（只沿 $a_M^{(1)}$ 变化，保留 $a_M^{(2)}$ 平移） | 数值 | 📜Q |

---

## 2. 推导链（顺论文演绎顺序）

### 2.0 总览

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 模型层 | Sec. II | 序参量 + 衬底 | GL 自由能（Eq. 1）+ 三类 DW 分类 | A1–A4 | 尺度 $\gg a_M$ |
| 推导层 | Sec. II | GL | 谷壁宽度 $\xi\sim a_M[\rho_v/(a_M\Delta_{\rm max}/w)]^{1/3}$、Chern 壁 $\propto\beta a_M$ | 变分（附录 F） | 缓变衬底 |
| 数值层 | Sec. III | CM + 衬底 | FHS 投影 + HF 方程 | A5–A8 | $\theta\sim1°$ |
| 推导层 | Sec. IV | HF 解 | 能差相图 + 宽度标度 + 交织壁亚稳 | 附录 G/H | — |
| 边界层 | Sec. V / 附录 K | DW 张力 | 有限温 Ising 相变、居里温度 | 熵论证 | — |

### 2.1 有效场论与三类畴壁（Sec. II）

- 设 $\nu=+3$ 的 OCI 态破缺谷与时间反演对称；$C=\sigma_z\tau_z$ 给两谷相反 Chern 数 📜Q。$m_z\sim\langle\sigma_z\tau_z\rangle$ = 局域 Chern 数、$n_z\sim\langle\tau_z\rangle$ = 局域谷极化；自由能 Eq. (1) 📜Q。
- **三类 DW 分类**（以 $m_z=n_z\to+1$（$x\to-\infty$）为参考，看 $x\to\infty$ 极限）：
  1. **Chern 壁**：$(m_z,n_z)\to(-1,1)$——Chern 翻转、谷不变。锐利（$m_z$ 是 $Z_2$ 变量，跨 Chern 相干区拓扑上被迫含涡旋）→ 宽度 $\propto\beta a_M$、**衬底无关** 📜Q。承载（至少）一对**手征共传播**边缘模（两侧 Chern 差 $\pm2$；背散射被手征性禁戒 → Luttinger 参数锁到非相互作用值）📜Q。
  2. **谷壁**：$(m_z,n_z)\to(1,-1)$——谷翻转、Chern 不变。可纹理化（有限谷刚度），宽度 $\xi\sim a_M[\rho_v/(a_M\Delta_{\rm max}/w)]^{1/3}$ 📜Q。承载**对向传播**模，Luttinger 参数可被前向散射重整化、可被背散射开隙（若含微观 $U_v(1)$ 破缺项）📜Q。
  3. **交织壁**：$(m_z,n_z)\to(-1,-1)$——Chern 与谷同时翻转。中心带电荷密度在 moiré 尺度调制 → 交织壁被 moiré 势**钉扎**在 AA 区间半奇数位置，长寿命**亚稳**态 📜Q。
- 换号衬底 $\Delta(\mathbf r)$ 强制存在 Chern 或谷壁（钉在 $\Delta=0$ 线）；均匀衬底则交织壁可自由传播但被 moiré 势钉扎 📜Q。

### 2.2 数值方法（Sec. III）

- 连续模型（BM）：$w_{AA}=0.08$ eV、$w_{AB}=0.11$ eV（含褶皱效应），$v_0\approx9\times10^5$ m/s，截断 228 带/自旋/谷 📜Q（附录 A，Eq. A1–A8）。
- **FHS 方法**：把相互作用 + 空间变化衬底 $\Delta(\mathbf r)$ 投影到中心带（衬底为零时中心带-远带能隙大，>99% 重叠验证）📜Q。双栅屏蔽库仑 $V(q)=\frac{2\pi e^2}{\epsilon_r q}\tanh qd$、$d=40$ nm、$\epsilon_r=9.5$；$V_{\rm HF}$ 方程（Eq. C2–C9）📜Q。
- **HFWQ 态**：HF 能带的 Wannier-Qi 轨道作参考基，初始 HF 投影由其组合；$\nu=+3$（7 条填充带，$\mathrm{Tr}P(k_2)=7N_1$）📜Q。自洽求解得到（亚）稳态的 Chern 或谷壁解 📜Q。

### 2.3 结果（Sec. IV）

- **能差相图**（Fig. 1，$(\theta,\Delta_{\rm max}/w)$ 平面）：小衬底梯度→谷壁有利（更多纹理化降交换能）；小角度→Chern 壁有利；$\theta<1.05°$ 的等值线为虚线（远带能隙变小、惰性远带近似变差）📜Q。超越 HF 的修正（RPA、双计数方案）可移定量相界，但 Chern-谷竞争是**普遍特征** 📜Q。
- **宽度标度**（Fig. 3，$\theta=1.2°$）：谷壁 $\xi$ 由衬底梯度控制，指数 $-1/3$ 与 Ginzburg-Landau 预言一致；大衬底时标度区被 moiré 尺度截断；Chern 壁锐利（$\xi\ll a_M$）、与 $\Delta_{\rm max}/w$ 无关（大 easy-axis 各向异性 $\beta$ + 拓扑论证抑制跨 Chern 相干）📜Q。
- **交织壁**：均匀 $\Delta(\mathbf r)$ 下稳定在 AA 区间半奇数位置；最大系统尺寸 + 多种初值仍不弛豫到均匀解 → 只能以 $a_M\sim14$ nm 步长增长/收缩 → 长寿命亚稳 📜Q。DW 张力 $\sim4$ meV/$a_M$（Fig. 10）→ 居里温度 $\sim40$ K 📜Q。

### 2.4 输运/探针含义（Sec. V）与有限温（附录 K）

- 渗流 Chern/交织壁 → 手征 DW 网络（类**加倍 Chalker-Coddington** 网络），描述 Hall 电导差 $2e^2/h$ 的两 QH 平台间相变 → **宏观 QAH 响应被破坏** 📜Q。
- 谷壁主导 → 对向传播模受 $U(1)_v$ 保护；微观 $U(1)_v$ 破缺可开隙 → "轨道铁磁、谷无序"基态（**QH 随机场顺磁体**）📜Q。
- 有限温 Ising 相变（附录 K）：小衬底斜率典型 DW 张力 $\sim0.5$ meV/$a_M$ → $T_c\sim13\ \text{K}\times\xi_{\rm dis}/a_M$；实验 $T\sim2$ K、畴尺寸 $\xi_{\rm dis}\sim1\ \mu m$ 时相变温度过高、不相关 → 除非接近相界，否则样品要么纯 Chern 壁、要么纯谷壁 📜Q。
- 衬底调制还产生远高于费米能的额外束缚态（交织壁无）→ 可用 STM（单栅样品）区分两区 📜Q（附录 I/J）。

---

## 3. 结论清单（分层）

### 3.1 定理式主张（拓扑/对称论证的产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| 三类 DW 分类 | Chern 壁/谷壁/交织壁（按 $(m_z,n_z)$ 极限行为） | A1–A4 |
| Chern 壁手征模 | Chern 差 $\pm2$ 的畴缝必承载（至少）一对共传播手征模，背散射被手征性禁戒 | A1、A4 |
| 谷壁非手征模 | 谷翻转畴缝承载对向传播模，Luttinger 参数可重整化 | A1、A4 |
| Chern 壁锐利 | 跨 Chern 相干区拓扑被迫含涡旋 → 不纹理化、宽度衬底无关 | A2 |

### 3.2 估算（经验/近似，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 谷壁宽度标度 | $\xi\sim a_M[\rho_v/(a_M\Delta_{\rm max}/w)]^{1/3}$（指数 $-1/3$） | A3、变分（附录 F） | 📜Q[~]（Fig. 3 标度 collapse 支持） |
| Chern 壁宽度 | $\propto\beta a_M$（衬底无关） | A2 | 📜Q[~] |
| 交织壁张力 | $\sim4$ meV/$a_M$ → 居里 $\sim40$ K | 附录 H | 📜Q[~] |
| 谷壁张力（小斜率） | $\sim0.5$ meV/$a_M$ → $T_c\sim13\ \text{K}\times\xi_{\rm dis}/a_M$ | 附录 K | 📜Q[~] |
| Hall 电导差 | $2e^2/h$（Chern/交织壁网络） | A1 | 📜Q[~] |

### 3.3 预言（可检验性 → §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 三类畴壁存在于 hBN-TBG OCI | "We have proposed the existence" 📜Q | 中——STM/谱函数 |
| 部分 $\nu=+3$ 样品 QAHE 缺失的候选解释 | "provide a candidate explanation" 📜Q | 弱——现象解释 |
| 手征 DW 网络破坏宏观 QAH 响应 | "macroscopic QAH response is always destroyed" 📜Q | 中——输运 |
| 交织壁亚稳（moiré 钉扎） | "suggests ... long-lived metastable" 📜Q | 中——扫描探针 |
| 电流驱动磁化反转的钉扎相关性 | "likely relevant to" 📜Q | 弱——后续 |

### 3.4 内部验证（自洽核对）

1. **标度 collapse**：Fig. 3 谷壁宽度对 $\Delta_{\rm max}/w$ 的标度 collapse 与 Eq. (1) 的 $-1/3$ 预言一致（大 $\Delta_{\rm max}/w$ 处因 moiré 物理偏离）📜Q。
2. **FHS vs CM 互验**：固定 Hilbert 空间方法 vs 直接连续模型（含衬底）的带能差（Fig. 5）与子空间重叠（Fig. 6，>0.99）验证投影合法 📜Q。
3. **双扣除方案对照**：$\nu_0=+4$ 与解耦层双扣除方案相图定性一致（定量相界不同）📜Q（Fig. 7）。
4. **单栅 vs 双栅屏蔽对照**：屏蔽形式不显著影响结果 📜Q。

### 3.5 概念区分（分类）

| 区分 | 依据 | 结论 |
|---|---|---|
| Chern 壁 vs 谷壁 vs 交织壁 | $(m_z,n_z)$ 跨越 DW 的变化 📜Q | 三类，能量竞争 |
| OCI 畴壁 vs AB/BA 螺旋态 | 前者在 QAHE 轨道 Chern 绝缘态、后者在偏压 mTBG 📜Q | **严格区分**（本文明说 distinct） |
| 手征 vs 非手征边缘模 | Chern 壁共传播 / 谷壁对向传播 📜Q | 输运性质不同 |
| 亚稳交织壁 vs 基态 | 交换能损失 → 永非基态，但 moiré 钉扎 → 长寿命 📜Q | 动力学亚稳 |

---

## 4. 假设-结论依赖图

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A7 HF 近似 | 强关联涨落（RPA 等） | 定量相界移动 | 作者声明定量移动但定性（竞争存在）稳健 📜Q |
| A2 子格极化标签 | 偏离 chiral 极限 | 中心带结构细节 | 作者声明物理上仍合理保留标签 📜Q |
| A4 忽略谷间散射 | $\theta\gtrsim1$ 谷间散射增强 | 谷壁受 $U(1)_v$ 保护的结论 | 作者声明 $\theta\lesssim1$ 抑制 📜Q |
| A3 衬底缓变 | 衬底锐变（moiré 尺度） | GL 标度 $\xi\sim a_M[\rho_v/(a_M\Delta/w)]^{1/3}$ 失效（标度区被 moiré 截断） | Fig. 3 大 $\Delta/w$ 偏离即证 📜Q |
| A5 中心带-远带能隙大 | $\theta<1.05°$ 远带隙变小 | FHS 惰性远带近似变差 | Fig. 1 虚线标注 📜Q |
| A6 屏蔽库仑 | 屏蔽形式/参数变化 | 定量相界 | 作者验证单/双栅差异不显著 📜Q |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- 局域单粒子谱函数 $A(\omega,r)$（附录 I，STM 隧穿电导）区分 Chern/交织/谷壁 📜Q；
- 手征 DW 网络 vs 谷 DW 网络的宏观输运（QAHE 有无）📜Q；
- 衬底调制诱导的远离费米能束缚态（Chern/谷壁有、交织壁无）→ STM 区分两区 📜Q。

### 5.2 设计原则（畴壁类型学）

$\Delta_{\rm max}/w$（衬底梯度）与 $\theta$（扭角）作两个"旋钮"调谐 Chern/谷壁竞争；均匀衬底 → 交织壁亚稳 📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- 本文与 **T15/T18（De Beule 网络）** 的 Chalker-Coddington 网络语言呼应，但对象不同（QAHE 轨道 Chern 绝缘体 vs 偏压 mTBG 谷霍尔网络）。
- 本文**明确区分**于 San-Jose & Prada 2013（T05）的 AB/BA 螺旋畴壁态 📜Q（正文 "distinct from the helical states ... between AB/BA stacking regions"）。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| HF 近似 | 超越 HF 修正（RPA）会移定量相界 | 📜Q（作者自述） |
| 双计数方案依赖 | $\nu_0=+4$ 与解耦层方案定量不同 | 📜Q（Fig. 7） |
| 网络输运未定量 | 手征/非手征 DW 网络的电导未计算 | 📜Q（讨论定性） |
| 忽略谷间散射 | 谷壁的 $U(1)_v$ 保护依赖之 | 📜Q |
| 近魔角远带近似变差 | $\theta<1.05°$ 惰性远带近似变差 | 📜Q（Fig. 1 虚线） |

## 7. 与其他工作的关系（跨论文对标）

| 工作 | 关系 |
|------|------|
| Sharpe 2019 (ref 4)、Serlin 2020 (ref 5)、Tschirhart 2021 (ref 6) | **直接引用**——$\nu=+3$ QAHE 实验（零场霍尔、量子化、轨道极化）📜Q |
| Bultinck 2020 (ref 7)、Zhang 2019 (ref 9) | hBN 稳定 $C=\pm1$ 态的机制理论 📜Q |
| Bistritzer-MacDonald 2011 (ref 10) | 连续模型来源 📜Q |
| Khalaf-Chatterjee-Bultinck-Zaletel 2021 (ref 33)、Khalaf-Bultinck 2020 (ref 34) | CP³ NLSM 软模理论来源 📜Q |
| Agarwal 2019 (ref 29)、QHFM 畴壁系列 (refs 25–31) | 量子霍尔铁磁体畴壁先驱 📜Q |
| San-Jose & Prada 2013 (ref 24, =T05) | 本文明说畴壁**不同于** AB/BA 螺旋态 📜Q |

> ⚠️ Phase S 外部对标（**非本文引用**，时间倒挂 💭I）见 §5.3。

## 8. 对后续研究的影响

- 建立 QAHE 畴壁的**类型学 + 能量竞争框架**（Chern/谷/交织壁 + 衬底梯度/扭角两旋钮）📜Q。
- 为"QAHE 样品间差异"提供候选机制解释（渗流手征网络破坏宏观 QAH）📜Q。
- 提出"手征 + 非手征混合网络"为开放问题 📜Q。

## 9. 理论模型映射（供计算对标）

| 映射 | 说明 |
|------|------|
| Eq. (1) GL 自由能 → 相场模拟 | $m_z,n$ 双序参量自由能可作相场/变分对标 📜Q |
| CM + FHS → HF | 本文 HF 流程（附录 C）是 QAHE 畴壁 TB 计算的直接对标对象 📜Q |
| $\xi\sim a_M[\rho_v/(a_M\Delta/w)]^{1/3}$ → 宽度标度 | 供数值宽度提取对标 📜Q |
| DW 张力 $\sigma=(E_{\rm Chern}-E_{\rm valley})/(2a_M N_2)$ | 供能量分解对标（附录 G）📜Q |

---

## Phase S 目的接口（引用式）

- **Q1（edge state 如何表征）**：QAHE 畴壁的边缘模表征 = Chern 壁（手征共传播、Luttinger 参数锁非相互作用值）vs 谷壁（非手征、可重整化）——**与 AB/BA 螺旋态是不同对象**，须严格区分 📜Q。
- **Q2（理论如何解释）**：有效场论（$m_z$=Chern、$n$=谷）+ HF 数值解释畴壁类型与能量选择（衬底梯度↔纹理化 ↔ 交换能竞争）📜Q。
- **Q3（理论↔实验对应）**：$\Delta_{\rm max}/w,\theta$ ↔ 器件衬底/扭角；手征网络破坏 QAHE ↔ 样品间 QAHE 差异；STM 谱函数 ↔ 探针信号 📜Q。

> **增量价值**：为 QAHE（关联 Chern 绝缘体）畴壁提供类型学，与 T05/T09/T12/T15/T18（**偏压 mTBG 谷霍尔网络**）分属两套体系；比前者多 = 强关联 HF + 衬底畴壁竞争；少 = 无散射网络/谷 Chern 输运定量。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取到 `/tmp/T20.txt`，逐项 grep 核对：**全部数字命中原文**——

| 数字 | grep 命中位置 | 结论 |
|------|--------------|------|
| $\nu=+3$、$C=\pm1$、$C=\sigma_z\tau_z$ | 摘要 / Sec. II | ✓ 📜Q |
| $w_{AA}=0.08$ eV、$w_{AB}=0.11$ eV、$v_0\approx9\times10^5$ m/s | 附录 A | ✓ |
| $d=40$ nm、$\epsilon_r=9.5$、$V(q)=\frac{2\pi e^2}{\epsilon_r q}\tanh qd$ | Sec. III | ✓ |
| $a_M\sim14$ nm、$a=1.42$ Å、$k_D=4\pi/3\sqrt3a$ | 引言 / 附录 A | ✓ |
| $\xi\sim a_M[\rho_v/(a_M\Delta_{\rm max}/w)]^{1/3}$、指数 $-1/3$ | Sec. II / Fig. 3 | ✓ |
| 228 带/自旋/谷、$7N_1$（$\nu=+3$） | 附录 A / Sec. III | ✓ |
| $N_1=N_2=10$、$2w=3a_M$（Fig. 1）、$\theta=1.2°$（Fig. 3） | Fig. captions | ✓ |
| $\Delta_{\rm max}=20$ meV（Fig. 11） | Fig. 11 caption | ✓ |
| DW 张力 $\sim4$ meV/$a_M$ → $\sim40$ K；$\sim0.5$ meV/$a_M$ → $T_c\sim13\ \text{K}\times\xi_{\rm dis}/a_M$ | Sec. IV / 附录 K | ✓ |
| Hall 电导差 $2e^2/h$ | Sec. V | ✓ |
| 石墨烯-hBN 失配 $\sim2\%$ | 引言 | ✓ |

⚠️ 修正/降级：① 旧版 Q2 "缠绕壁" → 统一"交织壁"（intertwined walls）；② 旧版"交织壁被摩尔晶格钉扎"保留（moiré 电荷密度调制钉扎）；③ 本文**明确区分** OCI 畴壁与 AB/BA 螺旋态，已在 §3.5/§5.3 显式标注；④ 未引入 $4e^2/h$（本文出现的是 Hall 电导**差** $2e^2/h$，非电导平台）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-06 | 初读（粗读版） |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧版归档 `archive/paper_review_T20_kwan2021_prb.backup_20260908.md`。补：GL 自由能 Eq. (1) + 序参量表、参数分册、8 条假设清单、推导链（Sec. II→V）、结论分层、假设-结论依赖图、反向核对 pass。 |
| 2026-09-08 | **降级/删除**：① 旧版 "交织壁" 与 Q2 "缠绕壁" 不一致 → 统一"交织壁"；② 旧版 "Chern 壁携带手征边缘模、谷壁携带非手征模" 保留并精确化（Chern 壁=共传播手征、谷壁=对向传播非手征，Luttinger 参数后果区分）；③ 补充 "QAHE 畴壁 ≠ AB/BA 螺旋态" 的显式区分（本文原文明说 distinct）。 |
