<!-- 临时协调文件：11 篇非精读实验论文按 4 块新架构重读的共享规范（供 subagent 执行，完成后可删除） -->

# 重读规范（E1–E18 中非精读实验论文 → 4 块辨识结构）

## 目标

把旧格式 review 重读并按「4 块辨识结构」新架构整体重写，严格执行 QC（禁止无源数字）。

## 格式唯一参照（先读）

1. **规范示例**：`note/experiments/paper_review_E12_xu2019_natcommun.md` —— 逐节对齐结构、粒度、证据标注风格（这是新架构的 canonical 版本）。
2. **模板**：`/home/wyl/.agents/skills/paper-reading/templates/paper_review.md`
3. **QC 协议**：`/home/wyl/.agents/skills/paper-reading/references/LITERATURE_QC_PROTOCOL.md`（v1.1）
4. **方法论**：`note/shared/method/paper_reading_methodology.md` + `mechanism_questions.md`

## 执行步骤

1. `pdftotext -layout "<PDF>" /tmp/<id>.txt`（有 SI 则连 SI 一起提取，正文+SI 都留底）。
2. 五步阅读法重读：Step0 黑箱三要素 → Step1 四层变量（符号层一次钉死）→ Step2 逐层传递函数 → **Step3 可辨识性判别表（含金量核心）+ 机制溯源五问** → Step4 闭环核对 → Step5 证据分级（从第一遍就做）。
3. 先读现有旧 review：保留仍有效的 📜Q 内容与全部历史「更正日志」（追加不覆盖）。
4. 用 write 工具**整体覆盖**重写 review 文件，结构如下（对齐 E12）：

```
头部 frontmatter（保留 @FilePath，@Description 注明"2026-09-XX 按 4 块新架构重读"）
+ 字段表（编号/标题/作者/期刊/DOI/arXiv/类型/课题组/PDF·SI/精读日期）
+ 共享知识引用一行（[PHY-*] 锚点）
## TL;DR（问题句式 + 主结果带不确定度 + 结论强度措辞）
## 1. 系统辨识导览
   四层变量表（L1 旋钮/L2 导出量/L3 模型量/固定参数/反推量/L4 观测量）
   可辨识性判别表（判据·数据 / 排除谁 / 确立谁）
   主结果 ↔ 判别表映射（显式）
   [前提与限定]（噪声·扰动 / 判别性扫轴 / 候选集 M 边界声明）
## 2. 结果与机制（按论文自身论证结构，非 IMRaD）
## 3. 实验方法（器件 / 静电学 / 测量；非常规预处理只一行 + [PHY-*] 锚点）
## 4. 关键数据（提取链 + 验证链 + 不确定度标注）
## 5. 主要结论
## 6. 局限与未解决
## 7. 与其他工作的关系（跨论文对标放这里，不放正文）
## 8. 对后续研究的影响
## 9. 理论模型映射（供计算对标）
## Phase S 目的接口（三问引用式 + 增量价值一行）
## 反向核对 pass（日期 + 逐项 grep 结论）
## 更正日志（表格，追加）
```

## QC 硬规则（v1.1）

- **禁止无源数字**：任何数字必须能 grep 到 `/tmp/<id>.txt` 原文全文文本；grep 不到 → 删除或降级 📊F/💭I 并显式标注。
- **禁止跨论文迁移**：数据只从所读论文原文取；引用其他论文数据需核对那篇原文。
- **禁止常识脑补**：原文没有的实验条件/结构/参数不得凭领域直觉补写；不确定写 `NEEDS_VERIFICATION`。
- **证据分级**：📜Q（原文事实，附位置）/ 推导（由原文公式合成）/ 📊F（读图估算）/ 💭I（推断）。
- **不确定度轴（与证据分级正交）**：[±] 原文误差棒 / [~] 原文无误差棒 / [读图] 图·色标提取 / [相对] 仅相对量。
- **报告准入**：正文只允许 📜Q；📊F/💭I 标 ⚠️；色标值必须标 [读图]。
- 写完做**反向核对 pass**：提取草稿全部数字与专名，逐项 grep 原文；找不到的删/降级；结论写入 review 末尾 + 更正日志。

## 共享物理锚点（引用不复制）

| 锚点 | 文件 | 内容 |
|------|------|------|
| [PHY-AB] | note/shared/physics/01_ab_interference.md | AB 干涉 + 退相干 + 振荡观测/数据处理 |
| [PHY-SDH] | 02_sdh_landau.md | SdH/朗道量子化 + LK + Landau fan + AB vs SdH 判别 |
| [PHY-MB] | 03_miniband_network.md | miniband 网络：驻波量子化、Δn=4/A、θ² 标度、v_DW 提取 |
| [PHY-BERRY] | 04_berry_vs_ab_phase.md | AB 电磁相位 vs Berry/valley 相位 |
| [PHY-GATE] | 05_electrostatics_gating.md | 双栅静电学：n/D 换算、共模/差模 |
| [PHY-FP] | 06_fp_dimension.md | FP 干涉与维度判据 k_F∝n^{1/d} |
| [PHY-HOF] | 07_hofstadter_moire.md | Hofstadter 蝴蝶（moiré 超晶格） |
| [PHY-QPI] | 08_qpi_intervalley.md | FT-STM/QPI：谷内 vs 谷间散射 → 谷保护判据 |
| [PHY-EF] | 09_fermi_level_band_bending.md | 费米能/化学势/band bending/CNP |

**不要新建 shared 文件**。本文特有、通用性不足以晋升的物理直接写在 review 内；通用性强的标注「💭 可晋升 [PHY-*]」。

## 约束

- 只改指定这篇 review，不动其他文件、不动 cards.md/plan.md/tasks.md。
- 保留旧 review 里 grep 可验证的 📜Q 事实；把旧的无源/过强论断按 QC 修正。
- 数字必须带证据分级 + 不确定度标注；全文无未标注数字。
