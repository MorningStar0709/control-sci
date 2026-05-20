$$
\begin{array}{l} C A ^ {n + 1} \mathbf {x} ^ {*} = - a _ {n - 1} C A ^ {n} \mathbf {x} ^ {*} - \dots - a _ {1} C A ^ {2} \mathbf {x} ^ {*} - a _ {0} C A \mathbf {x} ^ {*} \\ = 0. \\ \end{array}
$$

We proceed in the same manner to show that $CA^k\mathbf{x}^* = \mathbf{0}$ for all $k > n - 1$ . Using Equation 3.40, we see that $Ce^{At}\mathbf{x}^*$ and all its derivatives are zero at $t = 0$ . It follows that $Ce^{At}\mathbf{x}^* = \mathbf{0}$ for all $t$ ; i.e., $\mathbf{x}^*$ is unobservable.

This theorem leads to a test of system observability, by the requirement that there exist no observable states. That will be true if Equation 3.39 cannot be satisfied for any nonzero $\mathbf{x}^*$ . Equation 3.39 has a geometric interpretation. The vector $\mathbf{x}^*$ is orthogonal to all rows of the matrix it multiplies; for $\mathbf{x}^* \neq \mathbf{0}$ , that is possible only if the rows, considered as $n$ -vectors, do not span the full $n$ -dimensional space. In such a case, the rank of the matrix is less than its maximum possible value, $n$ . Conversely, if the rank is less than $n$ , it is always possible to find a vector that is orthogonal to all rows. It follows that a necessary and sufficient condition for observability is

$$
\operatorname{rank} \mathcal {O} = \operatorname{rank} \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {n - 1} \end{array} \right] = n. \tag {3.43}
$$

The matrix O, called the observability matrix, is the matrix on the left-hand side (LHS) of Equation 3.39.

Example 3.8 Verify that the system of Example 3.2 is unobservable for $y = x_{1} - x_{2}$ .

Solution The relevant matrices are

$$
A = \left[ \begin{array}{c c} - \frac {3}{2} & \frac {1}{2} \\ \frac {1}{2} & - \frac {3}{2} \end{array} \right] \quad C = \left[ \begin{array}{l l} 1 & - 1 \end{array} \right].
$$

Here, $n = 2$ , so the observability matrix is

$$
\mathcal {O} = \left[ \begin{array}{c} C \\ C A \end{array} \right] = \left[ \begin{array}{c c} 1 & - 1 \\ - 2 & 2 \end{array} \right].
$$

Because this matrix is square, the determinant is calculated to check for full rank. The determinant is zero, so the rank of the matrix is less than 2, and the system is unobservable.

Since

$$
\left[ \begin{array}{c c} 1 & - 1 \\ - 2 & 2 \end{array} \right] \left[ \begin{array}{l} a \\ a \end{array} \right] = \mathbf {0}
$$

the state $\begin{bmatrix} a \\ a \end{bmatrix}$ is unobservable, as expected from previous discussion.
