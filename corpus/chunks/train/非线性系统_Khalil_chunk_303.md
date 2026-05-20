$$\dot {z} = f (z + \bar {x} (t, \varepsilon)) - f (\bar {x} (t, \varepsilon)) + \varepsilon [ g (t, z + \bar {x} (t, \varepsilon), \varepsilon) - g (t, \bar {x} (t, \varepsilon), \varepsilon) ]\stackrel {\text { def }} {=} \hat {f} (t, z)$$

在 $z = 0$ 处线性化得

$$
\begin{array}{l} \left. \frac {\partial \hat {f}}{\partial z} \right| _ {z = 0} = \left. \frac {\partial f}{\partial x} \right| _ {z = 0} + \varepsilon \left. \frac {\partial g}{\partial x} \right| _ {z = 0} \\ = A + \left[ \frac {\partial f}{\partial x} (\bar {x} (t, \varepsilon)) - A \right] + \varepsilon \frac {\partial g}{\partial x} (t, \bar {x} (t, \varepsilon), \varepsilon) \\ \end{array}
$$

由 $[\partial f / \partial x]$ 的连续性可知，对于任意 $\delta > 0$ ，存在 $\varepsilon^{*} > 0$ ，使得当 $\varepsilon < \varepsilon^{*}$ 时，有

$$\left\| \frac {\partial f}{\partial x} (\bar {x} (t, \varepsilon)) - \frac {\partial f}{\partial x} (0) \right\| < \delta$$

由于 A 是赫尔维茨矩阵, 且 $\left[\frac{\partial g}{\partial x}\right](t,\bar{x},\varepsilon)$ 为 $O(1)$ , 从引理 9.1 可以推出, 对于足够小的 $\varepsilon$ , 线性系统

$$\dot {y} = \left[ A + \left(\frac {\partial f}{\partial x} (\bar {x} (t, \varepsilon)) - A\right) + \varepsilon \frac {\partial g}{\partial x} (t, \bar {x} (t, \varepsilon), \varepsilon) \right] y$$

在 y=0 处有一个指数稳定平衡点。因此，由定理 4.13 可知 z=0 是指数稳定平衡点。

![](image/3d559d7e71aa6197d254ccd9916239fac05b3c76d894a4ef7a0406c32fce214c.jpg)

下面的定理是上述结果的总结。
