y (k) = \left( \begin{array}{c c c c c c} 1 & 0 & 0 & \dots & 0 & 0 \end{array} \right) x (k)
$$

Assume that $H(z)$ represents a controller. Discuss the advantages and disadvantages with the different realizations of the controller.

9.17 A digital controller with the sampling period h = 0.2 has the pulse-transfer function

$$H (z) = \frac {6 . 2 5 z ^ {2} - 1 1 . 5 z + 5 . 5}{z ^ {2} - 1 . 5 z + 0 . 5}$$

The controller is used to control a process with the transfer function

$$G (s) = \frac {1}{s ^ {2} + 1}$$

Discuss the effect of roundoff and quantization noise when different realizations are used to implement the controller on a computer having fixed word length.

9.18 Show that the continued-fraction representation (9.20) can be obtained recursively as

$$H _ {i} (z) = \frac {1}{\beta_ {i} z + \frac {1}{\alpha_ {i} + H _ {i + 1} (z)}}$$

where $H_{n+1}(z) = 0$ .

9.19 Determine the $\delta$ -operator representations of the following continuous-time transfer functions:

(a) $1 / (s^2 + 1)$   
(h) $K / (1 + Ts)$   
(c) $1 / (s + a)^{3}$

Compute the poles and the zeros and investigate what happens when $h \rightarrow 0$ .

9.20 Let $H(z)$ be the pulse-transfer function obtained from step-invariant sampling of the rational transfer function $G(s)$ . Define

$$\bar {H} (\delta) = H (1 + \delta h)$$

Prove that

$$\lim _ {h \rightarrow 0} \bar {H} (\delta) = G (\delta)$$

Show that this is true also for ramp-invariant and impulse-invariant sampling.
