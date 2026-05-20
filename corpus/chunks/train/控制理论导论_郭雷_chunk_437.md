设 $X \in \mathbb{R}^{n \times n}$ 是对称阵，且 $F(X)$ 为 $X$ 的线性或者仿射矩阵函数。注意对称阵 $X$ 有 $m = n(n + 1)/2$ 个独立元 $x_i (i = 1, 2, \cdots, m)$ ，因此若取对应的基 $X_1, \cdots, X_m$ ，则 $X$ 可以表示为 $X_i$ 的线性组合，即

$$X = \sum_ {i = 1} ^ {m} x _ {i} X _ {i}.$$

与此对应， $F(X)$ 也可以表示为

$$F (X) = M (x) = F _ {0} + x _ {1} F _ {1} + x _ {2} F _ {2} + \dots + x _ {m} F _ {m},$$

其中 $x = [x_{1} x_{2} \cdots x_{m}]^{T} \in R^{m}, F_{0}, F_{1}, \cdots, F_{m}$ 均为与 $F(X)$ 具有相同阶数的定常矩阵.

引理6.3.1 如下定义的集合 $\pmb{M}$ 是凸集：

$$\mathcal {M} = \{x \in \mathbb {R} ^ {m} \mid M (x) > 0 \}. \tag {6.3.9}$$

证明 对于任意给定的 $x \in \mathcal{M}$ 和 $y \in \mathcal{M}$ , 有 $M(x) > 0, M(y) > 0$ . 所以

$$
\begin{array}{l} M (\alpha x + (1 - \alpha) y) = F _ {0} + \sum_ {i = 1} ^ {m} \left(\alpha x _ {i} + (1 - \alpha) y _ {i}\right) F _ {i} \\ = \alpha \left(F _ {0} + \sum_ {i = 1} ^ {m} x _ {i} F _ {i}\right) + (1 - \alpha) \left(F _ {0} + \sum_ {i = 1} ^ {m} y _ {i} F _ {i}\right) \\ = \alpha M (x) + (1 - \alpha) M (y) > 0, \forall \alpha \in [ 0, 1 ]. \\ \end{array}
$$

这表明 $\alpha x + (1 - \alpha)y\in \mathcal{M}$

与前一节讨论类似，存在正定阵 $X$ 满足Riccati不等式(6.3.4)的充分必要条件是存在正定阵 $Y > 0$ 使得

$$
\left[ \begin{array}{c c} A Y + Y A ^ {\mathrm{T}} + B _ {1} B _ {1} ^ {\mathrm{T}} - B _ {2} B _ {2} ^ {\mathrm{T}} & Y C _ {1} ^ {\mathrm{T}} \\ C _ {1} Y & - I \end{array} \right] <   0, \tag {6.3.10}
$$

或者等价地存在对称阵 $Y$ 使得

$$
F (Y) = \left[ \begin{array}{c c c} A Y + Y A ^ {\mathrm{T}} + B _ {1} B _ {1} ^ {\mathrm{T}} - B _ {2} B _ {2} ^ {\mathrm{T}} & Y C _ {1} ^ {\mathrm{T}} & 0 \\ C _ {1} Y & - I & 0 \\ 0 & 0 & - Y \end{array} \right] <   0. \tag {6.3.11}
$$

因此，若令

$$
F _ {0} = - \left[ \begin{array}{c c c} B _ {1} B _ {1} ^ {\mathrm{T}} - B _ {2} B _ {2} ^ {\mathrm{T}} & 0 & 0 \\ 0 & - I & 0 \\ 0 & 0 & 0 \end{array} \right],

F _ {i} = - \left[ \begin{array}{c c c} A Y _ {i} + Y _ {i} A ^ {\mathrm{T}} & Y _ {i} C _ {1} ^ {\mathrm{T}} & 0 \\ C _ {1} Y _ {i} & 0 & 0 \\ 0 & 0 & - Y _ {i} \end{array} \right],
$$

则

$$M (y) = - F (Y) = F _ {0} + \sum_ {i = 1} ^ {m} y _ {i} F _ {i}, \tag {6.3.12}$$

其中 $y = [y_{1} y_{2} \cdots y_{m}]^{T}$ ，且 $Y_{i}$ 为对称阵 Y 的基。所以根据引理 6.3.3，集合

$$\mathcal {M} = \{y \in R ^ {m} \mid M (y) > 0 \} = \{y \mid F (Y) < 0 \}$$

是凸集. 由于 $Y$ 满足不等式 (6.3.10) 当且仅当正定阵 $X = Y^{-1}$ 满足 Riccati 不等式 (6.3.4), 所以满足 Riccati 不等式 (6.3.4) 的正定阵 $X$ 的集合也是凸集.

由上述讨论可知，根据定理6.3.1求解 $H_{\infty}$ 设计问题等价于在凸集 $\pmb{M}$ 中寻找满足 $M(y) > 0$ 的元 $y$ . 因此我们有如下推论：

推论6.3.1 设定理6.3.1的假设成立．广义受控对象(6.3.1)所对应的 $H_{\infty}$ 设计问题有静态状态反馈解的充分必要条件是如下定义的凸可行问题有解 $\pmb{y}$

$$\text { 求 } y \in \mathbb {R} ^ {m} \text { 使得 } M (y) > 0. \tag {6.3.13}$$

若 $y = [y_{1} y_{2} \cdots y_{m}]^{T}$ 是上述凸可行问题的一个解，那么 $H_{\infty}$ 静态反馈控制器为
