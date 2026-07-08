<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-19 23:29:53
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-19 23:29:53
 * @FilePath     : /.agents/home/wyl/project/knowledge/Economics/macroeconomics/14_paper_registry.md
 * @Description  :
-->
# 14 Paper Registry / 关键文献注册

Last updated: 2026-06-19

## 0. 如何使用这份文献清单

这不是宏观经济学所有重要论文的完整列表，而是一个**分层阅读路径**。文献按"必须先读 → 核心构建 → 前沿拓展 → 连接用户背景"组织。每篇论文标注了为什么重要、核心论点、方法论和适合谁读。

## 1. 入门必读（教科书级经典 + 关键原始文献）

### 1.1 理解宏观经济学是什么

**Blanchard, O. (2017). *Macroeconomics* (7th ed.). Pearson.**

- 类型：研究生/高年级本科教材
- 核心贡献：标准新凯恩斯综合框架的完整展开（短期 IS-LM-PC + 中期 AS-AD + 长期 Solow）
- 为什么先读它：它是现代央行经济学家思考宏观的标准范式。读完你能理解 GDP、利率、通胀、失业率之间的基本关系，以及政策制定者如何思考 trade-off。
- 与用户背景的关系：数学强度适中，物理学背景的人应该能快速适应其中的动态系统分析和相位图。

**Romer, D. (2019). *Advanced Macroeconomics* (5th ed.). McGraw-Hill.**

- 类型：博士生标准教材
- 核心贡献：比 Blanchard 更深入、更形式化的处理。包含 Solow、RBC、NK-DSGE、消费/投资理论、失业、货币政策、财政政策、经济增长各章的严格推导。
- 为什么读它：如果你只需要一本宏观教材，就这本。它教你"宏观经济学家如何建模"而不只是"宏观经济学有什么结论"。
- 与用户背景的关系：建模风格与理论物理有相似性——从基本假设出发，推导出可检验的预测。

### 1.2 理解核心模型

**Solow, R. M. (1956). "A Contribution to the Theory of Economic Growth." *Quarterly Journal of Economics*, 70(1), 65-94.**

- 类型：原始论文 / 基石级
- 核心论点：资本积累不能解释长期增长——长期增长来自技术进步（"Solow 残差"）。没有技术进步，经济会收敛到稳态。
- 方法：微分方程描述资本动态，稳态分析
- 适合谁：所有人。5 页核心模型，改变了对增长的理解。
- 与用户背景的关系：微分方程和稳态分析——物理学家的舒适区。

**Lucas, R. E. (1976). "Econometric Policy Evaluation: A Critique." *Carnegie-Rochester Conference Series on Public Policy*, 1, 19-46.**

- 类型：方法论奠基 / 必读
- 核心论点（Lucas 批判）：当政策规则变化时，私人主体的决策规则也会变化，因此基于历史数据估计的统计关系不能用于预测政策变化的效果。
- 为什么重要：这篇 5 页的论文从根本上改变了宏观经济学的方法论标准——所有后续宏观模型都必须有"微观基础"。
- 适合谁：所有想认真做宏观研究的人。

**Kydland, F. E., & Prescott, E. C. (1982). "Time to Build and Aggregate Fluctuations." *Econometrica*, 50(6), 1345-1370.**

- 类型：RBC 理论的创始文献 / 2004 诺奖工作
- 核心论点：技术冲击（Solow 残差的随机波动）可以解释相当一部分经济周期波动。经济波动是经济对实际冲击的最优反应，不一定代表市场失灵。
- 方法：DSGE 的早期原型——校准（calibration）而非估计，模拟经济对技术冲击的脉冲响应。
- 为什么重要：定义了现代宏观经济学的方法论标准：DSGE + 校准/估计 + 脉冲响应分析。
- 限制：所有后续研究几乎都拒绝了"技术冲击可以解释大部分经济周期"这一核心主张。

### 1.3 理解危机后的宏观经济学

