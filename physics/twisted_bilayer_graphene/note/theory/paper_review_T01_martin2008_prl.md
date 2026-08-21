<!--
 * @Author       : Yulong Wang
 * @Date         : 2026-08-06 16:12:58
 * @LastEditors  : Yulong Wang
 * @LastEditTime : 2026-08-06 16:13:05
 * @FilePath     : /.agents/home/wyl/project/knowledge/physics/twisted_bilayer_graphene/paper_review_T01_martin2008_prl.md
 * @Description  :
-->
<!--
 * @Author       : AI精读 (research_onboarding_skill, Phase 4)
 * @Date         : 2026-08-06
 * @FilePath     : /project/knowledge/physics/twisted_bilayer_graphene/paper_review_T01_martin2008_prl.md
 * @Description  : T1: Martin/Blanter/Morpurgo 2008 — 电场畴壁拓扑零模的首次预言
-->

# Paper Review: Martin, Blanter & Morpurgo (2008)

| 字段 | 内容 |
|------|------|
| **标题** | Topological Confinement in Bilayer Graphene |
| **作者** | Ivar Martin, Ya. M. Blanter, A. F. Morpurgo |
| **期刊** | PRL 100, 036804 (2008) |
| **DOI** | 10.1103/PhysRevLett.100.036804 |
| **类型** | 理论 — 电场畴壁 (EFW) 拓扑零模 |
| **PDF** | ✅ reference/pdfs/ |

---

## 1. 核心贡献

**首次预言**：在双层石墨烯中，通过静电栅压产生符号反转的层间偏置（"voltage kink"），可以在畴壁上束缚 1D 手征零模。这是**电场畴壁（EFW）拓扑态**的原始理论论文。

## 2. 物理机制

不同于传统的 Dirac 费米子零模（如超导涡旋、聚乙炔孤子），BLG 中的零模来自**手征 BLG 准粒子**——它们有二次色散 $E \propto p^2$ 和零能隙。

关键哈密顿量（单谷，4 分量波函数 $\psi = (A_1, B_1, A_2, B_2)^T$）：

$$
H = \begin{pmatrix}
-V(x)/2 & c\pi^\dagger & 0 & 0 \\
c\pi & -V(x)/2 & t_\perp & 0 \\
0 & t_\perp & V(x)/2 & c\pi^\dagger \\
0 & 0 & c\pi & V(x)/2
\end{pmatrix}
$$

低能有效 2-band 模型（$V \ll t_\perp$）：

$$
\tilde{H} = \begin{pmatrix}
\frac{V}{2} - \frac{c^2 p^2}{t_\perp} & -\frac{c^2 \pi^{\dagger 2}}{t_\perp} \\
-\frac{c^2 \pi^2}{t_\perp} & -\frac{V}{2} + \frac{c^2 p^2}{t_\perp}
\end{pmatrix}
$$

**拓扑起源**：加偏置后 BLG 体能谱 $E^2 = V^2/4 + c^4 p^4/t_\perp^2$ 有能隙 $|V|$。$V(x)$ 改变符号时，体能隙在 $V=0$ 处关闭再打开 → 拓扑相变 → 畴壁上束缚零模。

能谱近似（$V < t_\perp$，忽略 $p^2$ 修正）：

$$E^2 = \frac{V^2}{4} + \frac{c^4 p^4}{t_\perp^2}$$

## 3. 关键结果

1. **每谷 2 条零模分支**（每自旋）：来自 BLG 的"拓扑真空荷"——绝缘 BLG 态的两个非平庸拓扑不变量
2. **手征锁定**：同一谷内两条零模同向传播；$K$ 和 $K'$ 谷传播方向相反 → 谷过滤效应
3. **拓扑 vs 普通约束**：普通约束（同极性偏置）也能产生 1D 通道，但没有拓扑保护
4. **实验签名**：两端的电导应为 $4e^2/h$（两谷 × 两零模 × $e^2/h$，无谷间散射时）💭I⚠️——原文未出现该字符串（grep "4e" 无命中），此数值为推演结论

## 4. 局限

- 假设 $V(x)$ 足够平滑（无谷间散射）；尖锐势变化会破坏谷守恒
- 仅考虑单粒子图像，无相互作用
- 实验上实现分裂栅的"电压扭结"在 2008 年极具挑战
- 简化的 2-band 模型仅在 $V \ll t_\perp$（约 0.4 eV）有效

## 5. 与 DW 项目关联

⭐⭐⭐⭐⭐ **DW 项目 EFW 计算的最直接理论参照**。这篇论文预言的不只是畴壁态的存在，而是**拓扑约束与普通约束的本质区别**——DW 项目中 cont.py 的 EFW LDOS 计算需区分两者。

## 6. 关键引用链
- 被 Li/Morpurgo/Büttiker/Martin 2010 (T2) 直接继承和发展
- 被 Zhang/MacDonald/Mele 2013 (T6) 置于更广阔的谷陈数框架中

---

## Phase S 补充 (2026-08-11): Q2/Q3

### Q2: 理论如何解释 edge state?
通过静电栅压产生符号反转的层间偏置（voltage kink），使 BLG 体能隙在畴壁处闭合-重开，束缚手征 1D 零模（每谷每自旋 2 条，原文 "two zero modes per kink per valley per spin" 📜Q）。两谷反向传播形成螺旋态。⚠️ 原文未用 Chern/$\mathbb{Z}_2$ 语言（grep "Chern" 仅命中致谢人名 Chernyak），以 "topological vacuum charge" 论证零模数目 📜Q；"$\Delta C_v = 2$" 是 T6 Zhang 2013 的后世语言 💭I。

### Q3: 理论如何与实验结合?
预言 clean 系统中栅压畴壁弹道电导约 $4e^2/h$ 💭I⚠️（推演，见上）。后续 Ju 2015 Nature、Li 2016 Nat. Nanotech. 证实偏压畴壁导电通道和谷极化输运（review 层综合 💭I，原文未引这两篇）。核心预言——栅压可开关畴壁通道——被实验广泛验证。

---

## 更正日志 (2026-08-20, S-REV)

- **§3 实验签名 $4e^2/h$**: 加注 💭I⚠️——原文未出现该字符串（grep "4e"=0），系两谷×两模×$e^2/h$ 推演。依据: appendix_B §B.5#9。
- **Q2 拓扑不变量语言**: 删除 "$\mathbb{Z}_2$ / $\Delta C_v = 2$" 表述——原文未用 Chern/$\mathbb{Z}_2$ 语言（grep "Chern" 仅命中致谢人名），改以原文 "topological vacuum charge" + "two zero modes per kink per valley per spin" 📜Q 表述；$\Delta C_v$ 标注为 T6 (2013) 后世语言 💭I。依据: §B.5#9 + cards.md T1。
