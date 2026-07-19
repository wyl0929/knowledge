<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-16 18:19:34
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-16 18:19:35
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/multilayer_graphene/subfields/stacking-dw/paper_review_jaskolski2024_arxiv.md
 * @Description  :
-->
<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-16
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/subfields/stacking-dw/paper_review_jaskolski2024_arxiv.md
 * @Description  : Jaskólski (2024) arXiv 阅读笔记
-->
# 论文精读：Jaskólski, arXiv:2403.11143 (2024)

> **Włodzimierz Jaskólski**
> "Metal-semiconductor behavior along the line of stacking order change in gated multilayer graphene"
> arXiv:2403.11143 (2024, 预印本)
>
> 作者单位：Nicolaus Copernicus University (Poland) | 单作者
>
> **DOI**: NEEDS_VERIFICATION（预印本，尚未正式发表）
> **Zotero Key**: `ZT_KEY_NEEDED`

---

## 1. 一句话总结

多层石墨烯中沿 armchair 方向的堆叠变化线可以表现为**金属**（无能隙态）或**半导体**（有效能隙），取决于栅压。$K$ 和 $K'$ 谷的拓扑态在动量空间中重叠 → 谷间耦合 → 有效能隙。特定栅压下费米能级处出现**平带**。

---

## 2. 背景与动机

### 2.1 已有知识背景

石墨烯中堆叠变化可以沿不同晶格方向：

| 方向 | $K$ 和 $K'$ 在 $k_{\parallel}$ 上的投影 | 谷间耦合 |
|---|---|---|
| **Zigzag** | 分离（投影到不同的 $k_{\parallel}$） | **弱**——谷间散射被动量守恒压制 |
| **Armchair** | **重叠**（投影到相同的 $k_{\parallel}$） | **强**——$K$ 和 $K'$ 态在 $k_{\parallel}$ 空间中重合 |

→ Armchair 方向的堆叠畴壁中，来自 $K$ 和 $K'$ 谷的拓扑态**强制相互作用**。

真实的堆叠畴壁处，剪切应变可以通过**层间裂纹**（某一层断裂）释放——裂纹引入原子尺度的缺陷，导致额外的散射势，进一步增强谷间耦合。

### 2.2 未解问题 / 本文填补的空白

此前 Jaskólski 2020 研究了 zigzag 方向的 ABC/CBA 畴壁（$K$ 和 $K'$ 可分离）。Armchair 方向畴壁的拓扑态行为——$K$-$K'$ 强制耦合的后果——完全未知。

---

## 3. 方法与模型

- **紧束缚模型**：多层石墨烯（$N \geq 3$），沿 armchair 方向的堆叠变化
- 考虑层间裂纹以释放剪切应变
- 沿畴壁方向平移对称性 → $k_{\parallel}$ 分类
- 栅压：层依赖 onsite 势

---

## 4. 核心结果

### 4.1 金属-半导体转变

- **低栅压**：畴壁处出现无能隙态 → **金属行为**（1D 导电通道）
- **高栅压**：$K$ 和 $K'$ 谷态重叠 + 裂纹散射 → 拓扑态之间打开**有效能隙** → **半导体行为**
- 通过调节栅压，可以在金属和半导体之间**可逆切换**

### 4.2 费米能级处的平带

- 在特定栅压下，畴壁处的能带色散变得**完全平坦**（$dE/dk_{\parallel} \approx 0$）
- 平带 = 态密度极大 → 电子-电子相互作用增强 → 可能出现关联效应
- 栅压的微小变化 → 平带中的电荷在层间振荡

### 4.3 谷间耦合的后果

- 与 zigzag 方向不同，armchair 畴壁中 $K$ 和 $K'$ 态**不可分离**
- → 畴壁态**不是纯谷极化的**（与 TBG AB/BA 畴壁的纯谷极化形成对比）
- → 谷间散射在 armchair 畴壁中**天然存在** → 弹道输运可能被抑制

### 4.4 层数的效应

- 更多层（$N > 3$）→ 更复杂的能带折叠 → 更多畴壁态
- 但谷间耦合和多带杂化使得金属行为**更难维持** → 半导体相更容易出现

---

## 5. 与其他工作的关系

| 维度 | Jaskólski 2020（zigzag 畴壁） | 本文（armchair 畴壁） |
|---|---|---|
| 畴壁方向 | zigzag | **armchair**（关键区别） |
| 层间裂纹 | 未考虑（平滑过渡） | **包含**裂纹缺陷 |
| $K$-$K'$ 耦合 | 弱（可分离处理） | **强**（重叠 → 强制耦合） |
| 畴壁行为 | 金属（无能隙态始终存在） | 金属**或**半导体（取决于栅压） |
| 平带 | 未涉及 | **预测**出现平带 |
| 发表状态 | PRB 102, 035424 | 预印本（NEEDS_VERIFICATION） |

---

## 6. 亮点与局限

### 亮点

1. **Armchair 畴壁的首次系统研究**：揭示 zigzag vs armchair 的谷间耦合本质差异
2. **金属-半导体栅控转变**：栅压可逆切换导电行为 → 可编程拓扑开关
3. **平带预测**：关联效应的可能平台

### 局限

| 局限 | 说明 |
|---|---|
| 预印本 | 未经同行评审，结果需独立验证 |
| 裂纹模型简化 | 真实裂纹的原子结构可能不同 |
| 仅能带计算 | 未涉及输运 |
| 无实验对标 | Armchair 方向的堆叠畴壁尚无可控实验 |

---

## 7. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **TBPM 独立验证** | Armchair vs zigzag 畴壁的 LDOS + $\sigma_{xx}$ 对比 → 验证谷间耦合差异 |
| **金属-半导体转变** | TBPM 扫 $D$ → 计算 $\sigma_{xx}$ → 验证电导开/关 |
| **平带验证** | TBPM DOS → 验证特定 $D$ 下畴壁处 DOS 峰 |
| **DW 项目新方向** | 不同的畴壁方向（armchair）可能提供与 zigzag 完全不同的输运特征 |

### NEEDS_VERIFICATION 标记

| 内容 | 状态 |
|---|---|
| 金属-半导体转变 | 预印本，需 TBPM 独立验证 |
| 平带的存在 | 未见实验报道 |
| 裂纹缺陷的必要性 | 真实体系中裂纹是否普遍？ |
| 栅压调控的可行性 | 实验上能否实现如此精细的栅压调控？ |

---

## 8. 参考文献链

```
Jaskólski 系列（堆叠畴壁 TB 理论）
├── Jaskólski et al., Nanoscale 8, 6079 (2016) — 双层 AB/BA 晶界：缺陷稳健性
├── Jaskólski & Sarbicki, PRB 102, 035424 (2020) — 三层 ABC/CBA zigzag 畴壁：每谷 3 条态
└── ★ 本文 — 多层 armchair 畴壁：金属-半导体转变 + 平带

相关实验
├── Yin et al., PRB 95, 081402(R) (2017) — 三层 ABA/ABC STM（畴壁方向未知）
└── Ju et al., Nature 520, 650 (2015) — 双层 AB/BA DW 输运

相关理论（谷间耦合）
├── Li et al., PRB 85, 201404(R) (2012) — ABC 三层 C_V=3，非平衡边缘模
└── Verbakel et al., PRB 103, 165134 (2021) — FT-STM 证明畴壁态谷保护
```

---

*报告生成日期：2026-07-16 | 基于 arXiv:2403.11143v1 (预印本)*
