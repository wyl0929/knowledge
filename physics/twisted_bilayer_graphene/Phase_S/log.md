<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-19 17:01:52
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-19 17:04:34
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/Phase_S/log.md
 * @Description  : Phase S AI 执行日志（run-task 追加，最新在最前）
-->
<a id="ai-0820-T05"></a>

## AI: 0820_T05 - note/ 目录重构 + bl-dw 统一迁移

执行用户指令: note/ 笔记命名分类重构（快速索引方案），同步修改 Phase S 文档引用，并将 bl-dw 的文献与笔记迁入 twisted_bilayer_graphene 统一管理。

**变更**:
- `note/` 原 7 个子目录（fundamental_theory/helical_network/network_theory_advanced/new_directions/mTBG_experiments/non_twisted_experiments/new_platforms）→ 4 个（theory/experiments/reviews/structure）；60 篇 review 全部改名为 `paper_review_{ID}_{authorYYYY}_{journal}.md`（两位 ID）
- 新建 `note/index.md` 总索引（64 行，含 ID/作者/年份/关键词/标签/路径）
- bl-dw: 独有 4 篇（E01/E03/E07/E17）迁入 `note/experiments/`；与 note 重复的 7 篇归档至 `archive/bl-dw/`（主副本为 Phase S QC 版）；3 个 PDF 与 `reference/pdfs/` 重复（Hou/Ju md5 相同、Zheng 为 6 页节选版）已删；bl-dw 留 README.md 指针
- Phase S 文档（plan/tasks/cards/appendix_A/appendix_B）中旧目录名与旧文件名引用全部替换为新路径；review 头部 `Phase_S/cards/*.md` 死链接改为 `cards.md`

**验证**: 引用可达性脚本检查 pass（目录级通配符引用除外）；`ls note/theory` = T01–T39 按 ID 排序。

---

<a id="ai-0820-T04"></a>

## AI: 0820_T04 - S-REV 逐篇修订 23 篇理论 review 的无源内容

执行任务 **S-REV**：按 `appendix_B_theory.md` §B.5 的 35 条更正日志，逐篇修订 23 篇理论 review 中被证伪/无源的数字与机制表述，每篇补证据分级并追加末尾「更正日志」节。所有替换文本均经 `reference/pdfs/` pdftotext + grep 复核（23 篇 PDF 全部重新提取至 /tmp/q2pdfs）。

**涉及文件**（23 篇 review 更新，每篇末尾新增更正日志节）：

