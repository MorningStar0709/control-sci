$$\frac {1}{1 - (\varepsilon / 4) \sin 2 t} = 1 + \frac {1}{4} \varepsilon \sin 2 t + O \left(\varepsilon^ {2}\right)$$

得到方程 $\dot{y}=\frac{1}{2}\varepsilon(y-y^{2})+\frac{1}{16}\varepsilon^{2}(y\sin4t+2y^{2}\sin2t)+O(\varepsilon^{3})$

该系统作为平均系统的扰动出现。为了求出二阶逼近,需要按照有限项泰勒级数

$$y = y _ {0} + \varepsilon y _ {1} + \varepsilon^ {2} R _ {y}$$

计算 $y_{0}$ 和 $y_{1}$ 。我们知道 $y_{0} = x_{\mathrm{av}}$ 是平均系统的解。关于 $y_{1}$ 的方程为

$$\dot {y} _ {1} = \varepsilon \left[ \left(\frac {1}{2} - y _ {0} (t)\right) y _ {1} + \frac {1}{1 6} y _ {0} (t) \sin 4 t + \frac {1}{8} y _ {0} ^ {2} (t) \sin 2 t \right], \quad y _ {1} (0) = 0$$

这里假设初始状态 $x(0)$ 与 $\varepsilon$ 无关。应用式(10.28)，得到 $x$ 的二阶逼近

$$x = \left(1 - \frac {1}{4} \varepsilon \sin 2 t\right) x _ {\mathrm{av}} (\varepsilon t) + \varepsilon y _ {1} (t, \varepsilon) + O (\varepsilon^ {2})$$

图 10.5 所示为当 $x(0)=0.7, \varepsilon=0.3$ 时，精确系统、平均系统和二阶逼近的解。该图清楚地说明了平均系统的解如何平均精确解，二阶逼近几乎和精确解一样，但当解达到稳定状态时可以看出其差别。

![](image/036473bff4bc3d01c32810868efc9bed5312b9c973e0283dbfc98a9bde93f66f.jpg)

<details>
<summary>line</summary>

| 时间 | 实线 | 液线 |
| --- | --- | --- |
| 0 | 0.68 | 0.70 |
| 5 | 0.90 | 0.82 |
| 10 | 0.85 | 0.88 |
| 15 | 1.02 | 0.94 |
| 20 | 0.90 | 0.98 |
| 25 | 1.05 | 0.99 |
| 30 | 1.01 | 1.00 |
</details>

图 10.5 例 10.9 在 $\varepsilon = 0.3$ 时的解: 精确解(实线)、平均解(虚线)和二阶逼近(点划线)

例 10.10 考虑 1.2.1 节的悬摆, 假设悬点服从小幅高频的垂直振动。假设悬点运动可由 $a \sin \omega t$ 描述, 其中 a 是振幅, $\omega$ 是频率。写出切线方向(与杆垂直)的牛顿定律运动方程为①

$$m (l \ddot {\theta} - a \omega^ {2} \sin \omega t \sin \theta) = - m g \sin \theta - k (l \dot {\theta} + a \omega \cos \omega t \sin \theta)$$

假设 $a / l \ll 1, \omega_0 / \omega \ll 1$ ，其中 $\omega_0 = \sqrt{g / l}$ 是悬摆在下平衡点 $\theta = 0$ 附近的自由振荡频率。设 $\varepsilon = a / l$ ，并记 $\omega_0 / \omega = \alpha \varepsilon$ ，其中 $\alpha = \omega_0 l / \omega a$ 。又设 $\beta = k / m\omega_0$ ，并将时间尺度由 $t$ 变为 $\tau = \omega t$ 。在新的时间尺度上，运动方程为

$$\frac {d ^ {2} \theta}{d \tau^ {2}} + \alpha \beta \varepsilon \frac {d \theta}{d \tau} + (\alpha^ {2} \varepsilon^ {2} - \varepsilon \sin \tau) \sin \theta + \alpha \beta \varepsilon^ {2} \cos \tau \sin \theta = 0$$

以 $x_{1} = \theta ,\quad x_{2} = \frac{1}{\varepsilon}\frac{d\theta}{d\tau} +\cos \tau \sin \theta$

作为状态变量,状态方程为 $\frac{dx}{d\tau} = \varepsilon f(\tau, x)$ (10.31)

其中 $f_{1}(\tau ,x) = x_{2} - \sin x_{1}\cos \tau$

$$f _ {2} (\tau , x) = - \alpha \beta x _ {2} - \alpha^ {2} \sin x _ {1} + x _ {2} \cos x _ {1} \cos \tau - \sin x _ {1} \cos x _ {1} \cos^ {2} \tau$$
