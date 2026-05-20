将式(7.41)中的上界代入方程(7.36)，可以看到 $\omega \in \Omega'$ 时半波对称周期解存在的必要条件是

$$\left| \frac {1}{G (j \omega)} + \Psi (a) \right| \leqslant \sigma (\omega)$$

从几何意义上讲,该条件说明点 $-\Psi(a)$ 必须包含于以 $1/G(j\omega)$ 为圆心、以 $\sigma(\omega)$ 为半径的圆内。对于每个 $\omega \in \Omega' \subset \Omega$ , 可以画出这样一个误差圆, 连通集 $\Omega'$ 上所有误差圆的包络形成了一条不确定带。这里选择 $\Omega$ 的子集是因为当 $\omega$ 接近 $\Omega$ 边缘时, 误差圆变为任意大, 不能给出有用的信息, 因而应根据能够画出较窄的不确定带原则选择子集 $\Omega'$ 。如果 $G(j\omega)$ 有锐截止的低通滤波特性, 那么在 $\Omega'$ 上的不确定带会相当窄。注意 $\rho(\omega)$ 是 $G(j\omega)$ 低通滤波器特性的测度, 由式(7.38)可以看出, 当 k > 1 时, $|G(jk\omega)|$ 越小, $\rho(\omega)$ 越大。由式(7.39)可以看出, 当 $\rho(\omega)$ 较大时, 得到误差圆的半径 $\sigma(\omega)$ 较小。

继续研究不确定带与 $-\Psi(a)$ 轨迹的相交情况。如果不确定带与 $-\Psi(a)$ 轨迹不相交，则显然当 $\omega \in \Omega'$ 时方程(7.36)无解；如果不确定带与 $-\Psi(a)$ 轨迹完全相交，如图7.20所示，则认为在 $\Omega'$ 内有解。如果排除一些退化的情况，在 $\Omega'$ 中就一定有解。实际上可以通过检测相交部分求出误差边界，设 $a_1$ 和 $a_2$ 是对应于 $-\Psi(a)$ 的轨迹与不确定带边界交点的幅度， $\omega_1$ 和 $\omega_2$ 是相应于半径分别为 $\sigma(\omega_1)$ 和 $\sigma(\omega_2)$ 的两个误差圆的频率，这两个误差圆的两边与 $-\Psi(a)$ 轨迹相切。在 $(\omega, a)$ 平面内定义矩形区域 $\Gamma$ 为

$$\Gamma = \left\{\left(\omega , a\right) \mid \omega_ {1} < \omega < \omega_ {2}, a _ {1} < a < a _ {2} \right\}$$

该区域包含 $1 / G$ 的轨迹与 $-\Psi$ 的交点 $(\omega_{s}, a_{s})$ ，即调和平衡方程(7.37)的解。这说明如果满足一定的正则条件，则有可能证明方程(7.36)在 $\Gamma$ 的闭包内有一个解。这些正则性条件是

$$\left. \frac {d}{d a} \Psi (a) \right| _ {a = a _ {s}} \neq 0; \quad \left. \frac {d}{d \omega} \mathrm{Im} [ G (j \omega) ] \right| _ {\omega = \omega_ {s}} \neq 0$$

![](image/0a426c4c389ea77c9b7ca203a3996e709866976f9a8939a0a4684e61714a0264.jpg)

<details>
<summary>text_image</summary>

-Ψ(a₁)
-β
不确定带 →
σ(ω₂)
-Ψ(a₂)
σ(ω₁)
-α
1/G(jω)
</details>

图7.20 完全相交

当 $1 / G(j\omega)$ 轨迹与 $-\Psi (a)$ 轨迹相交，且有限集 $\Gamma$ 有定义时, 不确定带与 $-\Psi(a)$ 轨迹之间的完全相交即可精确定义, 使得 $(\omega_{s}, a_{s})$ 为 $\Gamma$ 内的唯一交点, 且使正则性条件成立。

最后注意,在高频段,如果所有谐波(包括一次谐波)使所对应的 $1/G(j\omega)$ 的点位于临界圆外部,就不必画出不确定带。因此定义集合

$$\tilde {\Omega} = \left\{\omega \left| \left| \frac {\alpha + \beta}{2} + \frac {1}{G (j k \omega)} \right| > \frac {\beta - \alpha}{2}, k = 1, 3, 5, \dots \right. \right\}$$

并取 $\tilde{\Omega}$ 内的最小频率作为 $\Omega'$ 中的最大频率, 然后减小 $\omega$ , 直到误差圆变得非常大。

下面的判断描述函数法正确性的定理是本节的主要结果。

定理7.4 考虑图7.1所示的反馈连接,其中非线性特性 $\psi (\cdot)$ 是无记忆、时不变和奇对称的,斜率为 $\alpha$ 和 $\beta$ 之间的单值函数。在复平面内画出 $1 / G(j\omega)$ 和 $-\Psi (a)$ 的轨迹,并按照已描述的方法构造临界圆和不确定带,则
