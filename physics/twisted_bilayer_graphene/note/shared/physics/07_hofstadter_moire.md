<!--
 * @Author       : AI 整理 (从 E10 附录 A.4 剥离)
 * @Date         : 2026-08-31
 * @Description  : [PHY-HOF] Hofstadter 蝴蝶：moiré 超晶格中的朗道分形谱与标定用途
-->

# [PHY-HOF] Hofstadter 蝴蝶与 moiré 标定

> 复现于所有小扭角 moiré 输运论文（E10、Chou 2020/2021、Mahapatra 2022 等）。本文档讲通用物理；各 review 只写"本文代入"后的标定数值。

## 1. 物理实质

2D 周期晶格中的布洛赫电子 + 垂直磁场，能谱作为"每单胞磁通"的函数呈自相似分形（Hofstadter 1976）。核心无量纲参数：

$$\alpha=\frac{BA_{cell}}{\Phi_0}=\frac{A_{cell}}{2\pi l_B^2}\qquad(l_B=\sqrt{\hbar/eB})$$

- $\alpha=p/q$ 有理 → 谱劈裂为 $q$ 个子带（Harper 方程）；
- $\alpha$ 无理 → Cantor 集；
- $\alpha\to0$ → 普通朗道能级；$\alpha\to1$ → 恢复单条能带。

## 2. 为什么 moiré 让蝴蝶可见

- 原子晶格 $A_{atom}\approx0.052$ nm² → $\alpha=1$ 需 $B\approx8\times10^4$ T（不可及）；
- moiré 超晶格 $A_{MUC}=(\sqrt3/2)\lambda^2$（$\theta=0.42°$ → $\lambda=33$ nm → $A_{MUC}\approx943$ nm²）→ $B_1=\Phi_0/A_{MUC}\approx4.4$ T（可及）。
- moiré 把有效晶格放大 $\approx2\times10^4$ 倍。

## 3. 测量与读数

- 测量：$D=0$ 下测磁导图 $G(n_{out},B)$，取数值导数 $dG/dn_{out}$ 增强（微分=高通，见 [PHY-AB] §4）。
- 读数：主 Dirac 点（$n=0$）扇出的主朗道能级 + **2nd Dirac 点**（$\pm n_2$）扇出的卫星朗道能级；$B>0.5$ T 出现分形。低场 Dirac LL $E_N\propto\pm\sqrt{NB}$ → $(n,B)$ 平面 $n_N\propto N\cdot B$ 直线扇（Landau fan，见 [PHY-SDH] §4）。

## 4. 标定用途

- **满带密度**：$n_2=8/A_{MUC}=8/((\sqrt3/2)\lambda^2)$（每 moiré 单胞 8 电子 = 自旋×谷×层）→ 由实测 $\pm n_2$ 反推扭角 $\theta$。
- **regime 边界**：$|n_{in}|<|n_2|$ 标记 moiré 第一子带内，常兼作拓扑网络输运区的密度边界。
- 蝴蝶测量在 $D=0$ 做（前置标定），与 $D\neq0$ 的干涉测量分开。

> 实例数值（E10: $n_2\approx0.8\times10^{12}$ cm⁻² → $\theta=0.42°$；SI 文本指数笔误）见 E10 review §4.1。
