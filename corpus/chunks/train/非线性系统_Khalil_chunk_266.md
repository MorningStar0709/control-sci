# 引理9.5

1. 如果 $\int_0^\infty \gamma (\tau)d\tau \leqslant k$

则当 $\varepsilon=0,\eta=k$ 时，式(9.20)成立。

2. 如果 $\gamma (t)\to 0$ 当 $t\to \infty$

则对于任何 $\varepsilon > 0$ ，存在 $\eta = \eta(\varepsilon) > 0$ ，使式(9.20)成立。

3. 如果存在常数 $\Delta > 0, T \geqslant 0$ 和 $\varepsilon_{1} > 0$ , 使得

$$\frac {1}{\Delta} \int_ {t} ^ {t + \Delta} \gamma (\tau) d \tau \leqslant \varepsilon_ {1}, \forall t \geqslant T$$

则当 $\varepsilon = \varepsilon_{1}, \eta = \varepsilon_{1} \Delta + \int_{0}^{T} \gamma(t) dt$ 时，式(9.20)成立。

证明:第一种情况是显而易见的。为了证明第二种情况,注意到因为 $\lim_{t\to\infty}\gamma(t)=0$ , 故对于任何 $\varepsilon>0$ , 存在 $T_{1}=T_{1}(\varepsilon)>0$ , 使得对于所有 $t\geqslant T_{1}$ , 有 $\gamma(t)<\varepsilon$ 。设 $\eta=\int_{0}^{T_{1}}\gamma(t)dt$ , 如果 $t_{0}\geqslant T_{1}$ , 则

$$\int_ {t _ {0}} ^ {t} \gamma (\tau) d \tau \leqslant \int_ {t _ {0}} ^ {t} \varepsilon d \tau = \varepsilon (t - t _ {0})$$

如果 $t \leqslant T_{1}$ , 则 $\int_{t_0}^{t} \gamma(\tau) d\tau \leqslant \int_{0}^{T_{1}} \gamma(\tau) d\tau = \eta$

如果 $t_0 \leqslant T_1 \leqslant t$ ，则

$$
\begin{array}{l} \int_ {t _ {0}} ^ {t} \gamma (\tau) d \tau = \int_ {t _ {0}} ^ {T _ {1}} \gamma (\tau) d \tau + \int_ {T _ {1}} ^ {t} \gamma (\tau) d \tau \\ \leqslant \int_ {0} ^ {T _ {1}} \gamma (\tau) d \tau + \varepsilon (t - T _ {1}) \leqslant \eta + \varepsilon (t - t _ {0}) \\ \end{array}
$$

在最后一种情况下,如果 $t \leqslant T$ , 则

$$\int_ {t _ {0}} ^ {t} \gamma (\tau) d \tau \leqslant \int_ {0} ^ {T} \gamma (\tau) d \tau < \eta$$

当 $t \geqslant t_1 \geqslant T$ 时，对于 $(N - 1)\Delta \leqslant t - t_1 \leqslant N\Delta$ ，设 $N$ 是整数，则

$$
\begin{array}{l} \int_ {t _ {1}} ^ {t} \gamma (\tau) d \tau = \sum_ {i = 0} ^ {i = N - 2} \int_ {t _ {1} + i \Delta} ^ {t _ {1} + (i + 1) \Delta} \gamma (\tau) d \tau + \int_ {t _ {1} + (N - 1) \Delta} ^ {t} \gamma (\tau) d \tau \\ \leqslant \sum_ {i = 0} ^ {i = N - 2} \varepsilon_ {1} \Delta + \varepsilon_ {1} \Delta \leqslant \varepsilon_ {1} (t - t _ {1}) + \varepsilon_ {1} \Delta \\ \end{array}
$$

对于该不等式，当 $t \geqslant t_0 \geqslant T$ 时，取 $t_1 = t_0$ ，而当 $t_0 \leqslant T \leqslant t$ 时，取 $t_1 = T$ 。如果 $t \geqslant t_0 \geqslant T$ ，则有

$$\int_ {t _ {0}} ^ {t} \gamma (\tau) d \tau \leqslant \varepsilon_ {1} (t - t _ {0}) + \varepsilon_ {1} \Delta < \varepsilon_ {1} (t - t _ {0}) + \eta$$

如果 $t_0 \leqslant T \leqslant t$ ，则
