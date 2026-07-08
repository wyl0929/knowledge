<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-11 20:08:13
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-11 20:08:13
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/15_tool_registry.md
 * @Description  :
-->
# 15 Tool Registry / 工具生态

Last updated: 2026-06-11

> 本领域常用计算工具及其与用户现有资产的对比。

---

## 1. 连续模型（Continuum Model）工具

| 工具 | 语言 | 功能 | 成熟度 | 与用户关系 |
|---|---|---|---|---|
| **Koshino 组 MATLAB/Python 代码** | MATLAB/Python | 多层转角石墨烯能带计算 | 研究级 | ⭐⭐⭐⭐⭐ 可改写为 Python |
| **TBG continuum (个人开发)** | Python | BM 模型的最小实现 | 入门级 | ⭐⭐⭐⭐⭐ 用户可直接自研 |
| **Kwant** | Python | 通用紧束缚 + 输运 | 成熟 | ⭐⭐⭐⭐ 可嵌入转角几何 |

## 2. 紧束缚（Tight-Binding）工具

| 工具 | 语言 | 功能 | 成熟度 | 与用户关系 |
|---|---|---|---|---|
| **用户 TMBG 项目** | Python/MPI | 完整 TMBG/TBG 紧束缚电子结构计算 | ✅ 生产就绪 | ⭐⭐⭐⭐⭐ 核心资产 |
| **tbplas** | Python/C++ | 紧束缚核心库 (PrimitiveCell, TBPM, Haydock) | 成熟 | ⭐⭐⭐⭐⭐ TMBG 项目的底层依赖 |
| Pybinding | Python | TB 模型构建 + 对角化 + 输运 | 成熟 | ⭐⭐⭐ 用户已有 TBPM 替代 |
| Wannier90 | Fortran/Python | MLWF 构造 | 成熟 | ⭐⭐⭐ |
| 用户 TBPM 代码 | Python/MPI | 紧束缚传播法 DOS/输运 | usable | ⭐⭐⭐⭐⭐ 已整合入 TMBG 项目 |
| 用户 graphene.py | Python | 石墨烯 TB 模型 | usable | ⭐⭐⭐⭐⭐ 已整合入 TMBG 项目 |

## 3. DFT 与原子弛豫

| 工具 | 功能 | 成熟度 | 与用户关系 |
|---|---|---|---|
| **VASP** | 第一性原理 DFT | 工业级 | ⭐⭐ 需要 license + 集群 |
| **Quantum Espresso** | 开源 DFT | 成熟 | ⭐⭐ 需要学习 |
| **LAMMPS** | 分子动力学（力场弛豫）| 成熟 | ⭐⭐⭐ 可用于弛豫后 TB |
| **SIESTA** | 开源 DFT + TB | 成熟 | ⭐⭐⭐ |

## 4. 强关联求解器

| 工具 | 方法 | 成熟度 | 与用户关系 |
|---|---|---|---|
| **TRIQS** | DMFT/CT-QMC | 成熟 | ⭐ 强关联背景门槛高 |
| **ALPS** | QMC/DMRG | 成熟 | ⭐ 同上 |
| **iTensor** | DMRG/张量网络 | 成熟 | ⭐ 低维有效 |
| **TeNPy** | 张量网络 | 成熟 | ⭐ |

## 5. 用户改造路径预估

| 从 | 改造为 | 工作量估算 | 风险 |
|---|---|---|---|
| graphene.py | 转角双层 TB 模型 | 1–2 天（加层间耦合 + 超胞构建）| 低 |
| 转角双层 TB | TMBG/TDBG/螺旋三层 | 再 1–3 天（加层和转角）| 低 |
| TBPM | 转角石墨烯 DOS 计算 | 0.5 天（只需传新 Hamiltonian）| 低 |
| TBPM | 转角石墨烯输运（$\sigma_{xx}$, $\sigma_{xy}$）| 2–5 天（需要 Kubo 公式扩展）| 中 |
| 连续模型代码 | Hofstadter 谱（磁场） | 1–3 天 | 中 |
| 以上 | 关联修正的 TB（如 HF 平均场） | 1–2 周 | 中高 |

---

## 6. 实验数据资源

- **公开数据库**：暂无专门的转角石墨烯数据仓库
- **可以从论文中提取的数据**：输运相图、STS 谱、量子振荡频率
- **模拟数据对比标准**：TBG/Bilayer 的标准能带（BM 模型可作为验证基准）
