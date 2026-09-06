<!--
 * @Author       : AI 整理 (从 E9 Huang 2018 精读疑问 Q4 + Q0–Q3 提炼)
 * @Date         : 2026-09-01
 * @Description  : [PHY-EF] 费米能/化学势 + 局域能带/band bending：Dirac/CNP/E_F 区分、计数积分、局域能带近似、filling factor
-->

# [PHY-EF] 费米能 E_F、化学势与局域能带（CNP/Dirac 区分 + band bending + 局域能带近似）

> 复现于所有 STM/STS 谱学与栅控文献（E9 Huang 2018 的静电学疑问、E13/E14 等）。核心：分清**能带参考量（固定）** vs **化学势（可变）**，以及**全局 E_F** vs **局域 band bending**。与 [PHY-GATE]（栅→n/D）互补：本讲义管"能量参考与费米能"，[PHY-GATE] 管"栅压→密度/场"。

## 1. 三个能量参考量：Dirac point / CNP / E_F

| 量 | 含义 | 性质 |
|----|------|------|
| **Dirac point** | 能带特征点（单层：导带价带接触点 $E=0$；双层：每层 Dirac 点被 $2u$ 劈裂） | **固定**能带参考 |
| **CNP（charge neutrality point）** | $n=0$ 的位置（能量或栅压 $V_{CNP}$）；gapped 体系在**能隙中心** | **固定**条件/参考点 |
| **E_F（费米能 = 化学势 μ，T=0）** | 由电子占据决定的可变能量 | **可变**，随掺杂移动 |

**关系**：CNP = "E_F 恰好落在电中性能量"的那个特殊点。未掺杂单层石墨烯里 **CNP(能量) = Dirac point(能量)**，此时 $E_F$ = Dirac point；掺杂后 $E_F$ 离开 Dirac point，但 Dirac point（能带参考）固定不动。E9（gapped 双层）里 CNP = 能隙中心（Fig 4b caption 把 band gap 与 CNP 并列标注 📜Q），实验上对应 AB 区谱的 dip（−0.1 V）。

## 2. E_F 由计数积分决定 + 随全局 doping 移动 + 平衡态全局均匀

**计数积分（T=0）**：

$$n=\int^{E_F}\rho(E)\,dE$$

- E_F 由 **DOS 形状 $\rho(E)$ 和 载流子密度 n 两者共同**决定。**改变 n（doping）→ E_F 移动**；"固定不动"的是 DOS 形状（能带结构），**不是 E_F**（易混点）。
- **E_F 是全局平衡量**：连通器件平衡态化学势处处相等（否则有电流），由背栅/接触的全局 n 决定。

**局域性质变化不动全局 E_F**（关键）：
- 计数积分只对**全局** DOS 和**全局** n 成立；针尖只改**局域** DOS，不改全局 n → 不触达这条全局关系。
- 针尖的局域场 → 局域能带边相对**固定 E_F** 平移 = **band bending**（§4）→ 局域 n 变，但 E_F 不动。
- 例外：若**全局**改变能带形状且**固定总 n**，E_F 会动（计数积分重排）——但单背栅里 n 与 D 锁定（[PHY-GATE] §9），做不到"固定 n 只改 gap"。

## 3. 局域能带近似与 LDOS（"局域能带还有意义吗、能算吗"）

- **严格的量是 LDOS $\rho(r,E)$**：按定义允许空间非均匀、不需周期平移对称，是 STM 直接测的量（E9 SI 算 "theoretical LDOS" 📜Q）。
- **能带 $E(k)$ 严格只在周期体系有定义**；针尖非均匀场破坏平移对称 → 无"全局能带"。
- **局域能带 = 绝热/局域近似（local band approximation）**：每个点 r 把局域势（moiré 位形 + 局域场 u(r)）当均匀参数对角化 → 局域能带 $E(k;u(r))$。E9 SI 标题即 "DENSITY OF STATES IN LOCAL BAND APPROXIMATION"，并在 $r_{DW}=\{0,9.4\ \text{nm}\}$、$r_{AB/BA}=\{\pm16\ \text{nm},0\}$ 处算局域电子结构/LDOS 📜Q。
- **成立条件**：势在载流子德布罗意波长 $\lambda_F$ 上缓变。尺度层级 $a$(0.246 nm) ≪ 针尖场尺度(≈nm) ≲ $\lambda_F$(≈10–30 nm) < moiré 周期 λ(57.6 nm)。moiré 势对晶格缓变 → 连续模型成立；针尖场对晶格缓变但对 moiré 是"局域" → 只能局域处理。
- **怎么算**：连续模型 + 局部参数（$w$、$u(r)$），线性四面体法 tight-binding（github tflovorn，E9 SI ref [3]）📜Q。tbplas 可直接对标。

## 4. 能带弯曲 band bending

局域静电势 $\phi(r)$ 把局域能带边 $E_{band}(r)=E_{band}^0-e\phi(r)$ 相对**全局 E_F** 平移；E_F 处处相等（平衡态）。局域能带边相对 E_F 的距离决定局域载流子密度：

- 局域能带边下移（相对 E_F）→ 局域电子增多（n 型局域掺杂）。
- 局域能带边上移 → 局域空穴增多（p 型）。
- 局域 DOS 形状（如 gap 开合）变，但 **E_F 全局不动**。

> 这是半导体结/接触能带弯曲的标准图景。对双层石墨烯，针尖局域场在两层间加电势差 → 局域开隙（band 形状变）+ 局域能带平移（band bending）同时发生；对单层只发生平移（doping），不改变带形状（[PHY-GATE] §8）。

## 5. filling factor ν：无量纲化载流子密度

**filling factor = 按自然量化单元计的载流子密度**，$\nu=n\times(\text{自然面积})/(\text{简并度})\propto n$，只差一个常数因子。两套常用约定：

| 语境 | 定义 | "自然单元" |
|------|------|-----------|
| **量子霍尔**（磁输运） | $\nu=\dfrac{n}{eB/h}=\dfrac{n\Phi_0}{B}$（$\Phi_0=h/e$） | 每磁通量子里的电子数 = 已填朗道能级数（→ [PHY-SDH]） |
| **moiré（魔角 TBG）** | $\nu=\dfrac{n}{n_0},\ n_0=\dfrac{4}{A_M},\ A_M=\frac{\sqrt3}{2}\lambda^2$ | 每 moiré 单胞电子数（以 4 重简并=2自旋×2谷为满带单位）（→ [PHY-MB] 的 $\Delta n=4/A$） |

- moiré 语境 $\nu=\pm4$ = 第一 moiré 带填满，$\nu=\pm2$ = 半满（correlated insulator），$\nu=0$ = CNP，负号 = 空穴掺杂。
- 两者都是"**把 n 归一化到某个量子化自然尺度**"，用来消除样品几何差异、直接比"填到哪里了"。
- 注意：E9 Huang 2018（θ=0.245°、无 B、主题是拓扑螺旋态）正文**不用** "filling factor"；moiré ν 是 Cao 2018 魔角那支关联文献的语言，其"按几何计数"的逻辑与 [PHY-MB] 的 $\Delta n=4/A$ 同源。

## 6. 论文事实层去向

E9 的具体数值（$E_0\approx-0.1$ eV、$2u\approx\Delta\approx60$ meV、$w\approx0.45$ eV、鞍点 ±256 meV、$E_c,m^*$ 等）属**论文事实层**，见 E9 review §4；本讲义只保留通用物理。
