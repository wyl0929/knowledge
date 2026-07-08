<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-22 16:49:42
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-22 16:49:42
 * @FilePath     : /.agents/home/wyl/project/knowledge/computer_science/cpp_for_tbplas/USER_BRIEF.md
 * @Description  :
-->
# USER BRIEF / 本次需求说明

Last updated: 2026-06-22

## 这份文件的作用

这里保存用户对本 field pack 的特殊要求。生成或更新本包中的任何主体文档前，agent 都必须先读取本文件。

本文件与其他文件的区别：

- `10_self_inventory.md`：记录本次使用的 profile 或用户背景快照；
- `USER_BRIEF.md`：记录本次调研的目标、重点、写作方式和回避事项；
- `90_QA.md`：保存后续自由讨论，默认不自动成为持续要求；
- `99_update_log.md`：保存修改历史。

## 用户原始需求

> 学习 C++ 代码，已有 C 和 Python 的基础。走 project_incubation 路线，目标是以读懂和修改 tbplas C++ 源码为核心驱动。

## 当前有效要求

- mode: `project_incubation`
- domain archetype: `science_technical`
- profile: `default_user_profile.md`（计算凝聚态物理研究者）
- 最终目标：能独立理解、编译、修改 tbplas C++ 源码
- 学习方式：以 tbplas 真实源码为教材，不学与项目无关的 C++ 特性

## 内容侧重点

- 希望重点展开：C++ 与 C/Python 的关键差异、tbplas 中用到的 C++ 特性（模板、继承、STL、Eigen、RAII、移动语义、Cython 绑定）、从"能读懂"到"能改"的阶梯路径
- 希望简略处理：C++ 标准库的全面 API 文档、与 tbplas 无关的 C++ 特性（如 iostream 格式化、正则表达式、filesystem）
- 暂时不需要涉及：C++20/23 新特性、GUI 开发、网络编程

## 写作与呈现偏好

- 语言与风格：中文正文，代码和术语保留英文；先直觉后术语
- 期望深度：能直接指导行动的深度——每个概念都对应 tbplas 中的具体文件:行号
- 是否需要公式 / 流程 / 作品例子 / 图表：需要核心概念对比表（C vs C++ vs Python）、学习路径流程图
- 是否需要阅读清单：需要按难度分级的 tbplas 源码阅读顺序
- 是否需要派生子方向：暂不需要

## 与父方向的继承关系

本包为独立 field pack，无父方向。

## 修改记录

| 日期 | 修改内容 | 来源 |
|---|---|---|
| 2026-06-22 | 初始化本次需求说明 | user prompt: "学习 C++ 代码, 已有 C 和 python 的基础" + 选择路线 C |
