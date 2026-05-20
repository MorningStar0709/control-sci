证明过程如下：首先来证明 $N(s)D^{-1}(s)$ 是 $G(s)$ 的一个右MFD。为此利用(7.108)即有

$$
\begin{array}{l} N (s) D ^ {- 1} (s) = U ^ {- 1} (s) \Sigma (s) \cdot \Psi_ {r} ^ {- 1} (s) V ^ {- 1} (s) \\ = U ^ {- 1} (s) M (s) V ^ {- 1} (s) \\ = U ^ {- 1} (s) U (s) G (s) V (s) V ^ {- 1} (s) = G (s) \tag {7.109} \\ \end{array}
$$

表明 $N(s)D^{-1}(s)$ 为 $G(s)$ 的一个右 MFD。再来证明 $N(s)D^{-1}(s)$ 是不可简约的。已知 $\{\varepsilon_{i}(s), \psi_{i}(s)\}$ 为互质， $i=1,2,\cdots,r$ ，这意味着 $\{\Psi_{r}(s), \Sigma(s)\}$ 为右互质，也即存在单模阵 $\overline{U}(s)$ 使成立

$$
\overline {{U}} (s) \left[ \begin{array}{c} \Psi_ {r} (s) \\ \Sigma (s) \end{array} \right] = \left[ \begin{array}{c} R (s) \\ 0 \end{array} \right], R (s) \text {为单模阵} \tag {7.110}
$$

进而，可把上式改写为

$$
\begin{array}{l} \left[ \begin{array}{c} R (s) \\ 0 \end{array} \right] = \bar {U} (s) \left[ \begin{array}{c c} V (s) & \\ & U ^ {- 1} (s) \end{array} \right] ^ {- 1} \left[ \begin{array}{c c} V (s) & \\ & U ^ {- 1} (s) \end{array} \right] \left[ \begin{array}{c} \Psi_ {r} (s) \\ \Sigma (s) \end{array} \right] \\ = \widetilde {U} (s) \left[ \begin{array}{l} V (s) \Psi_ {r} (s) \\ U ^ {- 1} (s) \Sigma (s) \end{array} \right] = \widetilde {U} (s) \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] \tag {7.111} \\ \end{array}
$$

其中，由于 $V(s)$ 和 $U(s)$ 均为单模阵，可知

$$
\widetilde {U} (s) = \bar {U} (s) \left[ \begin{array}{c c} V (s) & \\ & U ^ {- 1} (s) \end{array} \right] ^ {- 1} \tag {7.112}
$$

也必为单模阵。这表明， $D(s)$ 和 $N(s)$ 的最大右公因子也为 $R(s)$ ，且 $R(s)$ 为单模阵。由此，进一步可知 $\{N(s), D(s)\}$ 为右互质。从而， $N(s)D^{-1}(s)$ 为 $G(s)$ 的一个不可简约 MFD。于是证明完成。
