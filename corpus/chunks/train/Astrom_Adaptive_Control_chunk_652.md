# 11.4 SOLVING THE DIOPHANTINE EQUATION

Several of the design methods discussed earlier involve the solution of a Diophantine equation

$$A R + B S = A _ {c} \tag {11.6}$$

Efficient methods for solving this equation are needed. The equation is linear in the polynomials R and S. A solution always exists if A and B are relatively prime. However, the equation has many solutions. This is easily seen: If $R^{0}$ and $S^{0}$ are solutions, then

$$
\begin{array}{l} R = R ^ {0} + B Q \\ S = S ^ {0} - A Q \\ \end{array}
$$

are also solutions, where Q is an arbitrary polynomial. A particular solution can be specified in several different ways. Since a controller must be causal, the condition $\deg S \leq \deg R$ must hold. This condition will restrict the number of solutions significantly. An efficient way to solve the equation is to use a classical algorithm of Euclid.
