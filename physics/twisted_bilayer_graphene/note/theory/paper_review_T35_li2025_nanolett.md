<!--
 * @Author       : AI 精读（白箱演绎结构）
 * @Date         : 2026-08-11（初读）→ 2026-09-02（4 块辨识结构，理论版）→ 2026-09-08（按 5 块演绎结构重写，旧版归档）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T35_li2025_nanolett.md
 * @Description  : T35: Li, Chen & Yao 2025 Nano Lett — 大转角 intervalley Umklapp 散射拓扑畴壁态（2026-09-08 按 5 块演绎结构重写：模型白箱/推导链/结论清单/假设-结论依赖图/接口）
-->

# Paper Review: Li, Chen & Yao (2025) — 大转角 Umklapp 散射拓扑畴壁态

| 字段 | 内容 |
|------|------|
| **编号** | T35 |
| **标题** | Topological Domain-Wall States from Umklapp Scattering in Twisted Bilayer Graphene |
| **作者** | Juncheng Li, Cong Chen*, Wang Yao* |
| **期刊** | Nano Lett. 2025, 25, 17025−17031（Received Aug 4 2025 / Published Nov 28 2025）📜Q |
| **DOI / arXiv** | 10.1021/acs.nanolett.5c04006 / arXiv:2508.03761（⚠️ 外部来源，正文未出现） |
| **类型** | 理论 — 大转角 intervalley Umklapp 散射畴壁态 |
| **课题组** | Wang Yao / Cong Chen group (University of Hong Kong) |
| **PDF / SI** | ✅ `reference/pdfs/Li 等 - 2025 - Topological Domain-Wall States from Umklapp Scattering in Twisted Bilayer Graphene.pdf`（正文 + SI） |
| **精读日期** | 2026-08-11（初读）→ 2026-09-02（4 块辨识结构）→ 2026-09-08（5 块重写） |

> **结构说明**：本篇按「理论论文演绎结构」的五块记（见 `note/shared/method/theory_paper_reading.md` §3）：**① 模型白箱 → ② 推导链 → ③ 结论清单（分层）→ ④ 假设-结论依赖图 → ⑤ 接口**。理论论文无黑箱、无反推、无可辨识实验（是"白箱演绎"而非"黑箱溯因"），故不用"四层变量表 + 判别表"这套实验框架词汇（旧 4 块版已废弃）。
> **共享知识引用**：valley Chern / Berry 相位 / chiral vs helical 见 `[PHY-BERRY]`；阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。⚠️ 本文畴壁态机制（Jackiw–Rebbi 型 λ 符号反转）与 `[PHY-BERRY]` 的 AB/BA valley Chern 数差畴壁机制是**两类**，§2.4/§7 显式对照。

---

## TL;DR

**本文想解决的问题**：大转角 TBG（θ ≈ ±21.8°）的低能物理是否由 **intervalley Umklapp 散射**主导，并能否在「手性反转界面」上产生拓扑畴壁态——即一种独立于小转角 mTBG「AB/BA 畴壁」范式的新机制？

**主结果**（全文无实验数据，均为理论预言 + 数值自洽）：① 大转角下同谷 Dirac 点远分离（抑制 intravalley 散射）、反谷 Kt/K′b 在 mBZ 角重叠 → **intervalley Umklapp 散射主导低能**；其隧穿能标 ~2 meV「不足以」显著重整化能带 → 能带高度色散、e–e 相互作用可忽略 📜Q；② 手性耦合 λ 印迹堆垛手性：D6 构型 gapped + hidden BHZ 拓扑，D3 构型 semimetallic + quadratic band crossing 📜Q；③ 手性反转（ζ=+ ↔ ζ=−）界面 → **Jackiw–Rebbi 型拓扑畴壁态** = 反向传播赝自旋模（两条零能模），即使两侧 bulk 能带与拓扑不变量**相同** 📜Q；④ 对称破缺微扰（Δs=15 meV）+ 7% 单轴应变 + 3.2–3.5 Å 层间距 + 22.79° 小偏角 + hBN 衬底下态稳健存活 📜Q。

