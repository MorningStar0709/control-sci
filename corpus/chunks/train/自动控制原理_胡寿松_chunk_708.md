# 2. 李雅普诺夫第一法(间接法)

李雅普诺夫第一法是利用状态方程解的特性来判断系统稳定性的方法，它适用于线性定常、线性时变以及非线性函数可线性化的情况。由于本章主要研究线性定常系统，所以在此仅介绍线性定常系统的特征值判据。

定理9-9 对于线性定常系统 $\dot{\pmb{x}} = \pmb {A}\pmb {x},\pmb {x}(0) = \pmb{x}_0,t\geqslant 0$ ，有

1) 系统的每一平衡状态是在李雅普诺夫意义下稳定的充分必要条件是, A 的所有特征值均具有非正(负或零)实部, 且具有零实部的特征值为 A 的最小多项式的单根。  
2) 系统的唯一平衡状态 $x_{e} = 0$ 是渐近稳定的充分必要条件是, $\mathbf{A}$ 的所有特征值均具有负实部。

证明 1) 设 $x_{e}$ 为 $\dot{x} = Ax$ 的平衡状态，则由性质 $\dot{x}_{e} = 0$ 和 $Ax_{e} = 0$ 可知，对于所有 $t \geqslant 0$ 均有

$$\boldsymbol {x} _ {e} = \mathrm{e} ^ {\boldsymbol {A} t} \boldsymbol {x} _ {e} \tag {9-256}$$

于是，考虑到 $x(t;x_0,0) = \mathrm{e}^{A t}x_0$ ，有

$$\boldsymbol {x} (t; \boldsymbol {x} _ {0}, 0) - \boldsymbol {x} _ {e} = \mathrm{e} ^ {\boldsymbol {A} t} \left(\boldsymbol {x} _ {0} - \boldsymbol {x} _ {e}\right), \quad \forall t \geqslant 0 \tag {9-257}$$

这表明，当且仅当 $\| e^{A^r}\| \leqslant k < \infty$ 时，对任给的一个实数 $\varepsilon >0$ ，都对应存在和初始时刻无关的一个实数 $\delta (\varepsilon) = \varepsilon /k$ ，使得由满足不等式

$$\left\| \boldsymbol {x} _ {0} - \boldsymbol {x} _ {e} \right\| \leqslant \delta (\varepsilon) \tag {9-258}$$

的任一初态 $x_0$ 出发的受扰运动都满足不等式

$$\| \boldsymbol {x} (t; \boldsymbol {x} _ {0}, 0) - \boldsymbol {x} _ {e} \| \leqslant \| e ^ {\boldsymbol {A} t} \| \cdot \| \boldsymbol {x} _ {0} - \boldsymbol {x} _ {e} \| \leqslant k \cdot \frac {\varepsilon}{k}, \quad \forall t \geqslant 0 \tag {9-259}$$

从而由定义知,系统的每一个平衡状态均为李雅普诺夫意义下稳定。再引入非奇异变换阵 P, 使得 $\hat{A} = P^{-1}AP$ 为矩阵 A 的约当规范型, 则又有

$$\left\| \mathrm{e} ^ {\hat {A} t} \right\| \leqslant \left\| \boldsymbol {P} ^ {- 1} \right\| \cdot \left\| \mathrm{e} ^ {A t} \right\| \cdot \| \boldsymbol {P} \| \tag {9-260}$$

因而 $\| e^{A^t}\|$ 有界等价于 $\| e^{\hat{A}^t}\|$ 有界。但是，由 $\hat{A}$ 为约当规范型可知 $e^{\hat{A}^t}$ 每一元的形式为

$$t ^ {\beta_ {i}} \mathrm{e} ^ {\alpha_ {i} t + \mathrm{j} \omega_ {i} t}, \quad \alpha_ {i} + \mathrm{j} \omega_ {i} = \lambda_ {i} (\hat {\boldsymbol {A}}) = \lambda_ {i} (\boldsymbol {A}) \tag {9-261}$$

式中， $\lambda_{i}(\cdot)$ 为 $(\cdot)$ 的特征值； $\beta_{i}$ 为特征值的重数。注意到式(9-261)中，当 $\alpha_{i} < 0$ 时对任何正整数 $\beta_{i}$ ，此元在 $[0, \infty)$ 上为有界，而 $\alpha_{i} = 0$ 时只对 $\beta_{i} = 0$ ，此元在 $[0, \infty)$ 上为有界。同时， $\mathrm{e}^{\hat{A}t}$ 的每一个元有界意味着 $\| \mathrm{e}^{\hat{A}t} \|$ 有界。由此可知，当且仅当 $A$ 的所有特征值均具有负或零实部，且具有零实部的特征值为单根时， $\| \mathrm{e}^{\hat{A}t} \|$ 为有界，也就是系统的每一个平衡状态为李雅普诺夫意义下的稳定。结论1）证毕。

2) 由式(9-257) 可知, 当且仅当 $\| e^{A^t} \|$ 对一切 $t \geqslant 0$ 为有界, 且当 $t \to 0$ 时 $\| e^{A^t} \| \to 0$ , 零平衡状态 $x_e = 0$ 为渐近稳定。如上所证, 当且仅当 $\mathbf{A}$ 的所有特征值均具有负或零实部时, $\| e^{A^t} \|$ 有界。又根据式(9-260) 和式(9-261) 可知, 当且仅当 $t \to \infty$ 时 $t^{\beta_i} e^{\alpha_i + j\omega_i t} \to 0$ , 可保证 $t \to 0$ 时 $\| e^{A^t} \| \to 0$ , 这等价于 $\mathbf{A}$ 的特征值均具有负实部。结论 2) 证毕。

由于所讨论的系统为线性定常系统,当其为稳定时必是一致稳定,当其为渐定稳定时必是大范围一致渐近稳定。
