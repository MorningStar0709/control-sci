# 11.2.3 仿真实例

设某伺服系统参数： $R = 7.77\Omega$ ， $K_{m} = 6N \cdot m/A$ ， $C_{e} = 1.2V/(rad/s)$ ， $J = 0.6kg \cdot m^{2}$ ， $K_{u} = 11V/V$ 。摩擦模型参数取 $F_{c} = 15N \cdot m$ ， $F_{m} = 20N \cdot m$ ， $a_{1} = 1.0$ ， $k_{v} = 2.0Nms/rad$ ， $\alpha = 0.01$ 。

采用连续系统仿真，运行 Simulink 主程序 chap11\_3sim.mdl，正弦跟踪信号指令为 $y_{\mathrm{d}}(t)=0.10\sin(2\pi t)$ ，采用 PD 控制 $u(t)=200e(t)+40\dot{e}(t)$ ，带有摩擦环节的 PID 控制仿真结果如图 11-5 和图 11-6 所示。仿真结果表明，在带有摩擦条件下，位置跟踪存在“平顶”现象，速度跟踪存在“死区”现象。采用 PID 控制鲁棒性差，不能达到高精度跟踪。

![](image/ad08be65553d65bf58759da94ab2040a3fe1e01fee59926d0e2eb2a5565894ee.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 0.1 | 0.1 |
| 1.0 | 0.0 | 0.0 |
| 1.5 | -0.1 | -0.1 |
| 2.0 | 0.0 | 0.0 |
| 2.5 | 0.1 | 0.1 |
| 3.0 | 0.0 | 0.0 |
</details>

![](image/f238dacb0e468d04033a6a690ae532024e110aae1a8dec74d8cfe87530a6593d.jpg)

<details>
<summary>line</summary>

| time(s) | ideal speed signal | speed tracking |
| --- | --- | --- |
| 0.0 | 0.5 | 0.5 |
| 0.5 | -0.5 | -0.5 |
| 1.0 | 0.5 | 0.5 |
| 1.5 | -0.5 | -0.5 |
| 2.0 | 0.5 | 0.5 |
| 2.5 | -0.5 | -0.5 |
| 3.0 | 0.5 | 0.5 |
</details>

图 11-5 带摩擦时的位置和速度跟踪

![](image/ba8c5b05bd3c6c428cdce3978730403f8c2d0a1358bd1c721193189a60c68649.jpg)

<details>
<summary>line</summary>

| Angle speed | Friction force |
| --- | --- |
| -0.8 | -20 |
| -0.6 | -20 |
| -0.4 | -20 |
| -0.2 | -20 |
| 0 | 0 |
| 0.2 | 20 |
| 0.4 | 20 |
| 0.6 | 20 |
| 0.8 | 20 |
</details>

图 11-6 摩擦力 $F_{\mathrm{f}}(t)$ 的变化
