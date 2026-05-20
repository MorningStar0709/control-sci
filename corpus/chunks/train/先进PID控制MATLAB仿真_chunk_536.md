# 13.4.2 边界 PD 控制律设计

取角度信号的误差信息为

$$e = \theta - \theta_ {\mathrm{d}}, \quad \dot {e} = \dot {\theta} - \dot {\theta} _ {\mathrm{d}} = \dot {\theta}, \quad \ddot {e} = \ddot {\theta} - \ddot {\theta} _ {\mathrm{d}} = \ddot {\theta}$$

考虑到机械臂的动能、机械臂的势能和负载的动能最小时， $y(x)$ 为最小，另外考虑跟踪误差和跟踪误差变化率，设计李雅普诺夫函数为

$$V = E _ {1} + E _ {2} \tag {13.43}$$

式中， $E_{1}=\frac{1}{2}\int_{0}^{L}\rho\dot{z}^{2}(x)\mathrm{d}x+\frac{1}{2}\mathrm{EI}\int_{0}^{L}y_{xx}^{2}(x)\mathrm{d}x$ ； $E_{2}=\frac{1}{2}I_{h}\dot{e}^{2}+\frac{1}{2}k_{p}e^{2}+\frac{1}{2}m\dot{z}^{2}(L)$ ， $k_{p}>0$ ； $E_{1}$ 为机械臂的动能和势能之和，表示对机械臂弯曲变形量和弯曲变化率的抑制指标； $E_{2}$ 中的前2项代表了控制的误差指标，第3项为负载的动能。则

$$\dot {V} = \dot {E} _ {1} + \dot {E} _ {2}$$

其中

$$\dot {E} _ {1} = \int_ {0} ^ {L} \rho \dot {z} (x) \ddot {z} (x) \mathrm{d} x + \operatorname{EI} \int_ {0} ^ {L} y _ {x x} (x) \dot {y} _ {x x} (x) \mathrm{d} x$$

将式（13.38）即 $\rho \ddot{z}(x) = -\mathrm{EI}z_{xxxx}(x)$ 代入上式中，则

$$
\dot {E} _ {1} = - \mathrm{EI} \int_ {0} ^ {L} \dot {z} (x) z _ {x x x} (x) \mathrm{d} x + \mathrm{EI} \int_ {0} ^ {L} y _ {x x} (x) \dot {y} _ {x x} (x) \mathrm{d} x
\begin{array}{l} \int_ {0} ^ {L} \dot {z} (x) z _ {x x x x} (x) \mathrm{d} x = \int_ {0} ^ {L} \dot {z} (x) \mathrm{d} z _ {x x x} (x) \\ = \dot {z} (x) z _ {x x x} (x) \Big | _ {0} ^ {L} - \int_ {0} ^ {L} z _ {x x x} (x) \dot {z} _ {x} (x) d x = \dot {z} (L) z _ {x x x} (L) - \int_ {0} ^ {L} z _ {x x x} (x) \dot {z} _ {x} (x) d x \\ \int_ {0} ^ {L} y _ {x x} (x) \dot {y} _ {x x} (x) \mathrm{d} x = \int_ {0} ^ {L} z _ {x x} (x) \dot {z} _ {x x} (x) \mathrm{d} x = \int_ {0} ^ {L} z _ {x x} (x) \mathrm{d} \dot {z} _ {x} (x) \\ = z _ {x x} (x) \dot {z} _ {x} (x) \Big | _ {0} ^ {L} - \int_ {0} ^ {L} \dot {z} _ {x} (x) z _ {x x x} (x) d x = - z _ {x x} (0) \dot {\theta} - \int_ {0} ^ {L} \dot {z} _ {x} (x) z _ {x x x} (x) d x \\ \end{array}
$$

式中， $z_{xx}(L) = 0$ ； $\dot{z}_x(0) = \dot{\theta}$ 。从而

$$
\begin{array}{l} \dot {E} _ {1} = - \mathrm{EI} \int_ {0} ^ {L} \dot {z} (x) z _ {x x x x} (x) \mathrm{d} x + \mathrm{EI} \int_ {0} ^ {L} y _ {x x} (x) \dot {y} _ {x x} (x) \mathrm{d} x \\ = - \operatorname{EI} \left(\dot {z} (L) z _ {x x x} (L) - \int_ {0} ^ {L} z _ {x x x} (x) \dot {z} _ {x} (x) \mathrm{d} x\right) + \operatorname{EI} \left(- z _ {x x} (0) \dot {\theta} - \int_ {0} ^ {L} \dot {z} _ {x} (x) z _ {x x x} (x) \mathrm{d} x\right) \\ = - \mathrm{EI} \dot {z} (L) y _ {x x x} (L) - \mathrm{EI} y _ {x x} (0) \dot {\theta} \\ \end{array}
$$

即
