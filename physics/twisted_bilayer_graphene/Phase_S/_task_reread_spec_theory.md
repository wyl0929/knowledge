<!-- 临时协调文件：Q2 理论精读 8 篇按 4 块新架构重读的共享规范（供 subagent 执行，完成后可删除） -->

# 重读规范（Q2 理论 8 篇 → 4 块辨识结构）

## 目标

把旧格式（research_onboarding Phase 4 风格）理论 review 重读并按「4 块辨识结构」新架构整体重写，严格执行 QC v1.1（禁止无源数字、禁止跨论文迁移、禁止常识脑补）。

## 先读（格式唯一参照，顺序执行）

1. **规范示例（canonical）**：`note/experiments/paper_review_E12_xu2019_natcommun.md` —— 逐节对齐结构、粒度、证据标注风格。⚠️ 它是**实验**论文，本文是**理论**论文：把 §3「实验方法（器件/静电学/测量）」替换为「理论模型与方法（模型/哈密顿量/推导/计算方法）」，§9 不变（供计算对标）。其余节结构与粒度完全对齐。
2. **模板**：`/home/wyl/.agents/skills/paper-reading/templates/paper_review.md`
3. **QC 协议**：`/home/wyl/.agents/skills/paper-reading/references/LITERATURE_QC_PROTOCOL.md`（v1.1，唯一权威）
4. **方法论**：`note/shared/method/theory_paper_reading.md`（理论专属：演绎结构 + 5 块模板）+ 入口 `note/shared/method/paper_reading_methodology.md`（公共规范）+ `mechanism_questions.md`
5. **共享物理锚点**（引用不复制）：`note/shared/README.md` 的锚点表；理论 8 篇主要用到 `[PHY-BERRY]`（Berry/valley Chern）、`[PHY-LB]`（Landauer-Büttiker 量子化电导）、`[PHY-MB]`（网络 miniband/驻波）、`[PHY-AB]`（AB 干涉，T15 用）、`[PHY-GATE]`（双栅静电学，T1/T5 偏压换算）。

## 执行步骤

1. 先读现有旧 review（路径见各篇任务），**保留仍有效的 📜Q 内容与全部历史「更正日志」**（新稿追加不覆盖）。
2. `pdftotext -layout` 已提取：正文在 `/tmp/<ID>.txt`（已留底）；grep 原文核对所有数字。
3. 五步阅读法重读：Step0 黑箱三要素 → Step1 四层变量（符号层一次钉死）→ Step2 逐层传递函数 → **Step3 可辨识性判别表（含金量核心，理论论文 = 区分竞争图景/竞争模型）+ 机制溯源五问** → Step4 闭环核对 → Step5 证据分级（从第一遍就做）。
4. 用 `write` 工具**整体覆盖**重写 review 文件（结构见下）。

## 输出结构（对齐 E12，理论适配）

```
头部 frontmatter（@FilePath 指向本文件实际路径，@Description 注明"2026-09-XX 按 4 块新架构重读"）
+ 字段表（编号/标题/作者/期刊/DOI/arXiv/类型[理论]/课题组/PDF·SI/精读日期）
+ 共享知识引用一行（[PHY-*] 锚点）
## TL;DR（问题句式：本文想解决的理论问题；主结果带不确定度；结论强度保留作者措辞）
## 1. 系统辨识导览
   黑箱三要素：{输入旋钮 | 输出观测量 | 声称结论}
   四层变量表（理论版）：
     L1 旋钮 u = 模型可调参数（θ、层间偏压 U/V、磁场 B、能量 E、栅压）
     L2 导出量 x₁ = 由旋钮导出的几何/能量量（moiré 周期 L、畴区能隙 δ、moiré 能标 E_M）
     L3 模型量 x₂ = 模型内部量（S 矩阵、valley Chern C_v、能带、DoS、色散）
     固定参数 = 晶格常数/hopping（t_⊥、γ₁、v_F）
     反推量 θ̂ = 从谱学/实验反推的量（v_DW 等，若本文有）
     L4 观测量 y = 可实验检验的预言（DoS 峰、电导平台、LDOS 图案、色散）
   可辨识性判别表（理论版：每条判别 = 判据/排除谁[竞争图景]/确立谁）
   主结果 ↔ 判别表映射（显式）
   [前提与限定]（近似假设 + 适用范围 + 候选模型集 M 边界声明：集外候选未排除须声明）
## 2. 结果与机制（按论文自身论证结构，非 IMRaD）
## 3. 理论模型与方法（模型/哈密顿量/推导/计算方法；非常规步骤只一行 + [PHY-*] 锚点）
## 4. 关键预言与数据（提取链 + 验证链 + 不确定度标注）
## 5. 主要结论
## 6. 局限与未解决
## 7. 与其他工作的关系（跨论文对标放这里，不放正文）
## 8. 对后续研究的影响
## 9. 理论模型映射（供 TBPM/Kubo 计算对标：本文参数 ↔ 可算量，如 θ→λ→A、U→δ、通道数→电导平台）
## Phase S 目的接口（三问引用式 + 增量价值一行）
## 反向核对 pass（日期 + 逐项 grep 结论）
## 更正日志（表格，追加旧条目 + 本次新增条目）
```

