<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 22:03:08
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 22:03:13
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/mTBG_experiments/paper_review_E13_verbakel2021_prb.md
 * @Description  :
-->
<!--
 * @Author       : AI 精读 (research_onboarding_skill)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/mTBG_experiments/paper_review_E13_verbakel2021_prb.md
 * @Description  : E13: Verbakel et al. 2021 — FFT-STM 证明谷保护 + 室温网络
-->

# Paper Review: Verbakel et al. (2021) — FFT-STM 谷保护证据

| 字段 | 内容 |
|------|------|
| **编号** | E13 |
| **标题** | Valley-protected one-dimensional states in small-angle twisted bilayer graphene |
| **作者** | J.D. Verbakel, Q. Yao, K. Sotthewes, H.J.W. Zandvliet |
| **期刊** | Physical Review B 103, 165134 (2021) |
| **DOI** | 10.1103/PhysRevB.103.165134 |
| **arXiv** | 2109.04128 |
| **类型** | 实验 — 室温 STM/FFT |
| **课题组** | Zandvliet group (Univ. Twente) |
| **PDF** | ✅ reference/pdfs/Verbakel 等 - 2021 - ...pdf |
| **DW.bib** | ✅ `verbakel_valley-protected_2021` |
| **精读日期** | 2026-08-06 |

---

## 1. 核心贡献

通过**原子分辨 STM 图像的 FFT 散射分析**，首次给出"1D 通道输运具有 **valley protection（谷保护）**"的**直接实验证据**。填补了此前工作（Huang 2018 等）只"看见网络形貌"但未验证谷保护机理的关键空白。另一重要发现：**网络在室温即可观测**，无需低温 STM。

## 2. 物理机制 — FFT 如何揭示谷保护

### 2.1 谷保护的理论预期

- 若存在 valley protection → K 与 K' 的 intervalley backscattering 被抑制
- 在 STM 原子分辨图的 FFT 中，intervalley 散射产生特定的 $(\sqrt{3}\times\sqrt{3})R30^\circ$ 峰
- **若这些峰缺失 → intervalley 散射被抑制 → 与谷保护一致**

### 2.2 关键散射矢量

| 参数 | 值 |
|------|-----|
| 晶格 1×1 倒易矢量 |b|| $|b| = \frac{4\pi}{3a} \approx 2.95$ Å⁻¹ |
| intervalley 矢量 |ΔK|| $|\Delta K| = \frac{4\pi}{3\sqrt{3}a} \approx 1.70$ Å⁻¹ |

### 2.3 对照实验设计

- **有缺陷（H 吸附）HOPG**：FFT 出现 $(\sqrt{3}\times\sqrt{3})R30^\circ$ 峰（有 intervalley — "阳性对照"）
- **pristine HOPG**：仅 1×1 六角峰（基准无 intervalley）
- **TBG 网络区域**：FFT 仅见 1×1 峰、无 intervalley 峰（谷保护）

### 2.4 电场来源

STM 中电场 = 样品偏压 + 针尖/样品功函数差（纳米间隙下小功函数差也可形成可观电场）。

## 3. 实验方法

| 参数 | 值 |
|------|-----|
| 样品 | HOPG（天然 Bernal 堆垛，表层常有自然扭转形成 TBG）|
| 仪器 | Omicron STM1 |
| 探针 | 电化学刻蚀 W 针尖 |
| 环境 | 超高真空，基底压强 3 × 10⁻¹¹ mbar |
| 温度 | **室温** |
| 网络图（Fig.1a）| V_b = 400 mV, I_t = 500 pA |
| pristine HOPG（Fig.3a）| V_b = −600 mV, I_t = 1 nA |
| H 缺陷 HOPG（Fig.3c）| V_b = −500 mV, I_t = 600 pA |
| TBG AA 原子分辨（Fig.3e）| V_b = 400 mV, I_t = 500 pA |

## 4. 关键数据

### 4.1 样品参数

