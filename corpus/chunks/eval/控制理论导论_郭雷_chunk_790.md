$$\dot {E} (t) = - \alpha | \dot {y} ^ {\prime} (1, t) | ^ {2} - \beta | \dot {y} (1, t) | ^ {2}.$$

从而系统能量是耗散的。下面我们利用乘子法证明系统能量 $E(t)$ 是指数衰减的，即由 $\mathcal{A}$ 生成的半群 $T(t)$ 是指数稳定的。

令

$$E _ {\varepsilon} (x, t) = 2 (1 - \varepsilon) t E (t) + \int_ {0} ^ {1} x (\dot {y} \overline {{y}} + ^ {\prime} \overline {{\dot {y}}} y ^ {\prime}) \mathrm{d} x, \quad 0 < \varepsilon < 1.$$

于是

$$\dot {E} _ {\varepsilon} (t) = P _ {0} (t) + P _ {1} (t) + P _ {2} (t) + P _ {3} (t),$$

其中

$$P _ {0} (t) = - \int_ {0} ^ {1} \left(\varepsilon | \dot {y} | ^ {2} + (2 + \varepsilon) a ^ {4} | y ^ {\prime \prime} | ^ {2}\right) d x,P _ {1} (t) = - 2 (1 - \varepsilon) t a ^ {8} \left(\beta^ {- 1} | y ^ {\prime \prime \prime} (1, t) | ^ {2} + \alpha^ {- 1} | y ^ {\prime \prime} (1, t) | ^ {2}\right),P _ {2} (t) = a ^ {8} \beta^ {- 2} | y ^ {\prime \prime \prime} (1, t) | ^ {2} + a ^ {4} | y ^ {\prime \prime} (1, t) | ^ {2},P _ {3} (t) = - 2 a ^ {4} y ^ {\prime} (1, t) y ^ {\prime \prime \prime} (1, t) + 2 a ^ {4} y (1, t) y ^ {\prime \prime \prime} (1, t).$$

我们已经假定 $\beta > 0$ . 注意当 $\alpha = 0$ 时 $y''(1, t) = 0$ . 此外，我们有估计

$$
\begin{array}{l} - 2 a ^ {4} y ^ {\prime} (1, t) y ^ {\prime \prime \prime} (1, t) \leqslant a ^ {4} \left(\gamma | y ^ {\prime} (1, t) | ^ {2} + \gamma^ {- 1} | y ^ {\prime \prime \prime} (1, t) | ^ {2}\right) \\ \leqslant a ^ {4} \left(\gamma K \int_ {0} ^ {1} | y ^ {\prime \prime} (x, t) | ^ {2} \mathrm{d} x + \gamma^ {- 1} | y ^ {\prime \prime \prime} (1, t) | ^ {2}\right), \\ 2 a ^ {4} y (1, t) y ^ {\prime \prime \prime} (1, t) \leqslant a ^ {4} \left(\gamma | y (1, t) | ^ {2} + \gamma^ {- 1} | y ^ {\prime \prime \prime} (1, t) | ^ {2}\right) \\ \leqslant a ^ {4} \left(\gamma K \int_ {0} ^ {1} | y ^ {\prime \prime} (x, t) | ^ {2} \mathrm{d} x + \gamma^ {- 1} | y ^ {\prime \prime \prime} (1, t) | ^ {2}\right), \\ \end{array}
$$

其中 $K$ 为与 $y$ 无关的一正常数，而 $\gamma$ 为任意正数。由此可见，对于任意选定的 $\varepsilon \in (0,1)$ ，取 $\gamma > 0$ 充分小，当 $t$ 充分大时 $P_{2}(t)$ 和 $P_{3}(t)$ 能被 $P_{0}(t)$ 和 $P_{1}(t)$ 吸收，从而保证 $P_{0}(t) + P_{1}(t) + P_{2}(t) + P_{3}(t) \leqslant 0$ ，即存在 $T_{0} > 0$ 使得

$$\dot {E} _ {\varepsilon} (t) \leqslant 0, \quad \forall t > T _ {0}.$$

因此上述梁振动反馈控制系统 (10.4.23) 能量指数衰减.
