$$
\begin{array}{l} \dot {V} _ {1} = \frac {\partial V _ {1}}{\partial t} + \frac {\partial V _ {1}}{\partial x} F + \frac {1}{\varepsilon} \frac {\partial V _ {1}}{\partial v} [ G (t, x, v, 0) + \Delta G ] \\ \leqslant c _ {5} \| v \| ^ {2} + c _ {6} k _ {0} \| v \| ^ {2} - \frac {c _ {3}}{\varepsilon} \| v \| ^ {2} + \frac {c _ {4}}{\varepsilon} \| v \| \left(k _ {4} \| v \| ^ {2} + k _ {5} k _ {1} \| v \| e ^ {- \alpha \tau} + \varepsilon a _ {2}\right) \\ \end{array}
$$

当 $\| v\| \leqslant c_3 / 4c_4k_4$ 和 $0 <   \varepsilon <  c_{3} / 4(c_{5} + c_{6}k_{0})$ 时，有

$$
\begin{array}{l} \dot {V} _ {1} \leqslant - \frac {c _ {3}}{2 \varepsilon} \| v \| ^ {2} + \frac {c _ {4} k _ {5} k _ {1}}{\varepsilon} \| v \| ^ {2} e ^ {- \alpha \tau} + c _ {4} a _ {2} \| v \| \\ \leqslant - \frac {2}{\varepsilon} \left(k _ {a} - k _ {b} e ^ {- \alpha \tau}\right) V _ {1} + 2 k _ {c} \sqrt {V _ {1}} \\ \end{array}
$$

其中 $k_{a} = c_{3} / 4c_{2}, k_{b} = c_{4}k_{5}k_{1} / 2c_{1}, k_{c} = c_{4}a_{2} / 2\sqrt{c_{1}}$ 。取 $W = \sqrt{V_1}$ ，得

$$D ^ {+} W (\tau) \leqslant - \left(k _ {a} - k _ {b} e ^ {- \alpha \tau}\right) W + \varepsilon k _ {c}$$

其中 $D^{+}W(\tau)$ 是 $W$ 对 $\tau$ 的上右导数。由比较原理（见引理3.4），可得

$$W (\tau) \leqslant \phi (\tau , 0) W (0) + \varepsilon \int_ {0} ^ {\tau} \phi (\tau , \sigma) k _ {c} d \sigma$$

其中 $\phi (\tau ,\sigma) = \exp \left[-\int_{\sigma}^{\tau}\left(k_{a} - k_{b}e^{-\alpha \lambda}\right)d\lambda \right],\qquad |\phi (\tau ,\sigma)|\leqslant k_{g}e^{-\alpha_{g}(\tau -\sigma)}$

$k_{g}, \alpha_{g} > 0$ 。利用 $v(0) = O(\varepsilon)$ ，可得对于所有 $\tau \geqslant 0$ ，有 $v(\tau) = O(\varepsilon)$ 。这就证明了对于足够小的 $\varepsilon$ ，当 $t \in [t_{0}, t_{1}]$ 时，方程(C.69)和方程(C.70)的解满足

$$x (t, \varepsilon) - \bar {x} (t) = O (\varepsilon), \quad y (t, \varepsilon) - \hat {y} \left(\frac {t}{\varepsilon}\right) = O (\varepsilon)$$

由于 $\bar{x}(t) \in S$ ，因此存在 $\varepsilon_2^* > 0$ 足够小，使得对于所有 $t \in [t_0, t_1]$ 和所有 $\varepsilon < \varepsilon_2^*$ ，有 $x(t, \varepsilon) \in S_1$ ，故 $x(t, \varepsilon)$ 和 $y(t, \varepsilon)$ 是方程(11.10)和方程(11.11)的解。根据式(11.9)，有

$$z (t, \varepsilon) - h (t, \bar {x} (t)) - \hat {y} \left(\frac {t}{\varepsilon}\right) = y (t, \varepsilon) - \hat {y} \left(\frac {t}{\varepsilon}\right) + h (t, x (t, \varepsilon)) - h (t, \bar {x} (t)) = O (\varepsilon)$$

其中用到 h 是 x 的利普希茨函数。最后，由于 $\hat{y}(\tau)$ 满足式(C.83)，且

$$\exp \left[ \frac {- \alpha (t - t _ {0})}{\varepsilon} \right] \leqslant \varepsilon , \forall \alpha (t - t _ {0}) \geqslant \varepsilon \ln \left(\frac {1}{\varepsilon}\right)$$

如果 $\varepsilon$ 足够小,且满足

$$\varepsilon \ln \left(\frac {1}{\varepsilon}\right) \leqslant \alpha (t _ {b} - t _ {0})$$

则 $\hat{y}(t/\varepsilon)$ 一项在 $[t_{b}, t_{1}]$ 上一致为 $O(\varepsilon)$ ，定理 11.1 证毕。
