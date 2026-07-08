<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-22 16:55:57
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-22 16:55:58
 * @FilePath     : /.agents/home/wyl/project/knowledge/computer_science/cpp_for_tbplas/00_beginner_guide.md
 * @Description  :
-->

# 00 Beginner Guide / C++ 入门指南（以 tbplas 为教材）

Last updated: 2026-06-22

## 这篇指南是给谁的

给懂 C 和 Python、需要阅读 tbplas C++ 源码的计算物理研究者。如果你：
- 能用 C 写 struct 和指针操作，能用 Python 写 numpy 数组运算
- 面对 `kubo_bastin.h` 里的 `ArrayXz`、`const Matrix3d&`、`template<model_t>` 感到困惑
- 不想花两个月啃《C++ Primer》，只想快速上手读懂你的研究代码

那这篇指南就是为你写的。

## 先用直觉建立地图

### C++ 不是"C 加了点东西"

把 C、C++、Python 想象成三种交通工具：

| | C | C++ | Python |
|------|:---:|:---:|:---:|
| **类型** | 自行车——每个零件你都看得见 | 汽车——引擎盖下有引擎，但你不需要每次都打开它 | 自动驾驶出租车——你只管说去哪 |
| **速度** | 快（如果你体力好） | 很快（同样的路比自行车快） | 慢一些，但够用 |
| **控制** | 完全控制——每个齿轮你自己拨 | 控制 + 自动化——自动挡，但你可以切手动 | 几乎不控制——你只能告诉司机目的地 |
| **出事时** | 链子掉了你自己修 | 仪表盘亮灯——你需要会读故障码 | 车坏了叫另一辆 |

tbplas 选 C++ 的原因是：它需要在"完全控制内存布局"（像 C）和"表达复杂数值算法"（像 Python/numpy）之间取一个平衡。Eigen 库提供了 numpy 级别的表达力，C++ 的模板提供了零开销抽象，RAII 提供了自动资源管理——三者相加 = 高性能 + 可维护的物理计算代码。

### 你只需要学 C++ 的 20%

C++ 是一门巨语言（~2000 页标准）。但 tbplas 只用到了其中一小部分。以下是你的"20% 地图"：

```
C++ 全语言 (100%)
  ├── 与你无关的 70%: iostream 格式化, regex, filesystem, coroutines, ...
  ├── 暂时不学的 10%: 移动语义, CRTP, 变参模板, Cython 编写, ...
  └── ★ 现在要学的 20%:
        ├── namespace + using          (5 分钟)
        ├── class/struct 带方法        (30 分钟)
        ├── vector<T> / complex<T>     (30 分钟)
        ├── const T& 引用传参          (30 分钟)
        ├── Eigen MatrixXd / ArrayXz   (1 小时)
        ├── 构造/析构/RAII             (1 小时)
        └── template <typename T>      (2 小时)
```

## 三个核心思维转变

### 转变 1：从"手动管理内存"到"让编译器帮你管"

**C 的做法**（你熟悉的）：
```c
double* data = (double*)malloc(100 * sizeof(double));
// ... 用 data ...
free(data);  // 忘了这行 → 内存泄漏
```

**C++ 的做法**（tbplas 中的做法）：
```cpp
std::vector<double> data(100);
// ... 用 data ...
// 不需要 free——离开作用域时自动释放
```

这就是 RAII（Resource Acquisition Is Initialization）的核心思想：**把资源的生命周期绑在对象的生命周期上**。对象创建时获取资源，对象销毁时释放资源。tbplas 的 `Timer` 类（`base/utils.h`）是 RAII 的最小完美示例——Timer 对象创建时记下起始时间，销毁时自动打印耗时。你不必手动调用 `timer_stop(t)`。

### 转变 2：从"传指针"到"传引用"

**C 的做法**：
```c
void normalize(double* vec, int n) {  // 传指针
    double norm = 0;
    for (int i = 0; i < n; i++) norm += vec[i] * vec[i];
    // ...
}
```

**C++ 的做法**（tbplas 中最常见的写法）：
```cpp
void normalize(const std::vector<double>& vec) {  // 传引用
    double norm = 0;
    for (auto x : vec) norm += x * x;  // 不需要 n 参数！
    // ...
}
```

