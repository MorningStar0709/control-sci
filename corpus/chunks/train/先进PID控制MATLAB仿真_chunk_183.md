# 2.7.1 基本原理

考虑如下被控对象：

$$G _ {\mathrm{p}} (s) = \frac {1}{T _ {\mathrm{p}} s + 1} \mathrm{e} ^ {- \tau s} \tag {2.26}$$

PID 控制算法为

$$u (t) = \frac {1}{\delta} \left(e + \frac {1}{T _ {\mathrm{I}}} \int_ {0} ^ {t} e \mathrm{d} t + T _ {\mathrm{D}} \frac {\mathrm{d} e}{\mathrm{d} t}\right) \tag {2.27}$$

步骤如下：

（1）先采用比例控制，从较大的比例度 $\delta$ 开始，逐步减小比例度，使系统对阶跃输入的响应达到临界振荡状态。将此时的比例度记作 $\delta_{r}$ ，临界振荡周期记作 $T_{r}$ 。临界振荡曲线如图 2-21 所示。  
（2）根据 Ziegler-Nichols 提供的临界比例度法经验公式确定 PID 控制器参数，见表 2-2。本方法适用于有自平衡能力的被控对象。

![](image/dc3670703729e3ddb4eca4049d6d235416775eba0168489d02ecffacd70e60ce.jpg)

<details>
<summary>line</summary>

| t | y |
| --- | --- |
| t₀ | 0 |
| Tr | 1 |
</details>

图 2-21 临界振荡曲线

表 2-2 临界比例度法整定 PID 参数

<table><tr><td>控制器类型</td><td>比例度 $\delta \%$ </td><td>积分时间 $T_{\mathrm {I}}$ </td><td>微分时间 $T_{\mathrm {D}}$ </td></tr><tr><td>P</td><td> $2\delta_{\mathrm {r}}$ </td><td></td><td></td></tr><tr><td>PI</td><td> $2.2\delta_{\mathrm {r}}$ </td><td> $0.85T_{\mathrm {r}}$ </td><td></td></tr><tr><td>PID</td><td> $1.7\delta_{\mathrm {r}}$ </td><td> $0.5T_{\mathrm {r}}$ </td><td> $0.13T_{\mathrm {r}}$ </td></tr></table>

![](image/f30256bee46b5e1af5b8979d19ff42d509e0d27f5f2fcae173d4b496af0f5c68.jpg)
