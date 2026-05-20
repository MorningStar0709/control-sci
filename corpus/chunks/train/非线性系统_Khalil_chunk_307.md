其中 $h(t,x)=f(t,x,0)-f_{\mathrm{av}}(x)$ (10.27)

因为 $h(t,x)$ 是以 $T$ 为周期并具有零均值的 $t$ 的函数，函数 $u(t,x)$ 对 $t$ 的周期为 $T$ ，所以 $u(t,x)$ 对于所有 $(t,x)\in [0,\infty)\times D_0$ 有界。此外 $\partial u / \partial t$ 和 $\partial u / \partial x$ 由下式给出：

$$\frac {\partial u}{\partial t} = h (t, x), \quad \frac {\partial u}{\partial x} = \int_ {0} ^ {t} \frac {\partial h}{\partial x} (\tau , x) d \tau$$

它们是以 T 为周期的 t 的函数,且在 $[0,\infty)\times D_{0}$ 上有界,这里用到 $\partial h/\partial x$ 在 t 上是以 T 为周期的,且有零均值。考虑变量代换

$$x = y + \varepsilon u (t, y) \tag {10.28}$$

方程两边对 $t$ 微分，得 $\dot{x} = \dot{y} +\varepsilon \frac{\partial u}{\partial t} (t,y) + \varepsilon \frac{\partial u}{\partial y} (t,y)\dot{y}$

把方程(10.23)的 $\dot{x}$ 代入,求得新的状态变量 y 满足方程

$$
\begin{array}{l} \left[ I + \varepsilon \frac {\partial u}{\partial y} \right] \dot {y} = \varepsilon f (t, y + \varepsilon u, \varepsilon) - \varepsilon \frac {\partial u}{\partial t} \\ = \varepsilon f (t, y + \varepsilon u, \varepsilon) - \varepsilon f (t, y, 0) + \varepsilon f _ {\mathrm{av}} (y) \\ \stackrel {\text { def }} {=} \varepsilon f _ {\mathrm{av}} (y) + \varepsilon p (t, y, \varepsilon) \\ \end{array}
$$

其中 $p(t,y,\varepsilon)=[f(t,y+\varepsilon u,\varepsilon)-f(t,y,\varepsilon)]+[f(t,y,\varepsilon)-f(t,y,0)]$

函数 $p(t,y,\varepsilon)$ 是以 T 为周期的 t 的函数, 应用均值定理, 可将其表示为

$$p (t, y, \varepsilon) = F _ {1} (t, y, \varepsilon u, \varepsilon) \varepsilon u + F _ {2} (t, y, \varepsilon) \varepsilon$$

因为 $\partial u / \partial y$ 在 $[0, \infty) \times D_0$ 上有界，矩阵 $I + \varepsilon \partial u / \partial y$ 对于足够小的 $\varepsilon$ 是非奇异的，且

$$\left[ I + \varepsilon \frac {\partial u}{\partial y} \right] ^ {- 1} = I + O (\varepsilon)$$

因此,关于 y 的状态方程为

$$\dot {y} = \varepsilon f _ {\mathrm{av}} (y) + \varepsilon^ {2} q (t, y, \varepsilon) \tag {10.29}$$

其中， $q(t,y,\varepsilon)$ 是以 $T$ 为周期的 $t$ 的函数，且在 $[0,\infty)\times D_0$ 上对于足够小的 $\varepsilon$ ，函数 $f_{\mathrm{av}}$ 和 $q$ 及其关于 $(y,\varepsilon)$ 的一阶偏导数都是连续有界的。该方程是平均系统(10.24)的一个扰动。扩展前三节的讨论，可以确立用平均系统(10.24)的解去逼近方程(10.29)的解的基础。

进行时间变量代换 $s = \varepsilon t$ ，方程(10.29)变换为

$$\frac {d y}{d s} = f _ {\mathrm{av}} (y) + \varepsilon q (s / \varepsilon , y, \varepsilon) \tag {10.30}$$

其中， $q(s / \varepsilon ,y,\varepsilon)$ 是以 $\varepsilon T$ 为周期的 $s$ 的函数，对于足够小的 $\varepsilon$ ，在 $[0,\infty)\times D_0$ 上有界。应用定理3.4和定理3.5关于解对于初始状态和参数的连续性，可以看出，如果平均系统

$$\frac {d y}{d s} = f _ {\mathrm{av}} (y)$$