| 参数 | 值 |
|------|-----|
| 扭角 θ | 0.55°（由 moiré 周期提取）|
| 边界 valley Chern 数变化 | ΔC_v = ±2 |
| 每边界每谷通道数 | 2（计入自旋 → 总电导 4e²/h）|

### 4.2 FFT 判据结果

| 区域 | 1×1 峰 | $(\sqrt{3}\times\sqrt{3})R30^\circ$ 峰 | 含义 |
|------|:---:|:---:|------|
| pristine HOPG | ✅ | ❌ | 基准无 intervalley |
| H 缺陷 HOPG | ✅ | ✅ | intervalley "阳性对照" |
| TBG 网络（AA+域墙）| ✅ | ❌ | intervalley 被抑制 = 谷保护 |

### 4.3 室温网络观测

在 θ = 0.55° 的 TBG 上直接看到三角形 1D 网络（域墙为链路、AA 为节点），证明网络在室温即可稳定存在。

## 5. 主要结论

1. 小角 TBG 中三角形 1D 网络态在**室温可观测**，不依赖低温 STM
2. FFT-STM 散射峰判据 → intervalley 散射缺失 → 输运 valley-protected（实验确认）
3. 谷保护网络可跨多个 moiré 周期延伸，前提是上下层晶格高质量、无缺陷
4. 单个原子级缺陷理论上可能局部破坏谷保护 → 实用化对材料质量要求高

## 6. 局限与未解决的问题

| 局限 | 说明 |
|------|------|
| 局域探针证据 | 非器件级非局域输运测量；长程输运长度/散射率未直接给出 |
| 电场未精确标定 | 功函数差依赖针尖几何，可控性有限 |
| 自然样品 | 来自 HOPG 表层自然扭转，"发现式"非可编程制备 |
| 温度窗口 | 仅证明"室温可见"，上限/热稳定性未系统测试 |
| 缺陷剂量-退化关系 | 仅有理论讨论，无受控缺陷实验 |
| 高温退火风险 | 可能导致 TBG "untwist" 回 Bernal → 器件后处理窗口受限 |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| Huang 2018 PRL | 低温 STM 发现网络 — 本文补上"是否 valley-protected"关键环节 + 推进到室温 |
| San-Jose & Prada、Efimkin & MacDonald、Tsim & Koshino | 理论预言 valley Chern 机制 — 本文给出直接实验呼应 |
| Rickhaus 2018 / Xu 2019（输运）| 网络导电现象 — 本文提供原子尺度散射通道"为什么能保持谷选择性"的显微证据 |
| Yin 2016（He group）| 最早 STM 观测单条畴壁 — 本文方法更系统（FFT 定量判据）|

## 8. 对后续研究的影响

- **FFT-STM 方法学**：可作"谷保护是否成立"的**快速诊断工具**
- 室温可观测性 → 降低器件化对极低温的依赖
- 强调"超低缺陷密度"是谷保护网络实用化的前提 → 推动更高质量 TBG 制备
- 为 valleytronic 网络器件（分束、路由、干涉）提供实验依据
- 后续关键问题：
  1. 缺陷类型/浓度 — intervalley 散射 — 器件性能定量图谱
  2. STM/FFT 证据与多端输运量测（非局域、长度依赖、温度依赖）一一对应

---

*精读完成日期：2026-08-06 | 基于 pdftotext 全文提取 + AI 精读分析*

---

## Phase S 补充 (2026-08-11): Q1

### Q1: edge state 实验上如何表征?
原子分辨 STM + 实空间晶格 FFT 分析。核心可观测量：FFT 中谷间散射峰 $(\sqrt{3}\times\sqrt{3})R30^\circ$ 的缺失——直接证明谷间背散射被抑制 = 谷保护。畴壁网络峰缺失 vs 缺陷石墨烯对照清晰可见。通过 1D 网络空间局限和选择性散射行为区分边缘 vs 体。首次直接 STM/FFT 证实谷保护。
