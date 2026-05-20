# 8.3.2 仿真实例

被控对象为

$$G (s) = \frac {1 3 3}{s ^ {2} + 2 5 s}$$

位置指令信号为 $\cos t$ ，采样时间为 1ms，采用 z 变换进行离散化，经过 z 变换后的离散化对象为

$$y (k) = - \mathrm{den} (2) y (k - 1) - \mathrm{den} (3) y (k - 2) + \mathrm{num} (2) u (k - 1) + \mathrm{num} (3) u (k - 2)$$

针对误差 e 及误差变化率 $\Delta e$ ，分别采用三个隶属函数进行模糊化，即 $\mu_{1}(x)=\exp\left[-\left(\frac{x+\pi/6}{\pi/12}\right)^{2}\right]$ ， $\mu_{2}(x)=\exp\left[-\left(\frac{x}{\pi/12}\right)^{2}\right]$ ， $\mu_{3}(x)=\exp\left[-\left(\frac{x-\pi/6}{\pi/12}\right)^{2}\right]$ ，隶属函数如图 8-7 所示。

![](image/2049f0c65275bcd04822859bea81c25d781f67bcae7be3bf76b238f039a7fea9.jpg)

<details>
<summary>line</summary>

| x | Membership function |
| --- | --- |
| -0.8 | 0.0 |
| -0.6 | 0.2 |
| -0.4 | 0.5 |
| -0.2 | 0.7 |
| 0.0 | 1.0 |
| 0.2 | 0.7 |
| 0.4 | 0.5 |
| 0.6 | 0.2 |
</details>

图 8-7 e 和 $\Delta e$ 的隶属函数度曲线

采用经验确定模糊规则表，根据实际被控对象和指令信号，将控制规则表设计为表8-2的形式。采用控制律式（8.26），正弦位置跟踪结果如图8-8所示。可见，控制器性能的好坏决定于控制规则表，而采用经验很难确定控制性能高的规则表。可采用定性分析及遗传算法对规则表中规则的数目和规则表中的数值进行优化[2]。

表 8-2 控制规则表

<table><tr><td rowspan="2" colspan="2"> $u_{ij}$ </td><td colspan="3"> $\Delta e$ </td></tr><tr><td>N</td><td>Z</td><td>P</td></tr><tr><td rowspan="3">e</td><td>N</td><td>-200</td><td>-100</td><td>0</td></tr><tr><td>Z</td><td>-100</td><td>0</td><td>100</td></tr><tr><td>P</td><td>0</td><td>100</td><td>200</td></tr></table>

![](image/84b43eb054cf273c52de3cfb8f7ed3d270b3dc809cea968ad65337d8927572b5.jpg)

<details>
<summary>line</summary>

| Time(s) | ideal position | position tracking |
| --- | --- | --- |
| 0 | 1.5 | 1.5 |
| 5 | -1.0 | -1.0 |
| 10 | 1.0 | 1.0 |
| 15 | -1.0 | -1.0 |
| 20 | 1.0 | 1.0 |
| 25 | -1.0 | -1.0 |
| 30 | 0.5 | 0.5 |
</details>

图 8-8 正弦位置跟踪
