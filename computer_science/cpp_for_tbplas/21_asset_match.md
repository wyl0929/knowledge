<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-22 16:51:45
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-22 16:51:46
 * @FilePath     : /.agents/home/wyl/project/knowledge/computer_science/cpp_for_tbplas/21_asset_match.md
 * @Description  :
-->
---
document_type: asset_match
schema_version: v1.0
field: "C++ 编程（面向 tbplas 源码）"
last_updated: 2026-06-22
---

# 21 Asset Match / 资产-缺口匹配

Last updated: 2026-06-22

## 已有资产与缺口的映射

| Gap ID | Gap 名称 | 已有资产 | 缺失资源 | 获取难度 | 优先级 |
|:---:|------|------|------|:---:|:---:|
| G01 | const & 参数 | C 指针概念 | C++ 引用语义的直觉 | 低 — 这是第一个要学的 | 🥇 |
| G02 | std::vector | C 数组、Python list | C++ 容器的模板语法 | 低 — STL 入门 | 🥇 |
| G03 | namespace | C 前缀命名习惯 | using/namespace 的作用域规则 | 低 — 语法简单 | 🥇 |
| G04 | template | 无直接基础 | 编译期泛型的思维模型 | **高** — C++ 最陡的学习曲线 | 🥈 |
| G05 | 继承/虚函数 | Python 继承 | C++ 的 vtable、virtual 机制 | 中 — 概念可类比 | 🥈 |
| G06 | RAII | Python `with` 语句 | 析构函数的确定性调用语义 | 中 — Timer 是最好的教材 | 🥈 |
| G07 | shared_ptr | C 手动内存管理 | 引用计数 + 所有权的概念 | 中 — 概念简单但陷阱多 | 🥈 |
| G11 | Eigen | numpy | Eigen 的惰性求值陷阱 | 低 — numpy 用户上手快 | 🥇 |
| G13 | .h/.cpp 分离 | C 的 .h/.c 分离 | C++ 的 ODR (One Definition Rule) | 低 — C 经验可迁移 | 🥇 |
| G08 | 运算符重载 | Python `__add__` | C++ 的运算符重载规则 | 中 — 概念可类比 | 🥉 |
| G09 | 移动语义 | 无 | 左值/右值/移动的完整模型 | **高** — 现代 C++ 核心难点 | 🥉 |
| G10 | CRTP | 无 | 模板 + 继承的混合范式 | **高** — 最后再学 | 🥉 |
| G14 | CMake | Makefile 基础 | CMake 的 target 模型 | 低 — tbplas 已有现成 CMake | 🥇 |
| G12 | Cython | Python 熟练 | Cython 的类型声明语法 | 低 — L3，暂时不学 | 搁置 |

## 可利用的独特优势

1. **你已经有 tbplas 的完整算法文档**：`02_kubo_bastin_deep_dive.md` 和 `tbplas-internals.md` 已经解释了代码的物理逻辑和每一行的作用。学 C++ 时你不需要同时猜测"这段代码在物理上做什么"——你只需要猜"C++ 怎么表达这个物理"。

2. **你已经会编译和运行 tbplas**（待确认）：如果你能跑 `cmake .. && make && python -c "import tbplas"`，那么学 C++ 时立刻就能实验——改了代码马上跑，看结果对不对。

3. **Python 的 numpy 就是 Eigen 的翻版**：Eigen 的 API 刻意模仿了 MATLAB/numpy，你熟悉的 `A @ B`、`np.linalg.eigh` 在 Eigen 中有几乎一样的写法。

4. **C 的内存管理经验是 C++ 的"反面教材"**：理解 C 的 `malloc/free` 之痛，才能真正理解为什么 C++ 需要 RAII。你不是从零学内存管理——你是从"手动管理"升级到"自动管理"。

## 需要额外获取的资源

| 资源 | 用途 | 获取方式 |
|------|------|------|
| C++ 编译器（g++ ≥ 9 或 clang++ ≥ 14） | 编译 C++ 学习代码 | 系统已有（Linux 环境） |
| Eigen 库（header-only） | 练习 Eigen 用法 | `apt install libeigen3-dev` 或直接 include tbplas 自带的 |
| C++ 参考网站 cppreference.com | 随时查语法和 STL API | 浏览器 |
| 一个小型 C++ 练习项目 | 在不破坏 tbplas 的前提下练手 | 可在 `~/project/cpp_practice/` 创建 |
