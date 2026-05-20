从而，注意到 $\widetilde{N}(s) = \overline{N}(s)R^{-1}(s)$ 和 $\widetilde{D}(s) = \overline{D}(s)R^{-1}(s)$ 的同时，可进一步导出

$$
\left\{ \begin{array}{l} \bar {N} (s) = \widetilde {N} (s) R (s) = N (s) [ U (s) R (s) ] = N (s) T (s) \\ \bar {D} (s) = \widetilde {D} (s) R (s) = D (s) [ U (s) R (s) ] = D (s) T (s) \end{array} \right. \tag {7.70}
$$

其中，已构造出 $T(s) = U(s)R(s)$ 。而且，由于 $U(s)$ 为单模阵，而 $R(s)$ 为非奇异，故 $T(s)$ 为非奇异多项式矩阵。由此，就完成了证明。

性质4[不可简约MFD在史密斯形和不变多项式意义下的同一性]对传递函数矩阵 $G(s)$ 的所有不可简约MFD

$$G (s) = N _ {i} (s) D _ {i} ^ {- 1} (s), i = 1, 2, \dots \tag {7.71}$$

必成立：（1） $N_{i}(s)$ ， $i=1,2,\cdots$ ，具有相同的史密斯形；（2） $D_{i}(s)$ ， $i=1,2,\cdots$ ，具有相同的不变多项式。

证（1）根据性质1，有 $N_{i}(s) = N_{1}(s)U_{i}(s)$ ，其中 $U_{i}(s)$ 为单模阵， $i = 2,3,\dots$ 。再令 $\Lambda (s) = \overline{U} (s)N_1(s)\overline{V} (s)$ 为 $N_{1}(s)$ 的史密斯形，那么即可导出

$$
\begin{array}{l} \Lambda (s) = \bar {U} (s) N _ {1} (s) \bar {V} (s) = \bar {U} (s) N _ {j} (s) U _ {j} ^ {- 1} (s) \bar {V} (s) \\ = \widetilde {U} _ {j} (s) N _ {j} (s) \widetilde {V} _ {j} (s), j = 2, 3, \dots \tag {7.72} \\ \end{array}
$$

其中 $\widetilde{U}_{i}(s)$ 和 $\widetilde{V}_{i}(s)$ 也为单模阵。这表明， $\Lambda(s)$ 也是 $N_{i}(s)$ 的史密斯形， $j=2,3,\cdots$ 。于是，此部分得证。

（2）根据性质1，又有 $D_{i}(s) = D_{1}(s)U_{j}(s)$ ，其中 $U_{i}(s)$ 为单模阵， $j = 2,3,\dots$ 。再注意到 $\det U_{i}(s) = c_{i}$ （非零常数），故由此即得

$$\det D _ {j} (s) = \det D _ {1} (s) \cdot \det U _ {j} (s) = c _ {j} \det D _ {1} (s) \tag {7.73}$$

从而，必成立

$$\det D _ {1} (s) \propto \det D _ {2} (s) \propto \dots \propto \det D _ {i} (s) \propto \dots \tag {7.74}$$

即 $D_{i}(s)(i=1,2,\cdots)$ 具有相同的不变多项式。因此证明完成。

性质5 [右不可简约 MFD 和左不可简约 MFD 在性质上的对偶性] 给定传递函数矩阵 $G(s)$ 的左不可简约 MFD 有着和右不可简约 MFD 相类同的性质 1—4，且两者在具体形式上是对偶的。

性质6 [左不可简约 MFD 和右不可简约 MFD 间的关系] 令 $A^{-1}(s)B(s)$ 和 $N(s)D^{-1}(s)$ 分别为给定传递函数矩阵 $G(s)$ 的任一左不可简约 MFD 和右不可简约 MFD，则必成立

$$\deg \det A (s) = \deg \det D (s) \tag {7.75}$$

证 根据实现理论， $G(s)$ 的不可简约MFD的次数为 $\deg \det A(s)$ 或 $\deg \det D(s)$ 的实现必为最小实现。因此，若式(7.75)不成立，则可导致次数不同的两个最小实现，而这是不可能的。因而，必有(7.75)成立。于是，证明完成。

性质7[不可简约MFD的最小阶性] 给定传递函数矩阵 $G(s)$ 的一个MFD为 $N(s)D^{-1}(s)$ 或 $A^{-1}(s)B(s)$ ，其阶次定义为

$$n _ {r} = \deg \det D (s) \text {或} n _ {l} = \deg \det A (s) \tag {7.76}$$

则当且仅当 $N(s)D^{-1}(s)$ 或 $A^{-1}(s)B(s)$ 为不可简约的MFD时，必为最小阶MFD。并且，当 $N(s)D^{-1}(s)$ 和 $A^{-1}(s)B(s)$ 均为最小阶MFD时，必有 $n_r = n_l$ 。

证（1）必要性：已知 $N(s)D^{-1}(s)$ 为 $G(s)$ 的一个不可简约MFD，则据性质3可知，对 $G(s)$ 的任一可简约 $\mathbf{MFD}\overline{N}(s)\overline{D}^{-1}(s)$ 成立关系式
