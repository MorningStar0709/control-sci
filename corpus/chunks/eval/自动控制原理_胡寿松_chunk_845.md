$$\mathrm{K} = 2; \mathrm{T} = 0. 5; \mathrm{K} 3 = 1 2; \mathrm{K} 1 = 1 3 6. 6; \mathrm{K} 2 = 5 1 2;\mathrm{G0} = \mathrm{tf} (\mathrm{K}, [ \mathrm{T} ^ {- 2}, 2 * \mathrm{T}, 1 ]); \quad \% \text {定义开环传递函数}\mathrm{Gc} = \mathrm{tf} ([ \mathrm{K3}, \mathrm{K1}, \mathrm{K2} ], [ 0, 1, 0 ]); \quad \% \text {定义PID控制器传递函数}\mathrm{G} = \text { series } (\mathrm{G0}, \mathrm{Gc});\mathrm{Gp} = \mathrm{tf} (4 2. 6 7, [ 1, 1 1. 3 8, 4 2. 6 7 ]);\text { sys0 } = \text { feedback } (G, 1);\text { sys } = \text { series } (\text { sys0 }, \text { Gp });$$

step(sys); axis([0,1,0,1.3]); grid; %带前置滤波器的闭环传递函数

需要指出, 实际的被控对象不容许有过大的输入量, 因而图 10-13 系统中控制器 $G_{c}(s)$ 的输出 $u(t)$ 有最大允许值的限制, 这样, 系统自然频率 $\omega_{n}$ 的可选值将会受到约束。通常, 当 $e(t)$ 的最大值为 1 时, $u(t)$ 的数值将不得大于 100。为了说明 $u(t)$ 对 $\omega_{n}$ 的影响, 以图 10-13 系统为例, 并假设

$$G _ {0} (s) = \frac {1}{s (s + 1)}$$

在进行 ITAE 最优设计时, 可参考表 10-8 中给出的 $\omega_{n}$ 分别取 10, 20 和 40 时的 PID 控制器参数、前置滤波器和最优闭环传递函数。

表 10-8 不同 ${\omega }_{n}$ 下的设计结果

<table><tr><td rowspan="2">ωn</td><td colspan="3">PID</td><td rowspan="2">Gp(s)</td><td rowspan="2">Φ(s)</td></tr><tr><td>K3</td><td>K1</td><td>K2</td></tr><tr><td>10</td><td>16.5</td><td>215</td><td>1000</td><td>60.6/s2+13.03s+60.6</td><td>1000/s3+17.5s2+215s+1000</td></tr><tr><td>20</td><td>34</td><td>860</td><td>8000</td><td>235.29/s2+25.29s+235.29</td><td>8000/s3+35s2+860s+8000</td></tr><tr><td>40</td><td>69</td><td>3440</td><td>64000</td><td>927.54/s2+49.86s+927.54</td><td>64000/s3+70s2+3440s+64000</td></tr></table>

表 10-9 被控对象的最大输入

<table><tr><td>ωn</td><td>10</td><td>20</td><td>40</td></tr><tr><td>当输入为R(s)=1/s时,u(t)的最大值</td><td>35</td><td>135</td><td>550</td></tr><tr><td>调节时间/s</td><td>0.8</td><td>0.4</td><td>0.2</td></tr></table>

根据表 10-8 中给出的结果, 表 10-9 给出了 $\omega_{n}$ 分别等于 10, 20 和 40 时允许的 $u(t)$ 最大值。从中可以推知, 如果 $u(t)$ 的最大允许值为 100, 系统自然频率 $\omega_{n}$ 就不能大于 16。显然, 限制 $\omega_{n}$ 的取值范围, 也就限制了系统能达到的

最小调节时间。

当取 $\omega_{n}=10$ 时，系统的单位阶跃响应 $y(t)$ 及被控对象输入响应 $u(t)$ 分别如图 10-20 及图 10-21 所示。

![](image/a71c409fdbe8b067a07b71f83c5a6d7b300f11d1caddf3a2dc04b3348b6fbe84.jpg)

<details>
<summary>line</summary>

| Time/sec | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.1 | 0.2 |
| 0.2 | 0.5 |
| 0.3 | 0.8 |
| 0.4 | 1.0 |
| 0.5 | 1.0 |
| 0.6 | 1.0 |
| 0.7 | 1.0 |
| 0.8 | 1.0 |
| 0.9 | 1.0 |
| 1.0 | 1.0 |
</details>

图 10-20 系统的时间响应( $\omega_{n}=10$ )
(MATLAB)
