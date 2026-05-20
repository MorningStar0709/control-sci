# The Hold Circuit

The hold circuit can be represented as an integrator that is automatically reset to zero after one sampling period. Such a system has the transfer function

$$G _ {\mathrm{zoh}} (s) = \frac {1}{s} \left(1 - e ^ {- s h}\right) \tag {7.27}$$

The impulse response of the transfer function 1/s is a unit step and the impulse response of $(1/s)\exp(-sh)$ is a unit step that is delayed h time units. Subtraction of these impulse responses gives the impulse response as a pulse of unit height and duration h.

Notice that the steady-state gain of the hold circuit is $G_{\mathrm{zoh}}(0) = h$ . Section 7.3 shows that ideal sampling could be said to have a gain 1/h. The combination of a sampler with a hold circuit thus has unit steady-state gain. For very fast sampling, the sample-and-hold circuit thus acts as a continuous-time system with unit transfer function.

The idealized model of a sample-and-hold circuit is thus obtained by combining a sampler with impulse modulation given by $(7.25)$ and $(7.26)$ with a hold circuit given by $(7.27)$ . A block-diagram representation of the system is shown in Fig. 7.19. Because the impulse modulator is a periodic system it follows that the sample-and-hold circuit is also a periodic system.
