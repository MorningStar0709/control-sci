定义常数 $\alpha$ 和 $\rho$ 为 $\alpha = \frac{1}{2}\left[\frac{c_3}{c_2} -\varepsilon \frac{c_4}{c_1}\right] > 0,\quad \rho = \exp \left(\frac{c_4\eta}{2c_1}\right)\geqslant 1$ (9.22)

将式(9.20)和式(9.21)代入式(9.19),可得

$$\| x (t) \| \leqslant \sqrt {\frac {c _ {2}}{c _ {1}}} \rho \| x (t _ {0}) \| e ^ {- \alpha (t - t _ {0})} + \frac {c _ {4} \rho}{2 c _ {1}} \int_ {t _ {0}} ^ {t} e ^ {- \alpha (t - \tau)} \delta (\tau) d \tau \tag {9.23}$$

必须保证对于所有 $t \geqslant t_{0}$ ， $\|x(t)\| < r$ ，才能使这个边界有效。同时注意到①

$$\| x (t) \| \leqslant \sqrt {\frac {c _ {2}}{c _ {1}}} \rho \| x \left(t _ {0}\right) \| e ^ {- \alpha \left(t - t _ {0}\right)} + \frac {c _ {4} \rho}{2 \alpha c _ {1}} \left[ 1 - e ^ {- \alpha \left(t - t _ {0}\right)} \right] \sup _ {t \geqslant t _ {0}} \delta (t)\leqslant \max \left\{\sqrt {\frac {c _ {2}}{c _ {1}}} \rho \| x (t _ {0}) \|, \frac {c _ {4} \rho}{2 \alpha c _ {1}} \sup _ {t \geqslant t _ {0}} \delta (t) \right\}$$

如果 $\| x(t_0)\| < \frac{r}{\rho}\sqrt{\frac{c_1}{c_2}}$ (9.24)

和 $\sup_{t\geqslant t_0}\delta (t) <   \frac{2c_1\alpha r}{c_4\rho}$ (9.25)

则条件 $\| x(t)\| < r$ 成立。为了易于参考，将上述结论总结成下面的引理。

引理9.4 设 $x = 0$ 是标称系统(9.2)的一个指数稳定平衡点， $V(t, x)$ 是标称系统的一个李雅普诺夫函数，在 $[0, \infty) \times D$ 上满足式(9.3)至式(9.5)，其中 $D = \{x \in R^n | \| x \|_2 < r\}$ 。假设扰动项 $g(t, x)$ 满足式(9.15)，其中 $\gamma(t)$ 满足式(9.20)和式(9.21)，如果解 $x(t_0)$ 满足式(9.24)，且 $\sup_{t \geqslant t_0} \delta(t)$ 满足式(9.25)，则扰动系统(9.1)的解满足式(9.23)。进而，如果所有假设全局成立，则对于任何 $x(t_0)$ 和任何有界 $\delta(t)$ ，式(9.23)成立。

上述引理的一个特例是零扰动的情况, 即当 $\delta(t) \equiv 0$ 时, 可得如下结果:

推论9.1 设 $x = 0$ 是标称系统(9.2)的一个指数稳定平衡点， $V(t, x)$ 是标称系统的一个李雅普诺夫函数，在 $[0, \infty) \times D$ 上满足式(9.3)至式(9.5)。假设扰动项 $g(t, x)$ 满足

$$\| g (t, x) \| \leqslant \gamma (t) \| x \|$$

其中 $\gamma(t)$ 满足式(9.20)和式(9.21)，则原点是扰动系统(9.1)的一个指数稳定平衡点。此外，如果所有假设全局成立，则原点是全局指数稳定的。

如果 $\gamma(t) \equiv \gamma$ ，为常数，则推论9.1要求 $\gamma$ 满足边界条件 $\gamma < c_1c_3 / c_2c_4$ ，由于 $(c_1 / c_2) \leqslant 1$ ，这个结果不优于由引理9.1提出的边界 $\gamma < c_3 / c_4$ 。事实上，只要 $(c_1 / c_2) < 1$ ，当前的边界比引理9.1所需的边界更为保守（也就是更小一些）。当 $\gamma(t)$ 的积分满足条件(9.20)和条件(9.21)，甚至 $\sup_{t \geqslant t_0} \gamma(t)$ 不足够小以满足 $\sup_{t \geqslant t_0} \gamma(t) < c_3 / c_4$ 时，就可看出推论9.1的优势。三种情况将在下面的引理中给出。
