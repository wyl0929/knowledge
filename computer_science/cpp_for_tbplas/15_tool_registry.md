<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-22 16:55:57
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-22 16:55:58
 * @FilePath     : /.agents/home/wyl/project/knowledge/computer_science/cpp_for_tbplas/15_tool_registry.md
 * @Description  :
-->
---
document_type: tool_registry
schema_version: v1.0
field: "C++ 编程（面向 tbplas 源码）"
last_updated: 2026-06-22
---

# 15 Tool Registry / 学习工具与资源注册

Last updated: 2026-06-22

## 编译器与构建工具

| 工具 | 用途 | 获取方式 | 相关性 |
|------|------|------|:---:|
| **g++** (≥ 9.0) | 编译 C++ 学习代码 | 系统自带（`sudo apt install g++`） | 高 |
| **clang++** (≥ 14) | 替代编译器，错误信息更友好 | `sudo apt install clang` | 中 |
| **CMake** (≥ 3.16) | 构建 tbplas | 系统自带或 `pip install cmake` | 高 |
| **make** / **ninja** | CMake 的后端构建工具 | 系统自带 | 高 |

## 文档与参考资料

| 资源 | 用途 | URL | 相关性 |
|------|------|------|:---:|
| **cppreference.com** | C++ 标准库和语法的权威在线文档 | https://en.cppreference.com/ | 高 |
| **Eigen 文档** | Eigen 库的 API 参考 | https://eigen.tuxfamily.org/ | 高 |
| **C++ Core Guidelines** | C++ 最佳实践（Bjarne Stroustrup 主编） | https://isocpp.github.io/CppCoreGuidelines/ | 中 |
| **Compiler Explorer** | 在线编译器，即时看汇编输出 | https://godbolt.org/ | 低 |

## 本包内部文档

| 文件 | 用途 | 何时阅读 |
|------|------|------|
| `00_beginner_guide.md` | 入门指南——先读这个 | 第一天 |
| `02_frontier_compass.md` | 边界罗盘——定位学习范围 | 第一天 |
| `11_term_disambiguation.md` | 术语澄清——C vs C++ vs Python | 遇到概念混淆时 |
| `12_field_map.md` | 领域地图——概念依赖关系 + 速查表 | 需要查语法时 |
| `20_gap_table.md` | 知识缺口表 | 规划学习顺序时 |
| `23_mvp_experiment_plan.md` | 5 天实验计划 | 执行学习时 |

## tbplas 相关资源

| 资源 | 位置 | 用途 |
|------|------|------|
| tbplas C++ 源码 | `~/tbplas/source/tbplas-cpp-a021ca8/sources/` | 学习教材 |
| tbplas Python 绑定 | `~/tbplas/source/tbplas-cpp-a021ca8/python/` | 理解 C++/Python 桥接（L3） |
| Kubo-Bastin 深度解析 | `~/project/knowledge/.../tbplas_conductivity/02_kubo_bastin_deep_dive.md` | 物理注释 |
| tbplas 内部文档 | `~/project/shared/tbplas-internals.md` | 数值稳定性分析 |
| MG 项目 | `~/project/MG/` | 运行和测试 tbplas |

## 推荐但不必须的 C++ 教材

如果某天你想脱离 tbplas、系统补 C++ 基础，以下教材按优先级排列：

| 教材 | 适合阶段 | 特点 | 厚度 |
|------|:---:|------|:---:|
| **A Tour of C++** (Stroustrup) | P1 完成后 | 180 页快速概览 C++17，作者是 C++ 之父 | ★★ |
| **Effective Modern C++** (Meyers) | P2 完成后 | 专门讲 C++11/14 的最佳实践，与你相关度高 | ★★★ |
| **C++ Primer** (Lippman) | 作为参考书 | 1000 页，不需要通读——当字典查 | ★★★★★ |
