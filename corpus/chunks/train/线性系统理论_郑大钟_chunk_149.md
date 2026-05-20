又因 $\alpha (\| x\|)$ 为连续非减且 $\alpha (0) = 0$ ，从而由上式即可导出，对满足 $\| x_0\| \leqslant \delta (\varepsilon)$ 的一切 $x_0$ 和一切 $t\geqslant t_0$ 都成立

$$\left\| \phi (t; x _ {0}, t _ {0}) \right\| \leqslant \varepsilon , \quad \forall t \geqslant t _ {0} \tag {4.36}$$

这表明，对给定的任一实数 $\varepsilon > 0$ 都对应地存在一个实数 $\delta(\varepsilon) > 0$ ，使得由满足 $\|x_0\| \leqslant \delta(\varepsilon)$ 的任一初态 $x_0$ 出发的受扰运动都满足不等式 (4.36)，且 $\delta(\varepsilon)$ 和初始时刻 $t_0$ 的选取无关。因此，根据定义可知，原点平衡状态 $x = 0$ 为一致稳定。

![](image/b670741a21936487975bb092a79d16c9d74847ae5fc60cf2e19ce15d25317f10.jpg)

<details>
<summary>line</summary>

| x | β(ε) | V(x, t) | α(ε) |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| δ(ε) | ~0.5 | ~0.2 | 0 |
| ε | 1 | 1 | 0 |
</details>

图4.4 定理条件(i)的几何描述

![](image/5953f19a4c4895d761e680046e089f13150555f757ded4b87574b12253bb07fc.jpg)

<details>
<summary>line</summary>

| x | α(ε) | β(δ) | α(μ) | β(ν) |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| μ | 0 | 0 | 0 | 0 |
| δ(ε) | 0 | 0 | 0 | 0 |
| ε | 0 | 0 | 0 | 0 |
</details>

图4.5 对选取 $T(\mu, \delta)$ 的几何说明

② 证明由满足 $\| x_0\| \leqslant \delta (\varepsilon)$ 的任一初始状态 $x_0$ 出发的运动 $\phi (t;x_0,t_0)$ ，其中初始时刻 $t_0$ 为任意值，当 $t\to \infty$ 时都收敛于原点平衡状态 $x = 0$ 。

首先，对任意给定的一个实数 $\mu > 0$ 和对于 $\delta(\varepsilon) > 0$ ，来找出对应的实数 $T(\mu, \delta) > 0$ 。设初始时刻 $t_0$ 为任意， $x_0$ 为满足 $\| x_0 \| \leqslant \delta(\varepsilon)$ 的任一初始状态，且任给 $0 <$ $\mu < \| x_0\|$ 。则利用 $V(x,t)$ 的有界性，可如图4.5所示那样，由给定的 $\mu > 0$ 找出对应的实数 $\nu (\mu) > 0$ ，使得 $\beta (\nu)\leqslant \alpha (\mu)$ 。再知 $\gamma (\| x\|)$ 为连续非减函数，且令 $\rho (\mu ,\delta)$ 为 $\gamma (\| x\|)$ 在区间 $\nu (\mu)\leqslant \| x\| \leqslant \varepsilon$ 上的极小值，则就取

$$T (\mu , \delta) = \frac {\beta (\delta)}{\rho (\mu , \delta)} \tag {4.37}$$

而且可知，对给定的每一个实数 $\mu > 0$ ， $T(\mu, \delta)$ 必对应地存在。

其次，对满足 $t_0 \leqslant t_2 \leqslant t_0 + T(\mu, \delta)$ 的某个时刻 $t_2$ ，来推证 $\| \phi(t_2; x_0, t_0) \| = v(\mu)$ 。表 $t_1 = t_0 + T(\mu, \delta)$ ，且反设对满足 $t_0 \leqslant t \leqslant t_1$ 的所有 $t$ 均有 $\| \phi(t; x_0, t_0) \| > v(\mu)$ ，则利用 $V(x, t)$ 的有界性和 $V(x, t)$ 的负定，可由此导出

$$
\begin{array}{l} 0 <   \alpha (\nu) \leqslant V \left(\phi \left(t _ {1}; x _ {0}, t _ {0}\right), t _ {1}\right) \leqslant V \left(x _ {0}, t _ {0}\right) \\ \leqslant V \left(x _ {0}, t _ {0}\right) - \left(t _ {1} - t _ {0}\right) \rho (\mu , \delta) \leqslant \beta (\delta) - T (\mu , \delta) \rho (\mu , \delta) \\ = \beta (\delta) - \beta (\delta) = 0 \tag {4.38} \\ \end{array}
$$
