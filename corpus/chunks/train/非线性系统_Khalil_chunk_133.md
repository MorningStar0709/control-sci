证明:由于线性系统在原点有一个指数稳定平衡点, $A(t)$ 连续且有界,定理4.12保证了存在一个连续可微且有界正定的对称矩阵 $P(t)$ 满足方程(4.28),其中 $Q(t)$ 是连续的正定对称矩阵。用 $V(t,x)=x^{\mathrm{T}}P(t)x$ 作为非线性系统的备选李雅普诺夫函数,则 $V(t,x)$ 沿系统轨线的导数为

$$
\begin{array}{l} \dot {V} (t, x) = x ^ {\mathrm{T}} P (t) f (t, x) + f ^ {\mathrm{T}} (t, x) P (t) x + x ^ {\mathrm{T}} \dot {P} (t) x \\ = x ^ {T} [ P (t) A (t) + A ^ {T} (t) P (t) + \dot {P} (t) ] x + 2 x ^ {T} P (t) g (t, x) \\ = - x ^ {T} Q (t) x + 2 x ^ {T} P (t) g (t, x) \\ \leqslant - c _ {3} \| x \| _ {2} ^ {2} + 2 c _ {2} L \| x \| _ {2} ^ {3} \\ \leqslant - \left(c _ {3} - 2 c _ {2} L \rho\right) \| x \| _ {2} ^ {2}, \forall \| x \| _ {2} <   \rho \\ \end{array}
$$

选择 $\rho < \min \{r, c_3 / (2c_2L)\}$ ，以保证当 $\|x\|_2 < \rho$ 时 $\dot{V}(t,x)$ 负定。因此，当 $\|x\|_2 < \rho$ 时定理4.10中的所有条件都满足。由此可得出结论，原点是指数稳定的。
