Using Eq. (7.64) and coefficients $a _ { 1 } = b / m$ and $a _ { 0 } = k / m$ , we see that the damping ratio is

$$\zeta = \frac {b}{2 \sqrt {k m}}$$

Therefore, for a mechanical system, damping ratio is the system’s actual damping coefficient (viscous friction b) divided by the critical damping coefficient $( 2 \sqrt { k m } )$ . This result makes intuitive sense: if the viscous friction coefficient b is very “small,” very little friction is present, and the valve mass will exhibit oscillations during the transient response. Conversely, if b is very “large,” then the friction force will inhibit oscillations, and the transient response will show an exponential decay to steady state.

Note that when coefficient $a _ { 1 } = 0$ , the two roots are imaginary numbers and the damping ratio $\zeta = 0$ . Consequently, the free response is an undamped sinusoid with constant amplitude. The frequency of oscillation for the case of no damping is called the undamped natural frequency $\omega _ { n }$ , and it is the magnitude of the two imaginary roots, which can be computed from Eq. (7.63) with $a _ { 1 } = 0$

$$\text { Undamped natural frequency: } \quad \omega_ {n} = \sqrt {a _ {0}} (\mathrm{rad/s}) \tag {7.65}$$

For the mass–spring–damper mechanical system, coefficient $a _ { 0 } = k / m .$ , and therefore the undamped natural frequency is $\omega _ { n } = \sqrt { k / m } \mathrm { r a d / s }$ . This result shows that increasing the spring constant k for a frictionless massspring system with a fixed mass m will increase the vibration frequency, which again makes intuitive sense.

We can replace the coefficients $a _ { 0 }$ and $a _ { 1 }$ in the general second-order I/O equation (7.62) with damping ratio and undamped natural frequency: using Eq. (7.65) we see that coefficient $a _ { 0 } = \omega _ { n } ^ { 2 }$ , and Eq. (7.64) shows that $a _ { 1 } = 2 \zeta \sqrt { a _ { 0 } } = 2 \zeta \omega _ { n }$ . Therefore, our general second-order I/O equation (7.62) can be written as

$$\ddot {y} + 2 \zeta \omega_ {n} \dot {y} + \omega_ {n} ^ {2} y = b _ {0} u (t) \tag {7.66}$$
