<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 16:14:40
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 16:14:41
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/paper_review_jung2011_prb.md
 * @Description  :
-->
<!--
 * @Author       : AI精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/paper_review_jung2011_prb.md
 * @Description  : T3: Jung/Zhang/Qiao/MacDonald 2011 — 多层石墨烯谷霍尔边缘态与扭结态
-->

# Paper Review: Jung, Zhang, Qiao & MacDonald (2011)

| 字段 | 内容 |
|------|------|
| **标题** | Valley-Hall Kink and Edge States in Multilayer Graphene |
| **作者** | Jeil Jung, Fan Zhang, Zhenhua Qiao, Allan H. MacDonald |
| **期刊** | PRB 84, 075418 (2011) |
| **DOI** | 10.1103/PhysRevB.84.075418 |
| **类型** | 理论 — $\pi$ 轨道紧束缚 + 连续模型 |
| **PDF** | ✅ reference/pdfs/ |

---

## 1. 核心贡献

系统研究了**多层石墨烯**（ABC 堆叠 $N$ 层）中的谷霍尔边缘态和扭结态（kink states）。关键发现：
1. **边缘态 (edge states)**：出现在锯齿型（zigzag）边，但**不在扶手椅型（armchair）边**——与晶体取向有关
2. **扭结态 (kink states)**：出现在谷霍尔电导符号改变的任何内部界面——**与晶体取向无关**，zigzag 和 armchair 方向都存在

这一区分对实验设计至关重要：内部畴壁比样品边缘更可靠地束缚拓扑态。

## 2. 方法

- **$\pi$ 轨道紧束缚模型**：仅最近邻跃迁 $t=2.8$ eV，层间耦合 $t_\perp=0.4$ eV
- **连续模型**：$N$ 层 ABC 石墨烯的低能有效理论
- **计算对象**：纳米带能带结构（边缘态 + 内部畴壁态）

哈密顿量（紧束缚）：

$$H = -t\sum_{\langle i,j\rangle} c_i^\dagger c_j + \sum_i U_i c_i^\dagger c_i$$

其中 $U_i$ 是位置依赖的外势（模拟电场和畴壁）。

## 3. 关键结果

### 3.1 谷霍尔电导

ABC 堆叠 $N$ 层石墨烯的谷霍尔电导：

$$\sigma_{xy}^v = \frac{N e^2}{2h}$$

→ 每个谷贡献 $N$ 条 1D 界面通道。

### 3.2 边缘态 vs 扭结态对比

| 特性 | 边缘态 (edge state) | 扭结态 (kink state) |
|------|:---:|:---:|
| 位置 | 样品-真空边界 | 内部畴壁（电场符号反转） |
| zigzag 方向 | ✅ 存在 | ✅ 存在 |
| armchair 方向 | ❌ 不存在 | ✅ 存在 |
| 拓扑保护 | 依赖边界条件 | 由 $\Delta N_\nu$ 保护 |
| 数目/谷 | 不确定（依赖截断） | $N$（由层数决定） |

### 3.3 两层具体结果

- **zigzag 纳米带**：除边缘态外，中心畴壁出现 2 条/谷的扭结态
- **armchair 纳米带**：无边缘态，但中心畴壁仍有 2 条/谷的扭结态
- 扭结态在 armchair 方向有微小 avoided crossing gap（$\sim 0.0014t$），来自原子尺度尖锐势变化——势越平滑，gap 越小

### 3.4 三层 (ABC) 的预言

三层 ABC 石墨烯预期 $N=3$ → 每谷 3 条扭结态分支 → 更大的谷霍尔电导 $\sigma_{xy}^v = 3e^2/2h$。

## 4. 局限

- 假设无谷间散射的理想晶体
- 连续模型无法描述短程 grain-boundary 效应
- 未考虑温度和无序对扭结态输运的影响
- 三层以上的实验验证在当时完全空白

## 5. 与 DW 项目关联

⭐⭐⭐⭐⭐ **DW 项目边缘态 vs 畴壁态区分的关键理论依据**。核心启示：
- **不要依赖样品边缘**：边缘态对晶体取向敏感，armchair 边可能没有态
- **内部畴壁是更好的平台**：畴壁态不依赖晶体取向（zigzag/armchair 都行）
- **三层可能有更丰富的拓扑态**：$N=3$ 时每谷 3 条通道——DW 项目 Phase 5 三层畴壁计算的直接理论动机

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
ABC 堆垛多层石墨烯中，valley Hall conductivity 跨越内部扭结产生拓扑扭结态。关键：zigzag 边缘有 edge state，armchair 无；内部畴壁对两种取向都支持。模式支数 = 层数 N。

### Q3: 理论如何与实验结合?
内部畴壁比边缘更稳健——不受晶体取向影响。多层系统预测更多模式支数（电导阶数可验证）。为后续 mTBG 和多层实验选择内部畴壁提供了理论依据。
