$$\frac {\partial H (k)}{\partial u (k)} = 0. 1 u (k) + 0. 1 \lambda_ {2} (k + 1) = 0\frac {\partial^ {2} H (k)}{\partial u ^ {2} (k)} = 0. 1 > 0$$

故 $u^{*}(k) = -\lambda_{2}(k + 1)$

可使 $H(k) = \min$ 。令 $k = 0$ 和 $k = 1$ ，得

$$u ^ {*} (0) = - \lambda_ {2} (1), \quad u ^ {*} (1) = - \lambda_ {2} (2)$$

将 $u^{*}(k)$ 表达式代入状态方程，可得

$$x _ {1} (k + 1) = x _ {1} (k) + 0. 1 x _ {2} (k)x _ {2} (k + 1) = x _ {2} (k) - 0. 1 \lambda_ {2} (k + 1)$$

令 $k$ 分别等于0和1，有

$$x _ {1} (1) = x _ {1} (0) + 0. 1 x _ {2} (0), \quad x _ {2} (1) = x _ {2} (0) - 0. 1 \lambda_ {2} (1)x _ {1} (2) = x _ {1} (1) + 0. 1 x _ {2} (1), \quad x _ {2} (2) = x _ {2} (1) - 0. 1 \lambda_ {2} (2)$$

由已知边界条件

$$x _ {1} (0) = 1, \quad x _ {2} (0) = 0x _ {1} (2) = 0, \quad x _ {2} (2) = 0$$

不难解出最优解

$$
u ^ {*} (0) = - 1 0 0, \quad u ^ {*} (1) = 1 0 0
\boldsymbol {x} ^ {*} (0) = \left[ \begin{array}{l} 1 \\ 0 \end{array} \right], \quad \boldsymbol {x} ^ {*} (1) = \left[ \begin{array}{c} 1 \\ - 1 0 \end{array} \right], \quad \boldsymbol {x} ^ {*} (2) = \left[ \begin{array}{l} 0 \\ 0 \end{array} \right]

\boldsymbol {\lambda} (0) = \left[ \begin{array}{l} 2 0 0 0 \\ 3 0 0 \end{array} \right], \quad \boldsymbol {\lambda} (1) = \left[ \begin{array}{l} 2 0 0 0 \\ 1 0 0 \end{array} \right], \quad \boldsymbol {\lambda} (2) = \left[ \begin{array}{l} 2 0 0 0 \\ - 1 0 0 \end{array} \right]
$$
