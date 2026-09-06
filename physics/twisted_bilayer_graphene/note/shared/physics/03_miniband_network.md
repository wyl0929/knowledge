<!--
 * @Author       : AI 整理 (从 E12 附录 A 剥离)
 * @Date         : 2026-08-31
 * @Description  : [PHY-MB] miniband 网络：驻波量子化、Δn=4/A 域计数、θ² 标度、v_DW 提取
-->

# [PHY-MB] miniband：1D 网络驻波量子化与谱学反推

> 复现于 E12/E14、T9/T12/T15 等"畴壁网络 miniband"文献。本文档讲通用物理；各 review 只写"本文代入"后的数据。

## 1. miniband 从何而来：闭合回路驻波 vs 开放墙

- **单条孤立畴壁** = 1D 导线 → 色散 $E=\hbar v_{DW}k$，$k$ 连续 → **连续带，无 miniband**。
- **网络把墙连成闭合三角回路** → 电子绕一圈回到起点必须**相位自洽**（周期边界条件）：

$$k_j L = 2\pi j \;\Rightarrow\; E_j = j\cdot\frac{h v_{DW}}{L}\quad (j=0,1,2,\dots)$$

连续带被"砍"成一串**等间距离散能级** = **miniband**。类比：拉直的弦（连续振动）→ 弯成圈（只有整数个波的驻波）。

**玻尔-索末菲驻波条件 $kL=2\pi j$ 就是 miniband 能级的半经典公式**——miniband 和 BS 是同一件事的两种说法。

## 2. 电子在墙上，为何填充数关联 moiré 面积

电子波函数集中在墙上（这是"电子在哪"），但 miniband 容量由"网络有几个量化单元"决定（这是"能装多少电子"）——两者不是一回事：

- 每个三角回路（面积 $A$）= 一个量化单元，每 miniband 每回路贡献一个态。
- 回路面密度 $=1/A$（$A=\tfrac{\sqrt3}{4}\lambda^2$，moiré 单胞面积 $2A$ 含 AB+BA 两畴）。
- 填满一个 miniband = 每回路 1 电子 ×（2 自旋 × 2 谷）4 重简并 × $1/A$ 回路/cm²：

$$\Delta n = \frac{4}{A}$$

> 类比：2D 晶体每带填 1 电子/单胞——电子集中在原子上，但带容量按单胞面积数。这里"单胞"=三角回路。

## 3. 密度振荡 ↔ AB 振荡：同一驻波条件在不同轴

统一玻尔-索末菲条件 $j=L k_F/2\pi \pm AB/\Phi_0$：
- 固定 n 扫 B → AB 项 $2\pi BA/\Phi_0$ 周期变化 → **B 周期**（$\Delta B=\Phi_0/A$）＝AB 振荡。
- 固定 B 扫 n → $k_F(n)$ 变化 → 逐条填 miniband → **n 周期**（$\Delta n=4/A$）＝密度振荡。

两者是**同一 1D 网络的同一量子化条件**在磁轴和密度轴上各显一次。

## 4. 从 miniband 间距做谱学反推（Δn→A→θ→v_DW）

**Δn → A → θ**：$\Delta n=4/A$ 反解 $A=4/\Delta n$，再用 $\theta=2\arcsin(\sqrt{\sqrt3 a^2/16A})$（SI Note 2）得扭角。与 $\Delta B=\Phi_0/A$ 反推的 A、结构值 $A=\tfrac{\sqrt3}{4}\lambda^2$ 三方互验。

**Δn ∝ θ²（标度预言）**：$\Delta n=4/A=16\theta^2/(\sqrt3 a^2)\propto\theta^2$ —— 多器件 Δn-θ 对照是网络模型的定量验证实例（Xu 2019 三器件数据见 E12 review §4.6）。

**miniband 数可定量计算**：$M\approx\delta/\varepsilon=\delta/(v_{DW}h/6\lambda)$（δ=间隙、ε=miniband 间隔；实例数值见 E12 review §4.4）。

**v_DW 的提取链**（谱学反推，非第一性）：数 miniband（M）→ $\varepsilon=\delta/M$ → 考虑 AB/BA 简并解除（谱加密一倍）$\Delta E=2\varepsilon$ → 驻波公式 $v_{DW}=\Delta E\cdot L/h=2\varepsilon\cdot3\lambda/h$。

- **v_DW 的定义**：畴壁 1D 态的**群速度 = 费米速度**（线性色散 $E=\hbar v_{DW}k$ 斜率）。⚠️ 不是输运里 $\mu E$ 的经典漂移速度，也不是 2D 石墨烯费米速度 $v$（虽数值相近）。
- **sharp 畴壁判据**（SI Note 6）：sharp 墙（$w<v/\sqrt{\gamma_1\delta}$）→ $v_{DW}\approx v$；宽墙 → $v_{DW}$ 变小且现抛物线型非拓扑通道 → M 变多。实验数得 $v_{DW}\approx v$ → **反证畴壁原子级 sharp**。

## 5. miniband ≠ 朗道/赝朗道：三种"离散能级"对照

| 机制 | 来源 | 间距 | ρxy |
|------|------|------|-----|
| 朗道能级 LL | 真磁场 B | $\hbar\omega_c\propto B$ | 单调阶梯、单侧恒号 |
| 赝朗道能级 | 应变赝磁场 | $\propto B_{ps}$ | 同上 |
| **网络 miniband** | **驻波（几何）** | $\varepsilon=h v_{DW}/L$ | **正负交替** |

**ρxy 为何正负震荡（vs LL 单调）**：LL 电子区所有能级同属电子型带 → ρxy 恒正单调；miniband 每个含电子+空穴型态 → 载流子类型交替 → ρxy 正负交替。变号次数 = 2×ρxx 峰数（中性点 + van Hove 各变一次）。

**miniband 周期 D 无关**：$\Delta n=4/A$、$n_j=4j/A$ 只含 λ 不含 D → 密度图峰位为竖直条纹不随 D 漂移；D 只定隙 δ（→M 个数）与可见度。周期 D 无关 + Δn∝θ² + ρxy 正负交替三条合起来把"几何驻波量子化"钉死，排除静电（D）与朗道/赝朗道（B/应变）两种竞争解释。

## 6. 论文事实层去向

SI Note 5（Efimkin-MacDonald 模型的理论依据）摘要与 Xu 2019 多器件 θ² 数据属**论文事实层**，已移回 E12 review §2.3/§4.6，不在此重复。
