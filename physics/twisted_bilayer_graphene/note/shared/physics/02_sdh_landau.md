<!--
 * @Author       : AI 整理 (从 E12 附录 A 剥离)
 * @Date         : 2026-08-31
 * @Description  : [PHY-SDH] SdH/朗道量子化 + LK 因子 + Landau fan + AB vs SdH 判别
-->

# [PHY-SDH] SdH 振荡、朗道量子化与 "AB vs SdH" 判别

> 复现于几乎所有磁输运论文。本文档讲通用物理 + 判别逻辑；各 review 只写"本文代入"后的数据。

## 1. SdH 机制（朗道量子化）

强场下态密度劈成离散朗道能级，扫 B 时费米能级逐个穿过（填充因子 $\nu=n\Phi_0/(gB)$ 过整数）→ 电阻振荡，**1/B 轴上等间距** $\Delta(1/B)=g/(n\Phi_0)$。存在两个硬条件：

1. **量子迁移条件** $\omega_c\tau=\mu B\gg1$（朗道能级需分得开）；
2. **热条件** $\hbar\omega_c\gg k_BT$。

## 2. LK 因子：SdH 的温度依赖

完整 LK 振幅 $\propto R_T\,R_D\,R_S\,\cos(2\pi(F/B+\gamma))$：

- **热阻尼** $R_T=X/\sinh X$，$X=2\pi^2k_BT/\hbar\omega_c$；高温极限 $X\gg1$ 时 $R_T\approx2X e^{-X}$（**指数抹平**）。物理起源：费米-狄拉克热展宽（宽度 $k_BT$）把间距 $\hbar\omega_c$ 的朗道能级抹糊，$R_T$ 是 $-\partial f/\partial E$ 的傅里叶变换在振荡频率处的取值。
- **Dingle 无序因子** $R_D=e^{-\pi/\omega_c\tau_q}$（$\tau_q$ 量子散射时间）。
- **自旋因子** $R_S=\cos(\pi g m^*/2m_0)$。

**量级示例**（以 120 K、m*≈0.01 m₀、B=1 T 计）：$k_BT\approx10$ meV、$\hbar\omega_c\approx12$ meV → $X\approx17.5$ → $R_T\sim10^{-7}$。故 SdH 在 120 K 被热抹平到百万分之一；AB 只需 $L_\phi>L$ 就能活（见 [PHY-AB]）。

## 3. "AB vs SdH" 判别（几何相位 vs 朗道量子化）

AB 是**几何相位**效应、SdH 是**朗道量子化**效应，对 B、T 依赖恰好相反。三条观测逐一排除 SdH：

| 观测 | SdH 的要求 | 排除结论 |
|------|-----------|---------|
| 低场（~0.1–1 T）已振荡 | $\omega_c\tau=\mu B\approx1$（B=1 T）→ 朗道能级未分辨 | 低场无 SdH；AB 不需朗道量子化 |
| 振幅达数十% ρxx | SdH 是背景小纹波（几个 %） | 巨幅 = 干涉开关主输运通道 = AB（Xu 2019 达 ~50%，数据见 E12 review） |
| 持续到高温（如 120 K） | $X\approx17.5$ → $R_T\sim10^{-7}$ | SdH 热抹平到百万分之一；AB 只要 $L_\phi>L$ |

**内交叉验证（作者自证）**：AB 振荡"持续到数 T 处才被 SdH 淹没"——同一器件里两机制先后登场（低场 AB、高场 SdH），若低场振荡是 SdH，应低场最弱、高场最强，而非反过来。

**最干净判据（B vs 1/B）**：AB 在 **B 轴**等间距（恒 ΔB）；SdH 在 **1/B 轴**等间距，换算回 B 轴 $\Delta B\approx B^2\Delta(1/B)$ 随 B 变密。画 $1/B$ 轴看是否等间距即教科书级判别。

⚠️ 两个限定使此判据严谨：① 须跨**宽 B 范围**——SdH 在窄窗口可"看起来近似 B 周期"（周期按 $\Delta B\approx B^2\Delta(1/B)$ 随 B 拉长；Xu 2019 数值自检见 E12 review §2.2）；② 论文还**直接并排观测到 SdH**——低场 AB 与高场 SdH 同台并存，是并列对照而非单一"B 周期"推断。"随 B 周期"只是 AB 的**必要条件**（排除 SdH 作主振荡），完整 AB 认定需多判据合取（低场/高温/振幅 + 谐波几何 + 面积互验）。

## 4. （B, n）二维图里的三种"线"签名

（区分三种机制各自的几何形态；x=B、y=n、z=振荡信号）

| 机制 | 共振条件 → n(B) | 形态 |
|------|----------------|------|
| **SdH（Landau fan）** | $\nu=\dfrac{n\Phi_0}{gB}=N\Rightarrow n=\dfrac{g}{\Phi_0}N B$ | **过原点直线扇**（电子侧正斜率、空穴侧负斜率）；仅高 B + 低温 |
| **AB（1D 网络）** | $j=\dfrac{L k_F}{2\pi}\pm\dfrac{AB}{\Phi_0}$，$k_F\propto n$ | **交叉斜线 X**（正负斜率并存于同一密度区，来自 ± 顺/逆时针环绕）；低 B 即现 |
| **2D FP/AB（√n 标度）** | $k_F=\sqrt{\pi n}$ → $n\propto(j\mp AB/\Phi_0)^2$ | **抛物线**（n 是 B 的二次函数） |

> **Landau fan 是 SdH 的可视化（直线扇），不是抛物线**；抛物线是 2D（√n）FP/AB 的签名。⚠️ AB 与 SdH 在（B,n）图都画直线，须靠**形态**（扇 vs 交叉 X）+ **B 范围** + **T 依赖** + **B vs 1/B 周期**联合判别。
