# 2.1 小时间常数惯性环节

下面考察小时间常数一阶惯性环节的一个典型性质.

一阶惯性环节的传递函数为

$$y = w (s) u = \frac {k}{T s + 1} u \tag {2.1.1}$$

式中：k 为系统放大系数；T 为时间常数。

记 $\alpha = \frac{1}{T}$ ，则

$$y = \frac {\alpha k}{s + \alpha} u \tag {2.1.2}$$

则传递函数(2.1.1)的状态空间实现为

$$\dot {y} = - \alpha (y - k u (t)) \tag {2.1.3}$$

当 $u(t) = 1$ ，初值为 $y(0) = 0$ 时的解 $y(t)$ 称为此系统的阶跃响

应. 这个阶跃响应(即系统(2.1.3)的解)的表达式为

$$y (t) = \mathrm{e} ^ {- \alpha t} \int_ {0} ^ {t} \mathrm{e} ^ {\alpha \tau} \alpha k u (\tau) \mathrm{d} \tau = \alpha k \mathrm{e} ^ {- \alpha t} \int_ {0} ^ {t} \mathrm{e} ^ {\alpha \tau} \mathrm{d} \tau = k (1 - \mathrm{e} ^ {- \alpha t}) \tag {2.1.4}$$

图2.1.1显示的是 $k = 2$ ，而 $\alpha$ 取三个不同值 $\alpha = 1, \alpha = 2, \alpha = 0.5$ 时的阶跃响应曲线.

![](image/f021800aa6f72786c089c825c6788a73a9049b479e1df806366721d9d16486d8.jpg)

<details>
<summary>line</summary>

| x | α=2 | α=1 | α=0.5 |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 1 | 1.4 | 1.2 | 0.8 |
| 2 | 1.6 | 1.4 | 1.0 |
| 3 | 1.7 | 1.5 | 1.1 |
| 4 | 1.8 | 1.6 | 1.2 |
| 5 | 1.85 | 1.7 | 1.3 |
| 6 | 1.9 | 1.8 | 1.4 |
| 7 | 1.95 | 1.85 | 1.5 |
| 8 | 1.98 | 1.9 | 1.6 |
| 9 | 2.0 | 1.95 | 1.7 |
| 10 | 2.0 | 2.0 | 1.8 |
</details>

图2.1.1

从图2.1.1中看出，放大系数 $k$ 是系统输出放大输入信号的倍数，而时间常数决定系统输出达到设定常值2的速度，因此时间常数越小，上升到2的速度越快．根据阶跃响应的表达式(2.1.4)，令 $t = T$ ，由于 $\alpha = \frac{1}{T}$ 就得

$$y (T) = k \left(1 - \mathrm{e} ^ {- 1}\right) = k \left(1 - \frac {1}{\mathrm{e}}\right) = k \left(1 - \frac {1}{2 . 7 1 8}\right) \approx 0. 6 3 k$$

于是时间常数 T 是系统输出 y 从 0 上升到目标值 1 的 63% 行程所需要的时间.

下面考察 $k = 1$ ，时间常数 $T$ 很小，即 $\alpha$ 很大，输入 $u(t)$ 为缓变的时变函数时的近似解．系统的解的表达式

$$y (t) = \alpha \mathrm{e} ^ {- \alpha t} \int_ {0} ^ {t} \mathrm{e} ^ {\alpha \zeta} u (\zeta) \mathrm{d} \zeta$$

经过分部积分,得

$$y (t) = \alpha \mathrm{e} ^ {- \alpha t} \left(\frac {1}{\alpha} \mathrm{e} ^ {\alpha \zeta} u (\zeta) \right. \Big | _ {0} ^ {t} - \frac {1}{\alpha} \int_ {0} ^ {t} \mathrm{e} ^ {\alpha \zeta} \dot {u} (\zeta) \mathrm{d} \zeta) =u (t) - \mathrm{e} ^ {- \alpha t} u (0) - \mathrm{e} ^ {- \alpha t} \int_ {0} ^ {t} \mathrm{e} ^ {\alpha \zeta} \dot {u} (\zeta) \mathrm{d} \zeta =u (t) - \mathrm{e} ^ {- \alpha t} u (0) - \frac {1}{\alpha} (\dot {u} (t) - \mathrm{e} ^ {- \alpha t} \dot {u} (0) + \mathrm{e} ^ {- \alpha t} \int_ {0} ^ {t} \mathrm{e} ^ {\alpha \zeta} \ddot {u} (\zeta) \mathrm{d} \zeta) =u (t) - \frac {1}{\alpha} \dot {u} (t) + e ^ {- \alpha t} \left(u (0) - \frac {1}{\alpha} \ddot {u} (0) + \frac {1}{\alpha} \int_ {0} ^ {t} e ^ {\alpha \zeta} \ddot {u} (\zeta) d \zeta\right)$$
