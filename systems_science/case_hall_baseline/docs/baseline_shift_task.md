<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-22 00:55:52
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-22 01:00:34
 * @FilePath     : /MG/docs/sigma/baseline_shift_task.md
 * @Description  : 基线偏移下一步测试任务（按 baseline_shift_plan.md §4.3）
-->

# 基线偏移验证 — 后续任务

> 父计划: `docs/sigma/baseline_shift_plan.md` §4.3

---

### [x] AI: 0622_0100_T1 — rs=16 完成检查与汇总

**父计划**: `baseline_shift_plan.md#4.3` (优先级 1)

**目标**: 确认 rs=16 作业 (Job 283661) 完成，下载数据，将所有 rs 数据点（1/2/4/8/16）汇总为最终 rs 标度曲线。

**背景**: T2 rs 扫描已获 rs=1/2/4/8 四点，均显示 rs≥2 后偏移饱和（S≈-685~-730）。rs=16 为最终确认点。

**执行步骤**:
1. 检查 Job 283661 状态，确认 exit 0
2. scp 下载 `hall_m512_M4096_rs16_B100.0.{txt,png}` 到 `runs/0621/`
3. 运行 Python 分析：提取 rs=16 偏移量 S，与 rs=1/2/4/8 对比
4. 若 S ≈ -685~-730 → 确认饱和；若 S 显著偏离 → 重新评估

**成功判据**:
- [ ] Job 283661 exit 0，数据完整
- [ ] rs=16 偏移量在 [-650, -750] 范围（饱和确认）或记录偏差
- [ ] 更新 `baseline_shift_plan.md` §3.2 的 rs=16 行

**约束**: 单节点，仅下载+分析，不提交新作业

**输入**: 集群 `runs/0621/hall_AB_d0.000_m512_shift_rs16_B100.0.txt`

**输出**: 更新后的 rs 标度表 + `baseline_shift_plan.md`

---

### [x] AI: 0622_0100_T2 — m=128 M=4096 补充 T3 数据点

**父计划**: `baseline_shift_plan.md#4.3` (优先级 2)

**目标**: 测试 m=128 超胞在 M=4096 下的基线偏移，与已有 m=256/512 数据共同拟合 m 标度律。

**背景**: 当前仅 m=256 (S=-234) 和 m=512 (S=-684) 两个点，无法可靠确定 S(m) 标度。

**执行步骤**:
1. 生成 YAML `configs/hall_m128_M4096.yaml`（m=128, M=4096, rs=8, 其余同 M 扫描模板）
2. scp 上传 + `sbatch --job-name=hall_m128_M4096 slurm/slm_single.sh`
3. 等待完成（预计 ~15min，单节点）→ 下载数据
4. 计算 S(m=128)，与 m=256/512 三点拟合 S ∝ m^p

**成功判据**:
- [ ] YAML 正确生成（tag=`m128_M4096`，输出无覆盖）
- [ ] Job exit 0, 数据完整
- [ ] 三点拟合的 p 值（S ∝ m^p）有明确物理含义

**约束**:
- 单节点 `slm_single.sh`
- 不覆盖已有 m=256/512 数据
- 环境: `conda activate tbplas-alpha`

**输入**: `configs/hall_m128_M4096.yaml`（待生成）

**输出**: `runs/MMDD/hall_AB_d0.000_m128_M4096_B100.0.{txt,png}`

---

### [x] AI: 0622_0100_T3 — M=3072 精确定位 M_c 阈值

**父计划**: `baseline_shift_plan.md#4.3` (优先级 3)

**目标**: 在 m=512 下测试 M=3072，确定基线偏移发生的精确临界 M_c ∈ [2048, 4096]。

**背景**: M=2048 偏移 ≈ 0, M=4096 偏移 ≈ -685。M=3072 正好位于中点，可判断偏移是突然跳变还是存在过渡区。

**执行步骤**:
1. 生成 YAML `configs/hall_m512_M3072.yaml`（m=512, M=3072, rs=8）
2. scp 上传 + `sbatch --job-name=hall_m512_M3072 slurm/slm_single.sh`
3. 等待完成（预计 ~1.5h）→ 下载数据
4. 提取偏移 S(3072)，与 S(2048)=0, S(4096)=-685 对比

**成功判据**:
- [ ] Job exit 0, 数据完整
- [ ] S(3072) 在 [0, -685] 范围内——若 ≈ 0 则 M_c > 3072；若 ≈ -685 则 M_c < 3072；若为中间值则存在过渡区

**约束**: 单节点，约 1.5h，环境 `tbplas-alpha`

**输入**: `configs/hall_m512_M3072.yaml`（待生成）

**输出**: `runs/MMDD/hall_AB_d0.000_m512_M3072_B100.0.{txt,png}` + M_c 区间约束

---

### [x] AI: 0622_0100_T4 — m=1024 M=4096 检验 H₁ (M_c ∝ N_orb)

**父计划**: `baseline_shift_plan.md#4.2` (H₁: $M_c \propto N_{\text{orb}}$)

**目标**: 测试 m=1024 超胞在 M=4096 下是否出现基线偏移，验证 H₁ 的核心预测——更大体系推迟偏移阈值。

**背景**: H₁ 预测 $M_c \propto N_{\text{orb}}$。已有数据：
- m=256 (N_orb~393k): M=4096 时 S=-234（已偏移）
- m=512 (N_orb~1.57M): M=4096 时 S=-685（已偏移）

若 H₁ 成立，m=1024 (N_orb~6.3M，~16× m=256) 的 $M_c \approx 16000$，则 M=4096 **不应产生偏移**。这是判别 H₁ 的关键实验。

**执行步骤**:
1. 生成 YAML `configs/hall_m1024_M4096.yaml`（m=1024, M=4096, rs=8）
2. scp 上传 + `sbatch --job-name=hall_m1024_M4096 slurm/slm.sh`（⚠️ 4 节点 MPI）
3. 等待完成（预计 ~3-5h）→ 下载数据
4. 提取 σ(1eV) 和偏移 S，若 S≈0 → 支持 H₁；若 S≈-685 → M_c 与 N_orb 无关

**成功判据**:
- [ ] YAML 正确生成（tag=`m1024_M4096`）
- [ ] Job exit 0，数据完整（排除 node30/56-59 C++ 节点）
- [ ] 偏移 S 用于 H₁ 判别

**约束**:
- **4 节点 MPI** (`slurm/slm.sh`)，排除 `node[28-31,41-64]`
- m=1024 轨道数 ~6.3M，需确认排除列表不影响作业调度
- 环境: `conda activate tbplas-alpha` + `TBPLAS_CORE_PATH`

**输入**: `configs/hall_m1024_M4096.yaml`（待生成）

**输出**: `runs/MMDD/hall_AB_d0.000_m1024_M4096_B100.0.{txt,png}` + H₁ 判别结论
