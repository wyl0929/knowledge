<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-16 17:44:11
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-16 17:44:12
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/stacking-dw/01_literature_scan.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-16
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-16
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/stacking-dw/01_literature_scan.md
 * @Description  : ABA/ABC 堆叠畴壁文献扫描 —— 1 实验 + 4 理论
-->
# ABA/ABC 堆叠畴壁 · 文献扫描

Last updated: 2026-07-16

> 三层石墨烯中 ABA（Bernal）和 ABC（Rhombohedral）堆叠区域之间的边界——即堆叠孤子（stacking soliton）或堆叠畴壁（stacking domain wall）。这是 TBG AB/BA 畴壁的"三层类比"。

---

## 论文 1：Yin et al., PRB 95, 081402(R) (2017) ★ 唯一实验

> **Long-Jing Yin, Wen-Xiao Wang, Yu Zhang, Yang-Yang Ou, Hao-Ting Zhang, Cai-Yun Shen, Lin He**
> "Observation of Chirality Transition of Quasiparticles at Stacking Solitons in Trilayer Graphene"
> arXiv:1609.00080 → PRB Rapid Comm.

### 方法
- **高场 STM/STS**（$B$ 高达 ~8 T），在实空间中分辨 ABA 和 ABC 堆叠畴
- **空间分辨的朗道能级谱学**：在不同位置（ABA 畴内、畴壁处、ABC 畴内）测量 $dI/dV$ 谱

### 核心发现

1. **堆叠孤子的实空间成像**：ABA 和 ABC 畴被 ~10 nm 宽的一维过渡区域（堆叠孤子）分隔
2. **朗道能级的手征性过渡**：
   - ABA 侧：LL 满足 $E_N \propto \sqrt{N}$（massless Dirac，手征性 $l=1$）+ $E_N \propto \sqrt{N(N-1)}$（massive chiral，$l=2$）→ 两套 LL 共存
   - ABC 侧：LL 满足 $E_N \propto B^{3/2} N^{3/2}$（cubic Dirac，手征性 $l=3$）→ 单一手征性
   - **畴壁处**：准粒子的手征性从 $l=1,2$ **平滑过渡**到 $l=3$
3. **畴壁宽度**：~10 nm，比 TBG 的 AB/BA 畴壁（~5 nm）略宽

### 物理重要性
- 首次证明：**晶体堆叠顺序直接决定了石墨烯中准粒子的手征性**
- 堆叠孤子 = 手征性过渡的"桥梁" → 暗示畴壁处可能存在非平凡的拓扑态
- 为后续理论（Jaskólski 2020, 2024）提供了实验基准

### 局限
- 仅测量了 LL 谱（DOS），未直接测量输运
- 无位移场 $D$ 调控
- 高场下测量（~8 T），零场行为未知

---

## 论文 2：Jaskólski & Sarbicki, PRB 102, 035424 (2020)

> **W. Jaskólski, G. Sarbicki**
> "Topologically protected gap states and resonances in gated trilayer graphene"
> arXiv:2005.11473 | 5 pp, 6 figs

### 方法
- **紧束缚模型**：门控三层石墨烯，层间耦合 $\gamma_0, \gamma_1, \gamma_3, \gamma_4$
- 堆叠从 ABC → CBA 通过顶层和底层的**波纹化/剥离**（corrugation/delamination）实现
- 计算畴壁处的能带结构和局域态密度

### 核心发现

1. **每个谷出现 3 条无能隙拓扑保护态**：当堆叠从 ABC 变为 CBA 时
   - 态的数量 = $|\Delta C_V|$，其中 $C_V$ 为谷 Chern 数
   - ABC 三层：$C_V = 3$（per valley），CBA 三层：$C_V = -3$ → $\Delta C_V = 6$
   - 但由于层间耦合的限制，实际观察到 3 条（而非 6 条）——这与 ABC/CBA 的层间对称性有关
2. **畴壁态 = AB/BA 双层畴壁态的叠加**：ABC→CBA 的堆叠变化同时产生了**两组**相邻层间的 AB/BA 型畴壁 → 解释了为何出现 3 条态
3. **门控可调**：在某些栅压下，导带和价带连续区中额外出现**拓扑共振态**（topological resonances）——这些态位于体态能隙中

### 与 Yin 2017 的关联
- Yin 2017 观察到畴壁处 LL 谱的平滑过渡 → Jaskólski 2020 从能带拓扑角度解释了这一现象的微观起源
- 3 条无能隙态 = 畴壁处手征性从 $l=3$（ABC）过渡到 $l=1,2$（ABA）的能带表现

---

## 论文 3：Jaskólski, arXiv:2403.11143 (2024)

> **Włodzimierz Jaskólski**
> "Metal-semiconductor behavior along the line of stacking order change in gated multilayer graphene"
> arXiv:2403.11143 (2024, 预印本)

### 方法
- 紧束缚模型，多层石墨烯（$N \geq 3$ 层），沿 armchair 方向的堆叠变化线
- 考虑了层间裂纹（crack）以释放堆叠畴壁处的剪切应变——这是对 2020 年工作的关键改进

### 核心发现

1. **金属-半导体转变**：堆叠畴壁可以表现为**金属**（无能隙态）或**半导体**（有效能隙），取决于栅压
2. **不同谷的拓扑态重叠**：armchair 方向堆叠变化时，$K$ 和 $K'$ 谷的能量锥在 $k$ 空间重叠 → 来自不同谷的拓扑态**强烈相互作用和分裂** → 产生有效能隙
3. **平带出现**：特定栅压下，费米能级处出现**平带**——栅压的小变化导致电荷在层间振荡
4. **裂纹效应**：层间裂纹（atomic-scale defects）导致的散射在决定畴壁是金属还是半导体中起关键作用

