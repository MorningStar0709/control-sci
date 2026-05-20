If the sensor noise has high spectral content in the system passband, its contribution to the error may be dominant. In some cases, it may even be necessary to reduce the design bandwidth to cut down the effect of the sensor noise. One conclusion is that, for good control, sensor noise should be low within the design bandwidth. Another is that the bandwidth of T should be no greater than necessary to meet specifications on set-point response and disturbance attenuation; it is desirable that $|T(j\omega)|$ be attenuated, or rolled off, outside the passband. Often, a rolloff rate, in decibels per decade, specifies the (negative) slope at the log magnitude of T outside the passband.

To address the actuator questions, we write, from Figure 4.20,

$$y (s) = P u (s) + d (s)u (s) = P ^ {- 1} (y - d).$$

Using Equation 4.46,

$$
\begin{array}{l} u (s) = P ^ {- 1} \left[ T y _ {d} + (S - 1) d - T v \right] \\ = P ^ {- 1} T \left(y _ {d} - d - v\right). (4.48) \\ u (s) = P ^ {- 1} \left[ T y _ {d} + (S - 1) d - T v \right] \\ = P ^ {- 1} T \left(y _ {d} - d - v\right). (4.48) \\ \end{array}
$$

The reasoning developed in the study of open-loop control also holds here. If $T(j\omega) \approx 1$ at frequencies beyond $\omega_{1}$ , the natural bandwidth of P, then $|P(j\omega)|$ will decrease well below 1 while $|P^{-1}(j\omega)T(j\omega)|$ will be large for $\omega > \omega_{1}$ , and the actuator may not have enough bandwidth to provide the required power. In some cases, the actuator may be damaged.
