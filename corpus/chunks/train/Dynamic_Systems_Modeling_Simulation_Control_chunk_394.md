Equation (7.95) is equal to the state equation (7.92). Equating the right-hand side of the state equation (7.92) with Eq. (7.95) (along with the substitution $\mathbf { x } = \mathbf { c } e ^ { \lambda t } )$ yields

$$\lambda \mathbf {c} e ^ {\lambda t} = \mathbf {A} \mathbf {c} e ^ {\lambda t} \tag {7.96}$$

Moving the right-hand side of Eq. (7.96) to the left-hand side and factoring out $\mathbf { c } e ^ { \lambda t }$ yields

$$[ \lambda \mathbf {I} - \mathbf {A} ] \mathbf {c} e ^ {\lambda t} = \mathbf {0} \tag {7.97}$$

Note that the bracket term in Eq. (7.97) must be an $n \times n$ matrix, and therefore the scalar ?? is multiplied by the $n \times n$ identity matrix I, which consists of ones on the main diagonal and zeros elsewhere. The right-hand side of Eq. (7.97) is an n × 1 column vector of zeros. Except for the trivial solution $\mathbf { x } = \mathbf { c } e ^ { \lambda t } = \mathbf { 0 }$ , the term $\mathbf { c } e ^ { \lambda t }$ is not zero for all values of time t, and therefore Eq. (7.97) is satisfied only if the determinant of the matrix in the brackets is zero, or

$$\left| \lambda \mathbf {I} - \mathbf {A} \right| = \det (\lambda \mathbf {I} - \mathbf {A}) = 0 \tag {7.98}$$

Expanding the determinant in Eq. (7.98) produces an nth-order polynomial in ??, which is best demonstrated by an example. Consider the third-order system matrix

$$
\mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 2 & - 8 & - 3 \end{array} \right] \tag {7.99}
$$

The matrix ??I − A is

$$
\lambda \mathbf {I} - \mathbf {A} = \left[ \begin{array}{l l l} \lambda & 0 & 0 \\ 0 & \lambda & 0 \\ 0 & 0 & \lambda \end{array} \right] - \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 2 & - 8 & - 3 \end{array} \right] = \left[ \begin{array}{c c c} \lambda & - 1 & 0 \\ 0 & \lambda & - 1 \\ 1 2 & 8 & \lambda + 3 \end{array} \right] \tag {7.100}
$$

The determinant of Eq. (7.100) is

$$
\left| \begin{array}{c c c} \lambda & - 1 & 0 \\ 0 & \lambda & - 1 \\ 1 2 & 8 & \lambda + 3 \end{array} \right| = \lambda^ {3} + 3 \lambda^ {2} + 8 \lambda + 1 2 = 0 \tag {7.101}
$$
