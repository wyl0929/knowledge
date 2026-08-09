<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 22:02:11
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 22:02:14
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/mTBG_experiments/paper_review_E10_rickhaus2018_nanolett.md
 * @Description  :
-->
<!--
 * @Author       : AI 精读 (research_onboarding_skill)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/mTBG_experiments/paper_review_E10_rickhaus2018_nanolett.md
 * @Description  : E10: Rickhaus et al. 2018 — mTBG 拓扑网络输运 FP+AB 振荡
-->

# Paper Review: Rickhaus et al. (2018) — mTBG 拓扑网络输运的 FP+AB 振荡

| 字段 | 内容 |
|------|------|
| **编号** | E10 |
| **标题** | Transport Through a Network of Topological Channels in Twisted Bilayer Graphene |
| **作者** | Peter Rickhaus, John Wallbank, Sergey Slizovskiy, Riccardo Pisoni, Hiske Overweg, Yongjin Lee, Marius Eich, Ming-Hao Liu, Kenji Watanabe, Takashi Taniguchi, Thomas Ihn, Klaus Ensslin |
| **期刊** | Nano Letters 18, 6725–6730 (2018) |
| **DOI** | 10.1021/acs.nanolett.8b02387 |
| **arXiv** | 1802.07317 |
| **类型** | 实验 — 低温输运 |
| **课题组** | Ensslin group (ETH Zurich) |
| **PDF** | ✅ reference/pdfs/Rickhaus 等 - 2018 - ...pdf |
| **DW.bib** | ✅ `rickhaus_transport_2018` |
| **精读日期** | 2026-08-06 |

---

## 1. 核心贡献

首次在 mTBG 输运实验中同时观测到：

1. **Fabry-Pérot（FP）振荡** — 随载流子密度调谐
2. **Aharonov-Bohm（AB）振荡** — 随磁场调谐

最关键发现：这些干涉振荡在 **0 到 8 T 垂直磁场下持续存在**，与常规二维体系截然不同（二维体态轨道会被洛伦兹力弯折而抑制 FP 干涉）。从"振荡对磁场鲁棒 + 振荡对密度呈线性周期"两点出发，证明体内电流主要沿**拓扑保护的一维通道网络**传播。

## 2. 物理机制

### 2.1 拓扑网络的形成

1. tBLG 中 AB/BA 堆垛交替出现 → moiré 超晶格
2. 外加位移场 D → AB/BA 区域开隙并被耗尽
3. AB/BA 区域 valley Chern number 不同 → 边界出现 helical valley Hall 通道
4. 通道连接 AA 节点 → 构成网络

### 2.2 扭角条件（重要修正）

- 早期理论：θ < 0.3° 才够
- **本文实测：θ ≈ 0.42° 仍观察到此网络输运** — 晶格弹性形变放宽了条件

### 2.3 为什么 FP 在磁场中持续存在？

- 常规二维 FP：$2R_c > L$ 需满足，B↑ 轨道弯折 → 干涉消失
- 本文 regime II：振荡持续到 8 T — 主导路径不是二维体轨道，而是受拓扑/谷守恒约束的一维通道
- 8 T 时磁长 ~9 nm ≪ 器件几何尺寸，仍保持干涉

### 2.4 为什么是 1D 而非 2D？

FP 共振在密度上呈**等间距 Δn**（线性周期），对应 1D 的 $k_F \propto n_{1D}$。若为 2D，应为 $k_F \propto \sqrt{n}$（非等间距），实验未见。

## 3. 实验方法

### 3.1 器件参数

| 参数 | 值 |
|------|-----|
| 扭角（制备目标） | ~0.5° |
| 扭角（Hofstadter 实测） | θ = 0.42° |
| moiré 周期 λ | 33 nm |
| hBN 厚度 | d_top = 27 nm, d_bottom = 45 nm |
| hBN 介电常数 | ε = 3.2 |
| 顶栅腔长 L | 200, 300, 400 nm |
| 器件宽度 W | 4.6 μm（L ≪ W，多并行通道） |

### 3.2 栅控关系

- $n_{in} = (C_{tg}V_{tg} + C_{bg}V_{bg})/e$
- $D \approx (D_{top} - D_{bottom})/2$

### 3.3 测量

