<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-21 05:04:51
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-21 05:04:52
 * @FilePath     : /.agents/home/wyl/project/knowledge/systems_science/10_self_inventory.md
 * @Description  :
-->
<!--
Field: 系统科学与控制论
Mode: full_onboarding
Domain archetype: science_technical
Created date: 2026-06-21
-->

# 10 Self Inventory / 用户背景与资产快照

Last updated: 2026-06-21

## 使用的 Profile

`profiles/default_user_profile.md`（计算凝聚态物理研究者），结合用户本次输入的系统科学兴趣。

## 基本身份与研究背景

- 身份：计算凝聚态物理研究者（Yulong Wang）
- 学科背景：物理学、计算物理、数值模拟
- 当前阶段：研究生/博士后（进行中）
- 主要训练：凝聚态理论、量子输运数值模拟（TBPM、紧束缚模型）

## 系统科学相关背景

- **数学基础**：扎实 —— 线性代数、微分方程、概率论、数值方法、傅里叶分析
- **编程能力**：强 —— Python、C/C++、MPI 并行、SLURM 集群
- **物理建模经验**：已有 —— 紧束缚哈密顿量构建、能带计算、输运模拟
- **控制/优化**：NEEDS_VERIFICATION —— 可能接触过自洽场迭代的收敛控制
- **信息论**：NEEDS_VERIFICATION —— 可能从统计力学中接触过熵的概念

## 已有代码和工具

| 工具 / 代码 | 类型 | 位置 | 成熟度 | 备注 |
|---|---|---|---|---|
| graphene.py | code | test/graphene.py | usable | 石墨烯紧束缚计算 |
| test_mpi.py | code | test/test_mpi.py | usable | MPI 并行测试 |
| TBPM/DOS 计算 | code | 工作区 | usable | 紧束缚传播法态密度计算 |
| submit.py | tool | ~/.agents/skills/cluster-workflow/assets/ | mature | SLURM 一键提交 |
| SLURM 脚本 | tool | slurm/ | mature | 集群作业模板 |

## 可调用资源

- 算力：远程 SLURM 集群（h3clogin），Intel oneAPI + MKL，多节点 MPI
- 数据：自产紧束缚计算数据
- 方法能力：紧束缚模型、能带理论、量子输运、MPI 并行、TBPM（熟练）
- 软件工程：Python、Shell、Git、SLURM（熟练）
- 写作与可视化：matplotlib、LaTeX（熟练）

## 与系统科学的可迁移能力（核心连接点）

### 1. 动力学系统 ↔ 量子动力学

物理学中的薛定谔方程 $i\hbar \partial_t|\psi\rangle = H|\psi\rangle$ 本质上是一个（无穷维）线性动力系统。你在 TBPM 中已经做的事情——对初始态作用 $e^{-iH\Delta t}$ 做时间演化——与控制论中的**状态转移矩阵** $\Phi(t) = e^{At}$ 是同构的数学结构。

### 2. 自洽场迭代 ↔ 反馈控制

DFT/Hartree-Fock 中的自洽场（SCF）循环：输入电荷密度 → 解 Kohn-Sham 方程 → 输出新电荷密度 → 混合迭代。这正是**闭环反馈系统**。混合参数（如 Pulay mixing、Broyden mixing）就是**控制器增益**。SCF 收敛失败就是控制系统失稳。

### 3. 变分法 ↔ 最优控制

物理中的最小作用量原理 $\delta S = 0$ 与控制论中的庞特里亚金极大值原理有共同的变分根源。你算基态用的是 $\min_{\psi} \langle\psi|H|\psi\rangle$，最优控制解的是 $\min_u \int L(x,u)dt$——数学形式上几乎一样。

### 4. 统计力学 ↔ 信息论

玻尔兹曼熵 $S = k_B \ln \Omega$ 和香农熵 $H = -\sum p_i \log p_i$ 只差一个常数因子。自由能 $F = U - TS$ 中的 $-TS$ 项对应信息论中的编码代价。Jaynes 的最大熵原理直接连通两个领域。

### 5. 格林函数 ↔ 传递函数

物理中 $G(E) = (E - H)^{-1}$ 给出系统对点扰动的响应；控制论中传递函数 $G(s) = C(sI - A)^{-1}B$ 给出系统对输入的响应——完全相同的数学结构，只是变量名从 $E$ 换成了 $s$。

### 6. 谱分析 ↔ 模态分析

你对角化哈密顿量得到本征值和本征态；控制论中对角化 $A$ 矩阵得到系统的固有模态和特征频率。矩阵的谱决定动力学行为——两边的直觉完全互通。

## 需要补充的知识

- 控制系统的基本术语（传递函数、根轨迹、Bode 图、Nyquist 判据）
- 非线性动力学（分岔、混沌、极限环）—— 如果有耗散系统经验会有帮助
- 最优化的数值方法（梯度下降、牛顿法、Lagrange 乘子）—— 物理中已有接触
- 系统辨识 —— 这是纯新内容

## 未确认事项（NEEDS_VERIFICATION）

- 是否系统学习过控制理论：NEEDS_VERIFICATION（假设未系统学习）
- 是否有非线性和混沌动力学背景：NEEDS_VERIFICATION
- 是否接触过信号处理：NEEDS_VERIFICATION
- 学习时间预算：NEEDS_VERIFICATION（假设弹性时间）
- 具体应用场景：NEEDS_VERIFICATION（用户未说明是否要将系统科学用于某个具体物理问题）
