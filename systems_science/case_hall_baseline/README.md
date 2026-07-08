<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-07-01 15:20:27
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-07-01 15:20:28
 * @FilePath     : /.agents/home/wyl/project/knowledge/systems_science/case_hall_baseline/README.md
 * @Description  :
-->
# case_hall_baseline 归档说明

> 本目录归档了 Kubo-Bastin Hall 电导基线偏移归因案例的关键文件。
> 完整案例叙述见: `../91_case_study_hall_conductance_baseline.md`

## 目录结构

```
case_hall_baseline/
├── README.md              # 本文件
├── figures/                # 关键诊断图表 (13 个)
├── scripts/                # 核心分析脚本 (10 个)
├── vbl_logs/               # VBL sum(θ) 插桩日志 (6 个)
├── docs/                   # 📋 归因全流程的 plan / task / log (11 个文件)
│   ├── log.md              #   全流程 AI 执行日志 (06-21 ~ 07-01)
│   ├── blue_print.md       #   项目战略路线图
│   ├── M_scan_test_plan.md #   M 扫描测试计划 (基线偏移首次发现)
│   ├── M_scan_test_task.md #   M 扫描测试任务单
│   ├── baseline_shift_plan.md  # H₀/H₁ 误差累积假说验证计划
│   ├── baseline_shift_task.md  # H₀/H₁ 验证任务单
│   ├── plan_m_M_grid.md    #   m×M 网格计划 (偏移特征表征)
│   ├── plan_baseline_root_cause.md # E1-E5 根因诊断计划 (H_A/H_B/H_C)
│   ├── task_baseline_root_cause.md # E1-E5 根因诊断任务单
│   ├── plan_vbl_trace.md   #   VBL 变量追踪计划 (Phase A-M)
│   └── task_vbl_trace.md   #   VBL 变量追踪任务单
└── data/                   # 关键数值数据
    ├── M_int/              # M×int 全矩阵扫描 (决定性证据)
    ├── kite_cross_check/   # quantum-kite 交叉验证
    └── *.txt               # 关键实验的 σ_xy 数据
```

## 数据来源

所有文件从 `/home/wyl/project/MG/` 的项目目录中提取，时间跨度为 2026-06-21 至 2026-07-01。

## 核心数据集

| 数据集 | 位置 | 说明 |
|--------|------|------|
| **M×int 全矩阵扫描** | `data/M_int/` | 5×5 (M×int) Hall 电导率数据 — Nyquist 混叠根因的决定性证据 |
| **quantum-kite 交叉验证** | `data/kite_cross_check/` | 独立代码实现的 Hall 电导率 (M=64~4096, B=100T) |
| **VBL sum(θ) 日志** | `vbl_logs/` | Γ·μ 累加中间量 vs θ 曲线 (M=2048~4096) |
| **M 扫描基线偏移** | `data/hall_m256_M*_B100.0.txt` | 基线偏移首次发现的原始数据 |
| **无核测试 (E2)** | `data/*_nokernel_*.txt` | Jackson 核关闭对比 |
| **rescale 扫描 (E3)** | `data/*_rescale_*.txt` | rescale=11, 12 对比 |
| **disorder 测试** | `data/*_clean/d027/d5*.txt` | Anderson 无序对照 |

## 关键图表

| 图表 | 文件 | 对应论文用途 |
|------|------|-------------|
| sum(θ) M 对比 | `figures/sum_vs_theta_all_M.png` | Fig 2: 被误解的 VBL 观测 |
| 积分发散 | `figures/sum_integral_convergence.png` | Fig 2(inset) |
| Kahan 无效 | `figures/kahan_vs_standard.png` | Fig 3: 排除累加精度假说 |
| Jackson 核无效 | `figures/J1_unified_kernel_S_vs_M.png` | Fig 4: 排除核 M 依赖性 |
| 随机游走验证 | `figures/M1_noise_injection.png` | Appendix: Phase M 独立验证 |
| M 扫描总览 | `figures/M_scan_summary.png` | Fig 1: 问题陈述 |

## .h5 大文件位置索引

以下文件因体积过大未打包，保留在原项目目录中：

| 文件 | 路径 | 大小 |
|------|------|------|
| μ 基准 (VBL) | `/home/wyl/project/MG/runs/0624/mu_raw_M4096_m64.h5` | 257 MB |
| μ 基准 (M_int) | `/home/wyl/project/MG/runs/0701/mu_raw_rescale20_m512_M4096.h5` | 257 MB |

## 相关文档

- `../91_case_study_hall_conductance_baseline.md` — 案例总结 (系统科学视角)
- `docs/log.md` — 全流程 AI 执行日志 (归因过程的第一手记录)
- `docs/plan_vbl_trace.md` — VBL 变量追踪计划 (Phase A-M 全 12 阶段)
- `docs/task_vbl_trace.md` — VBL 变量追踪任务单
- `docs/plan_baseline_root_cause.md` — 根因诊断计划 (E1-E5, H_A/H_B/H_C)
- `docs/blue_print.md` — 项目战略路线图
- `/home/wyl/project/MG/docs/references/02_kubo_bastin_deep_dive.md` — Kubo-Bastin 算法深度分析
- `/home/wyl/shared/tbplas-internals.md` §12 — tbplas 内部 NaN/Baseline 机制
