1. Implementing a PD controller will result in an impulsive control signal if the reference input is a step function because the discontinuous step input produces an infinite derivative in the error signal at t = 0.   
2. PD controllers must be used carefully because they greatly amplify the high-frequency component of a feedback signal (see the corresponding magnitude Bode diagram, Fig. 10.47). If noise is present in the feedback signal, it will be amplified by the PD controller.   
3. Adding a low-pass filter before a PD controller creates a lead controller, which consists of a zero/pole pair and alleviates the high-frequency (noise) problem.   
4. A lead controller is an approximation of the PD controller. Both controllers improve damping and reduce the settling time.

Example 10.13 shows that the lead controller does not add as much damping as the PD controller. The closedloop effect of the lead controller’s zero is magnified if the lead controller’s pole is placed farther to the left. In fact, if the pole of the lead controller is pushed too far left, then the low-pass filtering benefit is lost and the lead controller essentially becomes a PD controller (this effect is demonstrated in an end-of-chapter problem). On the other hand, if the lead controller’s zero and pole are too close together, they cancel each other and the lead controller has a diminished effect on the closed-loop response. A good rule-of-thumb is to make the lead controller’s denominator corner frequency 3–5 times greater than the numerator corner frequency. For example, the lead controller in Example 10.13

$$G _ {\mathrm{LF}} (s) = \frac {K (s + 3)}{s + 1 2}$$

provides a good trade-off between low-pass filtering and an active zero for damping. However, the lead controller

$$G _ {\mathrm{LF}} (s) = \frac {K (s + 3)}{s + 4}$$

will not provide good damping because the zero at s = −3 is nearly cancelled by the pole at s = −4. Finally, the lead controller

$$G _ {\mathrm{LF}} (s) = \frac {K (s + 3)}{s + 1 0 0}$$

will essentially act similar to a PD controller with a zero at s = −3 because the denominator corner frequency of 100 rad/s is much greater than the numerator corner frequency of 3 rad/s. This lead filter does not provide low-pass filtering.
