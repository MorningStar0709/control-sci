柔性关节的转动动能为 $\frac{1}{2}I_{h}\dot{\theta}^{2}$ ，柔性机械臂的动能为 $\frac{1}{2}\int_{0}^{L}\rho\dot{z}^{2}(x)\mathrm{d}x$ ，负载的动能为 $\frac{1}{2}m\dot{z}^{2}(L)$ ，则系统的总动能为

$$E _ {\mathrm{k}} = \frac {1}{2} I _ {\mathrm{h}} \dot {\theta} ^ {2} + \frac {1}{2} \int_ {0} ^ {L} \rho \dot {z} ^ {2} (x) \mathrm{d} x + \frac {1}{2} m \dot {z} ^ {2} (L) \tag {13.27}$$

柔性机械臂的势能可以表示为

$$E _ {\mathrm{p}} = \frac {1}{2} \int_ {0} ^ {L} \mathrm{EIy} _ {x x} ^ {2} (x) \mathrm{d} x \tag {13.28}$$

系统的非保守力做功为

$$W _ {\mathrm{c}} = \tau \theta + F z (L) \tag {13.29}$$

首先，将式（13.26）的第一项展开可得

$$
\begin{array}{l} \int_ {t _ {1}} ^ {t _ {2}} \delta E _ {k} \mathrm{d} t = \int_ {t _ {1}} ^ {t _ {2}} \delta \left(\frac {1}{2} I _ {\mathrm{h}} \dot {\theta} ^ {2} + \frac {\rho}{2} \int_ {0} ^ {L} \dot {z} (x) ^ {2} \mathrm{d} x + \frac {1}{2} m \dot {z} (L) ^ {2}\right) \mathrm{d} t \\ = \int_ {t _ {1}} ^ {t _ {2}} \delta \left(\frac {1}{2} I _ {\mathrm{h}} \dot {\theta} ^ {2}\right) \mathrm{d} t + \frac {\rho}{2} \int_ {t _ {1}} ^ {t _ {2}} \int_ {0} ^ {L} \delta \dot {z} (x) ^ {2} \mathrm{d} x \mathrm{d} t + \int_ {t _ {1}} ^ {t _ {2}} \delta \left(\frac {1}{2} m \dot {z} (L) ^ {2}\right) \mathrm{d} t \\ \end{array}
$$

由于

$$\int_ {t _ {1}} ^ {t _ {2}} \delta \left(\frac {1}{2} I _ {\mathrm{h}} \dot {\theta} ^ {2}\right) \mathrm{d} t = \int_ {t _ {1}} ^ {t _ {2}} I _ {\mathrm{h}} \dot {\theta} \delta \dot {\theta} \mathrm{d} t = I _ {\mathrm{h}} \dot {\theta} \delta \theta \big | _ {t _ {1}} ^ {t _ {2}} - \int_ {t _ {1}} ^ {t _ {2}} I _ {\mathrm{h}} \ddot {\theta} \delta \theta \mathrm{d} t = - \int_ {t _ {1}} ^ {t _ {2}} I _ {\mathrm{h}} \ddot {\theta} \delta \theta \mathrm{d} t$$

式中，由变分基本公式 $\delta\frac{dx}{dt}=\frac{d}{dt}\delta x$ 可得 $\delta\dot{\theta}dt=\frac{d}{dt}\delta\dot{\theta}$ 。

$$
\begin{array}{l} \frac {\rho}{2} \int_ {t _ {1}} ^ {t _ {2}} \int_ {0} ^ {L} \delta \dot {z} (x) ^ {2} \mathrm{d} x \mathrm{d} t = \int_ {0} ^ {L} \int_ {t _ {1}} ^ {t _ {2}} \rho \dot {z} (x) \delta \dot {z} (x) \mathrm{d} t \mathrm{d} x \\ = \int_ {0} ^ {L} \left( \right.\rho \dot {z} (x) \delta z (x) \left. \right| _ {t _ {1}} ^ {t _ {2}} - \int_ {t _ {1}} ^ {t _ {2}} \rho \ddot {z} (x) \delta z (x) d t\left. \right) d x \\ = - \int_ {0} ^ {L} \int_ {t _ {1}} ^ {t _ {2}} \rho \ddot {z} (x) \delta z (x) \mathrm{d} t \mathrm{d} x \\ = - \int_ {t _ {1}} ^ {t _ {2}} \int_ {0} ^ {L} \rho \ddot {z} (x) \delta z (x) \mathrm{d} x \mathrm{d} t \\ \end{array}
$$
