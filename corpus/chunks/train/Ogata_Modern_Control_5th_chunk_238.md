If all the coefficients in any derived row are zero, it indicates that there are roots of equal magnitude lying radially opposite in the s plane—that is, two real roots with equal magnitudes and opposite signs and/or two conjugate imaginary roots. In such a case, the evaluation of the rest of the array can be continued by forming an auxiliary polynomial with the coefficients of the last row and by using the coefficients of the derivative of this polynomial in the next row. Such roots with equal magnitudes and lying radially opposite in the s plane can be found by solving the auxiliary polynomial, which is always even. For a 2n-degree auxiliary polynomial, there are n pairs of equal and opposite roots. For example, consider the following equation:

$$s ^ {5} + 2 s ^ {4} + 2 4 s ^ {3} + 4 8 s ^ {2} - 2 5 s - 5 0 = 0$$

The array of coefficients is

$$
\begin{array}{l} s ^ {5} \quad 1 \quad 2 4 \quad - 2 5 \\ s ^ {4} \quad 2 \quad 4 8 \quad - 5 0 \quad \leftarrow \text { Auxiliary   polynomial } P (s) \\ s ^ {3} \quad 0 \quad 0 \\ \end{array}
$$

The terms in the $s ^ { 3 }$ row are all zero. (Note that such a case occurs only in an oddnumbered row.) The auxiliary polynomial is then formed from the coefficients of the $s ^ { 4 }$ row. The auxiliary polynomial $P ( s )$ is

$$P (s) = 2 s ^ {4} + 4 8 s ^ {2} - 5 0$$

which indicates that there are two pairs of roots of equal magnitude and opposite sign (that is, two real roots with the same magnitude but opposite signs or two complexconjugate roots on the imaginary axis).These pairs are obtained by solving the auxiliary polynomial equation $P ( s ) = 0$ . The derivative of P(s) with respect to s is

$$\frac {d P (s)}{d s} = 8 s ^ {3} + 9 6 s$$

The terms in the $s ^ { 3 }$ row are replaced by the coefficients of the last equation—that is, 8 and 96. The array of coefficients then becomes

$$
\begin{array}{c c c c c} s ^ {5} & 1 & 2 4 & - 2 5 \\ s ^ {4} & 2 & 4 8 & - 5 0 \\ s ^ {3} & 8 & 9 6 & \leftarrow \text {Coefficients of} d P (s) / d s \\ s ^ {2} & 2 4 & - 5 0 \\ s ^ {1} & 1 1 2. 7 & 0 \\ s ^ {0} & - 5 0 \end{array}
$$

We see that there is one change in sign in the first column of the new array.Thus, the original equation has one root with a positive real part. By solving for roots of the auxiliary polynomial equation,

$$2 s ^ {4} + 4 8 s ^ {2} - 5 0 = 0$$

we obtain

$$s ^ {2} = 1, \quad s ^ {2} = - 2 5$$

or

$$s = \pm 1, \quad s = \pm j 5$$

These two pairs of roots of $P ( s )$ are a part of the roots of the original equation. As a matter of fact, the original equation can be written in factored form as follows:
