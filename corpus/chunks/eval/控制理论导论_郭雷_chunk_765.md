$$\max \left\{1 - \frac {\delta^ {2}}{4}, 1 - \frac {\varepsilon}{2} \right\} \leqslant \| T (t _ {1} + t _ {0}) x _ {1} \| \leqslant \| T (t _ {1}) x _ {1} \|. \tag {10.3.12}$$

对于 $t \geqslant 0$ , 我们作分解 $T(t)x_{1} = y(t) + z(t)$ , 其中 $y(t) \in H_{n}$ , 而 $z(t) \in H_{n}^{\perp}$ . 如果对某个 $s \in [0, t_{1}]$ , 有 $\|y(s)\| > \delta$ , 那么 $\|T(s)x_{0}\|^2 = \|y(s)\|^2 + \|z(s)\|^2 \leqslant 1$ 意味着

$$\left\| z (s) \right\| ^ {2} < 1 - \delta^ {2} \leqslant \left(1 - \frac {\delta^ {2}}{2}\right) ^ {2},$$

从而

$$
\begin{array}{l} \| T (t _ {0} + t _ {1}) x _ {0} \| = \| T (t _ {0} + t _ {1} - s) T (s) x _ {0} \| \\ = \left\| T (t _ {0} + t _ {1} - s) (y (s) + z (s)) \right\| <   \frac {\delta^ {2}}{4} + 1 - \frac {\delta^ {2}}{2} = 1 - \frac {\delta^ {2}}{4}, \\ \end{array}
$$

这与式 (10.3.12) 矛盾. 因此

$$\| y (s) \| \leqslant \delta , \quad \forall s \in [ 0, t _ {1} ],$$

并且

$$\sup _ {0 \leqslant s \leqslant t _ {1}} \| B _ {n} T (s) x _ {0} \| \leqslant \| B _ {n} \| \delta . \tag {10.3.13}$$

最后，从式(10.3.11)，(10.3.12)和式(10.3.13)得到

$$\left\| S _ {n} (t _ {1}) x _ {1} \right\| \geqslant 1 - \varepsilon > \frac {1}{2},$$

而 $t_1$ 的任意性意味着 $S_n(t)$ 不是指数稳定的。由于 $S(t)$ 是指数稳定的，故存在常数 $M \geqslant 1$ 和 $\omega > 0$ ，使得 $\| S(t) \| \leqslant M e^{-\omega t}$ 。但根据定理5.3.8，我们有

$$\left\| S _ {n} (t) \right\| \leqslant M \mathrm{e} ^ {(- \omega + M \| B - B _ {n} \|) t},$$

因此当 $n$ 充分大时 $S_{n}(t)$ 是指数稳定的，与上述结论矛盾。证毕。
