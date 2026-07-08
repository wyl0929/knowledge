<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-11 20:09:34
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-11 20:09:35
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/21_asset_match.md
 * @Description  :
-->
# 21 Asset Match / 资产与缺口匹配

Last updated: 2026-06-11

> 将用户资产与 20_gap_table.md 中的缺口做匹配，评估可行性和缺失资源。

---

## 1. 匹配矩阵

> **注意**：用户已在 `/home/wyl/project/TMBG` 建立完整的 TMBG 紧束缚计算项目。
> 该项目具备: TBG/TMBG 模型构建 (init/rlxd)、TBPM DOS、Haydock LDOS、QE 波函数、对角化能带、
> auto-Δ 扫描配置生成、FWHM/gap 分析管线、集群批量提交。
> 父亲包中的资产匹配以实际代码能力为准。

| 缺口 ID | 缺口简介 | 所需能力 | 用户是否有 | 缺口资源 | 可行性 |
|---|---|---|---|---|---|
| G-T02 | 转角不均匀对平带的定量影响 | TB 模型 + 大超胞无序模拟 | ✅ TMBG 项目已支持 n=472 (~4M 轨道) | 需要无序模型定义 | ⭐⭐⭐⭐⭐ |
| G-T03 | 多层平带的拓扑分类 | TB 模型 + Berry curvature 计算 | ⚠️ TB 有，但 **TBPM 无法算 Berry 曲率**（需 diag）| diag 限 n≤29，大体系需新方法 | ⭐⭐ |
| G-M05 | 大超胞拓扑不变量计算 | 超越 diag 的拓扑方法 | ⚠️ 需探索 (Wilson loop? 实空间 Chern 标记?) | 方法空白 | ⭐⭐⭐ |
| G-M03 | 连续模型 vs TB 在超胞上的桥接 | BM 连续模型实现 + TB + 系统比较 | ✅ TMBG TB 就绪，⚠️ 连续模型在 src/arc/C_*.py 有参考 | 无（轻量） | ⭐⭐⭐⭐⭐ |
| G-M04 | TBPM 在转角体系中的适用性验证 | TBPM + 对角化对比 | ✅ TMBG 项目含对角化能带 | 无（轻量） | ⭐⭐⭐⭐⭐ |
| G-T06 | 位移场在 TB 中的微观实现 | TB 模型 + 层间电势差 | ✅ TMBG model.py 已实现 Δ → top/mid/bot onsite | 需要明确静电模型 | ⭐⭐⭐⭐ |
| G-T07 | 层间耦合参数的多层重整化 | DFT 数据 + TB 拟合 | ⚠️ 缺少 DFT 能力 | 需要 DFT 合作或文献参数 | ⭐⭐⭐ |
| G-T04 | 晶格弛豫的逐层效应 | LAMMPS/DFT + TB | ✅ TMBG 项目已支持 rlxd (LAMMPS 弛豫) 结构 | 需要弛豫数据或工具 | ⭐⭐⭐⭐ |
| G-M02 | 公开基准数据集 | 计算 + 整理 | ✅ | 无（需要时间投入） | ⭐⭐⭐⭐ |

---

## 2. 资产优势总结

| 资产 | 在转角石墨烯中的独特优势 |
|---|---|
| **TMBG 完整项目** (`/home/wyl/project/TMBG`) | 已实现 n=6/29/183/472 建模 + TBPM/LD/QE + auto-Δ 扫描 |
| **TBPM + MPI** | 可算 10⁶–10⁷ atoms → 小角度（θ ~ 0.24°）超胞，对角化无法企及 |
| **YAML 配置系统** | 支持批量参数扫描 (n, Δ, m, rs, ts, dt)，可直接产出相图 |
| **SLURM 集群** | batch_submit.sh 批量提交，参数扫描天然并行 |
| **LAMMPS 弛豫** | rlxd 结构支持，可比对弛豫/未弛豫的差异 |

## 3. 需要补充的缺失资源

| 缺失项 | 重要性 | 获取方式建议 |
|---|---|---|
| Berry curvature / Chern 数计算代码 | 高（拓扑分类需要） | src/arc/berry.py 有参考，整合到主线 (~1天) |
| 连续模型（BM 型）与 TB 一体化比较框架 | 高（G-M03 需要） | src/arc/C_*.py 有参考，整合到主线 (~1天) |
| 转角不均匀模型 | 中（G-T02 需要） | 在现有 TB 模型中引入空间缓变转角分布 |
| DFT 弛豫数据 | 中（精细化需要） | 合作或文献提取 |
| 关联求解能力（DMFT/QMC） | 低（本阶段不必须） | 中长期考虑合作 |

## 4. 推荐行动优先级

```
第一优先级（已有基础，本周可产出）:
  P1: 整合 src/arc/ 连续模型 → 与 TB 能带/DOS 系统对比 (G-M03, G-M04)
  P2: 基于已有 n=183/472 LDOS 数据产出公开基准 (G-M02)

第二优先级（1–2 周内）:
  P3: 在 TMBG TB 模型中引入转角不均匀 → 定量影响研究 (G-T02)
  P4: 小体系 (n=6,29) Berry 曲率计算 → 拓扑随体系大小的标度行为 (G-T03 的缩小版)

第三优先级（1 月内）:
  P5: 位移场微观建模精细化 (G-T06)
  P6: 文献层间耦合参数整理 + sensitivity analysis (G-T07)

需方法创新（中长期）:
  P7: 实空间拓扑标记探索 → 绕过 diag 限制在大超胞算拓扑 (G-M05)
```
