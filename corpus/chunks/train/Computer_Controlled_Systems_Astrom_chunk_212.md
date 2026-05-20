$$
x (k + 1) = \left( \begin{array}{l l l} 0 & 1 & 2 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{array} \right) x (k) + \left( \begin{array}{l} 0 \\ 1 \\ 0 \end{array} \right) u (k)
$$

(a) Determine a control sequence such that the system is taken from the initial stata $x^T(0) = \left( \begin{array}{ccc} 1 & 1 & 1 \end{array} \right)$ to the origin.

(b) Which is the minimum number of steps that solve the problem in (a)?

(c) Explain why it is not possible to find a sequence of control signals such that the state $\left( \begin{array}{lll}1 & 1 & 1 \end{array} \right)^T$ is reached from the origin.

3.9 Verify the formula for $W_{c}^{-1}$ given in Example 3.9 for an $n$ th-order system.

3.10 The system

$$x (k + 1) = \Phi x (k) + \Gamma u (k)$$

has been obtained from the system

$$z (k + 1) = F z (k) + G u (k)$$

by a linear transformation

$$z = T x$$

(a) Use the result in Sec. 3.4 to derive a formula for $T$ when $\dim(u) = 1$ and $\dim(u) = r$ .

(b) Use the result to solve Problem 2.7.

3.11 Determine the stability and the stationary value of the output for the system described by Fig. 3.21 with

$$H (q) = \frac {1}{q (q - 0 . 5)}$$

when $u_{c}$ is a step function and (a) $H_{c}(q) = K$ (proportional controller), $K > 0$ ; and (b) $H_{c}(q) = Kq / (q - 1)$ (intagral controller), $K > 0$ .

3.12 Consider the system in Problem 3.11. Determine the steady-stata error between the command signal, $u_{c}$ , and the output when $u_{c}$ is a unit ramp, that is, $u_{c}(k) = k$ . Assume that $H_{c}$ is (a) a proportional controller and (b) an integral controller.

3.13 Sample the system

$$G (s) = \frac {s + 1}{s ^ {2} + 0 . 2 s + 1}$$

and determine the sampling intervals for which the response of the system will have hidden oscillations. Verify by simulations.

3.14 Consider the tank system with the pulse-transfer operator given in Problem 2.10(b), that is, when the system is sampled with h = 12.

(a) Introduce a controller as in Fig. 3.21. Let the command input be a step and determine the steady-state error when using a proportional controller $K$ and an integral controller $K / (1 - q^{-1})$ .   
(b) Simulate the system using the controllers in (a). Investigate the influence of the controller gain $K$ . Determine $K$ such that the poles of the closed-loop system correspond to a damping of $\zeta = 0.7$ .

3.15 Consider the system in Fig. 3.5. Derive a formula for the velocity error coefficient. That is an expression for the steady-state error when the reference signal $u_{c}$ is a unit ramp.
