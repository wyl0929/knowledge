<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 16:13:34
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 16:13:39
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/paper_review_li2010_prb.md
 * @Description  :
-->
<!--
 * @Author       : AI精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/paper_review_li2010_prb.md
 * @Description  : T2: Li/Morpurgo/Büttiker/Martin 2010 — 单谷体-边对应关系的非普适性
-->

# Paper Review: Li, Morpurgo, Büttiker & Martin (2010)

| 字段 | 内容 |
|------|------|
| **标题** | Marginality of bulk-edge correspondence for single-valley Hamiltonians |
| **作者** | Jian Li, Alberto F. Morpurgo, Markus Büttiker, Ivar Martin |
| **期刊** | PRB 82, 245404 (2010) |
| **DOI** | 10.1103/PhysRevB.82.245404 |
| **类型** | 理论 — 拓扑分类的严格性检验 |
| **PDF** | ✅ reference/pdfs/ |

---

## 1. 核心贡献

**关键发现**：单谷体-边对应关系**不是普适的**。以 BLG 为原型系统，证明即使在没有谷间耦合的理想情况下，BLG-真空界面的零模数目**依赖于边界条件**（zigzag 边 1/2/0 条），而不是由"谷陈数"唯一决定。

这一发现区分了两类界面：
- **BLG-真空界面**：$N_\nu$ 不是良好拓扑不变量 → 边缘态数目不普适
- **BLG-BLG 界面**（畴壁）：$\Delta N_\nu = N_\nu^L - N_\nu^R$ 是良好拓扑不变量 → 边界态数目由两侧"谷陈数"之差确定

## 2. 方法

- **连续模型**：4-band BLG Hamiltonian → 解析求解不同边界条件下的边缘态
- **紧束缚模型**：验证解析解 → 四种 zigzag 边缘类型（图 2）
- **几何解释**：分析 $N_\nu$ 作为映射的拓扑不变量意义——说明为什么单谷的 $N_\nu$ 不构成良好拓扑不变量

## 3. 关键结果

**BLG 四类 zigzag 边缘的边缘态数目**（图 2）：

| 边缘类型 | 亚晶格终止 | 子能隙边缘态数目/谷 |
|:------:|------|:----:|
| (a) | B1-A2 exposed | 1 |
| (b) | A1-B2 exposed | 1 |
| (c) | B1-B2 exposed | 2 |
| (d) | A1-A2 exposed | **0** |

→ 即使谷守恒，边缘态数目也非普适！

**BLG-BLG 畴壁**：$\Delta N = N_L - N_R$ 是良好定义的拓扑不变量 → 畴壁态数目由两侧谷陈数差决定，不受边界细节影响。

**几何解释**：单谷 BLG 的 $g(k)$ 映射（从 $k$-空间到 Bloch 球）不覆盖整个球面 → $\pi_2(S^2)$ 的同伦分类不完备 → $N_\nu$ 不是真正拓扑不变量。但畴壁两侧的 $g_L(k)$ 和 $g_R(k)$ 之差可形成良好映射。

## 4. 关键公式

BLG 低能连续模型（单谷）：

$$H_\nu = \begin{pmatrix} H_1 & K_\nu \\ K_\nu & H_0 \end{pmatrix}$$

其中 $H_1 = \sigma_x + \Delta \sigma_z$, $H_0 = -\Delta \sigma_z$, $K_\nu$ 包含层间耦合。

有效 2-band 模型（$|\Delta| \ll t_\perp$）：

$$g_\nu(k) = \left(-\frac{k_x^2 - k_y^2}{2m}, -\nu\frac{2k_x k_y}{2m}, \Delta\right)$$

单谷"谷陈数" $N_\nu = -\nu \,\text{sgn}(\Delta)$。

**但**：$N_\nu$ 的积分 $\frac{1}{4\pi}\int d^2k\,\hat{g}\cdot(\partial_{k_x}\hat{g} \times \partial_{k_y}\hat{g})$ 在无限 $k$ 空间不收敛（$g(k)$ 在 $k \to \infty$ 时不指向固定方向）→ 这不是良好拓扑不变量。

## 5. 局限

- 仅考虑无谷间散射的理想情况
- 讨论限于非相互作用费米子
- 实际器件中无序边缘会使所有边缘态局域化

## 6. 与 DW 项目关联

⭐⭐⭐⭐⭐ **DW 项目拓扑分类的严格理论基础**。核心信息：
- 计算 EFW/LSW 的畴壁态数目时，应使用 $\Delta N_\nu$（两侧谷陈数差），而非单侧 $N_\nu$
- 边缘态数目可能依赖于具体的边界截断方式——这对 cont.py 和 tb.py 中的超胞建模至关重要
- 区分"真空边缘"和"畴壁界面"的不同拓扑保护程度
