# Relations to Linear Matrix Equations

The Diophantine equation can also be solved using matrix calculations. Assuming that the degrees of the polynomials are known, introducing the unknown coefficients of the polynomials as variables, and identifying coefficients of equal powers of z, we obtain a linear equation that can be solved in the usual manner. Consider, for example, Eq. (5.9). Assume that the degrees of the polynomials are $\deg A(z) = \deg B(z) = n$ and $\deg X(z) = \deg Y(z) = n - 1$ . The following

linear equations are then obtained.

$$
\left( \begin{array}{c c c c c c c c c c} a _ {0} & 0 & 0 & \dots & 0 & b _ {0} & 0 & 0 & \dots & 0 \\ a _ {1} & a _ {0} & 0 & \dots & 0 & b _ {1} & b _ {0} & 0 & \dots & 0 \\ a _ {2} & a _ {1} & a _ {0} & \dots & 0 & b _ {2} & b _ {1} & b _ {0} & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ a _ {n} & a _ {n - 1} & a _ {n - 2} & \dots & a _ {0} & b _ {n} & b _ {n - 1} & b _ {n - 2} & \dots & b _ {0} \\ 0 & a _ {n} & a _ {n - 1} & \dots & a _ {1} & 0 & b _ {n} & b _ {n - 1} & \dots & b _ {1} \\ 0 & 0 & a _ {n} & \dots & a _ {2} & 0 & 0 & b _ {n} & \dots & b _ {2} \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \dots & a _ {n} & 0 & 0 & 0 & \dots & b _ {n} \end{array} \right) \left( \begin{array}{c} x _ {0} \\ \vdots \\ x _ {n - 1} \\ y _ {0} \\ \vdots \\ y _ {n - 1} \end{array} \right) = \left( \begin{array}{c} c _ {0} \\ c _ {1} \\ c _ {3} \\ \vdots \\ c _ {n} \\ c _ {n + 1} \\ c _ {n + 2} \\ \vdots \\ c _ {2 n - 1} \end{array} \right)
$$

The matrix on the left-hand side, which is called the Sylvester matrix, occurs frequently in applied mathematics. It has the property that it is nonsingular if and only if the polynomials A and B do not have any common factors. Compare with Theorem 5.1. Notice, however, the nonuniqueness with respect to the orders of X and Y. Different choices of the orders of the polynomials give different solutions X and Y, as discussed before.

The solution to the preceding linear equation can be obtained by Gaussian elimination. This method does not use the special structure of the Sylvester matrix. The polynomial methods based on the extended Euclidean algorithm are faster and more efficient because they exploit the structure of the problem.
