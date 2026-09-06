<!--
 * @Author       : AI 整理 (从 E10 附录 A.2 剥离)
 * @Date         : 2026-08-31
 * @Description  : [PHY-FP] FP 干涉与维度判据：k_F∝n^{1/d}、等间距指纹、2R_c 抑制、n_1D 换算
-->

# [PHY-FP] Fabry-Pérot 干涉与维度判据

> 复现于所有"腔内驻波干涉"输运论文（E10、E12 的驻波条件同源、McDowell 2026 等）。本文档讲通用推导；各 review 只写"本文代入"后的数据。

## 1. FP 驻波条件

腔（两半透明镜 = p-n 结/密度台阶）+ 弹道载流子 → 驻波：

$$2L=j\cdot\frac{2\pi}{k_F}\quad(j=1,2,\dots)$$

即共振在 $k_F$ 空间**等间距**：$\Delta k_F=\pi/L$（线性腔）或 $2\pi/L_{tot}$（闭环）。闭环 + 磁场 = Bohr-Sommerfeld 统一条件（见 [PHY-MB] §3）。

## 2. k 空间态计数 → k_F ∝ n^{1/d}

$d$ 维自由电子气每个 k 态占 $(2\pi)^d$，态密度 $g/(2\pi)^d$（$g$ 简并度）：

| 维度 | 态计数 | $k_F(n)$ | FP 密度周期 |
|------|--------|----------|-------------|
| 1D | $n_{1D}=g\cdot\dfrac{2k_F}{2\pi}=\dfrac{g k_F}{\pi}$ | $\propto n_{1D}$ | **等间距**（$\Delta n=2g/L_{tot}$ 常数） |
| 2D | $n=g\cdot\dfrac{\pi k_F^2}{(2\pi)^2}=\dfrac{g k_F^2}{4\pi}$ | $\sqrt{4\pi n/g}$（$g$=4 → $\sqrt{\pi n}$） | 非等间距（$\Delta n\propto k_F$，磁导图**抛物线**） |

> **维度判据**：密度轴上"等间距（1D）vs 抛物线（2D）"是 FP 数据的 1D/2D 指纹。n-B 平面上的线签名对照见 [PHY-SDH] §4。
> ⚠️ **记号约定警示**：有的 SI 写 $k_F=(2\pi/g)n_{1D}$（比标准 $\pi/g$ 大 2 倍）——"费米点计数 vs 费米区间计数"约定差异，不影响 √n vs n 标度；跨文献引用时须核对约定。

## 3. 2D 面密度 → 1D 线密度（网络情形）

通道网络：单位宽度通道数 $N_{ch}$（三方向网络 $N_{ch}=2\sqrt3/\lambda$，$\lambda$ 为 moiré 周期）→

$$n_{1D}=\frac{n_{2D}}{N_{ch}}=n_{2D}\cdot\frac{\lambda}{2\sqrt3}$$

（仍保持 $k_F\propto n_{1D}\propto n_{2D}$ 线性标度，只是系数改变。）

## 4. 磁场对 FP 的抑制（2D 特有）

2D 载流子轨道被洛伦兹力弯折，驻波需回旋直径大于腔长：

$$2R_c=2\frac{\hbar k_F}{eB}>L$$

B 增大 → $2R_c<L$ → FP 消失（实验上 $R_c<2L$ 开始减弱、$R_c=L/2$ 完全消失）。**1D 通道轨迹不受洛伦兹力影响 → FP/AB 在高 B 持续** —— 这正是 E10 的"磁场持续"判据。

## 5. dG/dn 高通预处理

背景电导低频缓变、FP 纹波高频 → 数值求导 $dG/dn$ 压低背景放大振荡（周期不变）。与 E12 的 $d^2\rho/dB^2$ 同属"微分=高通滤波"，见 [PHY-AB] §4。

> 实例数值（E10: Δn_in=4.7×10¹⁰ cm⁻²、L_tot≈870 nm、g=4 的选择依据）见 E10 review §4。
