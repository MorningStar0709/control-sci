(a) Design a PI-controller such that the specifications are fulfilled.   
(b) Determine the poles and the zero of the closed-loop system. What is the damping corresponding to the complex poles?   
(c) Choose a suitable sampling interval and approximate the continuous-time controller using Tustin's method with warping. Use the crossover frequency as the warping frequency.   
(d) Simulate the system when the sampled-data controller is used. Compare with the desired response, that is, when the continuous-time controller is used.

8.6 Make an approximation, analogous to (8.16) and (8.17), such that the modifications are valid for terms up to and including $h^3$ .

8.9 The normalized motor has a state-space representation given by (A.5). The control law

$$u (t) = M u _ {c} (t) - L x (t)$$

with $M = 4$ and $L = \left( \begin{array}{ll}2 & 4 \end{array} \right)$ gives the continuous-time transfer function

$$\frac {4}{s ^ {2} + 3 s + 4}$$

from $u_{c}$ to $y$ . This corresponds to $\zeta = 0.75$ and $\omega_0 = 2$ .

(a) Make a sampled-data implementation of the controller.   
(b) Modify the control law using (8.16) and (8.17).   
(c) Simulate the controllers in (a) and (b) for different sampling periods and compare with the continuous-time controller.

8.10 Given the continuous-time system

$$
\frac {d x}{d t} = \left( \begin{array}{c c} - 3 & 1 \\ 0 & - 2 \end{array} \right) x + \binom{0}{1} u

y = \left( \begin{array}{c c} 1 & 0 \end{array} \right) x
$$

(a) Determine a continuous-time state-feedback controller

$$u (t) = - L x (t)$$

such that the characteristic polynomial of the closed-loop system is

$$s ^ {2} + 8 s + 3 2$$

A computer is then used to implement the controller as

$$u (k h) = - L x (k h)$$

(b) Modify the controller using (8.16).   
(c) Simulate the controllers in (a) and (b) and decide suitable sampling intervals. Assume that $x(0) = [1, 0]$ .

8.11 Use the w-plane method to design a compensator for the motor in Example 8.3 when h = 0.25. Design the compensator such that the transformed system has a crossover frequency corresponding to 1.4 rad/s and a phase margin of $50^{\circ}$ . Compare with the continuous-time design and the discrete-time approximations in Example 8.3. Investigate how long a sampling interval can be used for the w-plane method.

8.12 Consider the continuous-time double integrator described by (A.2). Assume that a time-continuous design has been made giving the controller
