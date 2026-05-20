在 y=0 处有一个平衡点, 因为对于任意固定的 $x \in R^{n}$ , 有

$$G (t, x, y, 0) = g (t, \varphi (x), y + h (t, \varphi (x)), 0)$$

边界层模型(C.71)可以表示为式(11.14)的边界层模型形式, $\varphi(x)\in D_{x}$ 为冻结参数(frozen parameter)。由于不等式(11.15)对于冻结参数一致成立,很明显对于所有 $x\in R^{n}$ ,模型(C.71)的解满足同一不等式,即

$$\| y (\tau) \| \leqslant k \| y (0) \| \exp (- \gamma \tau), \forall \| y (0) \| < \rho_ {0}, \forall (t, x) \in [ 0, t _ {1} ] \times R ^ {n}, \forall \tau \geqslant 0 \tag {C.72}$$

对方程(C.69)和方程(C.70)的简化问题是

$$\dot {x} = F (t, x, 0, 0), \quad \dot {x} (t _ {0}) = \xi_ {0} \tag {C.73}$$

只要 $x \in S_{1}$ ，该问题就与方程(11.8)的简化问题相同。由于方程(11.8)有唯一解 $\bar{x}(t)$ ，对于所有 $t \in [t_0, t_1]$ 和 $\bar{x}(t) \in S$ 有定义，故 $\bar{x}(t)$ 是 $t \in [t_0, t_1]$ 时方程(C.73)的唯一解。我们继续以方程(C.69)和方程(C.70)给出的修正奇异扰动问题证明此定理。在此基础上证明对于足够小的 $\varepsilon$ ，方程(C.69)和方程(C.70)的解 $x(t, \varepsilon)$ 属于 $S_1$ 。这样就证明了原始问题与修正问题有相同的解，并对方程(11.10)和方程(11.11)给出的原始问题证明了此定理。

考虑边界层模型(C.71)，由于 $[\partial G / \partial y]$ 对 $(t,x)$ 的一阶偏导数有界，且对于所有 $(t,x)$ ，有 $G(t,x,0,0) = 0$ ，因此雅可比矩阵 $[\partial G / \partial t]$ 和 $[\partial G / \partial x]$ 满足

$$\left\| \frac {\partial G}{\partial t} \right\| \leqslant L _ {1} \| y \|; \quad \left\| \frac {\partial G}{\partial x} \right\| \leqslant L _ {2} \| y \|$$

利用这些估计和式(C.72)，根据引理9.8可知存在一个李雅普诺夫函数 $V_{1}(t,x,y)$ ，对于所有 $y\in \{\| y\| < \rho_0\}$ 和所有 $(t,x)\in [0,t_1]\times R^n$ ，满足

$$c _ {1} \| y \| ^ {2} \leqslant V _ {1} (t, x, y) \leqslant c _ {2} \| y \| ^ {2} \tag {C.74}\frac {\partial V _ {1}}{\partial y} G (t, x, y, 0) \leqslant - c _ {3} \| y \| ^ {2} \tag {C.75}\left\| \frac {\partial V _ {1}}{\partial y} \right\| \leqslant c _ {4} \| y \|; \quad \left\| \frac {\partial V _ {1}}{\partial t} \right\| \leqslant c _ {5} \| y \| ^ {2}; \quad \left\| \frac {\partial V _ {1}}{\partial x} \right\| \leqslant c _ {6} \| y \| ^ {2} \tag {C.76}$$

$V_{1}$ 沿整个系统(C.69)\~(C.70)轨线的导数为

$$
\begin{array}{l} \dot {V} _ {1} = \frac {1}{\varepsilon} \frac {\partial V _ {1}}{\partial y} G (t, x, y, \varepsilon) + \frac {\partial V _ {1}}{\partial t} + \frac {\partial V _ {1}}{\partial x} F (t, x, y, \varepsilon) \\ = \frac {1}{\varepsilon} \frac {\partial V _ {1}}{\partial y} G (t, x, y, 0) + \frac {1}{\varepsilon} \frac {\partial V _ {1}}{\partial y} [ G (t, x, y, \varepsilon) - G (t, x, y, 0) ] \\ + \frac {\partial V _ {1}}{\partial t} + \frac {\partial V _ {1}}{\partial x} F (t, x, y, \varepsilon) \\ \end{array}
$$

利用式(C.75)、式(C.76)和估计