| 文件 | 修订要点（依据 §B.5 条目） |
|------|------|
| `note/fundamental_theory/paper_review_martin2008_prl.md` | #9: 4e²/h 标 💭I⚠️；Q2 删除 "ℤ₂/ΔC_v=2" 语言 → 原文 "topological vacuum charge" 📜Q |
| `note/helical_network/paper_review_efimkin2018_prb.md` | #1: 能带能标 ε_L=2πħv/L（72 meV）与 DoS 周期 ε_L/3（20 meV）分开表述，修正 §4.2/§8 |
| `note/helical_network/paper_review_hou2020_prb.md` | #2: review 本已用"半金属"表述，仅登记更正日志 |
| `note/helical_network/paper_review_tsim2020_prb.md` | #13: "S 矩阵对角" → 置换型确定性散射（mode 1↔2 于 ∓120°），修正 §3.2/§8 |
| `note/helical_network/paper_review_fujimoto2021_prb.md` | #14: review 无 AB 无源句，仅登记卡片侧修正 |
| `note/helical_network/paper_review_debeule2021_prb.md` | #15: "周期踢动（kick）" → 周期驱动 Floquet（grep kick=0） |
| `note/helical_network/paper_review_margetis2021_prb.md` | #16: review 无 Ju/Jiang 归属句，仅登记（原文引 Sunku/Ni 2020） |
| `note/network_theory_advanced/paper_review_T22.md` | #21: 非均匀应变/赝磁场/0.1%/nm/~100T 删除 → 层内单轴应变 + ε_c≈4.4%/8%；删 "~0.01% 控制精度" |
| `note/network_theory_advanced/paper_review_T24.md` | #22: S(θ) 参数化整段虚构删除 → 相互作用量子线 + 广义 Umklapp → 分数填充关联态 |
| `note/network_theory_advanced/paper_review_T25.md` | #23: Fano 术语删除（grep=0）→ 共振反共振 dip；删 "~3 nm"；机制改 AA 离散能级 + 能量依赖 S 矩阵 |
| `note/network_theory_advanced/paper_review_T26.md` | #33: K<1/K>1、Tc 10–50 K、CDW 开隙、维度渡越删除 → 玻色化模型 + 偏压/屏蔽/介电调控 + 声子相图；补 CDW/SDW 与 WB 奇异性 📜Q |
| `note/network_theory_advanced/paper_review_T27.md` | #24: "≳0.05%" 删除 → 均匀异质应变单独不足、需原子重构（grep "not sufficient" ✓）；算例 1%/4%；界面宽 4.5/9.1 nm |
| `note/network_theory_advanced/paper_review_T28.md` | #34: ~5-15°/~6°/~10° 删除 → θ_c=38.21°；删 "1 nm vs 5 nm"/"圆偏振"；补 Haldane/Semenoff 子谷质量 |
| `note/network_theory_advanced/paper_review_T29.md` | #3: t_inter≈0.05t、G≈0.8–0.95×N、平台 ~0.1 eV 删除 → NQCP 平台接近 1/2/3（单位 2e²/h）+ θ=0.82° 接近 2；"弱耦合"标 💭I⚠️；补 Rickhaus 引用 📜Q、Xu 对标标 💭I⚠️ |
| `note/network_theory_advanced/paper_review_T30.md` | #25: QSH/Z2/自旋-谷锁定/λ_I 1–5 meV 删除 → 仅 Rashba SOC：磁电导缩减 + 尖锐共振 + 自旋极化；α_R≈15 meV |
| `note/network_theory_advanced/paper_review_T32.md` | #26: 量子度规删除 → 谷欧拉数 VEN（Euler 曲率、I_ST 对称）ZBC QVHE；候选 h-BAs/h-BP |
| `note/new_directions/paper_review_T33.md` | #27: "zigzag ~2-4 支/谷" 删除 → 电导接近电导量子 + 非局域电阻（θ=1.696°） |
| `note/new_directions/paper_review_T34.md` | #28: 孤子角约定写反修正（φ=0° tensile/90° shear）；删 ~50–200 meV、shear 最强 → 两主峰连续抑制/增强、压强加倍峰能 |
| `note/new_directions/paper_review_T35.md` | #4/#5: ~6°/~10°/~13° 删除 → θ=21.8°（13.8°/22.79°）；删 10–50 meV → 2 meV 能标 + Δ_s=15 meV；删 "1.1° 魔角" 比较 |
| `note/new_directions/paper_review_T36.md` | #29: I_c 锯齿/ZBCP/Majorana 删除 → 三条 DW 工程策略（AB→Fraunhofer 复现 Barrier 2024、Josephson 二极管、超流分流） |
| `note/new_directions/paper_review_T37.md` | #30: mTBG → 大转角 tBLG 实验+模拟；删 20–50 meV/10 nm/DFT 一致/推广 → 隐腔体定位 + 磁输运区分腔模/全局共振；删 Xu 对标 |
| `note/new_directions/paper_review_T38.md` | #31: Little-Parks 删除（grep=0）→ 有限尺寸环 + 约束效应，SC 标度维数对隧穿强度不敏感 → 与无限尺寸定性失配 |
| `note/new_directions/paper_review_T39.md` | #32: 谷过滤 100%/∝N 删除 → 不可穿透势垒（两谷皆阻）+ 谷间相互作用为"阀" + SNS' 超流需谷间混合；删 Barrier 对标 |

**变更说明**:
- 每篇仅删改被 §B.5 证伪/无源的内容，已 📜Q 核对通过部分未动
- 修订后数字均 grep 到原文（📜Q）或显式标 💭I⚠️；跨论文对标（Xu 2019 等）逐条核原文引用列表
- 修订文本与 `cards.md` Q2 节（已回写）及 `appendix_B_theory.md` §B.5 三方一致

