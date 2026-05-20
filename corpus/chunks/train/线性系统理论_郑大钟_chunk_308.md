= \left[ \begin{array}{c c} \frac {s}{(s + 1) ^ {2} (s + 2) ^ {2}} & 0 \\ 0 & \frac {s ^ {2}}{(s + 2) ^ {2}} \end{array} \right]
$$

传递函数矩阵在无穷远处的评价值，对任一标量传递函数 $g(s) = n(s) / d(s)$ ，其在无穷远处的评价值定义为：

$g(s)$ 在 $\infty$ 处的评价值 = $v_{\infty}(g)$ $\triangleq$ “分母多项式 $d(s)$ 的次数”

$$- “ \text { 分子多项式 } n (s) \text { 的次数 } ” \tag {8.64}$$

将上述定义加以推广,可得到传递函数矩阵 $G(s)$ 在 $\infty$ 处的评价值定义为:

$G(s)$ 在 $\infty$ 处的第 $i$ 阶评价值 $\pmb{v}_{\infty}^{(i)}(G)\triangleq \min \{\pmb{v}_{\infty}(|G|^{i})\}$

$$i = 1, 2, \dots , r \tag {8.65}$$

其中， $|G|^{i}$ 为 $G(s)$ 的一个 $i \times i$ 子式， $r = \operatorname{rank} G(s)$ 。

对于 $G(s)$ 在无穷远处的评价值 $v_{\infty}^{(i)}(G)$ ，可导出如下的一个属性。

结论 给定传递函数矩阵 $G(s)$ ， $\operatorname{rank} G(s) = r$ ，表 $\{\sigma_{1}(\infty), \cdots, \sigma_{r}(\infty)\}$ 为 $G(s)$ 在 $\infty$ 处的结构指数， $\{\nu_{\infty}^{(1)}(G), \cdots, \nu_{\infty}^{(r)}(G)\}$ 为 $G(s)$ 在 $\infty$ 处的各阶评价值，则两者之间成立如下的关系式：

$$
\left\{ \begin{array}{l} \sigma_ {1} (\infty) = v _ {\infty} ^ {(1)} (G) \\ \sigma_ {2} (\infty) = v _ {\infty} ^ {(2)} (G) - v _ {\infty} ^ {(1)} (G) \\ \dots \dots \\ \sigma_ {r} (\infty) = v _ {\infty} ^ {(r)} (G) - v _ {\infty} ^ {(r - 1)} (G) \end{array} \right. \tag {8.66}
$$

上述结论的用处之一，就是通过计算 $G(s)$ 在 $\infty$ 处的各阶评价值 $v_{\infty}^{(i)}(G)$ (i = 1, 2, $\cdots$ , r)，来直接定出 $G(s)$ 在 $\infty$ 处的史密斯-麦克米伦形

$$\widetilde {M} _ {0} (\lambda) = \mathrm{diag} \{\lambda^ {\sigma_ {1} (\infty)}, \dots , \lambda^ {\sigma_ {r} (\infty)} \} \tag {8.67}$$

其中 $\lambda = 1 / s_{0}$

例 给定传递函数矩阵 $G(s)$ 如下:

$$
G (s) = \left[ \begin{array}{c c c} \frac {s}{s - 1} & & \\ & \frac {1}{s - 1} & \\ & & (s - 1) ^ {2} \end{array} \right]
$$

按定义,先求出 $G(s)$ 在 $\infty$ 处的各阶评价值:

$$
\begin{array}{l} \nu_ {\infty} ^ {(1)} (G) = \min \{0, 1, - 2 \} = - 2 \\ \nu_ {o} ^ {(2)} (G) = \min \{1, - 1, - 2 \} = - 2 \\ \nu_ {\infty} ^ {(3)} (G) = - 1 \\ \end{array}
$$

再根据(8.66)，来求出 $G(s)$ 在 $\infty$ 处的结构指数：

$\sigma_{1}(\infty) = \nu_{\infty}^{(1)}(G) = -2, \quad \sigma_{2}(\infty) = \nu_{\infty}^{(2)}(G) - \nu_{\infty}^{(1)}(G) = 0, \quad \sigma_{3}(\infty) = \nu_{\infty}^{(3)}(G) - \nu_{\infty}^{(2)}(G) = 1$ 。从而，即可定出 $G(s)$ 在 $\infty$ 处的史密斯-麦克米伦形为

$$\widetilde {M} _ {\bullet} (\lambda) = \operatorname{diag} \left(\frac {1}{\lambda^ {2}}, 1, \lambda\right)$$

传递函数矩阵的史密斯-麦克米伦形的完整表达式 当同时考虑传递函数矩阵 $G(s)$ 的有限极点零点和无穷远处的极点零点时，其史密斯-麦克米伦形就可由两种情况下的相应结果 $M(s)$ 和 $\widetilde{M}_0(\lambda)$ 的合成来表达，即

$$M (s, \lambda) = M (s) \widetilde {M} _ {0} (\lambda) \tag {8.68}$$
