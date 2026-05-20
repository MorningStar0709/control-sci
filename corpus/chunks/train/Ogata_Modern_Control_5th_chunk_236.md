The evaluation of the b’s is continued until the remaining ones are all zero. The same pattern of cross-multiplying the coefficients of the two previous rows is followed in evaluating the $c ^ { \prime } \mathrm { s } , d ^ { \prime } \mathrm { s } , e ^ { \prime } \mathrm { s } ,$ and so on. That is,

$$c _ {1} = \frac {b _ {1} a _ {3} - a _ {1} b _ {2}}{b _ {1}}c _ {2} = \frac {b _ {1} a _ {5} - a _ {1} b _ {3}}{b _ {1}}c _ {3} = \frac {b _ {1} a _ {7} - a _ {1} b _ {4}}{b _ {1}}$$

and

$$d _ {1} = \frac {c _ {1} b _ {2} - b _ {1} c _ {2}}{c _ {1}}d _ {2} = \frac {c _ {1} b _ {3} - b _ {1} c _ {3}}{c _ {1}}$$

This process is continued until the nth row has been completed. The complete array of coefficients is triangular. Note that in developing the array an entire row may be divided or multiplied by a positive number in order to simplify the subsequent numerical calculation without altering the stability conclusion.

Routh’s stability criterion states that the number of roots of Equation (5–61) with positive real parts is equal to the number of changes in sign of the coefficients of the first column of the array. It should be noted that the exact values of the terms in the first column need not be known; instead, only the signs are needed. The necessary and sufficient condition that all roots of Equation (5–61) lie in the left-half s plane is that all the coefficients of Equation (5–61) be positive and all terms in the first column of the array have positive signs.

EXAMPLE 5–11 Let us apply Routh’s stability criterion to the following third-order polynomial:

$$a _ {0} s ^ {3} + a _ {1} s ^ {2} + a _ {2} s + a _ {3} = 0$$

where all the coefficients are positive numbers. The array of coefficients becomes

$$
\begin{array}{l} s ^ {3} \qquad a _ {0} \qquad a _ {2} \\ s ^ {2} \qquad a _ {1} \qquad a _ {3} \\ s ^ {1} \quad \frac {a _ {1} a _ {2} - a _ {0} a _ {3}}{a _ {1}} \\ s ^ {0} \qquad a _ {3} \\ \end{array}
$$

The condition that all roots have negative real parts is given by

$$a _ {1} a _ {2} > a _ {0} a _ {3}$$

EXAMPLE 5–12 Consider the following polynomial:

$$s ^ {4} + 2 s ^ {3} + 3 s ^ {2} + 4 s + 5 = 0$$

Let us follow the procedure just presented and construct the array of coefficients. (The first two rows can be obtained directly from the given polynomial. The remaining terms are obtained from these. If any coefficients are missing, they may be replaced by zeros in the array.)
