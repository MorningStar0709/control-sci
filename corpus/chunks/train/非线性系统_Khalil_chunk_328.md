$$\varepsilon \frac {d y}{d t} = \frac {d y}{d \tau}; \text {因此} \frac {d \tau}{d t} = \frac {1}{\varepsilon}$$

并用 $\tau = 0$ 作为 $t = t_0$ 时刻的初始值。新的时间变量 $\tau = (t - t_0) / \varepsilon$ 延伸了，即如果 $\varepsilon$ 趋于零，则 $\tau$ 趋于无穷，即使有限的 $t$ 比 $t_0$ 稍微大一个固定（与 $\varepsilon$ 无关）的差值。在 $\tau$ 时间尺度下，方程(11.11)表示为

$$\frac {d y}{d \tau} = g (t, x, y + h (t, x), \varepsilon) - \varepsilon \frac {\partial h}{\partial t} \tag {11.12}- \varepsilon \frac {\partial h}{\partial x} f (t, x, y + h (t, x), \varepsilon), \quad y (0) = \eta (\varepsilon) - h \left(t _ {0}, \xi (\varepsilon)\right)$$

上述方程中的变量 t 和 x 变化缓慢, 因为在 $\tau$ 时间尺度上, 它们分别为

$$t = t _ {0} + \varepsilon \tau , \qquad x = x (t _ {0} + \varepsilon \tau , \varepsilon)$$

令 $\varepsilon=0$ , 当 $t=t_{0}$ 和 $x=\xi_{0}$ 时冻结这些变量, 方程(11.12)降阶为自治系统

$$\frac {d y}{d \tau} = g (t _ {0}, \xi_ {0}, y + h (t _ {0}, \xi_ {0}), 0), \quad y (0) = \eta (0) - h (t _ {0}, \xi_ {0}) \stackrel {\text { def }} {=} \eta_ {0} - h (t _ {0}, \xi_ {0}) \tag {11.13}$$

其平衡点为 $y = 0$ 。如果该平衡点是渐近稳定的，且 $y(0)$ 属于其吸引区，则有理由希望方程(11.13)的解在边界层区间内达到原点的 $O(\varepsilon)$ 邻域。在该区间之外，需要一个稳定性质，以保证 $y(\tau)$ 继续趋于零，而慢变参数 $(t,x)$ 远离其初始值 $(t_0,\xi_0)$ 。为了分析这种情况，允许冻结参数在慢变参数 $(t,x)$ 区域内取值①。假设降阶问题的解 $\bar{x}(t)$ 定义在 $t\in [0,t_1]$ ，且对于某个定义域 $D_{x}$ ，有 $\bar{x} (t)\in D_x\subset R^n$ 。把方程(11.13)重写为

$$\frac {d y}{d \tau} = g (t, x, y + h (t, x), 0) \tag {11.14}$$

其中，把 $(t,x)\in [0,t_1]\times D_x$ 看成固定参数，把方程(11.14)称为边界层模型（boundary-layer model)或边界层系统，有时也把方程(11.13)称为边界层模型。这样并不会引起混淆，因为方程(11.13)是由方程(11.14)在给定的初始时间和初始状态下计算得出的。对于方程(11.14)，最关键的稳定性是其原点的指数稳定性和对冻结参数的一致性，如下面的定义所示。

定义11.1 如果存在正常数 $k, \gamma$ 和 $\rho_0$ ，使得方程(11.14)的解满足

$$\| y (\tau) \| \leqslant k \| y (0) \| \exp (- \gamma \tau), \forall \| y (0) \| < \rho_ {0}, \forall (t, x) \in [ 0, t _ {1} ] \times D _ {x}, \forall \tau \geqslant 0 \tag {11.15}$$

则边界层系统(11.14)的平衡点 $y = 0$ 是指数稳定的，且对于 $(t,x)\in [0,t_1]\times D_x$ 一致。

除了平凡解,即边界层模型的解是闭式解,必须通过线性化或李雅普诺夫分析法验证原点的指数稳定性。可以证明(见习题11.5),如果雅可比矩阵 $\left[\partial g/\partial y\right]$ 满足特征值条件

$$\operatorname{Re} \left[ \lambda \left\{\frac {\partial g}{\partial y} (t, x, h (t, x), 0) \right\} \right] \leqslant - c < 0, \forall (t, x) \in [ 0, t _ {1} ] \times D _ {x} \tag {11.16}$$

则存在常数 $k, \gamma$ 和 $\rho_0$ 使式(11.15)成立。当然，这是个局部结果，即常数 $\rho_0$ 可能很小。还可以证明（见习题11.6），如果对于 $(t, x, y) \in [0, t_1] \times D_x \times D_y$ 其中 $D_y \subset R^m$ 是包含原点的定义域，存在一个李雅普诺夫函数 $V(t, x, y)$ 满足
