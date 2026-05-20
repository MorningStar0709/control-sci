![](image/6b50367605b1612b678312e5c393ddf4ed618ef9c3b59de1a0f97f4cc6823008.jpg)

<details>
<summary>line</summary>

| 时间/s | r | y |
| --- | --- | --- |
| 0 | 0 | 0 |
| 2 | 2 | 1 |
| 4 | 4 | 3 |
| 6 | 6 | 5 |
| 8 | 8 | 7 |
| 10 | 10 | 9 |
</details>

图 4.4 斜坡响应与 $K_{v}$ 之间的关系

应用式 $（4.33）$ ，这些结果可以概括为

$$K _ {\mathrm{p}} = \lim _ {s \rightarrow 0} G D _ {\mathrm{cl}} (s), \quad n = 0 \tag {4.36}K _ {\mathrm{v}} = \lim _ {s \rightarrow 0} s G D _ {\mathrm{cl}} (s), \quad n = 1 \tag {4.37}K _ {\mathrm{a}} = \lim _ {s \rightarrow 0} s ^ {2} G D _ {\mathrm{cl}} (s), n = 2 \tag {4.38}$$

稳态误差作为多项式输入阶以及系统类型的函数，选择合适的公式可计算系统稳态误

差，如表 4.1 所示。

表 4.1 误差关于系统类型的函数

<table><tr><td>型号输入</td><td>阶跃信号(位置信号)</td><td>斜坡信号(速度信号)</td><td>抛物线信号(加速度信号),</td></tr><tr><td>0型</td><td> $\frac{1}{1+K_p}$ </td><td> $+\infty$ </td><td> $+\infty$ </td></tr><tr><td>1型</td><td>0</td><td> $\frac{1}{K_v}$ </td><td> $+\infty$ </td></tr><tr><td>2型</td><td>0</td><td>0</td><td> $\frac{1}{K_a}$ </td></tr></table>
