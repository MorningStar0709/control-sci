# Calculating the Control Law

The Diophantine equation (5.43) can be solved by Euclid's algorithm, as was discussed previously. It can, however, also be solved in the following way. Assume that we have a solution $R^{0}$ and $S^{0}$ to the equation

$$A R ^ {0} + B S ^ {0} = A _ {c l} ^ {0} \tag {5.46}$$

and the minimum-degree solution U and V to the equation

$$A U + B V = 0 \tag {5.47}$$

Such solutions are typically obtained from the solution of a simple design problem. We introduce the polynomials R and S defined by

$$
\begin{array}{l} R = X R ^ {0} + Y U \\ \text {   S   } = X \tilde {\sigma} ^ {0} - \text {   III   } \end{array} \tag {5.48}
S = X S ^ {0} + Y V
$$

where $X$ is a stable monic polynomial; then

$$A R + B S = X A _ {c l} ^ {0}$$

If polynomials $A_{cl}^{0}$ and X are chosen so that $A_{cl} = A_{cl}^{0}X$ , we thus find that polynomials R and S given by (5.48) satisfy (5.43). To satisfy the compatibility conditions X should have $\deg R_{d} + \deg S_{d}$ . Polynomial Y will generically have $\deg R_{d} + \deg S_{d} - 1$ . To determine polynomial Y we impose the conditions that $R_{d}$ divides R and that $S_{d}$ divides S. This gives the following linear equations for determining the coefficients of polynomial Y.

$$
\begin{array}{l} X \left(z _ {i}\right) R ^ {0} \left(z _ {i}\right) - Y \left(z _ {i}\right) U \left(z _ {i}\right) = 0 \text {for} R _ {d} \left(z _ {i}\right) = 0 \\ \text {if} (z _ {i}) \in^ {0} (z _ {i}) = Y (z _ {i}) U (z _ {i}) = 0, \text {for} Z (z _ {i}) = 0 \end{array} \tag {5.49}
X \left(z _ {i}\right) S ^ {0} \left(z _ {i}\right) + Y \left(z _ {i}\right) U \left(z _ {i}\right) = 0 \text { for } S _ {d} \left(z _ {i}\right) = 0
$$

We illustrate the procedure by two examples.
