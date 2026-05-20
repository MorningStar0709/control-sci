# Autopilot Design

An autopilot has two main tasks: steady-state course keeping and turning. Minimization of drag induced by the steering is the important factor in course keeping, and steering precision is the important factor in turning. It is therefore natural to have a dual-mode operation. These two modes are described in the text that follows, together with the basic autopilot functions.

The influence of variations in the speed of the ship is handled by gain scheduling. The other disturbances are taken care of by feedback and adaptation. Implementation of the gain scheduling is discussed in Section 9.5. It requires a measurement of the forward velocity of the ship. If disturbances are regarded as stochastic processes, steady-state course keeping can be described as a linear quadratic Gaussian problem. It is then natural to estimate an ARMAX model (Eq. 2.38). The particular process model used is

$$
\begin{array}{l} \Delta \psi (t) - a \Delta \psi (t - h) = b _ {1} \delta (t - h) + b _ {2} \delta (t - 2 h) + b _ {3} \delta (t - 3 h) \\ + e (t) + c _ {1} e (t - h) + c _ {2} e (t - 2 h) \tag {12.4} \\ \end{array}
$$

This model is built on Nomoto's approximation (compare Section 9.5). The additional b term was introduced to allow additional dynamics to be captured as an increased time delay. The difference occurs because there is a pure integration in the model from rate of turn to heading angle. A control law that minimizes the criterion of Eq. (12.3) is then computed by using the certainty equivalence principle. This approach requires the solution of a Riccati equation, which can be done analytically in the particular case. A straightforward minimum-variance control law was used in some early experiments. This was replaced by the LQG control law described previously, because there were significant advantages at short sampling intervals, which could not be used with the minimum-variance control law. The sampling interval in the model is set during commissioning.
