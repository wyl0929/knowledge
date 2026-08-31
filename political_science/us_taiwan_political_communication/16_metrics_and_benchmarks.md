<!--
Field: us_taiwan_political_communication
Mode: full_onboarding
Domain archetype: social_science
Created date: 2026-08-30
-->

# 16 Metrics and Benchmarks / 指标与基准

Last updated: 2026-08-30

## 使用说明

本文件记录领域常用指标、benchmark、baseline 和评估风险。指标必须说明"测量什么"和"不测量什么"。每个指标都要说明定义或公式、高低值意味着什么、它可能误导什么，以及怎样构成公平 baseline。本包指标分三组：编码质量指标、框架分布/演变指标、跨媒介流向指标。

## Metric Entry / 指标条目

### 编码者间信度 Krippendorff's alpha

**人话解释：** 两个编码员（或人与机器）给同一批文本打框架标签，有多少一致是"真一致"而不是碰巧一致。它是框架编码能不能进论文的入场券。

**Definition / 定义：**

$$
\alpha = 1 - \frac{D_o}{D_e}, \quad D_o = \text{观察到的分歧比例}, \quad D_e = \text{随机期望分歧比例}
$$

**变量含义：** D_o 是实际编码中的分歧占比；D_e 是假设编码员随机乱标时的期望分歧占比；α=1 表示完全一致，α=0 表示与随机无异。

**高值 / 低值意味着什么：** 探索性研究惯例 α ≥ .67 可用、结论性研究 α ≥ .80 更好（阈值为领域经验共识，具体出处 NEEDS_VERIFICATION）；低于 .60 说明编码手册歧义大或编码员训练不足。

**可能误导的地方：** α 只测"一致"，不测"对不对"（两人可能一致地错）；它受标签分布不均衡影响（稀有框架的 α 会虚低）；人-机 α 高不代表机器理解语义，可能只是任务太简单。

**公平 baseline：** 人-人信度是机器的对标基线；LLM 编码必须与人工编码在同一子样本、同一编码手册上比较；不能只用"多数投票准确率"代替逐标签信度。

Field / 领域：内容分析 / 计算文本分析

### 主题一致性（topic coherence, C_V / NPMI）

**人话解释：** 主题模型吐出来的每个"主题"是不是真的一堆相关词聚在一起，而不是机器硬凑的噪声。

**Definition / 定义：**

$$
C_V(t) = \frac{1}{\binom{N}{2}} \sum_{i<j} \text{NPMI}(w_i, w_j) \text{ 的滑窗聚合形式}
$$

（C_V 基于主题前 N 个词的成对 NPMI 在参考语料上的滑窗共现，取平均；NPMI 为归一化点互信息。）

**变量含义：** w_i, w_j 是主题 t 的前 N 个高权重词；NPMI ∈ [−1,1]，1 表示词对总是共现。

**高值 / 低值意味着什么：** 高 C_V 说明主题内部词凝聚、可解释；低值说明主题数是凑出来的，需重新调参或换模型。

**可能误导的地方：** coherence 高只说明"词聚得好"，不说明"主题在语义上是一个框架"；选主题数 K 时只看 coherence 曲线会陷入过拟合式调参。

**公平 baseline：** 不同模型（STM vs BERTopic）比较时必须在同一语料、同一 K 下比较；报告 K 的选择过程而不是只报最优值。

Field / 领域：主题建模评估

### 框架分布及其变化量

**人话解释：** 每个事件、每个平台、每个时期里，各框架占了多少；比较这些占比的变化，就是"框架建构与演变"的原始读数。

**Definition / 定义：**

$$
P_{t}(f) = \frac{n_{t,f}}{\sum_{f'} n_{t,f'}}, \quad \Delta P(f) = P_{t_2}(f) - P_{t_1}(f)
$$

**变量含义：** n_{t,f} 是窗口 t 内被编码为框架 f 的文本数（允许共现编码时用加权占比）。

**高值 / 低值意味着什么：** 某一框架占比的持续上升/下降是演变描述的核心；占比跳变常与高烈度事件对齐。

**可能误导的地方：** 占比是相对量——"中国威胁框架占比上升"可能只是"选举框架占比下降"的镜像；文本总量（议题热度）与框架结构是两回事，须分开报告；共现编码时占比之和不等于 1，解读需小心。

**公平 baseline：** 事件-平台-时期三维对齐的样本才可比；基线比较对象应是"同事件跨平台"或"同平台跨事件"，不能拿不同事件结构的两期直接比均值（阶段混淆风险）。

Field / 领域：框架内容分析

### 领先-跟随检验（Granger 因果 / 交叉滞后相关）

**人话解释：** 问"新闻的框架变化是不是系统性地走在社交平台前面（或反过来）"，是"跨媒介传播特征"的可检验读数。

**Definition / 定义：**

$$
A_t^{social} = \alpha + \sum_{k=1}^{p} \beta_k A_{t-k}^{news} + \sum_{k=1}^{p} \gamma_k A_{t-k}^{social} + \varepsilon_t
$$

以滞后项系数 β_k 的联合显著性判定"新闻→社交"流向；反向方程同理。经典简化版是交叉滞后相关并用 Rozelle-Campbell baseline 修正自相关。

**变量含义：** A 为框架/议题显著性（频次或占比）序列，按小时或天聚合；p 为滞后阶数。

**高值 / 低值意味着什么：** 单方向 β 显著、γ 不显著 → 单向流向证据；双向显著 → 互惠/反馈关系；都不显著 → 无证据（不等于无关系）。

