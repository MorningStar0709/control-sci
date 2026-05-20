# 2.3.2 仿真实例

求三阶传递函数的阶跃响应

$$G _ {\mathrm{p}} (s) = \frac {5 2 3 5 0 0}{s ^ {3} + 8 7 . 3 5 s ^ {2} + 1 0 4 7 0 s}$$

其中,对象采样时间为 1ms。

采用 z 变换进行离散化, 经过 z 变换后的离散化对象为

$$
\begin{array}{l} y (k) = - \mathrm{den} (2) y (k - 1) - \mathrm{den} (3) y (k - 2) - \mathrm{den} (4) y (k - 3) \\ + \mathrm{num} (2) u (k - 1) + \mathrm{num} (3) u (k - 2) + \mathrm{num} (4) u (k - 3) \tag {2.6} \\ \end{array}
$$

对式(2.6)说明如下:首先针对传递函数 $G_{\mathrm{p}}(s)$ ，采用Matlab函数c2d将 $G_{\mathrm{p}}(s)$ 转化为如下离散系统

$$G (z) = \frac {\mathrm{num} (2) z ^ {2} + \mathrm{num} (3) z + \mathrm{num} (4)}{\mathrm{den} (1) z ^ {3} + \mathrm{den} (2) z ^ {2} + \mathrm{den} (3) z + \mathrm{den} (4)}$$

分子分母分别除以 $z^3$ ，可得

$$G (z) = \frac {\mathrm{num} (2) z ^ {- 1} + \mathrm{num} (3) z ^ {- 2} + \mathrm{num} (4) z ^ {- 3}}{\mathrm{den} (1) + \mathrm{den} (2) z ^ {- 1} + \mathrm{den} (3) z ^ {- 2} + \mathrm{den} (4) z ^ {- 3}}$$

令 $G(z) = \frac{Y(z)}{U(z)}$ ，则结合上式交叉相乘可得

$$
\begin{array}{l} (\mathrm{den} (1) + \mathrm{den} (2) z ^ {- 1} + \mathrm{den} (3) z ^ {- 2} + \mathrm{den} (4) z ^ {- 3}) Y (z) \\ = (\operatorname{num} (2) z ^ {- 1} + \operatorname{num} (3) z ^ {- 2} + \operatorname{num} (4) z ^ {- 3}) U (z) \\ \end{array}
$$

由仿真可知 $\mathrm{den}(1) = 1$ ，则

$$
\begin{array}{l} Y (z) + \mathrm{den} (2) z ^ {- 1} Y (z) + \mathrm{den} (3) z ^ {- 2} Y (z) + \mathrm{den} (4) z ^ {- 3} Y (z) \\ = \operatorname{num} (2) z ^ {- 1} U (z) + \operatorname{num} (3) z ^ {- 2} U (z) + \operatorname{num} (4) z ^ {- 3} U (z) \\ \end{array}
$$

即

$$
\begin{array}{l} Y (z) = - \operatorname{den} (2) z ^ {- 1} Y (z) - \operatorname{den} (3) z ^ {- 2} Y (z) - \operatorname{den} (4) z ^ {- 3} Y (z) \\ + \mathrm{num} (2) z ^ {- 1} U (z) + \mathrm{num} (3) z ^ {- 2} U (z) + \mathrm{num} (4) z ^ {- 3} U (z) \\ \end{array}
$$

则被控对象的离散化表达式为式(2.6)。

采用专家 PID 设计控制器。在仿真过程中， $\varepsilon$ 取 0.001，程序中的 5 条规则与控制算法的 5 种情况相对应。

专家 PID 控制仿真程序见本章附录程序 chap2\_1.m，仿真结果如图 2-6 和图 2-7 所示。

![](image/0c0aa8010b3d4984448de27885180684141f7d8e0a9d1051526c5b5dd8f02ee1.jpg)

<details>
<summary>line</summary>

| time(s) | r,y |
| --- | --- |
| 0.00 | 0.00 |
| 0.05 | 1.00 |
| 0.10 | 1.00 |
| 0.15 | 1.00 |
| 0.20 | 1.00 |
| 0.25 | 1.00 |
| 0.30 | 1.00 |
| 0.35 | 1.00 |
| 0.40 | 1.00 |
| 0.45 | 1.00 |
| 0.50 | 1.00 |
</details>

图 2-6 PID 控制阶跃响应曲线

![](image/16e77f77382028bf541204e210d466e8d82b82b8669451cea68a867b2ab4787d.jpg)

<details>
<summary>line</summary>

| time(s) | error |
| --- | --- |
| 0.00 | 1.0 |
| 0.05 | 0.2 |
| 0.10 | 0.0 |
| 0.15 | 0.0 |
| 0.20 | 0.0 |
| 0.25 | 0.0 |
| 0.30 | 0.0 |
| 0.35 | 0.0 |
| 0.40 | 0.0 |
| 0.45 | 0.0 |
| 0.50 | 0.0 |
</details>

图2-7 误差响应曲线
