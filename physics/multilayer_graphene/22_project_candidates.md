<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-11 20:10:23
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-11 20:10:24
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/22_project_candidates.md
 * @Description  :
-->
# 22 Project Candidates / 候选项目卡片

Last updated: 2026-06-11

> 基于 gap table 和 asset match 生成的候选研究项目。
> quick_scan 模式下不强制包含完整 Operationalization Contract，但标注操作化关键要素。

---

## 项目 P1：连续模型 vs 紧束缚的定量桥接 —— 转角石墨烯计算方法基准

### 基本信息

| 字段 | 内容 |
|---|---|
| 对应缺口 | G-M03, G-M04 |
| 类型 | 方法基准（methods benchmark） |
| 难度 | ⭐⭐ |
| 预计周期 | 1–2 周 |
| 产出形式 | 内部技术报告 + 可能的方法短文 |

### 动机

文献中连续模型和紧束缚模型各自独立使用，但缺少系统性的定量比较：TB 超胞多大才能收敛到连续模型的结果？TBPM 在大超胞下的精度如何？回答这个不仅能建立用户在该领域的可信度，也是所有后续计算的基础。

### 核心任务

1. 实现 BM 连续模型（Python，TBG/TDBG）
2. 改造 graphene.py 生成转角 TB 超胞
3. 对比不同超胞大小（10³–10⁵ atoms）下的能带收敛
4. TBPM DOS 与精确对角化 DOS 对比

### Baseline

- BM 模型给出的魔角平带带宽（~10 meV at θ=1.1° for TBG）
- Trambly de Laissardière (2010) 的 TB 能带结果
- Koshino (2019) 的 TDBG 能带

### Metrics

- 平带带宽 $W$ 在 BM vs TB 下的差异
- DOS 峰位置和宽度
- 超胞大小收敛性（$W$ vs $N_{atoms}$）

### Risks

| 风险 | 概率 | 缓解 |
|---|---|---|
| 层间耦合参数不准确导致 TB 与 BM 不一致 | 中 | 使用多组文献参数做 sensitivity analysis |
| 超胞边界条件导致伪能隙 | 低 | 比较不同边界条件 |

### Success Criteria

- TB 能带在超胞 > 10⁴ atoms 时收敛到 BM 结果（带宽差异 < 20%）
- TBPM DOS 与精确对角化 DOS 在可达体系上一致

### Stop Criteria

- 如果 BM 和 TB 在合理参数范围内存在不可调和的定性差异 → 记录为 finding，不继续微调参数

---

## 项目 P2：转角不均匀对多层体系平带的定量影响

### 基本信息

| 字段 | 内容 |
|---|---|
| 对应缺口 | G-T02 |
| 类型 | 物理研究（physics study） |
| 难度 | ⭐⭐⭐ |
| 预计周期 | 2–4 周 |
| 产出形式 | 可投稿的研究文章 |

### 动机

转角不均匀（twist angle disorder）被认为是限制样品质量的主要因素，但其定量影响——尤其在三层/多层体系中——缺乏系统模拟研究。TBPM 的大超胞能力天然适合这个课题：可以在超胞内引入空间分布的转角涨落，直接计算无序对 DOS、平带带宽和输运的影响。

### 核心任务

1. 在 TB 超胞中实现空间缓变的转角分布（$\theta(\mathbf{r})$）
2. 计算无序强度 $\delta\theta$ 对平带带宽和 DOS 的定量影响
3. 比较 TBG vs TDBG vs TMBG：多层中转角不均匀是累加还是平均？
4. （进阶）计算输运性质（$\sigma_{xx}$）随无序的演化

### Baseline

- 零无序极限的干净能带（来自 P1）
- 实验上 STM 测量的转角空间分布（文献值 $\delta\theta \sim 0.05^\circ$–$0.2^\circ$）
- Wilson et al. (2020) NEEDS_VERIFICATION 的 TBG 无序输运理论

### Metrics

- 平带带宽 $W(\delta\theta)$
- DOS 在费米能处的展宽
- （可选）输运散射率 $\Gamma$

### Operationalization（轻量版）

