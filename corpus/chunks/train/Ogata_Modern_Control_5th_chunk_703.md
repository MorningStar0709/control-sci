Since the greatest common divisor of the $n ^ { 2 }$ elements of $\mathbf { B } ( \boldsymbol { \lambda } )$ is unity, we have

$$g (\lambda) = 1$$

Therefore,

$$\psi (\lambda) = \phi (\lambda)$$

Then, from this last equation and Equation (9–99), we obtain

$$\phi (\lambda) = \frac {| \lambda \mathbf {I} - \mathbf {A} |}{d (\lambda)}$$

A–9–9. If an n\*n matrix A has n distinct eigenvalues, then the minimal polynomial of A is identical to the characteristic polynomial. Also, if the multiple eigenvalues of A are linked in a Jordan chain, the minimal polynomial and the characteristic polynomial are identical. If, however, the multiple eigenvalues of A are not linked in a Jordan chain, the minimal polynomial is of lower degree than the characteristic polynomial.

Using the following matrices A and B as examples, verify the foregoing statements about the minimal polynomial when multiple eigenvalues are involved:

$$
\mathbf {A} = \left[ \begin{array}{c c c} 2 & 1 & 4 \\ 0 & 2 & 0 \\ 0 & 3 & 1 \end{array} \right], \qquad \mathbf {B} = \left[ \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 3 & 1 \end{array} \right]
$$

Solution. First, consider the matrix A. The characteristic polynomial is given by

$$
| \lambda \mathbf {I} - \mathbf {A} | = \left| \begin{array}{c c c} \lambda - 2 & - 1 & - 4 \\ 0 & \lambda - 2 & 0 \\ 0 & - 3 & \lambda - 1 \end{array} \right| = (\lambda - 2) ^ {2} (\lambda - 1)
$$

Thus, the eigenvalues of A are 2, 2, and 1. It can be shown that the Jordan canonical form of A is

$$
\left[ \begin{array}{c c c} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right]
$$

and the multiple eigenvalues are linked in the Jordan chain as shown.

To determine the minimal polynomial, let us first obtain adj(lI-A). It is given by

$$
\operatorname{adj} (\lambda \mathbf {I} - \mathbf {A}) = \left[ \begin{array}{c c c} (\lambda - 2) (\lambda - 1) & (\lambda + 1 1) & 4 (\lambda - 2) \\ 0 & (\lambda - 2) (\lambda - 1) & 0 \\ 0 & 3 (\lambda - 2) & (\lambda - 2) ^ {2} \end{array} \right]
$$

Notice that there is no common divisor of all the elements of $\operatorname { a d j } ( \lambda \mathbf { I } - \mathbf { A } )$ Hence, d(l)=1.. Thus, the minimal polynomial f(l) is identical to the characteristic polynomial, or

$$
\begin{array}{l} \phi (\lambda) = | \lambda \mathbf {I} - \mathbf {A} | = (\lambda - 2) ^ {2} (\lambda - 1) \\ = \lambda^ {3} - 5 \lambda^ {2} + 8 \lambda - 4 \\ \end{array}
$$

A simple calculation proves that
