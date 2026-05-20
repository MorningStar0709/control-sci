$$\left\| F (t, x, y, \varepsilon) \right\| \leqslant k _ {0}; \quad \left\| G (t, x, y, \varepsilon) - G (t, x, y, 0) \right\| \leqslant \varepsilon L _ {3}$$

可得 $\dot{V}_{1} \leqslant -\frac{c_{3}}{\varepsilon}\|y\|^{2} + c_{4}L_{3}\|y\| + c_{5}\|y\|^{2} + c_{6}k_{0}\|y\|^{2}$

$$\leqslant - \frac {c _ {3}}{2 \varepsilon} \| y \| ^ {2} + c _ {4} L _ {3} \| y \|, \quad \varepsilon \leqslant \frac {c _ {3}}{2 c _ {5} + 2 c _ {6} k _ {0}}$$

这样,如果在某一时刻 $t^{*} \geqslant t_{0}$ ，有 $\|y(t^{*}, \varepsilon)\| < \rho_{0} \sqrt{c_{1}/c_{2}} \stackrel{\text{def}}{=} \mu$ ，则全部问题的解 $y(x, \varepsilon)$ 将满足按指数衰减的边界

$$\| y (t, \varepsilon) \| \leqslant \mu \sqrt {c _ {2} / c _ {1}} \exp \left[ \frac {- \alpha (t - t ^ {*})}{\varepsilon} \right] + \varepsilon \delta , \forall t \geqslant t ^ {*} \tag {C.77}$$

其中 $\alpha = c_{3} / 4c_{2},\delta = 2c_{2}c_{4}L_{3} / c_{1}c_{3}$ 。此外， $y(t_0,\varepsilon) = \eta (\varepsilon) - h(t_0,\xi (\varepsilon)) = \eta_0 - h(t_0,\xi_0) + O(\varepsilon)$ 及 $\eta_0 - h(t_0,\xi_0)$ 属于 $\Omega_y,\Omega_y$ 是边界层模型

$$\frac {d y}{d \tau} = G (t _ {0}, \xi_ {0}, y, 0) = g (t _ {0}, \xi_ {0}, y + h (t _ {0}, \xi_ {0}), 0) \tag {C.78}$$

吸引区的紧子集。回顾(逆李雅普诺夫)定理4.17可知,存在一个李雅普诺夫函数 $V_{0}(y)$ ，在吸引区上满足

$$\frac {\partial V _ {0}}{\partial y} g (t _ {0}, \xi_ {0}, y + h (t _ {0}, \xi_ {0}), 0) \leqslant - W _ {0} (y)$$

其中 $W_{0}(y)$ 是正定的，且对于任意 $c > 0, \{V_{0}(y) \leqslant c\}$ 是吸引区的紧子集。选择 $c_{0}$ ，使得 $\Omega_{y}$ 在 $\{V_{0}(y) \leqslant c_{0}\}$ 内， $V_{0}$ 沿整个系统(C.69)～(C.70)轨线的导数为

$$
\begin{array}{l} \dot {V} _ {0} = \frac {1}{\varepsilon} \frac {\partial V _ {0}}{\partial y} G (t, x, y, \varepsilon) \\ = \frac {1}{\varepsilon} \frac {\partial V _ {0}}{\partial y} G \left(t _ {0}, \xi_ {0}, y, 0\right) + \frac {1}{\varepsilon} \frac {\partial V _ {0}}{\partial y} [ G (t, x, y, \varepsilon) - G \left(t _ {0}, \xi_ {0}, y, 0\right) ] \\ \end{array}
$$

可以验证,对于所有 $(t,y)\in[t_{0},t_{0}+\varepsilon T]\times\{V_{0}(y)\leqslant c_{0}\}$ 及某一 $a_{0}>0$ ,有

$$\dot {V} _ {0} \leqslant \frac {1}{\varepsilon} [ - W _ {0} (y) + a _ {0} \varepsilon (1 + T) ]$$

应用定理4.18证明存在 $\varepsilon_1^* >0$ ，使得对于 $0 <   \varepsilon <  \varepsilon_{1}^{*},y(t,\varepsilon)$ 在区间 $[t_0,t_0 + \varepsilon T]$ 上满足不等式

$$\| y (t, \varepsilon) \| \leqslant \beta (\mu_ {2}, (t - t _ {0}) / \varepsilon) + \varrho (\varepsilon (1 + T))$$
