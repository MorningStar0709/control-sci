Rank of Matrix. A matrix A is said to have rank m if there exists an $m \times m$ submatrix M of A such that the determinant of M is nonzero and the determinant of every $r \times r$ submatrix (where $r \geq m + 1 )$ of A is zero.

As an example, consider the following matrix:

$$
\mathbf {A} = \left[ \begin{array}{c c c c} 1 & 2 & 3 & 4 \\ 0 & 1 & - 1 & 0 \\ 1 & 0 & 1 & 2 \\ 1 & 1 & 0 & 2 \end{array} \right]
$$

Note that $| \mathbf { A } | = 0$ . One of a number of largest submatrices whose determinant is not equal to zero is

$$
\left[ \begin{array}{c c c} 1 & 2 & 3 \\ 0 & 1 & - 1 \\ 1 & 0 & 1 \end{array} \right]
$$

Hence, the rank of the matrix A is 3.

Minor $M _ { i j } .$ If the ith row and jth column are deleted from an $n \times n$ matrix A, the resulting matrix is an $( n \mathrm { ~ - ~ } 1 ) \times ( n \mathrm { ~ - ~ } 1 )$ matrix. The determinant of this $( n \mathrm { ~ - ~ } 1 ) \times ( n \mathrm { ~ - ~ } 1 )$ matrix is called the minor $M _ { i j }$ of the matrix A.

Cofactor $A _ { i j } .$ The cofactor $A _ { i j }$ of the element $a _ { i j }$ of the $n \times n$ matrix A is defined by the equation

$$A _ {i j} = (- 1) ^ {i + j} M _ {i j}$$

That is, the cofactor $A _ { i j }$ of the element $a _ { i j } \mathrm { i s } ( - 1 ) ^ { i + j }$ times the determinant of the matrix formed by deleting the ith row and the jth column from A. Note that the cofactor $A _ { i j }$ of the element $a _ { i j }$ is the coefficient of the term $a _ { i j }$ in the expansion of the determinant $\left| \mathbf { \bar { A } } \right|$ , since it can be shown that

$$a _ {i 1} A _ {i 1} + a _ {i 2} A _ {i 2} + \dots + a _ {i n} A _ {i n} = | \mathbf {A} |$$

If $a _ { i 1 } , a _ { i 2 } , \ldots , a _ { i n }$ are replaced by $a _ { j 1 } , a _ { j 2 } , \dotsc , a _ { j n }$ then,

$$a _ {j 1} A _ {i 1} + a _ {j 2} A _ {i 2} + \dots + a _ {j n} A _ {i n} = 0 \quad i \neq j$$

because the determinant of A in this case possesses two identical rows. Hence, we obtain

$$\sum_ {k = 1} ^ {n} a _ {j k} A _ {i k} = \delta_ {j i} | \mathbf {A} |$$

Similarly,

$$\sum_ {k = 1} ^ {n} a _ {k i} A _ {k j} = \delta_ {i j} | \mathbf {A} |$$

Adjoint Matrix. The matrix B whose element in the ith row and jth column equals $A _ { j i }$ is called the adjoint of A and is denoted by adj A, or

$$\mathbf {B} = \left(b _ {i j}\right) = \left(A _ {j i}\right) = \operatorname{adj} \mathbf {A}$$

That is, the adjoint of A is the transpose of the matrix whose elements are the cofactors of A, or

$$
\operatorname{adj} \mathbf {A} = \left[ \begin{array}{c c c c} A _ {1 1} & A _ {2 1} & \ldots & A _ {n 1} \\ A _ {1 2} & A _ {2 2} & \ldots & A _ {n 2} \\ \vdots & \vdots & & \vdots \\ A _ {1 n} & A _ {2 n} & \ldots & A _ {n m} \end{array} \right]
$$
