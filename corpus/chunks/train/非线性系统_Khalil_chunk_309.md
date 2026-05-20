\- 如果原点 $x = 0 \in D$ 是平均系统(10.24)的一个指数稳定平衡点, 则存在正常数 $\varepsilon^{*}$ 和 $k$ , 使得对于所有 $0 < \varepsilon < \varepsilon^{*}$ , 方程(10.23)有唯一的指数稳定、以 $T$ 为周期的解 $\bar{x}(t, \varepsilon)$ , 且有 $\| \bar{x}(t, \varepsilon) \| \leqslant k \varepsilon$ 。

如果对于所有 $(t, \varepsilon) \in [0, \infty) \times [0, \varepsilon_0]$ , $f(t, 0, \varepsilon) = 0$ , 则原点是方程(10.23)的一个平衡点。根据以 $T$ 为周期的解 $\bar{x}(t, \varepsilon)$ 的唯一性, 可得 $\bar{x}(t, \varepsilon)$ 是平凡解 $x = 0$ 。在这种情况下该定理保证原点是方程(10.23)的一个指数稳定平衡点。

例10.8 考虑线性系统

$$\dot {x} = \varepsilon A (t) x$$

其中 $A(t + T) = A(t),\varepsilon >0$ 。设 $\bar{A} = \frac{1}{T}\int_0^T A(\tau)d\tau$

平均系统为

$$\dot {x} = \varepsilon \bar {A} x$$

它在 $x = 0$ 处有一个平衡点。假设 $\overline{A}$ 是赫尔维茨矩阵，则由定理10.4可得，对于足够小的 $\varepsilon ,\dot{x} = \varepsilon A(t)x$ 在原点 $x = 0$ 的 $O(\varepsilon)$ 邻域内有唯一的周期为 $T$ 的解。但 $x = 0$ 是系统的平衡点，因此该周期解是平凡解 $x(t) = 0$ 。由此可得，对于足够小的 $\varepsilon ,x = 0$ 是非自治系统 $\dot{x} = \varepsilon A(t)x$ 的一个指数稳定平衡点。

例10.9 考虑标量系统 $\dot{x} = \varepsilon (x\sin^2 t - 0.5x^2) = \varepsilon f(t,x)$

函数 $f(t,x)$ 是以 $\pi$ 为周期的 $t$ 的函数。平均函数 $f_{\mathrm{av}}(x)$ 为

$$f _ {\mathrm{av}} (x) = \frac {1}{\pi} \int_ {0} ^ {\pi} (x \sin^ {2} t - 0. 5 x ^ {2}) d t = 0. 5 (x - x ^ {2})$$

平均系统

$$\dot {x} = 0. 5 \varepsilon (x - x ^ {2})$$

在 $x = 0$ 和 $x = 1$ 处有两个平衡点。在平衡点求得的雅可比函数 $df_{\mathrm{av}} / dx$ 的值为

$$\frac {d f _ {\mathrm{av}}}{d x} \Big | _ {x = 0} = (0. 5 - x) | _ {x = 0} = 0. 5\left. \frac {d f _ {\mathrm{av}}}{d x} \right| _ {x = 1} = (0. 5 - x) | _ {x = 1} = - 0. 5$$

这样,对于足够小的 $\varepsilon$ , 系统在 x=1 的 $O(\varepsilon)$ 邻域内有一个以 $\pi$ 为周期的指数稳定的解, 而且由函数 $x-x_{2}$ 的曲线可以看出, x=1 的吸引区是 $(0,\infty)$ 。因此, 对于在紧区间 $[a,b]\subset(0,\infty)$ 内的各初始状态, 用与原系统相同的初始状态作为平均系统的初始状态, 求解平均系统, 可得逼近

$$x (t, \varepsilon) - x _ {\mathrm{av}} (\varepsilon t) = O (\varepsilon), \forall t \geqslant 0$$

假设要计算二阶逼近,需要用变量代换(10.28)把问题表示为标准扰动问题,然后按照10.1节的方法逼近解。应用式(10.26)可以求得函数 $u(t,x)$ 为

$$u (t, x) = \int_ {0} ^ {t} (x \sin^ {2} \tau - 0. 5 x ^ {2} - 0. 5 x + 0. 5 x ^ {2}) d \tau = - \frac {1}{4} x \sin 2 t$$

变量代换(10.28)的形式为

$$x = y - \frac {1}{4} \varepsilon y \sin 2 t = \left(1 - \frac {1}{4} \varepsilon \sin 2 t\right) y$$

方程两边对 t 微分, 得

$$\dot {x} = \left(1 - \frac {1}{4} \varepsilon \sin 2 t\right) \dot {y} - \frac {1}{2} \varepsilon y \cos 2 t$$

因此 $\dot{y} = \frac{\varepsilon}{1 - (\varepsilon / 4)\sin 2t}\left(x\sin^2 t - \frac{1}{2} x^2 +\frac{1}{2} y\cos 2t\right)$

用 $y$ 表示 $x$ , 并将 $1 / [1 - (\varepsilon / 4) \sin 2t]$ 按幂级数展开
