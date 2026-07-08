<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-19 23:27:17
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-19 23:27:17
 * @FilePath     : /.agents/home/wyl/project/knowledge/Economics/macroeconomics/10_self_inventory.md
 * @Description  :
-->
# 10 Self Inventory / 用户背景与资产快照

Last updated: 2026-06-19

## 使用的 Profile

`profiles/default_user_profile.md`（计算凝聚态物理研究者），结合用户本次输入的微观经济学基础。

## 基本身份与研究背景

- 身份：计算凝聚态物理研究者
- 学科背景：物理学、计算物理、数值模拟
- 当前阶段：研究生/博士后（进行中）
- 主要训练：凝聚态理论、量子输运数值模拟（TBPM、紧束缚模型）

## 经济学相关背景

- 微观经济学基础：已掌握供需理论、市场均衡、消费者理论、生产者理论、福利经济学基本概念
- 宏观经济学：本次入门目标
- 数学基础：扎实（线性代数、微积分、微分方程、概率论、数值方法）
- 编程与模拟能力：强（Python、C/C++、MPI 并行、SLURM 集群）
- 数据分析和可视化能力：强

## 已有代码和工具

| 工具 / 代码 | 类型 | 位置 | 成熟度 | 备注 |
|---|---|---|---|---|
| graphene.py | code | test/graphene.py | usable | 石墨烯紧束缚计算 |
| test_mpi.py | code | test/test_mpi.py | usable | MPI 并行测试 |
| TBPM/DOS 计算 | code | 工作区 | usable | 紧束缚传播法态密度计算 |
| submit.py | tool | ~/.agents/skills/cluster-workflow/assets/ | mature | SLURM 一键提交 |
| SLURM 脚本 | tool | slurm/ | mature | 集群作业模板 |

## 可调用课题组资源

- 算力：远程 SLURM 集群（h3clogin），Intel oneAPI + MKL
- 硬件：多节点 MPI 并行
- 数据：自产紧束缚计算数据
- 内部代码：TBPM、DOS 计算代码

## 本次覆盖项（用户输入优先于 profile）

| 项目 | Profile 默认 | 本次实际 | 原因 |
|---|---|---|---|
| 经济学背景 | 无 | 已有微观经济学基础 | 用户输入 |
| 本次目标 | 无 | 入门宏观经济学 | 用户输入 |

## 与宏观经济学的可迁移能力

- **数学建模思维**：物理学中的场论、微分方程、统计力学与宏观经济学中的动态系统、随机过程有形式上的共通之处
- **数值模拟经验**：DSGE 模型的数值求解（扰动法、投影法、值函数迭代）与物理学中的 PDE 求解、对角化有相似的计算逻辑
- **数据处理**：宏观经济时间序列分析与物理实验数据的频谱分析共享相同的数学工具（傅里叶变换、滤波、协整）
- **需要补充的知识**：经济学的制度背景、经济数据的生成机制（GDP 如何核算、通胀如何测量）、宏观经济学特有的识别问题（如 Lucas 批判）

## 未确认事项（NEEDS_VERIFICATION）

- 是否有经济学领域的合作者或导师：NEEDS_VERIFICATION
- 是否有特定的宏观经济数据访问权限：NEEDS_VERIFICATION
- 学习时间预算：NEEDS_VERIFICATION（假设为弹性时间）
