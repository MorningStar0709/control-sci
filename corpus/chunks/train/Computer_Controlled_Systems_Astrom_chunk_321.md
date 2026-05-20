# The Characteristic Polynomial

It is convenient to describe the characteristic polynomial in terms of factors of first and second order, which are described in terms of their continuous-time equivalents. The discrete-time equivalent of a first-order system characterized by $A(s) = s + \alpha$ is

$$\mathrm{A} _ {1} (z) = z - a$$

where $a = e^{-\alpha h}$ , and a second-order system $A(s) = s^2 + 2\zeta \omega_0 s + \omega_0^2$ is equivalent to

$$\mathrm{A} _ {2} (z) = z ^ {2} + a _ {1} z + a _ {2}$$

where $a_1 = -2e^{-\zeta \omega_0h}\cos (\omega_0h\sqrt{1 - \zeta^2})$ , and $a_2 = e^{-2\zeta \omega_0h}$ . A common choice is then

$$\mathrm{A} _ {\mathrm{c}} (z) = z ^ {d} \mathrm{A} _ {1} (z) \mathrm{A} _ {2} (z)$$

In this case the system has three dominating poles and the remaining poles are positioned at the origin.

It is practical to use the continuous-time parameters $\alpha$ , $\omega_{0}$ , and $\zeta$ instead of the equivalent discrete-time parameters $a$ , $a_{1}$ , and $a_{2}$ . The designer can then use the intuition developed for continuous-time systems and it is a simple task to compute the discrete-time parameters.

The poles of the closed-loop characteristic polynomial are normally chosen so that the dominating poles are of the same order of magnitude as the open-loop poles. It follows from the analysis of sensitivity to modeling errors that the closed-loop system will be very sensitive to parameter variations if the closed-loop bandwidth is chosen much higher than the bandwidth of the open-loop system. Compare with Fig. 5.6. The observer poles are often chosen to be a little faster than the controller poles.
