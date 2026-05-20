# Example 7.4 Ramp-invariant sampling of an integrator

Consider a system with the transfer function $G(s) = 1 / s$ . In this case we have $A = D = 0$ and $B = C = 1$ . Using (7.17) we get

$$
\begin{array}{l} \left( \begin{array}{c c c} \Phi & \Gamma & \Gamma_ {1} \end{array} \right) = \left( \begin{array}{l l l} 1 & 0 & 0 \end{array} \right) \exp \left(\left( \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right) h\right) \\ = \left(1 h \frac {1}{2} h ^ {2}\right) \\ \end{array}
$$

The pulse-transfer function becomes

$$H (z) = \frac {\frac {1}{2} z h + h - \frac {1}{2} h}{z - 1} = \frac {h}{2} \frac {z + 1}{z - 1}$$

This pulse-transfer function corresponds to the trapezoidal formula for computing an integral. Also notice that Tustin's transformation gives the same result in this case.