### 与 TBG 畴壁的关键差异
- TBG 畴壁：$K$ 和 $K'$ 谷态在动量空间中**分离**良好 → 谷间散射天然压制
- 三层堆叠畴壁（armchair）：$K$ 和 $K'$ 态**重叠** → 谷间耦合不可忽略 → 可能出现能隙

---

## 论文 4：Li, Qiao, Jung & Niu, PRB 85, 201404(R) (2012)

> **Xiao Li, Zhenhua Qiao, Jeil Jung, Qian Niu**
> "Unbalanced edge modes and topological phase transition in gated trilayer graphene"
> arXiv:1203.4033 | 5 pp, 4 figs

### 方法
- 连续模型 + 紧束缚，**手性堆叠（ABC）**三层石墨烯
- 施加层间电势差（位移场 $D$）打开体能隙
- 计算 zigzag 边界处的边缘态

### 核心发现

1. **非平衡边缘模（unbalanced edge modes）**：门控 ABC 三层石墨烯的**半整数谷霍尔电导**（$\sigma_{xy}^V = 3/2$ per valley）导致**相反的 zigzag 边界上边缘模数量不同**
   - 一边有 $M$ 条边缘态，另一边有 $M+1$ 条 → "非平衡"
2. **天然谷电流极化器**：这种非平衡性使器件成为天然的**谷过滤器**——不同谷的电流被导向不同的边缘
3. **Rashba SOC 效应**：引入 Rashba 自旋轨道耦合后，体系变为 **$Z_2$ 拓扑绝缘体**——出现奇数对螺旋边缘模
4. **拓扑相变**：通过改变 $D$ 场或 Rashba SOC 强度，可以在不同拓扑相之间切换

### 与 ABA/ABC 畴壁的关联
- 本文研究的是 ABC 三层的**外边界**（物理边缘），而非 ABA/ABC **内边界**（堆叠畴壁）
- 但物理机制相同：谷霍尔效应 + 位移场 → 拓扑保护的边界态
- 为后来理解 ABA/ABC 堆叠畴壁处的拓扑态奠定了理论基础

---

## 论文 5：Jaskólski et al., Nanoscale 8, 6079 (2016)

> **W. Jaskólski, M. Pelc, L. Chico, A. Ayuela**
> "Existence of nontrivial topologically protected states at grain boundaries in bilayer graphene: signatures and electrical switching"
> Nanoscale 8, 6079 (2016) | arXiv:1603.04390

### 方法
- 紧束缚模型，**双层**石墨烯中的 AB/BA 堆叠晶界
- 一层含有八边形-双五边形（8-5-5）缺陷线——这种缺陷**混合了石墨烯的子晶格**（sublattice mixing）

### 核心发现

1. **拓扑保护态在缺陷晶界中依然存在**：即使晶界含有五边形缺陷（混合子晶格），无能隙态仍然存活——这比之前理论预言的更普遍
2. **栅压不对称的电导**：反转栅压极性时，晶界处的导电通道数量**改变** → 栅压反转下的不对称电导
3. **电开关效应**：这种不对称性可用于**电控开关**——通过栅压极性控制晶界导电

### 与三层体系的关联
- 这是三层 ABA/ABC 畴壁工作的**直接前驱**
- 证明了一个关键点：**拓扑保护态对原子尺度的缺陷具有稳健性**
- 栅压不对称性 → 为三层堆叠畴壁的栅压调控（Jaskólski 2020, 2024）提供了早期启示

---

## 综合总结

### 这个领域的时间线

```
2012  Li et al.         ← 理论：ABC 三层边缘的非平衡边缘模
2016  Jaskólski et al.  ← 理论：双层 AB/BA 晶界的拓扑态（含缺陷）
2017  Yin et al.        ← ★ 唯一实验：STM 观测 ABA/ABC 堆叠孤子
2020  Jaskólski & Sarbicki ← 理论：三层 ABC→CBA 畴壁的拓扑 gap states
2024  Jaskólski         ← 理论：多层堆叠畴壁的金属-半导体行为
```

### 与 TBG AB/BA 畴壁的对比

| 维度 | TBG AB/BA 畴壁 | ABA/ABC 堆叠畴壁 |
|---|---|---|
| 实验论文数 | >10（STM + 输运） | **1**（仅 STM） |
| 理论论文数 | >20 | ~5 |
| 输运实验 | ✅ 丰富 | ❌ **零** |
| TBPM 计算 | 可做（大超胞） | **更容易**（无需转角，~几十原子宽） |
| 谷间散射 | 天然压制（$K, K'$ 分离） | Armchair 方向 $K, K'$ 重叠 → 可能较强 |
| 可控性 | $\theta$ + $D$ 场 | 仅 $D$ 场（畴壁位置不可控） |

### 对用户的启示

这个领域是**一片几乎未开垦的计算沃土**：

1. **Yin 2017 提供了唯一的实验基准**——TBPM 可以直接复现 ABA 侧、ABC 侧和畴壁处的 LDOS 和 LL 谱
2. **输运计算完全空白**——TBPM 算畴壁处的 $\sigma_{xx}$ 和 $\sigma_{xy}$ 将是该方向的首次输运预测
3. **FT-STM 模拟**——类比对 TBG 的做法，验证 ABA/ABC 畴壁是否谷保护（目前无人做过）
4. **$D$ 场调控**——Jaskólski 2024 预言的金属-半导体转变可以在 TBPM 中独立验证
