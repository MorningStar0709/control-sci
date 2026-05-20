# Example 12.6 Minimum-variance control

Consider a system given by (12.5), where

$$
\begin{array}{l} A (q) = q ^ {3} - 1. 7 q ^ {2} + 0. 7 q \\ B (q) = q + 0. 5 \\ C (q) = q ^ {3} - 0. 9 q ^ {2} \\ \end{array}
$$

The pole excess is $d = 2$ . Division of $q^{d-1}C(q)$ by $A(q)$ gives the quotient

$$F (q) = q + 0. 8$$

and the remainder

$$G (q) = 0. 6 6 q ^ {2} - 0. 5 6 q$$

The minimum-variance control law is thus

$$u (k) = - \frac {q (0 . 6 6 q - 0 . 5 6)}{(q + 0 . 5) (q + 0 . 8)} y (k)$$

The variance of the output when the optimal controller is used is

$$\mathbf {E} \mathbf {y} ^ {2} = 1 + (0. 8) ^ {2} = 1. 6 4$$
