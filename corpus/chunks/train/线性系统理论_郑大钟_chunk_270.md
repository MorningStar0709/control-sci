例 给定列既约的方多项式矩阵 $D(s)$ 如下：

$$
D (s) = \left[ \begin{array}{c c} - 3 s & s + 2 \\ - s + 1 & 1 \end{array} \right], L = 1, p = 2
$$

先组成增广多项式矩阵

$$
\mathcal {B} (s) = \left[ \begin{array}{c c c c c c c c} - 3 s & s + 2 & - 3 s ^ {2} & s ^ {2} + 2 s & - 1 & 0 & - s & 0 \\ - s + 1 & 1 & - s ^ {2} + s & s & 0 & - 1 & 0 & - s \\ \boldsymbol {b} _ {1} & \boldsymbol {b} _ {2} & \boldsymbol {b} _ {3} & \boldsymbol {b} _ {4} & \boldsymbol {b} _ {5} & \boldsymbol {b} _ {6} & \boldsymbol {b} _ {7} & \boldsymbol {b} _ {8} \end{array} \right]
$$

开设 $\mathcal{B}(s)$ 的右半部分，即从 $[b_5, b_6, b_7, b_8]$ 中搜索相关列，有

$$
\boldsymbol {b} _ {7} = \left[ \begin{array}{l} - s \\ 0 \end{array} \right] = - \left[ \begin{array}{l l} s + 2 \\ 1 \end{array} \right] - 2 \left[ \begin{array}{l} - 1 \\ 0 \end{array} \right] - \left[ \begin{array}{l} 0 \\ - 1 \end{array} \right] = - \boldsymbol {b} _ {2} - 2 \boldsymbol {b} _ {5} - \boldsymbol {b} _ {6}

\boldsymbol {b} _ {s} = \left[ \begin{array}{l} 0 \\ - s \end{array} \right] = \left[ \begin{array}{l} - 3 s \\ - s + 1 \end{array} \right] + \left[ \begin{array}{l} 0 \\ - 1 \end{array} \right] - 3 \left[ \begin{array}{l} - s \\ 0 \end{array} \right] = \boldsymbol {b} _ {1} + \boldsymbol {b} _ {6} - 3 \boldsymbol {b} _ {7}
$$

考虑到两者的列位置指数为强意义下不相等,所以 $b_{7}$ 和 $b_{8}$ 为首相关列。于是,由上分析就可导出如下的两个关系式:

$$
\begin{array}{l} \boldsymbol {b} _ {2} + 2 \boldsymbol {b} _ {5} + \boldsymbol {b} _ {6} + \boldsymbol {b} _ {7} = 0 \\ - b _ {1} - b _ {6} + 3 b _ {7} + b _ {8} = 0 \\ \end{array}
$$

也即有

$$
\mathcal {B} (s) _ {\mathcal {A}} = \left[ \begin{array}{l l l l l l l l} b _ {1} & b _ {2} & b _ {3} & b _ {4} & b _ {5} & b _ {6} & b _ {7} & b _ {8} \end{array} \right] \left[ \begin{array}{c c} 0 & - 1 \\ \frac {1}{0} & 0 \\ \frac {0}{2} & 0 \\ \frac {1}{1} & - 1 \\ 0 & 1 \end{array} \right] = 0
$$

从而，就可定出

$$
E (s) = E _ {1} s + E _ {0} = \left[ \begin{array}{l l} 1 & 3 \\ 0 & 1 \end{array} \right] s + \left[ \begin{array}{l l} 2 & 0 \\ 1 & - 1 \end{array} \right] = \left[ \begin{array}{c c} s + 2 & 3 s \\ 1 & s - 1 \end{array} \right]
$$

可以看出， $E(s)$ 为准波波夫形。为进一步导出波波夫形，现对 $\mathcal{A}'$ 作初等运算使之化为实阶梯形：

$$
\begin{array}{l} \mathscr {A} ^ {\prime} = \left[ \begin{array}{c c c c c c c c} 0 & 1 & 0 & 0 & 2 & 1 & 1 & 0 \\ - 1 & 0 & 0 & 0 & 0 & - 1 & 3 & 1 \end{array} \right] \xrightarrow {\text {行} 2 ^ {n} - ^ {a} 3 \times \text {行} 1 ^ {n}} \\ \left[ \begin{array}{c c c c c c c c} 0 & 1 & 0 & 0 & 2 & 1 & 1 & 0 \\ - 1 & - 3 & 0 & 0 & - 6 & - 4 & 0 & 1 \end{array} \right] = \mathscr {A}, \\ \end{array}
$$

因而，即可得到

$$
D _ {H} (s) = \tilde {E} _ {1} s + \tilde {E} _ {0} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] s + \left[ \begin{array}{l l} 2 & - 6 \\ 1 & - 4 \end{array} \right] = \left[ \begin{array}{c c} s + 2 & - 6 \\ 1 & s - 4 \end{array} \right]

U (s) = \widetilde {U} _ {1} s + \widetilde {U} _ {0} = \left[ \begin{array}{l l} 0 & 0 \\ 0 & 0 \end{array} \right] s + \left[ \begin{array}{l l} 0 & - 1 \\ 1 & - 3 \end{array} \right] = \left[ \begin{array}{l l} 0 & - 1 \\ 1 & - 3 \end{array} \right]
$$
