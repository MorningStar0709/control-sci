# (3) 过阻尼单位斜坡响应

在 $\zeta>1$ 时，输出量的拉氏变换式可写为

$$C (s) = \frac {1}{s ^ {2}} - \frac {\frac {2 \zeta}{\omega_ {n}}}{s} + \frac {\frac {2 \zeta}{\omega_ {n}} (s + \zeta \omega_ {n}) + (2 \zeta^ {2} - 1)}{\left[ s + \omega_ {n} (\zeta - \sqrt {\zeta^ {2} - 1}) \right] \left[ s + \omega_ {n} (\zeta + \sqrt {\zeta^ {2} - 1}) \right]}$$

所以得

$$
\begin{array}{l} c (t) = t - \frac {2 \zeta}{\omega_ {n}} + \frac {2 \zeta^ {2} - 1 + 2 \zeta \sqrt {\zeta^ {2} - 1}}{2 \omega_ {n} \sqrt {\zeta^ {2} - 1}} e ^ {- (\zeta - \sqrt {\zeta^ {2} - 1}) \omega_ {n} t} \\ - \frac {2 \zeta^ {2} - 1 - 2 \zeta \sqrt {\zeta^ {2} - 1}}{2 \omega_ {n} \sqrt {\zeta^ {2} - 1}} \mathrm{e} ^ {- (\zeta + \sqrt {\zeta^ {2} - 1}) \omega_ {n} t}, \quad t \geqslant 0 \tag {3-37} \\ \end{array}
$$

显然，稳态误差

$$e _ {s} (\infty) = \frac {2 \zeta}{\omega_ {n}}$$

误差响应

$$
\begin{array}{l} e (t) = \frac {2 \zeta}{\omega_ {n}} \left[ 1 - \frac {2 \zeta^ {2} - 1 + 2 \zeta \sqrt {\zeta^ {2} - 1}}{4 \zeta \sqrt {\zeta^ {2} - 1}} e ^ {- (\zeta - \sqrt {\zeta^ {2} - 1}) \omega_ {n} t} \right. \\ \left. + \frac {2 \zeta^ {2} - 1 - 2 \zeta \sqrt {\zeta^ {2} - 1}}{4 \zeta \sqrt {\zeta^ {2} - 1}} e ^ {- (\zeta + \sqrt {\zeta^ {2} - 1}) \omega_ {n} t} \right] \tag {3-38} \\ \end{array}
$$

一般来说，在单位斜坡输入信号作用下，过阻尼二阶系统的动态性能指标只能用计算机求得。

例 3-3 设控制系统如图 3-19 所示。图中，输入信号 $\theta_{i}(t)=t$ ，放大器增益 $K_{a}$ 分别取为 13.5,200 和 $1500(\mathrm{rad/s})^{2}$ 。试分别写出系统的误差响应表达式，并估算其性能指标。

![](image/b4f7b11e94c684a0fb8e8f84806a1fa882f7f6b9d713bf8de33f34e9c6997c6e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Θi(s)"] --> B((+))
    B --> C["Θe(s)"]
    C --> D["5Ka/(s+34.5)"]
    D --> E["Θo(s)"]
    E --> F["-"]
    F --> B
```
</details>

图 3-19 控制系统

解 由图知,系统开环传递函数为

$$G (s) = \frac {5 K _ {a}}{s (s + 3 4 . 5)} = \frac {\omega_ {n} ^ {2}}{s (s + 2 \zeta \omega_ {n})}$$

因而， $\zeta = 17.25 / \sqrt{5K_a}, \omega_n = \sqrt{5K_a}$ 。

当 $K_{a} = 13.5(\mathrm{rad / s})^{2}$ 时，算得 $\zeta = 2.1, \omega_{n} = 8.2$

rad/s,属过阻尼二阶系统。由式(3-38)可得

$$
\begin{array}{l} \theta_ {e} (t) = 0. 5 1 \left(1 - e ^ {- 2. 0 8 t} + 0. 0 0 4 e ^ {- 3 2. 4 t}\right) \\ \approx 0. 5 1 \left(1 - e ^ {- 2. 0 8 t}\right) \\ \end{array}
$$

此时，系统等效为一阶系统，其等效时间常数 $T = 0.48\mathrm{s}$ 。因而性能指标： $t_r = 1.06\mathrm{s}, t_s = 1.44\mathrm{s},$ $\theta_{\mathrm{ess}}(\infty) = 0.51\mathrm{rad}$ 。

当 $K_{a} = 200(\mathrm{rad / s})^{2}$ 时，算得 $\zeta = 0.55, \omega_{n} = 31.6\mathrm{rad / s}$ ，属于欠阻尼二阶系统。由式(3-29)可得
