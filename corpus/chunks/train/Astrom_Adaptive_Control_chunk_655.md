# Relations to Ordinary Linear Equations

By equating coefficients of equal order, the Diophantine equation given by Eq. (11.11) can be written as a set of linear equations:

$$
\left( \begin{array}{c c c c c c c c} 1 & 0 & \dots & 0 & b _ {0} & 0 & \dots & 0 \\ a _ {1} & 1 & \ddots & \vdots & b _ {1} & b _ {0} & \ddots & \vdots \\ a _ {2} & a _ {1} & \ddots & 0 & b _ {2} & b _ {1} & \ddots & 0 \\ \vdots & \vdots & \ddots & 1 & \vdots & \vdots & \ddots & b _ {0} \\ a _ {n} & \vdots & & a _ {1} & b _ {n} & \vdots & & b _ {1} \\ 0 & a _ {n} & & \vdots & 0 & b _ {n} & & \vdots \\ \vdots & \ddots & \ddots & & \vdots & \ddots & \ddots \\ 0 & \dots & 0 & a _ {n} & 0 & \dots & 0 & b _ {n} \end{array} \right) \underbrace {\left( \begin{array}{c} r _ {1} \\ \vdots \\ r _ {k} \\ s _ {0} \\ \vdots \\ s _ {l} \end{array} \right)} _ {k \text {columns}} = \left( \begin{array}{c} a _ {c 1} - a _ {1} \\ \vdots \\ a _ {c n} - a _ {n} \\ a _ {c n + 1} \\ \vdots \\ a _ {c k + l + 1} \end{array} \right) \tag {11.14}
$$

The matrix on the left-hand side is called the Sylvester matrix; it occurs frequently in applied mathematics. It has the property that it is nonsingular if and only if the polynomials A and B do not have any common factors. If there are no common factors, a unique solution to Eq. (11.14) exists. Notice, however, the nonuniqueness with respect to the orders of R and S. Different choices of k and l will give different R and S, as discussed above. The solution to Eq. (11.14) can be obtained by Gaussian elimination. This method does not use the special structure of the Sylvester matrix.
