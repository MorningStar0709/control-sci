$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - \sin x _ {3} + x _ {1} [ - 2 x _ {3} - \operatorname{sat} (y) ] ^ {2} \\ \dot {x} _ {3} = - 2 x _ {3} - \operatorname{sat} (y) \\ \text { 其中 } y = - 2 x _ {1} - 5 x _ {2} + 2 x _ {3} \\ \end{array}

\begin{array}{l} \dot {x} _ {1} = - 2 x _ {1} + x _ {1} ^ {3} \\ \dot {x} _ {2} = - x _ {2} + x _ {1} ^ {2} \tag {3} \\ \dot {x} _ {3} = - x _ {3} \\ \end{array}
\dot {x} _ {1} = - x _ {1}
$$

4.33 二阶系统 $\dot{x} = f(x)$ ，其中 $f(0) = 0$ 并且 $f(x)$ 在原点的某个邻域内是二阶连续可微的。假设 $[ \partial f / \partial x ] (0) = -B$ ，其中 $B$ 为赫尔维茨的。令 $P$ 是李雅普诺夫方程 $PB + B^{\mathrm{T}}P = -I$ 的正定解并设 $V(x) = x^{\mathrm{T}}Px$ 。试证存在 $c^{*} > 0$ ，对于每个 $0 < c < c^{*}$ ，曲面 $V(x) = c$ 是封闭的并且对于所有 $x \in \{V(x) = c\}$ 有 $[ \partial f / \partial x ] f(x) > 0$ 。

4.34 证明引理 4.2。

4.35 设 $\alpha$ 是区间 $[0, a)$ 上的 K 类函数, 证明

$$\alpha \left(r _ {1} + r _ {2}\right) \leqslant \alpha \left(2 r _ {1}\right) + \alpha \left(2 r _ {2}\right), \quad \forall r _ {1}, r _ {2} \in [ 0, a / 2)$$

4.36 标量系统 $\dot{x} = -x/(t+1)$ , $t \geqslant 0$ 的原点是一致渐近稳定的吗?

4.37 对于下列每个线性系统,用二次李雅普诺夫函数证明各个系统的原点是指数稳定的。

$$
(1) \quad \dot {x} = \left[ \begin{array}{c c} - 1 & \alpha (t) \\ \alpha (t) & - 2 \end{array} \right] x, | \alpha (t) | \leqslant 1

(2) \quad \dot {x} = \left[ \begin{array}{c c} - 1 & \alpha (t) \\ - \alpha (t) & - 2 \end{array} \right] x

(3) \quad \dot {x} = \left[ \begin{array}{c c} 0 & 1 \\ - 1 & - \alpha (t) \end{array} \right] x, \alpha (t) \geqslant 2

(4) \quad \dot {x} = \left[ \begin{array}{c c} - 1 & 0 \\ \alpha (t) & - 2 \end{array} \right] x
$$

在每个系统中,对于所有 $t \geqslant 0, \alpha(t)$ 是连续且有界的。

4.38 （见文献[95]）带有时变元件的RLC电路的表示式为

$$\dot {x} _ {1} = \frac {1}{L (t)} x _ {2}, \quad \dot {x} _ {2} = - \frac {1}{C (t)} x _ {1} - \frac {R (t)}{L (t)} x _ {2}$$

假设 $L(t), C(t)$ 和 $R(t)$ 是连续可微的且对于所有 $t \geqslant 0$ 满足不等式 $k_{1} \leqslant L(t) \leqslant k_{2}$ , $k_{3} \leqslant C(t) \leqslant k_{4}$ 和 $k_{5} \leqslant R(t) \leqslant k_{6}$ 。其中 $k_{1}, k_{3}$ 和 $k_{5}$ 是正的，李雅普诺夫函数为

$$V (t, x) = \left[ R (t) + \frac {2 L (t)}{R (t) C (t)} \right] x _ {1} ^ {2} + 2 x _ {1} x _ {2} + \frac {2}{R (t)} x _ {2} ^ {2}$$

(a) 证明 $V(t,x)$ 是正定且递减的。

(b) 为保证原点是指数稳定的,试求出 $\dot{L}(t)$ , $\dot{C}(t)$ 和 $\dot{R}(t)$ 应满足的条件。

4.39 （见文献[154]）带有时变摩擦的单摆系统的表示式为

$$\dot {x} _ {1} = x _ {2}, \quad \dot {x} _ {2} = - \sin x _ {1} - g (t) x _ {2}$$

假设 $g(t)$ 连续可微且对于所有 $t \geqslant 0$ 满足：

$$0 < a < \alpha \leqslant g (t) \leqslant \beta < \infty \quad {\text {和}} \quad \dot {g} (t) \leqslant \gamma < 2$$

考虑备选李雅普诺夫函数
