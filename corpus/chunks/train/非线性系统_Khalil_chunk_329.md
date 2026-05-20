$$c _ {1} \| y \| ^ {2} \leqslant V (t, x, y) \leqslant c _ {2} \| y \| ^ {2} \tag {11.17}\frac {\partial V}{\partial y} g (t, x, y + h (t, x), 0) \leqslant - c _ {3} \| y \| ^ {2} \tag {11.18}$$

则当估计值为 $\rho_{0}=\rho\sqrt{c_{1}/c_{2}}, k=\sqrt{c_{2}/c_{1}}, \gamma=c_{3}/2c_{2}$ (11.19)

时,式(11.5)成立,其中 $B_{\rho}\subset D_{y}$ 。

定理11.1 考虑方程(11.6)和方程(11.7)的奇异扰动问题,并设 $z = h(t,x)$ 是方程(11.3)的孤立的根,假设对于所有 $[t,x,z - h(t,x),\varepsilon ]\in [0,t_1]\times D_x\times D_y\times [0,\varepsilon_0]$

其中 $D_{x}\subset R^{n},D_{y}\subset R^{m},D_{x}$ 是凸集， $D_{y}$ 包含原点，且下列条件成立：

- 函数 $f$ 和 $g$ 及其关于 $(x, z, \varepsilon)$ 的一阶偏导数，以及 $g$ 关于 $t$ 的一阶偏导数都是连续的，函数 $h(t, x)$ 和雅可比矩阵 $[\partial g(t, x, z, 0) / \partial z]$ 有关于其自变量的连续一阶偏导数，初始数据 $\xi(\varepsilon)$ 和 $\eta(\varepsilon)$ 是 $\varepsilon$ 的光滑函数。  
- 对于 $t \in [t_0, t_1]$ , 降阶问题(11.8)有唯一解 $\bar{x}(t) \in S$ , 其中 $S$ 是 $D_x$ 的一个紧子集。  
- 原点是边界层模型(11.14)的一个指数稳定平衡点,对于 $(t,x)$ 是一致的。设 $R_{y}\subset D_{y}$ 是方程(11.3)的吸引区, $\Omega_{y}$ 是 $R_{y}$ 的一个紧子集。

则存在个正常数 $\varepsilon^{*}$ , 使得对于所有 $\eta_{0} - h(t_{0}, \xi_{0}) \in \Omega_{y}$ 和 $0 < \varepsilon < \varepsilon^{*}$ , 方程(11.6) \~ 方程(11.7)的奇异扰动问题在 $[t_{0}, t_{1}]$ 上有唯一解 $x(t, \varepsilon), z(t, \varepsilon)$ , 且

$$x (t, \varepsilon) - \bar {x} (t) = O (\varepsilon) \tag {11.20}z (t, \varepsilon) - h (t, \bar {x} (t)) - \hat {y} (t - t _ {0} / \varepsilon) = O (\varepsilon) \tag {11.21}$$

对于 $t \in [t_0, t_1]$ 一致成立，其中 $\hat{y}(\tau)$ 是边界层模型(11.13)的解，此外给定任意 $t_b > t_0$ ，存在 $\varepsilon^{**} \leqslant \varepsilon^*$ ，使得对于 $t \in [t_b, t_1]$ ，只要 $\varepsilon < \varepsilon^{**}$ ，则

$$z (t, \varepsilon) - h (t, \bar {x} (t)) = O (\varepsilon) \tag {11.22}$$

一致成立。

证明: 见附录 C.17。

该定理称为 Tikhonov 定理 $^{①}$ ，其证明用到边界层模型的稳定性性质，以证明

$$\| y (t, \varepsilon) \| \leqslant k _ {1} \exp \left[ \frac {- \alpha (t - t _ {0})}{\varepsilon} \right] + \varepsilon \delta$$

把上述边界用于方程(11.10)以证明(11.20)，这似乎还不够明确，由于 $\int_{0}^{t}\exp(-\alpha s/\varepsilon)ds$ 是 $O(\varepsilon)$ 。再利用方程(11.11)在 $\tau$ 时间尺度的误差分析，即可完成式(11.21)和式(11.22)的证明。

例 11.5 考虑例 11.1 中的直流电机, 设奇异扰动问题为

$$\dot {x} = z, \quad x (0) = \xi_ {0}\varepsilon \dot {z} = - x - z + u (t), \quad z (0) = \eta_ {0}$$

假设对于 $t \geqslant 0, u(t) = t$ ，我们希望在[0,1]区间上解状态方程。方程(11.3)的唯一根是 $h(t,x) = -x + t$ ，且边界层模型(11.14)为

$$\frac {d y}{d \tau} = - y$$

显然,边界层系统的原点是全局指数稳定的。降阶问题

$$\dot {x} = - x + t, \quad x (0) = \xi_ {0}$$

有唯一解 $\bar{x} (t) = t - 1 + (1 + \xi_0)\exp (-t)$
