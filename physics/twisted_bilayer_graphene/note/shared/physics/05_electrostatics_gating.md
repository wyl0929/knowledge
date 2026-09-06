<!--
 * @Author       : AI 整理 (从 E10 附录 A.1 剥离)
 * @Date         : 2026-08-31
 * @Description  : [PHY-GATE] 双栅静电学：平行板电容、n/D 换算、轴映射、共模/差模
-->

# [PHY-GATE] 双栅静电学：栅压 → 密度/位移场

> 复现于所有双栅输运论文（E10/E12/E13 等）。本文档讲通用推导；各 review 只写"本文代入"后的数值。

## 1. 平行板电容充电

栅压 $V$ 经介电层（厚度 $d$、介电常数 $\varepsilon_{hBN}$）在石墨烯感应面电荷密度 $CV$（$C=\varepsilon_0\varepsilon_{hBN}/d$，$Q=CV$ 面密度版），除以 $e$ 得载流子密度：

$$n=\frac{CV}{e}$$

⚠️ 近似：平行板（忽略边缘场）；**未含量子电容修正**（作者自陈 "simple approximation" / "parallel plate capacitor model"）。

## 2. 双栅叠加与局部/全局几何

$$n=\frac{1}{e}(C_{tg}V_{tg}+C_{bg}V_{bg})$$

- **局部栅**（顶栅只盖腔）→ 腔内 $n_{in}$ 由两栅共同决定；**全局栅**（背栅盖全器件）→ 腔外 $n_{out}=C_{bg}V_{bg}/e$ 只有背栅项。
- 腔边界的密度突变 $n_{in}\neq n_{out}$ → p-n 结 = 半透明"腔镜"（FP 干涉的前提）。

## 3. 位移场

$$D=\frac{D_{top}-D_{bottom}}{2},\qquad D_{top}=\frac{\varepsilon_r V_{tg}}{d_{top}}=\frac{C_{tg}V_{tg}}{\varepsilon_0}$$

代入电容形式：

$$D=\frac{C_{tg}V_{tg}-C_{bg}V_{bg}}{2\varepsilon_0}$$

## 4. 用 (n_in, n_out) 表达 D

由 $C_{tg}V_{tg}=e(n_{in}-n_{out})$、$C_{bg}V_{bg}=e n_{out}$：

$$D=\frac{e}{2\varepsilon_0}(n_{in}-2n_{out})\;\Longleftrightarrow\; n_{out}=\frac{n_{in}}{2}-\frac{\varepsilon_0}{e}D$$

常数 $D$ = 斜率 $1/2$ 的直线族；$n_{in}\approx0$ 时 $D=-\dfrac{e}{\varepsilon_0}n_{out}$。

## 5. 轴映射（线性剪切）与共模/差模

$(n_{in},n_{out})$ 与 $(V_{tg},V_{bg})$ 之间是上三角（剪切）变换：

$$\begin{pmatrix}n_{in}\\n_{out}\end{pmatrix}=\frac{1}{e}\begin{pmatrix}C_{tg}&C_{bg}\\0&C_{bg}\end{pmatrix}\begin{pmatrix}V_{tg}\\V_{bg}\end{pmatrix}$$

- 纵轴 $n_{out}$ = $V_{bg}$ 纯缩放；横轴 $n_{in}$ = $V_{tg}$ 缩放 + $n_{out}$ 平移。
- 系数比 $C_{tg}/C_{bg}=d_{bottom}/d_{top}$（更薄介质的一侧栅更"劲"）。
- **共模/差模正交**：共模 $(C_{tg}V_{tg}+C_{bg}V_{bg})$ → $n$；差模 $(C_{tg}V_{tg}-C_{bg}V_{bg})$ → $D$。双栅因此可**独立**调 $n$ 与 $D$ —— "固定 D 沿 D=const 线扫 n"（E12 的实验设计）的原理。

> 实例数值（E10: $C_{tg}/e\approx6.55\times10^{11}$、$C_{bg}/e\approx3.93\times10^{11}$ cm⁻²/V、$d_{bottom}/d_{top}=45/27=1.67$）见 E10 review §3.2。

## 6. STM 针尖 vs 平面栅：为什么针尖不能独立调 n 和 D

