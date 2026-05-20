3.21 对于任何 $x \in R^n - \{0\}$ 和 $p \in [1, \infty)$ ，由

$$y _ {i} = \frac {x _ {i} ^ {p - 1}}{\| x \| _ {p} ^ {p - 1}} \operatorname{sign} (x _ {i} ^ {p})$$

定义 $y \in R^n$ 。证明 $y^{\mathrm{T}}x = \| x\|_{p}$ 和 $\| y\|_{q} = 1$ ，其中 $q \in (1, \infty]$ 由 $1/p + 1/q = 1$ 确定。当 $p = \infty$ 时，求一个向量 $y$ ，满足 $y^{\mathrm{T}}x = \| x\|_{\infty}$ 和 $\| y\|_{1} = 1$ 。

3.22 证明引理 3.3。  
3.23 设 $f(x)$ 是把凸定义域 $D \subset R^n$ 映射到 $R^n$ 上的一个连续可微函数。设 $D$ 包含原点 $x = 0$ 和 $f(0) = 0$ ，证明

$$f (x) = \int_ {0} ^ {1} \frac {\partial f}{\partial x} (\sigma x) d \sigma x, \quad \forall x \in D$$

提示: 当 $0 \leqslant \sigma \leqslant 1$ 时, 设定 $g(\sigma) = f(\sigma x)$ , 并运用 $g(1) - g(0) = \int_{0}^{1} g'(\sigma) d\sigma$ 。

3.24 设 $V: R \times R^n \to R$ 连续可微。假设对于所有 $t \geqslant 0$ ，有 $V(t, 0) = 0$ ，且

$$V (t, x) \geqslant c _ {1} \| x \| ^ {2}; \quad \left\| \frac {\partial V}{\partial x} (t, x) \right\| \leqslant c _ {4} \| x \|, \forall (t, x) \in [ 0, \infty) \times D$$

其中 $c_{1}$ 和 $c_{4}$ 是正常数, 且 $D \subset R^{n}$ 是包含原点 x = 0 的凸定义域。

(a) 证明对于所有 $x \in D$ , 有 $V(t, x) \leqslant \frac{1}{2} c_4 \| x \|^2$ 。

提示:运用表达式 $V(t,x)=\int_{0}^{1}\frac{\partial V}{\partial X}(t,\sigma x)d\sigma x$ 。

(b) 证明常数 $c_{1}$ 和 $c_{4}$ 必须满足 $2c_{1} \leqslant c_{4}$ 。  
(c) 证明 $W(t, x) = \sqrt{V(t, x)}$ 满足利普希茨条件

$$| W (t, x _ {2}) - W (t, x _ {1}) | \leqslant \frac {c _ {4}}{2 \sqrt {c _ {1}}} \| x _ {2} - x _ {1} \|, \forall t \geqslant 0, \forall x _ {1}, x _ {2} \in D$$

3.25 设 $f(t, x)$ 在 $[t_0, t_1] \times D$ 上某一定义域 $D \subset R^n$ 内，对于 $t$ 分段连续，对于 $x$ 是局部利普希茨的， $W$ 是 $D$ 的紧子集， $x(t)$ 是 $\dot{x} = f(t, x)$ 始于 $x(t_0) = x_0 \in W$ 的解。假设 $x(t)$ 有定义，且对于所有 $t \in [t_0, T)$ ，有 $x(t) \in W, T < t_1$ 。

(a) 证明 $x(t)$ 在 $[t_0, T)$ 上一致连续。  
(b) 证明 $x(T)$ 有定义且属于 $W, x(t)$ 是 $[t_0, T]$ 上的一个解。  
(c) 证明存在 $\delta > 0$ ，使解可扩展到 $[t_{0}, T + \delta]$ 。

3.26 设 $f(t, x)$ 在 $[t_0, t_1] \times D$ 上某一定义域 $D \subset R^n$ 内，对于 $t$ 分段连续，对于 $x$ 是局部利普希茨的， $y(t)$ 是方程(3.1)在最大开区间 $[t_0, T) \subset [t_0, t_1]$ 上的解， $T < \infty$ 。设 $W$ 是 $D$ 的紧子集，证明存在 $t \in [t_0, T)$ ，使 $y(t) \notin W$ 。

提示:运用前面的习题。

3.27 （见文献[43]）设 $x_{1}:R\to R^{n}$ 和 $x_{2}:R\to R^{n}$ 是可微函数，当 $a\leqslant t\leqslant b$ 时

$$\| x _ {1} (a) - x _ {2} (a) \| \leqslant \gamma , \quad \| \dot {x} _ {i} (t) - f (t, x _ {i} (t)) \| \leqslant \mu_ {i}, \quad i = 1, 2$$

成立。如果 $f$ 满足式(3.2)的利普希茨条件，证明

$$\| x _ {1} (t) - x _ {2} (t) \| \leqslant \gamma e ^ {L (t - a)} + (\mu_ {1} + \mu_ {2}) \left[ \frac {e ^ {L (t - a)} - 1}{L} \right], \quad a \leqslant t \leqslant b$$

3.28 证明: 在定理 3.5 的假设下, 方程(3.1)的解连续取决于初始时刻 $t_{0}$ 。
