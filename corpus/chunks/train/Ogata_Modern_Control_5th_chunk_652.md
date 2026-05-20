$$
\begin{array}{l} y = \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{r r r} 1 & 1 & 1 \\ - 1 & - 2 & - 3 \\ 1 & 4 & 9 \end{array} \right] \left[ \begin{array}{c} z _ {1} \\ z _ {2} \\ z _ {3} \end{array} \right] \\ = \left[ \begin{array}{l l l} 1 & 1 & 1 \end{array} \right] \left[ \begin{array}{l} z _ {1} \\ z _ {2} \\ z _ {3} \end{array} \right] \tag {9-21} \\ \end{array}
$$

Notice that the transformation matrix P, defined by Equation (9–18), modifies the coefficient matrix of z into the diagonal matrix. As is clearly seen from Equation (9–20), the three scalar state equations are uncoupled. Notice also that the diagonal elements of the matrix $\mathbf { P } ^ { - 1 } \mathbf { A } \mathbf { P }$ in Equation (9–19) are identical with the three eigenvalues of A. It is very important to note that the eigenvalues of A and those of $\mathbf { P } ^ { - 1 } \mathbf { A } \mathbf { P }$ are identical.We shall prove this for a general case in what follows.

Invariance of Eigenvalues. To prove the invariance of the eigenvalues under a linear transformation, we must show that the characteristic polynomials $| \lambda \mathbf { I } - \mathbf { A } |$ and $\left| \lambda \mathbf { I } - \mathbf { P } ^ { - 1 } \mathbf { A } \mathbf { P } \right|$ are identical.

Since the determinant of a product is the product of the determinants, we obtain

$$
\begin{array}{l} \left| \lambda \mathbf {I} - \mathbf {P} ^ {- 1} \mathbf {A P} \right| = \left| \lambda \mathbf {P} ^ {- 1} \mathbf {P} - \mathbf {P} ^ {- 1} \mathbf {A P} \right| \\ = \left| \mathbf {P} ^ {- 1} (\lambda \mathbf {I} - \mathbf {A}) \mathbf {P} \right| \\ = \left| \mathbf {P} ^ {- 1} \right| \left| \lambda \mathbf {I} - \mathbf {A} \right| \left| \mathbf {P} \right| \\ = \left| \mathbf {P} ^ {- 1} \right| \left| \mathbf {P} \right| \left| \lambda \mathbf {I} - \mathbf {A} \right| \\ \end{array}
$$

Noting that the product of the determinants $\left| \mathbf { P } ^ { - 1 } \right|$ and $| \mathbf { P } |$ is the determinant of the product $\left| \mathbf { P } ^ { = _ { 1 } } \mathbf { P } \right|$ , we obtain

$$
\begin{array}{l} \left| \lambda \mathbf {I} - \mathbf {P} ^ {- 1} \mathbf {A P} \right| = \left| \mathbf {P} ^ {- 1} \mathbf {P} \right| \left| \lambda \mathbf {I} - \mathbf {A} \right| \\ = | \lambda \mathbf {I} - \mathbf {A} | \\ \end{array}
$$

Thus, we have proved that the eigenvalues of A are invariant under a linear transformation.