- **平面双栅**（§1–5）成立的前提：两栅都是均匀平行板 → 场 1D 均匀 → n（共模）与 D（差模）**全局良定义、可正交独立扫**。
- **STM 针尖不是可替代的"局部顶栅"**：① 局域点栅（nm 曲率、强边缘场）→ 场高度非均匀、只在针尖下方，n/D **无全局均匀定义**；② $V_{bias}$ 同时做两件事——设隧穿能量窗口（谱学）+ 产生局域垂直场（栅）→ 能量与场**共用同一旋钮**，无法"固定能量扫场"；③ 样品接地、$V_{bias}$ 驱动隧穿电流 → 针尖**不积累全局电荷**，只做局域能带弯曲（非充电式栅极）；④ 真空点接触，无平行板线性覆盖 + 功函数差 $\Delta\varphi$ 叠加不可控场（依赖针尖几何）。
- **背栅**：薄片样品可设全局 n（E9 Huang 2018 石墨背栅）；**块体 HOPG（E13）不可栅控** → 场几乎全来自 $V_{bias}+\Delta\varphi$。
- **T 依赖**：电容/场/n/D 是经典静电、与 T 无关；变的是能谱分辨率（~4k_B T）与热漂移/热占据。E13 的 FFT 散射判据是**动量空间**测量（非能量分辨）→ 不受热展宽限制 → 室温可用 💭I。

## 7. STM 偏压约定与能量轴（E9 疑问 Q1）

- **sample voltage = bias voltage = tip bias = 针尖–样品直流偏压 V**，是同一个量。E9 横轴标 "Sample voltage (V)"，正文电场贡献里叫 "tip bias" 📜Q。
- **符号约定**：E9 的"样品电压"= 样品相对针尖的电位（针尖虚地、经前置放大器接地）。"sample voltage +0.5 V" = 样品比针尖高 0.5 V（等价针尖比样品低 0.5 V）。若改"给针尖加 V"，符号相反 $V_{tip}=-V_{sample}$——只有差值 $V_{tip}-V_{sample}$ 有物理意义。
- **能量轴**：$dI/dV$ 在偏压 V 处探测样品 LDOS 在 $E=E_F+eV$ 处，即 **V>0 探空态（导带）、V<0 探占据态（价带）**。自检：E9 SI 说"正背栅下导带极小在负 sample voltage"📜Q——n 掺杂使 $E_F$ 进导带 → $E_c<E_F$ → $V=(E_c-E_F)/e<0$。

## 8. 针尖的三重作用：能量窗口 / 局域 band bending / 局域开隙（E9 疑问 Q2，深化 §6）

改变 V 同时做**三件纠缠的事**（针尖是"部分地"像局部顶栅，不能当平面顶栅）：

1. **设隧穿能量窗口**（谱学轴）$E=E_F+eV$——主作用，本身不是栅作用。
2. **局域 band bending ≈ 局域 doping**：针尖局域电场把局域能带边相对**全局 E_F** 平移 → 局域载流子密度 n 变。但针尖**不积累全局电荷**（非充电式栅极），只做局域能带弯曲 💭I（§6③）。
3. **局域垂直场 → 双层开隙**：两层间 on-site 能量差 $2u=eEd$ → 局域 gap $\Delta$ 变。**只对双层**（单层只 doping、不改变能带）💭I。

关键分层：**E_F 是全局量**（由背栅/接触的全局 doping 定）；针尖**不动全局 E_F**，只平移局域能带相对 E_F（band bending，见 [PHY-EF]）。且 V 同时当"能量旋钮"和"场旋钮"→ 无法"固定能量扫场"或"固定场扫能量"。

## 9. 单背栅：n 与 D 锁定 + 电荷密度 vs 载流子密度（E9 疑问 Q3、Q0）

**单背栅（无顶栅，$V_{tg}=0$）代入 §1/§3**：

$$n=\frac{C_{bg}V_{bg}}{e},\qquad D=-\frac{C_{bg}V_{bg}}{2\varepsilon_0}$$

二者都 $\propto V_{bg}$、比例固定 → **n 与 D 锁定，不能独立调**（要独立需双栅共模/差模正交，§5）。Vbg 因此**同时**改 n（全局掺杂）**和** D（垂直场 → 双层开隙 → 能带改变）。

- **低温/高温**：n/D/场/gap 是经典静电量、与 T 无关；T 只改能谱分辨率（~$4k_BT$）、费米边热占据/热漂移、以及热激活跨隙填充的次级效应（E9 全 4.5 K、无变温）。

**电荷密度 vs 载流子密度**（不等价）：
- **carrier density n** = 可自由移动的载流子（电子/空穴）面密度，石墨烯文献通常指净超额 $n=|n_e-n_h|$，CNP 处 n=0。
- **charge density** = 总电荷面密度，含自由载流子**和**束缚电荷（极化/离化杂质）。
- 栅感应净电荷 $Q=CV$：**无能隙（或 E_F 在带内）** → 全部进自由载流子，$n=CV/e$；**gapped（E_F 在 gap 内）** → 几乎不产生自由载流子（价带满、导带空，$n\approx0$），而是进**层间极化**（两层电荷转移 → D → 开隙）。所以二者只在掺杂/金属区相等。