**Christiano, L. J., Eichenbaum, M., & Evans, C. L. (2005). "Nominal Rigidities and the Dynamic Effects of a Shock to Monetary Policy." *Journal of Political Economy*, 113(1), 1-45.**

- 类型：NK-DSGE 实证基准
- 核心论点：包含价格粘性、工资粘性、习惯形成、投资调整成本的 DSGE 模型可以很好地匹配货币政策冲击后各宏观变量的经验脉冲响应。
- 关键发现：紧缩性货币政策冲击 → 产出、消费、投资、就业下降，通胀缓慢下降——符合新凯恩斯模型的预测，违背 RBC。
- 方法：结构 VAR 识别 + DSGE 估计
- 为什么重要：确立了 NK-DSGE 作为央行政策分析主流工具的地位。

**Eggertsson, G. B., & Woodford, M. (2003). "The Zero Bound on Interest Rates and Optimal Monetary Policy." *Brookings Papers on Economic Activity*, 2003(1), 139-211.**

- 类型：前瞻性政策分析
- 核心论点：当名义利率已经降到零（零利率下限，ZLB），传统货币政策失效。此时需要使用"预期管理"（承诺在未来维持宽松）和量化宽松等非常规工具。
- 为什么重要：2008 年后全球央行的政策工具箱主要依据这篇及后续文献的逻辑。
- 与用户背景：前面部分的状态空间模型和随机贴现因子的数学与统计物理有相似之处。

## 2. 核心构建（子方向关键论文）

### 2.1 货币政策

**Taylor, J. B. (1993). "Discretion versus Policy Rules in Practice." *Carnegie-Rochester Conference Series on Public Policy*, 39, 195-214.**

- 核心贡献：提出 Taylor 规则：$i_t = r^* + \pi_t + 0.5(\pi_t - \pi^*) + 0.5(y_t - y^*)$，并展示该规则很好地描述了 1987-1992 年美联储的实际行为。
- 为什么重要：成为央行政策分析的基准，也是最简单的可操作货币政策规则。

**Clarida, R., Gali, J., & Gertler, M. (1999). "The Science of Monetary Policy: A New Keynesian Perspective." *Journal of Economic Literature*, 37(4), 1661-1707.**

- 类型：综述 / 标准参考
- 核心贡献：将 NK-DSGE 模型中的最优货币政策系统化——包含 NKPC、动态 IS 曲线和 Taylor 型规则的完整框架。
- 为什么重要：如果你只能读一篇关于现代货币政策分析的论文，就是这篇。

### 2.2 财政政策

**Ramey, V. A. (2011). "Identifying Government Spending Shocks: It's All in the Timing." *Quarterly Journal of Economics*, 126(1), 1-50.**

- 类型：实证基准
- 核心贡献：利用军事支出的时间线（预期 vs 实际支出）识别政府支出冲击，估计财政乘数在 0.6-1.2 之间。
- 方法：叙事法（narrative approach）识别外生财政冲击。
- 为什么重要：财政乘数的实证估计仍然高度不确定，Ramey 的方法是识别策略的黄金标准之一。

### 2.3 劳动力市场

**Shimer, R. (2005). "The Cyclical Behavior of Equilibrium Unemployment and Vacancies." *American Economic Review*, 95(1), 25-49.**

- 类型：基准实证 + 理论挑战
- 核心发现（Shimer puzzle）：标准的 DMP 搜索匹配模型严重低估了失业和空缺岗位在经济周期中的波动幅度——模型需要不合理的大冲击来匹配数据中的波动。
- 为什么重要：定义了过去 20 年劳动宏观经济学最核心的研究议题。

### 2.4 异质性主体（HANK）

**Kaplan, G., Moll, B., & Violante, G. L. (2018). "Monetary Policy According to HANK." *American Economic Review*, 108(3), 697-743.**

