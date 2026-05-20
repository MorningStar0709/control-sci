# 6.9 互质性

右互质和左互质 称两个具有相同列数的多项式矩阵 $D(s)$ 和 $N(s)$ 是右互质的，如果它们的最大右公因子（gcrd）为单模阵。称两个具有相同行数的多项式矩阵 $A(s)$ 和 $B(s)$ 是左互质的，如果它们的最大左公因子（gcld）为单模阵。

右互质性判据 在基于多项式矩阵理论的线性系统分析中，常常会涉及到互质性的判别问题。下面，限于右互质性，介绍几种比较有用的判别准则。

判据1 [贝佐特等式判据] $p \times p$ 和 $q \times p$ 的多项式矩阵 $D(s)$ 和 $N(s)$ 是右互质的，当且仅当存在 $p \times p$ 和 $p \times q$ 的多项式矩阵 $X(s)$ 和 $Y(s)$ 使成立如下的贝佐特 (Bezout) 等式

$$X (s) D (s) + Y (s) N (s) = 1 \tag {6.40}$$

证 必要性： $D(s)$ 和 $N(s)$ 为右互质，欲证等式(6.40)成立。

根据 gcrd 的构造定理的关系式(6.23)，可以导出：

$$R (s) = U _ {1 1} (s) D (s) + U _ {1 2} (s) N (s) \tag {6.41}$$

其中 $U_{11}(s)$ 和 $U_{12}(s)$ 分别为 $p \times p$ 和 $p \times q$ 的多项式矩阵。现知 $D(s)$ 和 $N(s)$ 为右互质，则据定义可知 $R(s)$ 为单模阵，从而 $R^{-1}(s)$ 存在且也是多项式矩阵。由此，将式(6.41)左乘 $R^{-1}(s)$ ，就得到

$$R ^ {- 1} (s) U _ {1 1} (s) D (s) + R ^ {- 1} (s) U _ {1 2} (s) N (s) = I \tag {6.42}$$

上式中，令 $X(s) = R^{-1}(s)U_{11}(s)$ 和 $Y(s) = R^{-1}(s)U_{12}(s)$ ，即可导出(6.40)。必要性得证。

充分性：等式(6.40)成立，欲证 $D(s)$ 和 $N(s)$ 为右互质。

令 $R(s)$ 为 $D(s)$ 和 $N(s)$ 的一个 $\gcd$ ，则必存在多项式矩阵 $\overline{D}(s)$ 和 $\overline{N}(s)$ 使成立

$$D (s) = \overline {{D}} (s) R (s), \quad N (s) = \overline {{N}} (s) R (s) \tag {6.43}$$

现将(6.43)代入(6.40)，可得

$$[ X (s) \bar {D} (s) + Y (s) \bar {N} (s) ] R (s) = I \tag {6.44}$$

这表明 $R^{-1}(s)$ 存在，且

$$R ^ {- 1} (s) = X (s) \bar {D} (s) + Y (s) \bar {N} (s) \tag {6.45}$$

也是多项式矩阵。所以， $R(s)$ 为单模阵，也即 $D(s)$ 和 $N(s)$ 为右互质。充分性得证。

判据2 [秩判据] 给定 $p \times p$ 和 $q \times p$ 的多项式矩阵 $D(s)$ 和 $N(s), D(s)$ 为非奇异, 则 $D(s)$ 和 $N(s)$ 为右互质, 当且仅当

$$
\operatorname{rank} \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = p, \forall s \in \mathcal {C} \tag {6.46}
$$

证 根据 gcrd 的构造定理,有

$$
U (s) \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{c} R (s) \\ 0 \end{array} \right] \tag {6.47}
$$

其中 $U(s)$ 为单模阵。则当且仅当(6.46)成立时，有 $R(s)$ 为单模阵，也即 $D(s)$ 和 $N(s)$

为右互质。于是结论得证。

判据3 [非右互质判据] 给定 $p \times p$ 和 $q \times p$ 的多项式矩阵 $D(s)$ 和 $N(s), D(s)$ 为非奇异, 则 $D(s)$ 和 $N(s)$ 是非右互质的, 当且仅当存在 $q \times p$ 和 $q \times q$ 的多项式矩阵 $B(s)$ 和 $A(s)$ , 使同时成立

$$
- B (s) D (s) + A (s) N (s) = [ - B (s) A (s) ] \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = 0 \tag {6.48}
\deg \det A (s) < \deg \det D (s) \tag {6.49}
$$

证 (1)建立关系式(6.48)

由 gcrd 的构造定理的关系式

$$
U (s) \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{l l} U _ {1 1} (s) & U _ {1 2} (s) \\ U _ {2 1} (s) & U _ {2 2} (s) \end{array} \right] \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{c} R (s) \\ 0 \end{array} \right] \tag {6.50}
$$

可以导出
