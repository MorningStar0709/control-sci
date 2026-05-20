# Example 5.2 Controller with an integral action for the double integrator

Consider control of the double integrator where it is desired to have a controller with integral action. This means that the polynomial $R(z)$ must have z - 1 as a factor. Using the same arguments as in Example 5.1 we find that the simplest controller of second order with an integrator is

$$R (z) = (z - 1) (z + r _ {1})S (z) = s _ {0} z ^ {2} + s _ {1} z + s _ {2}$$

Inserting this into the Diophantine equation (5.4) we obtain

$$z ^ {4} + (r _ {1} - 3) z ^ {3} + \left(3 - 3 r _ {1} + \frac {h ^ {2}}{2} s _ {0}\right) z ^ {2} + \left(1 + 3 r _ {1} + \frac {h ^ {2}}{2} s _ {1}\right) z + r _ {1} + \frac {h ^ {2}}{2} = A _ {c l} (z)$$

The closed-loop system is of fourth order and we have four parameters $r_1, s_0, s_1$ , and $s_2$ to determine.
