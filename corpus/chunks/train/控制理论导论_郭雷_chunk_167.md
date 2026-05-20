证明 假定 $W(x)$ 为在闭球 $|x| \leqslant h$ 内正定的函数，且 $\dot{W}(x)|_{(2.4.19)}$ 为非正定的。对于任意给定的正数 $\varepsilon$ ，记 $v_0 = \min_{\varepsilon \leqslant |x| \leqslant h} W(x)$ ，则 $v_0 > 0$ 。

由于 $V(0) = 0$ ，根据 $W(x)$ 的连续性，对于这个 $v_{0}$ ，必定存在 $\delta > 0$ ，使当 $|x| < \delta$ 时，成立

$$0 \leqslant W (x) < v _ {0}.$$

在开球 $|x| < \delta$ 内任取 $x_0$ , 根据假设, 方程 (2.4.19) 的解 $x(t; x_0)$ 在 $[0, +\infty)$ 上有定义. 今证 $|x(t; x_0)| < \varepsilon$ , $\forall t \in [0, +\infty)$ .

设若不然，则必定存在 $x_0^*, |x_0^*| < \delta$ 和 $T > 0$ ，使得

$$| x (t; x _ {0} ^ {*}) | < \varepsilon , \qquad {\text {当}} t \in [ 0, T),| x (t; x _ {0} ^ {*}) | = \varepsilon , \qquad \text {当} t = T \text {时}.$$

依定理假设，有

$$\frac {\mathrm{d}}{\mathrm{d} t} W (x (t; x _ {0} ^ {*})) \leqslant 0, \quad \forall t \in [ 0, T ].$$

所以

$$W (x (T; x _ {0} ^ {*})) \leqslant W (x (0; x _ {0} ^ {*})) = W (x _ {0} ^ {*}) < v _ {0}. \tag {2.4.21}$$

注意到 $|x(T;x_0)| = \varepsilon$ ，而 $v_{0}$ 是 $W(x)$ 在闭区域 $\varepsilon \leqslant |x|\leqslant h$ 上的最小值，可知

$$W (x (T; x _ {0} ^ {*})) \geqslant v _ {0}, \tag {2.4.22}$$

得到矛盾. 因此微分方程 (2.4.19) 的零平衡解是稳定的.

定理2.4.8 对于微分方程(2.4.19)，如果能够找到正定（负定）函数 $W(x)$ ，使得它沿方程(2.4.19)对时间的全导数 $\dot{W}(x)|_{(2.4.19)}$ 是负定(正定)的，那么式(2.4.19)的零平衡解是渐近稳定的。

证明 根据定理 2.4.7, 微分方程 (2.4.19) 的零解是稳定的。今证存在正数 $\sigma$ ，使当 $|x_0| < \sigma$ 时，方程 (2.4.19) 的解 $x(t; x_0)$ 当 $t \to +\infty$ 时趋于零向量。事实上，依假设 $W(x)$ 和 $-\dot{W}(x)|_{(2.4.19)}$ 为区域 $|x| \leqslant h$ 中的正定函数，其中 $h$ 是某个正数。根据定理 2.4.7, 对于这个 $h$ ，存在 $\sigma > 0$ 。使当 $|x_0| < \sigma$ 时有

$$| x (t; x _ {0}) | < h, \quad \forall t \geqslant 0.$$

由于

$$\dot {W} (x (t; x _ {0})) \mid_ {(2. 4. 1 9)} \leqslant 0, \quad \forall t \in [ 0, + \infty),$$

故 $W(x(t;x_0))$ 是 $t$ 单调不增加函数，且 $W(x(t;x_0))\geqslant 0.$ 所以当 $t\to +\infty$ 时， $W(x(t;x_0))$ 趋于确定的极限 $\alpha \geqslant 0.$

如果 $\alpha > 0$ ，那么由于 $W(x(t; x_0)) \geqslant \alpha$ ，根据正定函数性质2知，存在正数 $\alpha_1$ ，使得

$$0 < \alpha_ {1} \leqslant | x (t; x _ {0}) | < h.$$

注意到 $-\dot{W}(x)\big|_{(2.4.19)}$ 为正定的，所以依正定函数的性质3，存在正数 $v_{1}$ ，使得当 $0 < \alpha_{1} \leqslant |x(t;x_{0})| < h$ 时，成立不等式

$$- \dot {W} (x (t; x _ {0})) \mid_ {(2. 4. 1 9)} \geqslant v _ {1}.$$

从0到 $t$ 积分上式，得

$$0 \leqslant W (x (t; x _ {0})) \leqslant W (x _ {0}) - v _ {1} t. \tag {2.4.23}$$

当 $t \to +\infty$ 时，不等式 (2.4.23) 右端趋于 $-\infty$ ，这与 $W(x)$ 的正定性矛盾。所以 $\alpha = 0$ ，这样就证明了

$$\lim _ {t \rightarrow + \infty} W (x (t; x _ {0})) = 0. \tag {2.4.24}$$

如果当 $t \to +\infty$ 时， $x(t; x_0)$ 不趋于零向量，则必存在正数 $\varepsilon_0$ 和一无穷递增时间序列 $\{t_k\}$ ， $\lim_{k \to +\infty} t_k = +\infty$ ，使得
