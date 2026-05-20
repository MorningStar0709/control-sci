# 6.8 公因子和最大公因子

公因子定义 称方多项式矩阵 $R(s)$ 为具有相同列数的两个多项式矩阵 $N(s)$ 和 $D(s)$ 的一个右公因子，如果存在多项式矩阵 $\overline{N}(s)$ 和 $\overline{D}(s)$ 使成立

$$N (s) = \bar {N} (s) R (s), D (s) = \bar {D} (s) R (s) \tag {6.21}$$

称方多项式矩阵 $Q(s)$ 为具有相同行数的两个多项式矩阵 $B(s)$ 和 $A(s)$ 的一个左公因子，如果存在多项式矩阵 $\bar{B}(s)$ 和 $\bar{A}(s)$ 使成立

$$B (s) = Q (s) \bar {B} (s), A (s) = Q (s) \bar {A} (s) \tag {6.22}$$

最大公因子定义 称方多项式矩阵 $R(s)$ 为具有相同列数的两个多项式矩阵 $N(s)$ 和 $D(s)$ 的一个最大右公因子，简记为 $\gcd$ 。如果：（1） $R(s)$ 是 $N(s)$ 和 $D(s)$ 的一个右公因子。（2） $N(s)$ 和 $D(s)$ 的任一其它右公因子（例如 $R_1(s)$ ）均为 $R(s)$ 的右乘因子，即存在一个多项式矩阵 $W(s)$ 使成立 $R(s) = W(s)R_1(s)$ 。

最大左公因子的定义具有对偶的形式。称 $Q(s)$ 为两个多项式矩阵 $B(s)$ 和 $A(s)$ 的一个最大左公因子，简记为 $\gcd$ ，如果：（1） $Q(s)$ 是 $B(s)$ 和 $A(s)$ 的一个左公因子。（2） $B(s)$ 和 $A(s)$ 的任一其它左公因子（例如 $Q_1(s)$ ）均为 $Q(s)$ 的左乘因子，即存在一个多项式矩阵 $V(s)$ 使成立 $Q(s) = Q_1(s)V(s)$ 。

gerd 的构造定理 下面,我们来给出用以构造最大右公因子的一个重要结论,它被表述为如下的一个定理。

定理 对给定的 $p \times p$ 和 $q \times p$ 的多项式矩阵 $D(s)$ 和 $N(s)$ ，如果可找到一个 $(p + q) \times (p + q)$ 的单模阵 $U(s)$ ，使成立

$$
U (s) \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{l l} U _ {1 1} (s) & U _ {1 2} (s) \\ U _ {2 1} (s) & U _ {2 2} (s) \end{array} \right] \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{c} R (s) \\ \mathbf {0} \end{array} \right] \tag {6.23}
$$

则 $p \times p$ 的多项式矩阵 $R(s)$ 即为 $D(s)$ 和 $N(s)$ 的一个 $\gcd$ 。

证（1）先证明 $R(s)$ 是 $D(s)$ 和 $N(s)$ 的一个右公因子。为此，表 $U(s)$ 的逆矩阵 $V(s)$ 为

$$
V (s) = U ^ {- 1} (s) = \left[ \begin{array}{l l} V _ {1 1} (s) & V _ {1 2} (s) \\ V _ {2 1} (s) & V _ {2 2} (s) \end{array} \right] \tag {6.24}
$$

则可由(6.23)导出

$$
\left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{l l} V _ {1 1} (s) & V _ {1 2} (s) \\ V _ {2 1} (s) & V _ {2 2} (s) \end{array} \right] \left[ \begin{array}{c} R (s) \\ 0 \end{array} \right] = \left[ \begin{array}{l} V _ {1 1} (s) R (s) \\ V _ {2 1} (s) R (s) \end{array} \right] \tag {6.25}
$$

表明存在多项式矩阵 $V_{11}(s)$ 和 $V_{21}(s)$ 使成立

$$D (s) = V _ {1 1} (s) R (s), N (s) = V _ {2 1} (s) R (s) \tag {6.26}$$

因此，据定义即知， $R(s)$ 为 $D(s)$ 和 $N(s)$ 的一个右公因子。

(2) 再来证明 $D(s)$ 和 $N(s)$ 的任一其它右公因子 $R_{1}(s)$ 均为 $R(s)$ 的右乘因子。因 $R_{1}(s)$ 为右乘因子，故可导出

$$D (s) = D _ {1} (s) R _ {1} (s), \quad N (s) = N _ {1} (s) R _ {1} (s) \tag {6.27}$$

再由式(6.23)可得到

$$R (s) = U _ {1 1} (s) D (s) + U _ {1 2} (s) N (s) \tag {6.28}$$

将(6.27)代入(6.28)，即可进而得到

$$R (s) = \left[ U _ {1 1} (s) D _ {1} (s) + U _ {1 2} (s) N _ {1} (s) \right] R _ {1} (s)= W (s) R _ {1} (s) \tag {6.29}$$

其中 $W(s)$ 为多项式矩阵。这表明 $R_{1}(s)$ 为 $R(s)$ 的右乘因子。
