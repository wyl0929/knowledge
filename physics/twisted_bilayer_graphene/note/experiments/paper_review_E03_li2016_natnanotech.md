<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-15 17:29:28
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-16 15:39:03
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/note/experiments/paper_review_E03_li2016_natnanotech.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-15
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-15
 * @FilePath     : /project/knowledge/physics/note/experiments/paper_review_E03_li2016_natnanotech.md
 * @Description  : Li et al. (2016) Nature Nanotechnology 精读报告 — 栅控拓扑导电通道的首次电学输运验证
-->

# 论文精读：Li et al., Nat. Nanotech. 11, 1060 (2016)

> **J. Li, K. Wang, K. J. McFaul, Z. Zern, Y. F. Ren, K. Watanabe, T. Taniguchi, Z. H. Qiao, J. Zhu**
> "Gate-controlled topological conducting channels in bilayer graphene"
> Nature Nanotechnology **11**, 1060–1065 (2016)
>
> 作者单位：Penn State（J. Zhu 组） + 中科大（Z. H. Qiao 组） + NIMS（Watanabe/Taniguchi）
>
> **DOI**: [10.1038/nnano.2016.158](https://doi.org/10.1038/nnano.2016.158)
> **arXiv**: [1509.03912](https://arxiv.org/abs/1509.03912)（39 页，含完整 Supplementary Information）
> **Zotero Key**: `6ZDG8PGT`

> **来源声明**：本笔记基于 arXiv:1509.03912v2 全文（pdftotext 提取，39 页含 SI）。数据可靠。

---

## 1. 一句话总结

通过**双分裂栅**（dual-split-gate）在 hBN 封装的双层石墨烯中**静电定义了拓扑导电通道**（kink states），首次实现了栅控的谷极化一维弹道输运。在零场下通道平均自由程 $L_k \sim 70\text{--}200$ nm，垂直磁场 8 T 下 400 nm 长的结达到弹道极限 $G \approx 4e^2/h$。

> ⚠️ **关键区分**：本文的畴壁是 **EFW（Electric Field Wall，电场壁）**——通过栅极施加反向位移场，在同一 AB 堆叠 BLG 中产生 $C_K(+D) \to C_K(-D)$ 的谷 Chern 数跳跃。**不是** LSW（Layer Stacking Wall，层堆叠壁，如 Ju 2015 和 Mania 2019 的结构 AB/BA 边界）。EFW 和 LSW 的相同点是 $|\Delta C_K| = 2$ 和 $4e^2/h$ 弹道极限；根本区别是 Chern 数跳跃的来源（电场翻转 vs 堆叠翻转）。

---

## 2. 背景与动机

### 2.1 已有基础

- **Martin et al., PRL 100, 036804 (2008)**：理论提出 **EFW（Electric Field Wall）** 方案——在同一 AB 堆叠 BLG 两侧施加反向位移场，$D(x)$ 过零处谷 Chern 数跳跃 $|\Delta C_K| = 2$，束缚 kink 态。这是本文的直接理论原型
- **Ju et al., Nature 520, 650 (2015)**：s-SNOM 看到天然 AB/BA 畴壁（LSW），并首次进行了电学输运测量
- 问题：能否实现 Martin 2008 的 EFW 方案——用**纯电学栅控**（不依赖天然畴壁的随机位置）定义和开关拓扑通道？

### 2.2 技术挑战

| 挑战 | 本文的解决方案 |
|---|---|
| 顶栅和底栅的分裂线需精确对准 | 多层石墨烯 split bottom gate + EBL，对准精度 < 10 nm |
| 体电导必须被压制（$E_F$ 在带隙内） | hBN 封装 → 迁移率 10⁵ cm²/Vs → CNP 电阻 > 10 MΩ |
| 栅极不能漏电 | 顶栅/底栅间 hBN 介质，漏电 < pA |

---

## 3. 方法与体系

### 3.1 器件结构

```
        顶栅 (TG)
    ──── hBN ────
    ════ BLG ════        ← 双层石墨烯
    ──── hBN ────
    ── 分裂底栅 (BG-L | BG-R) ──   ← 关键！分裂线定义结
    ──── SiO₂ ────
        Si++ (全局背栅)
```

| 参数 | Device 1 | Device 2 |
|---|---|---|
| 结宽 $w$ | 70 nm | 110 nm |
| 结长 $L$ | 1 μm | 400 nm |
| 迁移率 $\mu$ | 100,000 cm²/Vs | 22,000 cm²/Vs |

### 3.2 工作原理：EFW 的拓扑机制

本文实现的是 **EFW（Electric Field Wall）**：全片为同一 AB 堆叠 BLG，无结构畴壁。拓扑通道仅由栅控电场反转产生。

位移场 $D = (D_{\text{top}} - D_{\text{bottom}})/2$，结左右两侧独立控制：

| 配置 | $D_L \cdot D_R$ | $C_K$ 行为 | 结状态 |
|---|---|---|---|
| **奇（EFW on）** | $< 0$（如 $+D_0$, $-D_0$） | $C_K(+D) - C_K(-D) = 2$ | **kink 态导电** |
| **偶（EFW off）** | $> 0$（如 $+D_0$, $+D_0$） | $C_K$ 无跳跃 | **结绝缘** |

EFW 的谷 Chern 数跳跃来源：

$$|\Delta C_K^{\text{EFW}}| = |C_K(\text{AB}, +D) - C_K(\text{AB}, -D)| = |(+1) - (-1)| = 2$$

对比 LSW（Ju 2015）：

$$|\Delta C_K^{\text{LSW}}| = |C_K(\text{AB}, D) - C_K(\text{BA}, D)| = |(+1) - (-1)| = 2$$

两者 $|\Delta C_K| = 2$ 相同 → 都产生每谷 2 个手征模式 → 弹道极限 $G = 4e^2/h$。

每个谷支持 **4 个手征模式**（2 自旋 × 2 层），$K$ 和 $K'$ 谷的模式反向传播。

### 3.3 测量方案

- 四探针测量结电导 $\sigma_j = 1/R_j$
- 扫 $V_{Si}$（全局背栅，调 $E_F$）+ 固定 $D_L, D_R$ 组合
- 变温（1.6–40 K）+ 变磁场（0–14 T）

---

## 4. 核心结果

### 4.1 奇/偶场配置的鲜明对比——kink 态的"开/关"

| 配置 | $D_L D_R$ | CNP 处 $\sigma_j$ | 解释 |
|---|---|---|---|
| 偶 (++, −−) | > 0 | **< 1 μS** | 无能隙翻转 → 结绝缘 |
| 奇 (+−, −+) | < 0 | **10–15 μS** | 能隙翻转 → kink 态导电 |
| 对比度 | — | **> 10×** | 鲜明！ |

这是 kink 态存在的第一个直接电学证据——用栅压即可"打开"或"关闭"一维拓扑通道。

### 4.2 零场平均自由程：出乎意料的短

- $R_j = 40\text{--}100$ kΩ（零场、奇配置）
- Landauer-Büttiker: $R_j = R_0(1 + L/L_k)$，$R_0 = h/4e^2 = 6.5$ kΩ
- → **$L_k = 70\text{--}200$ nm**，仅与体 2D 平均自由程相当

**为什么这么短？** 理论上 $L_k \gg L_{2D}$ 应该成立（带间散射需要大动量转移，在 hBN 封装清洁样品中应罕见）。本文提出：

1. 平滑静电势剖面在体带隙中引入**非手征束缚态**（non-chiral states）→ 有效缩小带隙
2. 这些非手征态可形成量子点 → 介导 kink 态的谷间散射（多粒子过程、类 Kondo 机制）
3. 理论计算（Anderson 无序 + Green 函数）支持 $L_k$ 随 $E_F$ 增加而减少（更多散射路径）

### 4.3 磁场恢复弹道输运

| 磁场 | Device 1 ($L=1$ μm) | Device 2 ($L=400$ nm) |
|---|---|---|
| $B=0$ | $R_j \approx 40\text{--}100$ kΩ | NEEDS_VERIFICATION |
| $B \approx 7\text{--}8$ T | $R_j \approx 15$ kΩ, $L_k \approx 0.8$ μm | **$R_j \approx 6\text{--}10$ kΩ ≈ $h/4e^2$** |

两个机制解释 $B$ 场效应：
1. **朗道量子化推开非手征态** → 阻断其介导的散射
2. **Lorentz 力空间分离反向传播的 kink 态** → 谷间耦合进一步压制
3. 注意机制 2 在 $E_F=0$ 时不起作用，随 $|E_F|$ 增大而增强

---

## 5. 与其他工作的关系

### 5.1 在三篇单 LSW 实验中的独特地位

| 维度 | Ju 2015 | **Li 2016** | Mania 2019 |
|---|---|---|---|
| **DW 类型** | **LSW**（结构 AB/BA 边界） | **EFW**（电场壁，同堆叠反向 $D$） | **LSW**（折叠结构边界） |
| $\Delta C_K$ 来源 | $C_K(\text{AB}) - C_K(\text{BA}) = 2$ | $C_K(+D) - C_K(-D) = 2$ | $C_K(\text{top}) - C_K(\text{bottom}) = 2$ |
| 探针 | s-SNOM + 电学 | **纯电学（首个 EFW！）** | 电学 |
| 零场弹道 $L_0$ | **420 nm** | ❌ 70–200 nm | **✅ ~20 μm** |
| 栅控开/关 | 否 | **✅（EFW 核心优势）** | 否 |
| 可扩展性 | 低（畴壁随机） | **高（栅编程）** | 低（折叠随机） |

Li 2016 的独特贡献：**首次实验实现 Martin 2008 的 EFW 方案**——证明了栅压可以编程控制拓扑通道的开/关，这是 valleytronics 的关键一步。但其 EFW 的弱点是结宽 $w \sim 100$ nm 引入非手征束缚态 → 零场 $L_k$ 远短于 LSW 路线。

### 5.2 与 Zhang 2024 的理论关联

Li 2016 的 Green 函数计算（Anderson 无序 + Landauer-Büttiker）与 Zhang 2024 的 Bloch 模式计算互补：
- Li 2016：单条静电 DW，关注**非手征态介导的谷间散射**
- Zhang 2024：两条结构 LSW，关注**波函数重叠导致的谷内背散射**

---

## 6. 亮点与局限

### 亮点

1. **首个电学 kink 态实验**：用栅压打开/关闭一维拓扑通道 → 直接、可重复、可编程
2. **静电 DW 路线**：不依赖天然畴壁的随机位置 → 可扩展、可在任意位置定义通道
3. **$B$ 场恢复弹道性**：清晰揭示了非手征束缚态是零场背散射的主要来源
4. **理论与实验紧密结合**：Green 函数计算复现了 $L_k(E_F, w, \Delta)$ 的依赖关系

### 局限

1. **零场弹道性差**：$L_k \sim 100$ nm 远短于理论预期 → DW 通道的实际质量不如后发现的 Mania 2019 好
2. **非结构 DW**：静电 $V=0$ 线不是原子级 sharp 的 AB/BA 边界 → 结宽 $w \sim 70\text{--}110$ nm 引入了非手征束缚态
3. **复杂的 4-gate 结构**：加工难度极高，不利于规模化
4. **电导未量子化**：即使在 $B=8$ T 下也只是"接近" $4e^2/h$，而非精确平台
5. **非手征态的本质未完全理解**：量子点介导散射的具体机制留给了"未来研究"

---

## 7. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **TBPM 对标** | 静电 DW → TB 模型加层偏压（on-site energy offset）模拟 → 计算 $\sigma_{xx}$ + 提取 $L_k$ |
| **非手征态验证** | TBPM 可计算静电 DW 的完整能带 → 检查体带隙中是否出现非手征束缚态 |
| **$B$ 场效应** | Peierls 替换 → 验证朗道量子化推开非手征态 + Lorentz 力空间分离机制 |
| **$L_k$ 系统扫描** | 扫 $w$, $\Delta$, $E_F$ → 构建 $L_k$ 参数空间相图 |
| **与 Zhang 2024 对比** | 静电 DW vs 结构 LSW → 哪种给出更干净的弹道输运？ |

---

## 8. 关键参数速查

| 参数 | 值 | 来源 |
|---|---|---|
| DW 类型 | **EFW（电场壁）**——全片 AB 堆叠，栅控 $D(x)$ 反转，$C_K(+D)-C_K(-D)=2$ | 已确认 |
| 理论原型 | **Martin et al., PRL 100, 036804 (2008)** | 正文 |
| 结宽 $w$ | 70 nm (D1), 110 nm (D2) | 正文 |
| 结长 $L$ | 1 μm (D1), 400 nm (D2) | 正文 |
| 迁移率 | 10⁵ (D1), 2.2×10⁴ (D2) cm²/Vs | 正文 |
| 体带隙 $\Delta$ | ~30 meV（实验值） | 正文 |
| 零场 $L_k$ | 70–200 nm | Landauer-Büttiker 提取 |
| $R_j$ (B=0, 奇配置) | 40–100 kΩ | 正文 Fig. 2 |
| $R_j$ (B=8T, D2) | ~6–10 kΩ ≈ $h/4e^2$ | 正文 Fig. 4 |
| 温度 | 1.6 K（主要数据） | 正文 |
| 理论方法 | Green 函数 + Anderson 无序 | Supplementary §8–9 |

---

*报告生成日期：2026-07-15 | 基于 arXiv:1509.03912v2 全文（39 页）提取*
*SI 可用：arXiv PDF 包含完整 Supplementary Information (Notes 1–9)*
