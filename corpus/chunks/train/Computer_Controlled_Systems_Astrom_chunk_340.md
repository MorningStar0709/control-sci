# Specifications

The desired response is characterized by the continuous-time characteristic equation

$$s ^ {2} + 2 \zeta \omega s + \omega^ {2} = 0$$

The sampled-data form of this polynomial is $A_{c}(z)$ . Because the pulse-transfer function has a zero at -1, no zero cancellation is allowed. This implies that $B^{+} = 1$ and $B_{m} = const \cdot B$ . It is specified that the controller should have integral action. This implies that the observer polynomial at least should be of second order. We choose it as the discrete-time equivalent of

$$s ^ {2} + 2 \zeta_ {\mathrm{obs}} \omega_ {\mathrm{obs}} s + \omega_ {\mathrm{obs}} ^ {2}$$
