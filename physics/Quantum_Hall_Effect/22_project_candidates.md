<!--
Field: 量子霍尔效应
Mode: quick_scan
Domain archetype: science_technical
Created date: 2026-06-10
-->

---
document_type: project_candidates
schema_version: v1.0-rc2
field: "量子霍尔效应"
last_updated: YYYY-MM-DD
---

# 22 候选研究项目

Last updated: 2026-06-10

## Gate compliance / 门控合规

- Concept Boundary Contract: `resolved`
- 核心论断状态: `mixed`（CL-04/CL-05 为 confirmed，CL-06/CL-07 为 suspected）
- Operationalization status for priority projects: 见各项目条目

---

## 项目优先级总览

| ID | 项目 | 优先级 | 与工具契合度 | 操作化状态 | 预计周期 |
|----|------|:---:|:---:|:---:|:---:|
| P1 | TBPM 框架下 Chern 数计算模块 | 🔴 priority | ★★★★★ | specified | 1-2 周 |
| P2 | 石墨烯基 QAHE 材料 TB 扫描 | 🔴 priority | ★★★★★ | provisional | 2-4 周 |
| P3 | 无序-拓扑相互作用相图 | 🟡 high | ★★★★★ | provisional | 1-2 月 |
| P4 | 石墨烯 Kane-Mele 模型 $\mathbb{Z}_2$ 计算 | 🟡 high | ★★★★ | provisional | 2-4 周 |
| P5 | 高通量 Chern 数材料筛选 pipeline | 🟢 medium | ★★★ | unspecified | 1-3 月 |

---

## P1: TBPM 框架下 Chern 数计算模块 ⭐ 推荐首发

### 项目卡片

| 维度 | 内容 |
|------|------|
| 核心想法 | 在现有 TBPM 能带计算框架中增加 Berry 曲率 + Chern 数计算——先算有序极限，再扩展到无序 |
| 对应 Gap | GAP-03 (TBPM + 拓扑) |
| 依赖论断 | CL-04 (Chern 数可靠计算, confirmed) |
| 最小成功定义 | 复现 Haldane 模型 Chern 数 $C=0, \pm 1, \pm 2$ 相图，与解析结果一致（$< 0.01$ 误差） |
| 第一步行 | 选 Haldane 模型（六角晶格，$t_2 e^{i\phi}$ 次近邻跃迁），实现 FHS 离散 Chern 数计算 |
| 输入 | $H(\mathbf{k})$ 紧束缚哈密顿量（k 空间网格） |
| 计算流程 | 1. 在 $N_k \times N_k$ 网格上对角化 $H(\mathbf{k})$ → 占据态波函数 $\vert u_{n\mathbf{k}}\rangle$；2. 对每个 plaquette 计算 $U_\mu(\mathbf{k}) = \langle u_{n\mathbf{k}} \vert u_{n\mathbf{k}+\hat{\mu}}\rangle / \vert \cdots \vert$；3. $F(\mathbf{k}) = \ln[U_x(\mathbf{k})U_y(\mathbf{k}+\hat{x})U_x^*(\mathbf{k}+\hat{y})U_y^*(\mathbf{k})]$；4. $C = \frac{1}{2\pi i} \sum_{\mathbf{k}} F(\mathbf{k})$ |
| 成功判据 | $C$ 整数化（$|C - \text{round}(C)| < 0.01$），相图匹配已知文献 |
| 失败定义 | $C$ 在小 k 网格下不收敛；FHS plaquette 相位跳跃 > $\pi$ 未正确处理 |
| 后选择 | 无（确定性计算） |
| Baseline | Haldane 模型解析相图 (Haldane 1988) |
| 结果边界 | 该方法仅对能隙系统有效（金属态 Chern 数不定义） |
| 升级路径 | → 无序下的 Kubo 电导 (P3)；→ 真实材料 Wannier 插值 (P5) |

### Operationalization Contract

- **operational_status**: `specified` ✅
- 任务定义清晰，输入/输出/指标/失败定义完整
- 可直接进入 MVP

---

## P2: 石墨烯基 QAHE 材料 TB 扫描 ⭐ 推荐

### 项目卡片