**成功判据验证**:
- [x] 23 篇全部修订完成（fundamental_theory 1 + helical_network 6 + network_theory_advanced 9 + new_directions 7）
- [x] 每篇末尾有「更正日志」节（grep 复核 23/23 ✓）
- [x] 无源数字清零: 扫描 "0.05t / 0.8–0.95 / 0.1 eV / 3 nm / Fano / 0.05% / 0.1%/nm / 100T / Little-Parks / 锯齿 / ZBCP / kick / 10–50 meV / ~6°·~10°·~13°" 等全部仅存于更正日志条目
- [x] 与 cards.md / appendix_B §B.5 无冲突（修订文本逐条对照 §B.5 条目号）

---

<a id="ai-0820-T03"></a>

## AI: 0820_T03 - 附录 B 正文清理（弃用内容统一登记于 §B.5）

按用户要求清理 `appendix_B_theory.md` 正文：删除所有 "⚠️ review 旧版…已弃/见 §B.5" 类弃用注记（T9/T11/T13/T22–T39 共 20 处），正文只保留 📜Q/💭I⚠️ 证据分级后的干净表述；全部修正统一登记于 §B.5（35 条更正日志）。

**涉及文件**：

| 文件 | 操作 | 说明 |
|------|------|------|
| `Phase_S/appendix_B_theory.md` | 更新 | 20 处弃用注记删除；同步修正未核实表述: T29 "弱耦合/两个极限" → "独立传播 + NQCP"（B.2 节点、B.3 表、B.4 表、B.1.1 总览四处）；T31 增补 $J_c\sim1/N_l$ 衰减（📜Q）；T6 Ju/Li 对标补 💭I⚠️ 分级；§B.5 第 11 条加注（当时状态） |
| `Phase_S/log.md` | 更新 | 本条目 |

**验证**: 正文（§B.5 之前）grep "review 旧版/已弃/见 §B.5" 无残留（仅 QC 声明头部的指针性引用保留）；弃用内容全部集中于 §B.5 更正日志。

<a id="ai-0820-T02"></a>

## AI: 0820_T02 - 第三批 T26/T28/T31 PDF 核对（用户补齐最后三篇）

用户补齐最后 3 篇理论 PDF（T26 Wang & Hsu、T28 Mondal、T31 Kundu & Kundu）。pdftotext 提取后逐数字 grep 核对，至此 **39 篇理论卡片全部完成 PDF 反向核对**。

**涉及文件**：

| 文件 | 操作 | 说明 |
|------|------|------|
| `Phase_S/appendix_B_theory.md` | 更新 | QC 声明 36→39 篇；T26/T28/T31 节点三要素重写并升 pdf✓；B.3 三行重写；§B.5 新增第 33–35 条 |
| `Phase_S/cards.md` | 更新 | Q2 头部声明（39 篇全部核对）；T26/T28 卡片重写 |
| `Phase_S/log.md` | 更新 | 本条目 |
| `Phase_S/plan.md` | 更新 | §2.6.1 追加执行路径 |

**关键发现**:
1. T26 (Wang & Hsu, 2D Mater. 11, 035007): 补文章号；review "Tc~10–50 K"、"CDW 开隙→电阻陡增"、"K<1 吸引/K>1 排斥" 无源 → 原文为玻色化 TLL 模型 + 屏蔽相互作用可调 + 密度波/超导相图 📜Q
2. T28 (Mondal): review "~6°/~10°"、"~1 nm vs ~5 nm"、"圆偏振光读出" 无源 → 原文算例 θc=38.21°、子谷 Dirac 锥（Haldane/Semenoff）、非费米液体、电场/层滑动调控 📜Q
3. T31 (Kundu & Kundu): review "Fraunhofer 偏离 + AB 叠加"、"Ic ∝ 畴壁数目" 无源 → 原文 zigzag→4π 周期 Jc、pLL→体 Jc 消失（边缘 4π 响应）、锯齿→正弦 4π 转变、Jc~1/N_l 衰减 📜Q

**里程碑**: Q2 理论部分（39 卡片 + 附录 B + 更正日志 35 条）PDF 反向核对全部完成。剩余待办: 12+3 篇 review 文件（含 T29/T35）的无源内容逐篇修订；之后可启动 S-REP-3（report §3 初稿）。

