$$\dot {x} = - [ 1 + g (t) ] x ^ {3}$$

其中 $g(t)$ 连续，且对于所有 $t \geqslant 0$ ，有 $g(t) \geqslant 0$ 。利用备选李雅普诺夫函数 $V(x) = x^{2}/2$ ，可得

$$\dot {V} (t, x) = - [ 1 + g (t) ] x ^ {4} \leqslant - x ^ {4}, \quad \forall x \in R, \forall t \geqslant 0$$

$W_{1}(x)=W_{2}(x)=V(x)$ 及 $W_{3}(x)=x^{4}$ 全局满足定理 4.9 的假设, 因此原点是全局一致渐近稳定的。

例4.20 考虑系统

$$\dot {x} _ {1} = - x _ {1} - g (t) x _ {2}\dot {x} _ {2} = x _ {1} - x _ {2}$$

其中, $g(t)$ 是连续可微函数,且满足

$$0 \leqslant g (t) \leqslant k \quad {\text {和}} \quad \dot {g} (t) \leqslant g (t), \forall t \geqslant 0$$

取 $V(t,x) = x_1^2 +[1 + g(t)]x_2^2$ ，作为备选李雅普诺夫函数。很容易看出

$$x _ {1} ^ {2} + x _ {2} ^ {2} \leqslant V (t, x) \leqslant x _ {1} ^ {2} + (1 + k) x _ {2} ^ {2}, \forall x \in R ^ {2}$$

因此， $V(t,x)$ 是正定递减的，且径向无界。V沿系统轨线的导数为

$$\dot {V} (t, x) = - 2 x _ {1} ^ {2} + 2 x _ {1} x _ {2} - [ 2 + 2 g (t) - \dot {g} (t) ] x _ {2} ^ {2}$$

利用不等式 $2 + 2g(t) - \dot{g} (t)\geqslant 2 + 2g(t) - g(t)\geqslant 2$

得 $\dot{V} (t,x)\leqslant -2x_1^2 +2x_1x_2 - 2x_2^2 = -\left[ \begin{array}{c}x_{1}\\ x_{2} \end{array} \right]^{\mathrm{T}}\left[ \begin{array}{cc}2 & -1\\ -1 & 2 \end{array} \right]\left[ \begin{array}{c}x_{1}\\ x_{2} \end{array} \right]\stackrel {\mathrm{def}}{=} - x^{\mathrm{T}}Qx$

其中 Q 是正定的。因此， $\dot{V}(t,x)$ 是负定的。所以，正定二次函数 $W_{1}, W_{2}$ 和 $W_{3}$ 全局满足定理 4.9 的所有假设。由正定二次函数 $x^{T}Px$ 满足

$$\lambda_ {\min} (P) x ^ {T} x \leqslant x ^ {T} P x \leqslant \lambda_ {\max} (P) x ^ {T} x$$

可知，a=2 全局满足定理 4.10 的条件。因此，原点是全局指数稳定的。

例4.21 线性时变系统

$$\dot {x} = A (t) x \tag {4.27}$$

有一个平衡点 $x = 0$ 。设 $A(t)$ 对于所有 $t \geqslant 0$ 连续。假设存在连续可微、有界的正定对称矩阵 $P(t)$ ，即 $0 < c_{1}I \leqslant P(t) \leqslant c_{2}I, \forall t \geqslant 0$

满足矩阵微分方程 $-\dot{P}(t)=P(t)A(t)+A^{\mathrm{T}}(t)P(t)+Q(t)$ (4.28)

其中， $Q(t)$ 是连续的正定对称矩阵，即，

$$Q (t) \geqslant c _ {3} I > 0, \forall t \geqslant 0$$

备选李雅普诺夫函数 $V(t,x)=x^{\mathrm{T}}P(t)x$

满足 $c_{1}\| x\|_{2}^{2}\leqslant V(t,x)\leqslant c_{2}\| x\|_{2}^{2}$

其沿系统(4.27)的轨线的导数为

$$
\begin{array}{l} \dot {V} (t, x) = x ^ {\mathrm{T}} \dot {P} (t) x + x ^ {\mathrm{T}} P (t) \dot {x} + \dot {x} ^ {\mathrm{T}} P (t) x \\ = x ^ {\mathrm{T}} [ \dot {P} (t) + P (t) A (t) + A ^ {\mathrm{T}} (t) P (t) ] x = - x ^ {\mathrm{T}} Q (t) x \leqslant - c _ {3} \| x \| _ {2} ^ {2} \\ \end{array}
$$

因此，a=2 全局满足定理 4.10 的所有假设，由此可得原点是全局指数稳定的。
