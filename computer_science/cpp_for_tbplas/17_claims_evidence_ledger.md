<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-22 16:55:58
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-22 16:55:59
 * @FilePath     : /.agents/home/wyl/project/knowledge/computer_science/cpp_for_tbplas/17_claims_evidence_ledger.md
 * @Description  :
-->
---
document_type: claims_evidence_ledger
schema_version: v1.0
field: "C++ 编程（面向 tbplas 源码）"
last_updated: 2026-06-22
---

# 17 Claims and Evidence Ledger / 论断-证据台账

Last updated: 2026-06-22

## 使用说明

每个论断标注类型：
- **fact**：可被源码或文档直接验证
- **interpretation**：基于证据的合理推断
- **speculation**：尚无直接证据的猜测
- **recommendation**：基于以上类型的行动建议

## 论断清单

| ID | 论断 | 类型 | 证据 | 状态 |
|:---:|------|:---:|------|:---:|
| C1 | 懂 C 和 Python 的物理研究者可以跳过通用 C++ 教材，以 tbplas 源码为教材学习 C++ | interpretation | `12_field_map.md` 显示 tbplas 只用了 ~20% 的 C++ 特性；物理算法已通过 `02_kubo_bastin_deep_dive.md` 理解 | NEEDS_VERIFICATION — 需 MVP 实验验证 |
| C2 | `kbdc_mu()` 函数只用到了 L1 级别的 C++ 概念，不需要模板/继承/虚函数即可理解 | interpretation | 源码分析：`kbdc_mu()` 中未出现 template 关键字、虚函数声明、或继承语法 | confirmed — 源码直接验证 |
| C3 | Eigen 的 `ArrayXz` 在 tbplas 中主要用作存储容器（类似 numpy array），而非表达式模板 | interpretation | `kbdc_mu()` 中的 Eigen 用法主要是 `vec_copy`、`vec_dot`、索引访问，未涉及复杂表达式 | confirmed — 源码直接验证 |
| C4 | 用户已有的 C 指针经验对理解 C++ 引用（`&`）有阻碍作用（负迁移） | speculation | C 中 `&` 是取地址运算符，C++ 中 `T&` 是引用类型——同一符号不同语义 | NEEDS_VERIFICATION — 需用户实际操作确认 |
| C5 | 用户已有的 numpy 经验对理解 Eigen 有正迁移作用 | interpretation | Eigen API 刻意模仿 numpy/Matlab；`02_kubo_bastin_deep_dive.md` 中已建立 numpy↔Eigen 对应 | confirmed — API 设计可验证 |
| C6 | tbplas 是"对非 C++ 程序员友好"的计算物理代码 | interpretation | 代码不使用高级模板技巧、继承层次浅（1–2 层）、命名清晰 | confirmed — 源码结构可验证 |
| C7 | 5 天内能完成 `kbdc_mu()` 的逐行阅读（≥90% 行覆盖率） | speculation | 基于 C1–C6 的推断，但未经实际验证 | NEEDS_VERIFICATION — 这是 MVP 实验要验证的核心论断 |
| C8 | 物理理解先行（Layer 3 已知）可以将 C++ 语法学习效率提升 3–5 倍 | speculation | 基于教育心理学"先验知识促进学习"的一般原则 | NEEDS_VERIFICATION — MVP 的副产品可提供证据 |

## 核心论断依赖链

```text
C8 (物理先行提升效率)
  ├── 依赖 C1 (以 tbplas 为教材可行)
  ├── 依赖 C2 (L1 概念足够)
  └── 依赖 C5 (numpy→Eigen 正迁移)
        ↓
      C7 (5 天可完成)
        ├── 依赖 C3 (Eigen 简单用法)
        ├── 依赖 C6 (tbplas 友好)
        └── 反对 C4 (指针→引用负迁移可控)
```

## 待验证优先级

| 优先级 | 论断 | 验证方式 | 验证时间 |
|:---:|:---:|------|:---:|
| 🥇 | C7 — 5 天可完成 | 执行 MVP 实验 | 5 天后 |
| 🥈 | C4 — 指针→引用负迁移 | 观察 Day 1 是否卡在 `const &` 上 | Day 1 结束 |
| 🥉 | C8 — 物理先行 3–5× 效率提升 | 与"零物理背景学同样代码"的对照组比较（可能需要他人数据） | 长期 |

## 修改记录

| 日期 | 修改 | 来源 |
|------|------|------|
| 2026-06-22 | 初始化论断台账 | Explore subagent 源码扫描 + default_user_profile.md |
