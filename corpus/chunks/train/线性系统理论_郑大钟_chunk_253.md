$$
\widetilde {U} (s) = \left[ \begin{array}{c c} W (s) & 0 \\ 0 & I \end{array} \right] \tag {6.31}
$$

且将(6.30)两边左乘 $\widetilde{U}(s)$ ，可得

$$
\widetilde {U} (s) U (s) \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] - \left[ \begin{array}{c c} W (s) & 0 \\ 0 & I \end{array} \right] \left[ \begin{array}{l} R (s) \\ 0 \end{array} \right] - \left[ \begin{array}{c} W (s) R (s) \\ 0 \end{array} \right] \tag {6.32}
$$

再表 $\overline{U}(s) = \widetilde{U}(s)U(s)$ ，则 $\overline{U}(s)$ 也为单模阵。因此，式(6.32)意味着，存在单模阵 $\overline{U}(s)$ 使成立

$$
\overline {{{U}}} (s) \left[ \begin{array}{c} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{c} W (s) R (s) \\ 0 \end{array} \right] \tag {6.33}
$$

故由构造定理知， $W(s)R(s)$ 也为 $D(s)$ 和 $N(s)$ 的一个 $\mathbf{g}\mathbf{c}\mathbf{r}\mathbf{d}_{\circ}$ 于是证明完成。

性质2 gcrd 在非奇异性和单模性上的唯一性：设 $R_{1}(s)$ 和 $R_{2}(s)$ 是多项式矩阵 $D(s)$ 和 $N(s)$ 的任意两个 $\gcd$ ，则当 $R_{1}(s)$ 为非奇异(单模)时， $R_{2}(s)$ 也必为非奇异(单模)。

证 已知 $R_{1}(s)$ 和 $R_{2}(s)$ 都是 $D(s)$ 和 $N(s)$ 的 $\gcd$ ，因此根据定义可知，存在多项式矩阵 $W_{1}(s)$ 和 $W_{2}(s)$ 使成立

$$R _ {1} (s) = W _ {1} (s) R _ {2} (s), \quad R _ {2} (s) = W _ {2} (s) R _ {1} (s) \tag {6.34}$$

进而，将(6.34)中第二个关系式代入第一个关系式，又可得到

$$R _ {1} (s) = W _ {1} (s) W _ {2} (s) R _ {1} (s) \tag {6.35}$$

但已知 $R_{1}(s)$ 为非奇异(单模)，故有 $W_{1}(s)W_{2}(s) = I$ ，也即 $W_{1}(s)$ 和 $W_{2}(s)$ 均为单模阵。由此，由(6.34)即知，当 $R_{1}(s)$ 为非奇异时 $R_{2}(s)$ 也为非奇异，当 $R_{1}(s)$ 为单模时 $R_{2}(s)$ 也为单模。于是证明完成。

性质3 gcrd为非奇异的条件：给定 $p \times p$ 和 $q \times p$ 的多项式矩阵 $D(s)$ 和 $N(s)$ ，则当

$$
\left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] \text {为列满秩即} \operatorname{rank} \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = p \tag {6.36}
$$

时， $D(s)$ 和 $N(s)$ 的所有gcrd都必是非奇异的。

证 由构造定理,有

$$
U (s) \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{c} R (s) \\ 0 \end{array} \right] \tag {6.37}
$$

其中， $U(s)$ 为单模阵，gcrd $R(s)$ 为 $\pmb {p}\times \pmb{p}$ 多项式矩阵。从而，可得

$$
\operatorname{rank} R (s) = \operatorname{rank} \left[ \begin{array}{c} R (s) \\ 0 \end{array} \right] = \operatorname{rank} U (s) \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \operatorname{rank} \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right]
$$

这表明，当条件(6.36)成立时，必有 $\operatorname{rank} R(s) = p$ 即 $R(s)$ 为非奇异。再据 gcrd 在非奇异性上的唯一性，进而可知当(6.36)成立时所有 gcrd 均为非奇异。由此证明完成。

性质4 设 $R(s)$ 是 $p \times p$ 和 $q \times p$ 的多项式矩阵 $D(s)$ 和 $N(s)$ 的一个 $\gcd$ ，则 $R(s)$ 必可表为
