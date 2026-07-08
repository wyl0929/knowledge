<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-22 16:50:18
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-22 16:50:19
 * @FilePath     : /.agents/home/wyl/project/knowledge/computer_science/cpp_for_tbplas/11_term_disambiguation.md
 * @Description  :
-->
---
document_type: term_disambiguation
schema_version: v1.0
field: "C++ 编程（面向 tbplas 源码）"
last_updated: 2026-06-22
---

# 11 关键概念与边界说明

Last updated: 2026-06-22

## 概念边界契约 / Concept Boundary Contract

### 用户原始术语

用户说"学习 C++ 代码"——这里的"C++ 代码"是个大口袋，可能指：
1. C++ 语言本身（语法、语义、标准库）
2. C++ 生态（CMake、包管理、编译工具链）
3. C++ 在 tbplas 中的特定用法（Eigen、Cython 绑定、数值模板）

### 规范工作范围

本 field pack 实际讨论的对象按优先级分三层：

| 层级 | 范围 | 判断标准 |
|:---:|------|------|
| **L1 — 必学** | C++ 中与 C/Python 有本质差异、且在 tbplas 中出现 ≥3 次的特性 | 看不懂这些就看不懂 tbplas 核心逻辑 |
| **L2 — 应学** | tbplas 中出现 1–2 次、理解后可大幅提升代码阅读效率的特性 | 学了能加速理解，但不阻塞主线 |
| **L3 — 缓学** | C++ 通用但 tbplas 中未出现的特性 | 暂时不学，遇到再说 |

### 上位概念、下位概念与相邻概念

- **上位概念**：编程语言 → 系统编程语言 → C++（与 C、Rust 同属"编译型系统语言"）
- **下位概念**：C++11/14/17 标准、C++ 标准库（STL）、Eigen 库、Cython 桥接层
- **相邻但不同的概念**：
  - C —— C++ 的"父语言"，但写 C++ 不是写 C with classes
  - Python —— 同为高级语言但运行模型完全不同（解释型 vs 编译型、动态类型 vs 静态类型）
  - Fortran —— tbplas 依赖的 MKL/BLAS 的底层语言，不需要学

### 常见过度等同

| 危险等同 | 为什么错 | 正确理解 |
|------|------|------|
| "C++ 就是 C 加 class" | C++ 的模板、RAII、移动语义、STL 与 C 有本质断裂 | C++ 是一门独立语言，C 兼容只是历史遗留 |
| "C++ 的 `vector` 就是 Python 的 `list`" | `vector<T>` 是连续内存、编译期类型固定、无混合类型 | 更像 numpy 的 `ndarray` 但只有一维 |
| "C++ 的 `class` 就是 Python 的 `class`" | C++ class 有编译期确定的 memory layout、无运行时 monkey-patching | 更像 C 的 struct + 函数指针表，但编译器帮你管理 |
| "C++ reference 就是 C pointer" | 引用不能为 null、不能重绑定、语法更干净 | 引用是"别名"，指针是"地址" |
| "`template` 就是 Python 的 duck typing" | 模板在编译期生成代码（零运行时开销），duck typing 在运行时 | 模板更像"编译器帮你写的代码生成脚本" |

### 本包允许使用的表达

| 表达 | 语境 | 首次出现时的中文说明 |
|------|------|------|
| class / struct | 讨论 C++ 类型系统 | 类（class）/ 结构体（struct）—— 带数据和方法的自定义类型 |
| template | 讨论泛型编程 | 模板（template）—— 编译期类型参数化 |
| STL | 讨论标准库 | 标准模板库（STL）—— C++ 自带的数据结构和算法 |
| RAII | 讨论资源管理 | 资源获取即初始化（RAII）—— 用对象生命周期自动管理资源 |
| `shared_ptr<T>` | 讨论内存管理 | 共享指针——引用计数自动释放的智能指针 |
| Eigen | 讨论线性代数 | Eigen 库——C++ 的 numpy，tbplas 的核心数学引擎 |
| Cython | 讨论 Python 绑定 | Cython——把 C++ 类包装成 Python 可调用的 `.so` 模块的工具 |
| move semantics | 讨论性能优化 | 移动语义——把数据的所有权从一个对象"转移"到另一个，避免深拷贝 |

### 本包禁止直接推出的结论

- ❌ "懂了 C++ 语法就能改 tbplas"——还需要理解 Eigen 的惰性求值、Cython 的 GIL 问题、CMake 的链接逻辑
- ❌ "Python 熟练所以 C++ 好学"——编译-链接-运行循环、头文件/实现文件分离、模板编译错误信息是全新的心智负担
- ❌ "C 指针熟练所以 C++ 内存管理没问题"——C++ 的 RAII + 智能指针是全新的资源管理范式，C 的手动 malloc/free 在 C++ 中反而是反模式

### 对下游研究判断的影响

- **field map**：按 C++ 概念依赖关系（非字母序）组织，先 RAII 后 move，先 STL 后 template
- **frontier compass**：内圈=L1 必学概念；边界=L2 概念 + 能独立修改 `kubo_bastin.h` 中的递推循环
- **gap table**：每个 gap 对应一个具体的 tbplas 文件阅读障碍
- **project title**："以 tbplas 源码为教材的 C++ 速通路径"
- **MVP success criteria**："能独立为 tbplas 添加一个命令行参数并验证其效果"

### 核验状态

concept_status: working_definition

证据来源：
- tbplas 源码扫描（Explore subagent, 2026-06-22）
- `/home/wyl/project/shared/tbplas-internals.md`
- `/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/02_kubo_bastin_deep_dive.md`
- default_user_profile.md (2026-06-10)

待核验事项：
- NEEDS_VERIFICATION：用户对 C++ 编译-链接模型的实际熟悉程度
- NEEDS_VERIFICATION：用户是否能独立编译 tbplas（`cmake .. && make`）

## 0. 阅读说明

本文件比 `00_beginner_guide.md` 更严谨，但仍然先解释概念，再比较边界。它不是简单术语表，也不是翻译表；它要帮助学习者理解：一个 C++ 概念到底指什么，不指什么，和 C/Python 中的对应概念为什么容易混淆，以及这些区别会怎样影响阅读 tbplas 源码的效率。

正文以中文为主。重要英文术语第一次出现时，先给中文解释，再在括号中保留英文术语；后续优先使用中文或通行缩写。
