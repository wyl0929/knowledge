<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-27 23:16:00
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-27 23:16:07
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/gamma_mu_sim/STATUS.md
 * @Description  :
-->
# STATUS.md — Γ-μ 随机游走模拟

> 角色：状态观测器（人类仪表盘） | 读者：👤 人类
> 静态参考见 CONTEXT.md | 任务清单见 docs/tasks.md

## 当前阶段

- **最后操作时间**: 06-28 00:10
- **已完成**: T1 核心模块 + T2 流水线 + T3 基础验证 + T4 M 扫描 + T5 核模型对比 + T7 可视化与报告
- **进行中**: 无阻塞
- **阻塞**: 无

## 最近三次决策/发现

1. T5 全部判据证伪——Lorentz 核无法消除随机游走（α 始终 ≈2），核加权仅改变 β 不改变 α
2. T5 P4 Lorentz λ 扫描——λ∈[2,8] 全部 α≈2，无"甜点 λ"
3. T7 完成——8 张图表 + 最终报告 + 知识晋升（02_kubo_bastin_deep_dive.md §7.7）

## 下一步（明确可执行）

- T6: θ 依赖性扫描（已跳过，可后续补做）
- 同步文档：CONTEXT.md 更新注意事项

## 指标健康度

| 指标 | 状态 | 备注 |
|------|:---:|------|
| 代码进度 | █████████░ 90% | T1–T5✓ T6⏭️ T7✓ |
| 模块自测 | 🟢 全通 | 8/8 模块 exit 0（含 t4_scan） |
| Pylance | 🟢 零错误 | mu_matrix.py 修订后检查通过 |
| T3 基础验证 | 🟢 通过 | V1 a=1.0049, V2 mean≈0 std≈ε, V3 阈值内 |
| T4 M 扫描 | 🟢 完成 | 636 行, α≈2.08 全 6 线, float32 退化 10¹⁰× |
| T5 核模型对比 | 🟢 完成 | P4 250 行, 全部判据证伪, Lorentz 无法消除随机游走 |
| T7 可视化+报告 | 🟢 完成 | 8 张图表, report.md, 知识晋升 |
| NaN 修复 | 🟢 已修复 | eval_chebyt→cos(nπ/2) 解析式

## 当前主要目标（周）

- [x] Phase 1: 核心模块搭建（T1–T2）
- [x] Phase 2: 基础验证 + M 系统性扫描（T3–T5 ✓）
- [x] Phase 3: 可视化 + 报告（T7 ✓, T6 跳过）
