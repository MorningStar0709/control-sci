$$
d (s) = (s + 1) ^ {2} (s + 2) ^ {2}, N (s) = \left[ \begin{array}{c c} s & s (s + 1) ^ {2} \\ - s (s + 1) ^ {2} & - s (s + 1) ^ {2} \end{array} \right]
$$

再定出 $N(s)$ 的史密斯形 $\Lambda(s)$ ，为此取单模阵为

$$
U (s) = \left[ \begin{array}{c c} 1 & 0 \\ (s + 1) ^ {2} & 1 \end{array} \right], \quad V (s) = \left[ \begin{array}{c c} 1 & - (s + 1) ^ {2} \\ 0 & 1 \end{array} \right]
$$

则就有

$$
\Lambda (s) = U (s) N (s) V (s) = \left[ \begin{array}{c c} 1 & 0 \\ (s + 1) ^ {2} & 1 \end{array} \right] \left[ \begin{array}{c c} s & s (s + 1) ^ {2} \\ - s (s + 1) ^ {2} & - s (s + 1) ^ {2} \end{array} \right]

\times \left[ \begin{array}{c c} 1 & - (s + 1) ^ {2} \\ 0 & 1 \end{array} \right] = \left[ \begin{array}{c c} s & 0 \\ 0 & s ^ {2} (s + 1) ^ {2} (s + 2) \end{array} \right]
$$

从而，进一步，可得到

$$
M (s) = \frac {\Lambda (s)}{d (s)} = \left[ \begin{array}{c c} \frac {s}{(s + 1) ^ {2} (s + 2) ^ {2}} & 0 \\ 0 & \frac {s ^ {2} (s + 1) ^ {2} (s + 2)}{(s + 1) ^ {2} (s + 2) ^ {2}} \end{array} \right]
$$

而在消去元有理分式中的公因子后，就得到了给定 $G(s)$ 的史密斯-麦克米伦形为

$$
M (s) = U (s) G (s) V (s) = \left[ \begin{array}{c c} \frac {s}{(s + 1) ^ {2} (s + 2) ^ {2}} & 0 \\ 0 & \frac {s ^ {2}}{(s + 2)} \end{array} \right]
$$

几点讨论 下面，我们就传递函数矩阵 $G(s)$ 的史密斯-麦克米伦形 $M(s)$ 进行讨论，来指出它的一些重要的属性。

(1) 对于给定的传递函数矩阵 $G(s)$ , 其史密斯-麦克米伦形 $M(s)$ 是唯一的。但是, 化 $G(s)$ 为 $M(s)$ 的单模阵对 $\{U(s), V(s)\}$ 则不是唯一的。

(2) 即使给定传递函数矩阵 $G(s)$ 是严格真的, 其史密斯-麦克米伦形 $M(s)$ 也可能不是真的。也即, 单模变换阵对 $\{U(s), V(s)\}$ 的引入, 会可能附加引入乘子 $s^k$ , $k = 1, 2, \cdots$ 。前面所讨论的一个例子, 就是这一属性的一个例证。

(3) 如果给定的传递函数矩阵 $G(s)$ 为方的且非奇异, 则必成立

$$\det G (s) = \alpha \Pi \frac {\varepsilon_ {i} (s)}{\psi_ {i} (s)} \tag {7.103}$$

其中 $\alpha$ 为非零常数。

这是因为，由对 $M(s)$ 取行列式可导出

$$\det G (s) = \frac {1}{\det U (s) \det V (s)} \Pi \frac {\varepsilon_ {i} (s)}{\psi_ {i} (s)} \tag {7.104}$$

但已知 $U(s)$ 和 $V(s)$ 为单模阵，故 $\operatorname{det} U(s)$ 和 $\operatorname{det} V(s)$ 均为独立于 $s$ 的非零常数。因此，表

$$\alpha = 1 / \det U (s) \det V (s) \tag {7.105}$$

则由(7.104)和(7.105)即可导出(7.103)。

(4) 令 $M(s) = U(s)G(s)V(s)$ 为史密斯-麦克米伦形， $U(s)$ 和 $V(s)$ 为单模阵，再表

$$M (s) = \Sigma (s) \Psi_ {r} ^ {- 1} (s) \tag {7.106}$$

其中

$$
\Sigma (s) = \left[ \begin{array}{c c c} \varepsilon_ {1} (s) & & \\ & \ddots & 0 \\ & \varepsilon_ {r} (s) & \\ - & 0 & 0 \end{array} \right], \quad \Psi_ {r} (s) = \left[ \begin{array}{c c c} \psi_ {1} (s) & & \\ & \ddots & 0 \\ & \psi_ {r} (s) & \\ - & 0 & I \end{array} \right] \tag {7.107}
$$

则当取

$$N (s) = U ^ {- 1} (s) \Sigma (s), D (s) = V (s) \Psi_ {r} (s) \tag {7.108}$$

时， $N(s)D^{-1}(s)$ 为传递函数矩阵 $G(s)$ 的一个不可简约的 MFD。
