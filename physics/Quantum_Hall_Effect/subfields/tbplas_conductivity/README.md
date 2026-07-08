<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-21 02:30:28
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-24 01:00:00
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/subfields/tbplas_conductivity/README.md
 * @Description  :
-->
<!--
Subfield: tbplas 电导率计算方法
Parent: 量子霍尔效应
Domain archetype: science_technical
Created date: 2026-06-21
-->

# tbplas 电导率计算方法 — 子领域参考

Parent field: [量子霍尔效应](/home/wyl/project/knowledge/physics/Quantum_Hall_Effect/)

来源文档：
- [tbplas-internals.md §9–§12](/home/wyl/project/shared/tbplas-internals.md)
- Python 源码审计：`~/anaconda3/envs/tbplas-alpha/lib/python3.12/site-packages/tbplas/tbpm/solver.py`、`analysis.py`、`config.py`、`diag/lindhard.py`

## 本子领域的内容

tbplas 提供 **4 种电导率计算路径** + 动态极化率/介电函数双路径 + 7 种辅助计算方法，按算法范式分为：

- **TBPM 传播法**（随机波函数传播，适合大体系）：Kubo-Bastin Hall、DC 关联函数、AC 关联函数、动态极化率
- **Diag 对角化法**（k 空间直接对角化，适合中小体系）：Lindhard AC、动态极化率、介电函数

## 文件索引

| 文件 | 内容 |
|------|------|
| `01_methods_reference.md` | 四种电导率方法的物理意义、算法简述、参数表、适用场景、已知限制；双路径动态极化率/介电函数；TBPMSolver 完整方法清单 |
| `02_kubo_bastin_deep_dive.md` | **Kubo-Bastin C++ 核心深度解析**：两路 Chebyshev 三项递推机制、E1–E3 根因诊断结论 (2026-06-24 更新)、与 García 2015 逐项对比、MG 项目实测数据、基线偏移假说矩阵 |
| `03_tbpm_dc_correlation.md` | **TBPM DC 关联函数 C++ 核心深度解析**：准本征态构造、Chester-Thellung → VAC 路径、与 Kubo-Bastin 的核心差异 |
| `04_sigma_xx_equivalence.md` | **σ_xx 两条路径等价性证明**：Kubo-Bastin (能量域 Chebyshev) ≡ TBPM DC 关联函数 (时域 FTM)，均源自 Kubo-Greenwood 公式 |
| `03_M_scan_test_plan.md` | **M 扫描测试方案**：单层石墨烯 Kubo-Bastin Hall 系统性 M 扫描 |
| `chebyshev_precision/` | **子方向包：切比雪夫迭代浮点精度** — Phase A–M 根因诊断 + Γ·μ 随机游走机制 + 证据账本 + gap 表 + 候选项目 |

## 子方向包

| 子方向 | 路径 | 说明 |
|------|------|------|
| gamma_mu_sim | `gamma_mu_sim/` | Γ-μ 随机游走数值模拟项目（Python） |
| chebyshev_precision | `chebyshev_precision/` | 切比雪夫迭代精度问题系统化 field pack |

## 快速导航

- 想算 **Hall 电导率 $\sigma_{xy}(\mu)$**（与 QHE 实验对比）→ Kubo-Bastin（`01` §2）
- 想理解 **Kubo-Bastin 为何 M>512 发散** → `02_kubo_bastin_deep_dive.md`
- 想**实际跑 M 扫描测试** → `03_M_scan_test_plan.md`（含 YAML + SLURM + 分析脚本）
- 想算 **能量分辨 $\sigma_{xx}(E)$**（分析哪些态导电）→ DC 关联函数（`01` §3）
- 想算 **频率依赖 $\sigma(\omega)$** → AC 关联函数 或 Lindhard AC（`01` §4, §5）
- 想算 **动态极化率 / 介电函数** → TBPM 或 Lindhard 双路径（`01` §6）
- 想了解 **TBPMSolver 全部计算能力** → 其他方法速览（`01` §7）
