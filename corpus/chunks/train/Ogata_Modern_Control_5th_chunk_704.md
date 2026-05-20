$$
\begin{array}{l} \mathbf {A} ^ {3} - 5 \mathbf {A} ^ {2} + 8 \mathbf {A} - 4 \mathbf {I} \\ = \left[ \begin{array}{c c c} 8 & 7 2 & 2 8 \\ 0 & 8 & 0 \\ 0 & 2 1 & 1 \end{array} \right] - 5 \left[ \begin{array}{c c c} 4 & 1 6 & 1 2 \\ 0 & 4 & 0 \\ 0 & 9 & 1 \end{array} \right] + 8 \left[ \begin{array}{c c c} 2 & 1 & 4 \\ 0 & 2 & 0 \\ 0 & 3 & 1 \end{array} \right] - 4 \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] \\ = \left[ \begin{array}{l l l} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right] = \mathbf {0} \\ \end{array}
$$

but

$$
\begin{array}{l} \mathbf {A} ^ {2} - 3 \mathbf {A} + 2 \mathbf {I} \\ = \left[ \begin{array}{c c c} 4 & 1 6 & 1 2 \\ 0 & 4 & 0 \\ 0 & 9 & 1 \end{array} \right] - 3 \left[ \begin{array}{c c c} 2 & 1 & 4 \\ 0 & 2 & 0 \\ 0 & 3 & 1 \end{array} \right] + 2 \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] \\ = \left[ \begin{array}{c c c} 0 & 1 3 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right] \neq \mathbf {0} \\ \end{array}
$$

Thus, we have shown that the minimal polynomial and the characteristic polynomial of this matrix A are the same.

Next, consider the matrix B. The characteristic polynomial is given by

$$
| \lambda \mathbf {I} - \mathbf {B} | = \left| \begin{array}{c c c} \lambda - 2 & 0 & 0 \\ 0 & \lambda - 2 & 0 \\ 0 & - 3 & \lambda - 1 \end{array} \right| = (\lambda - 2) ^ {2} (\lambda - 1)
$$

A simple computation reveals that matrix B has three eigenvectors, and the Jordan canonical form of B is given by

$$
\left[ \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{array} \right]
$$

Thus, the multiple eigenvalues are not linked.To obtain the minimal polynomial, we first compute :adj(lI - B)

$$
\operatorname{adj} (\lambda \mathbf {I} - \mathbf {B}) = \left[ \begin{array}{c c c} (\lambda - 2) (\lambda - 1) & 0 & 0 \\ 0 & (\lambda - 2) (\lambda - 1) & 0 \\ 0 & 3 (\lambda - 2) & (\lambda - 2) ^ {2} \end{array} \right]
$$

from which it is evident that

$$d (\lambda) = \lambda - 2$$

Hence,

$$\phi (\lambda) = \frac {| \lambda \mathbf {I} - \mathbf {B} |}{d (\lambda)} = \frac {(\lambda - 2) ^ {2} (\lambda - 1)}{\lambda - 2} = \lambda^ {2} - 3 \lambda + 2$$

As a check, let us compute :f(B)

$$
\phi (\mathbf {B}) = \mathbf {B} ^ {2} - 3 \mathbf {B} + 2 \mathbf {I} = \left[ \begin{array}{l l l} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 9 & 1 \end{array} \right] - 3 \left[ \begin{array}{l l l} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 3 & 1 \end{array} \right] + 2 \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] = \left[ \begin{array}{l l l} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right] = \mathbf {0}
$$
