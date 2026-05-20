Equation (11.4) shows that the free response consists of two damped exponential functions and a damped sinusoidal function. Root $r _ { 1 } = - 6 7 . 5 9 5 8$ is the “fastest” root, as its exponential function decays to zero in about 0.06 s, and therefore its contribution to the total response is extremely short-lived. Root $r _ { 2 } = - 7 . 2 6 7 5$ corresponds to an exponential function that decays to zero in about 0.55 s. The complex roots are the “slowest” roots because their exponential function decays to zero in about 1.09 s. Therefore, real root $r _ { 2 }$ and complex roots $r _ { 3 }$ and $r _ { 4 }$ are the dominant roots.

We can construct the fourth-order characteristic equation from the four eigenvalues or roots:

$$(r + 6 7. 5 9 5 8) (r + 7. 2 6 7 5) (r + 3. 6 7 3 3 - j 1 0. 5 1 8 9) (r + 3. 6 7 3 3 + j 1 0. 5 1 8 9) = 0 \tag {11.5}$$

Therefore, the underdamped part of the characteristic equation can be determined by multiplying the last two (or complex) terms of Eq. (11.5)

$$r ^ {2} + 7. 3 4 6 7 r + 1 2 4. 1 4 0 3 = 0 \tag {11.6}$$

The undamped natural frequency is $\omega _ { n } = { \sqrt { 1 2 4 . 1 4 0 3 } } = 1 1 . 1 4 \mathrm { r a d / s }$ and the damping ratio is $\zeta = 7 . 3 4 6 7 / ( 2 \omega _ { n } ) = 0 . 3 2 9 7$ . Because the complex roots are dominant roots, we expect the free response of the seat-suspension system to exhibit underdamped response characteristics.

Next, we use Simulink to determine the seat-suspension system’s response to inputs, and we will first consider a “spike” input for the cabin floor displacement $z _ { 0 } ( t )$ . We assume that the vehicle passes over a bump, which causes a sudden displacement of the cabin floor. The floor displacement $z _ { 0 } ( t )$ is modeled by a “triangular pulse” with a peak displacement of 0.03 m (3 cm) and a constant vertical “bump $\mathrm { r a t e } ^ { \mathrm { * } }$ of $\dot { z } _ { 0 } = 5 . 4$ m/s (rising). The floor displacement is a symmetrical triangular pulse, and therefore the constant “bump rate” is $\dot { z } _ { 0 } = - 5 . 4$ m/s (descending) after the pulse reaches its peak value of 0.03 m. Hence, the duration of half of the triangular pulse is $\Delta t = z _ { 0 \mathrm { m a x } } / \dot { z } _ { 0 } = 0 . 0 0 5 6 \mathrm { s }$ or 5.6 ms. Because the total duration of the triangular pulse is about 11 ms, we can consider the “spike” input to essentially be an impulse input.
