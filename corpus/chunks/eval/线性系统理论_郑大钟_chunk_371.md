降秩的所有 s 值。如果 $G(s)$ 为奇异，则这一论断不一定成立；即可能出现这样的情况，解耦零点并不是使(10.97)的矩阵降秩的 s 值。这一点可举如下的例子来说明。

例 给定 PMD $\{P(s), Q(s), R(s), W(s)\}$ 为

$$
P (s) = \left[ \begin{array}{c c c} s + 1 & 0 & 0 \\ 0 & s + 2 & 0 \\ 0 & 0 & s + 3 \end{array} \right], \quad Q (s) = \left[ \begin{array}{l} 0 \\ 1 \\ 1 \end{array} \right]

R (s) = \left[ \begin{array}{c c c} 1 & - 4 & 0 \\ 0 & 3 & 1 \end{array} \right], W (s) = 0
$$

容易判断， $G(s)$ 必是奇异的，且使

$$
[ P (s) Q (s) ] = \left[ \begin{array}{c c c c} s + 1 & 0 & 0 & 0 \\ 0 & s + 2 & 0 & 1 \\ 0 & 0 & s + 3 & 1 \end{array} \right]
$$

降秩的 $s = -1$ ，也即输入解耦零点为 $s = -1$ 。但当 $s = -1$ 时，矩阵

$$
\left[ \begin{array}{c c} P (s) & Q (s) \\ - R (s) & W (s) \end{array} \right] = \left[ \begin{array}{r r r r} 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 2 & 1 \\ - 1 & 4 & 0 & 0 \\ 0 & - 3 & - 1 & 0 \end{array} \right]
$$

并不降秩。
