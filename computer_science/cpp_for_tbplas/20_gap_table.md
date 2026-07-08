<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-22 16:51:43
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-22 16:51:45
 * @FilePath     : /.agents/home/wyl/project/knowledge/computer_science/cpp_for_tbplas/20_gap_table.md
 * @Description  :
-->
---
document_type: gap_table
schema_version: v1.0
field: "C++ 编程（面向 tbplas 源码）"
last_updated: 2026-06-22
---

# 20 Gap Table / 知识缺口表

Last updated: 2026-06-22

## 使用说明

每个 gap 对应一个"阻碍你读懂 tbplas 某段代码的 C++ 知识盲区"。状态分四级：
- **confirmed**：经源码验证确实需要该知识才能读懂
- **suspected**：根据 C/Python 背景推断可能存在的盲区
- **weak**：影响较小，不阻塞主线
- **not-a-gap**：看起来像 gap 但其实不需要

## Gap 清单

| ID | Gap 名称 | 阻塞的文件 | 前置知识 | 状态 | 最小验证方式 |
|:---:|------|------|------|:---:|------|
| G01 | **看不懂 `class` 定义中的 `const &` 参数** | `base/lattice.h`, 几乎所有 `.h` | C 指针 | **confirmed** | 能解释 `void f(const Matrix3d& m)` 中 `const` 和 `&` 各自的作用 |
| G02 | **不知道 `std::vector` 和 C 数组的区别** | 各处 `vector<complex>` 用法 | C 数组、Python list | **confirmed** | 能写出 `vector<int> v = {1,2,3}; v.push_back(4);` |
| G03 | **看不懂 `namespace tbplas::base { }` 语法** | 所有 `.h` 文件 | C 前缀命名、Python import | **confirmed** | 能解释 `using namespace std;` 的后果 |
| G04 | **看不懂 `template <typename T>` 语法** | `tbpm/solver.h`, `base/results.h` | 无（C/Python 都无直接类比） | **confirmed** | 能解释 `vector<int>` 和 `vector<double>` 为什么是同一个模板的不同实例 |
| G05 | **看不懂派生类 `: public BaseClass`** | `tbpm/tbpm.h`, `base/io_text.h` | Python 继承 | **confirmed** | 能画出 `AbstractTBPM → TBPMCPU` 的继承关系 |
| G06 | **不理解构造/析构函数和 RAII** | `base/utils.h` (Timer), `builder/sample.h` | `__init__`/`__del__` | **confirmed** | 能解释为什么 Timer 对象离开作用域时自动打印时间 |
| G07 | **看不懂 `shared_ptr<SuperCell>` 在做什么** | `builder/sample.h:38` | C `malloc/free` | **confirmed** | 能解释 `shared_ptr` 和裸指针的区别 |
| G08 | **看不懂运算符重载 `operator=`** | `builder/sample.h:58-82` | Python `__add__` | **suspected** | 能解释 `a = b` 在 C++ 中可能是深拷贝 |
| G09 | **看不懂移动语义 `&&` 和 `std::move`** | `builder/sample.h:49-56` | 无 | **suspected** | 能解释移动构造和拷贝构造的调用时机差异 |
| G10 | **看不懂 CRTP `template<derived_t>` 模式** | `base/results.h:49` | 无 | **suspected** | 能画出 CRTP 的类关系图 |
| G11 | **看不懂 Eigen 的 `MatrixXd` 运算** | 几乎所有计算文件 | numpy | **confirmed** | 能将 numpy 的 `A @ B` 翻译成 Eigen 的 `A * B` |
| G12 | **看不懂 `.pyx` Cython 语法** | `python/` 目录下的 `.pyx` | Python C-extensions | **weak** | 能解释 `.pyx` 如何被编译成 `.so` |
| G13 | **不理解 `.h` / `.cpp` 分离的编译模型** | 所有文件 | Python 单文件 | **confirmed** | 能解释为什么 `.h` 中改了函数签名要重编译 |
| G14 | **看不懂 CMakeLists.txt 的 target_link** | 各目录 `CMakeLists.txt` | Makefile | **suspected** | 能给 `kubo_bastin` 添加一个新的 `.cpp` 并成功链接 |

## Gap 与 tbplas 文件的对应矩阵

| 文件 | 阻塞的 Gap |
|------|------|
| `base/datatypes.h` | G02 |
| `base/lattice.h` | G01, G03, G11 |
| `base/utils.h` | G06 |
| `base/io_base.h` | G05 |
| `base/results.h` | G04, G10 |
| `builder/sample.h` | G06, G07, G08, G09 |
| `tbpm/solver.h` | G04, G05, G11 |
| `tbpm/kubo_bastin.h` | G01, G02, G03, G11 |
| `python/builder/sample.pyx` | G12 |
| `CMakeLists.txt` | G14 |

## 核心结论

**confirmed gap 共 9 项**（G01–G07, G11, G13），这些是硬阻塞——不掌握就无法读懂对应的 tbplas 代码。其中 G01（const &）、G02（vector）、G11（Eigen）是最高优先级——这三个概念出现在几乎所有 tbplas 文件中，每读一行都要用到。

**suspected gap 共 4 项**（G08–G10, G14），这些比较高级，主要出现在 `builder/sample.h` 和 `base/results.h` 中。可以第一遍阅读时先跳过这些文件的细节，等 L1/L2 概念掌握后再回来攻克。

**weak gap 1 项**（G12），Cython 绑定目前不重要——你先要能读懂 C++ 端。
