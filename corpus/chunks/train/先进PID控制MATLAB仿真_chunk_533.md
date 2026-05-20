$$\delta \int_ {t _ {1}} ^ {t _ {2}} W _ {\mathrm{c}} \mathrm{d} t = \delta \int_ {t _ {1}} ^ {t _ {2}} (\tau \theta + F z (L)) \mathrm{d} t \tag {13.32}$$

根据上述分析，得

$$
\begin{array}{l} \int_ {t _ {1}} ^ {t _ {2}} \left(\delta E _ {\mathrm{k}} - \delta E _ {\mathrm{p}} + \delta W _ {\mathrm{c}}\right) \mathrm{d} t \\ = - \int_ {t _ {1}} ^ {t _ {2}} I _ {\mathrm{h}} \ddot {\theta} \delta \theta \mathrm{d} t - \int_ {t _ {1}} ^ {t _ {2}} \int_ {0} ^ {L} \rho \ddot {z} (x) \delta z (x) \mathrm{d} x \mathrm{d} t - \int_ {t _ {1}} ^ {t _ {2}} m \ddot {z} (L) \delta z (L) \mathrm{d} t \\ - \mathrm{EI} \int_ {t _ {1}} ^ {t _ {2}} \left(z _ {x x} (L) \delta z _ {x} (L) - z _ {x x} (0) \delta z _ {x} (0)\right) \mathrm{d} t + \mathrm{EI} \int_ {t _ {1}} ^ {t _ {2}} z _ {x x x} (L) \delta z (L) \mathrm{d} t \\ - \mathrm{EI} \int_ {t _ {1}} ^ {t _ {2}} \int_ {0} ^ {L} z _ {x x x x} (x) \delta z (x) \mathrm{d} x \mathrm{d} t + \delta \int_ {t _ {1}} ^ {t _ {2}} \tau \theta + F z (L) \mathrm{d} t \\ \end{array}
$$

将 $z(0) = 0$ ， $z_{x}(0) = \theta$ ， $\ddot{z}_x(0) = \ddot{\theta}$ ， $\frac{\partial^n z(x)}{\partial x^n} = \frac{\partial^n y(x)}{\partial x^n}, (n\geqslant 2)$ 代入上式，可得

$$
\begin{array}{l} \int_ {t _ {1}} ^ {t _ {2}} \left(\delta E _ {\mathrm{k}} - \delta E _ {\mathrm{p}} + \delta W _ {\mathrm{c}}\right) \mathrm{d} t \\ = - \int_ {t _ {1}} ^ {t _ {2}} \int_ {0} ^ {L} (\rho \ddot {z} (x) + \mathrm{EI} z _ {x x x} (x)) \delta z (x) \mathrm{d} x \mathrm{d} t - \int_ {t _ {1}} ^ {t _ {2}} (I _ {\mathrm{h}} \ddot {\theta} - \mathrm{EI} z _ {x x} (0) - \tau) \delta z _ {x} (0) \mathrm{d} t \\ - \int_ {t _ {1}} ^ {t _ {2}} (m \ddot {z} (L) - \mathrm{EI} z _ {x x x} (L) - F) \delta z (L) \mathrm{d} t - \int_ {t _ {1}} ^ {t _ {2}} \mathrm{EI} z _ {x x} (L) \delta z _ {x} (L) \mathrm{d} t \\ = - \int_ {t _ {1}} ^ {t _ {2}} \int_ {0} ^ {L} A \delta z (x) \mathrm{d} x \mathrm{d} t - \int_ {t _ {1}} ^ {t _ {2}} B \delta z _ {x} (0) \mathrm{d} t - \int_ {t _ {1}} ^ {t _ {2}} C \delta z (L) \mathrm{d} t - \int_ {t _ {1}} ^ {t _ {2}} D \delta z _ {x} (L) \mathrm{d} t \\ \end{array}
$$

其中

$$A = \rho \ddot {z} (x) + \mathrm{EI} z _ {x x x x} (x)B = I _ {\mathrm{h}} \ddot {z} _ {x} (0) - \mathrm{EI} z _ {x x} (0) - \tauC = m \ddot {z} (L) - \mathrm{EI} z _ {x x x} (L) - FD = \mathrm{EI} z _ {x x} (L)$$

根据 Hamilton 方程式（13.26），有

$$- \int_ {t _ {1}} ^ {t _ {2}} \int_ {0} ^ {L} A \delta z (x) \mathrm{d} x \mathrm{d} t - \int_ {t _ {1}} ^ {t _ {2}} B \delta z _ {x} (0) \mathrm{d} t - \int_ {t _ {1}} ^ {t _ {2}} C \delta z (L) \mathrm{d} t - \int_ {t _ {1}} ^ {t _ {2}} D \delta z _ {x} (L) \mathrm{d} t = 0 \tag {13.33}$$

由于 $\delta z(x)$ 、 $\delta z_{x}(0)$ 、 $\delta z(L)$ 、 $\delta z_{\bar{x}}(L)$ 属于独立的变量，即上式中的各项线性无关，则有 A = B = C = D = 0，从而得到 PDE 动力学模型如下

$$\rho \ddot {z} (x) = - \mathrm{EI} z _ {x x x x} (x) \tag {13.34}\tau = I _ {\mathrm{h}} \ddot {z} _ {x} (0) - \mathrm{EI} z _ {x x} (0) \tag {13.35}F = m \ddot {z} (L) - \mathrm{EI} z _ {x x x} (L) \tag {13.36}z _ {x x} (L) = 0 \tag {13.37}$$

式中， $\ddot{z}(x)=x\ddot{\theta}+\ddot{y}(x)$ ； $\ddot{z}(L)=L\ddot{\theta}+\ddot{y}(L)$ 。

![](image/5cd78793ee18dfcd27cb666df95c0eb1b28acc8d8cca7d3fcc906700e645e1fc.jpg)
