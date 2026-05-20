(a) Determine the order of the system.   
(b) Determine the poles of the filter and make a state-space representation of the filter.

2.17 Use the z-transform to determine the output sequence of the difference equation

$$y (k + 2) - 1. 5 y (k + 1) + 0. 5 y (k) = u (k + 1)$$

when $u(k)$ is a step at $k = 0$ and when $y(0) = 0.5$ and $y(-1) = 1$ .

2.18 Verify that

$$\mathcal {Z} \left\{\frac {1}{2} (k h) ^ {2} \right\} = \frac {h ^ {2} z (z + 1)}{2 (z - 1) ^ {3}}$$

Compare with Table 2.3 and use that to determine the pulse-transfer function of the double integrator (see Example A.1).

2.19 Use (2.30) to determine the pulse-transfer function of (a) the system in Problem 2.1 and (b) the normalized motor (see Example A.2).

2.20 Show that a curve of constant damping $\zeta$ in the $s$ -plane is a logarithmic spiral in the $z$ -plane when using the mapping $z = \exp(sh)$ . That is, the distance to the origin can be written as $r = ae^{m\varphi}$ , where $\varphi$ is the angle.

2.21 If $\beta < \alpha$ , then

$$\frac {s + \beta}{s + \alpha}$$

is called a lead network (i.e., it gives a phase advance). Consider the discrete-time system

$$\frac {z + b}{z + a}$$

(a) Determine when it is a lead network.   
(b) Simulate the step response for different pole and zero locations.

2.22 Consider the system

$$\frac {z + b}{(1 + b) (z ^ {2} - 1 . 1 z + 0 . 4)}$$

The pole location corresponds to a continuous-time system with damping $\zeta = 0.7$ . Simulate the system and determine the overshoot for different values of b in the interval $(-1, 1)$ .

2.23 Consider the stable continuous-time system

$$G (s) = \frac {s + b}{s + a}$$

where $a \neq b$ . Sample the system with the sampling period h. Derive conditions for when the sampled system will have a stable inverse.

2.24 Consider the discrete-time system

$$H (z) = \frac {b _ {1} z + b _ {2}}{z ^ {n + 1} (z - a)}$$

This system is obtained by sampling a continuous-time system with the transfer function

$$G (s) = \frac {K e ^ {- s t}}{1 + s T}$$

using the sampling interval h. Show that

$$T = - h / \ln aK = \frac {b _ {1} + b _ {2}}{1 - a}\tau = n h - \frac {h}{\ln \alpha} \ln \frac {a b _ {1} + b _ {2}}{a (b _ {1} + b _ {2})}$$

2.25 Use (2.30) to determine the pulse-transfer function associated with

$$G (s) = \frac {1}{s ^ {3}}$$

2.26 Use Eq. (2.30) to show that the pulse-transfer function obtained with zero-order-hold samplings of the transfer function

$$G (s) = \frac {1}{s ^ {n}}$$

is given by

$$H (z) = \frac {h ^ {n}}{n !} \frac {B _ {n} (z)}{(z - 1) ^ {n}}$$

where
