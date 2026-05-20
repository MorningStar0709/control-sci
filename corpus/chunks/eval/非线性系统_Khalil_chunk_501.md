# C. 8 证明定理 4.17

对于 $\dot{x}=f(x),\quad x(0)=x_{0}\in R_{A}$ (C.11)

的任何给定解 $x(t)$ ，把时间变量 $t$ 代换为 $\tau = \int_0^t (1 + \| f(x(s)) \|)$ ，得到系统

$$\frac {d \bar {x}}{d \tau} = \frac {1}{1 + \| f (\bar {x}) \|} f (\bar {x}) \stackrel {\text {def}} {=} \bar {f} (\bar {x}), \quad \bar {x} (0) = x _ {0} \tag {C.12}$$

其中 $\bar{x}(\tau)=x(t)$ 是用 $\tau$ 代换 t 后的 $x(t)$ 。原点是式(C.12)的渐近稳定平衡点， $R_{A}$ 是其吸引区。如果 $V(x)$ 是方程(C.12)的李雅普诺夫函数，对于某个正定函数 $W(x)$ 满足

$$\frac {\partial V}{\partial x} \bar {f} (x) \leqslant - W (x)$$

则 $\frac{\partial V}{\partial x} f(x) = (1 + \| f(x)\|)\frac{\partial V}{\partial x}\bar{f} (x)\leqslant -(1 + \| f(x)\|)W(x)\leqslant -W(x)$

因为 $1 + \| f(x) \| \geqslant 1$ 。因此，上式足以构造出方程(C.12)的李雅普诺夫函数。用方程(C.12)构造李雅普诺夫函数更为容易，因为性质 $\| \bar{f} \| \leqslant 1$ 是指当 $t < 0$ 时，不具有有限逃逸时间。我们用式(C.12)证明定理的其余部分，将其改写为

$$\dot {x} = \bar {f} (x) \tag {C.13}$$

式中去掉了 $\bar{x}$ 上的横线，用 $\dot{x}$ 表示对 $\tau$ 的导数。

由引理8.1可知 $R_{A}$ 是开集，当 $R_{A} \neq R^{n}$ 时，设 $F$ 是 $R^{n}$ 中 $R_{A}$ 的补集。对于每个 $x \in R_{A}$ ，如果 $R_{A} \neq R^{n}$ ，定义

$$\omega (x) = \max \left\{\| x \|, \frac {1}{\operatorname{dist} (x , F)} - \frac {2}{\operatorname{dist} (0 , F)} \right\} \tag {C.14}$$

如果 $R_{A} = R^{n}$ ，则定义 $\omega (x) = \| x\|$ 。容易验证， $\omega (x)$ 是正定的且是局部利普希茨的。由于当 $x$ 趋于 $\partial R_{A}$ 时， $\mathrm{dist}(x,F)$ 趋于零，因此当 $x$ 趋于 $\partial R_{A}$ 时， $\omega (x)$ 趋于无穷，而且，当 $r_0 = (1 / 2)\mathrm{dist}(0,$ $F)$ 时，有

$$\inf _ {y \in F} \left\{\| x - y \| \right\} \geqslant \inf _ {y \in F} \left\{\| y \| - \| x \| \right\} \geqslant \inf _ {y \in F} \left\{\| y \| - r _ {0} \right\}, \quad \forall \| x \| \leqslant r _ {0}$$

故 $\mathrm{dist}(x,F)\geqslant \mathrm{dist}(0,F) - \frac{1}{2}\mathrm{dist}(0,F) = \frac{1}{2}\mathrm{dist}(0,F),\forall \| x\| \leqslant r_0$

因此，对于所有 $\| x\| \leqslant r_0$ ，有 $\omega (x) = \| x\|$ 。

引理C.2 方程(C.13)的解满足

$$\omega (x (t)) \leqslant \beta (\omega (x (0)), t), \forall t \geqslant 0, \forall x (0) \in R _ {A} \tag {C.15}$$

其中 $\beta (r,s)$ 是定义在所有 $r\geqslant 0$ 和 $s\geqslant 0$ 上的K类函数，且 $\beta (r,0)$ 是 $\mathcal{K}_{\infty}$ 类函数。