| 维度 | 内容 |
|------|------|
| 核心想法 | 在石墨烯紧束缚模型中加入 SOC + 交换场（模拟磁性邻近效应），扫描参数空间，寻找 QAHE 相 |
| 对应 Gap | GAP-05 (石墨烯拓扑异质结) |
| 依赖论断 | CL-03 (QAHE 可实现, confirmed), CL-06 (高温候选, suspected) |
| 最小成功定义 | 找到至少一个参数区域显示 $C=\pm 1$ 且有非零能隙，画相图 |
| 第一步行 | graphene.py + Kane-Mele SOC ($\lambda_{\text{SO}}$) + 交错子晶格势 + 交换场 ($M$)，画 $(\lambda_{\text{SO}}, M)$ 相图 |
| 关键参数 | $\lambda_{\text{SO}}$ — SOC 强度；$M$ — 交换场/自旋劈裂；$\lambda_v$ — 子晶格不对称（BN 衬底） |
| 扫描策略 | 粗扫 $(\lambda_{\text{SO}}, M)$ 平面 → 精扫相边界 → 确认 Chern 数跳变伴随能隙闭合 |
| 成功判据 | 发现丰富的 Chern 数相 ($C=0, \pm 1, \pm 2$)，相边界处能隙闭合 |
| 失败可能 | 石墨烯 SOC 过弱（~μeV）→ 实验中相区不可达；需要极强交换场 |
| 后选择 | 排除能隙 < $k_B T_{\text{exp}}$ 的相（区分"数学上存在"和"实验可观测"） |
| Baseline | Kane-Mele 相图 (Kane-Mele 2005), 石墨烯 QAHE 已有 DFT 文献（NEEDS_VERIFICATION: 具体 TB 扫描文献） |
| 结果边界 | TB 参数来自拟合 DFT——对真实材料的预测力取决于参数精度 |
| 升级路径 | → 真实材料 Wannier TB (P5)；→ 无序效应 (P3) |

### Operationalization Contract

- **operational_status**: `provisional` ⚠️
- 输入集合、扫描策略已明确
- 但交换场参数范围、SOC 参数来源需要进一步界定
- 建议先跑 P1（工具链），再跑 P2（应用）

---

## P3: 无序-拓扑相互作用相图

### 项目卡片

| 维度 | 内容 |
|------|------|
| 核心想法 | 在 Haldane 模型（已跑通 P1）中加入 Anderson 无序 + 紧束缚传播法计算 Kubo 霍尔电导 → 画无序 vs Chern 数的相图 |
| 对应 Gap | GAP-02 (无序-拓扑) |
| 依赖论断 | CL-04 (Chern 数计算, confirmed), CL-07 (无序影响不完全, suspected) |
| 最小成功定义 | 对一个拓扑模型，展示霍尔电导平台随无序强度增加而维持/破坏的阈值 |
| 第一步行 | Haldane 模型 + Anderson 无序 + Kubo-Bastin 或 Kubo-Greenwood 公式，计算 $\sigma_{xy}(E_F, W)$ |
| 关键问题 | 拓扑安德森绝缘体（无序诱导拓扑）是否存在？ |
| 成功判据 | 看到 $\sigma_{xy}$ 平台在弱无序下鲁棒，在强无序下坍塌；确认临界无序强度的标度行为 |
| 失败可能 | TBPM 的 Kubo 公式实现在大系统上收敛困难；有限尺寸效应模糊平台 |
| Baseline | 清洁极限下的量子化值 $e^2/h \times C$ |
| 结果边界 | 仅对 2D A 类拓扑绝缘体（无自旋）有效；对 QSHE 需处理自旋分辨 |
| 升级路径 | → 真实材料 + 真实无序类型（带电杂质 vs 中性缺陷 vs 磁性杂质） |

### Operationalization Contract

- **operational_status**: `provisional` ⚠️
- 输运计算的指标需要详细定义（Kubo 收敛判据、无序平均的构型数）
- 建议在 P1 完成后，先做收敛性测试再全量跑

---

## P4: 石墨烯 Kane-Mele 模型 $\mathbb{Z}_2$ 计算

### 项目卡片

