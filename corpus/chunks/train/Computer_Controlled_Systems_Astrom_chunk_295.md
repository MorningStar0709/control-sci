# ALGORITHM 5.2 THE DIOPHANTINE EQUATION

Step 1. Determine the greatest common divisor G of A and B and the associated polynomials X, Y, U, and V using the extended Euclidean algorithm. If G does not divide C the problem has no solution.

Step 2. If $G$ divides $C$ a particular solution is given by

$$X _ {0} = X C \mathrm{div} GY _ {0} = Y C \text { div } G$$

and the general solution is given by

$$
\begin{array}{l} \boldsymbol {X} = \boldsymbol {X} _ {0} + \boldsymbol {Q} \boldsymbol {U} \\ \boldsymbol {Y} = \boldsymbol {Y} _ {0} - \boldsymbol {Q} \boldsymbol {U} \end{array} \tag {5.18}
Y = Y _ {0} - Q V
$$

where Q is an arbitrary polynomial.

COROLLARY 5.1 UNIQUE SOLUTION There are unique solutions to (5.9) such that $\deg X < \deg B$ or $\deg Y < \deg A$ .

These solutions with $\deg X < \deg B$ is obtained from the general solution given by Eq. (5.18) by choosing $Q = -X_0$ div $U$ .