## 10. 层间 on-site 2u 与位移场 D、零场偏移（E9 疑问 Q5、Q6）

**2u 与 D 的关系**：$2u$ = 两层 on-site 能量差 = 层间势能差 = $e\cdot(\text{垂直电场})\cdot d$（$d\approx0.335$ nm 层间距）：

$$2u=e\,D\,d\ \propto\ D$$

（文献"D"即垂直电场、V/nm 单位。）小 u 极限下 gap $\Delta\approx2u$（$2u\ll\gamma_1\approx0.4$ eV）。E9 数值：$2u\approx\Delta\approx60$ meV @ Vg=60 V → $D=2u/(ed)\approx0.18$ V/nm（推导）。

**零场偏移（为何 E9 的 0 场在 Vg=−50 V 而非 0 V）**：层间垂直场有**三贡献** = 背栅 + 针尖偏压 + 针尖–TBLG 功函数失配 📜Q（正文 "contributions from the back gate voltage, the tip bias, and the work function mismatch"）。后两者给一个**内置偏移场**（接触电势差 $V_{CPD}=(\phi_{sample}-\phi_{tip})/e$ + 偏压 $V_b$）→ "give rise to an offset in gate voltage of the zero in the electric field" 📜Q → 零场点从 Vg=0 平移到 Vg=−50 V（Fig 3c 处 Vb=0.1 V、Vg=−50 V 电场≈0 📜Q）。

**为何功函数（局域量）进入 D**：STM 几何里 **D 从来不是"全局"的**——它是双层所在位置的局域垂直场，"全局"只有背栅那一项。功函数失配虽产生于针尖–样品的局域界面，但它修改了针尖的**边界电位**（叠加接触电势差），在针尖正下方贡献一个真实的内置垂直场；STM 只测针尖正下方那一小块 → 该局域内置场**就是**被测处 D 的一部分。一句话："全局 D"只适用于平面双栅均匀场；STM 里 D 是局域场，针尖电位（含功函数失配）是其边界条件。

## 11. STM 谱学开隙的两种途径：背栅 vs 针尖功函数（场-掺杂解耦）

双层石墨烯开隙（产生层间场 D）有两条途径，取舍不同：

| | 背栅 Vbg | 针尖功函数 Δw（换针尖材料） |
|---|---|---|
| 场范围 | **全局**（均匀） | **局域**（针尖下方） |
| 掺杂 | **n 与 D 锁定**（§9）→ 大 D 必重掺杂、E_F 进带 | **不全局掺杂**（局域场，全局 E_F 停 CNP） |
| 场强 | 弱：0.5 V/nm 需 ~73–170 V @ 285 nm SiO₂ | 强：Δw~0.5 eV 跨 ~1 nm → 0.5 V/nm |
| 器件要求 | 需栅电极 | **无需电极，任何绝缘衬底可用** |

**关键澄清（防误读）**：两种方法**都能**成像 gap 内态——因为 STS 的 V_b 轴独立于场，可扫到 E_F 上下的任意能量。**"成像 gap 内态" ≠ "E_F 在 gap 内"**。

- **背栅**：大 D 同时把 E_F 掺杂进带（n、D 锁定）。gap 内态要靠 V_b 扫到偏离 E_F 处（E9 Huang 2018 在 Vg=+60 V、V_b=−0.11 V 成像，此时 CNP 在 −0.1 V、E_F 已进导带 ~70–100 meV，见 E9 review §4.5）。
- **针尖功函数**：局域场、不全局掺杂 → E_F 真停 CNP、无自由载流子屏蔽，gap 内态在电中性下、近 V_b≈0 成像；且局域场只在针尖下、与探测位置重合。
- **实例（E14 Zheng 2022）**：W 尖（Δw≈0，场关）vs Au 尖（Δw 大，场开）在同一器件"开关"层间场，得 D=0.5 V/nm、U≈0.165 V、gap ~30–50 meV——靠 Δw 而非背栅（样品在 WSe₂/h-BN 绝缘衬底、无栅）。

**针尖功函数方案的真实优势** = ① 不全局掺杂（E_F 真停 CNP）② 场强更大 ③ 无需栅电极——**不是**"只有它才能成像 gap 内态"。
