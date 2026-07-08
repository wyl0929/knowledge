<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-22 16:53:32
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-22 16:53:33
 * @FilePath     : /.agents/home/wyl/project/knowledge/computer_science/cpp_for_tbplas/22_project_candidates.md
 * @Description  :
-->
---
document_type: project_candidates
schema_version: v1.0
field: "C++ 编程（面向 tbplas 源码）"
last_updated: 2026-06-22
---

# 22 候选项目卡片

Last updated: 2026-06-22

## 项目总览

三个候选项目形成递进关系：P1 验证"能读懂"，P2 验证"能编译和改参数"，P3 验证"能加功能"。建议从 P1 开始，P1 完成即达到 MVP 成功标准。

---

## P1: tbplas 核心文件逐行通读 ⭐ 推荐 MVP

| 维度 | 内容 |
|------|------|
| **一句话目标** | 独立阅读 `kubo_bastin.h` 的 `kbdc_mu()` 函数（~100 行），能逐行解释每一句 C++ 代码在做什么 |
| **为什么选这个** | 这是你研究工作的核心——Kubo-Bastin Hall 电导率的数值实现。你已经从物理/算法层面完全理解它（`02_kubo_bastin_deep_dive.md`），唯一缺的是 C++ 语法层 |
| **前置 Gap** | G01, G02, G03, G11（const &、vector、namespace、Eigen） |
| **输入** | `kubo_bastin.h:175-269`（已带物理注释的源码） |
| **成功标准** | 能对着 `kbdc_mu()` 的每一行说：①这行声明了什么变量/类型 ②这行调用了什么方法 ③数据在内存中如何流动 |
| **估算时间** | 3–5 天（每天 2 小时） |
| **risks** | 模板语法 (`ArrayXz`) 可能卡住——此时先跳过模板细节，把 `ArrayXz` 当"复数向量"理解即可 |
| **stop criteria** | 如果第 3 天仍无法解释第 2.1 节的三项递推循环（`for (int i = 2; i < num_kernel; ++i)`），则回退到更简单的文件（`base/lattice.h`） |

### 操作化状态

operational_status: metric_checked — 成功标准已明确为"每行可解释"

---

## P2: tbplas 编译链掌握 + 参数修改

| 维度 | 内容 |
|------|------|
| **一句话目标** | 修改 `solver.h` 中的默认参数（如 `dckb_num_kernel`），重新编译 tbplas，运行 MG 项目验证修改生效 |
| **为什么选这个** | 从"读"到"改"的关键一步。tbplas 已有 CMake 构建系统和 Python 运行脚本，你只需要找到参数位置、修改、重编译、跑测试 |
| **前置 Gap** | G13, G14（.h/.cpp 分离、CMake） + P1 完成 |
| **输入** | `solver.h` 参数区、`CMakeLists.txt`、MG 项目的 `run_mg.py` |
| **成功标准** | ①找到 `dckb_num_kernel` 的定义位置 ②将其从默认值改为 512 ③ `cmake --build .` 成功 ④用 MG 项目跑一次 Hall 电导率计算，结果与 M=512 文献值一致 |
| **估算时间** | 1–2 天 |
| **risks** | 集群编译环境可能有坑（oneAPI 路径、MKL 链接）——用 `submit.py` 提交编译任务可以规避 |
| **stop criteria** | 如果编译失败且错误信息完全看不懂，先回到 P1 继续积累 C++ 语感 |

### 操作化状态

operational_status: resource_checked — 集群编译环境可用，但不排除配置问题

---

## P3: 为 tbplas 添加一个新的输出量

| 维度 | 内容 |
|------|------|
| **一句话目标** | 在 `kubo_bastin.h` 中添加代码，输出中间量 $\mu_{00}$（零阶 Chebyshev 矩）到文件，用于诊断基线偏移问题 |
| **为什么选这个** | 这是你论文里可能需要的东西——$\mu_{00}$ 的数值可以直接验证 §3.3 问题 B 的基线偏移假设。这也是一个"最小侵入"的修改：不改变算法逻辑，只加输出 |
| **前置 Gap** | G04, G05, G06, G07（模板、继承、RAII、智能指针）+ P1+P2 完成 |
| **输入** | `kubo_bastin.h:262-268`（mu_avg 累加处）、`base/io_text.h`（文件输出接口） |
| **成功标准** | ①在 mu_avg 累加后添加 `std::cout << mu_avg(0,0) << std::endl;` ②编译通过 ③运行 MG 项目看到终端输出 $\mu_{00}$ 值 ④输出值随 M 增大而显著偏移（验证了基线偏移假设） |
| **估算时间** | 2–3 天 |
| **risks** | 模板函数中的 I/O 可能有编译问题——需要理解 `ArrayXz` 的模板参数 |
| **stop criteria** | 如果无法定位 mu_avg 的准确累加位置，则退回到只加 `cout << "hello"` 验证编译链 |

### 操作化状态

operational_status: provisional — 需要 P1+P2 完成后重新评估

---

## 项目选择建议

**选 P1 作为 MVP。** 理由：
1. P1 直接服务于你的研究——读懂 `kbdc_mu()` 对理解基线偏移问题（§3.3 问题 B）至关重要
2. P1 不需要修改代码，不依赖编译环境，可以立刻开始
3. P1 的成功标准最明确：每行都能解释
4. P1 完成后，P2（编译修改）是自然的下一步，不需要重新规划

P2 和 P3 作为 P1 的自然延伸，不需要现在决定是否执行——等 P1 完成后再评估。