**结论/意义**：作者表态「our work unveils a novel approach to achieving robust topological channels」「open new pathways for engineering domain-wall states in twisted materials」——大转角 + 结构手性 = 畴壁态工程的新参数空间（理论预言，非实验证实）📜Q。

---

## 1. 模型白箱（理想系统 + 假设清单）

> 理论论文的研究对象是**白箱**——作者自写的理想模型，无需"反推内部"。本节只做两件事：**写下模型**（§1.1），**列出它成立的全部假设**（§1.3）。假设清单是本文一切结论的"前提集合"，§4 的依赖图据此展开。

### 1.1 对称约束 k·p 有效模型

**结构**：θ 满足 $\cos\theta=(3m^2+3mn+n^2/2)/(3m^2+3mn+n^2)$（Eq. 1）；(m,n)=(1,1) 给最小 commensurate 转角 θ≈±21.8°；moiré 超胞 28 atoms、原胞矢量相对单层拉长 7 倍、实空间 moiré 周期 Li/7（7 倍收缩）📜Q。三种高对称构型：D6（绕六角中心转，space group No. 177，保留 C3z+C2z+C2x）/ D3（tA–bB，No. 150，破 C2z）/ D3′（tB–bA）；位移 d=±(L1+L2)/21 使 D6↔D3/D3′ 互转 📜Q。

**层间耦合分区**：T 分解为 **P 保持（M，非手性）+ P 破缺（λ，手性）** 两项；λ 是反演破缺标志，解除镜像对称简并、把系统劈成左手（ζ=+）/右手（ζ=−）📜Q。D6 四带低能模型（Eq. 3–4）；D3 到 q² 阶（Eq. 5–6，含 p 波手性耦合 + f(q) 三角翘曲项）；D3′ 经 C2z 与 D3 联系（Eq. 7）📜Q。

**变量含义表**：

| 符号 | 含义 | 值/定义 |
|---|---|---|
| $\theta$ | 扭角 | ±21.8°（主）、13.8°、22.79°、4° 对照 |
| $\zeta$ | 结构手性 | ±（左右手，λ 符号） |
| M | 层间耦合非手性项（P 保持） | 4.70 meV（D6）/ 5.40 meV（D3） |
| $\lambda$ | 层间耦合手性项（P 破缺） | 1.31 meV（D6） |
| $\Delta_s$ | 对称破缺微扰强度 | 15 meV |
| $\hbar v_F$ | 费米速度 | 6.61 eV·Å（D6）/ 6.43 eV·Å（D3） |

### 1.2 参数分册（替代旧"四层变量表"：区分"作者设定" vs "推导所得"）

| 类 | 内容 |
|----|------|
| **自由参数（旋钮）** | $\theta$（±21.8°/13.8°/22.79°/4°）、结构手性 $\zeta=\pm$、堆垛（D6/D3/D3′）、层间位移 d、微扰 $\Delta_s$、层间距（3.2–3.5 Å）、7% 单轴应变、hBN 衬底 |
| **导出量（由旋钮+常数算出）** | moiré 超胞（28 atoms）、moiré 周期 Li/7（7 倍收缩）、mBZ 角 Km/K′m、Dirac 锥动量分离（C2/C4 同心圆） |
| **模型内部量（解的性质）** | k·p 哈密顿 $H_{D6}/H_{D3}$、层间耦合 T=M+λ、bulk 能隙、hidden BHZ 拓扑、ζ 投影赝自旋织构、in-gap 零能模、能带几何量 ωn(k) |
| **固定参数（拟合，非旋钮）** | D6：ℏvF=6.61 eV·Å、M=4.70 meV、λ=1.31 meV；D3：ℏvF=6.43 eV·Å、ℏ²v²/2m=10.40 eV·Å²、ℏv⊥=7.32 meV·Å、M=5.40 meV（由 a-SKTB 低能带拟合） |
| **预言量（可检验）** | 畴壁能谱（Fig 4b,c / Fig 5）、bulk 能带（Fig 3）、ωn(k) 色标 |

