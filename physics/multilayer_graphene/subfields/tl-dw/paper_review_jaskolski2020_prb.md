<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-16 18:19:32
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-16 18:19:33
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/stacking-dw/paper_review_jaskolski2020_prb.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-16
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/stacking-dw/paper_review_jaskolski2020_prb.md
 * @Description  : Jaskólski & Sarbicki (2020) PRB 阅读笔记
-->
# 论文精读：Jaskólski & Sarbicki, PRB 102, 035424 (2020)

> **W. Jaskólski, G. Sarbicki**
> "Topologically protected gap states and resonances in gated trilayer graphene"
> Phys. Rev. B 102, 035424 (2020) | arXiv:2005.11473
>
> 作者单位：Nicolaus Copernicus University (Poland)
>
> **DOI**: [10.1103/PhysRevB.102.035424](https://doi.org/10.1103/PhysRevB.102.035424)
> **Zotero Key**: `ZT_KEY_NEEDED`

---

## 1. 一句话总结

门控三层石墨烯中，当堆叠从 ABC 变为 CBA 时，**每个谷出现 3 条无能隙拓扑保护态**——数量由谷 Chern 数变化决定。这些态局域在堆叠畴壁处，是 ABA/ABC 畴壁一维导电通道的**微观理论描述**。

---

## 2. 背景与动机

### 2.1 已有知识背景

- ABC 和 CBA 是镜像关系：CBA = ABC 的上中下三层颠倒
- 两者手征性相同（$l=3$），但谷 Chern 数符号**相反**：$C^{ABC}_V = -C^{CBA}_V$
- ABC → CBA 的堆叠变化 = **纯粹的谷 Chern 数翻转** → 拓扑上最"干净"的畴壁

### 2.2 未解问题 / 本文填补的空白

- ABA → ABC 的堆叠变化更复杂（ABA 有两套能带，谷拓扑不纯粹）
- 如何通过顶层和底层的波纹化/剥离（corrugation/delamination）实现 ABC → CBA？
- 畴壁处会出现多少条无能隙态？与 $\Delta C_V$ 的关系是什么？
- 态的空间局域长度？栅压可调性？

---

## 3. 方法与模型

- **紧束缚模型**：标准石墨烯 $p_z$ 轨道 TB
- 层内耦合：$\gamma_0$（最近邻）
- 层间耦合：$\gamma_1, \gamma_3, \gamma_4$（包含三角翘曲）
- 门控：层依赖的 onsite 势 $\pm U/2$
- 沿畴壁方向保持平移对称性 → $k_{\parallel}$ 分类

---

## 4. 核心结果

### 4.1 每谷 3 条无能隙拓扑态

- 当 ABC → CBA 堆叠变化时，在体能隙中出现**3 条无能隙态**（per valley）
- 这 3 条态 = 顶层和底层剥离所产生的两组 AB/BA 双层畴壁的总贡献
- 态的数量与 $\Delta C_V$ 一致：$C^{ABC}_V = +3 \to C^{CBA}_V = -3$，但实际出现 3 条而非 6 条 → 层间耦合的选择定则

### 4.2 拓扑共振态（topological resonances）

- 在某些栅压范围内，导带和价带的**连续区**中额外出现**共振态**
- 共振态 = 准束缚在畴壁处但不完全位于能隙中的态
- 它们对态密度的贡献表现为展宽的峰（而非 $\delta$ 函数）→ 实验上可通过 STS 观测

### 4.3 态的空间局域

- 无能隙态高度局域在堆叠畴壁处（~几 nm）
- 共振态局域程度较弱，向畴内延伸

### 4.4 栅压可调性

- 改变栅压 → 体能隙大小变化 → 畴壁态的色散和局域长度随之变化
- 在特定栅压下，畴壁态的费米速度可通过最大值

---

## 5. 与其他工作的关系

| Yin 2017 实验观测 | 本文的理论解释 |
|---|---|
| 畴壁处 LL 从 $l=1,2$ → $l=3$ 平滑过渡 | 3 条无能隙拓扑态 = 手征性过渡的能带表现 |
| 畴壁 ~10 nm 宽 | 拓扑态的局域长度 ~几 nm → 态比畴壁本身更窄 |
| LL 峰在畴壁处展宽 | 3 条态混合 → 能级展宽 |

本文是 Li 2012（ABC 三层外边界 $C_V=3$）→ **内边界（堆叠畴壁）** 的直接推广，也是 Jaskólski 2024（金属-半导体转变）的理论前驱。

---

## 6. 亮点与局限

### 亮点

1. **首次 TB 级 ABC/CBA 畴壁能带计算**：给出每谷 3 条无能隙态的定量预测
2. **拓扑共振态概念**：连续区中的准束缚态——实验上可通过 STS 观测
3. **栅压可调性**：畴壁态的色散和局域长度可被栅压连续调控

### 局限

| 局限 | 说明 |
|---|---|
| ABC → CBA 非自然畴壁 | 需要层间剥离——实验上难以实现 |
| 无 ABA → ABC 畴壁 | 三层中最常见的畴壁类型（Yin 2017）未直接研究 |
| 仅能带计算 | 未涉及输运（$\sigma_{xx}, \sigma_{xy}$） |
| 忽略无序和温度效应 | 纯单粒子 TB + 完美周期性 |

---

## 7. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **TBPM 最直接基准** | 构造 ABC → CBA 畴壁 → TBPM 算 LDOS → 验证每谷 3 条无能隙态 |
| **输运扩展** | 本文未涉输运 → TBPM 可首次计算三层畴壁的 $\sigma_{xx}$ 和 $\sigma_{xy}$ |
| **栅压扫描** | TBPM 扫 $D$ 场 → 验证畴壁态的费米速度和局域长度的栅压依赖 |
| **DW 项目 Phase 5** | 本文的能带结果是三层 DW $\sigma_{xy}$ 计算的输入基准 |

---

## 8. 参考文献链

```
ABC 三层拓扑理论
├── Li et al., PRB 85, 201404(R) (2012) — C_V=3，非平衡边缘模
├── ★ 本文 — ABC/CBA 畴壁：每谷 3 条无能隙态 + 拓扑共振态
└── Jaskólski, arXiv:2403.11143 (2024) — 多层金属-半导体转变

实验基准
├── Yin et al., PRB 95, 081402(R) (2017) — 三层 ABA/ABC STM 实验
└── Ju et al., Nature 520, 650 (2015) — 双层 AB/BA DW 实验（方法论参考）
```

---

*报告生成日期：2026-07-16 | 基于 arXiv:2005.11473 + PRB 102, 035424 (2020)*
