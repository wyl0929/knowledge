<!--
Field: 量子霍尔效应
Mode: quick_scan
Domain archetype: science_technical
Created date: 2026-06-10
-->

# 99 Update Log / 更新日志

Last updated: 2026-06-27

## 使用说明

每次新增或修改 living layer 文件，都要在这里记录。不要静默修改 paper registry、gap table、project candidates 或 MVP plan。

Field / 领域：
Maintainer / 维护者：

## Status Tags / 状态标签

- `seed`：来自草稿或已有笔记。
- `skimmed`：快速读过标题、摘要或摘要级材料。
- `parsed`：已经抽取方法、证据和局限。
- `verified`：已对照 primary source 或官方来源核验。
- `archived`：保留历史但不再作为活跃依据。
- `NEEDS_VERIFICATION`：有用但未核验。

## Log / 日志

| Date | File | Change | Reason | Source | Follow-up |
|------|------|--------|--------|--------|-----------|
| 2026-06-10 | field pack | 初始化 `量子霍尔效应`，模式 `quick_scan`，domain `science_technical` | 用户请求 | init_field_pack.py | 按推荐 prompt 填充正文 |
| 2026-06-10 | 10_self_inventory.md | 填充用户背景快照 | 从 default_user_profile.md 和 project 工作区推断 | 工作区 CONTEXT.md / README.md | NEEDS_VERIFICATION: 部分背景信息 |
| 2026-06-10 | 11_term_disambiguation.md | 完成 5 组核心概念区分 + Concept Boundary Contract | quick_scan 要求术语边界清晰 | 领域知识 + TKNN/Haldane/Kane-Mele 文献 | 待用户确认未覆盖的概念 |
| 2026-06-10 | 12_field_map.md | 完成领域地图（6 子方向 + 方法谱系 + 成熟度） | quick_scan 要求建立全貌 | 领域知识 + 综述文献 | 待后续细化为子方向包 |
| 2026-06-10 | 13_actor_map.md | 记录 15+ 研究组谱系 | 帮助用户了解社区格局 | 公开出版信息 | NEEDS_VERIFICATION: 部分组当前人员 |
| 2026-06-10 | 14_paper_registry.md | 记录 20+ 关键论文 + 综述 + 计算文献 | 提供阅读入口 | 公开文献 | NEEDS_VERIFICATION: 部分近期趋势细节 |
| 2026-06-10 | 17_claims_evidence_ledger.md | 建立 7 条中心论断 + Operationalization Contract | Core Claims Gate 要求 | 综合前述文件 | 待用户推进项目时更新操作化状态 |
| 2026-06-10 | 20_gap_table.md | 识别 6 个 gap + 2 个 not-a-gap | 对接项目候选 | 综合 field map + claims | 优先验证 GAP-02/03 的状态 |
| 2026-06-10 | 22_project_candidates.md | 生成 5 个候选项目 + 推荐顺序 | 与用户资产匹配 | 综合 gap + inventory | P1 推荐立刻执行 |
| 2026-06-10 | 00_beginner_guide.md | 生成人话入门指南 | phase_beginner_guide | 综合所有结构化文件 | — |
| 2026-06-10 | 01_research_overview.md | 生成研究总述报告 | phase_summary_overview_report | 综合所有结构化文件 | — |
| 2026-06-10 | 02_frontier_compass.md | 生成边界罗盘 | phase_frontier_compass | 综合 field_map + gaps + projects | 3-6 月后重新评估 |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
| 2026-06-10 | field pack | 初始化 `量子霍尔效应`，模式 `quick_scan`，domain `science_technical`，profile `/home/wyl/.agents/skills/research_onboarding_skill/profiles/default_user_profile.md` | 从模板创建 | init_field_pack.py | 先读取 USER_BRIEF.md，再按推荐 prompt 填充正文 |
| 2026-06-21 | subfields/tbplas_conductivity/ | 新建子方向包 `tbplas_conductivity`，含 README.md + 01_methods_reference.md | 用户请求整理 tbplas 四种电导率计算方法的物理意义与算法简述 | `tbplas-internals.md` §9–§12 | 后续可细化为 Kubo-Bastin 数值稳定性专项或 Lindhard ω→0 外推方案 |
| 2026-06-21 | subfields/tbplas_conductivity/01_methods_reference.md | 源码审计修正 + 大幅扩充 | 对照 tbplas-alpha 实际 Python/C++ 源码核验正确性 | `solver.py`, `analysis.py`, `config.py`, `lindhard.py` (tbplas-alpha conda env) | 修正了返回类型、调用方式、参数默认值；新增 §6 TBPM/Diag 双路径动态极化率、§7 TBPMSolver 全部方法清单 |
| 2026-06-21 | subfields/tbplas_conductivity/02_kubo_bastin_deep_dive.md | 新建 Kubo-Bastin C++ 核心深度解析 | 用户请求详细检查 C++ 核心并解释 M>512 发散问题 | `kubo_bastin.h`, `solver.h`, `kpm.cpp`, `chebyshev.h`, `fermi_dirac.h` (tbplas-cpp-a021ca8) | 确认根因为 double 精度两路三项递推正交性丢失；fermi_dirac() 使用 f(E) 而非 -df/dE 待验证 |
| 2026-06-21 | subfields/tbplas_conductivity/02_kubo_bastin_deep_dive.md | 对照 Yuan 2016 (PRB 94.195434) 更新 | 用户指示阅读 Yuan 2016 论文并更新文档 | Yuan 等 (2016), PRB 94, 195434 | 新增文献参数基准表（M=15000）；f(E) 因子经 Yuan 2016 Eq.12 交叉验证通过；§5 三方对比表（García 2015 / Yuan 2016 / tbplas） |
| 2026-06-21 | subfields/tbplas_conductivity/02_kubo_bastin_deep_dive.md | 🔴 重大修正：NaN 根因从"Chebyshev 稳定性"改为"rescale 误配" | 用户确认 NaN 由 rescale 参数导致（rescale=9.0 < 半带宽 ~10 eV） | MG 0621 实测：rescale=-1 下 M≤1024 NaN=0 | 重写 §3.3（两种数值问题）、§5（对比表）、§6.2（M 扫描表）、§7（根因总结）；M≥4096 表现为基线偏移而非 NaN |
| 2026-06-21 | subfields/tbplas_conductivity/03_M_scan_test_plan.md | 新建 Kubo-Bastin M 发散测试方案 | 用户请求单层石墨烯 Hall M 扫描的详细测试方案 | MG 项目 `calc.py`, `config.yaml`, `slm.sh` | 含 8 组 YAML 配置生成脚本、批量 SLURM 提交、结果分析 Python 脚本、预期 RMS vs M 对照表 |
| 2026-06-26 | subfields/tbplas_conductivity/02_kubo_bastin_deep_dive.md | 🔴 重大修订：H_F 干净极限条件收敛假说 | 用户新发现——高阶 Γ×μ 贡献不收敛，有限 η 可压制；跨论文交叉验证 García 2015 的无序参数 | KPM 标准理论 (Weiße et al. RMP 2006) + García 2015 原文 (γ=0.1t) + Yuan 2016 (未讨论 η/disorder) | §1.2 数值关键完全重写（条件收敛分析）；§3.4 纠正 García 成功归因（无序 > 精度）；§3.5 新增 E4 收敛性分析 + H_F 假说详述；§5 结论更新；§7 完全重写（含 F1–F3 检验方案） |
| 2026-06-26 | subfields/tbplas_conductivity/02_kubo_bastin_deep_dive.md | 新增 Anderson 无序的指数阻尼效应分析 | 解释 García 2015 用 M=6144 无发散的真正原因 | García 2015 (γ=0.1t, N=2×128×1024) | 无序使 μ_n ∼ e^{-γn/ΔE} → M_eff ∼ 70，超此阶数后物理上为零 |
| 2026-06-27 | subfields/tbplas_conductivity/chebyshev_precision/ | 新建子方向 field pack：切比雪夫迭代浮点精度问题 | subfield_onboarding 路线，系统化记录 Phase A–M (06-22~27) 全链路根因诊断 | user memory (kubo-bastin-convergence.md), shared/tbplas-internals.md §12.3, gamma_mu_sim 项目 | 含 12 个文档：USER_BRIEF, beginner guide, overview, frontier compass, self inventory, term disambiguation, field map, claims ledger, gap table, project candidates, QA, update log |