## QC 硬规则（v1.1）

- **禁止无源数字**：任何数字必须能 grep 到 `/tmp/<ID>.txt` 原文全文文本；grep 不到 → 删除或降级 📊F/💭I 并显式标注。
- **禁止跨论文迁移**：数据只从所读论文原文取；引用其他论文数据需核对那篇原文。跨论文对标（如"本文解释 Xu 2019"）放 §7，且必须核对**本文引用列表是否真有该文献**。
- **禁止常识脑补**：原文没有的参数/公式/结论不得凭领域直觉补写；不确定写 `NEEDS_VERIFICATION`。
- **证据分级**：📜Q（原文事实，附位置：正文段落/Fig./SI 章节）/ 推导（由原文公式合成）/ 📊F（读图估算）/ 💭I（推断）。
- **不确定度轴（正交）**：[±] 原文误差棒 / [~] 原文无误差棒 / [读图] 图·色标提取 / [相对] 仅相对量。
- 写完做**反向核对 pass**：提取草稿全部数字与专名，逐项 grep 原文；找不到的删/降级；结论写入 review 末尾 + 更正日志。

## 共享物理锚点（引用不复制）

| 锚点 | 文件 | 内容 |
|------|------|------|
| [PHY-BERRY] | note/shared/physics/04_berry_vs_ab_phase.md | Berry/valley Chern、chiral vs helical、AB 相位无关拓扑 |
| [PHY-LB] | 10_landauer_buttiker.md | Landauer-Büttiker、量子化电导、通道计数/自旋简并约定 |
| [PHY-MB] | 03_miniband_network.md | 网络 miniband 驻波量子化、Δn=4/A、v_DW 提取 |
| [PHY-AB] | 01_ab_interference.md | AB 干涉、退相干 e^{-L/L_φ}、谐波（T15 用） |
| [PHY-GATE] | 05_electrostatics_gating.md | 双栅静电学 n/D 换算（T1/T5/T9 偏压换算用） |
| [PHY-SDH] | 02_sdh_landau.md | SdH/朗道量子化、AB vs SdH 判别（T15 SdH 振荡用） |

**不要新建 shared 文件**。本文特有、通用性不足以晋升的物理直接写在 review 内；通用性强的标注「💭 可晋升 [PHY-*]」。

## 约束

- 只改指定这一篇 review 文件，**不动其他文件、不动 cards.md/plan.md/tasks.md**。
- 保留旧 review 里 grep 可验证的 📜Q 事实；把旧的无源/过强论断按 QC 修正（各篇已知修正项见各篇任务，依据 `Phase_S/appendix_B_theory.md` §B.5 与 `Phase_S/cards.md` Q2 卡片）。
- 数字必须带证据分级 + 不确定度标注；全文无未标注数字。
- 理论论文注意：作者的"预言/建议"是**结论**不是**已验证事实**，须用作者措辞（propose/predict/suggest）并标 📜Q，不得写成已证实。