`const T&` 的含义拆解：
- `T&` = T 的引用（别名，不是副本，不是指针）
- `const` = 我不会修改它
- 合起来 = "给我看你的数据，我保证不改，而且不需要拷贝"

在 tbplas 中，你会在几乎每个函数参数里看到 `const Matrix3d&`、`const vector<complex>&`——这就是 C++ 的"传大数据但不拷贝"的方式。

### 转变 3：从"duck typing"到"编译器检查一切"

**Python 的做法**：
```python
def add(a, b):
    return a + b  # a 和 b 可以是任何能相加的东西
```

**C++ 的做法**（tbplas `base/funcs.h` 的风格）：
```cpp
double add(double a, double b) {
    return a + b;  // a 和 b 必须是 double，编译时就确定了
}
```

C++ 的类型在编译时就完全确定。这意味着：
- 好处：拼写错误、类型不匹配在编译时就会发现（不用等到运行时崩）
- 代价：你需要明确写出类型，模板编译错误信息可能长达 100 行

tbplas 用 `auto` 关键字缓解了这个代价——让编译器帮你写类型：
```cpp
auto result = a + b;  // 编译器知道 result 的类型
```

## 你的第一条 C++ 学习路径

### Step 0（今天就做，5 分钟）

打开 `kubo_bastin.h`，第 175 行开始。不要试图理解，只观察：
- 你能认出的 C 结构（`for`, `int`, `double`, `*ptr`）
- 你不认识的 C++ 结构（`ArrayXz`, `const auto&`, `template`）

把你不认识的 3–5 个东西记下来。这就是你的 Day 1 学习清单。

### Step 1（Day 1，2 小时）

按顺序阅读 `12_field_map.md` 的"第一梯度"文件：
1. `base/datatypes.h` — 只看类型定义
2. `base/lattice.h` — 第一个真正的 class
3. 每个文件读完后，用自己的话写一行注释在脑子里

### Step 2（Day 2–4，每天 2 小时）

对照 `02_kubo_bastin_deep_dive.md` §2 的物理注释，逐行阅读 `kbdc_mu()`。
- 遇到不懂的 C++ 语法 → 查本包的 `12_field_map.md` §3 速查表
- 速查表没覆盖的 → 查 cppreference.com
- 物理理解（Layer 3）已经由文档提供，你只需要解码语法（Layer 1）和语义（Layer 2）

### Step 3（Day 5，2 小时）

闭卷自测：不看任何参考资料，从头到尾口头解释 `kbdc_mu()` 的每一行。录音，然后对比物理注释。

## 需要避免的常见陷阱

| 陷阱 | 为什么危险 | 正确做法 |
|------|------|------|
| **先通读《C++ Primer》再看代码** | 你会花 80% 时间学 tbplas 不需要的东西，然后失去动力 | 以代码为教材，遇到不懂的才查 |
| **试图理解每一个 template 展开** | template 编译错误可能 100+ 行，深追会迷失 | 第一遍把 `ArrayXz` 当"复数向量"黑箱，第二遍再深入 |
| **用 C 风格写 C++** | `malloc` + `free` + 裸指针在 C++ 中反而是反模式 | 用 `vector`、`shared_ptr`、RAII |
| **把 `&` 当指针** | C 中 `&` 是取地址，C++ 中 `&` 在类型后面是引用——完全不同的东西 | 记住：`T*` 是指针（和 C 一样），`T&` 是引用（C 没有） |
| **跳过编译直接猜代码行为** | C++ 的未定义行为 (UB) 不会报错，只会静默地产生错误结果 | 不确定就编译运行一个小例子验证 |

## 推荐资源

- **查语法**：[cppreference.com](https://en.cppreference.com/) — C++ 的权威在线文档
- **查 Eigen**：[Eigen 官方文档](https://eigen.tuxfamily.org/) — 特别是 "Quick reference guide" 页面
- **查编译错误**：把错误信息贴到搜索引擎，通常 StackOverflow 前三条就是答案
- **快速实验**：用 `g++ -std=c++17 test.cpp && ./a.out` 验证任何你不确定的语法行为

## 下一步

翻到 `23_mvp_experiment_plan.md`——那里有一份精确到每天的 5 天实验计划。现在就做 Step 0：打开 `kubo_bastin.h` 第 175 行，记录你的前 3 个困惑。