| 维度 | 内容 |
|------|------|
| 核心想法 | 在 graphene.py 中实现 Kane-Mele SOC → 用 Wilson loop 方法计算 $\mathbb{Z}_2$ 不变量 |
| 对应 Gap | GAP-03 (TBPM + 拓扑) |
| 依赖论断 | CL-05 ($\mathbb{Z}_2$ 计算要求, confirmed) |
| 最小成功定义 | 正确区分 $\mathbb{Z}_2=0$（普通绝缘体）和 $\mathbb{Z}_2=1$（QSHE）相 |
| 关键风险 | Wilson loop 实现比 Chern 数复杂一个量级；时间反演对称性在数值上不易严格保持 |
| 第一步行 | Kane-Mele SOC + 保持时间反演对称的 k 网格 → Wilson loop 沿 $k_y$ 方向 → 看 Wannier 电荷中心演化是 winding (1) 还是 non-winding (0) |
| 建议 | 可先简化为自旋 Chern 数（当 $s_z$ 近似守恒时）做快速判断，再实现完整 $\mathbb{Z}_2$ |

### Operationalization Contract

- **operational_status**: `provisional` ⚠️
- 需要先确认时间反演对称 k 点配对的实现方式
- 建议先用小体系（2-band BHZ）测试，再扩展

---

## P5: 高通量 Chern 数材料筛选 pipeline

| 维度 | 内容 |
|------|------|
| 核心想法 | 结合 DFT + Wannier90 + 自动 Chern 数计算，在已知材料数据库中筛选高 Chern 数材料 |
| 对应 Gap | GAP-01 (高温 QAHE 材料) |
| 操作化状态 | **unspecified** — 需要先明确工作流（DFT 接口、自动化程度、筛选数据库来源） |
| 依赖 | 需要与 DFT 社区接轨，非纯 TB 路线 |
| 建议 | 作为中长期方向，先完成 P1-P4 积累 TB 层工具和直觉 |

---

## 推荐行动顺序

```
第 1 步（本周）:  P1 — Chern 数计算 → 验证工具链
第 2 步（2-3 周）: P2 — 石墨烯拓扑相图 → 出第一个有物理意义的图
第 3 步（3-6 周）: P3 — 无序相图 → 利用 TBPM 的独特优势
第 4 步（按需）:   P4 — $\mathbb{Z}_2$ → 扩展方法能力
第 5 步（中长期）: P5 — 高通量 → 需要额外学习 DFT 接口
```

## 使用说明

本文件把 `20_gap_table.md` 中值得继续验证的缺口，改写成研究者能读懂、能执行、能止损的候选项目。正文以中文为主，不写成英文表单。每个项目必须先有一段连续中文说明，再给必要的结构化栏目。

## 项目卡片

### 项目编号：

### 研究题目：

可以在括号中保留英文工作标题，但正文题目优先使用中文。

### 给用户看的项目解释

用连续中文说明：这个项目到底想做什么，为什么值得验证，为什么不是简单重复已有工作，第一张关键图可能长什么样。

### 这项研究想解决什么问题：

### 已有工作做到哪里：

### 仍然缺什么：

### 核心思路：

### 为什么现在值得做：

### 为什么不只是重复造轮子：

### 任务可操作化契约 / Operationalization Contract

#### 声称要验证的任务

#### 输入对象与允许输入集合

#### 编码、控制、演化、解码与读出流程

```text
输入
  -> 编码 / 制备
  -> 物理演化或算法执行
  -> 可允许的控制 / 恢复 / 校正
  -> 解码或读出
  -> 指标计算
  -> 结论
```

#### 目标变换

#### 指标定义

- 指标：
- 计算方式：
- 真正测到了什么：
- 没有测到什么：
- 依赖假设：

#### 泄漏、损失、失败事件与后选择处理

#### Baseline 公平性

#### 阳性结果能证明什么

#### 阳性结果不能证明什么

#### 阴性结果意味着什么

#### operational_status

unspecified / provisional / metric_checked / resource_checked

### 需要的用户已有条件：

如果使用兴趣型 profile，可以写“不适用，本模式不做用户资产匹配”。

### 需要的外部资源：

### 第一阶段：第一个可跑实验

**第一步可执行动作：**

**最小验证实验：**

**输入：**

**输出：**

**预期关键图：**

**对比基线：**

**评价指标：**

**成功标准：**

**止损标准：**

**风险：**

**可能形成的贡献：**

**优先级：**

---

## 候选项目排序

| 项目编号 | 研究题目 | 新颖性 | 可行性 | 证据质量 | 用户匹配 | operational_status | 第一项可执行动作 | 优先级 |
|---|---|---|---|---|---|---|---|---|
| P-001 |  | 1-5 | 1-5 | 1-5 | 1-5 / 不适用 | unspecified |  |  |

