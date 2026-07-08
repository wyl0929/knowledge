<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-22 16:49:42
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-22 16:49:44
 * @FilePath     : /.agents/home/wyl/project/knowledge/computer_science/cpp_for_tbplas/10_self_inventory.md
 * @Description  :
-->
# 10 Self Inventory / 用户背景快照

Last updated: 2026-06-22

## 使用说明

本文件是当前 field pack 使用的 profile 快照。它记录"这次生成时默认假设用户是谁、有没有研究资产、是否需要资产匹配"。

Field / 领域：C++ 编程（面向 tbplas 源码阅读与修改）

Depth mode / 深度模式：project_incubation

## Profile source / 背景来源

`profiles/default_user_profile.md`（2026-06-10 快照），结合用户本次声明"已有 C 和 Python 的基础"。

## Snapshot date / 快照日期

2026-06-22

## 用户研究背景

- 身份与学科背景：计算凝聚态物理研究者（研究生/博士后阶段）
- 主要研究方向：石墨烯及相关二维材料的电子性质计算、TBPM 大规模量子输运模拟
- 已有领域知识：紧束缚模型、能带理论、量子霍尔效应、Kubo-Bastin 电导率计算
- 数学、理论、实验或写作基础：量子力学、数值线性代数（中等）、MPI 并行（熟练）

## 编程能力现状

| 语言 | 水平 | 具体能力 | 差距 |
|------|:---:|------|------|
| **C** | 熟练 | 指针、struct、动态内存、文件 I/O、基本的 CMake | 无 class、模板、STL、RAII 概念 |
| **Python** | 熟练 | numpy/scipy、matplotlib、Cython 调用、SLURM 脚本 | 不熟悉 C++ 的 Python 绑定编写 |
| **C++** | 入门 | 可能能读简单 `.cpp` 文件 | **核心差距见下表** |
| **Shell** | 熟练 | bash 脚本、集群作业管理 | — |
| **Git** | 熟练 | 版本控制 | — |

## C++ 核心知识差距（相对于 tbplas 需求）

| C++ 概念 | C 用户的理解负担 | Python 用户的类比 | tbplas 中的典型位置 |
|------|:---:|------|------|
| **class / struct 带方法** | 高——C 的 struct 只有数据 | Python class 但编译期确定 | `base/lattice.h` |
| **public/private/protected** | 新概念 | Python `_` 约定但编译器强制执行 | 各处 |
| **继承与虚函数** | 新概念 | Python 继承但无 virtual 机制 | `tbpm/backend.h` → `tbpm/tbpm.h` |
| **模板 (template)** | 新概念 | Python duck typing 但编译期 | `tbpm/solver.h:52` |
| **STL (vector, complex, ...)** | 部分熟悉——C 数组 | Python list 但类型固定 | `base/datatypes.h` |
| **引用 (&) vs 指针 (*)** | 新概念——C 只有指针 | Python 一切皆引用但语法不同 | 各处函数参数 |
| **const 正确性** | C 有 const 但用法更简单 | 无直接类比 | `base/lattice.h:30` |
| **RAII / 析构函数** | 新概念——C 手动 free | Python `with` / `__del__` | `base/utils.h:18` (Timer) |
| **移动语义 (&&)** | 新概念 | 无直接类比 | `builder/sample.h:49-56` |
| **运算符重载** | 新概念 | Python `__add__` 等 | `builder/sample.h:58-82` |
| **namespace** | 新概念——C 用前缀 | Python module | `tbplas::base` 等 |
| **智能指针** | 新概念——C 手动管理 | Python 自动 GC | `builder/sample.h:38` |
| **Eigen 库** | 新概念 | numpy | 几乎所有 `.h` |
| **Cython (.pyx)** | 新概念 | 知道调用但不知编写 | `python/builder/sample.pyx` |

## 用户已有工具或材料

| 工具 / 材料 | 类型 | 位置 | 成熟度 | 相关性 | 备注 |
|---|---|---|---|---|---|
| tbplas C++ 源码 | code | `~/tbplas/source/tbplas-cpp-a021ca8/sources/` | mature | **高** — 学习目标本身 | 约 20+ 文件，CMake 构建 |
| tbplas Python 绑定 | code | `~/tbplas/.../python/` | usable | 高 — 理解 C++/Python 桥接 | Cython .pyx 文件 |
| MG 项目工作区 | code+data | `~/project/MG/` | usable | 高 — 学习动机来源 | Kubo-Bastin Hall 电导率计算 |
| tbplas-internals.md | doc | `~/project/shared/` | mature | 高 — 已有内部文档 | 数值不稳定性分析 |
| 02_kubo_bastin_deep_dive.md | doc | `~/project/knowledge/.../tbplas_conductivity/` | mature | 高 — 核心算法文档 | 含源码行号索引 |
| SLURM 集群 | hardware | h3clogin | mature | 中 — 编译和测试环境 | Intel oneAPI + MKL |
| submit.py | tool | `~/.agents/skills/cluster-workflow/assets/` | mature | 低 — 与 C++ 学习无直接关系 | 集群作业提交 |

## 本次调用中的特殊覆盖项

| 覆盖项 | 来源 | 对 field pack 的影响 | Last updated |
|---|---|---|---|
| 学习目标明确为 tbplas 源码 | user input | 所有 C++ 教学材料必须关联 tbplas 真实代码 | 2026-06-22 |
| 走 project_incubation 路线 | user input | 产出以 MVP 实验计划为核心，非完整入门教程 | 2026-06-22 |

## Claims to Verify / 待核验判断

| 判断 | 为什么重要 | 需要来源 | 状态 |
|---|---|---|---|
| 用户能独立编译 tbplas C++ 代码 | 若无法编译则无法验证修改 | 实际操作测试 | NEEDS_VERIFICATION |
| 用户的 C 基础足以快速理解 C++ 的 class/STL | 决定 Level 1 学习速度 | 实际操作测试 | NEEDS_VERIFICATION |
