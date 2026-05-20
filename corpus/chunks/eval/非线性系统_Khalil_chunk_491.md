$$\delta \leqslant \min \left\{t _ {1} - t _ {0}, \frac {r}{L r + h}, \frac {\rho}{L} \right\}, \quad \rho < 1 \tag {C.4}$$

则方程(C.2)在 $S$ 内有唯一解。但证明尚未结束，因为我们要证明在所有连续函数 $x(t)$ 中解的唯一性，即在 $\mathcal{X}$ 内解的唯一性，归结为证明方程(C.2)在 $\mathcal{X}$ 内的任何解都在 $S$ 内。为了理解这一点，注意到 $x(t_0) = x_0$ 在球 $B$ 内，所以对某一时间区间任意连续解 $x(t)$ 也一定在球 $B$ 内。假定 $x(t)$ 离开球 $B$ ，并设 $t_0 + \mu$ 是 $x(t)$ 与球 $B$ 边界第一次相交的时间，则

$$\| x (t _ {0} + \mu) - x _ {0} \| = r$$

另一方面，对于所有 $t \leqslant t_0 + \mu$ ，有

$$
\begin{array}{l} \| x (t) - x _ {0} \| \leqslant \int_ {t _ {0}} ^ {t} [ \| f (s, x (s)) - f (s, x _ {0}) \| + \| f (s, x _ {0}) \| ] d s \\ \leqslant \int_ {t _ {0}} ^ {t} [ L \| x (s) - x _ {0} \| + h ] d s \leqslant \int_ {t _ {0}} ^ {t} (L r + h) d s \\ \end{array}
$$

因此 $r = \| x(t_0 + \mu) - x_0\| \leqslant (Lr + h)\mu \Rightarrow \mu \geqslant \frac{r}{Lr + h}\geqslant \delta$

由此可知，在时间区间 $[t_0, t_0 + \delta]$ 内，解 $x(t)$ 不可能离开集合 $B$ ，这就是说 $\mathcal{X}$ 内的任意解也在 $S$ 内，因而在 $S$ 内解的唯一性也就是在 $\mathcal{X}$ 内解的唯一性。

证明定理3.2 证明的关键是说明可使定理3.1中的常数 $\delta$ 与初始状态 $x_0$ 无关。由式(C.4)可知 $\delta$ 与初始状态的关系是通过 $r / (Lr + h)$ 一项中的常数 $h$ 来实现的。由于在目前情况下，利普希茨条件全局成立，故可选择 $r$ 为任意大。因此，对于任何有限的 $h$ ，可选择足够大的 $r$ ，使 $r / (Lr + h) > \rho / L$ 。这样，式(C.4)就可以简化为

$$\delta \leqslant \min \Big \{t _ {1} - t _ {0}, \frac {\rho}{L} \Big \}, \qquad \rho < 1$$

如果 $t_1 - t_0 \leqslant \rho / L$ ，选择 $\delta = t_1 - t_0$ 即可证明定理3.2。否则，选择 $\delta$ 满足 $\delta \leqslant \rho / L$ ，将 $[t_0, t_1]$ 划分为有限个长度为 $\delta \leqslant \rho / L$ 的子区间，重复应用定理3.1，即可证明定理3.2①。
