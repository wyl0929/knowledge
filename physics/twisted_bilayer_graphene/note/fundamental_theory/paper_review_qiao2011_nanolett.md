<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 16:14:41
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 16:14:44
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/paper_review_qiao2011_nanolett.md
 * @Description  :
-->
<!--
 * @Author       : AI精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/paper_review_qiao2011_nanolett.md
 * @Description  : T4: Qiao/Jung/Niu/MacDonald 2011 — 扭结态弹道输运 + 谷赝自旋记忆
-->

# Paper Review: Qiao, Jung, Niu & MacDonald (2011)

| 字段 | 内容 |
|------|------|
| **标题** | Electronic Highways in Bilayer Graphene |
| **作者** | Zhenhua Qiao, Jeil Jung, Qian Niu, Allan H. MacDonald |
| **期刊** | Nano Letters 11, 3453–3459 (2011) |
| **DOI** | 10.1021/nl201941f |
| **类型** | 理论 — NEGF 量子输运模拟 |
| **PDF** | ✅ reference/pdfs/ |

---

## 1. 核心贡献

**首次用 NEGF 量子输运模拟**证明：双层石墨烯中的扭结态（kink states）具有**极长平均自由程**（干净样品中可达数百微米）和**显著的谷赝自旋记忆**——即使在路径弯曲和交叉处，电子仍保持谷标签。

这篇论文将扭结态从"拓扑好奇心"推进到"可能做纳米电子器件的导电高速公路"。

## 2. 方法

- **$\pi$ 轨道紧束缚模型**：$H = -t\sum_{\langle i,j\rangle} c_i^\dagger c_j + \sum_i U_i c_i^\dagger c_i$
- **非平衡格林函数 (NEGF)**：计算四端器件的 Landauer 电导
- **器件几何**（图 1a）：两层石墨烯分为四个象限，各象限独立控制层间偏置 $V$ 的符号 → 零线（扭结态路径）可被栅压"编程"
- **参数**：$t=2.8$ eV, $U = \pm 0.1t$（约 $\pm 0.28$ eV）

## 3. 关键结果

### 3.1 能带结构

- **zigzag 零线纳米带**（图 1c）：除中心扭结态外，zigzag 边还有额外的边缘态通道（简并，来自反演对称）
- **armchair 零线纳米带**（图 1d）：仅中心扭结态，无边缘态。微小 avoided crossing gap $\Delta \sim 0.0014t$ 来自原子尺度尖锐势——势越平滑，gap 越小

### 3.2 弹道输运与平均自由程

- 干净样品：扭结态弹道输运
- 弱无序（无序强度 $\ll$ 体能隙）：平均自由程可达**数百微米**
- 原因：扭结态在实空间局域在畴壁上，两个反向传播态在实空间和动量空间都分离 → 背散射被强烈压制

### 3.3 谷赝自旋记忆

- **直零线**：完美谷记忆——$K$ 谷电子只沿一个方向走
- **弯曲零线**（包括 armchair 方向段）：谷标签**基本保持**——与连续模型预测高度一致
- **零线交叉**：电子在交叉处仍主要保持原始路径，谷间散射弱
- 这意味着：**输运路径由零线拓扑决定，而非晶体取向**

### 3.4 器件应用前景

- **谷阀 (valley valve)**：两个谷过滤器串联 → 通过调节中间栅压可开关电流
- **谷过滤器**：将 $K$ 谷电子引导到一个接触、$K'$ 谷电子引导到另一个接触
- **栅压可编程电路**：改变栅压图案 → 重配置扭结态路径 → 实现可重构电子学

## 4. 关键数值

| 参数 | 值 |
|------|-----|
| 层内跃迁 $t$ | 2.8 eV |
| 层间偏置 $U$ | $\pm 0.1t$ (≈ 0.28 eV) |
| Armchair avoided gap | $\sim 0.0014t$ (≈ 4 meV) |
| 干净样品平均自由程 | > 数百 μm |
| 谷霍尔电导（2层）| $\sigma_{xy}^v = e^2/h$（每谷） |

## 5. 局限

- 未考虑有限温度效应（声子散射）
- 尖锐势变化产生的人工 avoided gap 在真实器件中可能被无序掩盖
- 四端器件几何较简单——更复杂的网络拓扑（三角网络等）未探索
- 仅两层——三层的扭结态输运未计算

## 6. 与 DW 项目关联

⭐⭐⭐⭐⭐ **DW 项目输运模拟的直接方法论文献**。核心启示：
- **NEGF + 紧束缚** 是验证扭结态输运性质的标准方法——DW 项目的 tb.py 可参照此方法
- **谷赝自旋记忆**是构建可编程拓扑电路的关键——即使路径弯曲，信息（谷标签）不丢失
- **零线拓扑决定输运路径**——这对设计 domain-wall computing 架构至关重要
- **弱无序下平均自由程极大**——说明扭结态网络在实验上可能是可行的

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
扭结态是沿畴壁局域的"电子高速公路"——谷极化、可弹道长距离传播，弯曲/交叉时保持谷赝自旋。拓扑保护来自畴壁两侧相反的 valley Hall conductivity。

### Q3: 理论如何与实验结合?
预言长平均自由程、弹道输运和谷阀/谷过滤行为。提出栅压可重构扭结网络——可编程电子通道概念。深刻影响后续谷电子学和畴壁输运实验设计。