> 无"反推量 θ̂"层——纯理论论文，M/λ/vF 由 SKTB 低能带拟合（非谱学/输运反推）。

### 1.3 显式假设清单（本文结论的前提集合）

| # | 假设/近似 | 属于 | 出处 |
|---|---|---|---|
| A1 | **k·p 模型截断到低能**（高阶项远离 K/K′ 才显著，对低能可忽略；对光学响应等可能关键） | 模型 | 📜Q |
| A2 | **单粒子图景**（e–e 只定量重整化参数、不诱发 band inversion/gap closure） | 模型 | 📜Q |
| A3 | **理想周期 moiré**（真实无序仅抽查典型：应变/层间距/偏角/hBN） | 模型 | 📜Q |
| A4 | **21.8° 下 D6 vs D3 能量差可忽略 → 抑制晶格重构** | 模型 | 📜Q |
| A5 | **intervalley Umklapp 隧穿能标 ~2 meV 不足以重整化能带** | 推导 | 📜Q |
| A6 | **平坦边界 x=0 + qy 好量子数**（畴壁模型） | 推导 | 📜Q |

> 判别性扫轴：θ（±21.8°/13.8°/22.79°/4°）、ζ=±、堆垛（D6/D3/D3′）、Δs（15 meV）/应变（7%）/层间距（3.2–3.5 Å）/hBN——均为计算扫参。这些假设在 §4 逐一映射到"失效 → 结论崩塌"。

---

## 2. 推导链（演绎结构：顺论文顺序，每步"输入→输出→所用假设/定理→合法域"）

### 2.0 总览：论文是一条演绎链

| 层 | 论文节 | 输入 | 输出 | 所用假设/定理 | 合法域 |
|---|---|---|---|---|---|
| 前提定理层 | 引言 | 小转角 intravalley 范式（已知） | 大转角 intervalley Umklapp 主导 | Umklapp 条件 Eq.2 | θ≈21.8° |
| 模型层 | 结构 + Umklapp | commensurate 结构 + k·p 模型 | D6/D3 构型 + 能标 | A1–A5 | 大转角 |
| 推导层 | D6/D3 能带拓扑 | 手性耦合 λ | D6 gapped+BHZ / D3 semimetallic | 对称性分类 | — |
| 推导层2 | 畴壁 Jackiw–Rebbi | ζ=+ ↔ ζ=− 界面 | 两条反向传播零能模 | A6、λ 反转 | qy=0 |
| 边界层 | 稳健性 | 微扰 + 现实无序 | in-gap 模存活 | — | — |

### 2.1 前提定理层（引言）：小转角 vs 大转角主导散射

- **小转角**：同谷 Dirac 锥接近，**intravalley** 主导（连续模型基础 + 平带 + 多体）📜Q。
- **大转角**：同谷 Dirac 点远分离（抑制 intravalley），反谷 Kt/K′b 在外同心圆接近——13.8° 在 C4 圆重叠、21.8° 在 C2 圆重叠（更接近原点）→ **intervalley Umklapp 主导低能** 📜Q（Fig. 2b）。
- **Umklapp 条件**（Eq. 2）：$k_1+G_t=k_2+G_b \Rightarrow G=k_1-k_2=G_b-G_t=G_m$（moiré 倒格矢参与散射）📜Q。

### 2.2 模型层：commensurate 结构 + 能标自洽

