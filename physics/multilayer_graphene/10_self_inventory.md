<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-11 20:02:07
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-11 20:02:08
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/10_self_inventory.md
 * @Description  :
-->
# 10 Self Inventory / 自检清单

Last updated: 2026-06-11

> 基于 `profiles/default_user_profile.md`，本次 quick_scan 不做深度资产匹配，仅记录关键背景快照。

## 基本身份

- 身份：计算凝聚态物理研究者（研究生/博士后阶段）
- 学科背景：物理学、计算物理
- 主要训练：凝聚态理论、数值模拟

## 核心研究方向

- 石墨烯及相关二维材料的电子性质计算
- TBPM（紧束缚传播法）大规模量子输运模拟
- 相关：拓扑物态、量子输运、DOS 计算

## 已有代码资产

### 主要代码资产：TMBG 项目 (`/home/wyl/project/TMBG`)

| 资产 | 说明 | 成熟度 |
|---|---|---|
| **TMBG 完整代码库** | 三层扭曲石墨烯紧束缚电子结构计算 | ✅ 生产就绪 |
| `src/main.py` | YAML 配置驱动的主入口，支持 band/dos/ldos/qe 四种计算 | ✅ 成熟 |
| `src/model.py` | TMBG + TBG 模型构建 (init/rlxd × 多层体系) | ✅ 成熟 |
| `src/calc.py` | TBPM DOS / Haydock LDOS / 对角化能带 / QE 波函数 | ✅ 成熟 |
| `src/func.py` | 转角计算、moire 常数、Δ→Uext→Vg 映射、calc_gap、calc_ldos_fwhm | ✅ 成熟 |
| `src/io_vis.py` | 三层架构 I/O + 可视化 (prefix 模式: save/read→load→vis) | ✅ 成熟 |
| `src/arc/` | 旧版归档代码 (连续模型/Berry曲率/边缘态/拓扑分析参考) | 📦 归档 |
| `configs/` | YAML 配置系统 (n=183/472 批量扫描配置已生成) | ✅ 完整 |
| `slurm/` | SLURM 集群提交脚本 (batch_submit.sh 批量提交) | ✅ 就绪 |

### 旧版/辅助资产

| 工具 | 类型 | 位置 | 成熟度 | 与转角石墨烯的潜在关联 |
|---|---|---|---|---|
| graphene.py | 紧束缚计算 | TMBG/src/arc/graphene.py | usable | 已被 TMBG 项目取代 |
| test_mpi.py | MPI 并行 | TBG/test/test_mpi.py | usable | 大规模转角超胞需要 MPI |
| submit.py | SLURM 提交 | ~/.agents/skills/cluster-workflow/assets/ | mature | 辅助集群任务提交 |

## 算力资源

- 远程 SLURM 集群（h3clogin），Intel oneAPI + MKL
- 多节点 MPI 并行
- **TMBG 项目已有生产级数据**：n=6 (762 轨道), n=29 (~15k), n=183 (~600k), n=472 (~4M)
- 已执行 runs: 06/10 (LDOS 扫描), 06/11 (FWHM 收敛测试), 06/12 (最新计算)

## 方法能力

| 能力 | 水平 | 备注 |
|---|---|---|
| 紧束缚模型 / 能带理论 | ⭐⭐⭐ 良好 | TMBG 项目已验证 n=6/29/183/472 体系 |
| MPI 并行 / TBPM | ⭐⭐⭐⭐⭐ 熟练 | 生产级 MPI 并行，cpu_fast 后端已配置 |
| Python / Shell / Git / SLURM | ⭐⭐⭐⭐⭐ 熟练 | 全套工具链就绪 |
| LAMMPS 弛豫 | ⭐⭐⭐ 可用 | TMBG 支持 rlxd 结构 (DRIP+REBO) |
| 连续模型 (BM/Koshino) | ⭐⭐ 基础 | src/arc/ 中有参考实现，待整合到主线 |
| 拓扑能带理论 (Berry curvature, Chern 数) | ⭐⭐ 基础 | src/arc/berry.py 参考实现，⚠️ **仅对角化可用**（TBPM 无法访问本征态），大体系受限 |
| 机器学习 | NEEDS_VERIFICATION | 暂无 |

## 当前科研目标

- 理解拓扑物态的计算方法
- 寻找可结合现有 TBPM/石墨烯代码的研究切口
- 具体论文目标：NEEDS_VERIFICATION

## 与转角石墨烯的关联预判

- **强关联**：现有紧束缚代码可直接改写为转角石墨烯的 Slater-Koster 参数化
- **中等关联**：TBPM 方法天然适合大超胞（转角体系超胞可达 10^4 atoms）
- **需要补充**：层间耦合参数、弛豫效应、魔角附近的强关联物理可能需要 beyond-TB 方法