**Plan Feedback**: 🟡 需补充 — 已追加 §2.6.1 执行路径记录。

<a id="ai-0820-T01"></a>

## AI: 0820_T01 - 第二批 12 篇理论 PDF 反向核对并更新附录 B（用户补齐 PDF）

用户补齐 12 篇理论论文 PDF（T22/T24/T25/T27/T30/T32/T33/T34/T36/T37/T38/T39）。pdftotext 提取后逐数字 grep 核对，发现 review 层存在**整组机制误解与无源数字**，已重写 appendix_B 对应节点与 cards.md 对应卡片。

**涉及文件**：

| 文件 | 操作 | 说明 |
|------|------|------|
| `Phase_S/appendix_B_theory.md` | 更新 | QC 声明 24→36 篇；12 节点三要素重写并升 pdf✓；B.3 表 12 行重写；mermaid T25/T27 标签；§B.5 新增第 21–32 条 |
| `Phase_S/cards.md` | 更新 | Q2 头部声明 24→36 篇；T22/T24/T25/T27/T30/T32/T37/T39 卡片修正 + 📜Q |
| `Phase_S/log.md` | 更新 | 本条目 |
| `Phase_S/plan.md` | 更新 | §2.6.1 追加执行路径 |

**关键发现（新失败模式: review 整段机制虚构）**:
1. T24 (Hsu 2023): review 的 "S(θ) 参数化、θ=0/π/2 连接 T9/T12、Peierls 磁场调控" 整段无源 → 实为相互作用量子线 + 广义 Umklapp 散射
2. T30 (Wittig 2024): "QSH/Z2=1/自旋-谷锁定/λ_I 1-5 meV" 无源 → 原文只含 Rashba SOC
3. T32 (Ghadimi 2024): "量子度规" → 实为谷欧拉数 VEN
4. T39 (Phong 2026): "谷过滤 ~100%/电场开关" → 实为畴壁不可穿透势垒 + 谷间相互作用充当阀
5. T36 (Du 2025): "ZBCP/Majorana" → 实为三条 DW 工程策略（AB→Fraunhofer 复现 Barrier 2024 等）
6. T37 (McDowell 2026): 是实验+模拟论文、大转角（非 mTBG）；"moiré 势 20-50 meV/DFT 一致" 无源
7. T34 (Wen 2024): 孤子角约定写反（0°=tensile/90°=shear）；"50-200 meV" 无源 → 压强可加倍峰能
8. T27 (Georgoulea 2024): 均匀异质应变**单独不足以**产生通道，需原子重构；"≳0.05%" 无源（原文 1%/4%）
9. T22 (Sinner 2023): "应变梯度 0.1%/nm、赝磁场 100 T" 无源 → 层内单轴应变 + mBZ 变形，ϵ_c≈4.4%/8%
10. T25/T33/T38: Fano 术语/~3 nm、"zigzag 2-4 支/谷"、Little-Parks 均无源已弃

**仍缺 PDF 的 3 篇**: T26 (Wang & Hsu)、T28 (Mondal)、T31 (Kundu & Kundu)——已全目录检索确认不在 `reference/pdfs/`，B.3 表撤除其 pdf✓ 标记，数字继续 💭I⚠️。

**待办**: 12 篇 review 文件（含此前 T29/T35）的无源内容待逐篇修订；用户若能提供 T26/T28/T31 PDF 可继续核对。

**Plan Feedback**: 🟡 需补充 — 已追加 §2.6.1 执行路径记录。

<a id="ai-0819-T04"></a>

## AI: 0819_T04 - Q2 理论卡片 PDF 反向核对回写（用户确认）

用户确认将 appendix_B §B.5 的 QC 发现回写 cards.md，并要求将 Q2 理论部分按 PDF 原文系统性重新验证。对 24 篇有 PDF 的理论卡片逐条 grep 原文核对，除 §B.5 既有 12 条外新增 8 条发现（合计 20 条），全部回写 cards.md；同步修正 appendix_B_theory.md 与 review_T23.md。

**涉及文件**：

