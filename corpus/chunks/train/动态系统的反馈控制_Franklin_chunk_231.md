![](image/bfa47fb908d679e39ffbdba8d932cc7260f0d14b443ca7803a3523a2784250d9.jpg)

<details>
<summary>line</summary>

| 时间/s | 脉冲响应 |
| --- | --- |
| 0 | 0.0000 |
| 20 | 0.0090 |
| 40 | -0.0080 |
| 60 | 0.0090 |
| 80 | -0.0080 |
| 100 | 0.0090 |
| 120 | -0.0070 |
</details>

图 4.16 中立稳定系统

表 4.3 基于极限灵敏度法的齐格勒-尼科尔斯调节器 $D_{c}(s)=k_{p}(1+1/T_{1}s+T_{D}s)$ 的整定

<table><tr><td>控制器类型</td><td>最优增益</td></tr><tr><td>P</td><td> $k_{\text{P}} = 0.5K_{\text{u}}$ </td></tr><tr><td>PI</td><td> $\begin{cases} k_{\text{P}} = 0.45K_{\text{u}} \\ T_{\text{I}} = \frac{P_{\text{u}}}{1.2} \end{cases}$ </td></tr><tr><td>PID</td><td> $\begin{cases} k_{\text{P}} = 1.6K_{\text{u}} \\ T_{\text{I}} = 0.5P_{\text{u}} \\ T_{\text{D}} = 0.125P_{\text{u}} \end{cases}$ </td></tr></table>

大量的实验表明，齐格勒-尼科尔斯提出的控制器参数整定方法对于大多数闭环系统都能获得可以接受的闭环响应特性。从后面的例子中可知，用阶跃响应方法得到的增益一般比极限灵敏度法得到的高。要使系统的控制效果更好，就必须以上述方法确定的系统参数为初始条件重复地微调各个参数。
