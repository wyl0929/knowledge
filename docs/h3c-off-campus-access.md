# h3c 集群校外访问临时措施复盘

> 日期：2026-09-12
> 性质：**校外临时措施**（校外网络 + 校园 VPN 场景下，WSL 无法直连集群，改用 Windows Xshell 隧道桥接）
> 状态：生效中（仅校外使用；**恢复校内网络后应回退**，见 §5）

---

## 1. 问题现象

校外环境（WSL + 校园 VPN）连接 h3c 集群失败：

- `tnl`（`ssh -NfL 10022:slurm-login-1:22 h3cmaster`）报
  `ssh: connect to host 202.114.78.116 port 222: Connection timed out`
- `ssh h3clogin` 报 `ssh: connect to host 127.0.0.1 port 10022: Connection refused`
- 但 **Windows 侧 Xshell 能正常连接 h3c**

---

## 2. 根因分析

校园 VPN（深信服 EasyConnect 类）是**进程劫持型** VPN，不是纯路由型：

- 它通过虚拟网卡 + WFP 驱动，按**进程**劫持流量进隧道；
- Windows 进程（Xshell）的流量被正确劫持 → Xshell 能连；
- WSL 的流量（无论 NAT 还是 mirrored）不在劫持范围内，发到 VPN 虚拟网关后被静默丢弃。

### 关键证据链

| 检查 | 结果 |
|------|------|
| 本机公网（`223.5.5.5:53`） | ✅ 可达（排除断网/沙箱假阴性） |
| `202.114.78.116` ping / TCP 22/222/223 | ❌ 全超时 |
| 切 mirrored 后 WSL 路由表 | ✅ 已同步 VPN 路由（`202.114.78.0/25 via 2.0.0.4`） |
| ping VPN 网关 `2.0.0.4` | ❌ 100% 丢包 |

→ **路由表正确，但隧道不接 WSL 的包**，故「切换网络模式」本身治标不治本，必须借道 Windows 进程。

---

## 3. 做出的修改清单

### 修改 1：WSL2 切换到 mirrored（镜像）网络模式

- 文件：`C:\Users\22418\.wslconfig`（即 `/mnt/c/Users/22418/.wslconfig`，**新建**）
- 内容：
  ```ini
  [wsl2]
  networkingMode=mirrored
  ```
- 目的：让 WSL 与 Windows 共享网络栈（IP、路由、**localhost**），使 Xshell 隧道监听在 `127.0.0.1:10022` 的端口能被 WSL 直接访问。
- 生效方式：`wsl --shutdown` 重启 WSL 后生效。
- 副作用提示：mirrored 下 WSL 的 localhost 服务（如 dsh web 的 3080）也会暴露给 Windows 本机。

### 修改 2：Xshell 会话新增本地端口转发（手动）

- 位置：Xshell → h3c 会话 → 属性 → 连接 → SSH → 隧道 → 添加
- 类型：`Local (Outgoing)` / 本地传出
- 源主机：`127.0.0.1`，监听端口：`10022`
- 目标主机：`slurm-login-1`，目标端口：`22`
- 目的：在 Windows 侧建立 `10022 → slurm-login-1:22` 隧道，借 Xshell 的 VPN 通道完成第一段跳转。

### 修改 3：ControlMaster socket 重建（临时，非持久）

- 清理失效 socket：`rm -f ~/.ssh/controlmasters/ylwang@127.0.0.1:10022`
- 手动 `ssh h3clogin` 输一次密码短语，重建 ControlMaster（pid 9155）。

### 修改 4：known_hosts（间接，可能新增）

- `~/.ssh/known_hosts` 为 hashed 格式（`|1|...`），经新隧道连接 `slurm-login-1` 时可能新增一条 host key 记录。

---

## 4. 当前连接工作流（校外）

1. 保持校园 VPN 连接；
2. 保持 Xshell 的 h3c 会话连接（带 10022 隧道，**必须保持**）；
3. WSL 里 `ssh h3clogin`（首次输密码短语，之后 ControlMaster 免密）；
4. 可选 `h3c-poll` 后台续命（每 5min squeue，保持免密窗口）。

> ⚠️ 原 `tnl` 函数已不再使用（它依赖 WSL 直连 `202.114.78.116`，校外不可达）。
> 连接顺序变了：**先 Xshell，后 ssh h3clogin**。

---

## 5. 回退方案（恢复校内网络后执行）

1. 还原 `.wslconfig`：
   - 删除 `C:\Users\22418\.wslconfig`，或改为默认：
     ```ini
     [wsl2]
     networkingMode=nat
     ```
   - 然后 `wsl --shutdown` 重启。
2. 移除 Xshell 会话的 10022 隧道配置（可选，保留也无害但不必要）。
3. 恢复原流程：`tnl`（或 `ssh -NfL 10022:slurm-login-1:22 h3cmaster2`）→ `ssh h3clogin`。

---

## 6. 遗留问题 / 备忘

- `tnl` 函数用的是 `h3cmaster`（Port 222），但 config 里 `h3cmaster2` 是 Port 223，**端口不一致**，待确认哪个是当前正确入口。
- 集群 `module` 命令是 bmod 别名，非交互 shell 不展开（报 `module: command not found`）；SLURM 脚本需显式 `source /hpc/software/intel/oneapi/mpi/2021.9.0/env/vars.sh`。
- conda 环境：`tbplas`（当前激活）、`tbplas-exp`、`tbplas-exp-theta`、`tbplas-quad`（**无 `tbplas-alpha`**，与旧文档记录不一致）。
