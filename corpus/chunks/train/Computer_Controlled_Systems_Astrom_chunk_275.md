Let the observer be of the deadbeat type; that is, the poles of the observer should be in the origin.

4.6 Determine the full-state observer based on (4.28) for the tank system in Problem 2.10. Choose the observer gain such that the observer is twice as fast as the open-loop system.

4.7 Consider the observer of (4.32) and let the control law be given by

$$u (k) = - L \hat {x} (k \mid k)$$

Show that the resulting controller can be written as

$$w (k + 1) = \Phi_ {o} w (k) + \Gamma_ {o} y (k)u (k) = C _ {o} w (k) + D _ {o} y (k)$$

where

$$
\begin{array}{l} \Phi_ {o} = (I - K C) (\Phi - \Gamma L) \quad \Gamma_ {o} = (I - K C) (\Phi - \Gamma L) K \\ C _ {o} = - L \quad D _ {o} = - L K \\ \end{array}
$$

4.8 Given the discrete-time system

$$
\begin{array}{l} x (k + 1) = \left( \begin{array}{l l} 0. 5 & 1 \\ 0. 5 & 0. 7 \end{array} \right) x (k) + \left( \begin{array}{l} 0. 2 \\ 0. 1 \end{array} \right) u (k) + \left( \begin{array}{l} 1 \\ 0 \end{array} \right) v (k) \\ y (k) = \left( \begin{array}{c c} 1 & 0 \end{array} \right) x (k) \\ \end{array}
$$

where v is a constant disturbance. Determine controllers such that the influence of v can be eliminated in steady state in each case.

(a) The state and v can be measured.   
(b) The state can be measured.

(c) Only the output can be measured.

4.9 Consider the two-tank system in Problem 2.10 for h = 12 s.

(a) Determine a state-feedback controller such that the closed-loop poles are given by the characteristic equation

$$z ^ {2} - 1. 5 5 z + 0. 6 4 = 0$$

This corresponds to $\zeta = 0.7$ and $\omega = 0.027$ rad/s.

(b) Introduce a command signal and determine a controller such that the steady-state error between the command signal and the output is zero in steady state; that is, introduce an integrator in the system.

(c) Simulate the system using the regulators in (a) and (b).

4.10 Consider the double integrator with a load disturbance acting on the process input. The disturbance can be described as a sinusoid with frequency $\omega_{0}$ , but with unknown amplitude and phase. Design a state-feedback controller and an observer such that there is no steady-state error due to the sinusoidal perturbation.

4.11 Consider the discrete-time process

$$
x (k + 1) = \left( \begin{array}{c c} 0. 9 & 0 \\ 1 & 0. 7 \end{array} \right) x (k) + \binom {1} {0} u (k)

y (k) = \left( \begin{array}{l l} 0 & 1 \end{array} \right) x (k)
$$

(a) Determine a state deadbeat controller that gives unit static gain, that is, determine $L_{c}$ and L in the controller
