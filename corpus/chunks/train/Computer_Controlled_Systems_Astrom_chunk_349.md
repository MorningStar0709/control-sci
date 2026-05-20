# Specifications

It is desired to obtain a closed-loop system with a good response to command signals. The response should be similar to a second-order system with $\omega_{c}=0.5$ rad/s and a relative damping $\zeta_{c}=0.7$ . These specifications were discussed in Sec. 4.7. The system composed of the robot joint and the antialias filter is of fifth order. The polynomial $A_{c}$ is thus also of fifth order. Three of the poles are chosen as the discrete-time equivalents of

$$\left(s ^ {2} + 2 \zeta_ {c} \omega_ {c} s + \omega_ {c} ^ {2}\right) \left(s + \alpha \omega_ {c}\right)$$

The remaining poles are chosen as the discrete-time equivalents of the poles of the antialiasing filter.