| 文件 | 操作 | 说明 |
|------|------|------|
| `Phase_S/cards.md` | 更新 | Q2 头部加核对声明；T1/T3/T6/T9/T11/T12/T13/T15/T18/T19/T21/T23/T25/T26/T27/T29/T35 修正 + 📜Q/💭I⚠️ 分级；Q3 表 T13/T22/T23/T27 行修正 |
| `Phase_S/appendix_B_theory.md` | 更新 | T23 作者/年份（Moulsdale 2024）、T9 S 矩阵对称性、T13/T18 表述；§B.5 补第 13–20 条并标注回写状态 |
| `note/network_theory_advanced/paper_review_T23.md` | 修正 | 作者序（Moulsdale 第一作者）、期刊（Academia Nano 1, 2024）、删“势阱 10–20 meV”无源数字、“解释 Zheng 2022”降级 💭I |
| `Phase_S/tasks.md` | 更新 | S-APP-B 附加产出注记 → 已回写 |
| `Phase_S/plan.md` | 更新 | §2.6.1 追加 T04 执行路径 |

**新增发现（§B.5 第 13–20 条）**:
- T12 “S 矩阵是对角的”不符原文（置换型确定性散射 ±120°）→ 已改
- T13 “AB 振荡来源于规范场周期”无源（原文全文无 AB 振荡讨论、未引 Xu/Rickhaus）→ 已删；Q3 年份 2020→2021
- T18 “1D 周期踢动”不符（原文为周期驱动 Floquet 映射）→ 已改
- T21 “为 Ju 2015/Jiang 2017 提供框架”无源（引用列表无这两篇）→ 已改一般化
- T23 第一作者为 Moulsdale（非 Enaldiev）、期刊 Academia Nano 2024;1；“解释 E14 (Zheng 2022)”无源（grep “Zheng” 无命中）→ 降级 💭I⚠️
- T27 “第三种机制”与 T22 重复计数 → 实为第四种
- T22 Q3 表年份 2022→2023；E18 对标为 2026 论文非原文引用 → 标 💭I⚠️

**核对通过**（📜Q）: T3 “N 1D kink state branches per valley” 与 armchair 取向论断、T6 ΔN_ν=±2 与补偿壁完全 gapped、T15 原文引用 Rickhaus [29]/Xu [30]、T19 “non-Fermi-liquid resistivity”、T29 “propagate independently”/NQCP 1/2/3。

**待办**: review_T29.md（t_inter≈0.05t、0.8–0.95×N、0.1 eV 三处无源数字）与 review_T35.md（转角列表、能隙）待修订；无 PDF 的 15 篇（T22、T24–T28、T30–T34、T36–T39）待补 PDF 后复核。Q1 侧 T01 遗留项（E4 “无磁场”、E10 dG/dV、E11 STEM/~5 nm、E15 “唯一”等）仍未回写 cards.md，建议另行处理。

**Plan Feedback**: 🟡 需补充 — 已追加 §2.6.1 执行路径记录。

<a id="ai-0819-T03"></a>

## AI: 0819_T03 - 组装 appendix_B 理论谱系演进树（S-APP-B）

执行 tasks.md 任务 S-APP-B：从 cards.md Q2 节（T1–T39）+ 38 篇理论精读组装理论解释谱系演进树，写入 `Phase_S/appendix_B_theory.md`（458 行，3–4 页）。含 §B.1 四时代总览 + mermaid 演进树、§B.2 四时代 39 节点详解（每个节点含核心假设/关键预言/已知局限三要素）、§B.3 三要素速查表、§B.4 三类关系（继承/推翻/并存）标注汇总、§B.5 QC 更正日志。

**涉及文件**：

| 文件 | 操作 | 说明 |
|------|------|------|
| `Phase_S/appendix_B_theory.md` | 新建 | 附录 B 全文（T1–T39 全覆盖） |
| `Phase_S/tasks.md` | 更新 | S-APP-B: ⬜ → [x]，成功判据全勾，追加完成记录 |
| `Phase_S/log.md` | 更新 | 本条目 |
| `Phase_S/plan.md` | 更新 | §2.6.1 追加 T03 执行路径；§三 交付物表 A/B 行 ⬜ → ✅ |

