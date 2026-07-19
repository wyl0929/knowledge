<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-16 18:18:08
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-17 20:43:26
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/tl-dw/paper_review_yin2017_prb.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-16
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-16
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/stacking-dw/paper_review_yin2017_prb.md
 * @Description  : Yin et al. (2017) PRB Rapid Comm. 阅读笔记
-->
# 论文精读：Yin et al., PRB 95, 081402(R) (2017) ★ 唯一实验

> **Long-Jing Yin, Wen-Xiao Wang, Yu Zhang, Yang-Yang Ou, Hao-Ting Zhang, Cai-Yun Shen, Lin He**
> "Observation of Chirality Transition of Quasiparticles at Stacking Solitons in Trilayer Graphene"
> Phys. Rev. B 95, 081402(R) (2017) | arXiv:1609.00080
>
> 作者单位：北京师范大学，Lin He 组（STM 石墨烯研究的主要组之一）
>
> **DOI**: [10.1103/PhysRevB.95.081402](https://doi.org/10.1103/PhysRevB.95.081402)
> **Zotero Key**: `P5NHJ629`

---

## 1. 一句话总结

通过**高场 STM 朗道能级谱学**在实空间中直接观测到：三层石墨烯中 ABA 和 ABC 堆叠畴被 ~10 nm 宽的堆叠孤子分隔，准粒子的手征性在畴壁处从 ABA 侧的 $l=1,2$ **平滑过渡**到 ABC 侧的 $l=3$。这是 ABA/ABC 堆叠畴壁领域的**唯一实验基准**。

---

## 2. 背景与动机

### 2.1 已有知识背景：三层石墨烯的手征性

石墨烯中准粒子的"手征性"由低能哈密顿量的形式决定：

| 体系 | 低能色散 | 手征性 $l$ | 朗道能级 |
|---|---|---|---|
| 单层 | $E \propto k$ (Dirac) | $l=1$ | $E_N \propto \sqrt{N}$ |
| AB 双层 | $E \propto k^2$ | $l=2$ | $E_N \propto \sqrt{N(N-1)}$ |
| ABC 三层 | $E \propto k^3$ | $l=3$ | $E_N \propto B^{3/2} N^{3/2}$ |
| **ABA 三层** | ML 带 $E \propto k$ + BL 带 $E \propto k^2$ | **$l=1,2$ 混合** | 两套 LL 共存 |

### 2.2 未解问题 / 本文填补的空白

- ABA 和 ABC 堆叠是三层石墨烯的两种最稳定构型
- 真实样品中两者常以**畴**的形式共存，被堆叠孤子分隔
- 但**堆叠孤子处准粒子的行为**——手征性如何从一侧过渡到另一侧——完全未知

---

## 3. 方法与模型

### 3.1 实验技术

| 参数 | 细节 |
|---|---|
| 技术 | 低温高场 STM/STS（扫描隧道显微镜/谱学） |
| 磁场 | 高达 ~8 T（垂直样品平面） |
| 温度 | ~4.2 K |
| 样品 | 机械剥离三层石墨烯 on SiO₂/Si |

### 3.2 关键测量策略

**空间分辨的朗道能级谱学**：
1. 在实空间中定位 ABA 畴、ABC 畴和畴壁
2. 在每个位置测量 $dI/dV$ 谱（反映局域 DOS）
3. 在高场下（$B \sim 8$ T），DOS 中出现尖锐的朗道能级峰
4. 通过 LL 峰的**能量位置和间距**反推准粒子的手征性

---

## 4. 核心结果

### 4.1 堆叠孤子的实空间成像

- ABA 和 ABC 畴在 STM 形貌图中可区分（不同的摩尔条纹或原子分辨特征）
- 畴壁宽度：**~10 nm**——比 TBG 的 AB/BA 畴壁（~5 nm，晶格重构后）更宽
- 畴壁是平滑的、无原子尺度尖锐特征 → 堆叠变化是渐进的

### 4.2 ABA 侧的朗道能级

- 观测到**两套 LL**：$l=1$（monolayer-like，$E_N \propto \sqrt{N}$）和 $l=2$（bilayer-like，$E_N \propto \sqrt{N(N-1)}$）
- $N=0$ LL 在电荷中性点附近 → 两套 LL 的 $N=0$ 能量接近

### 4.3 ABC 侧的朗道能级

- 观测到**单一手征性**的 LL 序列：$E_N \propto B^{3/2} N^{3/2}$
- 与 ABC 三层的理论预测（$l=3$ cubic Dirac）一致

### 4.4 畴壁处：手征性的平滑过渡（核心发现）

- 在不同位置（ABA 侧 → 中心 → ABC 侧）测量 $dI/dV$
- **ABA 侧**：清晰的 $l=1,2$ 两套 LL 峰
- **畴壁中心**：LL 峰展宽，两套峰开始合并
- **ABC 侧**：单一 $l=3$ 的 LL 序列
- **关键结论**：准粒子的手征性在 ~10 nm 的空间尺度上从 $l=1,2$ **连续过渡**到 $l=3$

---

## 5. 与其他工作的关系

### 5.1 "晶体堆叠 → 准粒子手征性"的直接证明

首次在实验上建立了**实空间晶体结构与动量空间电子性质之间的直接对应**。

### 5.2 堆叠孤子 = 拓扑畴壁

$l=1,2 \to l=3$ 的手征性变化 → 体能带拓扑变化 → 堆叠孤子分隔不同拓扑相 → 暗示畴壁处可能存在拓扑保护的 1D 态。本文为 Jaskólski 2020, 2024 理论提供了直接实验动机。

### 5.3 与 TBG AB/BA 畴壁的类比

| 维度 | TBG AB/BA 畴壁 | ABA/ABC 堆叠孤子 |
|---|---|---|
| 畴壁起源 | 转角 → 摩尔超晶格 | 晶体生长/应变 → 堆叠变化 |
| 拓扑保护 | 谷 Chern 数差 $\Delta C_V$ | 手征性 $l$ 差异 → 能带拓扑类差异 |
| 畴壁宽度 | ~5 nm | ~10 nm |
| 表征手段 | STM/STEM + 输运 | 仅 STM |

---

## 6. 亮点与局限

### 亮点

1. **唯一实验**：ABA/ABC 堆叠畴壁的唯一实验基准——所有后续理论（Jaskólski 系列）的唯一定标参考
2. **高场 LL 谱学**：通过 LL 能量间距反推手征性变化——方法优雅
3. **畴壁宽度 ~10 nm**：比 TBG 畴壁宽——为理论计算提供了过渡区宽度参数

### 局限

| 局限 | 说明 |
|---|---|
| 仅高场（~8 T） | 零场下的畴壁电子结构未知 |
| 无 $D$ 场调控 | SiO₂ 背栅无法施加大的位移场 |
| 无输运测量 | 仅 DOS，未测畴壁处 $\sigma$ 或 $R$ |
| 单样品 | 畴壁宽度的普适性未知 |
| 空间分辨有限 | STM ~1 nm → 畴壁内部精细电子结构未被分辨 |

---

## 7. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **TBPM 直接复现** | 构造 ABA/ABC DW → Peierls 替换加磁场 → TBPM LDOS → 提取 LL 谱 → 对标本文 |
| **零场 LDOS 预测** | 本文仅高场数据 → TBPM 可计算零场下畴壁处的能带和 LDOS |
| **$D$ 场效应** | 本文无 $D$ 场调控 → TBPM 可扫层偏压预测 $D$ 场对畴壁态的影响 |
| **DW 输运扩展** | 本文仅 DOS → TBPM 可首次计算 ABA/ABC DW 的 $\sigma_{xx}$ 和 $\sigma_{xy}$ |

---

## 8. 关键参数速查

| 参数 | 值 |
|---|---|
| 畴壁宽度 | ~10 nm |
| 磁场 | ~8 T |
| 温度 | ~4.2 K |
| ABA 侧手征性 | $l=1,2$（两套 LL） |
| ABC 侧手征性 | $l=3$（单套 LL） |
| 畴壁处行为 | 手征性平滑过渡（~10 nm 空间尺度） |
| 样品 | 机械剥离 TLG on SiO₂ |
| 技术 | 高场 STM/STS，$dI/dV$ 谱学 |

---

*报告生成日期：2026-07-16 | 基于 arXiv:1609.00080 + PRB 95, 081402(R) (2017)*
