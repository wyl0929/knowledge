<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 16:16:31
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 16:16:36
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/paper_review_T06_zhang2013_pnas.md
 * @Description  :
-->
<!--
 * @Author       : AI精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/paper_review_T06_zhang2013_pnas.md
 * @Description  : T6: Zhang/MacDonald/Mele 2013 — 谷陈数和三类畴壁边界模的统一理论
-->

# Paper Review: Zhang, MacDonald & Mele (2013)

| 字段 | 内容 |
|------|------|
| **标题** | Valley Chern numbers and boundary modes in gapped bilayer graphene |
| **作者** | Fan Zhang, Allan H. MacDonald, Eugene J. Mele |
| **期刊** | PNAS 110, 10546–10551 (2013) |
| **DOI** | 10.1073/pnas.1308853110 |
| **类型** | 理论 — 畴壁拓扑分类的统一框架 |
| **PDF** | ✅ reference/pdfs/ |

---

## 1. 核心贡献

**畴壁物理的"罗塞塔石碑"**：系统统一了三类双层石墨烯畴壁的拓扑分类——

1. **电场反转墙 (EFW)**：层间偏置 $\Delta$ 符号反转
2. **层堆垛反转墙 (LSW)**：AB ↔ BA 堆叠滑移
3. **补偿墙 (Compensated wall)**：电场 + 堆垛同时反转

关键结论：**EFW 和 LSW 在拓扑上等价**（都由谷陈数跳变 $\Delta C_\nu = 2\nu$ 束缚边界态），但补偿墙的拓扑变化互相抵消 → 边界态完全打开。

## 2. 方法

- **四带 + 两带连续模型**：推导 Berry 曲率、谷陈数
- **晶格紧束缚**：检验短程结构效应
- **DFT-LDA**：实际畴壁（含应变）的第一性原理验证
- **对称性保护拓扑 (SPT) 分类**：Wen 的框架 → 将 chirally stacked 多层石墨烯放入统一语言

## 3. 关键公式与结果

### 3.1 两带有效模型（单谷）

低能 2-band Hamiltonian（在 $|\Delta| \ll t_\perp$ 极限）：

$$\tilde{H}_\nu = \mathbf{g}_\nu(\mathbf{q}) \cdot \tilde{\boldsymbol{\sigma}}$$

$$\mathbf{g}_\nu(\mathbf{q}) = \left(-\frac{q_x^2 - q_y^2}{\gamma},\; \frac{2\nu q_x q_y}{\gamma},\; \Delta\right)$$

其中 $\gamma = t_\perp/(\hbar v_F)^2$。

Berry 曲率：

$$\Omega_\nu(\mathbf{q}) = \mp \frac{2\nu\gamma\Delta\, q^2}{(q^4 + \gamma^2\Delta^2)^{3/2}}$$

单谷的"谷陈数"：$N_\nu = -\nu\,\text{sgn}(\Delta)$。

### 3.2 相图

$\Delta-\mu$ 平面上的两个关键隙闭合线：
- $\Delta = 0$：体能隙关闭（$q=0$）
- $\mu = 0$：在有限动量 $q_x = \pm\sqrt{\Delta^2 + \gamma^2/4}$, $q_y=0$ 处线性交叉关闭

→ 这两条线分隔不同的拓扑相。

### 3.3 三类畴壁对比

| 畴壁类型 | $\Delta C_\nu$ | 边界态分支/谷 | 拓扑保护 |
|------|:---:|:---:|:---:|
| EFW ($\Delta \to -\Delta$) | $2\nu$ | 2 | ✅ 谷陈数保护 |
| LSW (AB $\to$ BA) | $2\nu$ | 2 | ✅ 谷陈数保护 |
| 补偿墙 (EFW+LSW) | $0$ | 0 | ❌ 无保护边界态 |

### 3.4 多层推广

Chirally stacked $N$ 层石墨烯：

$$C_K = -C_{K'} = \frac{N}{2}\,\text{sgn}(t_\perp \Delta)$$

→ 每谷 $N$ 条边界态分支。

### 3.5 数值结果

- **LSW 紧束缚**（$t=2.8$ eV, $t_\perp=0.4$ eV, $V=0.5$ eV, 200 晶胞超胞）：每个 $K/K'$ 谷各 2 条边缘态/自旋
- **LSW + 跨畴耦合**：额外出现平带 → 打开后可能产生第三条 gapless mode
- **DFT-LDA**（3.1 nm 宽畴壁, 1.5 nm 域, 5 V/nm 电场）：两条清晰的 1D Dirac 色散；畴壁处应变导致 $K_1$ 和 $K_2$ Dirac 点能量分裂
- **LSW Landauer 电导**（无谷间散射）：可达 $N e^2/h$

## 4. 局限

- 谷陈数 $N_\nu$ 不是严格拓扑不变量——依赖谷守恒近似
- armchair 型边界、原子级尖锐缺陷可使谷保护失效
- LSW 的短程细节产生额外平带和"脆弱模"——连续模型不足以完全描述
- SPT 分类在强关联体系中可能失效

## 5. 与 DW 项目关联

⭐⭐⭐⭐⭐ **DW 项目的"拓扑域壁字典"**。直接指导：
- **识别畴壁类型**：LSW 和 EFW 拓扑等价 → 可以用统一的计算框架
- **判断拓扑保护**：补偿墙没有拓扑保护 → 不是好的器件平台
- **层数 scaling**：$N$ 层 → $N$ 条/谷通道 → 三层畴壁可能有更丰富的输运
- **数值基准**：LSW 紧束缚和 DFT 结果是 DW 项目 tb.py 和 cont.py 验证的参照标准

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
谷陈数统一分类 BLG 边界模式：畴壁两侧 $\Delta C_v \neq 0$ → 保护边界模。EFW 和 LSW 的 $\Delta C_v$ 相同 → 都支持两支手征支/谷。补偿畴壁 $\Delta C_v = 0$ → 无保护模。多层系统模式数 $\propto N$。

### Q3: 理论如何与实验结合?
三类畴壁明确实验预言：EFW/LSW 有通道、补偿壁无通道（可作对照）、模式数随层数增加。为 Ju 2015 (EFW) 和 Yin 2016 (LSW) 提供统一理论解释框架。
