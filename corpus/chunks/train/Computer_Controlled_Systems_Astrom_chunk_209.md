# Example 3.14 Hidden oscillation in an open-loop system

Consider a continuous-time system with the transfer function

$$G (s) = \frac {1}{s + 1} + \frac {\pi}{(s + 0 . 0 2) ^ {2} + \pi^ {2}}$$

Sampling this system with h = 2 gives the pulse-transfer function

$$H (z) = \frac {1 - a}{z a} + \frac {0 . 0 1 2 5}{z \alpha}$$

where $a = e^{-2}$ and $\alpha = e^{-0.04}$ .

The oscillatory part of the continuous-time system has the frequency $\pi$ and damping of 0.02. The sampling frequency is $\pi$ , which implies that the oscillation is sampled only once per period.

The discrete-time system is of second order and the continuous-time system is of third order. The cancellation of poles and zeros that are oscillatory is an indication that hidden oscillation may occur. Figure 3.19 shows the step response of the continuous-time system. The sampling points are indicated by dots. The system behaves like a second-order system at the sampling points. Figure 3.19 also shows the sampled output when h = 1.8. The oscillation is now clearly seen in the sampled output although it now appears at a lower frequency.

The second type of hidden oscillation occurs if there are poorly damped zeros in the open-loop system that are canceled by the controller. In this case, the oscillation can be seen in the control signal. This type of hidden oscillation will not be detected if the sampling period is changed, provided that the design is still such that the process zeros are canceled.
