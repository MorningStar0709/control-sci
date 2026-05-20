# Causality Conditions

It follows from the analysis that there may be infinitely many solutions to the Diophantine equation (5.4). For the Diophantine equations that appear when solving the pole-placement problem, it is natural to introduce some constraints on the solution. The degrees of the polynomials $S(z)$ and $T(z)$ must be less than or equal to the degree of $R(z)$ . If this is not the case the control signal at time k will depend on values of the measured signal and the command signal at times larger than k. We call this the causality condition.

If the time to calculate the control signal in the computer is only a small fraction of the sampling period, it is natural to neglect the time to compute the control signal. The causality constraint then becomes

$$\deg R = \deg T = \deg S \tag {5.19}$$

If the computation time is one sampling period we have

$$\deg R = \deg T + 1 = \deg S + 1$$

The constraint of $(5.19)$ is normally used as a standard case. Possible computational delays can be included in the process model instead of in the controller; compare with Sec. 2.3.
