$$F P = \frac {k (s ^ {2} + 8 5 . 8 6 1)}{s ^ {2} + 1 . 4 \omega_ {0} s + \omega_ {0} ^ {2}}.$$

Choose $k$ such that $F(0)P(0) = 1$ .

c. Obtain the magnitude Bode plots of $y/y_{R}$ for $\omega_{0}=4,10$ , and 50 rad/s.

d. Calculate $u/y_{R}$ for the values of $\omega_{0}$ in part (c), and obtain magnitude Bode plots. What can you conclude about the behavior of the control u as a function of bandwidth?

![](image/9f07126225dcaa292d44062c57090b2afe5e308db65ae2904c5dc957fb7c1509.jpg)

4.9 Given $FP = k / [s(s + 1)(.1s + 1)]$ :

a. Compute the Bode plots (magnitude and phase) of $F(s)P(s)$ for $k = 1$ .

b. Compute the Bode plots of $T = \frac{FP}{1 + FP}$ and $S = \frac{1}{1 + FP}$ .

c. Over what range of frequencies do the high-gain approximations $T(s) \approx 1$ and $S(s) \approx 1 / FP$ yield magnitudes that are within 3 db of the true values? Over what range are the approximate phases within $10^{\circ}$ of the true values?

d. Repeat part (c) for the low-gain approximations $T \approx FP$ and $S \approx 1$ .   
e. Over what range of frequencies is neither approximation satisfactory?

4.10 Given $P(s) = [4(s + 2)] / (s^2 + .1s + 1)$ , design a 1-DOF feedback system such that $T(s) = 1 / (s^2 + 1.4s + 1)$ .

4.11 Given $P(s) = 4 / (s^2 + 4)$ :

a. Show that it is not possible to design a 1-DOF system that is stable and has a proper controller $F$ and $S$ of the form $(s^2 + b_1 s + b_0) / (s^2 + a_1 s + a_0)$ .   
b. Show that it is possible to satisfy the requirements of part (a) with $S = (s^3 + a_2 s^2 + a_1 s + a_0) / (s + 2)^3$ .

Calculate $a_1, a_2, a_3$ , and $F(s)$ .

4.12 A 1-DOF system is to be designed for a stable plant with a single RHP zero, at $s = a > 0$ . The complementary sensitivity $T(s) = [(-\tau_1s + 1) / (\tau_1s + 1)] \cdot [1 / (\tau_2s + 1)]$ is close to 1 at low frequencies, and its magnitude frequency response is that of $1 / (\tau_2s + 1)$ .

a. Calculate $\tau_{1}$ so as to ensure stability.   
b. Calculate $S(s)$ .   
c. Plot the Bode magnitude plot of $S(s)$ for $\tau_2 = 1$ and $a = .1, 1,$ and 10. Discuss the effect of $a$ on the sensitivity.

M

4.13 Active suspension With reference to Problem 4.8, the suspension system is to be controlled by a 1-DOF feedback system.
