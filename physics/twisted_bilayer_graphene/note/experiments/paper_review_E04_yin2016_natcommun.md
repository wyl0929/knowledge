<!--
 * @Author       : AI 精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-11
 * @Description  : E4: Yin et al. (He group) 2016
-->
# Paper Review: Yin et al. (He group) (2016)

| 字段 | 内容 |
|------|------|
| **编号** | E4 |
| **标题** | Direct imaging of topological edge states at a bilayer graphene domain wall |
| **作者** | Yin et al. (He group) |
| **期刊** | Nat. Commun. 7, 11760 (2016) | **arXiv** | 10.1038/ncomms11760 |
| **类型** | 实验 — STM 直接成像畴壁拓扑边缘态 |
| **Phase S 卡片** | [../../Phase_S/cards.md](../../Phase_S/cards.md) |
| **精读日期** | 2026-08-11 |

---

## 1. 核心贡献

STM/STS 直接成像 BLG 畴壁处的拓扑边缘态。dI/dV 谱显示畴壁上的 gap 内 LDOS 增强——边缘态的直接空间-能量指纹。原子级分辨率确认 1D 态主要局域在畴壁的两条边缘上（畴壁结构宽度 (8±1) nm）。

## 2. 物理机制 / 实验方法

- 低温 STM/STS (4.5K)
- 样品：机械剥离 BLG，解耦地躺在石墨衬底上（无栅极!）+ shear domain wall
- ⚠️ 注意：gap ≈ 80 meV 由**石墨衬底破坏反演对称性**诱导，非栅压打开；全文无 Vg 实验
- dI/dV 空间网格扫描 → LDOS 图 $\propto dI/dV(\mathbf{r}, E)$
- 能谱在畴壁上和 AB/BA 区域分别采集 → 边-体对比
- tight-binding Hamiltonian with nearest-neighbour intra- and interlayer hopping and a finite chemical potential difference

## 3. 关键结果

1. 畴壁处 gap 内 LDOS 增强 📜Q（Fig. 3a-c: 隙内能量处 1D 通道清晰可见；原文未给增强倍数）
2. 畴壁结构宽度 (8±1) nm 📜Q（Fig. 1e caption; 正文: 晶格形变 ~1.5% → ≈9 nm，二者一致）；边缘态 FWHM 随 B 增大而减小 📜Q（SI Fig. 11 caption）；0T FWHM ~13±2 nm 📊F（读图估算，文字未给出）
3. 边缘态位于 gap 内 (~0 meV)，局域于畴壁两边缘——与理论（D = 0.06 eV 层间化学势差）一致 📜Q
4. gap 内出现 gapless 模式 📜Q（正文 "symmetry-protected gapless modes"）；能带 crossing 呈线性（Fig. 3d）📊F——"Dirac 型色散"为读图印象，原文未用此词

## 4. 局限与开放问题

- 单条畴壁的测量——未涉及 mTBG 网络
- 无栅压控制——gap (80 meV) 固定由衬底诱导，不可调
- STM 测量本征是局域的——不代表宏观输运

## 5. 与用户研究的相关性

- TBPM 可计算畴壁 LDOS 直接对标 dI/dV 数据——最强直接对标
- 若 DW 项目需要验证畴壁态的存在性，本文是实验基准

---

## 6. 理论计算细节（Methods: "Calculation of the topological edge states"）

### 6.1 模型几何

- 两种典型 AB–BA 畴壁构型：(i) **zigzag**（SI Fig. 9d）、(ii) **armchair**（SI Fig. 9a，同 Koshino 2013）；任意几何的畴壁可视为二者混合。
- 畴壁区位于 $x \in [-W/2,\ W/2]$；AB/BA 两侧为**开放边界条件**的宽纳米带。

### 6.2 哈密顿量（Eq. (2)，沿用 Vaezi 2013 PRX）

$$H = -t\sum_{l=1}^{2}\sum_{\langle i,j\rangle} a^\dagger_{l,i} b_{l,j} + D\sum_{l=1}^{2}\sum_i (-1)^l\,(a^\dagger_{l,i}a_{l,i} + b^\dagger_{l,i}b_{l,i}) - t_\perp\sum_i a^\dagger_{1,i}b_{2,i} + \mathrm{h.c.}$$

- $a^\dagger_{l,i}$ / $b^\dagger_{l,i}$：第 $l$ 层、格点 $i=(x,y)$、子格 A/B 的产生算符；$l=1$ 顶层、$l=2$ 底层。
- 三层结构按区处理：
  - **AB 区**：上式原样（层间 $a^\dagger_1 b_2$ 耦合）。
  - **BA 区**：层间项替换为 $-t_\perp \sum_i b^\dagger_{1,i} a_{2,i} + \mathrm{h.c.}$。
  - **畴壁区**：晶格失配使层间 hopping 远弱于 AB/BA 区 → **设 $t_\perp = 0$**。
- ⚠️ 注意：Fig. 3d caption 称理论 gap 为 80 meV，与 $D = 0.06$ eV 的换算原文未明示（若每层 ±D 则 $U = 2D = 120$ meV，若 $U = D$ 则 60 meV）；此处 D 用于重现实验观测的 gap，具体对应关系论文未展开。

