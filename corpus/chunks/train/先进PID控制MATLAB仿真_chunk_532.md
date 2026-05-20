式中， $\int_0^L\int_{t_1}^{t_2}\rho \ddot{z}(x)\delta z(x)\mathrm{d}t\mathrm{d}x = \int_{t_1}^{t_2}\int_0^L\rho \ddot{z}(x)\delta z(x)\mathrm{d}x\mathrm{d}t$

$$
\begin{array}{l} \int_ {t _ {1}} ^ {t _ {2}} \delta \left(\frac {1}{2} m \dot {z} (L) ^ {2}\right) \mathrm{d} t = \int_ {t _ {1}} ^ {t _ {2}} m \dot {z} (L) \delta \dot {z} (L) \mathrm{d} t \\ = m \dot {z} (L) \delta z (L) \Big | _ {t _ {1}} ^ {t _ {2}} - \int_ {t _ {1}} ^ {t _ {2}} m \ddot {z} (L) \delta z (L) \mathrm{d} t = - \int_ {t _ {1}} ^ {t _ {2}} m \ddot {z} (L) \delta z (L) \mathrm{d} t \\ \end{array}
$$

则

$$\delta \int_ {t _ {1}} ^ {t _ {2}} E _ {\mathrm{k}} \mathrm{d} t = - \int_ {t _ {1}} ^ {t _ {2}} I _ {\mathrm{h}} \ddot {\theta} \delta \theta \mathrm{d} t - \int_ {t _ {1}} ^ {t _ {2}} \int_ {0} ^ {L} \rho \ddot {z} (x) \delta z (x) \mathrm{d} x \mathrm{d} t - \int_ {t _ {1}} ^ {t _ {2}} m \ddot {z} (L) \delta z (L) \mathrm{d} t \tag {13.30}$$

然后，将式（13.26）的第二项展开，根据 $z_{xx}(x) = y_{xx}(x)$ 可得

$$
\begin{array}{l} - \delta \int_ {t _ {1}} ^ {t _ {2}} E _ {\mathrm{p}} \mathrm{d} t = - \delta \int_ {t _ {1}} ^ {t _ {2}} \frac {\mathrm{EI}}{2} \int_ {0} ^ {L} \left(z _ {x x} (x)\right) ^ {2} \mathrm{d} x \mathrm{d} t \\ = - \mathrm{EI} \int_ {t _ {1}} ^ {t _ {2}} \int_ {0} ^ {L} z _ {x x} (x) \delta z _ {x x} (x) \mathrm{d} x \mathrm{d} t \\ = - \mathrm{EI} \int_ {t _ {1}} ^ {t _ {2}} \left( \right.z _ {x x} (x) \delta z _ {x} (x) \left. \right| _ {0} ^ {L} - \int_ {0} ^ {L} z _ {x x x} (x) \delta z _ {x} (x) \mathrm{d} x\left. \right) \mathrm{d} t \\ = - \mathrm{EI} \int_ {t _ {1}} ^ {t _ {2}} \left(z _ {x x} (L) \delta z _ {x} (L) - z _ {x x} (0) \delta z _ {x} (0)\right) \mathrm{d} t + \mathrm{EI} \int_ {t _ {1}} ^ {t _ {2}} \int_ {0} ^ {L} z _ {x x x} (x) \delta z _ {x} (x) \mathrm{d} x \mathrm{d} t \\ = - \operatorname{EI} \int_ {t _ {1}} ^ {t _ {2}} \left(z _ {x x} (L) \delta z _ {x} (L) - z _ {x x} (0) \delta z _ {x} (0)\right) \mathrm{d} t + \operatorname{EI} \int_ {t _ {1}} ^ {t _ {2}} \left(z _ {x x x} (x) \delta z (x) \big | _ {0} ^ {L} - \int_ {0} ^ {L} z _ {x x x x} (x) \delta z (x) \mathrm{d} x\right) \mathrm{d} t \\ = - \mathrm{EI} \int_ {t _ {1}} ^ {t _ {2}} \left(z _ {x x} (L) \delta z _ {x} (L) - z _ {x x} (0) \delta z _ {x} (0)\right) \mathrm{d} t + \mathrm{EI} \int_ {t _ {1}} ^ {t _ {2}} z _ {x x x} (L) \delta z (L) \mathrm{d} t - E I \int_ {t _ {1}} ^ {t _ {2}} \int_ {0} ^ {L} z _ {x x x x} (x) \delta z (x) \mathrm{d} x \mathrm{d} t \tag {13.31} \\ \end{array}
$$

最后，将式（13.26）的第三项展开可得
