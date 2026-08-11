<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 17:20:37
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 17:20:38
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/note/helical_network/paper_review_chou2021_prb.md
 * @Description  :
-->
<!--
 * @Author       : AI精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/note/helical_network/paper_review_chou2021_prb.md
 * @Description  : T19: Chou, Wu & Sau 2021 — CDW与有限温度输运
-->

# 论文精读：Chou, Wu & Sau, PRB (2021)

> **Yang-Zhi Chou, Fengcheng Wu, Jay D. Sau**
> "Charge density wave and finite-temperature transport in minimally twisted bilayer graphene"
> PRB 104, 045146 (2021) | arXiv:2104.02084
>
> 作者单位：University of Maryland

---

## 1. 一句话总结

首次系统研究 mTBG 畴壁网络中**电子-电子相互作用**的效应：预言了道间自旋能隙 CDW 态 + 有限温度的 Luttinger 液体幂律电阻率 $\rho \propto T^\alpha$，并解释了实验中观测到的电阻率极小值。

---

## 2. 核心物理

### 2.1 模型

- 每根畴壁含两个 1D 手征通道（来自 $\Delta C = 2$），考虑道间杂化 $t$
- 1D 费米子 + 短程排斥相互作用 → 玻色化 → Luttinger 液体

### 2.2 零温相：道间 CDW

- 两个通道间的库仑相互作用驱动**自旋能隙 + 道间电荷密度波**（interchannel CDW）
- CDW 态下两个通道的电荷模式锁定（"Coulomb drag"） → 仅剩一个导电模式
- 条件：需要谷对称性弱破缺（允许 umklapp 散射）

### 2.3 有限温输运

- 电荷 umklapp 散射 → 幂律电阻率 $\rho(T) \propto T^{2K_c-2}$（$K_c$ 为电荷 Luttinger 参数）
- **CDW 关联导致电阻率极小值**：中间温度 $T \sim \Delta_{\text{CDW}}$ 处 $\rho(T)$ 出现极小 → 与实验定性一致

---

## 3. 与用户研究的关联

| 维度 | 关联 |
|---|---|
| **方法** | 玻色化 + RG — DW 项目可结合 tbplas 检验非费米液体输运 |
| **可验证性** | $\rho(T) \propto T^\alpha$ 的指数 $\alpha$ 可用 tbplas NEGF + 无序检验 |

---

*报告生成日期：2026-08-06 | 基于 PDF pdftotext 精读*

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
畴壁网络中相互作用在手征通道间打开 CDW 能隙 → 非费米液体行为。畴壁态是强关联 1D 系统，输运有特征温度依赖的幂律行为。

### Q3: 理论如何与实验结合?
解释 mTBG 输运在关联能标附近的电阻率极小值和幂律温度依赖。对低温输运中关联效应可见时特别相关。
