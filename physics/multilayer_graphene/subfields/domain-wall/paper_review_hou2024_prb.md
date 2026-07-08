<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-08 16:02:17
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-08 16:02:18
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/domain-wall/paper_review_hou2024_prb.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-08
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-08
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/domain-wall/paper_review_hou2024_prb.md
 * @Description  : Hou et al. (2024) PRB Letter 精读报告
-->
# 论文精读：Hou, Yuan & Jiang, PRB 110, L161406 (2024)

> **Zhe Hou, Kai Yuan, Hua Jiang**
> "Arrays of one-dimensional conducting channels in minimally twisted bilayer graphene"
> Phys. Rev. B 110, L161406 (2024) | arXiv:2408.09843
>
> 作者单位：侯哲（南京师范大学物理科学与技术学院）、袁凯（联合微电子中心）、蒋华（复旦大学）
>
> **DOI**: [10.1103/PhysRevB.110.L161406](https://doi.org/10.1103/PhysRevB.110.L161406)
> **Zotero Key**: `ZT_KEY_NEEDED` → `cmd.exe /c start "zotero://select/items/ZT_KEY_NEEDED"`

---

## 1. 一句话总结

在小转角双层石墨烯（mTBG）中施加层间偏压后，AB/BA 堆叠畴壁处的拓扑螺旋态（THS）**不是**形成人们普遍认为的二维三角网络，而是**自组织成独立传播的一维拓扑锯齿模式（TZM）**，每条 TZM 绕过 AA 堆叠点、独立传播——等效于在二维平台上实现了一维导电通道阵列。

---

## 2. 背景与动机

### 2.1 物理背景

在小转角（$\theta \ll 1.1^\circ$，远小于魔角）的双层石墨烯中：
- 摩尔周期极大 → AB 和 BA 堆叠区域形成大片畴（domain）
- 畴壁（domain wall）处出现拓扑保护的螺旋边缘态（topological helical states, THSs）
- 这些 THSs 来源于 AB/BA 畴壁两侧谷 Chern 数之差 $\Delta C_V = 2$

### 2.2 核心争议

| 模型 | 描述 | 支持证据 |
|---|---|---|
| **二维三角网络模型**（主流观点） | THSs 在 AA 堆叠点处交汇，电子被散射到其他三个方向 → 形成 2D 导电网络 | LDOS 分布、Aharonov-Bohm 振荡实验（Rickhaus 2018, Xu 2019） |
| **一维锯齿模式（TZM）模型**（少数派） | THSs 在 AA 点处**不交汇**，而是绕过 AA 点、沿三个独立方向传播 | 能带计算（Tsim & Koshino 2020）、对称性分析（De Beule 2020） |

**本文目标**：通过严格的量子输运模拟，**首次**在真实空间结构中裁决这场争议。

---

## 3. 方法与模型

### 3.1 器件结构

- **两端口输运器件**：底部为未转角的 graphene nanoribbon（宽度 $N$），顶部放置一个转角矩形 graphene flake（长度 $L$，转角 $\theta$）
- 未重叠区域通过物理刻蚀或电学门控去除 → 获得**平直边界**的 TBG 纳米片
- 层间施加偏压 $\Delta$（通过双栅调控）

### 3.2 紧束缚哈密顿量

$$
H = \sum_{\alpha,i} (-1)^\alpha \Delta |i,\alpha\rangle\langle i,\alpha| + \sum_{\alpha,i,j} t_{ij}^{\alpha\alpha} |i,\alpha\rangle\langle j,\alpha| + \sum_{\alpha\neq\alpha',i,j} t_{ij}^{\alpha\alpha'} |i,\alpha\rangle\langle j,\alpha'|
$$

- $\alpha=1(2)$：顶层（底层）
- 层内 hopping：标准 graphene $p_z$ 轨道紧束缚
- 层间 hopping：Slater-Koster 公式，$V_{pp\pi}$ 和 $V_{pp\sigma}$ 为位置依赖的衰减函数
- hopping 截断：面内 $3a$（$a$ 为 C-C 键长）

### 3.3 输运计算方法

零温两端口微分电导：

$$
G(E_F) = \frac{2e^2}{h} \text{Tr}\left[\Gamma_L G_C^r \Gamma_R G_C^a\right]
$$

- 使用非平衡格林函数（NEGF）方法
- 左右 lead 为 monolayer graphene 半无限纳米带
- 自能 $\Sigma_{L(R)}^r$ 通过迭代方法计算

---

## 4. 核心结果

### 4.1 近量子化电导平台（NQCP）

**主要发现**：在 $0.76^\circ < \theta < 0.91^\circ$ 范围内，$G \approx 1.99 \times 2e^2/h$，接近量子化值 2。

<center>

| 条件 | 平台值 | 物理来源 |
|---|---|---|
| 扭转中心在原点 $O$，$\Delta = 0.3$ eV，$E_F = -70$ meV | $G \approx 2$（单位 $2e^2/h$） | 两条纵向 TZM |
| 扭转中心移至下边界 | $G \approx 1$ | 一条纵向 TZM |
| 更大宽度 $N=209$，$\theta=0.74^\circ$ | $G \approx 3$ | 三条纵向 TZM |

</center>

### 4.2 TZM 数目的调控

TZM 数目 = 器件宽度内容纳的 AA 堆叠点阵列数 − 1，可通过以下方式调控：
- **扭转中心位置**：移动扭转中心改变 AA 点阵列相对于边界的排列
- **纳米带宽度 $N$**：更宽 → 更多 AA 点阵列 → 更多 TZM
- **扭转角 $\theta$**：更大的 $\theta$ → 更密的摩尔图案 → 更多 TZM（但耦合也会增强）

### 4.3 非平衡 LDOS 直接可视化

通过计算非平衡局域态密度 $\rho_{NE}(\mathbf{r}_i^b)$，直接展示了：
- TZM 呈现**扭曲的一维轨迹**，绕过 AA 堆叠点
- 不同 TZM 在实空间中**完全不耦合**
- 这排除了二维网络模型的散射图像

### 4.4 稳健性

- 对边界形状不敏感（平直边界即可）
- 对短程点杂质不敏感（一维通道中电子散射率显著降低）
- 晶格重构（lattice reconstruction）会**增强**平台质量——因为 AB/BA 区域扩大、畴壁更锐利

### 4.5 谷极化

所有导电通道都是**100% 谷极化**的（通过偏压符号可切换 $K \leftrightarrow K'$），在 valleytronics 中有应用前景。

---

## 5. 与实验的关系

| 实验 | 本文解释 |
|---|---|
| **Rickhaus et al., Nano Lett. 18, 6725 (2018)** — Fabry-Pérot 振荡 | 被 TZM 模型自然解释（电子在边界之间来回反射），**不需要**二维网络 |
| **Xu et al., Nat. Commun. 10, 4008 (2019)** — Aharonov-Bohm 振荡 | 可能来源于两条 TZM + 接触电极形成的闭合回路，**不证明**二维网络模型 |
| **Mahapatra et al., Nano Lett. 22, 5708 (2022)** — 量子霍尔干涉 | 与 TZM 图像一致 |

**关键实验预言**：近量子化电导平台（$G \approx 1, 2, 3 \times 2e^2/h$）是 TZM 的**决定性实验特征**（smoking gun）。如果实验上在 mTBG 两端口器件中观测到这些平台，将直接证实 TZM 模型。

---

## 6. 论文亮点与局限

### 亮点

1. **裁决了领域内的重要争议**：首次通过严格量子输运计算证明 TZM 模型而非二维网络模型
2. **方法可靠**：使用真实空间紧束缚 + NEGF，捕捉了 AA/AB/BA 区域的平滑过渡（之前的等效模型无法做到）
3. **实验可检验**：提出了明确、可操作的实验验证方案（NQCP）
4. **应用前景清晰**：等效于在二维材料上实现一维导电通道阵列，可用于 valleytronics

### 局限

1. **仅考虑弹道输运**：未包含声子散射、电子-电子相互作用
2. **零温计算**：有限温度下的平台热展宽未讨论
3. **无磁场**：有限磁场下的物理（如 Hofstadter 物理与 TZM 的相互作用）未被探讨
4. **紧束缚参数的敏感性**：层间耦合参数 $\gamma_0, \gamma_1$ 的选择可能影响定量结果

---

## 7. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **紧束缚方法** | 与用户的 graphene TB 代码同源——可以直接在自己的代码中复现 mTBG 结构 |
| **输运计算** | NEGF 方法与用户的 TBPM Kubo-Bastin 互补——NEGF 适合弹道/相干输运，TBPM 适合大体系扩散输运 |
| **畴壁物理** | mTBG 的 AB/BA 畴壁是转角体系中普遍存在的结构——在 TMBG 等三层体系中也可能存在类似的一维通道 |
| **可验证性** | 该文的 NQCP 预言可以在用户的 TBPM 代码中用 Kubo-Bastin 方法独立验证（计算两端口 $\sigma_{xy}$ 或 $G$） |
| **扩展方向** | (1) mTBG 的有限温/Fermi 能扫描；(2) 三层 mTBG 的畴壁通道；(3) 磁场下的 TZM |

---

## 8. 关键参考文献链

```
Martin, Blanter & Morpurgo, PRL 100, 036804 (2008)
  └→ 预言 bilayer graphene 畴壁处的拓扑束缚态
      └→ San-Jose & Prada, PRB 88, 121408 (2013) — TBG 中的螺旋网络
          └→ Efimkin & MacDonald, PRB 98, 035404 (2018) — 螺旋网络模型
              ├→ Tsim & Koshino, PRB 101, 125409 (2020) — TZM 的能带证据
              ├→ De Beule et al., PRL 125, 096402 (2020) — 对称性论证
              └→ ★ Hou, Yuan & Jiang, PRB 110, L161406 (2024) — 输运裁决
```

---

*报告生成日期：2026-07-08 | 基于 arXiv:2408.09843v1 + PRB 110, L161406*
