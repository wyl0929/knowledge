<!--
 * @Author       : AI 精读 (系统辨识式阅读法 → 三层分离整理)
 * @Date         : 2026-08-06（初读）→ 2026-09-02（按 4 块新架构重读）
 * @FilePath     : /home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/theory/paper_review_T05_sanjose2013_prb.md
 * @Description  : T5: San-Jose & Prada 2013 — mTBG 层间偏压下螺旋网络（理论 — 螺旋网络模型奠基；2026-09-02 按 4 块辨识结构整体重写）
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
| **精读日期** | 2026-08-06（初读）→ 2026-09-02（按 4 块新架构重读） |

> **共享知识引用**：通用物理（Berry/valley Chern、螺旋 vs 手征、Landauer-Büttiker 通道计数、网络 miniband、双栅偏压）已剥离到 `note/shared/physics/`，本 review 用锚点 `[PHY-BERRY] [PHY-LB] [PHY-MB] [PHY-GATE]` 引用，不重复讲义。阅读疑问见 `note/shared/method/mechanism_questions.md` `[METHOD-Q]`。

---

## TL;DR

**本文想解决的理论问题**：扭角双层石墨烯（TBG）在均匀层间偏压 $U$ 下，能否**不经应变**、仅靠偏压让 AB/BA 畴壁自发承载拓扑保护的螺旋模，并构成一张可编程的二维导电网络？

**主结果**：① 小角度 + 足够大偏压 → AB/BA 区打开能隙、谷陈数符号相反并被电子耗尽 → 畴壁出现**每谷每自旋 2 条**螺旋模（TPH），构成三角 **Chalker-Coddington 型**离域网络（能窗 $|\varepsilon|<|U|/2$）📜Q；② 网络形成经验判据 Eq. (1)：$z^2(l_\perp/L_M)^2 < U/\gamma_\perp < 1$，据此估算 $U\sim90$ meV 需 $L_M\gtrsim290a_0$（$\theta<0.2°$）、100 nm 周期阈值偏压 $\sim45$ meV 📜Q（作者 "estimate"）；③ 谷混合吸附原子/空位可**阻断单条链接** → 作者**提出**"可编程拓扑纳米电子学"（propose / open the possibility；TB 模拟 Fig. 3 支持）📜Q。

**结论/意义**：首次把畴壁物理从"孤立边缘态"推进到"**连通网络**"范式——这是 mTBG 畴壁网络物理的开创性理论。⚠️ 全文为理论预言/估算，作者用词 propose / find / show / estimate / believe，**非已验证事实**（后续 Efimkin 2018 系统化、Tsim 2020 TZM 部分推翻连通性，见 §7/§8）。

---

## 1. 系统辨识导览（判别表为全文唯一权威，机制细节见 [PHY-*]）

**黑箱三要素**：`{输入旋钮：扭角 θ、层间偏压 U、能量 ε | 输出观测量（预言）：DOS 谱、光学电导 σxx(ω)、网络空间密度图案 | 声称结论：偏压下畴壁螺旋模构成可编程导电网络}`

**四层变量图**（符号层一次钉死）：

| 层 | San-Jose & Prada 2013 实例 |
|----|---------------------------|
| **L1 旋钮 u** | $\theta$（扭角）、$U$（均匀层间偏压）、$\varepsilon$（能量，扫谱） |
| **L2 导出量 x₁** | $L_M=a_0/[2\sin(\theta/2)]$、$\varepsilon_M(\theta)=\hbar v_F K/2\approx 88\,\text{meV}\cdot\theta(\text{deg})$、$\Delta K=2|K|\sin(\theta/2)$、$R=L_M/(2\sqrt3)$、$l_\perp=\hbar v_F/\gamma_\perp\approx7.3a_0$、无量纲 $\alpha(\theta)$ |
| **L3 模型量 x₂** | 谷 Chern 数 $C_K$、TPH 模数 $N$、能带 / DOS / 色散、重整化费米速度 $v_F^*$ |
| **固定参数（非旋钮）** | $a_0=2.46$ Å、$|K|=4\pi/3a_0$、层间耦合 $\gamma_\perp\approx0.33$ eV、$v_F$ |
| **反推量 θ̂** | 阈值偏压 $U_{th}$（由 Eq. (1) 反解）、魔角 $\theta_1\approx1.05°$（由 $v_F\to0$ 求）——⚠️ 纯理论，**无实验数据反推** |
| **L4 观测量 y（预言）** | sharp 局域共振 DOS 峰、$\sigma_{xx}(\omega)$、Fig. 2/3 空间概率密度图案、链接"开关" |

