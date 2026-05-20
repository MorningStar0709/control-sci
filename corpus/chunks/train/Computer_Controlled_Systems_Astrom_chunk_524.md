$$
u (t) = 2 u _ {c} (t) - \left( \begin{array}{l l} 1 & 2 \end{array} \right) \hat {x} (t)
\frac {d \hat {x} (t)}{d t} = A \hat {x} (t) + B u (t) + K (y (t) - C \hat {x} (t))
$$

with $K^{T} = \left( \begin{array}{cc} 1 & 1 \end{array} \right)$ .

(a) Assume that the controller should be implemented using a computer. Modify the controller (not the observer part) for the sampling interval $h = 0.2$ using (8.16) and (8.17).   
(b) Approximate the observer using backward-difference approximation.   
(c) Simulate the continuous-time controller and the discrete-time approximation. Let the initial values be $x(0) = \left( \begin{array}{ll}1 & 1 \end{array} \right)^T$ and $\hat{x}(0) = \left( \begin{array}{ll}0 & 0 \end{array} \right)^T$ .

8.13 Derive ramp-invariant approximations of the transfer function

$$G (s) = \frac {1}{s + a}$$

and

$$G (s) = \frac {s}{s + a}$$

8.14 Derive the ramp-invariant equivalent of the PID-controller.   
8.15 There are many different ways to sample a continuous-time system. The key difference is the assumption made on the behavior of the control signal over the sampling interval. So far we have discussed step invariance and ramp invariance. Derive formula for impulse invariant sampling of the system (8.11) when the continuous-time signal is assumed to be a sequence of impulses that occur just after the sampling instants.   
8.16 Derive the impulse-invariant approximations of the transfer functions in Problem 8.13.   
8.17 The frequency prewarping in Sec. 8.2 gives the correct transformation at one frequency along the imaginary axis. Derive the necessary warping transformation such that one point at an arbitrary ray through the origin is transformed correctly.
