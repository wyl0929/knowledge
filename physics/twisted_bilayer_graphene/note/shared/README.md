<!--
 * @Author       : AI 整理 (三层分离方案)
 * @Date         : 2026-08-31
 * @Description  : note/shared/ — 跨论文复用的共享知识（问题模板 + 答案讲义）
-->

# note/shared/ — 跨论文共享知识

> 三层分离方案（问题模板 → 方法层；答案讲义 → 物理层；论文事实 → 各 review）。本目录放前两层：**论文 review 只保留事实 + 主结果 + 引用本目录的锚点**，不重复写通用物理。

## 目录

| 锚点 | 文件 | 内容 | 复现于（举例） |
|------|------|------|---------------|
| `[PHY-AB]` | `physics/01_ab_interference.md` | AB 双路径干涉、几何相位、谐波、退相干 $e^{-L/L_\phi}$、FFT 峰高、高通滤波 | E10/E12/E15、T15 |
| `[PHY-SDH]` | `physics/02_sdh_landau.md` | SdH/朗道量子化、LK 因子、Landau fan、AB vs SdH 判别 | 几乎所有磁输运论文 |
| `[PHY-MB]` | `physics/03_miniband_network.md` | miniband 驻波量子化、Δn=4/A 域计数、θ² 标度、v_DW 提取 | E12/E14、T9/T12/T15 |
| `[PHY-BERRY]` | `physics/04_berry_vs_ab_phase.md` | Berry 相位 vs AB 电磁相位、valley Chern、sharp 畴壁判据 | 拓扑畴壁类文献 |
| `[PHY-GATE]` | `physics/05_electrostatics_gating.md` | 双栅静电学：Q=CV、n/D 换算、轴映射、共模/差模正交；STM 针尖 vs 平面栅（为何不能独立调 n/D） | 所有双栅输运论文（E10/E12）、STM 论文（E9/E13） |
| `[PHY-FP]` | `physics/06_fp_dimension.md` | FP 驻波、k_F∝n^{1/d} 维度判据、2R_c 抑制、n_1D 换算 | E10、E12（驻波同源）、McDowell 2026 |
| `[PHY-HOF]` | `physics/07_hofstadter_moire.md` | Hofstadter 蝴蝶、moiré 放大、n₂=8/A_MUC 标定 | E10、Chou 2020/2021、Mahapatra 2022 |
| `[PHY-QPI]` | `physics/08_qpi_intervalley.md` | FT-STM / 准粒子干涉（QPI）：q 空间谷内 vs 谷间散射分离、intervalley (√3×√3)R30° 斑判据 | E13、Rutter 2007、Dutreix 2019 |
| `[PHY-EF]` | `physics/09_fermi_level_band_bending.md` | 费米能/化学势 + 局域能带：Dirac/CNP/E_F 区分、计数积分、band bending、局域能带近似、filling factor | E9/E13/E14 谱学与栅控 |
| `[PHY-LB]` | `physics/10_landauer_buttiker.md` | Landauer-Büttiker：散射图景 G=(e²/h)T、通道计数/自旋简并约定、扩散透射 T=N·L0/(L+L0)、量子接触电阻、使用条件（金属区 L≪ξ） | E1/E3/E12 等 1D 通道电导论文 |
| `[PHY-2BAND]` | `physics/11_bilayer_two_component_kink.md` | Bernal 双层 two-component 约化 + EFW（质量 kink）→ LSW（μ 序参量）推广 + kink 零模衰减 λ=√(Uγ⊥)/2ħv + TPH 判据 Eq.(1) 推导 + cont.py 实现核对 | T0 Snyman / T01 Martin / T06 Zhang / T05 San-Jose + DW/cont.py |
| `[METHOD]` | `method/paper_reading_methodology.md`（入口）· `method/experiment_paper_reading.md` · `method/theory_paper_reading.md` | 读文献方法论：入口/公共层（目的层·类型分诊·三层分离·证据分级）+ 实验论文（系统辨识五步 + 4 块模板）+ 理论论文（演绎结构 + 5 块模板），二者互不影响 | **方法层入口** |
| `[METHOD-Q]` | `method/mechanism_questions.md` | 读实验论文的"机制理解提问"模板（机制溯源五问）+ E12 疑问实例 | 阅读方法层（`[METHOD]` §1.2 之②） |

## 引用约定

- 每篇 review 在需要处写 `见 [PHY-AB]` 等锚点，**不复制讲义内容**；只写"本文代入"后的具体数字。
- 讲义文件里：📜Q = 原文事实（附出处）｜💭I = 教科书背景/推断。
- 本目录内容跨 Phase、跨子领域复用；若未来超出 twisted_bilayer_graphene 项目，可提升到 `physics/` 根级。
