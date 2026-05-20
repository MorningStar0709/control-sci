5.8 Consider the system in Problem 5.2. Use (5.52) to determine the maximum value of the control signal as a function of $\alpha$ and $\alpha$ when the command signal is a step.

5.9 A polynomial design for the normalized motor is given in Example 5.5 Simulate the system and investigate the sensitivity of the design method with respect to the choice of the sampling interval. Assume that the closed-loop specifications correspond to a second-order continuous-time system with damping $\zeta = 0.7$ and natural frequency $\omega = 1\mathrm{rad / s}$ .

5.10 Consider the system described by

$$A _ {1} (z) x (k) = B _ {1} (z) u (k)A _ {2} (z) y (k) = B _ {2} (z) x (k)$$

Assume that the variable to be controlled is $x(k)$ , but that the measured variable is $y(k)$ . Further assume that $A_{2}$ has its roots inside the unit disc. Derive a controller of the form (5.2) such that the closed-loop system is

$$A _ {c} (z) x (z) = B _ {m} (z) u _ {c} (k)$$

What are the restrictions that have to be imposed? How will uncertainties in $A_{2}$ and $B_{2}$ influence the pulse-transfer function of the closed-loop system?

5.11 Consider the two-tank system in Problem 2.10 for h = 12 s.

(a) Use polynomial methods to design a controller with an integrator. Assume that the desired closed-loop characteristic equation is

$$z ^ {2} - 1. 5 5 z + 0. 6 4 = 0$$

This corresponds to $\zeta = 0.7$ and $\omega = 0.027$ rad/s.

(h) Redesign the controller for different values of $\omega$ and study how the magnitude of the control signal varies with $\omega$ .

5.12 Consider the control of the normalized motor in Example A.2. Show that velocity feedback can be designed using pole-placement design. (Hint: First, design a feedback law with position feedback only. Show then that the control law can be rewritten as a combination of position and velocity feedback.)

5.13 Generalize the results in Problem 5.12 to a general process with several outputs.

5.14 Assume that the desired closed-loop system is given as the continuous-time model

$$G _ {m} (s) = \frac {0 . 0 1}{s ^ {2} + 0 . 1 4 s + 0 . 0 1}$$

(a) Choose an appropriate sampling interval.

(b) Determine the corresponding discrete-time transfer operator. Sketch the singularity diagram for the continuous- and the discrete-time systems, respectively.

5.15 Assume that the process has the pulse-transfer operator

$$H (q) = \frac {0 . 4 q + 0 . 3}{q ^ {2} - 1 . 6 q + 0 . 6 5}$$
