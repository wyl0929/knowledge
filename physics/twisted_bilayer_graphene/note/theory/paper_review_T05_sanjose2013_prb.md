<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 16:15:17
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 16:15:19
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/paper_review_T05_sanjose2013_prb.md
 * @Description  :
-->
<!--
 * @Author       : AI精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/paper_review_T05_sanjose2013_prb.md
 * @Description  : T5: San-Jose/Prada 2013 — 扭转双层石墨烯中的螺旋网络
-->

# Paper Review: San-Jose & Prada (2013)

| 字段 | 内容 |
|------|------|
| **标题** | Helical networks in twisted bilayer graphene under interlayer bias |
| **作者** | Pablo San-Jose, Elsa Prada |
| **期刊** | PRB 88, 121408(R) (2013) |
| **DOI** | 10.1103/PhysRevB.88.121408 |
| **arXiv** | 1304.5344 |
| **类型** | 理论 — 螺旋网络模型奠基 |
| **PDF** | ✅ reference/pdfs/ |

---

## 1. 核心贡献

**螺旋网络 (helical network) 模型奠基论文**。首次明确提出：在小角度扭转双层石墨烯中，通过施加层间偏置，AB/BA 堆叠畴壁自然形成一张由拓扑保护螺旋模组成的**可编程二维导电网络**——类似于 Chalker-Coddington 型网络。提出用吸附原子选择性阻断网络链接，实现"拓扑纳米电子学"。

## 2. 物理机制

### 2.1 莫尔图样与局域堆叠

- 两层以微小扭角 $\theta$ 堆叠 → 形成三角莫尔图案
- 莫尔周期：$L_M = a_0/[2\sin(\theta/2)]$
- 局部堆叠在 AA、AB、BA 之间平滑交替
- 低能能标：$E_M = \hbar v_F K/2 \approx 88\,\text{meV} \times \theta(\text{deg})$

### 2.2 层间偏置下的拓扑

- 加偏置 $U$：AB 和 BA 区域都打开能隙，但谷陈数符号相反
- 单谷近似：$C_K^{\text{AB}} = -C_K^{\text{BA}} \approx \text{sgn}(U)$
- AB/BA 边界 → 谷陈数跳变 → 束缚拓扑螺旋模
- 螺旋 = 手征 + 谷-动量锁定：给定谷的电子沿畴壁只能单向传播

### 2.3 网络形成条件

经验判据：
- 足够小的扭角 $\theta$ → 足够大的莫尔周期
- 足够大的偏置 $U$ → AB/BA 区域被电子耗尽
- $|E| < |U|/2$ → 费米能位于畴区能隙内

估算：若 $U \sim 90$ meV，需要 $L_M \sim 290a_0$（$\theta \approx 0.2^\circ$）；对于 100 nm 莫尔周期，阈值偏置约 45 meV。

### 2.4 网络的可编程性

- **氢吸附原子**：在特定能窗内通过谷间散射完全阻断某条网络链接 → 实现"开关"
- **空位**：类似效应
- 通过控制吸附原子位置 → 可编程定制网络连通性 → 拓扑纳米电子电路

## 3. 关键结果

1. 大角度（$\theta=4^\circ$）加偏置仅平移 Dirac 锥，不形成网络
2. 小角度（$\theta \approx 0.2^\circ$）+ 偏置：形成完整的螺旋网络
3. 网络态局域化长度由 $U$ 和层间耦合长度 $l_\perp = \hbar v_F/\gamma_\perp$ 控制
4. 单个氢吸附原子可阻断一条链接——网络具有开关功能
5. 网络类似于 Chalker-Coddington 模型——量子霍尔平台-平台转变的标准模型

## 4. 局限

- 依赖谷近似守恒——对原子尺度缺陷和强谷间散射敏感
- 假设理想周期莫尔图案——真实样品有弹性畸变和非均匀扭角
- 连续模型无法描述吸附原子处的局域电子结构细节
- 更像是"设计原则"而非对所有真实样品的定量预测

## 5. 与 DW 项目关联

⭐⭐⭐⭐⭐ **DW 项目 domain-wall computing 概念的最直接理论祖先**。核心启示：
- **畴壁 = 可编程导线**：堆叠孤子天然形成互连网络
- **吸附原子 = 开关**：局域杂质选择性阻断网络链接
- **莫尔网络 = 电路图**：通过扭角 + 偏置设计网络连通性
- 这正是 DW 项目"拓扑互连"概念的物理基础

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
mTBG 螺旋网络模型奠基：偏压下 moire AB/BA 区域拓扑不等价 → 畴壁形成连通网络。畴壁束缚螺旋拓扑模——两谷反向传播。系统是 2D 可编程网络而非孤立边缘态。

### Q3: 理论如何与实验结合?
预言 mTBG 偏压下支持拓扑导电通道网络。概念性器件蓝图——深刻影响 Huang 2018、Rickhaus 2018 等实验解读，使"网络"成为核心范式。
