定义 2.4.13 $^{[10]}$ 称集合 $E(x_{0}) \stackrel{\mathrm{def}}{=} \{x \mid x = x(t;0,x_{0}), t \geqslant 0\}$ 为微分方程 (2.4.19) 过点 $(0,x_{0})$ 的正半轨线；当 $x_{0} \neq 0$ 时，称 $E(x_{0})$ 为非平凡正半轨线；如果存在序列 $\{t_{k}\}, t_{k} \to \infty (k \to \infty)$ ，使得

$$x ^ {*} = \lim _ {k \rightarrow \infty} x (t _ {k}; 0, x _ {0}),$$

则称 $x^{*}$ 为正半轨线 $E(x_0)$ 的 $\omega$ 极限点，正半轨线 $E(x_0)$ 的 $\omega$ 极限点全体称为 $\omega$ 极限集，记为 $\Omega(x_0)$ .

当 $x = 0$ 是微分方程 (2.4.19) 的全局渐近稳定平衡点时，则 $x = 0$ 是 (2.4.19) 的任何正半轨线 $E(x_0)$ 的唯一的 $\omega$ 极限点.

引理2.4.1[10] 设 $x^{*}$ 是 $E(x_{0})$ 的 $\omega$ 极限点, 则正半轨线 $E(x_{0})$ 上的点 $x(t;0,x_0)$ 都是 $\omega$ 极限点, 从而 $\Omega (x_0)$ 由半正轨线本身组成.

证明 留作练习.

定义 2.4.14 $^{[10]}$ 称集合 $M \subset R^{n}$ 为微分方程 (2.4.19) 的轨线的正向不变集，简称方程 (2.4.19) 的不变集，如果 $\forall x_{0} \in M$ 恒有 $x(t;0,x_{0}) \in M, \forall t \geqslant 0$ . 称 $x(t;t_{0},x_{0}) \to M (t \to \infty)$ ，如果 $\exists p \in M$ ，使得 $x(t;t_{0},x_{0}) \to p (t \to \infty)$ .

定理 2.4.11 $^{[10]}$ 设 $W(x)$ 为区域 $D_{a} \stackrel{\text{def}}{=} \{x \mid |x| < a\}$ 上的连续可微正定标量函数，并满足

$$\dot {W} (x) \mid_ {(2. 4. 1 9)} \leqslant 0, \quad \forall x \in D _ {\alpha}.$$

如果集合 $M \stackrel{\mathrm{def}}{=} \{x \in D_a \mid \dot{W}(x) \big|_{(2.4.19)} = 0\}$ 除 $x = 0$ 外，不包含方程 (2.4.19) 的非零解的正半轨线，则方程 (2.4.19) 的零解渐近稳定。

引理2.4.2[10] 若 $x(t;0,x_0)$ 对一切 $t\geqslant 0$ 有界，则 $x(t;0,x_0)$ 的 $\omega$ 极限集 $\Omega (x_0)$ 有下列性质：

(1) $\Omega(x_0)$ 非空，紧集；

(2) 对于任意 $p \in \Omega(x_0), \Omega(x_0)$ 是微分方程 (2.4.19) 过点 $(0, p)$ 的轨线的不变集；

(3) 当 $t \to \infty$ 时, $x(t;0,x_0) \to \Omega(x_0)$ .

证明 依 $x(t) \stackrel{\mathrm{def}}{=} x(t;0, x_0)$ 有界假设，从Weierstrass定理可知存在 $t_k \to \infty$ ，使得 $\lim_{k \to \infty} x(t_k) = x^* \in \Omega(x_0)$ . 所以 $\Omega(x_0)$ 非空.

令 $p_k \in \Omega(x_0)$ 且 $p_k \to p (k \to \infty)$ , 于是 $\forall \varepsilon > 0$ , $\exists k_0$ , 使得

$$\left| p _ {k _ {0}} - p \right| < \frac {\varepsilon}{2}.$$

由于 $p_{k_0} \in \Omega(x_0)$ , 故 $\exists t_m \to \infty$ , 和充分大的正数 $N$ 使得

$$\left| x (t _ {m}) - p _ {k _ {0}} \right| < \frac {\varepsilon}{2}, \quad \forall m \geqslant N.$$

由此得到 $|x(t_m) - p| \leqslant |x(t_m) - p_{k_0}| + |p_{k_0} - p| < \varepsilon, \forall m \geqslant N, p \in \Omega(x_0)$ ，这表明 $\Omega(x_0)$ 为闭集。显然 $\Omega(x_0)$ 有界，因此 $\Omega(x_0)$ 为紧集。

注意到 $\forall p \in \Omega(x_0)$ , 存在 $t_k \to \infty$ 使得 $\lim_{t_k \to \infty} x(t_k) = p$ . 于是依微分方程解的唯一性有

$$x (t + t _ {k}) = x (t + t _ {k}, 0, x _ {0}) = x (t; 0, x (t _ {k}; 0, x _ {0})),$$

而根据微分方程解对初值的连续依赖性有
