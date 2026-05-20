$$\left| x (t; t _ {0}, x _ {0}) \right| \leqslant \| \Phi (t; t _ {0}) \| | x _ {0} | \leqslant M | x _ {0} | \mathrm{e} ^ {- \alpha (t - t _ {0})}, \quad \forall t \geqslant t _ {0}.$$

于是对于任给的 $\varepsilon > 0$ ，取 $\delta = \frac{\varepsilon}{M}$ ，则当 $|x_0| < \delta$ 时有

$$\left| x (t; t _ {0}, x _ {0}) \right| < \varepsilon \mathrm{e} ^ {- \alpha (t - t _ {0})} \leqslant \varepsilon , \quad \forall t \geqslant t _ {0}.$$

取 $\delta_{1} = 1$ ，并设 $\eta > 0$ 。如果 $\eta \geqslant M$ ，则取 $T(\eta) = 1$ ；如果 $\eta < M$ ，则取 $T(\eta) = -\frac{1}{\alpha} \ln \left(\frac{\eta}{M}\right) > 0$ 。于是当 $|x_{0}| < \delta_{1}$ 时显然有

$$\left| x (t; t _ {0}, x _ {0}) \right| < \eta , \quad \forall t \geqslant t _ {0} + T (\eta).$$

这就证明了充分性.

必要性. 设方程 (2.4.11) 的平衡解 $x = 0$ 是一致渐近稳定的. 依定义, 对于任意给定 $\eta > 0$ , 必存在 $T(\eta) > 0$ 和 $\delta_1 > 0$ , 使得对任意固定的 $t_0 \geqslant 0$ , 只要 $|x(t_0)| < \delta_1$ , 就有

$$\left| x (t; t _ {0}, x (t _ {0})) \right| < \eta , \quad \forall t \geqslant t _ {0} + T (\eta).$$

由 $x(t; t_0, x(t_0)) = \Phi(t; t_0)x(t_0)$ 知， $\forall t \geqslant 0$ 。可选取 $x, |\bar{x}| = \frac{1}{2}\delta_1$ ，使得

$$\boldsymbol {x} (t + T (\eta); t, \bar {\boldsymbol {x}}) = \Phi (t + T (\eta); t) \bar {\boldsymbol {x}}.$$

因为 $|x(t)| = |\overline{x}| = \frac{1}{2}\delta_1 < \delta_1$ ，所以

$$\left| x (t + T (\eta); t, \bar {x}) \right| < \eta .$$

于是

$$\| \Phi (t + T (\eta); t) \| = \sup \left\{\frac {| x (t + T (\eta) ; t , \bar {x}) |}{| \bar {x} |} \Bigg | | \bar {x} | \leqslant \frac {\delta_ {1}}{2} \right\} \leqslant 2 \delta_ {1} ^ {- 1} \eta , \quad \forall t \geqslant 0. \tag {2.4.17}$$

另外，因为矩阵 $\Phi(t; t_0)$ 的每一列都是方程 (2.4.11) 的解，根据一致稳定性的定义可知，存在 $M > 0$ ，使得

$$\max _ {\tau \in [ t, t + T (\eta) ]} \| \Phi (\tau ; t) \| < M, \quad \forall t \geqslant 0.$$

取 $\eta = \frac{\delta_1}{4}$ . 令 $t_1 = T(\eta)$ , $m = \left[\frac{t - t_0}{t_1}\right]$ , 这里记号 $[q]$ 表示数 $q$ 的整数部分. 显然 $m \leqslant \frac{t - t_0}{t_1} \leqslant m + 1$ . 根据状态转移矩阵的性质知,

$$\Phi (t; t _ {0}) = \Phi (t; t _ {0} + m t _ {1}) \Phi (t _ {0} + m t _ {1}; t _ {0} + (m - 1) t _ {1}) \dots \Phi (t _ {0} + t _ {1}; t _ {0}).$$

由此联合式 (2.4.17) 得到

$$\left\| \Phi (t; t _ {0}) \right\| \leqslant \left\| \Phi (t; t _ {0} + m t _ {1}) \right\| \left\| \Phi \left(t _ {0} + m t _ {1}; t _ {0} + (m - 1) t _ {1}\right) \right\| \dots \left\| \Phi \left(t _ {0} + t _ {1}; t _ {0}\right) \right\|\leqslant M \frac {1}{2 ^ {\pi n}}. \tag {2.4.18}$$

由于

$$2 ^ {- m} = \mathrm{e} ^ {- m \ln 2} \leqslant \mathrm{e} ^ {- (\ln 2) t - t _ {0} / t _ {1}},$$

因此
