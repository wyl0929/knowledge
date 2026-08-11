<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 17:17:04
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 17:17:07
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/helical_network/paper_review_fujimoto2021_prb.md
 * @Description  :
-->
<!--
 * @Author       : AI精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/helical_network/paper_review_fujimoto2021_prb.md
 * @Description  : T13: Fujimoto & Koshino 2021 — 摩尔边缘态与滑动陈数量子泵浦
-->

# 论文精读：Fujimoto & Koshino, PRB (2021)

> **Manato Fujimoto, Mikito Koshino**
> "Moiré edge states in twisted bilayer graphene and their topological relation to quantum pumping"
> PRB 103, 155410 (2021) | arXiv:2012.02537
>
> 作者单位：Osaka University

---

## 1. 一句话总结

发现 TBG 的**摩尔边缘态**（moiré edge states），并建立其与**滑动陈数**（sliding Chern number）的体-边对应：层间滑动一个原子周期 → 边缘态从一个能带泵浦到另一个 → 泵浦数 = 滑动陈数。

---

## 2. 背景与动机

### 2.1 已有知识背景

- TBG 体能带陈数为零 → 无传统 QH/QVH 边缘态
- 但 TBG 有畴壁拓扑态和 zigzag 边缘态（继承自单层石墨烯）
- 滑动陈数 $C_{\text{slid}}$ 是此前提出的 TBG 新拓扑不变量（描述层间滑动时的电荷泵浦）

### 2.2 未解问题

TBG 的**摩尔边缘态**（远离零能、依赖于摩尔周期边界截断的边缘态）是否有拓扑起源？如果有，对应什么体不变量？

---

## 3. 方法与模型

### 3.1 体系

- TBG 纳米带（$\theta = 2.65^\circ$），宽度方向 5 个摩尔单胞，长度方向周期性
- 边界近 armchair 方向（抑制 zigzag 边缘态干扰）
- 紧束缚模型（$\gamma_0 = -2.6$ eV, $\gamma_1 = 0.34$ eV）

### 3.2 滑动协议

层 2 相对层 1 沿纳米带长度方向（$y$）滑动，位移矢量 $(\nu_1, \nu_2) = \lambda(1/2, -1)$，$\lambda \in [0,1]$。

摩尔图案的移动 $X$ 与滑动矢量 $x^{(2)}$ 的关系：
$$\mathbf{X} = \frac{\pm 1}{2\sin(\theta/2)} R(-\pi/2 \mp \theta/2) \mathbf{x}^{(l)}$$

当 $\theta \ll 1$ 时，摩尔位移 $X$ **几乎垂直于**滑动方向，且被放大 $1/\theta$ 倍。

### 3.3 滑动陈数

$$C_{\text{slid}} = \frac{1}{2\pi} \int dk_y \int_0^1 d\lambda \, \Omega(k_y, \lambda)$$

其中 $\Omega$ 是 $(k_y, \lambda)$ 空间的 Berry 曲率。

---

## 4. 核心结果

### 4.1 摩尔边缘态的发现

TBG 有两种边缘态：
1. **Zigzag 边缘态**：$E=0$，继承自单层石墨烯，对摩尔周期不敏感
2. **摩尔边缘态**（本文重点）：远离 $E=0$，出现在平带与激发带之间的能隙中，**强烈依赖于摩尔图案的边缘截断**

### 4.2 滑动泵浦：体-边对应

**核心发现**：层间滑动 $\lambda: 0 \to 1$ 过程中，摩尔边缘态**从一个能带转移到另一个能带**，跨越体能隙：

$$\text{泵浦边缘态数} = C_{\text{slid}}(\text{能隙})$$

具体过程：
- $\lambda = 0$：边缘态附着在平带上
- $\lambda = 0.5$：边缘态进入能隙中间
- $\lambda = 1$：边缘态转移到激发带上

过了一个完整周期，AA 点移动一排 → 净泵浦电荷 = $C_{\text{slid}} \times$ 摩尔单胞数。

### 4.3 与畴壁拓扑态的关系

- 摩尔边缘态与 AB/BA 畴壁上的 THS **并非同一概念**
- THS 是畴壁内的 1D 束缚态；摩尔边缘态是整个 TBG 纳米带的边界态
- 但两者的拓扑起源可能共享同一数学结构（滑动陈数）

---

## 5. 与其他工作的关系

| 相关工作 | 关系 |
|----------|------|
| Tsim & Koshino 2020 (TZM) | 同一组，互补：TZM 是畴壁内的 1D 态，本文是 TBG 边界上的边缘态 |
| Efimkin & MacDonald 2018 | 网络模型处理畴壁 THS，未涉及摩尔边缘态 |
| Thouless 泵浦 (1983) | 方法论祖先：绝热泵浦 + 拓扑不变量 |
| Zhang/MacDonald/Mele 2013 | 谷陈数边界态 — 本文的滑动陈数是另一种体-边对应 |

---

## 6. 亮点与局限

### 亮点
- **新边缘态类型**：摩尔边缘态 ≠ zigzag 态 ≠ THS，丰富了 TBG 边缘物理
- **新体-边对应**：滑动陈数 ↔ 摩尔边缘态泵浦 — 摩尔体系的独特拓扑原理
- **方法优雅**：将层间滑动映射为绝热泵浦，Berry 曲率在 $(k_y, \lambda)$ 空间

### 局限
- 仅计算了无相互作用的紧束缚模型
- 未讨论实验如何实现可控的层间滑动（实用挑战大）
- 摩尔边缘态与 THS 畴壁态的明确区分需要更多工作
- 仅单一转角 $\theta = 2.65^\circ$，转角依赖性未系统研究

---

## 7. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **方法** | 纳米带边界态计算可参考本文的 armchair 截断策略 |
| **扩展方向** | DW 项目中检验：TBG 纳米带的滑动陈数能否用 tbplas 复现 |
| **可验证性** | 摩尔边缘态的能谱演化 vs $\lambda$ 可用 tbplas 独立验证 |

---

## 8. 关键参数速查

| 参数 | 值 |
|------|-----|
| $\theta$ | $2.65^\circ$ |
| $\gamma_0$ | $-2.6$ eV |
| 纳米带宽度 | 5 摩尔单胞 |
| 边界方向 | 近 armchair |
| 滑动矢量 | $\lambda(1/2, -1)$, $\lambda \in [0,1]$ |
| 摩尔位移放大因子 | $1/[2\sin(\theta/2)] \sim 1/\theta$ |

---

*报告生成日期：2026-08-06 | 基于 PDF pdftotext 精读*

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
TBG 纳米带中 moire 边缘态通过参数空间体边对应与滑动陈数联系。层间绝热滑动时边缘态被泵浦穿过能隙——泵浦边缘态数 = 滑动陈数。

### Q3: 理论如何与实验结合?
预言 moire 边界附近边缘局域态对截断方式高敏感——为 STM/纳米带测量提供光谱特征。将 TBG 边缘态与 Thouless 泵浦联系。
