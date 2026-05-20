# 6.28 Heat exchanger

a. Modify the proportional-control design of Problem 6.13 to PID control. Retain the same phase margin, but increase the crossover frequency to 2.8 rad/s.   
b. Compute the closed-loop step response, using the linearized model.   
c. Compute the closed-loop responses to steps of increasing amplitudes, using the full nonlinear model. What can you conclude about the range of validity of the linear model?

6.29 Crane The plant with the transfer function $\Delta x / F$ of Problem 3.20 (Chapter 3) cannot be stabilized by pure-gain feedback.

a. Design a lead compensator for a phase margin of $50^{\circ}$ and a crossover frequency of 0.6 rad/s.   
b. With the lead compensator of part (a) but letting the gain vary, compute the Root Locus.   
c. Compute the unit-step and unit-ramp responses for the compensator of part (a), using the linear model.   
d. Compute the responses to steps and ramps of increasing amplitudes, using the full nonlinear model. What can you conclude about the range of validity of the linear model?

6.30 In Problem 6.23, a lead-lag compensator was designed for the system of Problem 6.1. Suppose the disturbance-to-output transmission is given as

$$\frac {y}{w} = P _ {w} (s) = \frac {. 5 (s + 2)}{(s + 1) ^ {2} (s ^ {2} + s + 1)}.$$

a. Add a feedforward control such that the magnitude of the disturbance frequency response is at most -10 db to 4 rad/s.   
b. Compute the responses to a unit-step disturbance with and without feedforward.

6.31 In Problem 6.24, a lead-lag compensator was designed for the system of Problem 6.2. Suppose the disturbance-to-output transmissions is given as

$$\frac {y}{w} = P _ {w} (s) = \frac {. 5 (s + 2) ^ {2}}{s (s ^ {2} + s + 1) (s + 4)}.$$

a. Add a feedforward control such that the magnitude of the disturbance frequency response is at most -10 db to 6 rad/s.   
b. Compute the responses to a unit-step disturbance with and without feed forward.

6.32 Heat exchanger In a heat exchanger, the objective is to control the outlet temperature of the cold stream by varying the flow rate of the hot stream. Suppose the flow rate of the cold stream is subject to variations, $\Delta F_{C}$ . A PID control was designed in Problem 6.28.
