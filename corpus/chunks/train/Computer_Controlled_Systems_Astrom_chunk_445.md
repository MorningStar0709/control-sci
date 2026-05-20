# Example 7.8 Pole-placement design of a double integrator

In Example 7.7 we derived the pulse-transfer function for a double integrator under predictive first-order-hold sampling. It follows from this example that the system is characterized by

$$
\begin{array}{l} A (z) = (z - 1) ^ {2} \\ B (z) = \frac {h ^ {2}}{6} (z ^ {2} + 4 z + 1) \\ \end{array}
$$

Assuming that a controller with integral action is desired we find that the Diophantine equation (7.23) becomes

$$(z - 1) ^ {3} \bar {R} (z) + \frac {h ^ {2}}{6} (z ^ {2} + 4 z + 1) S (z) = A _ {c!} (z)$$

where $R(z) = (z - 1)\bar{R}(z)$ . The minimum-degree solution of this equation has the property $\deg S(z) = 2$ . It then follows from the order condition (7.22) that $\deg R(z) = 3$ and consequently that $\deg \bar{R}(z) = 2$ . The minimum-degree solution thus gives a closed-loop system of order five. The previous Diophantine equation becomes

$$(z - 1) ^ {3} (z ^ {2} + r _ {1} z + r _ {2}) + \frac {h ^ {2}}{6} (z ^ {2} + 4 z + 1) (s _ {0} z ^ {2} + s _ {1} z + s _ {2}) = A _ {\epsilon l} (z)$$

The solution of this equation was discussed in Sec. 5.3.
