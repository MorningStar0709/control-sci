取 $t = 0$ ，可得 $\phi (T;0,y,\varepsilon) = \phi (0;0,y,\varepsilon) = y$

这说明 y 是方程(10.17)的一个解。

引理10.2 在上述条件下,存在正常数 $k$ 和 $\varepsilon_{2}$ ,使得方程(10.17)对于所有 $|\varepsilon|<\varepsilon_{2}$ ,在 $\|x\|<k|\varepsilon|$ 内有唯一解。

证明: 当 $\varepsilon=0$ 时, $\phi(t;0,x,0)$ 是非扰动系统 (10.16) 始于 $(0,x)$ 的解。由于 x=0 是方

程(10.16)的一个平衡点,对于所有 $t\geqslant0,0=\phi(t;0,0,0)$ ,因此有

$$P _ {0} (0) = \phi (T; 0, 0, 0) = 0$$

根据隐函数定理,如果雅可比矩阵

$$J = I - \left. \frac {\partial P _ {\varepsilon}}{\partial x} \right| _ {x = 0, \varepsilon = 0}$$

是非奇异的,则存在一个正常数 $\varepsilon_{2}$ , 使方程(10.17)在 $|\varepsilon|<\varepsilon_{2}$ 内有唯一解 $p_{\varepsilon}$ 。为了检验雅可比矩阵的非奇异性,回顾解 $\phi(t;0,x,\varepsilon)$ 是由下式给出的:

$$\phi (t; 0, x, \varepsilon) = x + \int_ {0} ^ {t} [ f (\phi (\tau ; 0, x, \varepsilon)) + \varepsilon g (\tau , \phi (\tau ; 0, x, \varepsilon), \varepsilon) ] d \tau$$

对 $x$ 微分, 得 $\frac{\partial}{\partial x}\phi(t;0,x,\varepsilon) = I + \int_0^t\left[\frac{\partial f}{\partial x} (\cdot)\frac{\partial\phi}{\partial x} (\cdot) + \varepsilon \frac{\partial g}{\partial x} (\cdot)\frac{\partial\phi}{\partial x} (\cdot)\right]d\tau$

设 $U(t) = \frac{\partial}{\partial x}\phi (t;0,x,\varepsilon)\Bigg|_{x = 0,\varepsilon = 0}$

则有 $U(t)=I+\int_{0}^{t}\frac{\partial f}{\partial x}(0)U(\tau)d\tau=I+\int_{0}^{t}AU(\tau)d\tau$

和 $\frac{d}{dt} U(t) = AU(t), U(0) = I$

这样有 $u(t) = \exp (At)$ ，因而

$$I - \left. \frac {\partial P _ {\varepsilon}}{\partial x} \right| _ {x = 0, \varepsilon = 0} = I - \exp (A T)$$

因为 $A$ 是赫尔维茨矩阵， $\exp (AT)$ 的所有特征值严格地在单位圆内①，因而 $J$ 是非奇异的。因此，方程(10.17)有唯一解 $p_{\varepsilon}, \forall |\varepsilon| < \varepsilon_2$ 。另一方面，由于当 $t$ 趋于无穷时，方程(10.15)的所有解都趋于原点的 $O(\varepsilon)$ 邻域，所以 $p_{\varepsilon}$ 一定是 $O(\varepsilon)$ ，因为当 $t$ 趋于无穷时，相应的周期解无限次经过 $p_{\varepsilon}$ 。

现在很明显,对于足够小的 $\varepsilon$ , 扰动系统(10.15)在原点的 $O(\varepsilon)$ 邻域内有一个以 T 为周期的解。事实上,由于方程(10.17)的解的唯一性,周期解一定是唯一的。应用 A 的赫尔维茨性质,可以进一步证明周期解是指数稳定的。

引理10.3 在上述条件下,如果 $\bar{x}(t,\varepsilon)$ 是方程(10.15)的以 $T$ 为周期的解,使得 $\| \bar{x}(t,\varepsilon)\| \leqslant k|\varepsilon|$ ,则 $\bar{x}(t,\varepsilon)$ 是指数稳定的。

证明:研究 $\bar{x}(t,\varepsilon)$ 的稳定性的系统过程是运用变量代换 $z=x-\bar{x}(t,\varepsilon)$ ，在 z=0 处研究平衡点的稳定性。新的变量 z 满足方程