- **21.8° 结构**：28 atoms、原胞矢量拉长 7×、周期 Li/7 📜Q；D6↔D3/D3′ 经 d=±(L1+L2)/21 平移互转 📜Q。**与小转角区别**：21.8° 下 D6 vs D3 能量差可忽略 → **抑制晶格重构**（动量空间折叠 vs 实空间重构的对立）📜Q。
- **能标自洽**：intervalley Umklapp 隧穿能标 **~2 meV**「不足以」诱导显著能带重整化 → 能带高度色散 → e–e 相互作用可忽略 📜Q。
- **隙与拓扑**：Kt 与 K′b 折叠到 mBZ 角 Km 后简并 → intervalley Umklapp 在 Dirac 点打开 hybridization gap + 引入非平凡拓扑 📜Q。

### 2.3 推导层：D6 vs D3 能带拓扑（λ 印迹手性）

- **对称性定构型**：D6（No. 177）保留 C3z+C2z+C2x；D3（No. 150）破 C2z（其余面内转动全破）📜Q。
- **手性耦合 λ**：T = M（非手性 P 保持）+ λ（手性 P 破缺）；λ 解除镜像对称简并、劈成 ζ=± 左右手 📜Q。
- **D6**：gapped + **hidden BHZ-like 拓扑** 📜Q；**D3**：semimetallic + **quadratic band crossing**（q² 项不可或缺）📜Q。
- **模型参数**（Fig. 3 caption）：D6 → ℏvF=6.61 eV·Å、M=4.70 meV、λ=1.31 meV；D3 → ℏvF=6.43 eV·Å、ℏ²v²/2m=10.40 eV·Å²、ℏv⊥=7.32 meV·Å、M=5.40 meV 📜Q[~]。k·p 复现 a-SKTB 能带色散**与**能带几何量 ωn(k)（ζ 敏感）📜Q。

### 2.4 推导层2：手性反转 → Jackiw–Rebbi 拓扑畴壁态（核心预言）

- **问题设定**：ζ=+ 与 ζ=− 两侧 bulk 能带色散与二阶拓扑**相同**，但界面拓扑畴壁模是开放问题 📜Q。
- **畴壁模型**（Eq. 9–11）：平坦边界 x=0，左手 tBG（ζ=+）占 x<0、右手（ζ=−）占 x>0；qy 边界好量子数、$q_x\to-i\hbar\partial_x$；qy=0 处解出**两条指数局域零能模** $\psi_{1,2}$，投影得 $H_{\rm edge}=\hbar v_F q_y\sigma_y$ 📜Q。
- **关键判别**：态存在于 bulk 能带与拓扑不变量**相同**的界面——band-crossing 来自内禀 bulk 参数 **λ 的符号反转** = Jackiw–Rebbi mass inversion 📜Q。⚠️ 排除「畴壁态由两侧 valley Chern 数差产生」的 mTBG 机制（本文畴壁两侧拓扑相同）。
- **M=0 极限与 BHZ 映射**：M=0 时 $\psi_{1,2}$ 是 $\hbar v_F q_y\tau_0\sigma_y$ 本征态（本征值 ±ℏvF）= 手性模沿 y 反向传播；有限 M 混合赝自旋通道但不毁拓扑（类比 BHZ 面内 Zeeman field）📜Q。单式变换 $U^\dagger H_{D6}U=\hbar v_F\tau_0\cdot q+(\lambda/2)\tau_z\sigma_z$（Eq. 12）映射到 BHZ（QSH）；M 对应有效 exchange field，破 TRS 但不毁拓扑 📜Q。
- **数值确认**：a-SKTB 谱确认 in-gap band-crossing 模（Fig. 4b,c 红线）📜Q。**术语辨析**：摘要称 "counterpropagating pseudospin modes"；机制是 K/K′ 谷锁定反向（helical，QVH 畴壁态），非总电荷手征 QH 边缘通道（[PHY-BERRY]）💭I。

### 2.5 边界层：稳健性（对称破缺 + 现实无序）

