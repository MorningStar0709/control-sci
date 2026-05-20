\mathbf {Q} = \left[ \begin{array}{l l} 2 & 3 \\ 3 & 5 \end{array} \right]; \quad \mathbf {R} = r = \frac {1}{4}; \quad t _ {0} = 0; \quad t _ {f} = \infty . \tag {3.5.21}
$$

Let $\bar{\mathbf{P}}$ be the 2x2 symmetric matrix

$$
\bar {\mathbf {P}} = \left[ \begin{array}{l l} \bar {p} _ {1 1} & \bar {p} _ {1 2} \\ \bar {p} _ {1 2} & \bar {p} _ {2 2} \end{array} \right]. \tag {3.5.22}
$$

Then, the optimal control (3.5.14) is given by

$$
\begin{array}{l} u ^ {*} (t) = - 4 \left[ \begin{array}{c c} 0 & 1 \end{array} \right] \left[ \begin{array}{c c} \bar {p} _ {1 1} & \bar {p} _ {1 2} \\ \bar {p} _ {1 2} & \bar {p} _ {2 2} \end{array} \right] \left[ \begin{array}{c} x _ {1} ^ {*} (t) \\ x _ {2} ^ {*} (t) \end{array} \right], \\ = - 4 \left[ \bar {p} _ {1 2} x _ {1} ^ {*} (t) + \bar {p} _ {2 2} x _ {2} ^ {*} (t) \right], \tag {3.5.23} \\ \end{array}
$$

where, $\bar{P}$ , the 2x2 symmetric, positive definite matrix, is the solution of the matrix algebraic Riccati equation (3.5.15)

$$
\begin{array}{l} \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \right] = - \left[ \begin{array}{c c} \bar {p} _ {1 1} & \bar {p} _ {1 2} \\ \bar {p} _ {1 2} & \bar {p} _ {2 2} \end{array} \right] \left[ \begin{array}{c c} 0 & 1 \\ - 2 & 1 \end{array} \right] - \left[ \begin{array}{c c} 0 & - 2 \\ 1 & 1 \end{array} \right] \left[ \begin{array}{c c} \bar {p} _ {1 1} & \bar {p} _ {1 2} \\ \bar {p} _ {1 2} & \bar {p} _ {2 2} \end{array} \right] + \\ \left[ \begin{array}{l l} \bar {p} _ {1 1} & \bar {p} _ {1 2} \\ \bar {p} _ {1 2} & \bar {p} _ {2 2} \end{array} \right] \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] 4 [ 0 1 ] \left[ \begin{array}{l l} \bar {p} _ {1 1} & \bar {p} _ {1 2} \\ \bar {p} _ {1 2} & \bar {p} _ {2 2} \end{array} \right] - \left[ \begin{array}{l l} 2 & 3 \\ 3 & 5 \end{array} \right]. \tag {3.5.24} \\ \end{array}
$$

Simplifying the equation (3.5.24), we get

$$
\begin{array}{l} 4 \bar {p} _ {1 2} ^ {2} + 4 \bar {p} _ {1 2} - 2 = 0 \\ - \bar {p} _ {1 1} - \bar {p} _ {1 2} + 2 \bar {p} _ {2 2} + 4 \bar {p} _ {1 2} \bar {p} _ {2 2} - 3 = 0 \\ - 2 \bar {p} _ {1 2} - 2 \bar {p} _ {2 2} + 4 \bar {p} _ {2 2} ^ {2} - 5 = 0. \tag {3.5.25} \\ \end{array}
$$