| 要素 | 内容 |
|---|---|
| 输入集合 | $\{\theta_0, \delta\theta, \text{构型}, \text{超胞大小}, \text{层间耦合参数}\}$ |
| 目标变换 | 干净能带 → 无序能带/DOS |
| 编码/读出 | 实空间 TB Hamiltonian → 对角化能带 / TBPM → DOS |
| 指标成立条件 | 超胞足够大使得 $\delta\theta$ 在超胞内有统计意义 |
| 失败事件 | 无序展宽超过平带带宽本身（此时平带被完全抹平） |
| Baseline 公平性 | 干净极限用相同的超胞大小和 TB 参数计算 |

### Risks

| 风险 | 概率 | 缓解 |
|---|---|---|
| 无序模型过于简化（高斯分布 vs 真实空间关联） | 中 | 对比多种无序模型 |
| 大超胞 + 无序 → 需要统计平均，计算量大 | 高 | MPI 并行 + 合理采样 |

### Success Criteria

- 定量给出 $W(\delta\theta)$ 的标度关系
- 明确多层体系中转角无序是增强还是抑制
- 结果与已有 TBG 实验估计在量级上一致

### Stop Criteria

- 如果在实验合理的 $\delta\theta$ 范围内平带完全被抹平 → 记录，作为"转角质量需求的定量判据"

---

## 项目 P3：多层转角石墨烯平带的拓扑分类

### 基本信息

| 字段 | 内容 |
|---|---|
| 对应缺口 | G-T03 |
| 类型 | 物理研究 |
| 难度 | ⭐⭐⭐ |
| 预计周期 | 2–4 周 |
| 产出形式 | 可投稿的研究文章 |

### 动机

TBG 的平带携带非零 Chern 数（在磁场或特定条件下）。多层体系中平带数目更多，Chern 数序列的规律尚未被系统分类。这个课题结合 TB 能带计算 + Berry curvature 积分，在用户现有代码基础上加一个模块即可完成。

### 核心任务

1. 实现 TB 基下的 Berry curvature 和 Chern 数计算
2. 对 TDBG 计算 $(θ, D)$ 空间的 Chern 数相图
3. 对 TMBG 计算 Chern 数相图
4. 比较不同构型的拓扑相图规律

### Baseline

- TDBG 的已知拓扑相变（Liu et al. 2020, Nature）
- TBG 的 Hofstadter 谱和 Chern 数

### Metrics

- Chern 数序列 $C = (C_1, C_2, ...)$
- 拓扑相边界在 $(θ, D)$ 空间的形状
- 平带的总 Chern 数 $C_{FB}$

### Risks

| 风险 | 概率 | 缓解 |
|---|---|---|
| Berry curvature 在动量空间需要很密的 k 网格 | 中 | 自适应网格或 Wannier 插值 |
| TB 超胞的 k 空间定义不如连续模型直观 | 中 | 与连续模型结果交叉验证 |

### Success Criteria

- 正确复现 TDBG 的已知 Chern 数相变（→ 验证方法）
- 发现新的拓扑相变线或提出 Chern 数序列的规律

---

## 项目 P4：构建转角石墨烯紧束缚计算基准数据集

### 基本信息

| 字段 | 内容 |
|---|---|
| 对应缺口 | G-M02 |
| 类型 | 社区服务 / 数据集 |
| 难度 | ⭐ |
| 预计周期 | 1 周 |
| 产出形式 | 公开数据集 + 短报告 |

### 动机

领域缺少公开的基准数据集。用户在 P1-P3 中产生的结果天然构成一个基准数据集。整理和公开这些数据有助于建立 visibility。

### 核心任务

1. 标准化数据格式（能带、DOS、Chern 数 vs θ, D, 构型）
2. 整理 P1-P3 的输出
3. 写短报告或 data descriptor

---

## 5. 快速对照

| 项目 | 难度 | 周期 | 产出类型 | TBPM 优势 | 推荐优先级 |
|---|---|---|---|---|---|
| P1 方法基准 | ⭐⭐ | 1–2 周 | 技术报告 | 中 | **最高（所有后续的基础）** |
| P2 转角无序 | ⭐⭐⭐ | 2–4 周 | 研究文章 | **极高** | 高 |
| P3 拓扑分类 | ⭐⭐⭐ | 2–4 周 | 研究文章 | 中 | 高 |
| P4 基准数据 | ⭐ | 1 周 | 数据集 | 低 | 中（依赖 P1-P3） |
