<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 22:04:41
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 22:04:42
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E14_zheng2022_prl.md
 * @Description  :
-->
<!--
 * @Author       : AI 精读 (research_onboarding_skill)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/experiments/paper_review_E14_zheng2022_prl.md
 * @Description  : E14: Zheng et al. 2022 — 可调样品级电子 Kagome 晶格
-->

# Paper Review: Zheng et al. (2022) — 可调电子 Kagome 晶格

| 字段 | 内容 |
|------|------|
| **编号** | E14 |
| **标题** | Tunable Sample-Wide Electronic Kagome Lattice in Low-Angle Twisted Bilayer Graphene |
| **作者** | Qi Zheng, Chen-Yue Hao, Xiao-Feng Zhou, Ya-Xin Zhao, Jia-Qi He, Lin He |
| **期刊** | Physical Review Letters 129, 076803 (2022) |
| **DOI** | 10.1103/PhysRevLett.129.076803 |
| **类型** | 实验 — STM/STS |
| **课题组** | He group (Beijing Normal Univ.) |
| **PDF** | ✅ reference/pdfs/Zheng 等 - 2022 - ...pdf |
| **DW.bib** | ✅ `zheng_tunable_2022` |
| **精读日期** | 2026-08-06 |

> **注意**：当前精读主要基于 Supplementary Information 文本；主文正文的定量细节（如完整 PLL 序列索引、赝磁场 B_ps 绝对数值）待补充主文提取后更新。

---

## 1. 核心贡献

在低角度 TBG 的 AB/BA 畴壁（DW）通道中发现：

1. **局域化平带态**（PLL = pseudo-Landau-level-like 态），主要出现在**空穴侧**（~0.2–0.4 eV）
2. 在 PLL 能量做定能 dI/dV mapping 时，DW 网络显现**Kagome-like 电子图样**
3. 可在多种扭角样品中复现（~0.46° 到 ~1.15°）
4. DW 通道中同时存在两种态：**DW 中心 PLL（局域）+ DW 两侧拓扑边态（helical）**
5. 可通过基底工程（h-BN vs WSe₂）和探针功函数（W vs Au 修饰）调控

## 2. 物理机制

### 2.1 电子 Kagome 晶格形成

- 结构重构 → AB/BA 三角域 + AA 节点 + DW 三角网络
- 在 PLL 能量处 dI/dV 映射 → 信号集中在 DW 中心 → 几何上呈 Kagome-like

### 2.2 PLL 态 vs 拓扑边态

| 特征 | PLL/DW 中心态 | 拓扑边态 |
|------|-------------|---------|
| 空间分布 | DW **中心**最强 | DW **两边**亮 |
| 典型能量 | 230/260/290 meV（空穴侧）| ~30 meV（隙内）|
| 物理来源 | 层间偏压 + 堆垛/重构相关有效规范场 → PLL | AB/BA 反号谷 Chern 数界面 helical 态 |

### 2.3 规范场与赝磁场

- 机制：层间偏压 + 重构相关有效规范场 → PLL 形成（引用 Ramires & Lado, PRL 2018）
- 局域应变与原子堆垛差异 → 不同 DW 通道上的 PLL 能量差异（如 230 vs 260 meV）
- 结构重构**不抑制空穴侧 PLL 形成**，但引入**强电子-空穴不对称**（电子侧几乎无 PLL）

## 3. 实验方法

### 3.1 样品制备

- **CVD 生长石墨烯**：Cu 箔（99.8%, 25 μm），LPCVD 法
  - Ar 50 sccm + H₂ 50 sccm 全程
  - 1030°C 退火 12 h → CH₄ 5 sccm 生长 20 min
- **低角 TBG**：湿法 PMMA 转移 + 切割叠转
  - 转移到 WSe₂/Si/SiO₂（285 nm 氧化层）或 h-BN 上
  - 去 PMMA 后低压 Ar/H₂（各 50 sccm）~300°C 退火 1 h
- **h-BN 器件**：tear-and-stack 法 + HOPG/Au 电极

### 3.2 STM/STS 参数

| 参数 | 值 |
|------|-----|
| 温度 | 77 K |
| 真空 | ~10⁻¹⁰ Torr |
| 设备 | UNISOKU USM-1400 |
| dI/dV 锁相调制 | 5 mV @ 793 Hz |
| 成像设定 | V_bias ~ 400–500 mV, I ~ 100–200 pA |

### 3.3 探针效应

| 探针类型 | 效果 |
|----------|------|
| 裸 W tip | Δw 小 → 等效外电场弱 → AB/BA 近似无隙 → DW 不显著 PLL |
| Au 修饰 W tip | Δw 大 → 明显层间电场 → AB/BA 开隙 → DW 中出现 PLL（空穴侧）|

## 4. 关键数据

### 4.1 h-BN 上极小角样品