> 符号说明：本文 $\gamma_\perp$ 是层间耦合（≈0.33 eV），$l_\perp=\hbar v_F/\gamma_\perp$ 是"层间耦合长度"，二者不同层、不可混用。$\varepsilon_M$ 是低能能标（两 Dirac 锥在 M 点相交能量），不是畴区能隙。

**可辨识性判别表**（理论版：每条判别 = 判据 / 排除谁[竞争图景] / 确立谁）：

| 判别 | 判据（理论/计算） | 排除谁 | 确立谁 |
|------|------------------|--------|--------|
| **大角度 vs 小角度** | $\theta=4°$（$L_M\approx14.3a_0$）加偏压仅平移两 Dirac 锥 $\pm U/2$、$|\varepsilon|<|U|/2$ 内 DOS 平坦（无网络，Fig. 1）📜Q；$\theta\approx0.2°$（$L_M=290a_0$）偏压下 AB/BA 耗尽 → 畴壁网络（Fig. 2）📜Q | 大角度"无网络"图景 | 小角度"螺旋网络"图景（判据 Eq. (1)） |
| **网络态 vs 局域共振态** | 偏共振能区 DOS 弱且无特征 = 离域 TPH 网络态；共振能处 sharp 峰 = 局域于 AB/BA 之外的局域态（Fig. 2 顶部曲线 vs 平滑背景）📜Q | 把 sharp DOS 峰误读为网络 | 两者**并存**：网络（离域）+ 共振局域态（局域） |
| **螺旋 vs 手征** | 有/无时间反演不变性（ref 4）📜Q；本文体系 TRS 保持 | 手征（TRS 破缺，如 QH 边缘）图景 | 螺旋（helical = 谷-动量锁定，ref 15）📜Q |
| **弱保护 vs 强保护** | $N=|C_2-C_1|\mod2$，本文 $\mod2$ 缺省（$N=2$）因仅考虑谷守恒扰动 → "weak" 拓扑保护；谷间散射（吸附原子/空位）可阻断链接（Fig. 3）📜Q | 强拓扑保护（mod 2 不变量）图景 | 弱（谷保护）拓扑保护图景 |
| **平台：TBG vs h-BN** | h-BN 上石墨烯晶格失配无法任意增大 Moiré 周期 → 网络不能完全发展 📜Q | h-BN 作为网络平台 | 扭角双层（可调 $\theta$）作为平台 |

> **主结果 ↔ 判别表映射**：
> - 主结果① 螺旋网络形成（小角度 + 偏压）← {大角度 vs 小角度, 网络态 vs 局域共振态}
> - 主结果② 可编程开关（吸附原子阻断链接）← {弱保护 vs 强保护}
> - 主结果③ 平台选择（TBG 而非 h-BN）← {平台：TBG vs h-BN}
> - （术语前提）helical 而非 chiral ← {螺旋 vs 手征}
>
> **分层排除注**：本文是理论判别（区分参数区间/竞争图景），非实验排除。作者用词 "we find / we show / we estimate / we believe" 📜Q，未用"证明已实现"。

