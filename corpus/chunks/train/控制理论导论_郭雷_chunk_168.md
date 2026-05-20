$$0 < \varepsilon_ {0} \leqslant | x (t _ {N}; x _ {0}) | < h.$$

根据正定函数的性质3, 存在正数 $v_{0}$ 满足

$$W (x (t _ {N}; x _ {0})) \geqslant v _ {0} > 0,$$

这与式 (2.4.24) 相矛盾，从而有 $\lim_{t \to +\infty} x(t; x_0) = 0$ .

定理2.4.9 对于微分方程(2.4.19)，如果存在一个连续可微函数 $W(x)$ ，它沿方程(2.4.19)的解关于时间 $t$ 的全导数 $\dot{W} (x)\mid_{(2.4.19)}$ 是正定的，并且在 $x = 0$ 的任一邻域内 $W(x)$ 总能取到正值，则微分方程(2.4.19)的零平衡解是不稳定的.

证明 根据假设 $\dot{W}(x)\mid_{(2.4.19)}$ 在闭球 $|x|\leqslant h$ 上是正定的，并且对于任意的 $\delta >0$ ，存在 $x_0$ ，当 $|x_0| < \delta$ 时有

$$W (x _ {0}) > h.$$

今证方程 (2.4.19) 的轨线 $x(t; x_0)$ 不能永远停留在闭球 $|x| \leqslant h$ 内。事实上，如果不然，则

$$\left| x (t; x _ {0}) \right| \leqslant h, \quad \forall t \in [ 0, + \infty).$$

于是作为 $t \geqslant 0$ 的连续函数 $W(x(t; x_0))$ 有界.

另一方面，当 $|x(t;x_0)|\leqslant h$ 时，有

$$\dot {W} (x (t; x _ {0})) \mid_ {(2. 4. 1 9)} \geqslant 0, \quad \forall t \geqslant 0.$$

所以 $W(x(t;x_0))\geqslant W(x_0) > 0,\forall t\geqslant 0.$

根据正函数的性质 2, 必定存在 $\alpha_{1} > 0$ , 使得

$$h \geqslant | x (t; x _ {0}) | \geqslant \alpha_ {1}, \quad \forall t \geqslant 0.$$

由此根据正定函数的性质3, 存在 $v_{1} > 0$ 使

$$\dot {W} (x (t; x _ {0})) \mid_ {(2. 4. 1 9)} \geqslant v _ {1} > 0, \quad \forall t \geqslant 0.$$

积分上式得到

$$W (x (t; x _ {0})) \geqslant W (x _ {0}) + v _ {1} t, \quad \forall t \geqslant 0.$$

所以当 $t \to +\infty$ 时，上式右端趋于无穷，而这与 $W(x(t; x_0))$ 有界矛盾.

因此，微分方程(2.4.19)的轨线 $x(t;x_0)$ 不能永远停留在闭球内，这表明微分方程(2.4.19)的零平衡解是不稳定的.

定理2.4.10 对于微分方程(2.4.19)，如果有一个连续可微标量函数 $W(x)$ ，使得当 $|x| \leqslant h$ 时，成立不等式

$$\dot {W} \mid_ {(2. 4. 1 9)} \geqslant \lambda W, \quad \forall t \geqslant 0,$$

其中 $\lambda$ 为某正常数，并且 $W(x)$ 在 $x = 0$ 的任一邻域内总能取到正值，则微分方程(2.4.19)的零平衡解是不稳定的.

证明 对于任给的 $\delta > 0$ , 依假设存在 $x_0$ , 使得当 $|x_0| < \delta$ 时有 $W(x_0) > 0$ .

设微分方程 (2.4.19) 的满足 $x(0) = x_0$ 的解为 $x(t; x_0)$ . 今证它所对应的轨线不能永远停留在闭球 $|x| \leqslant h$ 内.

用反证法，设

$$\left| x (t; x _ {0}) \right| \leqslant h, \quad \forall t \geqslant 0.$$

于是当 $t \geqslant 0$ 时， $W(x(t; x_0))$ 有界。这时依假设有

$$\dot {W} (x (t; x _ {0})) \mid_ {(2. 4. 1 9)} \geqslant \lambda W (x (t; x _ {0})), \quad \forall t \geqslant 0. \tag {2.4.25}$$

由此可得

$$W (x (t; x _ {0})) \geqslant W (x _ {0}) \mathrm{e} ^ {\lambda t}, \quad \forall t \geqslant 0.$$

当 $t \to +\infty$ 时，上不等式的右端趋于无穷，与 $W(x(t; x_0))$ 有界相矛盾。这说明 $x(t; x_0)$ 不能永远停留在闭球 $|x| \leqslant h$ 内部，即微分方程 (2.4.19) 的零平衡解是不稳定的。
