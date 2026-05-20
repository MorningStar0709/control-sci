For the given matrix B, the degree of the minimal polynomial is lower by 1 than that of the characteristic polynomial.As shown here, if the multiple eigenvalues of an n\*n matrix are not linked in a Jordan chain, the minimal polynomial is of lower degree than the characteristic polynomial.

A–9–10. Show that by use of the minimal polynomial, the inverse of a nonsingular matrix A can be expressed as a polynomial in A with scalar coefficients as follows:

$$\mathbf {A} ^ {- 1} = - \frac {1}{a _ {m}} \left(\mathbf {A} ^ {m - 1} + a _ {1} \mathbf {A} ^ {m - 2} + \dots + a _ {m - 2} \mathbf {A} + a _ {m - 1} \mathbf {I}\right) \tag {9-100}$$

where $a _ { 1 } , a _ { 2 } , \ldots , a _ { m }$ are coefficients of the minimal polynomial

$$\phi (\lambda) = \lambda^ {m} + a _ {1} \lambda^ {m - 1} + \dots + a _ {m - 1} \lambda + a _ {m}$$

Then obtain the inverse of the following matrix A:

$$
\mathbf {A} = \left[ \begin{array}{c c c} 1 & 2 & 0 \\ 3 & - 1 & - 2 \\ 1 & 0 & - 3 \end{array} \right]
$$

Solution. For a nonsingular matrix A, its minimal polynomial $\phi ( \mathbf { A } )$ can be written as

$$\phi (\mathbf {A}) = \mathbf {A} ^ {m} + a _ {1} \mathbf {A} ^ {m - 1} + \dots + a _ {m - 1} \mathbf {A} + a _ {m} \mathbf {I} = \mathbf {0}$$

where $a _ { m } \neq 0 .$ . Hence,

$$\mathbf {I} = - \frac {1}{a _ {m}} \left(\mathbf {A} ^ {m} + a _ {1} \mathbf {A} ^ {m - 1} + \dots + a _ {m - 2} \mathbf {A} ^ {2} + a _ {m - 1} \mathbf {A}\right)$$

Premultiplying by $\mathbf { A } ^ { - 1 }$ , we obtain

$$\mathbf {A} ^ {- 1} = - \frac {1}{a _ {m}} \left(\mathbf {A} ^ {m - 1} + a _ {1} \mathbf {A} ^ {m - 2} + \dots + a _ {m - 2} \mathbf {A} + a _ {m - 1} \mathbf {I}\right)$$

which is Equation (9–100).

For the given matrix A, adj(lI-A) can be given as

$$
\operatorname{adj} (\lambda \mathbf {I} - \mathbf {A}) = \left[ \begin{array}{c c c} \lambda^ {2} + 4 \lambda + 3 & 2 \lambda + 6 & - 4 \\ 3 \lambda + 7 & \lambda^ {2} + 2 \lambda - 3 & - 2 \lambda + 2 \\ \lambda + 1 & 2 & \lambda^ {2} - 7 \end{array} \right]
$$

Clearly, there is no common divisor $d ( \lambda )$ of all elements of adj(lI-A). Hence, d(l)=1. Consequently, the minimal polynomial f(l) is given by

$$\phi (\lambda) = \frac {| \lambda \mathbf {I} - \mathbf {A} |}{d (\lambda)} = | \lambda \mathbf {I} - \mathbf {A} |$$

Thus, the minimal polynomial f(l) is the same as the characteristic polynomial.

Since the characteristic polynomial is

$$\left| \lambda \mathbf {I} - \mathbf {A} \right| = \lambda^ {3} + 3 \lambda^ {2} - 7 \lambda - 1 7$$

we obtain

$$\phi (\lambda) = \lambda^ {3} + 3 \lambda^ {2} - 7 \lambda - 1 7$$