- **三种 on-site 微扰**（Fig. 5a–c，Δs=15 meV）：C2z 破缺 $H_s^{(1)}=\Delta_s\tau_z\sigma_z$、C2z+C2x 破缺 $H_s^{(2)}=\Delta_s\tau_0\sigma_z$、C2x 破缺 $H_s^{(3)}=\Delta_s\tau_z\sigma_0$ → in-gap 模均存活（SKTB 佐证 Fig. S2）📜Q。
- **现实无序**：层间距 3.2–3.5 Å ✅；7% 面内单轴应变（破 C3z）✅；22.79° 小偏角 ✅；hBN 衬底 ✅；e–e 仅定量重整化 ✅ 📜Q。
- **generic tBG 推广**：任意层间位移 H = H_D6 + Δ，只要 Δ 不闭合 bulk gap 则畴壁态存活；θ=21.8° 随机位移下 band-crossing 存活（Fig. 5e,f）📜Q。**⚠️ 末尾注**：ζ 反转畴壁态在 gapless 区消失，但 **valley-Chern 主导**的拓扑通道出现（D3/D3′ 界面，见 SI）📜Q。

---

## 3. 结论清单（分层：定理 / 估算 / 预言）

> 理论论文的结论必须按**性质**分层，而非平铺。每条标：**依赖假设** + **可检验性**。

### 3.1 定理式主张（数学/对称性论证的产物）

| 主张 | 内容 | 依赖假设 |
|---|---|---|
| Umklapp 主导 | 大转角 intervalley Umklapp 散射主导低能（同谷远分离、反谷重叠） | A4、A5 |
| D6/D3 拓扑区分 | λ 印迹手性：D6 gapped+BHZ / D3 semimetallic+quadratic crossing | 对称性分类 |
| 畴壁态来源 | 手性反转 → Jackiw–Rebbi（λ 符号反转），两侧拓扑不变量相同 | A6 |
| BHZ 映射 | 单式变换映射到 BHZ（QSH），M=exchange field 不毁拓扑 | 单式变换 U |

### 3.2 估算（数值算例，非严格定理）

| 估算 | 值 | 依赖假设 | 证据 |
|---|---|---|---|
| 主算例转角 | ±21.8°（(m,n)=(1,1)） | Eq. (1) | 📜Q[~] |
| Umklapp 隧穿能标 | ~2 meV「insufficient」 | A5 | 📜Q[~] |
| D6 模型参数 | ℏvF=6.61 eV·Å、M=4.70 meV、λ=1.31 meV | Fig. 3 caption | 📜Q[~] |
| D3 模型参数 | ℏvF=6.43 eV·Å、ℏ²v²/2m=10.40 eV·Å²、ℏv⊥=7.32 meV·Å、M=5.40 meV | Fig. 3 caption | 📜Q[~] |
| 对称破缺微扰 | Δs=15 meV | Fig. 5 caption | 📜Q[~] |
| 稳健性参数 | 层间距 3.2–3.5 Å、7% 应变、22.79°、hBN | Fig. S5–S7/5d | 📜Q[~] |
| 畴壁零能模数 | 两条（ψ1,2，反向传播） | Eq. (10) | 📜Q[~] |

### 3.3 预言（可检验性 → 见 §5.1）

| 预言 | 作者措辞强度 | 可检验性 |
|---|---|---|
| 手性反转界面拓扑畴壁态 | "predict / demonstrate"（理论构造 + 数值）📜Q | 中——尚未实验 |
| 稳健拓扑通道工程新路径 | "unveil a novel approach"、"open new pathways"（定性表态）📜Q | 弱——定性 |
| chiral transport 现象 | 定性（"chiral transport engineering/phenomena"）📜Q[相对] | 弱——无定量信号 |

### 3.4 内部验证（自洽核对，非"排除竞争解释"）

1. **k·p ↔ a-SKTB 互验**：能带色散 + ωn(k) 几何量均复现 📜Q。
2. **解析 ↔ 数值互验**：解析零能模 ↔ 数值 in-gap band-crossing 模（Fig. 4b,c 红线）📜Q。
3. **BHZ 单式映射 ↔ hidden BHZ 拓扑互验** 📜Q。

### 3.5 概念区分（作者论证中的"分类"，非溯因排除）

