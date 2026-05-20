# 4.8 有界性和毕竟有界性

李雅普诺夫分析可用于说明状态方程解的有界性,即使在原点处无平衡点。为了激发这一思想,考虑标量方程 $\dot{x} = -x + \delta \sin t,\quad x(t_{0}) = a,\quad a > \delta > 0$

该方程无平衡点,且其解为

$$x (t) = e ^ {- (t - t _ {0})} a + \delta \int_ {t _ {0}} ^ {t} e ^ {- (t - \tau)} \sin \tau d \tau$$

此解的边界为

$$
\begin{array}{l} | x (t) | \leqslant e ^ {- (t - t _ {0})} a + \delta \int_ {t _ {0}} ^ {t} e ^ {- (t - \tau)} d \tau = e ^ {- (t - t _ {0})} a + \delta [ 1 - e ^ {- (t - t _ {0})} ] \\ \leqslant a, \forall t \geqslant t _ {0} \\ \end{array}
$$

上式表明: 解对于所有 $t \geqslant t_{0}$ 都有界, 且对 $t_{0}$ 一致, 即边界与 $t_{0}$ 无关。当此边界对于所有 $t \geqslant t_{0}$ 都成立时, 它将随时间变化而成为解的保守估计, 因为没有考虑到指数衰减项。但如果取任意数 b 满足 $\delta < b < a$ , 则容易看出

$$| x (t) | \leqslant b, \quad \forall t \geqslant t _ {0} + \ln \left(\frac {a - \delta}{b - \delta}\right)$$

边界 $b$ 同样与 $t_0$ 无关, 经过瞬态周期后, 它给出解的更好估计。这种情况称为解是一致毕竟有界的, $b$ 称为最终边界。通过李雅普诺夫分析就可以说明 $\dot{x} = -x + \delta$ 的解具有一致有界性和毕竟有界性, 而无须状态方程的显式解。由 $V(x) = x^2 / 2$ 出发, 计算 $V$ 沿系统轨线的导数, 得

$$\dot {V} = x \dot {x} = - x ^ {2} + x \delta \sin t \leqslant - x ^ {2} + \delta | x |$$

不等式的右边不是负定的,因为在原点附近,正线性项 $\delta|x|$ 与 $-x^{2}$ 项相比起决定作用。但在 $\{|x|\leqslant\delta\}$ 之外 $\dot{V}$ 是负的。由 $c>\delta^{2}/2$ 可知始于 $\{V(x)\leqslant c\}$ 内的解在所有未来时刻都保持在其内,因为 $\dot{V}$ 在边界 V=c 上是负的。因此,解是一致有界的。而且,如果取任意数 $\varepsilon$ 满足 $(\delta^{2}/2)<\varepsilon<c$ ,则 $\dot{V}$ 在 $\{\varepsilon\leqslant V\leqslant c\}$ 内为负,这说明在此集合内,V 单调递减直到解进入 $\{V\leqslant\varepsilon\}$ 内。从那一时刻起,解将不再离开 $\{V\leqslant\varepsilon\}$ ,因为 $\dot{V}$ 在边界 $V=\varepsilon$ 上为负。由此可得,解是一致毕竟有界的,且最终边界为 $|x|\leqslant\sqrt{2\varepsilon}$ 。

本节的目的是说明如何把李雅普诺夫分析用于描述系统

$$\dot {x} = f (t, x) \tag {4.32}$$

的类似结论。其中 $f: [0, \infty) \times D \to R^n$ 在 $[0, \infty) \times D$ 上是 $t$ 的分段连续函数，是 $x$ 的局部利普希茨函数，且 $D \subset R^n$ 是包含原点的定义域。
