$$\left\| \frac {\partial f}{\partial x} (t, x) \right\| _ {2} \leqslant L, \forall x \in D$$

则 $\| f(t,x)\| _2\leqslant L\| x\| _2$ ，且 $\phi (\tau ;t,x)$ 满足下界(见习题3.17)

$$\| \phi (\tau ; t, x) \| _ {2} ^ {2} \geqslant \| x \| _ {2} ^ {2} e ^ {- 2 L (\tau - t)}$$

所以 $V(t,x)\geqslant \int_{t}^{t + \delta}e^{-2L(\tau -t)}d\tau \| x\| _2^2 = \frac{1}{2L} (1 - e^{-2L\delta})\| x\| _2^2$

当 $c_{1} = \frac{(1 - e^{-2L\delta})}{2L},\quad c_{2} = \frac{k^{2}(1 - e^{-2\lambda\delta})}{2\lambda}$

时， $V(t,x)$ 满足定理的第一个不等式。

为了计算 V 沿系统轨线的导数, 定义灵敏度函数

$$\phi_ {t} (\tau ; t, x) = \frac {\partial}{\partial t} \phi (\tau ; t, x); \quad \phi_ {x} (\tau ; t, x) = \frac {\partial}{\partial x} \phi (\tau ; t, x)$$

那么 $\frac{\partial V}{\partial t} +\frac{\partial V}{\partial x} f(t,x) = \phi^{\mathrm{T}}(t + \delta ;t,x)\phi (t + \delta ;t,x) - \phi^{\mathrm{T}}(t;t,x)\phi (t;t,x)$

$$
\begin{array}{l} + \int_ {t} ^ {t + \delta} 2 \phi^ {\mathrm{T}} (\tau ; t, x) \phi_ {t} (\tau ; t, x) d \tau \\ + \int_ {t} ^ {t + \delta} 2 \phi^ {\mathrm{T}} (\tau ; t, x) \phi_ {x} (\tau ; t, x) d \tau f (t, x) \\ = \phi^ {\mathrm{T}} (t + \delta ; t, x) \phi (t + \delta ; t, x) - \| x \| _ {2} ^ {2} \\ + \int_ {t} ^ {t + \delta} 2 \phi^ {\mathrm{T}} (\tau ; t, x) [ \phi_ {t} (\tau ; t, x) + \phi_ {x} (\tau ; t, x) f (t, x) ] d \tau \\ \end{array}
$$

不难证明(见习题3.30)

$$\phi_ {t} (\tau ; t, x) + \phi_ {x} (\tau ; t, x) f (t, x) \equiv 0, \forall \tau \geqslant t$$

因此 $\frac{\partial V}{\partial t} +\frac{\partial V}{\partial x} f(t,x) = \phi^{\mathrm{T}}(t + \delta ;t,x)\phi (t + \delta ;t,x) - \| x\|_{2}^{2}$

$$\leqslant - (1 - k ^ {2} e ^ {- 2 \lambda \delta}) \| x \| _ {2} ^ {2}$$

选择 $\delta = \ln (2k^2) / (2\lambda)$ ，当 $c_{3} = 1 / 2$ 时 $V(t,x)$ 满足定理的第二个不等式。为了证明最后一个不等式，注意到 $\phi_x(\tau ;t,x)$ 满足灵敏度方程

$$\frac {\partial}{\partial \tau} \phi_ {x} = \frac {\partial f}{\partial x} (\tau , \phi (\tau ; t, x)) \phi_ {x}, \quad \phi_ {x} (t; t, x) = I$$

由于 $\left\| \frac{\partial f}{\partial x} (t,x)\right\| _2\leqslant L$

所以在 D 上, $\phi_{x}$ 满足边界(见习题 3.17)

$$\left\| \phi_ {x} (\tau ; t, x) \right\| _ {2} \leqslant e ^ {L (\tau - t)}$$

因此 $\left\| \frac{\partial V}{\partial x}\right\| _2 = \left\| \int_t^{t + \delta}2\phi^{\mathrm{T}}(\tau ;t,x)\phi_x(\tau ;t,x)d\tau \right\| _2$
