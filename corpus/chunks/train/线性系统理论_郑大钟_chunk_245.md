# 6.4 秩

秩的定义 称 $q \times p$ 的多项式矩阵 $Q(s)$ 的秩为 $r, r \leqslant \min(q, p)$ ，如果至少存在一个 $r \times r$ 的子式不恒等于零，而所有等于和大于 $(r + 1) \times (r \times 1)$ 的子式均恒等零。并且，常记成为 $\operatorname{rank} Q(s) = r_0$ 。

例 给定多项式矩阵 $Q(s)$ 如下:

$$
Q (s) = \left[ \begin{array}{c c c} s + 1 & 0 & s - 2 \\ 0 & s - 2 & s + 1 \end{array} \right]
$$

易知， $Q(s)$ 包含不恒等于零的 $1\times 1$ 和 $2\times 2$ 子式。因此，据定义，有 $\operatorname {rank}Q(s) = 2_{0}$

几点推论 根据秩的定义,很容易导出如下的几点推论:

(1) 对任一非零多项式矩阵 $Q(s)$ , 令 $q$ 和 $p$ 表示其行数和列数, 则必成立

$$1 \leqslant \operatorname{rank} Q (s) \leqslant \min (q, p) \tag {6.5}$$

(2) rank $Q(s) = r$ 等价于 $Q(s)$ 有且仅有 $r$ 个列(行)向量为线性无关。

(3) $q \times p$ 多项式矩阵 $Q(s)$ 为满秩，当且仅当 $\operatorname{rank} Q(s) = \min (q, p)$ 。

(4) 对于方多项式矩阵 $Q(s)$ , $Q(s)$ 为非奇异等同于 $\operatorname{rank} Q(s) = p$ , $Q(s)$ 为奇异等同于 $\operatorname{rank} Q(s) < p$ ，其中 $p$ 为 $Q(s)$ 的维数。

(5) 对 $q \times p$ 的多项式矩阵 $Q(s)$ , 令 $q \times q$ 的 $P(s)$ 和 $p \times p$ 的 $R(s)$ 为任意非奇异多项式矩阵, 则必成立

$$\operatorname{rank} Q (s) = \operatorname{rank} P (s) Q (s) = \operatorname{rank} Q (s) R (s) \tag {6.6}$$

(6) 令 $Q(s)$ 和 $R(s)$ 分别为 $q \times p$ 和 $p \times r$ 的任意多项式矩阵, 则一般地有

$$\operatorname{rank} Q (s) R (s) \leqslant \min (\operatorname{rank} Q (s), \operatorname{rank} R (s)) \tag {6.7}$$
