# Solving the Diophantine Equation

By using the extended Euclidean algorithm it is now straightforward to solve the Diophantine equation

$$A R + B S = A _ {c} \tag {11.11}$$

This is done as follows: Determine the greatest common divisor G and the associated polynomials X, Y, U, and V using the extended Euclidean algorithm. To have a solution to Eq. (11.11), G must divide $A_{c}$ . A particular solution is given by

$$R ^ {0} = X A _ {c} \operatorname{div} G \tag {11.12}S ^ {0} = Y A _ {c} \operatorname{div} G$$

and the general solution is

$$
\begin{array}{l} R = R ^ {0} + Q U \\ \tilde {C} = C ^ {0} - Q U \end{array} \tag {11.13}
S = S ^ {0} + Q V
$$

where Q is an arbitrary polynomial. The minimum-degree solution is obtained by choosing $Q = -S^{0}$ div V. This implies that $S = S^{0} \mod V$ .
