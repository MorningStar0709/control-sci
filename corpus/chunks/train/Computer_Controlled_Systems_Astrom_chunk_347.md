# 5.9 Design of a Controller for a Flexible Robot Arm

In this section we will discuss design of a controller for a robot arm with a flexible joint. This problem was discussed in Sec. 4.7. The process that is described by Eq. (4.65) is of third order. It has one integrator, two poorly damped complex poles at $-0.05 \pm 0.999i$ , and one zero -10. Guided by the analysis in Sec. 4.7 we choose a sampling period h = 0.5 s. Furthermore we choose a second-order antialiasing filter

$$\frac {\omega_ {f} ^ {2}}{s ^ {2} + 1 . 4 \omega_ {f} s + \overline {{\omega_ {f} ^ {2}}}}$$

with $\omega_{f}=2\ rad/s$ . The filter has a gain of about 0.1 at the Nyquist frequency $\omega_{N}\approx6\ rad/s$ .

We will consider two different controllers. One controller does not attempt to damp the poorly damped process pole. The other will introduce active damping of the process pole.

![](image/f81619cb4d14d9aa1ecfba69e2bac7cbc48eff3379d5a1b1272aaf615e839f07.jpg)  
Figure 5.24 Pole-zero diagram for the process and the filter sampled with h = 0.5. The leftmost zero represents the zero at -12.1314.
