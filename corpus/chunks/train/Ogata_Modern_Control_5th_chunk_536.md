# EXAMPLE PROBLEMS AND SOLUTIONS

A–7–1. Consider a system whose closed-loop transfer function is

$$\frac {C (s)}{R (s)} = \frac {1 0 (s + 1)}{(s + 2) (s + 5)}$$

Clearly, the closed-loop poles are located at $s = - 2$ and $s = - 5$ , and the system is not oscillatory.

Show that the closed-loop frequency response of this system will exhibit a resonant peak, although the damping ratio of the closed-loop poles is greater than unity.

Solution. Figure 7–118 shows the Bode diagram for the system. The resonant peak value is approximately 3.5 dB. (Note that, in the absence of a zero, the second-order system with $\zeta > 0 . 7$ will not exhibit a resonant peak; however, the presence of a closed-loop zero will cause such a peak.)

![](image/1c362bf75a2074ec94a7236e52b48863ff6b9fe04bc77e6870346e8339e450f3.jpg)  
Figure 7–118   
Bode diagram for

$$1 0 (1 + j \omega) / [ (2 + j \omega) (5 + j \omega) ].$$

A–7–2. Consider the system defined by

$$
\begin{array}{l} \left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 2 5 & - 4 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c c} 1 & 1 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right] \\ \left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] \\ \end{array}
$$

Obtain the sinusoidal transfer functions $Y _ { 1 } ( j \omega ) / U _ { 1 } ( j \omega ) , ~ Y _ { 2 } ( j \omega ) / U _ { 1 } ( j \omega ) , ~ Y _ { 1 } ( j \omega ) / U _ { 2 } ( j \omega )$ and, $Y _ { 2 } ( j \omega ) / U _ { 2 } ( j \omega )$ In deriving. $Y _ { 1 } ( j \omega ) / U _ { 1 } ( j \omega )$ and $Y _ { 2 } ( j \omega ) / U _ { 1 } ( j \omega )$ we assume that, $U _ { 2 } ( j \omega ) = 0$ Simi-. larly, in obtaining $Y _ { 1 } ( j \omega ) / U _ { 2 } ( j \omega )$ and $Y _ { 2 } ( j \omega ) / U _ { 2 } ( j \omega )$ we assume that, $U _ { 1 } ( j \omega ) = 0$ .

Solution. The transfer matrix expression for the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}\dot {\mathbf {y}} = \mathbf {C x} + \mathbf {D u}$$

is given by

$$\mathbf {Y} (s) = \mathbf {G} (s) \mathbf {U} (s)$$

where $\mathbf { G } ( s )$ is the transfer matrix and is given by

$$\mathbf {G} (s) = \mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} + \mathbf {D}$$

For the system considered here, the transfer matrix becomes