**可能误导的地方：** 伪回归（需差分/平稳化）；聚合层级不同结论可能反转；时间戳噪声（推文时间 vs 新闻发布时间精度）；第三变量（同一事件驱动两边同时涨）会被误读为因果——所以 Granger 只算"预测性领先"，不是真因果。

**公平 baseline：** 两平台序列必须用同一时间窗粒度、同一显著性定义；至少与"事件热度本身"（GDELT 或全平台提及量）做对照，检验领先关系是否只是共同事件驱动的假象。

Field / 领域：媒介间议程设置

### 人机一致性 / 分类指标（F1 等）

**人话解释：** 机器（或 LLM）编码与人工黄金标准的吻合程度，决定自动编码能否替代人工。

**Definition / 定义：**

$$
F1 = 2 \cdot \frac{\text{precision} \cdot \text{recall}}{\text{precision} + \text{recall}}
$$

**变量含义：** precision = 机器标为正类中真为正类的比例；recall = 真为正类中被机器找到的比例。

**高值 / 低值意味着什么：** 高 F1（相对人工标准）才允许用机器编码代替人工做全量推断；低 F1 说明只能把机器结果当探索。

**可能误导的地方：** 类别不均衡时宏平均与微平均差距大；LLM 的"高 F1"若建立在简单任务（如"是否提到台湾"）上，不能外推到语义框架任务；人工标准本身有噪声（人-人 α 是机器 F1 的天花板）。

**公平 baseline：** 报告人-人 α 作为天花板，机器 F1 与之并列；同一子样本、同一编码手册、同一提示版本；不能拿旧模型结果与新提示比较。

Field / 领域：计算文本分析

## Benchmark Entry / 基准条目

Benchmark / 基准：Media Frames Corpus（Card et al. 2015, ACL）
Plain-language summary / 人话摘要：跨议题通用政策框架标注语料，是新闻框架检测的标准 benchmark。
Task / 任务：新闻文本的通用政策框架分类（15 类，如经济、安全与国防、道德、公平与平等……）
Dataset / platform / 数据或平台：约 1.2 万条新闻标题与段落（具体规模 NEEDS_VERIFICATION），公开 GitHub 发布
Baseline / 基线：朴素多数类；传统监督分类器（SVM/逻辑回归）；现代 LLM zero-shot
Metric / 指标：F1（宏/微）、准确率
Known results / 已知结果：原作者报告了跨议题泛化难度（具体数字 NEEDS_VERIFICATION，需读原文）
Reproducibility status / 可复现状态：数据公开、可复现
Hardware / compute needs / 硬件或算力：单机 CPU 可跑传统基线；LLM 基线需 API 预算
Relation to user assets / 与用户资产关系：用户可先在该语料上标定 LLM 编码流程（prompt、版本、信度），再迁移到涉台语料
Need verification / 待核验：语料规模、基线数字
Last updated / 最后更新：2026-08-30

---

Benchmark / 基准：事件驱动跨平台比较模板（Valenzuela et al. 2017；Wang & Guo 2018）
Plain-language summary / 人话摘要：同事件锚定新闻与 Twitter 双语料、比较议程/框架的研究设计模板——用户设计的直接方法学对标。
Task / 任务：同一事件下跨平台议程/框架分布比较与流向检验
Dataset / platform / 数据或平台：灾害/议题事件的新闻与 Twitter 语料
Baseline / 基线：平台内自相关序列；事件热度序列（第三变量对照）
Metric / 指标：框架/议题分布差异、交叉滞后相关、Granger 检验
Known results / 已知结果：Wang & Guo 2018 在帧层面验证了媒介间框架设置（细节 NEEDS_VERIFICATION，需读原文）
Reproducibility status / 可复现状态：数据依赖平台采集，部分可复现
Hardware / compute needs / 硬件或算力：普通工作站
Relation to user assets / 与用户资产关系：用户 MVP 应复刻该模板的最小版本（1 个事件 × 2 平台）
Need verification / 待核验：原文方法细节与结论数值
Last updated / 最后更新：2026-08-30

## Summary Table / 汇总表

| Metric / Benchmark | Type | 人话解释 | What it tests | Common baseline | Risk | Status | Last updated |
|---|---|---|---|---|---|---|---|
| Krippendorff's alpha | metric | 编码一致性 | 编码手册稳定性 | 人-人信度 | 稀有标签虚低 | 领域惯例（阈值出处待核验） | 2026-08-30 |
| Topic coherence (C_V/NPMI) | metric | 主题词凝聚度 | 主题模型质量 | 同语料同 K 比较 | coherence≠语义框架 | verified（Röder 2015） | 2026-08-30 |
| 框架分布变化量 ΔP(f) | metric | 框架占比与变化 | 框架建构/演变 | 事件-平台-时期对齐 | 占比是相对量；阶段混淆 | working_definition | 2026-08-30 |
| Granger/交叉滞后 | metric | 新闻↔社交流向 | 跨媒介传播方向 | 事件热度对照 | 伪回归、第三变量 | mature（第一层）/ emerging（帧层面） | 2026-08-30 |
| F1/人机一致性 | metric | 机器编码质量 | LLM 编码可用性 | 人-人 α 天花板 | 任务太简单虚高 | mature | 2026-08-30 |
| Media Frames Corpus | benchmark | 通用框架检测基准 | 帧检测流程标定 | 多数类/监督/LLM | 无涉台专属框架 | verified（ACL 2015） | 2026-08-30 |
| 事件驱动跨平台模板 | benchmark | 同事件双平台比较设计 | 用户设计对标 | 平台内自相关 | 模板数据依赖 | skimmed（需读原文） | 2026-08-30 |
