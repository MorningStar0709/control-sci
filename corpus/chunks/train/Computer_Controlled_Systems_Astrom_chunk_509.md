# Incremental Algorithms

Equation (8.24) is called a position algorithm or an absolute algorithm. The reason is that the output of the controller is the absolut value of the control signal, for instance, a valve position. In some cases it is advantageous to move the integral action outside the control algorithm. This is natural when a stepper motor is used. The output of the controller should then represent the increments of the control signal, and the motor implements the integrator. Another case is when an actuator with pulse-width control is used.

To obtain an incremental algorithm the control algorithm is rewritten so that its output is the increment of the control signal. Because it follows from (8.26) that the polynomial R in (8.25) always has a factor $(q - 1)$ this is easy to do. Introducing

$$\Delta u (k h) = u (k h) - u (k h - h)$$

we get

$$(q - a _ {d}) \Delta u (k h + h) = T (q) u _ {c} (k h) - S (q) y (k h)$$

This is called the incremental form of the controller. A drawback with the incremental algorithm is that it cannot be used for P- or PD-controllers. If this is attempted the controller will be unable to keep the reference value, because an unstable mode z - 1 is canceled.
