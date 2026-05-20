# Example 5.1 Control of a double integrator

For the double integrator we have

$$
\begin{array}{l} A (z) = (z - 1) ^ {2} \\ B (z) = \frac {h ^ {2}}{2} (z + 1) \\ \end{array}
$$

and the Diophantine equation (5.4) becomes

$$(z ^ {2} - 2 z + 1) R (z) + \frac {h ^ {2}}{2} (z + 1) S (z) = A _ {c l} (z)$$

The closed-loop characteristic polynomial $A_{cl}$ is a design parameter. Both its degree and its parameters will be selected to achieve the design goals. It is natural to look for as simple controllers as possible. This means that we will search for polynomials $R(z)$ and $S(z)$ of the lowest order that satisfies the Diophantine equation. The simplest case is $R(z) = 1$ and $S(z) = s_{0}$ , that is, a proportional controller. This gives the equation

$$z ^ {2} - 2 z + 1 + \frac {s _ {0} h ^ {2}}{2} (z + 1) = A _ {c l} (z)$$

which cannot be solved for an arbitrary $A_{cl}(z)$ of second order. With a first-order controller we have $R(z) = z + r_{1}$ and $S(z) = s_{0}z + s_{1}$ , which gives

$$(z ^ {2} - 2 z + 1) (z + r _ {1}) + \frac {h ^ {2}}{2} (z + 1) (s _ {0} z + s _ {1}) = A _ {c l} (z)$$

Hence

$$z ^ {3} + \left(r _ {1} + \frac {h ^ {2}}{2} s _ {0} - 2\right) z ^ {2} + \left(1 - 2 r _ {1} + \frac {h ^ {2}}{2} (s _ {0} + s _ {1})\right) z + r _ {1} + s _ {1} \frac {h ^ {2}}{2} = A _ {c l} (z)$$

and we find that it is possible to select the controller coefficients $r_{1}$ , $s_{0}$ , and $s_{1}$ to obtain an arbitrary polynomial $A_{cl}(z)$ of third degree. Choosing

$$A _ {c l} (z) = z ^ {3} + p _ {1} z ^ {2} + p _ {2} z + p _ {3}$$

and identifying coefficients of powers of equal degree we find that

$$
\begin{array}{l} r _ {1} + \frac {h ^ {2}}{2} s _ {0} = p _ {1} + 2 \\ - 2 r _ {1} + \frac {h ^ {2}}{2} (s _ {0} + s _ {1}) = p _ {2} - 1 \\ r _ {1} + s _ {1} \frac {h ^ {2}}{2} = p _ {3} \\ \end{array}
$$

This equation has the solution

$$
\begin{array}{l} r _ {1} = \frac {3 + p _ {1} + p _ {2} - p _ {3}}{4} \\ s _ {0} = \frac {5 + 3 p _ {1} + p _ {2} - p _ {3}}{2 h ^ {2}} \\ s _ {1} = - \frac {3 + p _ {1} - p _ {2} - 3 p _ {3}}{2 h ^ {2}} \\ \end{array}
$$

It now remains to determine the polynomial $T(z)$ . For this purpose we will factor the closed-loop characteristic polynomial as $A_{cl}(z) = A_o(z)A_c(z)$ . The closed-loop characteristic polynomial $A_{cl}(z)$ is of third order. Because a third-order polynomial always has a real root we will select this to correspond with the observer polynomial $A_o(z)$ and we have $T(z) = t_0A_o(z)$ , where $t_0 = A(1)/B(1)$ .
