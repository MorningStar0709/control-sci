这说明在 $V(t, x) = c$ 上 $\dot{V}$ 是负的；这样集合 $\{V(t, x) \leqslant c\}$ 是正不变集。因此，对于所有 $z(t_0) \in \{W_2(x) \leqslant c\}$ ，系统(9.27)的解 $z(t)$ 是一致有界的。由于 $\Omega$ 是在 $\{W_2(x) \leqslant c\}$ 内部的，所以只要 $y(t_0) \in \Omega$ 且 $\|z(t_0) - y(t_0)\| \leqslant \mu_1$ ，就存在 $\mu_1 > 0$ ，使得 $z(t_0) \in \{W_2(x) \leqslant c\}$ 。同样，对于 $y(t_0) \in \Omega, y(t)$ 一致有界，且当 $t$ 趋于无穷时， $y(t)$ 趋于零， $y(t)$ 在 $t_0$ 上一致。误差 $e(t) = z(t) - y(t)$ 满足方程

$$\dot {e} = \dot {z} - \dot {y} = f (t, z) + g (t, z) - f (t, y) = f (t, e) + \Delta (t, e) + g (t, z) \tag {9.31}$$

其中 $\Delta (t,e) = f(t,y(t) + e) - f(t,y(t)) - f(t,e)$

下面我们在球 $\{\| e\| \leqslant r\} \subset D$ 上分析误差方程(9.31)。方程(9.31)可以看成系统

$$\dot {e} = f (t, e)$$

的扰动,其原点是指数稳定的。由定理4.14可知,存在一个李雅普诺夫函数 $V(t,e)$ ,当 $\|e\|<r_{0}<r$ 时满足式(9.3)至式(9.5)。根据均值定理,误差项 $\Delta_{i}$ 可以写为

$$\Delta_ {i} (t, e) = \left[ \frac {\partial f _ {i}}{\partial x} (t, \lambda_ {1} e + y) - \frac {\partial f _ {i}}{\partial x} (t, \lambda_ {2} e) \right] e$$

其中 $0 < \lambda_{i} < 1$ 。由于雅可比矩阵 $[\partial f / \partial x]$ 对于 $x$ 是利普希茨的，对于 $t$ 一致，故扰动项 $(\Delta + g)$ 满足

$$\| \Delta (t, e) + g (t, z) \| \leqslant L _ {1} \| e \| ^ {2} + L _ {2} \| e \| \| y (t) \| + \delta$$

式中当 $t$ 趋于无穷时， $y(t)$ 趋于零，且 $y(t)$ 对于 $t_0$ 一致。因而对于所有 $\| e \| \leqslant r_1 < r_0$ ，有

$$\| \Delta (t, e) + g (t, z) \| \leqslant \{L _ {1} r _ {1} + L _ {2} \| y (t) \| \} \| e \| + \delta$$

该不等式当 $\gamma(t) = \{L_1 r_1 + L_2 \| y(t) \|\}$ 和 $\delta(t) \equiv \delta$ 时，取式(9.15)的形式。给定任意 $\varepsilon_1 > 0$ ，存在 $T_1 > 0$ ，使得对于所有 $t \geqslant t_0 + T_1$ ，有 $\|y(t)\| \leqslant \varepsilon_1$ 。因此式满足(9.20)，即

$$\int_ {t _ {0}} ^ {t} \gamma (\tau) d \tau \leqslant (\varepsilon_ {1} + L _ {1} r _ {1}) (t - t _ {0}) + T _ {1} \max _ {t \geqslant t _ {0}} L _ {2} \| y (t) \|$$

取 $\varepsilon_{1}$ 和 $r_1$ 足够小，即可满足式(9.21)。因此，引理9.4的所有假设成立，式(9.30)由式(9.23)得出。
