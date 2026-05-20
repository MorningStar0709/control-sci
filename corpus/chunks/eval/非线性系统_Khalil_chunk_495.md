# C. 5 证明引理 4.4

由于 $\alpha (\cdot)$ 是局部利普希茨的，因此对于每个初态 $y_0\geqslant 0$ ，方程都有唯一解。因为只要 $y(t) > 0$ ，就有 $\dot{y} (t) <   0$ ，所以方程的解具有对于所有 $t\geqslant t_0,y(t)\leqslant y_0$ 的特性。因此当 $t\geqslant t_0$ 时，方程的解有界且可扩展。通过积分，有

$$- \int_ {y _ {0}} ^ {y} \frac {d x}{\alpha (x)} = \int_ {t _ {0}} ^ {t} d \tau$$

令 $b$ 是小于 $a$ 的任意正数, 定义 $\eta(y) = -\int_{b}^{y} \frac{dx}{\alpha(x)}$

函数 $\eta(y)$ 在 $(0, a)$ 上是严格递减的可微函数，而且 $\lim_{y \to 0} \eta(y) = \infty$ 。该极限可根据以下两点得出。第一，因为只要 $y(t) > 0$ ，就有 $\dot{y}(t) = 0$ ，所以当 $t$ 趋于无穷时，微分方程的解 $y(t) < 0$ 。第二，极限 $y(t)$ 趋于零仅在 $t$ 趋于无穷时渐近出现，但由于解的唯一性，它不可能在有限时间出现。设 $c = -\lim_{y \to a} \eta(y)$ （ $c$ 可为 $\infty$ ），函数 $\eta$ 的值域为 $(-c, \infty)$ ，由于 $\eta$ 是严格递减的，其反函数 $\eta^{-1}$ 定义在 $(-c, \infty)$ ，对于任意 $y_0 > 0$ ，解 $y(t)$ 满足

$$\eta (y (t)) - \eta (y _ {0}) = t - t _ {0}$$

因此

$$y (t) = \eta^ {- 1} (\eta (y _ {0}) + t - t _ {0})$$

另一方面，如果 $y_0 = 0$ ，那么 $y(t)\equiv 0$ ，因为 $y = 0$ 是平衡点。定义函数 $\sigma (r,s)$ 为

$$
\sigma (r, s) = \left\{ \begin{array}{l l} \eta^ {- 1} (\eta (r) + s), & r > 0 \\ 0, & r = 0 \end{array} \right.
$$

则对于所有 $t \geqslant t_0$ 和 $y_0 \geqslant 0$ , 有 $y(t) = \sigma(y_0, t - t_0)$ 。由于 $\eta$ 和 $\eta^{-1}$ 在其定义域内都是连续的, 且 $\lim_{x \to \infty} \eta^{-1}(x) = 0$ , 所以函数 $\sigma$ 是连续的。对于每个固定的 $s, \sigma$ 在 $r$ 上是严格递增的, 因为

$$\frac {\partial}{\partial r} \sigma (r, s) = \frac {\alpha (\sigma (r , s))}{\alpha (r)} > 0$$

而对于每个固定的 $r, \sigma$ 在 $s$ 上是严格递减的，因为

$$\frac {\partial}{\partial s} \sigma (r, s) = - \alpha (\sigma (r, s)) < 0$$

此外，当 $s$ 趋于无穷时， $\sigma (r,s)$ 趋于零，故 $\sigma$ 是K类函数。
