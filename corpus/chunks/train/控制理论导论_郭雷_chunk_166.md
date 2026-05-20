例2.4.3 正定，非负定，变号函数的例子：

$$W (x _ {1}, x _ {2}, x _ {3}) = a _ {1} x _ {1} ^ {2} + a _ {2} x _ {2} ^ {2} + a _ {3} x _ {3} ^ {2}, a _ {i} > 0, i = 1, 2, 3. \text {为正定函数，}W (x _ {1}, x _ {2}, x _ {3}) = a _ {2} x _ {2} ^ {2} + a _ {3} x _ {3} ^ {2}, a _ {i} > 0, i = 2, 3, \text {为半正定函数},W (x _ {1}, x _ {2}, x _ {3}) = 2 x _ {1} ^ {2} - 3 x _ {2} ^ {2} - 5 x _ {3} ^ {2}, \text {为变号函数,}V (t, x _ {1}, x _ {2}) = (1 + \mathrm{e} ^ {- 2 t}) (x _ {1} ^ {2} + x _ {2} ^ {2} + \cos (x _ {1} + x _ {2})). \text {为正定函数，}V (t, x _ {1}, x _ {2}) = \mathbf {e} ^ {t} (x _ {1} ^ {2} + x _ {2} ^ {2}), \text {为半正定函数},V (t, x _ {1}, x _ {2}) = (\sin t) x _ {1} ^ {2} + (\cos t) x _ {2} ^ {2}, \text {为变号函数，}$$

$W(x_{1},x_{2}) = \frac{1}{2} x_{2}^{2} + k(1 - \cos x_{1}), k > 0$ : 在 $0 < x_{1} < 2\pi$ 和 $0 \leqslant x_{1} \leqslant 2\pi$ 上分别为正定函数和半正定函数.

正定函数有下列几个显见的性质：

性质1. 设 $W(x)$ 在闭球 $|x| \leqslant h$ 上是正定函数， $c$ 为充分小的正数，那么由关系式

$$W (x) = c \tag {2.4.20}$$

确定的一个围绕 $x = 0$ 的封闭曲面当 $c \to 0$ 时，收缩到原点.

性质2. 如果函数 $W(x)$ 在闭球 $|x| \leqslant h$ 上是连续的，且 $W(0) = 0$ ，则对于任意正数 $l_1 > 0$ ，存在 $\alpha_1 > 0$ ，只要点 $x$ 满足 $W(x) \geqslant l_1$ ，就有 $|x| \geqslant \alpha_1$ .

性质3. 如果 $W(x)$ 是在闭球 $|x| \leqslant h$ 中的正定函数，那么对于任意正数 $\varepsilon < h$ 必定存在正数 $\delta$ ，使得当 $\varepsilon \leqslant |x| \leqslant h$ 时，成立

$$W (x) \geqslant \delta .$$

定义 2.4.12 $^{[10]}$ (1) 设 $\varphi:[0,\bar{r}]\to R$ 为连续函数。如果 $\varphi(r)$ 是严格单调上升的，且 $\varphi(0)=0$ ，则称 $\varphi$ 属于 K 类函数（楔函数），简称 $\varphi(r)$ 为 K 函数，记为 $\varphi\in K$ ;

(2) 如果 $\varphi: \mathbb{R}_{+} \longrightarrow \mathbb{R}_{+}$ , 且 $\varphi \in K$ , $\lim_{r \to +\infty} \varphi(r) = \infty$ , 则称 $\varphi$ 属于 $KR$ 类函数, 记为 $\varphi \in KR$ (或 $\varphi \in K_{\infty}$ ), 这里 $\mathbb{R}_{+}$ 表示非负实数集.

命题2.4.3 (1) 对任一定义在 $|x| \leqslant \bar{r}$ 上的连续正定函数 $V(x)$ , 必存在两个 $K$ 类函数 $\varphi_1, \varphi_2$ , 满足

$$\varphi_ {1} (\| x \|) \leqslant V (x) \leqslant \varphi_ {2} (\| x \|), \quad \forall | x | \leqslant \bar {r};$$

(2) 对任一定义在 $\mathbb{R}^n$ 上的无穷大正定函数 $V(x)$ , 必存在两个 $KR$ 类函数 $\varphi_1, \varphi_2$ 满足

$$\varphi_ {1} (\| x \|) \leqslant V (x) \leqslant \varphi_ {2} (\| x \|), \quad \forall x \in \mathbb {R} ^ {n}.$$

下面介绍 Lyapunov 直接方法 研究微分方程 (2.4.19) 的基本结果.

任取 $x_0 \in \mathbb{R}^n, x_0 \neq 0$ , 微分方程 (2.4.19) 的以 $x(0) = x_0$ 为初值的解记为 $x(t; x_0)$ . 记 $\dot{W}(x(t; x_0))|_{(2.4.19)} = \frac{\mathrm{d}}{\mathrm{d}t} W(x(t; x_0))|_{(2.4.19)}$ .

定理2.4.7 对于微分方程(2.4.19)，如果存在一个正定（负定）函数 $W(x)$ ，使得它沿微分方程(2.4.19)对时间的全导数 $\dot{W}(x)|_{(2.4.19)}$ 是非正定（非负定）的，则方程(2.4.19)的零平衡解是稳定的。