| 区分 | 依据 | 结论 |
|---|---|---|
| 小转角 intravalley vs 大转角 intervalley | 同谷 Dirac 点接近 vs 远分离 📜Q | 大转角 Umklapp 主导 |
| D6 vs D3 | C2z 保留（No. 177）vs 破缺（No. 150）📜Q | gapped+BHZ vs semimetallic |
| Chern 数差畴壁 vs Jackiw–Rebbi | 两侧拓扑不同 vs 两侧拓扑相同（λ 反转）📜Q | 本文 = Jackiw–Rebbi |
| 手征 vs 螺旋 | counterpropagating 赝自旋模 = 谷锁定反向（helical）💭I | QVH 畴壁态 |

> 注：这些是**概念/图景分类**（taxonomy），不是实验论文那种"数据排除竞争解释"（溯因排除）——理论论文没有后者。

---

## 4. 假设-结论依赖图（含金量所在）

| 假设 | 失效方式 | 崩塌/改变的结论 | 致命性（作者如何对待） |
|---|---|---|---|
| A4 抑制晶格重构 | 弛豫/重构发生 | 结构图景、D6/D3 区分 | 致命——21.8° 能量差可忽略的前提 📜Q |
| A5 ~2 meV 不足以重整化 | 能标变大的其他角 | 色散带、单粒子图景 | 局部——机制适用域 📜Q |
| A2 单粒子 | e-e 诱发 band inversion | 单粒子拓扑图像 | 作者论证 e-e 仅定量重整化 📜Q |
| A1 k·p 低能截断 | 高阶项（光学响应等） | 低能定量 | 作者明言对光学响应可能关键 📜Q |
| A3 理想周期 moiré | 真实无序 | 畴壁态稳健性 | 抽查了典型无序、未穷尽 💭I |
| 手性反转界面可制备性 | 实验实现 θ=+↔−21.8° 界面 | 实验验证 | 未讨论 💭I |

---

## 5. 接口（可检验性 / 设计原则 / 后续修正）

### 5.1 可检验性（本文预言的实验靶标）

- 畴壁能谱 in-gap band-crossing 模（Fig. 4b,c / Fig. 5）+ 反向传播赝自旋模 📜Q；
- 潜在信号仅定性「chiral transport」（grep "STM"=0、"LDOS"=0 → 无定量实验信号预言）📜Q。

### 5.2 设计原则（大转角畴壁工程）

大转角（θ≈21.8°，抑制晶格重构）+ 结构手性（ζ=±，λ 印迹拓扑）+ 手性反转界面（Jackiw–Rebbi 畴壁态）📜Q。

### 5.3 后续文献修正（时间倒挂，💭I）

- 尚未有实验验证；21.8° commensurate 结构稳定性已实验证实（refs 30–32，引用非本文实验）📜Q。

---

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 实验验证空白 | 全部为理论预言 + 数值自洽，无 STM/输运实验 | 📜Q（无实验） |
| 无定量实验信号预言 | 只给「chiral transport」定性，无 STM/电导/LDOS 定量预言 | 📜Q（grep "STM"=0） |
| k·p 低能截断 | 高阶项对低能可忽略，但作者明言对光学响应等可能关键 | 📜Q |
| 理想周期 moiré | 只抽查典型无序，未穷尽真实样品无序 | 📜Q→💭I |
| 手性反转界面可制备性 | θ=+21.8° ↔ −21.8° 界面如何实验实现未讨论 | 💭I |
| gapless 区 valley-Chern 通道 | 仅一句话提及，D3/D3′ 界面机制见 SI | 📜Q |

---

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）

