6.36 In Problem 6.23, a lead-lag compensator was designed for the system of Problem 6.1. Modify the design to obtain a 2-DOF system such that (i) both the forward-path and feedback-path compensators are proper or strictly proper and (ii) the frequency response to the reference input has a bandwidth of 3 rad/s and a peak response of no more than 3 db.

6.37 In Problem 6.24, a lead-lag compensator was designed for the system of Problem 6.2. Repeat Problem 6.36 for this system, but with a bandwidth of 6 rad/s.

6.38 dc servo, simplified model Modify the design of Problem 6.25 to a 2-DOF system such that the voltage input required by the response to a reference step of 2 rad does not exceed 3 V.

6.39 Chemical reactor In a chemical reactor, it is often desirable to avoid excessive speed in the response to a step change in the set point. Modify the design of Problem 6.27 to a 2-DOF design such that (i) both the forward-path and feedback-path compensators are proper or strictly proper and (ii) the step response is overdamped, with a dominant time constant of 10 s.

6.40 A second-order Padé approximation of the form $H(s) = (as^2 - bs + 1) / (as^2 + bs + 1)$ may be developed.

a. Use long division to obtain the series for $H(s)$ .   
b. Choose $a$ , and $b$ so as to match the series for $e^{-sT}$ to as many terms as possible.   
c. Obtain $\ell(j\omega)$ , following the procedure set out in Section 6.6, for the first-order approximation. For what value of $\omega T$ does $\ell$ first reach the value of 1?

6.41 For $P(s) = e^{-.5s} / [(.5s + 1)(s + 1)]$ :

a. Compute the Nyquist plot and calculate the range of gain for which a pure-gain feedback system is stable.   
b. Replace the delay with a first-order Padé approximation, and use the Routh criterion to calculate the range of stable gains.

6.42 In process control, the step response is sometimes used to generate an approximate model of the form $\kappa e^{-sT} / (\tau s + 1)$ . For $\kappa = 2, \tau = .5$ s and $T = 1$ s:

a. Design a proportional controller with a phase margin of $50^{\circ}$ .   
b. Add integral action such that the phase at crossover is almost as in part (a).   
c. Outline an algorithm that would accomplish this tuning for any given $\kappa, \tau$ , and $T$ .

6.43 Repeat Problem 6.42 for $\kappa = 2$ , $\tau = 1$ s, and $T = 0.5$ s.

6.44 If the delay is the dominant dynamic element, lead compensation is not effective as a means of increasing bandwidth. For the model of Problem 6.42, with $\kappa = 1$ , $\tau = 0.1$ s, and $T = 1$ s,
