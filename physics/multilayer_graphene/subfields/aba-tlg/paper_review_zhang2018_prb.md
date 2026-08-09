<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-20 19:54:45
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-20 19:54:46
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/stacking-dw/paper_review_zhang2018_prb.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-20
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/stacking-dw/paper_review_zhang2018_prb.md
 * @Description  : Zhang et al. (2018) PRB — ABA TLG 高分辨 STS 阅读笔记
-->
# 论文阅读笔记：Zhang et al., PRB 98, 045413 (2018)

> **Yu Zhang, Jia-Bin Qiao, Long-Jing Yin, Lin He**
> "High-resolution Tunneling Spectroscopy of ABA-stacked Trilayer Graphene"
> Phys. Rev. B 98, 045413 (2018) | arXiv:1804.08196
>
> 机构：北京师范大学，Lin He 组

---

## 1. 一句话总结

通过**高分辨 STM/STS** 首次在 ABA 三层石墨烯中同时观测到无质量 Dirac 费米子（$l=1$）和有质量 Dirac 费米子（$l=2$）的朗道能级——包括两者的 LL 交叉、有效质量重整化，以及**超出紧束缚模型预测的最低 LL 非常规分裂**→ 多体效应诱导的破缺对称量子霍尔态。

---

## 2. 背景：ABA TLG 的独特电子结构

### 2.1 两套 Dirac 费米子共存

ABA 三层是唯一同时包含两类 Dirac 费米子的石墨烯体系：

| 费米子类型 | 来源 | 色散 | LL 序列 |
|---|---|---|---|
| 无质量（massless） | Monolayer-like 带 | $E \propto k$ | $E_N \propto \sqrt{NB}$ |
| 有质量（massive） | Bilayer-like 带 | $E \propto k^2$ | $E_N \propto \sqrt{N(N-1)}B$ |

### 2.2 此前实验的困境

- ABA 和 ABC 堆叠在 STM 形貌图中难以区分 → 前人无法确保测量的是纯 ABA 区域
- 能谱分辨率不足 → LL 的精细分裂特征被掩盖
- 本文突破：**高分辨 STS** + 堆叠序的原子分辨鉴定

---

## 3. 实验方法

| 参数 | 细节 |
|---|---|
| 技术 | 低温 STM/STS（~4.2 K） |
| 磁场 | 0–8 T（垂直） |
| 样品 | 机械剥离三层石墨烯 on SiO₂ |
| 堆叠鉴定 | 原子分辨 STM 形貌图 → 区分 ABA vs ABC 畴 |
| 谱学 | 高分辨 $dI/dV$ 谱 → 朗道能级峰 |

---

## 4. 核心实验结果

### 4.1 无质量 + 有质量 Dirac 费米子的 LL 同时观测

- 在 $dI/dV$ 谱中同时观测到**两套 LL 序列**
- 一套满足 $\sqrt{N}$ 标度（$l=1$，massless）→ 来自 monolayer-like 带
- 一套满足 $\sqrt{N(N-1)}$ 标度（$l=2$，massive）→ 来自 bilayer-like 带
- 两套 LL 的 $N=0$ 都在电荷中性点（CNP）附近

### 4.2 LL 交叉（核心发现之一）

- 随着 $B$ 增大，massless 和 massive LL 在能量上**交叉**
- LL 交叉 = 两套 LL 的能级在特定 $B$ 下重合 → 态密度增强 → $dI/dV$ 中出现增强峰
- **为什么重要**：LL 交叉是 ABA TLG 特有的——单层和双层石墨烯都不具备。它是两套独立 LL 体系的直接证据。

### 4.3 有效质量重整化

- Massive Dirac 费米子的有效质量 $m^*$ 随 $B$ 增大
- $m^*(B) > m^*_{\text{TB}}$（紧束缚模型预测的裸质量）→ **电子-电子相互作用增强了有效质量**
- 这是多体效应的直接特征

### 4.4 最低 LL 的非常规分裂（最意外的发现）

- **massless $N=0$ LL** 和 **massive $N=0,1$ LL** 在高场下出现**超出紧束缚预测的额外分裂**
- 紧束缚（单粒子）计算无法复现这些分裂 → **多体效应机制**
- 可能的起源：
  - 谷对称性破缺（valley symmetry breaking）
  - 自旋极化（spin polarization）
  - 量子霍尔铁磁序（QH ferromagnetism）
- 这些分裂 = ABA TLG 中**破缺对称量子霍尔态**的 STS 直接证据

---

## 5. 物理意义

### 5.1 首次在单一样品中同时表征两套 Dirac 费米子的 LL

此前的研究要么只看 ABA 的输运（无法空间分辨），要么只看 ABC 的 STS。本文是**第一个**对纯 ABA 区域做高分辨 LL 谱学的工作。

### 5.2 LL 非常规分裂 → 多体物理的 STS 窗口

ABA TLG 的 QH 输运实验（如 Henriksen PRX 2012, Datta Nat. Commun. 2017）已暗示破缺对称态的存在。本文从**局域谱学**角度直接观测到这些态的**能谱特征**——互补于输运测量。

### 5.3 对 TBPM 计算的启示

| 观测 | TBPM 可验证 |
|---|---|
| massless + massive 两套 LL | ✅ 直接计算 LDOS vs $B$ |
| LL 交叉点 | ✅ 提取交叉 $B$ 和能量 |
| 有效质量 $m^*$ | ✅ 从 LL 间距拟合 $m^*$ |
| **LL 非常规分裂** | ⚠️ 单粒子 TB 无法复现 → 需要加 Hubbard $U$ 或 HF 修正 |

---

## 6. 关键参数

| 参数 | 值 |
|---|---|
| 体系 | ABA 堆叠三层石墨烯 |
| 磁场范围 | 0–8 T |
| 温度 | ~4.2 K |
| 两套 LL | $l=1$ (massless) + $l=2$ (massive) |
| 非常规分裂 | $N=0$ LL (massless) + $N=0,1$ LL (massive) |

---

## 7. 与 Lin He 组其他论文的关系

```
Zhang 2018 (PRB) ← 本文：ABA TLG 高分辨 STS
  ↓ 纯 ABA 区域的 LL 物理
Yin 2019 (PRL)  ← ABC TLG 高场 STS
  ↓ 纯 ABC 区域的 LL 物理
Yin 2017 (PRB)  ← ABA/ABC 堆叠孤子
  ↓ 两种区域的边界
```

---

*笔记创建日期：2026-07-20 | arXiv:1804.08196v1 + PRB 98, 045413 (2018)*