| 工作 | 关系 |
|------|------|
| 小转角 mTBG（BM 连续模型，refs 15/36/37） | 对照：intravalley + 平带 + 多体；本文 intervalley Umklapp + 色散 + 单粒子 📜Q |
| AB/BA 畴壁（valley Chern，[PHY-BERRY]） | **对照（核心卖点）**：mTBG 畴壁 = 两侧 Cv 相反 → gap 反号；本文 = 两侧拓扑相同、态来自 λ 符号反转（Jackiw–Rebbi）📜Q |
| Park 2019 (ref 20) / Liu 2021 (ref 21) | 2D 二阶拓扑绝缘体（hidden BHZ 与 ζ 二阶拓扑谱系）📜Q |
| Qian 2023 (ref 22) / Chen & Yao 2025 (ref 23) | 3D chiral 拓扑半金属 / 交替扭转多层——Umklapp 谱系 📜Q |
| 21.8° 合成（refs 30–32） | 结构稳定性已实验证实（引用，非本文实验）📜Q |
| Mele 2010 (ref 38) / Moon 2013 (ref 39) | 21.8° 四带低能谱与未扭转双层相似 📜Q |

> ⚠️ Phase S 外部对标（非本文引用）：cards.md 的「突破小转角范式 / 开辟大转角新参数空间」属项目层定性评价 💭I，非本文原话。

---

## 8. 对后续研究的影响

- 开辟「大转角 + 结构手性」畴壁工程新路径（作者 "novel approach"、"new pathways"）📜Q。
- 供计算对标：大转角 σxy / 畴壁 in-gap 模 / 手性反转界面透射（§9）💭I。
- 遗留任务：高阶项对光学响应的作用、gapless 区 valley-Chern 通道、实验信号定量化 💭I→📜Q。

---

## 9. 理论模型映射（供 TBPM / Kubo-Bastin 对照）

| 映射 | 说明 |
|------|------|
| θ → moiré 超胞 | 21.8° → 28 atoms、原胞矢量 7×、周期 Li/7 📜Q |
| 手性 ζ → 结构 chirality | ζ=± ↔ 左右手 ↔ λ 符号 📜Q |
| H_D6 (Eq. 4) → TBPM 哈密顿 | ℏvF=6.61 eV·Å、M=4.70 meV、λ=1.31 meV 📜Q |
| 畴壁 ↔ 界面构型 | θ=+21.8°(ζ=+) ↔ −21.8°(ζ=−) ribbon（Fig. 4a）📜Q |
| 拓扑 ↔ σxy / 边缘态 | hidden BHZ ↔ QSH 类比（helical 反向通道）→ TBPM 可算畴壁 in-gap 模与 σxy 💭I |
| 能标 ↔ 数值网格 | 隧穿 ~2 meV、Δs=15 meV → 需 < meV 能级分辨率 💭I |

---

## Phase S 目的接口（三问引用式）

- **Q1（edge state 如何表征）**：本文是理论，无实验表征；预言 = 畴壁能谱 in-gap band-crossing 模（Fig 4b,c/5）+ 反向传播赝自旋模 📜Q（§2.4）。
- **Q2（理论如何解释）**：大转角 intervalley Umklapp → mBZ 角开隙 → 手性 λ 印迹拓扑；畴壁态 = Jackiw–Rebbi（λ 反转），**非** valley Chern 数差 📜Q（§2.1–2.4）。
- **Q3（理论↔实验对应）**：尚无实验；潜在信号仅定性「chiral transport」📜Q；作者未给 STM/电导定量预言（grep "STM"=0）📜Q。

> **增量价值**：提供与 mTBG 对照的**第二种畴壁机制**——动量空间 Umklapp + Jackiw–Rebbi（λ 反转）vs 实空间 AB/BA valley Chern；供大转角 TBPM 对标（§9）；并纠正旧版两处无源数字（"STM 信号"、"Chern 数决定态数目"）。

## 反向核对 pass (2026-09-08)

`pdftotext -layout` 提取正文到 `/tmp/T35.txt`（507 行），逐项 grep 核对：**全部数字/专名命中原文**——

