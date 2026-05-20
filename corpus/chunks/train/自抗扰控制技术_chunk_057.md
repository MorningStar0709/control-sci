# 2.2 经典微分器

在经典调节理论中,对给定信号的微分信号是用如下微分环节

$$y = w (s) v = \frac {s}{T s + 1} v = \frac {1}{T} \left(1 - \frac {1}{T s + 1}\right) v \tag {2.2.1}$$

来得到的,式中 T 是比较小的时间常数.

这个微分环节可改写成

$$y = w (s) v = \frac {1}{T} \left(v - \frac {1}{T s + 1} v\right) \tag {2.2.2}$$

这里右边括号内的第二项是时间常数为 T 的惯性环节, 而第一项是把输入信号直接传递到输出的过程. 其等价的方块图如图 2.2.1 所示.

![](image/b1f64d07e0b1c359abf42fa9845d9f030380817049fceb1e86ecebcbde88a727.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["v(t)"] --> B["1/(Ts+1)"]
    B --> C((-))
    C --> D["1/T"]
    D --> E["v(t)"]
```
</details>

图2.2.1

如果把第二项惯性环节的输出记做 $v$ ，那么式(2.2.2)将满足等式

$$y (t) = \frac {1}{T} (v (t) - \bar {v} (t)) \tag {2.2.3}$$

于是根据前一节的讨论,当输入信号 $v(t)$ 的变化比较缓慢而时间常数 T 较小时,就有近似关系

$$\bar {v} (t) \approx v (t - T)$$

因此由式(2.2.2)，得

$$y (t) = \frac {1}{T} (v (t) - \bar {v} (t)) \approx \frac {1}{T} (v (t) - v (t - T)) \approx \dot {v} (t) \tag {2.2.4}$$

当然, 时间常数 T 越小, 输出 $y(t)$ 越接近微分 $\dot{v}(t)$ . 这就是微分环节 (2.2.1) 的数学含义.

可以说,这里的微分是用微分近似公式

$$\dot {v} (t) \approx \frac {v (t) - v (t - T)}{T} \tag {2.2.5}$$

来实现的. 式中的延迟信号 $v(t - T)$ 是通过惯性环节 $1 / (Ts + 1)$ 来实现. 这个惯性环节的时间常数越小, 延迟信号 $v(t - T)$ 越接近 $v(t)$ , 从而微分的近似度也就越高.

但是,如果输入信号 $v(t)$ 被随机噪声 $n(t)$ 所污染,那么由式(2.2.2)和式(2.2.3)得到

$$y (t) = \frac {1}{\tau} (v (t) + n (t) - \overline {{v (t) + n (t)}}) \tag {2.2.6}$$

式中， $v(t)+n(t)$ 是信号 $v(t)+n(t)$ 通过惯性环节 $\frac{1}{Ts+1}$ 所得信号，因此满足微分方程

$$\frac {\mathrm{d} y}{\mathrm{d} t} = - \frac {1}{T} (y - (v (t) + n (t)))$$

这个方程有解的表达式为

$$
\begin{array}{l} y (t) = \int_ {0} ^ {\infty} \mathrm{e} ^ {\frac {1}{\gamma} (t - \zeta)} (v (\zeta) + n (\zeta)) \mathrm{d} \zeta = \\ \int_ {0} ^ {\infty} \mathrm{e} ^ {\frac {1}{T} (t - \zeta)} v (\zeta) \mathrm{d} \zeta + \int_ {0} ^ {\infty} \mathrm{e} ^ {\frac {1}{T} (t - \zeta)} n (\zeta) \mathrm{d} \zeta \\ \end{array}
$$

在这里，由于 $n(\zeta)$ 是均值为0的高频噪声，因此积分项 $\int_0^\infty \mathrm{e}^{\frac{1}{T}(t - \zeta)}n(\zeta)\mathrm{d}\zeta$ 几乎等于零，右端积分只剩第一项$\int_0^\infty \mathrm{e}^{\frac{1}{T}(t - \zeta)}v(\zeta)\mathrm{d}\zeta \approx v(t - T).$ 由此等式(2.2.6)变成

$$y (t) \approx \frac {1}{T} (v (t) + n (t) - v (t - T)) =\frac {1}{T} (v (t) - v (t - T) + n (t)) \approx\dot {v} (t) + \frac {1}{T} n (t) \tag {2.2.7}$$

即输出信号 $y(t)$ 是输入信号 $v(t)$ 的微分信号叠加上放大了 1/T 倍的噪声信号，从而 T 越小，噪声放大越严重，完全可以淹没微分信号 $\dot{v}(t)$ 。这就是经典微分环节 (2.2.1) 的噪声放大效应。

为了消除或减弱噪声放大效应,把微分近似公式(2.2.5)换成另一种微分近似公式
