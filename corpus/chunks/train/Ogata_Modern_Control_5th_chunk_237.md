$$
\begin{array}{c c c c c c c c c} s ^ {4} & & 1 & 3 & 5 \\ s ^ {3} & & 2 & 4 & 0 \\ & & & & \\ s ^ {2} & & 1 & 5 \\ s ^ {1} & & - 6 \\ s ^ {0} & & 5 \end{array} \left| \begin{array}{c c c c c} s ^ {4} & & 1 & 3 & 5 \\ s ^ {3} & & \mathcal {Z} & \mathcal {A} & \emptyset \\ & & 1 & 2 & 0 \\ s ^ {2} & & 1 & 5 \\ s ^ {1} & & - 3 \\ s ^ {0} & & 5 \end{array} \right. \text {   The   second   row   is   divided   by   2.   }
$$

In this example, the number of changes in sign of the coefficients in the first column is 2. This means that there are two roots with positive real parts. Note that the result is unchanged when the coefficients of any row are multiplied or divided by a positive number in order to simplify the computation.

Special Cases. If a first-column term in any row is zero, but the remaining terms are not zero or there is no remaining term, then the zero term is replaced by a very small positive number  and the rest of the array is evaluated. For example, consider the following equation:

$$s ^ {3} + 2 s ^ {2} + s + 2 = 0 \tag {5-62}$$

The array of coefficients is

$$
\begin{array}{c c c} s ^ {3} & 1 & 1 \\ s ^ {2} & 2 & 2 \\ s ^ {1} & 0 \approx \epsilon \\ s ^ {0} & 2 \end{array}
$$

If the sign of the coefficient above the zero () is the same as that below it, it indicates that there are a pair of imaginary roots. Actually, Equation (5–62) has two roots at s=; j.

If, however, the sign of the coefficient above the zero () is opposite that below it, it indicates that there is one sign change. For example, for the equation

$$s ^ {3} - 3 s + 2 = (s - 1) ^ {2} (s + 2) = 0$$

the array of coefficients is

$$
\begin{array}{l l} \text {One sign change:} & \left( \begin{array}{c c c} s ^ {3} & 1 & - 3 \\ s ^ {2} & 0 \approx \epsilon & 2 \\ s ^ {1} & - 3 - \frac {2}{\epsilon} \\ s ^ {0} & 2 \end{array} \right) \\ \text {One sign change:} & \end{array}
$$

There are two sign changes of the coefficients in the first column. So there are two roots in the right-half s plane. This agrees with the correct result indicated by the factored form of the polynomial equation.
