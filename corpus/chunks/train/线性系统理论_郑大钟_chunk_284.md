对于右不可简约 MFD 而言, 当 $G(s)$ 的一个不可简约 $N_{1}(s)D_{1}^{-1}(s)$ 被定出后, 则所有其它的不可简约 $N_{i}(s)D_{i}^{-1}(s)$ 的分子矩阵和分母矩阵即为:

$$N _ {i} (s) = N _ {1} (s) U _ {i} (s), D _ {i} (s) = D _ {1} (s) U _ {i} (s) \tag {7.63}$$

其中， $U_{i}(s)$ 为单模阵， $i=2,3,\cdots$ 。

对于左不可简约 MFD 而言, 则当 $G(s)$ 的一个左不可简约 $A_{1}^{-1}(s)B_{1}(s)$ 被确定后, 所有其它的不可简约 $A_{j}^{-1}(s)B_{j}(s)$ 的分子矩阵和分母矩阵就即为

$$B _ {i} (s) = V _ {i} (s) B _ {1} (s), \quad A _ {i} (s) = V _ {i} (s) A _ {1} (s) \tag {7.64}$$

其中， $V_{i}(s)$ 为单模阵， $j=2,3,\cdots$ 。

性质3[不可简约MFD和可简约MFD间的关系]设 $N(s)D^{-1}(s)$ 为给定传递函数矩阵 $G(s)$ 的一个不可简约MFD，则对它的任一可简约 $\mathrm{MFD}\bar{N} (s)\overline{D}^{-1}(s)$ ，一定存在一个非奇异多项式矩阵 $T(s)$ ，使成立

$$\bar {N} (s) = N (s) T (s), \bar {D} (s) = D (s) T (s) \tag {7.65}$$

证（1）由可简约 $\overline{N}(s)\overline{D}^{-1}(s)$ 找出一个不可简约 $\widetilde{N}(s)\widetilde{D}^{-1}(s)$ ：已知 $\overline{N}(s)\overline{D}^{-1}(s)$ 可简约，表明 $\{\overline{N}(s),\overline{D}(s)\}$ 不是右互质的，从而可知 $\overline{D}(s)$ 和 $\overline{N}(s)$ 的最大右公因子 $R(s)$ 不是单模阵，但 $R(s)$ 是非奇异的。由此，取 $\widetilde{N}(s) = \overline{N}(s)R^{-1}(s)$ 和 $\widetilde{D}(s) = \overline{D}\times$ $(s)R^{-1}(s)$ ，则即有

$$\widetilde {N} (s) \widetilde {D} ^ {- 1} (s) = \bar {N} (s) R ^ {- 1} (s) \cdot R (s) \overrightarrow {D} ^ {- 1} (s) = \bar {N} (s) \overrightarrow {D} ^ {- 1} (s) \tag {7.66}$$

表明 $\widetilde{N}(s)\widetilde{D}^{-1}(s)$ 也是 $G(s)$ 的一个MFD。再由

$$
\overline {{U}} (s) \left[ \begin{array}{c} \overline {{D}} (s) \\ \overline {{N}} (s) \end{array} \right] = \left[ \begin{array}{c} R (s) \\ \mathbf {0} \end{array} \right] = \left[ \begin{array}{c} I \\ \mathbf {0} \end{array} \right] R (s) \tag {7.67}
$$

则通过将上式右乘 $R^{-1}(s)$ 即可导出

$$
\overline {{U}} (s) \left[ \begin{array}{l} \overline {{D}} (s) R ^ {- 1} (s) \\ \overline {{N}} (s) R ^ {- 1} (s) \end{array} \right] = \overline {{U}} (s) \left[ \begin{array}{l} \widetilde {D} (s) \\ \widetilde {N} (s) \end{array} \right] = \left[ \begin{array}{l} I \\ 0 \end{array} \right] \tag {7.68}
$$

表明 $\{\widetilde{D}(s),\widetilde{N}(s)\}$ 的最大右公因子为单模阵 $I$ ，从而进一步可知 $\{\widetilde{D}(s),\widetilde{N}(s)\}$ 为

右互质，即由可简约的 $\widetilde{N}(s)\widetilde{D}^{-1}(s)$ 找到了一个不可简约的 $\widetilde{N}(s)\widetilde{D}^{-1}(s)$ 。

(2) 构造 $T(s)$ : 由于 $N(s)D^{-1}(s)$ 和 $\widetilde{N}(s)\widetilde{D}^{-1}(s)$ 均为 $G(s)$ 的不可简约 MFD, 所以根据性质 1 可知, 存在单模阵 $U(s)$ 使成立

$$\widetilde {N} (s) = N (s) U (s), \quad \widetilde {D} (s) = D (s) U (s) \tag {7.69}$$
