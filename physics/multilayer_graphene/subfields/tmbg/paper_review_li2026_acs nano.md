<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-03 11:56:45
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-03 11:56:46
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/tmbg/paper_review_li2026_acs nano.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-03
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/tmbg/paper_review_li2026_acs nano.md
 * @Description  : Li et al. (2026) ACS Nano 阅读笔记 — mtMBG 中重入平带与非平庸拓扑
-->
# 论文阅读笔记：Li et al., ACS Nano 20, 5940 (2026)

> **Si-yu Li, Junnan Jiang, Zhengwen Wang, Yingbo Wang, Yingzhuo Han, Min Li, Jing Hu, Youle Zhang, Kenji Watanabe, Takashi Taniguchi, Hong-Jun Gao, Yuhang Jiang, Jinhai Mao**
> "Reentrant Flat Bands with Nontrivial Topology and Electronic Correlations in Artificial Rhombohedral Trilayer Graphene"
> ACS Nano 20, 5940–5950 (2026) | DOI: [10.1021/acsnano.5c19130](https://doi.org/10.1021/acsnano.5c19130)
>
> 机构：中国科学院大学 (UCAS) + 物理所 (IOP) + NIMS (Watanabe/Taniguchi) | STM/STS 实验
> 投稿：2025-11-04, 接收：2026-02-04, 发表：2026-02-10

---

## 1. 一句话总结

在**小转角单层-双层石墨烯（mtMBG, $\theta \sim 0.07^\circ$）**中，结构弛豫自发形成大面积 ABC 堆叠畴，其电子性质**重入**（reentrant）菱方三层石墨烯的平带特征——平带带宽仅 ~12 meV（FWHM）。平带部分填充时出现**四重劈裂**的关联态级联相变，畴壁处观测到拓扑边缘态和电子极化。

---

## 2. 核心概念：mtMBG 中的"人工菱方三层"

### 2.1 结构

mtMBG = 单层 graphene + AB 堆叠双层 graphene，极小转角 $\theta \ll 1^\circ$：

```
    单层 graphene (顶层, 微小转角 θ)
    ─────────────────────
    AB 堆叠双层 graphene (底层)
```

- $\theta \sim 1^\circ$（魔角附近）：ABB、ABA、ABC 三种畴共存
- $\theta \sim 0.18^\circ$：ABA 和 ABC 畴扩大
- **$\theta \sim 0.07^\circ$（本文关键）**：ABC 畴 >100 nm → 电子性质**完全复现**菱方三层石墨烯

### 2.2 "重入"的含义

- **魔角 TBG（$\theta \sim 1.1^\circ$）**：平带来自摩尔超晶格
- mtMBG 的平带**不来自摩尔超晶格**（转角太小，摩尔周期极大）→ 而是来自**结构弛豫后的大面积 ABC 畴**——即 ABC 三层石墨烯的本征平带
- "重入" = 绕过了魔角条件，通过堆叠工程重新获得了平带

---

## 3. 实验方法

| 参数 | 细节 |
|---|---|
| 技术 | 低温 STM/STS |
| 温度 | **4.8 K**（液氦） |
| 真空 | < 1×10⁻¹⁰ mbar |
| 衬底 | hBN |
| 转角范围 | $\theta \sim 0.07^\circ$–$1.12^\circ$ |
| 背栅 | 有（SiO₂/Si），但 **Figure 3b 未施加栅压**（见下文 §7） |
| 针尖 | 校准于 Au(111) 和 Cu(111)（材料未显式说明，推测标准 PtIr 或 W） |

---

## 4. 核心实验结果

### 4.1 转角演化的三个阶段

| 转角 | 畴结构 | 平带特征 |
|---|---|---|
| $\theta \sim 1.12^\circ$ | ABB, ABA, ABC 小畴共存 | **无**明显平带（摩尔能带为主） |
| $\theta \sim 0.18^\circ$ | ABA+ABC 畴扩大 (~80 nm) | **初步**平带，FWHM ~21 meV，但不主导 |
| **$\theta \sim 0.07^\circ$** | **ABC 畴 >100 nm** | **平带主导**！FWHM **~12 meV**，接近本征 ABC 三层 |

### 4.2 $\theta = 0.07^\circ$ 的关键特征 (Figure 3)

- **Figure 3a**：STM 形貌图——大面积 ABA（亮）和 ABC（暗）三角畴
- **Figure 3b**：ABC 区域 $dI/dV$ 谱 → **极窄平带峰**（FWHM ~12 meV）主导低能 DOS；ABA 区域信号弱得多
- **Figure 3c**：平带能量的 LDOS map → **平带完全局限在 ABC 畴内**
- **Figure 3d**：20 meV LDOS map → 信号分布于 ABA 和 ABC 畴
- **Figure 3e**：$E_F$ 处 LDOS map → 畴壁（DW）处 LDOS 增强 → **拓扑边缘态**
- **Figure 3h**：跨畴壁的线扫描谱 → 能带弯曲（band bending）→ **电子极化**

### 4.3 平带的关联劈裂 (Figure 4, 施加栅压时)

- CFB（导带平带）接近 $E_F$ 时**逐步劈裂为 4 个子带**
- 劈裂**不能**用单粒子效应（如位移场能隙）解释 → **关联驱动的 4 重自旋-谷简并度破缺**
- 类似现象之前在近魔角 TBG 和本征菱方多层中报道过
- 子带能量随栅压演化 → 量子相变级联

### 4.4 畴壁处拓扑边缘态 (Figure 3e–h)

- $E_F$ 处畴壁 LDOS 增强 → 1D 拓扑边缘态（类似于 AB/BA 畴壁的 QVH 边缘态）
- 畴壁处能带弯曲 → 源自 ABA 和 ABC 畴之间的**电子极化**（electromechanical coupling）

---

## 5. 物理意义

### 5.1 "人工" vs "本征"菱方三层

| 维度 | 本征 ABC 三层 | mtMBG ABC 畴 |
|---|---|---|
| 稳定性 | **亚稳态**，易转变为 ABA | **稳定**——被畴壁和结构弛豫锁定 |
| 产率 | 极低（剥离后需筛选） | **高**——通过转角工程可控 |
| 畴尺寸 | 数十 μm（天然畴） | ~100–200 nm（可进一步优化） |
| 平带质量 | 最佳（本征） | **接近本征**（FWHM ~12 meV vs 本征 ~10 meV） |
| 调控性 | 有限 | **可调**——$\theta$ + 栅压双调控 |

### 5.2 与魔角 TBG 的对比

- **魔角 TBG**：平带来自摩尔超晶格 → 需要精确 $\theta \sim 1.1^\circ$
- **mtMBG**：平带来自堆叠弛豫的 ABC 畴 → $\theta$ 在很宽范围（< 0.1°）均可实现

---

## 6. 关键参数速查

| 参数 | 值 |
|---|---|
| 最优转角 | $\sim 0.07^\circ$ |
| ABC 平带 FWHM | ~12 meV |
| 温度 | 4.8 K |
| 衬底 | hBN |
| 畴尺寸 | >100 nm (ABC), >200 nm (ABA) |
| 平带劈裂级数 | 4（关联驱动） |

---

## 7. ★ Figure 3b 是否有外加电场？

### 结论：**Figure 3b 没有施加外加电场（栅压）。**

### 证据链

1. **Figure 3 标题没有栅压参数**：
   - Figure 3b 标题：`dI/dV spectra (I = 300 pA, Vbias = −100 mV, Vmodulation = 3 mV, plot offset = 1)`
   - **未提及背栅电压** $V_g$。
   - 对比 Figure 4a：`as a function of back-gate voltage ranging from −30 to 30 V`——明确写了栅压扫描。
   - 对比 Figure 2e：同样有 `back-gate voltage`。

2. **正文中的措辞**：
   - "Moreover, a tip-induced displacement field **can** break the layer symmetry..."（line 323）
   - 使用 "**can**"（可以）而非 "**is applied**"（被施加）→ 描述的是**物理可能性**，不是实验事实。这是在解释 ABA 区域谱的特征起源，而非说明测量条件。
   - 对比 Figure 4 讨论中："under charge doping **and** the displacement field"——明确说施加了位移场。

3. **实验方法部分**：
   - STM 针尖仅说"校准于 Au(111) 和 Cu(111)"，**未提及**使用 Au 涂层针尖（与 Zheng 2022 PRL 的"Au-coated W tip"不同）。
   - 未像 Zheng 2022 那样做 W tip vs Au tip 的对比实验。

4. **论文逻辑**：
   - Figure 3 的目标是展示 mtMBG 在**零栅压/零位移场**下的本征平带
   - Figure 4 才是展示栅压调控下的关联态级联
   - 如果在 Figure 3 就加了电场，Figure 4 的"栅压驱动关联态"论证逻辑就不通了

### 针尖诱导电场的微弱残余

任何 STM 实验中针尖和样品间都有功函数差 → 微小的局域电场总是存在的。但本文**并非故意施加**位移场（不像 Zheng 2022 那样用 Au 针尖 vs W 针尖对比来主动产生 $D$ 场），且 Figure 3b 的测量条件下这一效应是**最小化**的。

---

## 8. 与用户研究领域的关联

| 维度 | 关联 |
|---|---|
| **TMBG 子领域** | 本文的 mtMBG 就是 TMBG 在极小 $\theta$ 极限——与用户研究的 TMBG 直接相关 |
| **ABA/ABC 畴壁** | Figure 3e–h 观测到畴壁拓扑边缘态和电子极化 → 与畴壁物理系列（Yin 2017, Jaskólski 2020 等）直接对接 |
| **TBPM 计算** | (1) 构造 $\theta \sim 0.07^\circ$ 的 TMBG TB 模型 → 验证 ABC 畴平带的形成；(2) 畴壁处 LDOS 增强；(3) 栅压下平带四重劈裂（需要 HF 修正） |
| **Li 2020 堆叠控制** | Li 2020 展示了可通过 $D$ 场全局切换 ABA/ABC 堆叠——与本文的畴壁网络形成互补调控手段 |

---

## 9. 与同类论文的对比

| 维度 | Li 2026 (本文) | Li 2020 (Nano Lett.) | Zheng 2022 (PRL) |
|---|---|---|---|
| 体系 | mtMBG ($\theta<0.1^\circ$) | Few-layer graphene | mTBG (0.075°–1.2°) |
| 核心发现 | ABC 畴平带 + 关联劈裂 | 堆叠序电控全局相变 | PLL + 电子 Kagome |
| 平带来源 | ABC 本征平带（结构弛豫） | N/A | 畴壁 PLL（人工规范场） |
| 外加 $D$ 场 | Fig 3: **无**, Fig 4: 有 | 双栅全局调控 | 针尖诱导局域 $D$ |
| 温度 | 4.8 K | 300 K | 78 K |

---

*笔记创建日期：2026-08-03 | PDF 全文已读 ✓*