> **[前提与限定]**（判别结论的适用范围）：
> - **扰动/噪声**：① 谷间散射（原子尺度缺陷、空位、小吸附原子）破坏弱保护、可关断链接——这是"开关"的来源也是主要脆弱点 📜Q；② 弹性畸变（偏离理想周期模型）smooth 于晶格尺度 → 不破坏 TPH，反因扩大耗尽区而**增强**网络 📜Q；③ 谷守恒是单谷近似 $C_K\approx\pm\text{sgn}(U)$ 成立的前提（要求 $U$ 与晶格平滑）📜Q。
> - **判别性扫轴**：$\theta$ 轴（$4°\to0.2°$）、$U$ 轴（0–180 meV 扫，Fig. 1/2）、$\varepsilon$ 轴（$|\varepsilon|<|U|/2$ 能窗）；两分量近似仅 $U<\gamma_\perp$ 有效 📜Q。
> - **候选集 M 边界**：{大角度"无网络", 小角度"网络", 局域共振, 强拓扑保护, h-BN 平台}——"螺旋网络"在该集合内由 $\theta/U$ 双轴判别确立；**集外候选未建模**（应变重构、真实无序、多体/关联、魔角平带物理），原文未排除，须声明（封闭世界假设风险）。

三层标注：📜Q = 原文事实（附位置）｜推导 = 由原文公式合成｜📊F = 读图估算｜💭I = 推断。**不确定度（正交轴）**：[±] 原文误差棒 / [~] 原文以 ≈/∼ 给出但无误差棒 / [读图] 图·色标提取 / [相对] 仅相对量。**本文为理论论文，全文无实验误差棒**：所有数字均为作者解析/数值估算（≈/∼ 语气），统一标 📜Q[~]。

---

## 2. 结果与机制（按论文论证结构：拓扑 → 连续模型 → 判据 → 可编程）

### 2.1 能带拓扑与螺旋模（"Band topology and helical modes" 节）

