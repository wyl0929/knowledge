<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-06-11 20:08:43
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-06-11 20:08:44
 * @FilePath     : /project/knowledge/physics/multilayer_graphene/17_claims_evidence_ledger.md
 * @Description  :
-->
# 17 Claims and Evidence Ledger / 论断-证据台账

Last updated: 2026-06-11

> 将本 field pack 中的重要判断按证据强度分类：
> `fact` = 多组独立验证、无争议；
> `interpretation` = 数据支持但存在替代解释；
> `speculation` = 有理论/直觉支持但缺少直接实验证据；
> `recommendation` = 策略性建议。

---

## 1. 关于平带与魔角

| ID | 论断 | 类型 | 证据摘要 | 可靠性 |
|---|---|---|---|---|
| C-01 | TBG 在 θ ≈ 1.1° 处出现近零带宽的平带 | fact | BM 模型 + 多组 DFT + STM/STS 实验一致验证 | ★★★★★ |
| C-02 | TDBG 在 θ ≈ 1.1°–1.3° 处存在电场可调的平带 | fact | 连续模型 + 实验输运 + 压缩率一致 | ★★★★★ |
| C-03 | TMBG 在 θ ≈ 1.0°–1.2° 处存在平带 | fact | 多组实验独立报道 | ★★★★ |
| C-04 | 螺旋三层存在两组平带，魔角条件与 TBG 不同 | interpretation | 连续模型理论预测，尚无直接实验 | ★★★ |
| C-05 | 多层转角石墨烯中"魔角"应是多维参数空间中的流形 | interpretation | 理论推广，待实验检验 | ★★★ |

---

## 2. 关于关联物态

| ID | 论断 | 类型 | 证据摘要 | 可靠性 |
|---|---|---|---|---|
| C-06 | TBG 魔角处存在关联绝缘态（整数和分数填充） | fact | 超过 10 个独立实验组报道 | ★★★★★ |
| C-07 | TBG 魔角处存在非常规超导 | fact | 多组独立验证，但 Tc 和相边界有样品差异 | ★★★★ |
| C-08 | TDBG 中存在关联绝缘态 | fact | 三组以上独立实验 | ★★★★ |
| C-09 | TDBG 中存在超导 | interpretation | 初步实验信号，可重复性待提高 | ★★★ |
| C-10 | TMBG 中存在关联绝缘态 | fact | 多组独立实验 | ★★★★ |
| C-11 | TMBG 中存在超导 | interpretation | 部分实验组报道，待独立验证 | ★★★ |
| C-12 | 超导 Tc 在多层体系中可能高于 TBG | speculation | 态密度增加在理论上有利于提高 Tc，但无序和竞争序可能抵消 | ★★ |
| C-13 | 关联绝缘态的对称性破缺模式（谷极化、自旋极化、向列序）在 TBG 中部分确定 | interpretation | 不同实验探针给出不同答案（输运 vs STM vs 压缩率） | ★★★ |
| C-14 | 多层体系中存在 TBG 没有的新奇量子相（拓扑超导、手性自旋液体等） | speculation | 理论提出可能性，无实验证据 | ★★ |

---

## 3. 关于调控与相图

| ID | 论断 | 类型 | 证据摘要 | 可靠性 |
|---|---|---|---|---|
| C-15 | TDBG 中位移场 D 可驱动能带拓扑相变（Chern 数改变） | fact | 输运中观测到量子化霍尔电阻 + 理论一致 | ★★★★★ |
| C-16 | TMBG 中位移场可调控关联态 | fact | 多组实验相图 | ★★★★ |
| C-17 | 静水压可连续调控层间耦合 → 调魔角 | interpretation | 初步实验（TBG），多层待做 | ★★★ |
| C-18 | 转角不均匀（twist angle disorder）是限制样品质量的主要因素 | fact | STM 直接成像 + 输运样品差异统计 | ★★★★ |
| C-19 | 多层体系中转角不均匀可能被平均化 | speculation | 直觉推论，无定量实验或模拟验证 | ★★ |

---

## 4. 关于理论与方法

| ID | 论断 | 类型 | 证据摘要 | 可靠性 |
|---|---|---|---|---|
| C-20 | BM 连续模型在 θ < 2° 时有效描述 TBG 低能物理 | fact | 10+ 年验证，与实验和 DFT 一致 | ★★★★★ |
| C-21 | BM 模型在三层/多层的直接推广基本正确 | interpretation | 与实验定性一致，定量有待系统比较 | ★★★★ |
| C-22 | 晶格弛豫对平带带宽有 ~20–50% 的修正 | fact | 多组 DFT 和力场模拟验证 | ★★★★ |
| C-23 | DMFT 和 Hartree-Fock 对关联态给出定性一致的相图 | interpretation | 方法间存在定量差异 | ★★★ |
| C-24 | 紧束缚方法可以可靠描述转角石墨烯的全带结构 | fact | 与 DFT 和连续模型在重叠区域一致 | ★★★★ |

---

## 5. 对本 pack 用户的策略性建议

| ID | 建议 | 类型 | 理由 |
|---|---|---|---|
| R-01 | 优先以紧束缚 + TBPM 做大超胞能带/DOS 计算 | recommendation | 用户已有代码，改造成本低，产出明确 |
| R-02 | 首先复现 TBG/TDBG 的已知能带作为验证 | recommendation | 建立可信度，熟悉参数 |
| R-03 | 研究转角不均匀的定量效应 | recommendation | 文献的 open question + TBPM 大超胞优势 |
| R-04 | 谨慎投入强关联计算（DMFT/QMC） | recommendation | 高门槛，建议先产出 TB 结果再决定 |
