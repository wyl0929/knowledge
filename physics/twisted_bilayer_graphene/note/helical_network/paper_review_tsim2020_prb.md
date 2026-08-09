<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 17:17:01
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 17:17:05
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/helical_network/paper_review_tsim2020_prb.md
 * @Description  :
-->
<!--
 * @Author       : AI精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/helical_network/paper_review_tsim2020_prb.md
 * @Description  : T12: Tsim, Nam & Koshino 2020 — TZM: 完美 1D 手征通道的发现
-->

# 论文精读：Tsim, Nam & Koshino, PRB (2020)

> **Bonnie Tsim, Nguyen N. T. Nam, Mikito Koshino**
> "Perfect one-dimensional chiral states in biased twisted bilayer graphene"
> PRB 101, 125409 (2020) | arXiv:2001.06257
>
> 作者单位：Manchester (Tsim), AIST Sendai (Nam), Osaka Univ. (Koshino)

---

## 1. 一句话总结

**推翻螺旋网络图景**：偏置下 mTBG 的拓扑通道**不形成渗流网络**，而是自组织为三组**独立的完美 1D 本征模**（topological zigzag mode, TZM），沿三个方向独立传播、永不杂化。

---

## 2. 背景与动机

### 2.1 已有知识背景

- Efimkin & MacDonald 2018 建立了螺旋网络模型：畴壁通道在 AA 点通过散射矩阵连接 → 2D 渗流网络
- 实验（Rickhaus 2018, Huang 2018）似乎支持网络图景
- 但在网络模型中，入射模在节点处分裂为多个出射模——是否存在更简单的图景？

### 2.2 未解问题

**TBG 的拓扑通道究竟是 2D 网络还是独立 1D 链？** 这决定了输运的本质是 2D 弱局域化还是 1D 弹道输运。

---

## 3. 方法与模型

### 3.1 连续模型

$$H_{\text{TBG}} = \begin{pmatrix} H_1 & U^\dagger \\ U & H_2 \end{pmatrix}$$

其中 $H_{1,2}$ 为单层 Dirac 哈密顿量（含偏置 $\pm\Delta/2$），$U$ 为摩尔层间耦合。

### 3.2 散射矩阵的关键发现

在每个 AA 节点，三进三出的 $S$ 矩阵是**对角的**（而非 Efimkin-MacDonald 的满矩阵）：

$$S_{\text{TZM}} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix} \quad \text{或等价排列}$$

即：每条入射通道**唯一地**连接到一个出射通道 → 无分束、无杂化 → 完美 1D 传播。

### 3.3 紧束缚 + 晶格弛豫

除连续模型外，还用了 TB 模型结合晶格弛豫（lattice relaxation）验证 TZM 对结构变形的稳健性。

---

## 4. 核心结果

### 4.1 两个 1D 能量窗口

偏置产生**两个明确的能量窗口**，每个窗口内含稀疏分布的完美 1D 本征模：

| 窗口 | 能量范围 | 特征 |
|------|---------|------|
| 窗口 1 | $E > 0$（导带侧） | 1D 模稀疏分布 |
| 窗口 2 | $E < 0$（价带侧） | 同上，电子-空穴不对称 |

两个窗口被电荷中性点附近的**近扁平带簇**隔开。

### 4.2 TZM 的几何结构

如图所示（Fig. 1(b)），TZM 沿 AB/BA 畴壁传播，但在 AA 点**绕过而非穿过**：
- 同一方向的 TZM 形成锯齿链（zigzag）
- 三个方向的 TZM 彼此独立——从不交叉杂化
- 每个 TZM 贡献 1 个 1D 导电通道（每谷每自旋）

### 4.3 晶格弛豫效应

晶格弛豫（AB/BA 区扩大、畴壁变窄）**不破坏 TZM**：
- TZM 仍然存在，能量窗口略有移动
- 证明 TZM 是 TBG 偏置相的 robust 特征，不依赖于理想化几何

### 4.4 物理起源

从**弱层间耦合极限**出发：偏置使上层 Dirac 锥（电子型）和下层 Dirac 锥（空穴型）在动量空间相交 → 交点处能隙打开 → 交点附近的态形成 1D 通道。两带模型的解析计算完美复现 TZM。

---

## 5. 与其他工作的关系

| 相关工作 | 关系 |
|----------|------|
| **Efimkin & MacDonald 2018** | 核心分歧：网络 vs TZM |
| De Beule et al. 2020 PRL (T15) | 对称性支持 TZM 不连通 |
| **Hou/Yuan/Jiang 2024** | 量子输运裁决：确认 TZM 胜出 |
| Rickhaus 2018 (实验) | FP+AB 振荡可用 TZM 重新解释（域内 FP，域间不连通） |

---

## 6. 亮点与局限

### 亮点
- **颠覆性发现**：推翻渗流网络图景，重新定义 TBG 畴壁输运的范式
- **方法完整**：连续模型 + TB + 晶格弛豫，三重交叉验证
- **实验可检验**：预言 1D 弹道输运特征（电导平台），区别于网络的 2D 弱局域化
- **物理图像清晰**：两带交叉模型直观解释 1D 窗口的起源

### 局限
- 仅考虑无相互作用单粒子物理
- 未计算有限温度 / 无序下的输运
- TZM 电导是否**严格**量子化未给出明确答案（Hou 2024 用 NQCP 补充）
- 未讨论不同偏置 / 转角下的相图边界

---

## 7. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **方法** | TZM 的 $S$ 矩阵对角性可用 tbplas + NEGF 验证 |
| **扩展方向** | DW 项目中检验：真实 TBG 几何下 TZM 的电导量子化程度 |
| **可验证性** | 1D 能量窗口的 LDOS 特征可用 tbplas 直接复现 |

---

## 8. 关键参数速查

| 参数 | 值/说明 |
|------|--------|
| 偏置 | $\Delta$（层间电位差）|
| TZM 方向数 | 3（沿三组平行畴壁方向）|
| 每方向通道数 | 1 条 TZM / 谷 / 自旋 |
| $S$ 矩阵 | 对角排列矩阵（无分束）|
| 1D 窗口宽度 | 依赖 $\Delta$ 和 $\theta$ |
| 晶格弛豫影响 | 不破坏 TZM，仅移动窗口 |

---

*报告生成日期：2026-08-06 | 基于 PDF pdftotext 精读*
