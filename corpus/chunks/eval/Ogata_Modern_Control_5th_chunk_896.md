Note that the element of the jth row and ith column of the product A(adj A) is

$$\sum_ {k = 1} ^ {n} a _ {j k} b _ {k i} = \sum_ {k = 1} ^ {n} a _ {j k} A _ {i k} = \delta_ {j i} | \mathbf {A} |$$

Hence, A(adj A) is a diagonal matrix with diagonal elements equal to $| \mathbf { A } |$ , or

$$\mathbf {A} (\operatorname{adj} \mathbf {A}) = | \mathbf {A} | \mathbf {I}$$

Similarly, the element in the jth row and ith column of the product (adj A)A is

$$\sum_ {k = 1} ^ {n} b _ {j k} a _ {k i} = \sum_ {k = 1} ^ {n} A _ {k j} a _ {k i} = \delta_ {i j} | \mathbf {A} |$$

Hence, we have the relationship

$$\mathbf {A} (\operatorname{adj} \mathbf {A}) = (\operatorname{adj} \mathbf {A}) \mathbf {A} = | \mathbf {A} | \mathbf {I} \tag {C-1}$$

Thus

$$
\mathbf {A} ^ {- 1} = \frac {\operatorname{adj} \mathbf {A}}{| \mathbf {A} |} = \left[ \begin{array}{c c c c} \frac {A _ {1 1}}{| \mathbf {A} |} & \frac {A _ {2 1}}{| \mathbf {A} |} & \dots & \frac {A _ {n 1}}{| \mathbf {A} |} \\ \frac {A _ {1 2}}{| \mathbf {A} |} & \frac {A _ {2 2}}{| \mathbf {A} |} & \dots & \frac {A _ {n 2}}{| \mathbf {A} |} \\ \vdots & \vdots & & \vdots \\ \frac {A _ {1 n}}{| \mathbf {A} |} & \frac {A _ {2 n}}{| \mathbf {A} |} & \dots & \frac {A _ {n n}}{| \mathbf {A} |} \end{array} \right]
$$

where $A _ { i j }$ is the cofactor of $a _ { i j }$ of the matrix A. Thus, the terms in the ith column of $\mathbf { A } ^ { - 1 }$ are $1 / \lvert \mathbf { A } \rvert$ times the cofactors of the ith row of the original matrix A. For example, if

$$
\mathbf {A} = \left[ \begin{array}{c c c} 1 & 2 & 0 \\ 3 & - 1 & - 2 \\ 1 & 0 & - 3 \end{array} \right]
$$

then the adjoint of A and the determinant $| \mathbf { A } |$ are respectively found to be

$$
\begin{array}{l} \operatorname{adj} \mathbf {A} = \left[ \begin{array}{c c c c c} \left| \begin{array}{c c} - 1 & - 2 \\ 0 & - 3 \end{array} \right| & - \left| \begin{array}{c c} 2 & 0 \\ 0 & - 3 \end{array} \right| & \left| \begin{array}{c c} 2 & 0 \\ - 1 & - 2 \end{array} \right| \\ - \left| \begin{array}{c c} 3 & - 2 \\ 1 & - 3 \end{array} \right| & \left| \begin{array}{c c} 1 & 0 \\ 1 & - 3 \end{array} \right| & - \left| \begin{array}{c c} 1 & 0 \\ 3 & - 2 \end{array} \right| \\ \left| \begin{array}{c c} 3 & - 1 \\ 1 & 0 \end{array} \right| & - \left| \begin{array}{c c} 1 & 2 \\ 1 & 0 \end{array} \right| & \left| \begin{array}{c c} 1 & 2 \\ 3 & - 1 \end{array} \right| \end{array} \right] \\ = \left[ \begin{array}{c c c} 3 & 6 & - 4 \\ 7 & - 3 & 2 \\ 1 & 2 & - 7 \end{array} \right] \\ \end{array}
$$

and

$$\left| \mathbf {A} \right| = 1 7$$

Hence, the inverse of A is
