# A Computational Procedure

Theorem 12.4 gives a convenient way to compute the LQG-control law for SISO systems, which can be described as follows.

1. Rewrite the model of the process and the disturbance in the standard form (12.5), where $C(z)$ is a stable polynomial. It may be necessary to use a spectral factorization to obtain this form.

2. Use a spectral factorization to calculate $P(z)$ . If the polynomials $A(z)$ and $B(z)$ have a stable common factor $A_2(z)$ , the calculations of the control law can be simplified by first factoring $A(z)$ and $B(z)$ as $A(z) = A_1(z)A_2(z)$ and $B(z) = B_1(z)A_2(z)$ . It follows from (12.45) that $A_2(z)$ also divides $P(z)$ . This polynomial can thus be written as $P(z) = P_1(z)A_2(z)$ , where $P_1(z)$ is given by

$$r P _ {1} (z) P _ {1} \left(z ^ {- 1}\right) = \rho A _ {1} (z) A _ {1} \left(z ^ {- 1}\right) + B _ {1} (z) B _ {1} \left(z ^ {- 1}\right)$$

The polynomial $P(z)$ is then equal to $P_{1}(z)A_{2}(z)$ , which is stable, because $A_{2}(z)$ was assumed stable. Equation (12.47) can also be divided by $A_{2}(z)$ to give

$$P _ {1} (z) C (z) = A _ {1} (z) R (z) + B _ {1} (z) S (z)$$

where $\deg R(z) = \deg S(z) = \deg C(z) = n$ , and $S(0) = 0$ .

3a. If there are no common factors between $A$ and $B$ and if $A(0) \neq 0$ then the controller is given by a unique solution to the Diophantine equation (12.47) such that $\deg R(z) = \deg S(z) = n$ , and $S(0) = 0$ .

3b. If there are stable common factors of $A$ and $B$ or if $A(0) = 0$ the solution is obtained from the Equation (12.49) or Diophantine equation (12.47), and (12.54).

The computational procedure shows that when there are no common factors between A and B and when $A(0) \neq 0$ then it is sufficient to solve only one Diophantine equation with the extra constraint $S(0) = 0$ to obtain a unique solution. In other cases it is necessary to solve the coupled equations (12.49). Theorem 12.4 is illustrated by two examples.