- 类型：前沿基准
- 核心贡献：构建包含异质性家庭（不同财富水平、不同边际消费倾向）的新凯恩斯模型（HANK），展示货币政策不仅通过传统的跨期替代渠道传导，还通过间接的"收入不均等"渠道（如房贷利率对不同家庭的影响不同）。
- 方法：连续时间异质性主体模型 + 数值求解（有限差分/FEG 方法）
- 为什么重要：HANK 是目前最活跃的宏观前沿之一。
- 与用户背景：连续时间模型的数值求解——与物理学中的 PDE 求解和分布函数演化有直接方法连接。

## 3. 前沿探索

**Nakamura, E., & Steinsson, J. (2018). "Identification in Macroeconomics." *Journal of Economic Perspectives*, 32(3), 59-86.**

- 类型：方法论综述
- 核心贡献：清晰解释宏观经济学中识别（identification）的核心挑战——如何从观测数据中区分因果关系和相关关系。
- 为什么重要：宏观经济学中几乎所有实证争议最终都可以归结为识别问题。

**Auclert, A. (2019). "Monetary Policy and the Redistribution Channel." *American Economic Review*, 109(6), 2333-2367.**

- 核心贡献：系统分析货币政策通过资产价格、收入构成和消费篮子的再分配效应。

**Jordà, Ò., Schularick, M., & Taylor, A. M. (2017). "Macrofinancial History and the New Business Cycle Facts." *NBER Macroeconomics Annual*, 31, 213-263.**

- 核心贡献：使用 140 年 17 国的历史数据，系统性地记录金融周期与实体经济周期的关系。核心发现：信贷增长是金融危机和深度衰退的最稳健预测指标之一。

## 4. 与用户背景连接的文献（计算/物理方向）

**Axtell, R. L. (2016). "Agent-Based Macroeconomics." In *Handbook of Computational Economics* (Vol. 4).**

- 类型：非主流方法介绍
- 核心贡献：综述用大规模异质性 Agent 的计算机模拟替代 DSGE 解析模型的宏观经济学路线。
- 与用户背景：直接使用大规模并行计算，与统计物理、复杂系统模拟共享技术基础。

**Achdou, Y., Han, J., Lasry, J. M., Lions, P. L., & Moll, B. (2022). "Income and Wealth Distribution in Macroeconomics: A Continuous-Time Approach." *Review of Economic Studies*, 89(1), 45-86.**

- 类型：方法论
- 核心贡献：展示如何使用连续时间 PDE 方法（Fokker-Planck 方程 + Hamilton-Jacobi-Bellman 方程）求解异质性主体宏观模型。
- 与用户背景：**直接连接**——这种方法在物理上等价于统计力学中的 Fokker-Planck 方程和随机控制。物理学家的技能几乎可以直接迁移。

## 5. 阅读路径建议

### 路径 A：快速入门（1-2 周）
1. Blanchard *Macroeconomics* 第 1-9 章（IS-LM, AS-AD, Phillips 曲线）
2. Blanchard 第 10-13 章（增长、技术进步）
3. Romer 第 5 章（新凯恩斯经济学基础）
4. Lucas (1976) 原文

### 路径 B：系统进入（1-2 月）
1. 路径 A 的全部
2. Romer 全书（除方法论章节外，逐章阅读）
3. Christiano, Eichenbaum & Evans (2005) —— 看 NK-DSGE 如何与数据对话
4. Clarida, Gali & Gertler (1999) —— 货币政策的完整框架
5. Kaplan, Moll & Violante (2018) —— 前沿方向

### 路径 C：计算/量化方向（结合用户背景）
1. 路径 B 全部
2. Achdou et al. (2022) —— 物理学家友好的宏观数值方法
3. 学习 Dynare（标准 DSGE 求解软件）或 Julia 的宏观工具包
4. Ramey (2011), Nakamura & Steinsson (2018) —— 宏观实证的识别方法论

## 6. 未确认信息（NEEDS_VERIFICATION）

- 部分论文的版本和页码范围需要核对
- 部分学者的最新论文未收录
- Agent-Based Macroeconomics 的最新综述可能有更新的版本
