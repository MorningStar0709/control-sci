所以 $\{x_{k}(t)\}$ 是 $R^n$ 中的一个Cauchy序列。 $R^n$ 对任意 $p$ 范数都是完备的，因为收敛意味着分量收敛并且 $R$ 是完备的，因此序列收敛到一个实向量 $x(t): x_{k}(t) \to x(t)$ ，这证明了是点态(pointwise)收敛。下面，我们将证明在 $t \in [a, b]$ 时，收敛是一致收敛。给定 $\varepsilon > 0$ ，存在一个 $N$ ，使得当 $k, m > N$ 时， $\| x_{k} - x_{m} \|_{C} < \varepsilon / 2$ 。那么，对于 $k > N$ 有

$$
\begin{array}{l} \left\| x _ {k} (t) - x (t) \right\| \leqslant \left\| x _ {k} (t) - x _ {m} (t) \right\| + \left\| x _ {m} (t) - x (t) \right\| \\ \leqslant \left\| x _ {k} - x _ {m} \right\| _ {C} + \left\| x _ {m} (t) - x (t) \right\| \\ \end{array}
$$

选择充分大的 $m$ （可能取决于 $t$ ），上式右边的每一项都小于 $\varepsilon / 2$ ，因此，对于 $k > N$ ，有 $\| x_{k}(t) - x(t) \| < \varepsilon$ ，故 $\{x_{k}\}$ 在 $t \in [a, b]$ 上一致收敛到 $x$ 。为了完成证明，我们还要证明 $x(t)$ 是连续的，并且 $\{x_{k}\}$ 依 $C[a, b]$ 范数收敛到 $x$ 。为了证明连续性，假设

$$
\begin{array}{l} \left\| x (t + \delta) - x (t) \right\| \leqslant \left\| x (t + \delta) - x _ {k} (t + \delta) \right\| \\ + \left\| x _ {k} (t + \delta) - x _ {k} (t) \right\| + \left\| x _ {k} (t) - x (t) \right\| \\ \end{array}
$$

因为 $\{x_{k}\}$ 一致收敛到 $x$ ，给定任意 $\varepsilon >0$ ，可选择足够大的 $k$ ，使上式右边的第一项和第三项小于 $\varepsilon /3$ ，由于 $x_{k}(t)$ 是连续的，我们可选择足够小的 $\delta$ ，使第二项小于 $\varepsilon /3$ ，故 $x(t)$ 是连续的。 $x_{k}$ 依 $\| \cdot \| _C$ 收敛到 $x$ 是一致收敛的直接结果。

定理 B.1 (压缩映射) 设 S 是 Banach 空间 X 的闭子集, T 是 S 到 S 的映射, 设

$$\| T (x) - T (y) \| \leqslant \rho \| x - y \|, \forall x, y \in S, 0 \leqslant \rho < 1$$

那么

- 存在唯一的向量 $x^{*} \in S$ ，满足 $x^{*} = T(x^{*})$ 。  
- $x^{*}$ 可通过逐次逼近方法得到，逼近过程可从 $S$ 中任意初始向量开始。

证明:选择任意一个 $x_{1} \in S$ ，并且用 $x_{k+1} = T(x_{k})$ 定义序列 $\{x_{k}\}$ ，由于 T 是 S 到 S 的映射，因此 $x_{k} \in S$ ，其中 $k \geqslant 1$ 。证明的第一步是证明 $\{x_{k}\}$ 为 Cauchy 序列，我们有

$$
\begin{array}{l} \left\| x _ {k + 1} - x _ {k} \right\| = \left\| T \left(x _ {k}\right) - T \left(x _ {k - 1}\right) \right\| \\ \leqslant \rho \| x _ {k} - x _ {k - 1} \| \leqslant \rho^ {2} \| x _ {k - 1} - x _ {k - 2} \| \leqslant \dots \leqslant \rho^ {k - 1} \| x _ {2} - x _ {1} \| \\ \end{array}
\left\| x _ {k + r} - x _ {k} \right\| \leqslant \left\| x _ {k + r} - x _ {k + r - 1} \right\| + \left\| x _ {k + r - 1} - x _ {k + r - 2} \right\| + \dots + \left\| x _ {k + 1} - x _ {k} \right\|\leqslant \left[ \rho^ {k + r - 2} + \rho^ {k + r - 3} + \dots + \rho^ {k - 1} \right] \| x _ {2} - x _ {1} \|\leqslant \rho^ {k - 1} \sum_ {i = 0} ^ {\infty} \rho^ {i} \| x _ {2} - x _ {1} \| = \frac {\rho^ {k - 1}}{1 - \rho} \| x _ {2} - x _ {1} \|
$$

可得
