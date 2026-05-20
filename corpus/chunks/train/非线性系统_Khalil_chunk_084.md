引理3.1 设 $f: [a, b] \times D \to R^m$ 在某一定义域 $D \subset R^n$ 内是连续的。假设 $[\partial f / \partial x]$ 存在，且在 $[a, b] \times D$ 上连续。如果对于一个凸子集 $W \subset D$ ，存在一个常数 $L \geqslant 0$ ，使得在 $[a, b] \times W$ 内

$$\left\| \frac {\partial f}{\partial x} (t, x) \right\| \leqslant L$$

那么，对于所有 $t \in [a, b]$ ， $x \in W$ 和 $y \in W$ ，有

$$\| f (t, x) - f (t, y) \| \leqslant L \| x - y \|$$

证明: 设 $\|\cdot\|_{p}$ 是对于任意 $p \in [1, \infty]$ 的底范数 (underlying norm), $q \in [1, \infty]$ 由关系式 $1/p + 1/q = 1$ 确定。固定 $t \in [a, b], x \in W, y \in W$ ，对于所有 $s \in R$ 定义 $\gamma(s) = (1 - s)x + sy$ ，使 $\gamma(s) \in D$ 。由于 $W \subset D$ 是凸子集，当 $0 \leqslant s \leqslant 1$ 时 $\gamma(s) \in W$ 。取 $z \in R^{m}$ ，使①

$$\| z \| _ {q} = 1, \quad z ^ {\mathrm{T}} [ f (t, y) - f (t, x) ] = \| f (t, y) - f (t, x) \| _ {p}$$

设 $g(s) = z^{\mathrm{T}}f(t,\gamma (s))$ 。由于 $g(s)$ 是实值函数，在开区间[0,1]内连续可微。根据均值定理，存在 $s_1\in (0,1)$ ，使

$$g (1) - g (0) = g ^ {\prime} \left(s _ {1}\right)$$

当 $s = 0, s = 1$ 时计算 $g$ , 并根据链式法则计算 $g'(s)$ , 得

$$
\begin{array}{l} z ^ {\mathrm{T}} [ f (t, y) - f (t, x) ] = z ^ {\mathrm{T}} \frac {\partial f}{\partial x} (t, \gamma (s _ {1})) (y - x) \\ \| f (t, y) - f (t, x) \| _ {p} \leqslant \| z \| _ {q} \left\| \frac {\partial f}{\partial x} (t, \gamma (s _ {1})) \right\| _ {p} \| y - x \| _ {p} \leqslant L \| y - x \| _ {p} \\ \end{array}
$$

其中用到 Hölder 不等式 $|z^{\mathrm{T}}w|\leqslant \| z\|_{q}\| w\|_{p}$

引理 3.1 说明利普希茨常数可通过计算 $\left[\frac{\partial f}{\partial x}\right]$ 求得。

函数的利普希茨性比连续性更强。显然，如果 $f(x)$ 在 $\pmb{W}$ 上是利普希茨的，那么它在 $\pmb{W}$ 上就是一致连续的（见习题3.20）。反之则不成立，从函数 $f(x) = x^{1 / 3}$ 即可看出它是连续的，但在 $x = 0$ 点不是局部利普希茨的。下一个引理将论述利普希茨性要比连续可微性弱。

引理3.2 如果在某一定义域 $D \subset R^n$ 内, $f(t, x)$ 和 $[\partial f / \partial x](t, x)$ 在 $[a, b] \times D$ 内是连续的, 那么 $f$ 在 $[a, b] \times D$ 上对于 $x$ 是局部利普希茨的。

证明:对于 $x_{0} \in D$ ，设 r 足够小，使球 $D_{0} = \{x \in R^{n} \mid \|x - x_{0}\| \leqslant r\}$ 包含在 D 内， $D_{0}$ 是紧凸集。由连续性可知， $[\partial f/\partial x]$ 在 $[a, b] \times D_{0}$ 上有界，设 $L_{0}$ 是 $\|\partial f/\partial x\|$ 在 $[a, b] \times D_{0}$ 上的界，由引理 3.1 可知，f 在 $[a, b] \times D_{0}$ 上是利普希茨的，利普希茨常数为 $L_{0}$ 。

把引理 3.1 的证明扩展到证明下面的引理,作为习题留给读者(见习题 3.22)。

引理3.3 如果 $f(t,x)$ 和 $[\partial f / \partial x](t,x)$ 在 $[a,b]\times R^n$ 上连续，那么当且仅当 $[\partial f / \partial x]$ 在 $[a,b]\times R^n$ 上一致有界时， $f$ 在 $[a,b]\times R^n$ 上对于 $x$ 是全局利普希茨的。

例3.1 函数 $f(x) = \left[ \begin{array}{c} - x_{1} + x_{1}x_{2}\\ x_{2} - x_{1}x_{2} \end{array} \right]$