**成功判据验证**:
- [x] T1–T39 全部 39 张卡片覆盖（grep 验证 39 个 ID 全部出现；T8 为 Q3 映射表条目、T31 为 registry scope-out 条目，均已注明）
- [x] 每节点含假设/预言/局限三要素（§B.2 详解 + §B.3 速查表双形式）
- [x] 演进树含继承/推翻/并存三类关系标注（mermaid 边标签 + §B.4 汇总表）
- [x] QC: 全部数字带 📜Q/💭I⚠️ 分级，无未标注数字

**QC 反向核对（用户要求验证真实性）**: 24 篇理论 PDF（`reference/pdfs/`）pdftotext 后逐数字 grep，发现 6 处卡片/精读错误（详见附录 §B.5）:
1. T9 卡片 "E_λ = 2πħv/3λ" 不精确 → 原文能带能标 ε_L = 2πħv/L（θ=0.245° 时 ≈72 meV），DoS 周期为其 1/3
2. T11 卡片 "金属性网络" → 原文 "semimetallic with Dirac dispersion"（半金属）
3. T29 精读三处无源数字: "t_inter≈0.05t"、"G≈0.8–0.95×N·2e²/h"、"平台宽度~0.1 eV" → 原文为 NQCP 接近 1/2/3 × 2e²/h
4. T35 精读 "~6°/~10°/~13°" 与 "能隙 10–50 meV" 无源 → 原文 θ=21.8°
5. T23 精读 "势阱深 10–20 meV" 无源 → 原文 10/20 meV 是层间不对称势 Δ 取值
6. T26/T27 出版年份 cards 写 2023 → review 标 2024

**核对通过的数字**（📜Q 级）: T1 每谷每自旋 2 零模、T5 88 meV·θ(deg) 与 45 meV 阈值、T6 ΔN_ν=±2 与补偿壁无模、T9 ε_L 与 DoS 周期、T12 双窗口/独立 zigzag 模、T15 φ=0/π/2 两极限、T29 NQCP 1/2/3、T35 θ=21.8°。

**无 PDF 的 15 篇**（T22、T24–T28、T30–T34、T36–T39）: 全部数字降级 💭I⚠️（精读层），附录与 report 正文不得引用其量化数字；待补 PDF 后可复用 S-APP-A 流程升格。

**Plan Feedback**: 🟡 需补充 — 任务结果与 plan §三 交付物清单一致，QC 发现为新增信息，已追加 §2.6.1 实际执行路径记录；交付物表 A/B 行状态标记更新为 ✅。
<a id="ai-0819-T02"></a>

## AI: 0819_T02 - E5/E6/E8 补 PDF 后核对并修正（用户补传 PDF）

用户补传 E5（Li 2016 corrugation）/E6（Jiang 2017）/E8（Hsu 2020）三篇 PDF 至 `reference/pdfs/`。pdftotext 提取后逐数字 grep 核对，发现旧 review 存在**整组虚构/误读数字**，已修正三个 review、cards.md 对应卡片、appendix_A §A.1 行与 §A.5。

**涉及文件**：

| 文件 | 操作 | 说明 |
|------|------|------|
| `note/non_twisted_experiments/paper_review_E5.md` | 修正 | 加证据分级 + 反向核对 pass + 更正日志（3 nm/50 nm 为标尺与图尺寸误读；gap≈170 meV 由 Rh 箔有效电场诱导；样品为 CVD/Rh 箔非机械剥离；孤子宽 ~10 nm；77 K） |
| `note/non_twisted_experiments/paper_review_E6.md` | 修正 | 删虚构数字（反射率 5-15%、λp 100-200 nm、分辨 20 nm、10.6 μm、仅 D≠0）；实为 λ=11.2 μm、壁宽 6-10 nm、反射系数 r 定性结果（拉伸壁幅值大近虚数/剪切壁小近实数）、单底栅无 D 控制 |
| `note/non_twisted_experiments/paper_review_E8.md` | 修正 | 赝磁场 ~100-300 T → 最高 ~800 T（部分区 ~600 T）；纳米压痕 → architected 纳米结构；单层石墨烯；删 0.1%/nm 与 0.5% 不可逆（原文无） |
| `Phase_S/cards.md` | 更新 | E5/E6/E8 卡片重写（带 📜Q 与 ⚠️ 修正注记） |
| `Phase_S/appendix_A_methods.md` | 更新 | 三行升 pdf✓ 并替换为核对后数据；§A.5 #9 拆为 #9/#10/#11；头部 PDF 计数 17→20 |

