则满足互联条件。满足式(11.39)和 $\| \partial V / \partial x\| \leqslant k_1\psi_1(x)$ 的李雅普诺夫函数 $V(x)$ 称为二次型李雅普诺夫函数，并称 $\psi_{1}$ 为比较函数。这样，如果能找到比较函数为 $\psi_{1}$ 和 $\psi_{2}$ 的二次型李雅普诺夫函数 $V$ 和 $W$ ，使得 $\| f(x,h(x))\|$ 以 $\psi_1(x)$ 为界， $\| f(x,y + h(x)) - f(x,h(x))\|$ 以 $\psi_{2}(y)$ 为界，则搜寻成功。如果成功地找到 $V$ 和 $W$ ，就可以确定对于 $\varepsilon < \varepsilon^{*}$ ，原点是指数稳定的。对于给定的 $\varepsilon < \varepsilon^{*}$ ，存在一个范围 $(d_{1},d_{2})$ ，使得对于任何 $d\in (d_1,d_2)$ ，函数 $\nu (x,y) = (1 - d)V(x)+$ $dW(x,y)$ 是一个有效李雅普诺夫函数。自由选择 $d$ 可以实现其他目的，如改善吸引区的估计值。

例11.12 二阶系统 $\begin{array}{rcl}\dot{x} & = & f(x,z) = x - x^3 +z\\ \varepsilon \dot{z} & = & g(x,z) = -x - z \end{array}$

在原点有唯一平衡点。设 $y = z - h(x) = z + x$ 并重写系统为

$$
\begin{array}{l} \dot {x} = - x ^ {3} + y \\ \varepsilon \dot {y} = - y + \varepsilon \left(- x ^ {3} + y\right) \\ \end{array}
$$

对于降阶系统 $\dot{x} = -x^{3}$

取 $V(x) = (1 / 4)x^4,\psi_1(x) = |x|^3$ 和 $\alpha_{1} = 1$ 时，满足式(11.39)。对于边界层系统

$$\frac {d y}{d \tau} = - y$$

取 $W(y) = (1 / 2)y^2$ ，当 $\psi_{2}(y) = |y|$ 且 $\alpha_{2} = 1$ 时，方程满足式(11.40)。至于式(11.43)和式(11.44)的互联条件，有

$$\frac {\partial V}{\partial x} [ f (x, y + h (x)) - f (x, h (x)) ] = x ^ {3} y \leqslant \psi_ {1} \psi_ {2}$$

和 $\frac{\partial W}{\partial y} f(x,y + h(x)) = y(-x^3 +y)\leqslant \psi_1\psi_2 + \psi_2^2$

注意 $\partial W / \partial x = 0$ 。因此，当 $\beta_{1} = \beta_{2} = \gamma = 1$ 时，式(11.43)和式(11.44)成立。于是当 $\varepsilon < \varepsilon^{*} = 0.5$ 时，原点是渐近稳定的。实际上，由于所有条件全局满足，且 $\nu (x,y) = (1 - d)V(x) + dW(y)$ 径向无界，故当 $\varepsilon < 0.5$ 时，原点是全局渐近稳定的。为了理解该边界的保守程度，考虑在原点线性化的特征方程

$$\lambda^ {2} + \left(\frac {1}{\varepsilon} - 1\right) \lambda = 0$$

它表明当 $\varepsilon > 1$ 时, 原点是非稳定的。由于本例是简单的二阶系统, 所以可计算出李雅普诺夫函数

$$\nu (x, y) = \frac {1 - d}{4} x ^ {4} + \frac {d}{2} y ^ {2}$$

沿整个奇异扰动系统的轨线的导数,与定理11.3提供的边界相比,看看是否能够得到 $\varepsilon$ 的一个宽松上界:

$$
\begin{array}{l} \dot {\nu} = (1 - d) x ^ {3} \left(- x ^ {3} + y\right) - \frac {d}{\varepsilon} y ^ {2} + d y \left(- x ^ {3} + y\right) \\ = - (1 - d) x ^ {6} + (1 - 2 d) x ^ {3} y - d \left(\frac {1}{\varepsilon} - 1\right) y ^ {2} \\ \end{array}
$$

很明显,选择 d=1/2 消去向量积项,得

$$\dot {\nu} = - \frac {1}{2} x ^ {6} - \frac {1}{2} \left(\frac {1}{\varepsilon} - 1\right) y ^ {2}$$

对于所有 $\varepsilon < 1$ ，它是负定的。该估计确实没有定理 11.3 给出的保守。事实上，这正是使原点渐近稳定的 $\varepsilon$ 的实际取值范围。

例11.13 系统 $\dot{x} = -x + z$ $\varepsilon \dot{z} = \arctan (1 - x - z)$

在 $(0.5,0.5)$ 处有一个平衡点。应用变量代换

$$\tilde {x} = x - 0. 5; \quad \tilde {z} = z - 0. 5$$