| 参数 | 值 |
|------|-----|
| θ | ~0.075°, ~0.176° |
| 裸 W tip → AB 区 | gapless 谱 |
| DW 区 | 无 PLL |
| AA 态 | 近 0 meV 显著峰（局域 AA），±100/±180 meV 局域 AB/BA |

### 4.2 Au 修饰 tip（θ ~ 0.09°, 0.12°）

| 参数 | 值 |
|------|-----|
| AB/BA 隙 | ~30 meV（gap-like）|
| PLL 能量 | 258 meV（定能图完全局域 DW）|

### 4.3 WSe₂ 上各角度样品汇总

| θ | AB/BA 特征 | DW PLL 特征 |
|---|----------|------------|
| ~0.2° | gap-like | 230 meV（某些 DW 260 meV）；30 meV 处双边拓扑态 |
| ~0.46° | — | 290 meV DW 局域；0.2–0.4 eV 区间有 DW 相关峰 |
| ~0.88° | 234 meV gap-like（双 band-edge）| 0.3–0.4 eV 弱峰；25 meV 局域 AA, 118 meV 局域 AB/BA |
| ~1.02° | — | 0.3–0.4 eV 弱峰；380 meV 定能图 Kagome-like |
| ~1.15° | — | DW 态能量随 θ 增大单调上升 |

### 4.4 跨角度趋势

- DW 局域态能量总体随扭角增大单调上升
- DW 态主要落在 **0.2–0.4 eV 空穴侧**
- 电子侧（−120, −200, −400 meV；θ ~ 1.07°, 0.98°, 0.8°）：**未见 Kagome/PLL 特征** → 强电子-空穴不对称

## 5. 主要结论

1. **电子 Kagome 晶格是样品级（sample-wide）特征**，非局部偶发（多角度复现）
2. DW 通道中 PLL 局域态 + 拓扑 helical 边态**共存但空间分离**（中心 vs 两边）
3. 结构重构不抑制空穴侧 PLL，但显著抑制电子侧 PLL → 强电子-空穴不对称
4. 基底与电场工程（h-BN/WSe₂、尖端功函数、层间偏压）可调控能带开隙与 DW 谱特征
5. PLL 能量对扭角、局域应变、堆垛细节敏感

## 6. 局限与未解决的问题

| 局限 | 说明 |
|------|------|
| 主文定量缺失 | 当前文件仅含 SI；PLL 序列完整索引、B_ps 绝对数值、拟合模型参数待补 |
| 电子侧机制不明 | 为何系统性缺失 PLL 仅给出经验结论，微观机制需定量理论 |
| 高阶 PLL 不清 | 峰宽增大 + 高能背景抬升限制分辨 |
| DW 通道差异 | 230 vs 260 meV 能量漂移观察到，但局域应变/原子堆垛逐点定量不足 |
| 探针条件依赖 | Au 修饰引入局域电场利于观测，但与器件栅控下的可重复性需交叉验证 |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| Yin et al. 2016（He group）| 最早 STM 单条 DW 拓扑边态 — 本文再分辨拓扑边态 + 发现中心 PLL 共存 |
| Huang 2018 PRL / Rickhaus 2018 | "可传导拓扑网络"图景 — 本文推进到"拓扑网络 + 局域化 PLL 共存" |
| Ramires & Lado 2018 PRL | 预言低角 TBG 中可电调规范场/PLL — 本文给出实验呼应，但揭示重构导致强电子-空穴非对称的现实修正 |
| Yoo 2019 Nat. Mater. | 结构重构基础 — 本文的 Kagome 图样是其自然电子学后果 |

## 8. 对后续研究的影响

- 为"可编程 DW 量子网络"提供**新自由度**：拓扑边态（边）+ PLL 局域态（中心）可分工设计
- 指向**基底与电场工程路线**：WSe₂/h-BN、栅控偏压、局域应变作为 Kagome 电子态控制旋钮
- 样品尺度 Kagome 电子纹理 → 探索非常规关联、分数量子输运、非平庸局域模的实验平台
- 建议后续：
  1. 双栅器件替代探针局域场，系统提取 PLL 序列与 B_ps
  2. 原子分辨应变场反演 → 解释不同 DW 通道能量分裂
  3. 扩展到温度、磁场与输运耦合测量

---

*精读完成日期：2026-08-06 | 基于 pdftotext 全文提取（SI 部分）+ AI 精读分析 | ⚠️ 主文正文定量细节待补充*

---

## Phase S 补充 (2026-08-11): Q1

### Q1: edge state 实验上如何表征?
STM/STS dI/dV 固定能量空间图。核心发现：畴壁网络呈现两类不同电子态——中心局域赝朗道能级态 + 两侧螺旋边缘态 → 样品尺度电子 Kagome 图案。通过中心和侧翼不同谱权重/能量依赖、畴壁通道空间分离和 AB/BA 区域不同谱区分边缘 vs 体。