**关键发现（新增 QC 失败模式）**: ① 标尺/图像尺寸误读为物理量（E5: "3 nm" 是原子分辨图标尺、"50 nm×40 nm" 是 STM 图像尺寸）；② 整组虚构测量数值（E6 的 5-15%/100-200 nm/20 nm 原文不存在）；③ 样品/方法张冠李戴（E5 机械剥离→CVD/Rh 箔；E8 纳米压痕→图案化纳米结构、且为单层石墨烯）；④ 数值系统性低估（E8 赝磁场 100-300 T → 800 T）。已固化到 `/memories/literature-review-qc.md`。

**待办**: E2（Shimazaki 2015）仍无 PDF，"圆偏振光" 待核；E5 期刊发表状态待查（arXiv:1609.03313）。

<a id="ai-0819-T01"></a>

## AI: 0819_T01 - 组装 appendix_A 实验方法横向对比表（S-APP-A）

执行 tasks.md 任务 S-APP-A：从 cards.md Q1 节 + 16 篇已有精读组装实验表征方法横向对比表，写入 `Phase_S/appendix_A_methods.md`（~210 行，3–4 页）。额外完成用户要求的卡片真实性核查：17 篇论文的 PDF 原文（`reference/pdfs/`，pdftotext 提取）逐一 grep 核对关键数字。

**涉及文件**：

| 文件 | 操作 | 说明 |
|------|------|------|
| `Phase_S/appendix_A_methods.md` | 新建 | 附录 A 全文（§A.1 四张对比表 / §A.2 四类技术说明 / §A.3 边-体区分策略 / §A.4 演进 / §A.5 更正日志） |
| `Phase_S/tasks.md` | 更新 | S-APP-A: ⬜ → [x]，成功判据全勾，追加完成记录 |
| `Phase_S/log.md` | 新建 | 本日志文件（后续 run-task 追加） |

**成功判据验证**:
- [x] E1–E18 每篇至少出现一次（§A.1 四表共 21 行，含 S1–S3）
- [x] 4 类技术各有方法说明（STM/STS、电学输运、s-SNOM、电子显微与衍射 §A.2.1–A.2.4）
- [x] 逐条来源标注（每行含 cards 卡片 ID + rev 精读文件 + pdf✓ 标记）
- [x] QC: 全部数字带 📜Q/💭I⚠️ 分级，无未标注数字

**卡片真实性核查发现（§A.5，待人类确认后回写 cards.md）**:
1. E11 "STEM 原子分辨成像" ✗ → 原文为 TEM 暗场 + SAED（"STEM" 出现 0 次）
2. E11 "~5 nm 宽度" ✗ → Yoo 原文 "5 nm" 仅指 hBN/电极厚度；畴壁宽度出处应归位 T23 (Enaldiev 2023)
3. E4 "无磁场" ✗ → Yin 2016 有磁场依赖 LL 光谱 + FWHM(B)；应改"无输运测量"
4. E10 "dG/dV" → 原文为 dG/dn_in
5. E2 技术含"圆偏振光"未能核实（无 PDF）
6. S3 年份 2024 → 2025（J. Phys.: Condens. Matter 37, 073001）
7. E15 "唯一"降级为"首批之一"；E1 红外波长 6.1 μm 因 PDF 文本层歧义（"6.1 mm"）未引用

**Plan Feedback**: 任务结果与 plan.md §三 交付物清单一致；卡片纠错为新发现，属 🟡 需补充级别——plan.md §2.6（QC）已追加实际执行路径记录。tasks.md 中 S-APP-A 输入节原写 `subfields/domain-wall/`，实际路径为 `subfields/bl-dw/`，已同步修正为实际路径。

**备注**: 本项目无 STATUS.md/CONTEXT.md（知识库目录结构），按 S-LOG 约定最终由 99_update_log.md 记录 Phase 级条目。