- **偏压开隙 + 谷 Chern 数**：Bernal 型（AB/BA）堆叠加偏压 $U$ 在各谷打开能隙；$U<\gamma_\perp$ 时单谷（非量子化）谷 Chern 数近似量子化 $C_K=-C_{K'}\approx\text{sign}(U)$ 📜Q。AB 与 BA 堆叠互为镜像，谷 Chern 数相反：$C_K^{AB}(\varepsilon)=-C_K^{BA}(\varepsilon)$ 📜Q。
- **畴壁 TPH 模**：$U$（因而 $C_K$）空间反号的界面，或 AB→BA 平滑过渡，各产生**每谷每自旋 2 条** TPH 模 📜Q。体-边对应 $N=|C_2-C_1|\mod2$；本文 $\mod2$ 缺省（$N=2$）因只考虑谷守恒扰动 → "weak" 拓扑保护 📜Q。
- **helical 定义**：helical vs chiral = 有/无时间反演不变性（ref 4）📜Q；石墨烯双层螺旋模 = 传播方向与谷量子数**固定锁定**（ref 15）📜Q。每条链接两谷承载相反方向电流（Fig. 2 白箭头）📜Q；"helicity 通过动量散射抑制耗散" 📜Q。

### 2.2 连续模型：大角度平移 vs 小角度成网（"Continuum theory" 节）

- **模型**：每谷连续自旋简并哈密顿量，写在 $A,B,A',B'$ 基下，两层各带 $U/2$（见 §3.1）。层间耦合 $V(r)=\tfrac13\gamma_\perp\sum_{i=1}^3 e^{ig_i\cdot r}$，$\gamma_\perp\approx0.33$ eV 📜Q。无量纲参数 $\alpha(\theta)$ 区分两区间 📜Q。
- **大角度（$\theta\gtrsim1°$，$\alpha\ll1$）**：可微扰处理。van Hove 奇点 $\varepsilon_{vH}\approx\varepsilon_M(1-2\alpha)$、$v_F^*\approx v_F(1-9\alpha^2)$ 📜Q。加偏压仅把两 Dirac 锥平移 $\pm U/2$（本征态分层局域）→ $|\varepsilon|<|U|/2$ 内 DOS 平坦（类 AA 堆叠双锥），**不形成网络**（Fig. 1，$\theta=4°$ 算例）📜Q。
- **小角度（复杂区）**：$U=0$ 时二次 van Hove 奇点随 $\theta$ 减小下移，逐个 morph 成准平坦 miniband + 费米速度消失，发生在魔角 $\theta_i$，最高 $\theta_1\approx1.05°$（$L_M\approx52a_0$）📜Q；简单图景止于 $\theta\sim0.35°$，其下 $U=0$ 谱复杂、态离域，仅剩一个 AA 局域态钉在 $\varepsilon\sim0.17\varepsilon_M$ 📜Q。**加偏压后谱简化**：AB/BA 区开隙、谷陈数反号，偏压高于阈值且角度足够小 → AB/BA 电子耗尽 → 态被强约束离开耗尽区，出现 sharp 局域共振谱 + 弱平滑背景（= 离域 TPH 网络态）📜Q（Fig. 2）。

### 2.3 网络形成判据 Eq. (1) 与阈值估算

- **经验判据**（作者 "One can approximately quantify this condition"）：简化为突变 AB/BA 界面 + 均匀偏压，用两分量近似（$U<\gamma_\perp$ 有效），界面模 $\sim e^{-\lambda|x|}$ 衰减（$\lambda=\sqrt{U\gamma_\perp}/(2v_F)$，引 ref 12）📜Q。要求界面模在 $R=L_M/(2\sqrt3)$ 内衰减 ≥95% → 判据：
$$z^2\left(\frac{l_\perp}{L_M(\theta)}\right)^2 < \frac{U}{\gamma_\perp} < 1,\qquad |\varepsilon|<\frac{|U|}{2}\quad(1)$$
其中 $z\equiv-4\sqrt3\ln0.05=20.76$、$l_\perp=\hbar v_F/\gamma_\perp\approx7.3a_0$ 📜Q。判据三要素：**小 $\theta$（大 $L_M$）+ 大 $U$ + $|\varepsilon|<|U|/2$** 📜Q。
- **阈值估算**（作者 "This analysis suggests ... for a realistic value of $U\sim90$ meV, the network requires $L_M\gtrsim290a_0$ ($\theta<0.2°$)"，即 Fig. 2 取值）📜Q；Fig. 2(a) 虚线框标出该角度下满足判据的 $(U,\varepsilon)$ 区，与螺旋网络区（sharp DOS 峰 + 弱平滑背景）大致吻合 📜Q。
- **与实验周期对标**：Alden 等已成像堆叠孤子、最大典型周期近 $1\,\mu$m 且可移动 📜Q；"用 $\sim100$ nm Moiré 周期（如该实验），我们**估算**阈值偏压 $\sim45$ meV" 📜Q（作者 "estimate"）。

### 2.4 可编程性：谷混合吸附原子阻断链接

- **机制**：螺旋通道保护是**弱**保护，可被局域谷间散射破坏；空位/小吸附原子是高效谷散射体 📜Q。单个氢吸附原子可**完全阻断**一条网络链接 📜Q。
- **TB 模拟验证**（Fig. 3）：在扭角双层完整晶格上做紧束缚模拟（连续模型谷守恒，不适合此类模拟）📜Q；每 Moiré 单胞同套缺陷，发现**任何带单个原子缺陷的链接在特定能窗内被高效阻断**（反向谷的子带交叉处，链接 1D 螺旋色散开隙）📜Q。
- **作者提出**（propose / could be used to）：可控沉积吸附原子可"at will"改写网络连通性 → 定制无耗散拓扑电路、拓扑纳米电子学 📜Q；前提是把不想要的吸附原子退火去除 📜Q。

---

## 3. 理论模型与方法

### 3.1 连续模型（每谷、自旋简并）

写在 $A,B,A',B'$ 基下的 $4\times4$ 哈密顿量，两层各带对角项 $\pm U/2$，层内 Dirac 项 $\hbar v_F(\sigma\cdot\pi)$，层间耦合 $V(r)=\tfrac13\gamma_\perp\sum_{i=1}^3 e^{ig_i\cdot r}$（AA 亚晶格在原点，AB/BA 亚晶格偏移 $\pm\delta r=(a_1-a_2)/3$，$g_i\cdot a_j=2\pi\delta_{ij}$，$g_3=0$）📜Q。$\gamma_\perp\approx0.33$ eV、$a_0=2.46$ Å、$|K|=4\pi/3a_0$、$\Delta K=2|K|\sin(\theta/2)$ 📜Q。谷间解耦是连续模型的前提 📜Q。

### 3.2 谷 Chern 数与 TPH 计数（推导见 [PHY-BERRY]，本文数值在此）

单谷 Chern 数 $C_K(\varepsilon)=\frac1{2\pi}\int_K d^2k\,F(k)$（Berry 曲率谷内积分）📜Q；$U<\gamma_\perp$ 时 $C_K=-C_{K'}\approx\text{sign}(U)$ 近似量子化，充当拓扑荷（谷解耦时）📜Q。畴壁 TPH 模数 $N=|C_2-C_1|\mod2$，本文 $N=2$/谷/自旋（弱保护）📜Q。

### 3.3 计算方法

- **能谱/DOS**：对角化连续模型，扫 $\theta,U$ 得能带与 DOS（Fig. 1/2）📜Q。
- **光学电导 $\sigma_{xx}(\omega)$**：Kubo 公式，细节见 Supplemental Material 📜Q。
- **吸附原子阻断**：TB 模拟（refs 58,59），因连续模型谷守恒不适用 📜Q。

> 背景锚点：Bernal 双层加偏压开隙的实验上限 250 meV（refs 10,11，Mak 2009 / Zhang 2009）📜Q——是"偏压可调隙"的实验动机，非本文扭角体系的数值。

---

## 4. 关键预言与数据（提取链 + 验证链 + 不确定度标注）

> 全文为理论论文，无实验误差棒：所有数字为作者解析/数值估算，统一 📜Q[~]（原文 ≈/∼ 语气），除特别注明外无 ±。

### 4.1 几何与能标

| 参数 | 值 | 证据 |
|------|-----|------|
| Moiré 周期 $L_M$ | $a_0/[2\sin(\theta/2)]$，$a_0=2.46$ Å | 📜Q[~]（Continuum theory 节） |
| Moiré 能标 $\varepsilon_M$ | $\hbar v_F K/2\approx88\,\text{meV}\cdot\theta(\text{deg})$ | 📜Q[~]（"for small angles"） |
| 层间耦合 $\gamma_\perp$ | $\approx0.33$ eV | 📜Q[~] |
| 层间耦合长度 $l_\perp$ | $\hbar v_F/\gamma_\perp\approx7.3a_0$ | 📜Q[~]（Eq. (1) 附近） |
| 判据常数 $z$ | $-4\sqrt3\ln0.05=20.76$ | 📜Q[~] |
| 魔角 $\theta_1$ | $\approx1.05°$（$L_M\approx52a_0$） | 📜Q[~] |
| 简单图景下限 | $\theta\sim0.35°$ | 📜Q[~] |
| AA 局域态 | $\varepsilon\sim0.17\varepsilon_M$ | 📜Q[~] |
| 大角度算例 $\theta=4°$ | $L_M\approx14.3a_0$ | 📜Q[~]（Fig. 1 caption） |
| 小角度算例 | $L_M=290a_0$（$\theta\approx0.2°$） | 📜Q[~]（Fig. 2 caption） |

### 4.2 网络形成阈值（提取链：Eq. (1) 代入 R=L_M/(2√3)、λR=−ln0.05）

| 估算 | 值 | 证据 |
|------|-----|------|
| 现实偏压 $U\sim90$ meV 所需周期 | $L_M\gtrsim290a_0$（$\theta<0.2°$） | 📜Q[~]（"for a realistic value of U∼90 meV"） |
| 100 nm 周期阈值偏压 | $\sim45$ meV | 📜Q[~]（"we estimate"；对标 Alden 实验周期） |
| 网络能窗 | $|\varepsilon|<|U|/2$ | 📜Q[~]（摘要 + Eq. (1)） |
| Bernal 双层开隙实验上限（背景） | 250 meV | 📜Q[~]（refs 10,11） |

### 4.3 通道计数与拓扑

每谷每自旋 2 条 TPH 模 📜Q；$N=|C_2-C_1|\mod2$、本文 $N=2$（$\mod2$ 缺省）📜Q；$C_K=-C_{K'}\approx\text{sign}(U)$、$C_K^{AB}=-C_K^{BA}$ 📜Q。⚠️ 本文**未**讨论量子化电导（如 $4e^2/h$）——网络的可测签名是 DOS 与 $\sigma_{xx}(\omega)$，不引入电导平台数字。

### 4.4 可编程性预言

单个氢吸附原子完全阻断单条链接 📜Q（TB 模拟，Fig. 3）；空位/小吸附原子高效谷散射体 📜Q；可控沉积改写连通性 → 定制拓扑电路（作者 propose / "could be used to"）📜Q。

### 4.5 证据链与论证结构（三支柱）

| 支柱 | 轴 | 证什么 | 依据 |
|------|-----|--------|------|
| ① 拓扑前提 | 谷轴 | AB/BA 谷陈数反号 → 畴壁 TPH 模存在 | "Band topology" 节 |
| ② 网络判据 | θ-U 轴 | 小 θ + 大 U → 耗尽 → 离域网络（Eq. (1)） | Fig. 2 + Eq. (1) |
| ③ 可编程性 | 缺陷轴 | 谷间散射阻断链接 → 开关 | Fig. 3（TB） |

**交叉验证**：Eq. (1) 阈值线（Fig. 2(a) 虚线）与 DOS 谱 sharp 峰→平滑背景的"螺旋网络区"**大致吻合**（作者 "roughly correlates"）📜Q——解析判据与数值 DOS 自洽互验。

---

## 5. 主要结论

1. 小角度 TBG + 均匀层间偏压 $U$ 下，AB/BA 区耗尽 → 畴壁自发承载每谷每自旋 2 条螺旋模，构成三角 Chalker-Coddington 型离域网络（能窗 $|\varepsilon|<|U|/2$）📜Q。
2. 网络形成判据 Eq. (1)（小 $\theta$ + 大 $U$），给出 $U\sim90$ meV ↔ $L_M\gtrsim290a_0$（$\theta<0.2°$）、100 nm ↔ $\sim45$ meV 的阈值换算 📜Q（估算）。
3. 单氢吸附原子可完全阻断单条链接 → 作者**提出**可编程/可定制的拓扑纳米电子学（propose，TB 模拟支持）📜Q。
4. 大角度（$\theta=4°$）偏压仅平移 Dirac 锥、不形成网络——网络是小角度特有现象 📜Q。
5. 弹性畸变（smooth 于晶格）不破坏 TPH，反因扩大耗尽区而增强网络 📜Q。
6. 作者**谨慎表态**：这是"believe ... ideal platform"（相信是理想平台）与 "estimate" 阈值，未声称已实验实现 📜Q。

## 6. 局限与未解决

| 局限 | 说明 | 证据 |
|------|------|------|
| 弱拓扑保护 | 谷守恒破坏即失效——原子尺度缺陷/强谷间散射敏感 | 📜Q（"weak" protection） |
| 理想周期 Moiré 假设 | 真实样品有弹性畸变/非均匀扭角；作者论证 smooth 畸变不破坏反而增强，但未定量处理无序 | 📜Q |
| 连续模型盲区 | 谷守恒构造，无法描述吸附原子处局域电子结构（故吸附原子用 TB） | 📜Q |
| 设计原则而非定量预言 | 网络导电性/电路性能未定量；σxx(ω) 细节在 SI 未展开 | 📜Q→💭I |
| 未处理多体/魔角 | 魔角 $\theta_1\approx1.05°$ 处平带（关联态）未纳入网络图景 | 💭I（原文未讨论关联） |

## 7. 与其他工作的关系（跨论文对标放这里，不放正文）

| 工作 | 关系 |
|------|------|
| Alden et al. 2013, PNAS 110, 11256 (ref 6) | **直接引用**——堆叠孤子实验成像（最大周期近 1 μm、可移动），本文以此为实验动机与周期对标 📜Q |
| Martin 2008 (ref 12) / Qiao 2011 (ref 14) / Vaezi 2013 (ref 18) / Zhang 2013 (ref 19) | 引用——偏压 kink / 应变 / 倾角晶界 / 谷陈数分类的畴壁 TPH 先驱理论（本文的"网络"是这些孤立畴壁的推广）📜Q |
| Chalker & Coddington 1988 (ref 21) | 引用——网络模型的类比来源 📜Q |
| Tudorovskiy & Katsnelson 2012 (ref 20) | 引用——zero mass lines / 谷电流涡旋 📜Q |
| h-BN 上石墨烯 (refs 27–30) | 引用——机制也出现但晶格失配限制 Moiré 周期，网络不能完全发展 📜Q |

> ⚠️ Phase S 外部对标（**非本文引用**，时间倒挂，须标 💭I）：
> - **Efimkin & MacDonald 2018**（T9）：本文"网络范式"的系统化/严格化版本。
> - **Huang 2018 (E9) / Rickhaus 2018 (E10)**：本文概念被用于解读 mTBG 畴壁螺旋态实验（后验解读）。
> - **Tsim 2020 (T12, TZM)**：推翻"连通网络"——AA 节点确定性散射、不渗流；**部分修正本文网络图景**。
> - **Hou 2024 (T29, NQCP)**：裁决为独立 1D 通道 + 近量子化平台。
> - **De Beule 2020 (T15)**：散射统一（$\phi=0$=TZM / $\phi=\pi/2$=pLL 两极限）。
> 以上引用关系依据 `cards.md` Q2 卡片与 `appendix_B_theory.md` §B.2，非本文原文引用。

## 8. 对后续研究的影响

- 把畴壁物理从"孤立 1D 边缘态"推进到"**连通 2D 网络**"范式——"网络"成为 mTBG 畴壁物理的核心语言 📜Q。
- 提出"可编程拓扑电路"三要素（$\theta$ 设连通几何 + $U$ 开隙/耗尽 + 吸附原子开关）💭I（本文 "propose / could be used to"）。
- 可测签名（DOS 峰 + $\sigma_{xx}(\omega)$）为后续 STM/输运实验提供理论靶标 📜Q。
- 留下"连通性是否成立"的核心张力——被 TZM (T12) 挑战、被 NQCP (T29) 裁决为"独立通道 + 近量子化"（见 §7）💭I。

## 9. 理论模型映射（供 TBPM / Kubo 计算对标）

| 映射 | 说明 |
|------|------|
| $\theta\to L_M\to A$ | 扭角→Moiré 周期 $L_M=a_0/[2\sin(\theta/2)]$→三角畴面积 $A=\frac{\sqrt3}{4}L_M^2$（超晶格单胞一半）📜Q→💭I |
| $U\to\delta$ | 均匀偏压→AB/BA 区局域能隙（耗尽条件），能窗 $|\varepsilon|<|U|/2$ 📜Q |
| Eq. (1) → 相图 | $z^2(l_\perp/L_M)^2<U/\gamma_\perp<1$ 给出 TBPM/Kubo 可扫的 $(\theta,U)$ 网络相图边界 📜Q |
| 通道数 $N=2$/谷/自旋 → 电导 | 若做 Landauer/Fisher-Lee 透射计算，通道数决定弹道电导上限（本文**未**算量子化电导，属计算扩展）💭I（通道计数约定见 [PHY-LB]） |
| DOS 峰 + 网络态空间图案 | 本文可算量；对应 TBPM 的 LDOS/DoS 与 Kubo 的 $\sigma_{xx}(\omega)$ 📜Q |

> 与 TBPM/Kubo 对应：本文连续模型 + TB 是 TBPM/Kubo 的直接上游（同一 $V(r)=\tfrac13\gamma_\perp\sum e^{ig_i\cdot r}$ 层间耦合）；复现"网络 vs 局域共振"需同时算 DOS 与空间 LDOS 图案，纯体 $\sigma_{xx}$ 只给背景（同 E12 §9 注记精神）💭I。

---

## Phase S 目的接口（引用式）

- **Q1（edge state 如何表征）**：本文给出**理论预言**的表征靶标——DOS 谱（弱平滑背景 = 离域网络 + sharp 峰 = 局域共振）、$\sigma_{xx}(\omega)$、空间密度图案（Fig. 2 三角网络白箭头 = 谷电流）📜Q；后续实验（Huang 2018 STM 双线、Rickhaus 2018 输运）按此靶标解读（见 §7）。
- **Q2（理论如何解释）**：螺旋网络奠基——偏压下 AB/BA 谷陈数反号 + 耗尽 → 畴壁每谷每自旋 2 条螺旋模 → 连通网络；判据 Eq. (1) 定量化（小 θ + 大 U + $|\varepsilon|<|U|/2$）📜Q。⚠️ 连通性后被 TZM 部分修正（§7）。
- **Q3（理论↔实验对应）**：$\theta\to L_M$ ↔ 实验周期；$U$ ↔ 阈值偏压（100 nm ↔ ~45 meV）↔ Alden 周期；吸附原子开关 ↔ 可编程器件蓝图；DOS/σxx ↔ 谱学可观测量 📜Q。

> **增量价值**：与 T9（Efimkin 系统理论）分工——本文是**概念奠基 + 经验判据 Eq. (1) + 可编程性预言**，T9 是 $S$ 矩阵严格化；report/appendix_B 用本文 $E_M\approx88$ meV·θ(deg)、$L_M=290a_0$、100 nm↔45 meV 三处数字（均 📜Q，已核对）。比 T9 多的 = 网络形成判据与可编程开关概念；少的 = 无 $S$ 矩阵/网络能带定量。

## 反向核对 pass (2026-09-02)

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

⚠️ 修正/降级：① 旧 review "网络态局域化长度由 U 和 l⊥ 控制" → 精确化为界面模 $\sim e^{-\lambda|x|}$、$\lambda=\sqrt{U\gamma_\perp}/(2v_F)$（引 ref 12；原文 λ 公式的根号在 OCR 中位移至 "$U\sqrt<\gamma_\perp$"，由 Eq. (1) 的 $z^2$ 因子与 $\lambda R=-\ln0.05$ 反推自洽确认）。② arXiv 号 1304.5344 正文未出现（grep 仅命中 ref 29 的 1304.1734）→ 头部表已标"外部来源"。③ 旧 review 未讨论量子化电导，保持不引入 $4e^2/h$（本文未出现该量）。

## 更正日志

| 日期 | 条目 |
|------|------|
| 2026-08-19 | （appendix_B §B.5 #10）T5 数字核对通过：$E_M\approx88$ meV·θ(deg) ✓、100 nm 周期阈值 ≈45 meV ✓、$L_M=290a_0$（θ≈0.2°）✓（均 📜Q）。旧 review 无独立更正日志（旧格式无此节），本条为历史基线。 |
| 2026-09-02 | **按 4 块辨识结构整体重写**：旧格式（5 节叙事）→ 4 块架构（TL;DR + 四层变量表 + 判别表置顶 + 数据/提取链）。保留旧 📜Q 事实（$E_M\approx88$、$L_M=290a_0$、45 meV、$C_K^{AB}=-C_K^{BA}$、螺旋=谷-动量锁定、Chalker-Coddington 类比、θ=4° vs 小角度判别、氢吸附原子开关）。 |
| 2026-09-02 | **新增/修正**：① 补网络形成判据 Eq. (1) 完整式（$z^2(l_\perp/L_M)^2<U/\gamma_\perp<1$，$|\varepsilon|<|U|/2$，$z=20.76$、$l_\perp\approx7.3a_0$）——旧版只有经验判据三要素无公式；② 精确化"界面模衰减"：$\lambda=\sqrt{U\gamma_\perp}/(2v_F)$（引 ref 12）；③ 补大角度定量（$\varepsilon_{vH}\approx\varepsilon_M(1-2\alpha)$、$v_F^*\approx v_F(1-9\alpha^2)$、$\theta_1\approx1.05°$、$L_M\approx52a_0$、AA 局域态 $0.17\varepsilon_M$）；④ 判据表 + [前提与限定] 块（M 边界声明：应变/无序/多体未建模）；⑤ arXiv 号标外部来源；⑥ 全文统一 📜Q[~] 不确定度标注（理论论文无 ±）。 |
| 2026-09-02 | **降级/删除**：① 旧 review 无源/过强论断未发现（旧版内容全部 grep 可验证）；② 未引入 $4e^2/h$（本文未讨论量子化电导，避免跨论文迁移）；③ 跨论文对标（Efimkin/TZM/NQCP/Huang/Rickhaus）移出正文至 §7 并标 💭I 外部对标（时间倒挂，非本文引用）。 |