| 数字/专名 | grep 命中位置 | 结论 |
|------|--------------|------|
| θ=21.8°（18 处）、13.8°、22.79°、4° | 全文 | ✓ 📜Q[~] |
| ~2 meV「insufficient」 | 正文段 | ✓ 📜Q[~] |
| Δs=15 meV | Fig. 5 caption | ✓ 📜Q[~] |
| M=4.70 meV、λ=1.31 meV、ℏvF=6.61 eV·Å | Fig. 3 caption | ✓ 📜Q[~] |
| ℏvF=6.43 eV·Å、ℏ²v²/2m=10.40 eV·Å²、ℏv⊥=7.32 meV·Å、M=5.40 meV | Fig. 3 caption | ✓ 📜Q[~] |
| 28 atoms、7-fold、Li/7 | 正文 | ✓ 📜Q |
| 3.2–3.5 Å、7%、hBN | Fig. S5–S7/5d | ✓ 📜Q[~] |
| Jackiw–Rebbi、BHZ、counterpropagating pseudospin modes | 摘要/正文 | ✓ 📜Q |
| space group 177 & 150、C2 & C4 circle、(m,n)=(1,1)、d=±(L1+L2)/21 | 正文 | ✓ 📜Q |
| cos θ=(3m²+3mn+n²/2)/(3m²+3mn+n²) | Eq. (1) | ✓ 📜Q |

⚠️ 修正/降级：① grep "STM"(0)/"spectroscopy"(0)/"LDOS"(0) → 旧版「STM 预期信号」删除，降级为定性「chiral transport」📜Q[相对]。② grep "number of"(0) + 原文「identical bulk bands and topological invariants」→ 旧版「畴壁态数目由 Chern 数决定」删除，改为「两条反向传播模 + Jackiw–Rebbi」。③ 旧无源数字 "10 meV"(0)/"50 meV"(0)/"~6°~10°~13°"(0)/"1.1° 魔角比较" 已删。④ arXiv:2508.03761 正文未出现 → 头部表已标外部来源。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-20 | **删除转角列表**："(~5-15°)"、"(~6°, ~10°, ~13°)" 无源 → 改为原文算例 θ=21.8°（grep "21.8"=18）、13.8°、22.79°。依据 §B.5#4 |
| 2026-08-20 | **删除 "Umklapp 能隙 10-50 meV"**：无源 → 改原文 "energy scale of ∼2 meV … insufficient" + 模型参数 Δs=15 meV。依据 §B.5#5 |
| 2026-08-20 | **删除 "与超导魔角 (1.1°) 比较"**：原文无此比较（grep "magic" 仅命中参考文献）。依据 QC 跨论文迁移规则 |
| 2026-09-02 | **4 块新架构整体重写**（理论适配）：TL;DR 问题句式 + 四层变量表 + 可辨识性判别表（5 条）+ [前提与限定] + §2 按论文论证结构 + §3 理论模型与方法 + §4 关键预言与数据 + §5–9 + Phase S 接口 + 反向核对 pass |
| 2026-09-02 | **删除无源 "STM 预期信号"**：grep "STM"=0 → 降级为定性「chiral transport」📜Q[相对] |
| 2026-09-02 | **删除无源且矛盾 "畴壁态数目由 Chern 数决定"**：grep "number of"=0，且原文明言「identical bulk bands and topological invariants」→ 改为「两条反向传播赝自旋模 + Jackiw–Rebbi」 |
| 2026-09-08 | **按 5 块演绎结构整体重写**（应用户要求）。旧 4 块版归档 `archive/paper_review_T35_li2025_nanolett.backup_20260908.md`。黑箱三要素/四层变量表/判别表/[前提与限定] → 拆为"模型白箱（k·p 模型+参数分册+6 条假设清单）"+"推导链（前提定理/模型/推导/边界四层）"+"结论清单（定理/估算/预言分层）"+"假设-结论依赖图"+"接口"；内部验证（§3.4）+ 概念区分（§3.5）取代判别表；删"反推量 θ̂"层。全部 📜Q 事实与数字无丢失。 |
