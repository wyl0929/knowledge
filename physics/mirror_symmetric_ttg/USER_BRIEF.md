<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-09-03
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-09-03
 * @FilePath     : /project/knowledge/physics/mirror_symmetric_ttg/USER_BRIEF.md
 * @Description  : mirror-symmetric twisted trilayer graphene 调研需求
-->
# USER_BRIEF / Mirror-symmetric Twisted Trilayer Graphene 调研需求

Last updated: 2026-09-03

## 调研领域

**Mirror-symmetric twisted trilayer graphene（镜面对称转角三层石墨烯）**

几何构型：三层单层石墨烯，上下两层彼此对齐（取向相同），仅中间一层相对它们扭转一个魔角 θ。
三层转角序列 (bottom, middle, top) = (0°, θ, 0°)，相邻两层间的相对转角为 +θ 与 −θ（交替扭转）。

英文/同义名称（同一构型，文献中混用）：

- mirror-symmetric twisted trilayer graphene (mirror-symmetric TTG) —— 最常用的描述性名称
- twisted symmetric trilayer graphene (TSG) —— Călugăru 等的理论工作用名
- alternating-twist trilayer graphene (ATTLG / ATMG) —— 超导实验论文用名
- magic-angle twisted trilayer graphene（广义伞形名，也含螺旋 TTG，需按堆垛区分）

## 与已有体系的关键区别

| 体系 | 层数/界面 | 堆垛 | 说明 |
|------|-----------|------|------|
| **本体系 (mirror-symmetric TTG)** | 3 单层 / 2 界面 | 上下对齐，中间层转 θ | 镜面对称，flat band + Dirac cone 共存 |
| TMBG (twisted monolayer-bilayer) | 1 单层 + 1 AB 双层 / 1 界面 | 底 AB 双层 + 顶单层扭转 | **不同构型**，勿混淆（旧 `ttg_*.py` 实为 TMBG） |
| 螺旋 TTG (helical TTG) | 3 单层 / 2 界面 | 相邻界面同号扭转 | 对照体系，仅在对比时提及 |

## 调研模式

full_onboarding（完整入场），参照 `../twisted_bilayer_graphene/Phase_S/` 的文献调研流程执行。

## 核心物理问题（导师假说，需在调研中检验）

> 导师推测：该体系 **flat band + Dirac cone 共存的能带结构**导致的高可调性，与其超导相关。

调研需回答三个问题（对应项目三步中的第 1 步「前期考察」）：

1. **实验**：实验上观察到了什么现象？（超导、关联态、flat band/Dirac cone 的谱学表征、电场/位移场可调性）
2. **理论**：理论上做了哪些解释？（能带结构来源、平带+Dirac 锥共存机制、可调性来源、超导配对机制）
3. **连接**：flat band + Dirac cone 高可调性 → 超导 这条因果链在文献中有多强/多弱的证据支撑？

## 项目三步走（本 pack 只覆盖第 1 步）

1. **前期考察**（本 pack）：文献调研 → 实验现象 + 理论解释 + 假说检验
2. tbplas 电学性质计算：DOS、band 等（**计算侧暂时搁置，等文献调研结束后启动**，届时新建 compute 项目）
3. 若性质/理论有趣：推进超导相关计算（后续决策）

## 写作偏好

- 主体中文，关键术语附英文
- 先直觉后公式
- 明确区分 confirmed fact / suspected / speculation / NEEDS_VERIFICATION
- 证据分级与 QC 规范继承 `../twisted_bilayer_graphene/Phase_S/plan.md` §2.6（三层防线）

## 用户背景结合

是。用户为计算凝聚态物理研究者，已有：

- tbplas 紧束缚 + TBPM 计算代码（`graphene.py`、TBG/TMBG 的 `src/` 五模块结构可复用）
- LAMMPS 原子弛豫、MPI 并行、远程 SLURM 集群算力
- 无 DFT/DMFT 经验，无实验合作

## 是否寻找研究选题

是（full_onboarding 含 gap table、候选项目卡片、MVP 实验计划）