### 6.3 具体参数

| 参数 | 值 | 说明 |
|------|------|------|
| $t$ | 2.8 eV | 层内最近邻 hopping |
| $t_\perp$ (AB/BA 区) | 0.4 eV | 层间最近邻 hopping |
| $t_\perp$ (畴壁区) | 0 | 晶格失配，层间耦合设零 |
| $D$ | 0.06 eV | 层间化学势差（顶层 +D、底层 −D） |
| $W$ (zigzag) | 8.52 nm | 畴壁宽度；系统总宽 264 nm |
| $W$ (armchair) | 8.40 nm | 畴壁宽度；系统总宽 156 nm |
| 边界条件 | 开放 | 纳米带，沿 x 方向 |

### 6.4 求解流程

1. y 方向有平移对称性 → $k_y$ 是好量子数 → 部分傅里叶变换 → 哈密顿量 $H(k,l,x)$（基为 $[l,x]$）。
2. 直接对角化 $H(k,l,x)$ → 能带 $E(k)$（Fig. 3d，畴壁处出现隙内 gapless 模式，不依赖畴壁类型与宽度）。
3. 固定能量 $E$：若 $E$ 与能带相交于 $k_a = k_1,\dots,k_M$ → 系统有 $M$ 个本征模，解 $H(k_a,l,x)\,C_{l,a}(x) = E\,C_{l,a}(x)$。
4. 模 $k_a$ 的空间分布 $\rho_a(l,x) = |C_{l,a}(x)|^2$；主要局域在畴壁 → **kink 态**；近均匀分布 → **体态**。
5. 顶层态密度 $\rho(E,x) = \sum_{a=1}^{M}\rho_a(l=1,x)$——STS 主要探测顶层，$\rho(E,x)$ **正比于实验 dI/dV(x, E)**（Fig. 3f 即该理论分布，两边缘增强，与实验一致）。

---

## Phase S 补充 (2026-08-11): Q1/Q2/Q3

### Q1: edge state 实验上如何表征?
STM/STS 直接成像畴壁拓扑边缘态。dI/dV 谱在畴壁上显示 gap 内 LDOS 增强。原子级分辨率确认 1D 态主要局域于畴壁的两条边缘（畴壁结构宽度 (8±1) nm，非态宽度）。通过畴壁 vs AB/BA 区域谱对比区分边缘 vs 体。

### Q2 (2026-08-18): 4.5K 下 Vg 与 sample bias 的关系?
- **本文无 Vg**：样品是石墨衬底上解耦的剥离 BLG，没有栅极。gap 由衬底破坏反演对称性诱导（≈80 meV）。
- **sample bias Vb** = STM 针尖-样品直流偏压，是 STS 谱的能量轴：E = e·Vb。图 2 横轴即 Sample bias (mV)。
- 4.5K 的意义：kBT ≈ 0.39 meV ≪ gap (80 meV) 和 5 mV 调制 → 谱分辨率不受热展宽限制。
- dI/dV 测量：关反馈 + 793 Hz、5 mV ac 调制加在样品电压上（锁相）。

### Q3 (2026-08-18): Vg 与打开 AB BLG gap 的 Δ 的关系?
- 本文语境：gap 与 Vg 无关（无栅压）。Δ = E_g ≈ 80 meV 由衬底诱导；从 LL 谱拟合 Eq. (1) 得 |U| = 77±3 meV ≈ E_g（SI Fig 2: "|U| ≈ Eg"）。
- 理论模型 Eq. (2)：层间化学势差 D 项 H ⊃ Σ_l (-1)^l D·n_l（top +D, bottom -D），层间偏压 U = 2D；低能有效理论 gap ≈ |U|。理论计算取 D = 0.06 eV。
- 若要在 gated 器件中换算：Δ 由位移场决定，Δ ≈ γ₁·U/√(γ₁²+U²)（U ≪ γ₁ = 0.4 eV 时 Δ ≈ U），U 与栅压差 (V_t - V_b) 成正比（比例取决于器件几何）。参考 Vaezi 2013 PRX、Zhang 2013 PNAS、Ju 2015 Nature (E2)。

### 更正日志 (2026-08-18 ~ 19)

| 原表述 | 问题 | 修正 |
|---|---|---|
| 态局域宽度 ~3-5 nm | 无源数字（幻觉） | → "局域于畴壁两边缘；畴壁结构宽度 (8±1) nm" |
| 石墨局域底栅 | 与原文不符（石墨是衬底，非栅极） | → "石墨衬底，无栅极" |
| 栅压依赖性 / 栅压范围 ~20V | 跨论文混淆（Vg 数据属 Huang 2018 E9） | → 删除，改为衬底诱导 gap 不可调 |
| LDOS 增强 5-10× | 无源数字（原文未给倍数） | → 删除倍数，标注 📜Q |
| FWHM ~13±2 nm / 3-5 nm | 图读值未标注 | → 13±2 保留并标 📊F 读图估算 |
