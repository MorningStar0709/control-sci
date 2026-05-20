则上面的不等式可重写为 $\dot{V} \leqslant -c_{3}\| z\|^{2} + c_{4}\gamma (t)\| z\|^{2} + c_{4}\delta (t)\| z\|$

它具有9.3节中不等式(9.16)的形式。因此,正如9.3节中应用比较引理,可以证明:如果 $\dot{u}(t)$ 满足

$$\int_ {t _ {0}} ^ {t} \| \dot {u} (\tau) \| d \tau \leqslant \varepsilon_ {1} (t - t _ {0}) + \eta_ {1}, \quad \varepsilon_ {1} < \frac {c _ {1} c _ {3}}{c _ {2} c _ {5}} \tag {9.46}$$

和

$$\| z (0) \| < \frac {r}{\rho_ {1}} \sqrt {\frac {c _ {1}}{c _ {2}}}; \quad \sup _ {t \geqslant 0} \| \dot {u} (t) \| \leqslant \frac {2 c _ {1} \alpha_ {1} r}{c _ {4} \rho_ {1} L}$$

其中的 $\alpha_{1}$ 和 $\rho_{1}$ 定义为

$$\alpha_ {1} = \frac {1}{2} \left[ \frac {c _ {3}}{c _ {2}} - \varepsilon_ {1} \frac {c _ {5}}{c _ {1}} \right] > 0, \quad \rho_ {1} = \exp \left(\frac {c _ {5} \eta_ {1}}{2 c _ {1}}\right) \geqslant 1$$

则 $z(t)$ 满足不等式

$$\| z (t) \| \leqslant \sqrt {\frac {c _ {2}}{c _ {1}}} \rho_ {1} \| z (0) \| e ^ {- \alpha_ {1} t} + \frac {c _ {4} \rho_ {1} L}{2 c _ {1}} \int_ {0} ^ {t} e ^ {- \alpha_ {1} (t - \tau)} \| \dot {u} (\tau) \| d \tau \tag {9.47}$$

视 $\| \dot{u}\|$ 的假设不同，可由前面的不等式得出几个结论，由下面的定理给出。

定理 9.3 考虑系统(9.45)，假设 $\left[\partial h/\partial u\right]$ 满足式(9.39)，且对于所有 $t\geqslant0,\|\dot{u}(t)\|\leqslant\varepsilon$ ，并假设存在一个李雅普诺夫函数 $V(z,u)$ ，满足式(9.41)至式(9.44)。如果

$$\varepsilon < \frac {c _ {1} c _ {3}}{c _ {2} c _ {5}} \times \frac {r}{r + c _ {4} L / c _ {5}}$$

则对于所有 $\|z(0)\|<r\sqrt{c_{1}/c_{2}}$ ，系统(9.45)的解对所有 $t\geqslant0$ 是一致有界的和一致毕竟有界的，由

$$b = \frac {c _ {2} c _ {4} L \varepsilon}{\theta (c _ {1} c _ {3} - \varepsilon c _ {2} c _ {5})}$$

确定,式中 $\theta\in(0,1)$ 是任意常数。另外,如果当 t 趋于无穷时, $\dot{u}(t)$ 趋于零,则当 t 趋于无穷时, $z(t)$ 趋于零。最后,如果对于所有 $u\in\Gamma$ 和 $\varepsilon<c_{3}/c_{5}$ ,有 $h(u)=0$ ,则 z=0 是系统(9.45)的一个指数平衡点。同样,x=0 是系统(9.38)的指数稳定平衡点。

证明：由于 $\| \dot{u}(t)\| \leqslant \varepsilon < c_1c_3 / c_2c_5$ ，则当 $\varepsilon_{1} = \varepsilon ,\eta_{1} = 0$ 时，不等式(9.46)得到满足。因此，

$$\alpha_ {1} = \frac {1}{2} \left[ \frac {c _ {3}}{c _ {2}} - \varepsilon \frac {c _ {5}}{c _ {1}} \right], \quad \rho_ {1} = 1$$

用给定的 $\varepsilon$ 的上界可以得到

$$
\begin{array}{l} \frac {2 c _ {1} \alpha_ {1} r}{c _ {4} L} = \frac {c _ {1} r}{c _ {4} L} \left[ \frac {c _ {3}}{c _ {2}} - \varepsilon \frac {c _ {5}}{c _ {1}} \right] \\ > \frac {c _ {1} r}{c _ {4} L} \left[ \frac {c _ {3}}{c _ {2}} - \frac {c _ {3}}{c _ {2}} \times \frac {r}{r + c _ {4} L / c _ {5}} \right] \\ = \frac {c _ {1} c _ {3}}{c _ {2} c _ {5}} \times \frac {r}{r + c _ {4} L / c _ {5}} > \varepsilon \\ \end{array}
$$