- 温度：1.5 K
- 方法：低频锁相差分电导 dG/dn_in(n_in, n_out)
- 分析：FFT（含 2D FFT）提取周期与特征尺度

## 4. 关键数据

### 4.1 Moiré 标定

| 参数 | 值 |
|------|-----|
| 第一带充满密度 |n₂| | ~0.8 × 10¹² cm⁻² |

### 4.2 Regime I（常规 n-p-n FP）

- 条件：n_in ≪ 0, n_out ≫ 0
- 提取有效腔长 ~550 nm（> 设计 400 nm，归因于平滑边界过渡）
- 振荡在 B > 0.5 T 时消失（符合 2D 轨道弯折图像）

### 4.3 Regime II（拓扑网络主导）

- 条件：小 |n_in| < |n₂| + 大 D（AB/BA 开隙）
- n-B 图出现交叉斜线共振（正负斜率并存 = 顺/逆时针包围同一区域）
- **振荡从 0 持续到至少 8 T**

### 4.4 振荡周期提取

| 参数 | 值 | 含义 |
|------|-----|------|
| ΔB | 0.37 T | AB 磁场周期 |
| A = Φ₀/ΔB | ~11200 nm² | 闭合回路面积 |
| Δn_in | 4.7 × 10¹⁰ cm⁻² | FP 密度周期 |
| L_tot | ~870 nm | 相干路径总长 |
| 等效长方形 | 408 nm × 27 nm | 27 nm ≈ λ√3/2 ≈ 29 nm |

> 面积 > moiré 单胞（~950 nm²），≪ 顶栅腔面积（~2 × 10⁶ nm²），支持"环绕一排 AB/BA 区域"的图像。

### 4.5 顶栅长度依赖

L = 200/300/400 nm 比较：L 越小 → ΔB 与 Δn_in 越"慢"（更大尺度周期），与"环绕一排 AB/BA 区域"模型一致。

### 4.6 位移场依赖

D 减小时振荡的 n_in 窗口收缩（如 D = −1 V/nm）；D 减小 → AB/BA 能隙变小 → 1D 费米面涂抹 → 退相干。

## 5. 主要结论

### 证明 1D 输运的证据链

1. FP 共振在密度上呈线性等间距（非 √n 标度）
2. n-B 图共振线形态与 1D 通道模型一致
3. 背景电导平缓 → 固定数量 1D 通道参与输运

### 证明拓扑保护的证据链

1. 仅在大 D + 小 n_in 条件下出现 → 符合 valley Hall 网络形成条件
2. 振荡 0–8 T 持续 → 不受洛伦兹力弯折抑制
3. 轨道尺度介于"单胞与整腔之间" → 体内网络闭环，非边缘态
4. D 依赖边界与理论费米速度涂抹一致

## 6. 局限与未解决的问题

| 局限 | 说明 |
|------|------|
| 无实空间成像 | 路径几何有非唯一性 |
| 多闭环族 | AA 节点多谷散射路径复杂，实验只提取主导尺度 |
| B 上限 | 仅到 8 T（设备限制），更高场行为未知 |
| 非拓扑替代机制 | 未完全排除所有非拓扑解释 |
| 节点散射矩阵 | 谷间散射率与无序的定量关系未知 |

## 7. 与其他工作的关系

| 工作 | 关系 |
|------|------|
| Huang 2018 PRL | STM 给出局域实空间证据 — 本文提供互补输运证据 |
| Efimkin & MacDonald 2018 | 理论框架 — 本文 D 触发机制与之一致 |
| San-Jose & Prada 2013 | 螺旋网络预言 |
| 传统 QH 干涉 | 本文是体内网络干涉（低场→高场连续），非边缘态主导 |

## 8. 对后续研究的影响

- 证明 moiré 拓扑网络不仅在局域探针下可见，**在器件尺度上也可支持相干量子输运**
- 为 valleytronics 提供二维可编程网络平台（优于单一边缘通道几何）
- 展示"避开物理边缘"的鲁棒性优势
- 推动 AA 节点散射与谷守恒规则的定量建模
- 从"能带与局域态"走向"可操控相干输运功能器件"的关键桥梁

---

*精读完成日期：2026-08-06 | 基于 pdftotext 全文提取 + AI 精读分析*
