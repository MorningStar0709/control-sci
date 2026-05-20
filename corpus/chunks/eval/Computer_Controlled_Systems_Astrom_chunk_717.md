# Calculation of the Optimal Predictor

It follows from (12.17) that $F(q)$ is the quotient and $G(q)$ the remainder when dividing $q^{m-1}C(q)$ by $A(q)$ . The polynomials $F$ and $G$ can thus be determined by polynomial division. An explicit formula for the coefficients of the polynomials can also be given. Equating the coefficients of equal powers of $q$ in (12.17) gives the following equations:

$$
\begin{array}{l} c _ {1} = a _ {1} + f _ {1} \\ c _ {2} = a _ {2} + a _ {1} f _ {1} + f _ {2} \\ c _ {m - 1} = a _ {m - 1} + a _ {m - 2} f _ {1} + \dots + a _ {1} f _ {m - 2} + f _ {m - 1} \\ c _ {m} = a _ {m} + a _ {m - 1} f _ {1} + \dots + a _ {1} f _ {m - 1} + g _ {0} \\ c _ {m + 1} = a _ {m + 1} + a _ {m} f _ {1} + \dots + a _ {2} f _ {m - 1} + g _ {1} \\ c _ {n} = a _ {n} + a _ {n - 1} f _ {1} + \dots + a _ {n - m + 1} f _ {m - 1} + g _ {n - m} \\ 0 = a _ {n} f _ {1} + a _ {n - 1} f _ {2} + \dots + a _ {n - m + 2} f _ {m - 1} + g _ {n - m + 1} \\ 0 = a _ {n} f _ {m - 1} + g _ {n - 1} \\ \end{array}
$$

•
•
•

•
•
•

:

These equations are easy to solve recursively. Compare the solution of the Diophantine equation in Chapter 5.
