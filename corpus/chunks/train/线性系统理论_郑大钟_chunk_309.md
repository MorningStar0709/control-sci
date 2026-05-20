这是一个二元有理分式矩阵，且具有分离性，其中以 $s$ 为变量的部分用以反映 $G(s)$ 的有限极点和零点，而以 $\lambda = 1 / s$ 为变量的部分则反映了 $G(s)$ 的无穷远处的极点和零点。这样做，避免了可能引起的史密斯-麦克米伦形在 $s = 0$ 和 $s = \infty$ 时的行为的混淆。

例 给定传递函数矩阵 $G(s)$ 如下:

$$
G (s) = \left[ \begin{array}{c c c} \frac {s}{s - 1} & & \\ & \frac {1}{s - 1} & \\ & & (s - 1) ^ {2} \end{array} \right]
$$

先定出 $G(s)$ 在有限处的评价值：

$$v _ {0} ^ {(1)} (G) = 0, \quad v _ {0} ^ {(2)} (G) = 0, \quad v _ {0} ^ {(3)} (G) = 1v _ {1} ^ {(1)} (G) = - 1, v _ {1} ^ {(2)} (G) = - 2, v _ {1} ^ {(3)} (G) = 0$$

因此， $G(s)$ 的结构指数就可由此定出为：

$$\sigma_ {1} (0) = 0, \quad \sigma_ {2} (0) = 0, \quad \sigma_ {3} (0) = 1\sigma_ {1} (1) = - 1, \quad \sigma_ {2} (1) = - 1, \quad \sigma_ {3} (1) = 2$$

从而， $G(s)$ 在有限极点和零点处的史密斯-麦克米伦形为：

$$
M (s) = \left[ \begin{array}{l l l} 1 & & \\ & 1 & \\ & & s \end{array} \right] \left[ \begin{array}{c c c} (s - 1) ^ {- 1} & & \\ & (s - 1) ^ {- 1} & \\ & & (s - 1) ^ {2} \end{array} \right]
$$

而 $G(s)$ 在无穷远处极点和零点上的史密斯-麦克米伦形已在前面求出，即为：

$$
\widetilde {M} _ {0} (\lambda) = \left[ \begin{array}{c c c} \left(\frac {1}{\lambda}\right) ^ {2} & & \\ & 1 & \\ & & \left(\frac {1}{\lambda}\right) ^ {- 1} \end{array} \right]
$$

于是，给定 $G(s)$ 的史密斯-麦克米伦形的完整表达式就为

$$
M (s, \lambda) = \left[ \begin{array}{l l l} 1 & & \\ & 1 & \\ & & s \end{array} \right] \left[ \begin{array}{c c c} (s - 1) ^ {- 1} & & \\ & (s - 1) ^ {- 1} & \\ & & (s - 1) ^ {2} \end{array} \right]

\times \left[ \begin{array}{c c c} \left(\frac {1}{\lambda}\right) ^ {2} & & \\ & 1 & \\ & & \left(\frac {1}{\lambda}\right) ^ {- 1} \end{array} \right]
$$
