证 此结论中的论断(1)可由秩判据予以证明，论断(2)可由PBH秩判据予以证明。前一种情况比较简单，故推证过程略去。下面只来推证后一种情况，并且为符号不致过于繁杂，不妨设 $\hat{A}$ 和 $\hat{B}$ 为：

$$
\hat {A} = \left[ \begin{array}{c c c c c c c c} \lambda_ {1} & 1 & 0 \\ 0 & \lambda_ {1} & 1 \\ 0 & 0 & \lambda_ {1} \\ \hline & & & \lambda_ {1} & 1 \\ & & & 0 & \lambda_ {2} \\ & & & & & \lambda_ {2} & 1 \\ & & & & & 0 & \lambda_ {2} \end{array} \right] \quad \hat {B} = \left[ \begin{array}{c} \hat {b} _ {1 1 1} \\ \hat {b} _ {2 1 1} \\ \hat {b} _ {r 1 1} \\ \hline \hat {b} _ {1 1 2} \\ \hat {b} _ {r 1 2} \\ \hline \hat {b} _ {2 2 1} \\ \hat {b} _ {r 2 1} \end{array} \right] \tag {3.46}
$$

则即可导出

$$
[ s I - A, B ] = \left[ \begin{array}{c c c} s - \lambda_ {1} & - 1 & 0 \\ 0 & s - \lambda_ {1} & - 1 \\ 0 & 0 & s - \lambda_ {1} \end{array} \right] \left| \begin{array}{c c c} & & \hat {\boldsymbol {b}} _ {1 1 1} \\ & & \hat {\boldsymbol {b}} _ {2 1 2} \\ & & \hat {\boldsymbol {b}} _ {r 1 1} \\ \hline s - \lambda_ {1} & - 1 \\ 0 & s - \lambda_ {1} \end{array} \right| \left| \begin{array}{c c c} & & \hat {\boldsymbol {b}} _ {1 1 2} \\ & & \hat {\boldsymbol {b}} _ {r 1 2} \\ \hline s - \lambda_ {2} & - 1 \\ 0 & s - \lambda_ {2} \end{array} \right| \left| \begin{array}{c c c} & & \hat {\boldsymbol {b}} _ {1 2 1} \\ & & \hat {\boldsymbol {b}} _ {r 2 1} \end{array} \right] \tag {3.47}
$$

由(3.46)可知，在所考虑情况下， $\hat{A}$ 有两个特征值 $\lambda_1$ 和 $\lambda_2$ ，且 $\lambda_1 \neq \lambda_2$ 。并且，相对于 $\lambda_1$ ，有两个约当小块；而对应于 $\lambda_2$ ，有一个约当小块。利用 PBH 秩判据，先对 $s = \lambda_1$ 进行判断，于是由(3.47)中令 $s = \lambda_1$ 可导出

$$
[ \lambda_ {1} I - A, B ] = \left[ \begin{array}{c c c c c c c c c} 0 & - 1 & 0 \\ 0 & 0 & - 1 \\ 0 & 0 & 0 \\ \hline & & & 0 & - 1 \\ & & & 0 & 0 \\ \hline & & & & \lambda_ {1} - \lambda_ {2} & - 1 \\ & & & & 0 & \lambda_ {1} - \lambda_ {2} \end{array} \right] \left[ \begin{array}{c c c c c c c c c} \hat {\boldsymbol {b}} _ {1 1 1} \\ \hat {\boldsymbol {b}} _ {2 1 1} \\ \hat {\boldsymbol {b}} _ {r 1 1} \\ \hline \hat {\boldsymbol {b}} _ {1 1 2} \\ \hat {\boldsymbol {b}} _ {r 1 2} \\ \hline \lambda_ {1} - \lambda_ {2} & - 1 \\ 0 & \lambda_ {1} - \lambda_ {2} \end{array} \right] \tag {3.48}
$$

其中 $\lambda_{1} - \lambda_{2} \neq 0$ 。再对式(3.48)作一系列的列和行变换，那么上式可变换为：

$$
\left[ \begin{array}{c c c c c c c c c} 0 & - 1 & 0 \\ 0 & 0 & - 1 \\ 0 & 0 & 0 \\ \hline & & & 0 & - 1 \\ & & & 0 & 0 \\ \hline & & & & \lambda_ {1} - \lambda_ {2} & 0 \\ & & & & 0 & \lambda_ {1} - \lambda_ {2} \end{array} \right] \left[ \begin{array}{c} 0 \\ 0 \\ \hat {b} _ {r 1 1} \\ \hline 0 \\ \hat {b} _ {r 1 2} \\ \hline 0 \\ 0 \end{array} \right] \tag {3.49}
$$

这表明，(3.49)中的矩阵，也即 $[\lambda_1I - A, B]$ 为行满秩的充分必要条件为
