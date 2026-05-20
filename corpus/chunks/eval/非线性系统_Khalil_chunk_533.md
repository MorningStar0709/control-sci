其中 $\beta$ 是 $\mathcal{KL}$ 类函数， $\varrho$ 是 $\mathcal{K}$ 类函数，且 $\mu_{2}$ 是正常数。选择 $T$ 足够大，使 $\beta (\mu_2,T) < \mu /2$ ，然后选择 $\varepsilon^{*} < \varepsilon_{1}^{*}$ 足够小，使 $\varrho (\varepsilon^{*}(1 + T)) < \mu /2$ 。由此可得，当 $\varepsilon < \varepsilon^{*}$ 时， $y(t,\varepsilon)$ 满足

$$\| y (t, \varepsilon) \| < \mu_ {1} + \mu / 2, \quad t \in [ t _ {0}, t _ {0} + \varepsilon T ] \text {且} \| y (t _ {0} + \varepsilon T, \varepsilon) \| < \mu \tag {C.79}$$

其中 $\mu_{1}=\beta(\mu_{2},0)$ 。根据式(C.77)和式(C.79)，当 $k_{1}>0$ 时有

$$\| y (t, \varepsilon) \| \leqslant k _ {1} \exp \left[ \frac {- \alpha (t - t _ {0})}{\varepsilon} \right] + \varepsilon \delta , \forall t \geqslant t _ {0} \tag {C.80}$$

考虑式(C.69)，将其右边记为

$$F (t, x, y, \varepsilon) = F (t, x, 0, 0) + [ F (t, x, y, \varepsilon) - F (t, x, 0, 0) ]$$

把式(C.69)看成降价系统(C.73)的扰动,括号内的扰动项满足

$$
\begin{array}{l} \| F (t, x, y, \varepsilon) - F (t, x, 0, 0) \| \leqslant \| F (t, x, y, \varepsilon) - F (t, x, y, 0) \| \\ + \left\| F (t, x, y, 0) - F (t, x, 0, 0) \right\| \\ \leqslant L _ {4} \varepsilon + L _ {5} \| y \| \\ \leqslant \theta_ {1} \varepsilon + \theta_ {2} \exp \left[ \frac {- \alpha (t - t _ {0})}{\varepsilon} \right] \\ \end{array}
$$

其中 $\theta_{1} = L_{4} + L_{5}\delta, \theta_{2} = L_{5}k_{1}$ 定义

$$u (t, \varepsilon) = x (t, \varepsilon) - \bar {x} (t)$$

则有 $u(t,\varepsilon) = \xi (\varepsilon) - \xi (0) + \int_{t_0}^t [F(s,x(s,\varepsilon),y(s,\varepsilon),\varepsilon) - F(s,\bar{x}(s),0,0)]ds$

$$= \xi (\varepsilon) - \xi (0) + \int_ {t _ {0}} ^ {t} [ F (s, x (s, \varepsilon), y (s, \varepsilon), \varepsilon) - F (s, x (s, \varepsilon), 0, 0) ] d s+ \int_ {t _ {0}} ^ {t} [ F (s, x (s, \varepsilon), 0, 0) - F (s, \bar {x} (s), 0, 0) ] d s$$

且 $\|u(t,\varepsilon)\|\leqslant k_{2}\varepsilon+\int_{t_{0}}^{t}\left\{\theta_{1}\varepsilon+\theta_{2}\exp\left[\frac{-\alpha(s-t_{0})}{\varepsilon}\right]\right\}ds+\int_{t_{0}}^{t}L_{6}\|u(s,\varepsilon)\|ds$

$$\leqslant k _ {2} \varepsilon + \left[ \theta_ {1} \varepsilon \left(t _ {1} - t _ {0}\right) + \frac {\theta_ {2} \varepsilon}{\alpha} \right] + \int_ {t _ {0}} ^ {t} L _ {6} \| u (s, \varepsilon) \| d s$$

由 Gronwall-Bellman 引理, 可得估计

$$\left\| x (t, \varepsilon) - \bar {x} (t) \right\| \leqslant \varepsilon k _ {3} \left[ 1 + t _ {1} - t _ {0} \right] \exp \left[ L _ {6} \left(t _ {1} - t _ {0}\right) \right] \tag {C.81}$$

这就证明了对 x 的误差估计。还可得出，对于足够小的 $\varepsilon$ ，解 $x(t, \varepsilon)$ 对于所有 $t \in [t_{0}, t_{1}]$ 有定义。
