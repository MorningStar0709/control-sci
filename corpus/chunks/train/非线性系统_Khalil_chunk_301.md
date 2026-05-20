# 10.3 自治系统的周期扰动

考虑系统

$$\dot {x} = f (x) + \varepsilon g (t, x, \varepsilon) \tag {10.15}$$

其中,对于每个紧集 $D_{0}\subset D$ ,以及所有 $(t,x,\varepsilon)\in[0,\infty)\times D_{0}\times[-\varepsilon_{0},\varepsilon_{0}]$ ,f和g及其关于x的一阶偏导数是连续有界的, $D\subset R^{n}$ 是包含原点的定义域。假设原点是自治系统

$$\dot {x} = f (x) \tag {10.16}$$

的指数稳定平衡点,也就是说①矩阵 $A=\left[\partial f/\partial x\right](0)$ 是赫尔维茨矩阵。由于 g 的有界性,我们可应用定理 4.14 和引理 9.2 证明存在 r>0 和 $\varepsilon_{1}>0$ ,使得对于所有 $\|x(0)\|\leqslant r$ 和 $|\varepsilon|\leqslant\varepsilon_{1}$ ,方程(10.15)的解是一致毕竟有界的,其最终边界与 $|\varepsilon|$ 成比例。换句话说,当 t 趋于无穷时,所有的解趋于原点的 $O(\varepsilon)$ 邻域，这对任何有界的 $g$ 都成立。本节关心的是当 $g$ 在时间 $t$ 上以 $T$ 为周期，即

$$g (t + T, x, \varepsilon) = g (t, x, \varepsilon), \forall (t, x, \varepsilon) \in [ 0, \infty) \times D \times [ - \varepsilon_ {0}, \varepsilon_ {0} ]$$

时,在 $O(\varepsilon)$ 邻域内会发生什么,特别应该关注在原点的 $O(\varepsilon)$ 邻域内存在以 T 为周期的解的可能性。

设 $\phi (t;t_0,x_0,\varepsilon)$ 是方程(10.15)始于 $(t_0,x_0)$ 的解，即 $x_0 = \phi (t_0;t_0,x_0,\varepsilon)$ 。对于所有 $\| x\| < r$ 定义映射 $P_{\varepsilon}(x)$ 为 $P_{\varepsilon}(x) = \phi (T;0,x,\varepsilon)$

即当初始状态在零时刻为 x 时, $P_{\varepsilon}(x)$ 是系统在 T 时刻的状态。该映射在研究方程(10.15)存在周期解的问题中,起着关键作用①。

引理 10.1 在上述条件下, 方程(10.15)有一个周期为 T 的解, 当且仅当方程

$$x = P _ {\varepsilon} (x) \tag {10.17}$$

有解。

◇

证明:由于 g 在 t 上以 T 为周期,所以当时移 T 的整数倍时,方程(10.15)的解不变。特别地, $\phi(t+T;T,x,\varepsilon)=\phi(t;0,x,\varepsilon),\quad\forall t\geqslant0$ (10.18)

通过变量代换可看出这一点,即把时间变量 t 变换为 $\tau = t - T$ , 得

$$\frac {d x}{d \tau} = f (x) + \varepsilon g (\tau + T, x, \varepsilon) = f (x) + \varepsilon g (\tau , x, \varepsilon)$$

另一方面，由解的唯一性，有

$$\phi (t + T; 0, x, \varepsilon) = \phi (t + T; T, \phi (T; 0, x, \varepsilon), \varepsilon), \quad \forall t \geqslant 0 \tag {10.19}$$

为了证明充分性,设

$$p _ {\varepsilon} = P _ {\varepsilon} (p _ {\varepsilon}) = \phi (T; 0, p _ {\varepsilon}, \varepsilon)$$

则有 $\phi (t + T;0,p_{\varepsilon},\varepsilon) = \phi (t + T;T,\phi (T;0,p_{\varepsilon},\varepsilon),\varepsilon)$

$$= \phi (t + T; T, p _ {\varepsilon}, \varepsilon) \tag {10.20}= \phi (t; 0, p _ {\varepsilon}, \varepsilon)$$

其中,第一个等号根据式(10.19)得出,最后一个等号根据式(10.18)得出。方程(10.20)说明始于 $(0,p_{\varepsilon})$ 的解是以T为周期的。为证明必要性,设 $\bar{x}(t)$ 是方程(10.15)的以T为周期的解。设 $y=\bar{x}(0)$ ,则有

$$\phi (t + T; 0, y, \varepsilon) = \phi (t; 0, y, \varepsilon), \quad \forall t \geqslant 0$$
