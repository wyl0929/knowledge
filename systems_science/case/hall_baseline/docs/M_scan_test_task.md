<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-21 03:24:51
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-21 03:26:31
 * @FilePath     : /MG/docs/sigma/M_scan_test_task.md
 * @Description  :
-->

# [x] AI: 0621_0324 - Kubo-Bastin Hall M 发散测试任务

> 完成记录: [log.md](../../log.md#ai-0621-0324) → AI: 0621_0324
> M=64-1024 ×7 全部成功 (exit 0), **M=1024 全无 NaN** (推翻计划预期)

**目标**: 系统测试单层石墨烯 Kubo-Bastin Hall 电导率随 `dckb_num_kernel` (M) 增大的完整演化轨迹，验证三个预期区间——"可用区"(M=64–256)、"发散区"(M=384–512)、"崩溃区"(M≥1024 全 NaN)，并确认 M=256 为最优平衡点。

**背景**: 此前实测（`tbplas-internals.md` §12）发现 M 增大时 Hall 电导率噪声指数增长，M≥1024 全 NaN。本测试固定其余参数（单层 graphene, B=100T, m=256, rs=8, ts=64, T=10K），仅扫描 M=[64, 128, 256, 384, 512, 768, 1024, 2048]，系统收集每个 M 下的 σ_xy(E) 曲线和收敛指标。详细设计方案见 `docs/sigma/M_scan_test_plan.md`。

**执行步骤**:

1. **生成 8 个 YAML 配置文件**（`configs/hall_M064.yaml` ~ `hall_M2048.yaml`）：
   - 基于 `M_scan_test_plan.md` §1.2 的母配置模板创建 `hall_M_base.yaml`
   - 用 shell 循环 + Python 一行脚本批量生成 8 个独立 YAML，仅修改 `model.tag` 和 `hall.dckb_num_kernel` 字段
   - 完成后 `rm hall_M_base.yaml`，确认 8 个文件全部存在且语法合法

2. **检查并准备 SLURM 提交脚本**：
   - 确认 `slurm/slm_single.sh` 存在且 CONFIG_FILE 路径与项目实际路径一致（ `/home/wyl/project/MG/configs/` 而非 `/home/ylwang/scratch/MG/configs/`）
   - 若不一致则修正 `slm_single.sh` 中的 CONFIG_FILE 变量

3. **批量提交 8 个 SLURM 作业**：
   - `for M in 64 128 256 384 512 768 1024 2048; do sbatch --job-name=hall_M${M} slurm/slm_single.sh; done`
   - 用 `squeue -u $USER` 确认全部作业进入队列
   - 优先提交 M=64,128,256,384,512 五组（预计各 5min–2h），观测 NaN 出现后再决定是否继续 M≥1024

4. **等待作业完成后收集结果**：
   - 所有输出位于 `runs/0621/`（或实际运行日期 `runs/MMDD/`）
   - 预期每 M 产出 3 个文件：`hall_ABC_d0.000_M{M}_B100.yaml` + `.dat` + `.png`
   - 检查各 SLURM `.out` 日志无 fatal error

5. **创建并运行分析脚本**：
   - 在 `test/` 下创建 `analyze_M_scan.py`（源码见 `M_scan_test_plan.md` §2.2）
   - 修改脚本中的 `RUNS_DIR` 为实际输出目录
   - `conda run -n tbplas-alpha python test/analyze_M_scan.py`
   - 输出汇总表（NaN 比例 + RMS）和 `runs/MMDD/M_scan_summary.png`

**成功判据**:
- [ ] 8 个 YAML 配置文件全部生成，`model.tag` 和 `hall.dckb_num_kernel` 正确对应
- [ ] 8 个 SLURM 作业全部提交并正常完成（无 OOM / timeout）
- [ ] M=64–256 的 σ_xy 曲线信号随 M 增强，噪声可接受
- [ ] M=256 为最优平衡点：RMS (低能窗口 [-0.5,0.5] eV) ≈ 0.3 e²/h
- [ ] M=384–512 噪声指数增长，M=512 时 RMS 量级 ≈ 3 e²/h（与预期物理值相当）
- [ ] M≥1024 全部能量点的 σ_xy 为 NaN（NaN 比例 = 1.0）
- [ ] （高级）M=256–512 可看到 σ_xy ≈ ±2, ±6, ±10 e²/h 的 QHE 平台结构雏形
- [ ] `analyze_M_scan.py` 运行成功，产出汇总表 + `M_scan_summary.png`
- [ ] Pylance 对 `test/analyze_M_scan.py` 零错误

**约束**:
- 环境: `conda activate tbplas-alpha` + `export TBPLAS_CORE_PATH=/home/wyl/tbplas/install/tbplas-cpp-a021ca8/lib`
- 不修改 `src/` 下任何代码（纯测试任务）
- 不修改 `configs/config.yaml` 主配置（生成独立 YAML，不覆盖主配置）
- 优先提交 M≤512 的 5 组，确认结果后再决定 M≥1024
- 所有输出归入 `runs/MMDD/`，遵循项目归档约定
- 日志只追加到 `docs/log.md`，不删除历史内容

**输入**:
- `docs/sigma/M_scan_test_plan.md` — 完整测试方案（母配置、shell 脚本、分析脚本）
- `slurm/slm_single.sh` — SLURM 单节点提交模板（需确认路径）
- 项目 `src/` 代码 — 由 `slm_single.sh` 调用 `src/main.py` 执行

**输出**:
- `configs/hall_M{064,128,256,384,512,768,1024,2048}.yaml` × 8 — 各 M 值的独立配置
- `runs/MMDD/hall_ABC_d0.000_M{M}_B100.yaml` × 8 — 运行时存档配置
- `runs/MMDD/hall_ABC_d0.000_M{M}_B100.dat` × 8 — σ_xy(E) 原始数据
- `runs/MMDD/hall_ABC_d0.000_M{M}_B100.png` × 8 — 自动生成的单图
- `test/analyze_M_scan.py` — M 扫描汇总分析脚本
- `runs/MMDD/M_scan_summary.png` — 汇总对比图（σ_xy 叠加 + RMS vs M）

**参考**: `docs/sigma/M_scan_test_plan.md`（完整方案）、`/home/wyl/.agents/memories/kubo-bastin-convergence.md`（KPM 收敛参数）、`../shared/tbplas-internals.md` §9.8 & §12（tbplas Hall 计算清单 + M 发散实测）
