# Example 7.7 Predictive first-order-hold sampling of a double integrator

A double integrator has the transfer function $G(s) = 1/s^{2}$ . It follows from Table 2.1 that the zero-order-hold sampling of $1/s^{3}$ is

$$\frac {h ^ {3}}{6} \frac {z ^ {2} + 4 z + 1}{(z - 1) ^ {3}}$$

It then follows from Eq. (7.20) that

$$H (z) = \frac {h ^ {2}}{6} \frac {z ^ {2} + 4 z + 1}{(z - 1) ^ {2}}$$

Notice that in this case the orders of the numerator and denominator polynomials are the same. This is due to the predictive nature of the hold.
