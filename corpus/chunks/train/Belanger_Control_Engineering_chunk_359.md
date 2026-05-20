# Problems

6.1 Given $P(s) = [-(s - 1)] / [(s + 1)^2 (s^2 + s + 1)]$ and pure-gain control (gain $k > 0$ ):

a. Calculate the range of values of gain $k$ for which the controller yields a gain margin of at least 6 db and a phase margin of at least $50^{\circ}$ .   
b. Calculate, as a function of $k$ , the steady-state error for a unit-step set-point input, assuming stability.

6.2 Repeat Problem 6.1 for $P(s) = [(s + 1)] / [s(s^2 + s + 1)(s + 4)]$ , and calculate the steady-state error for a unit-ramp set-point input.

6.3 To investigate the concept of dominant complex poles, consider

$$H _ {d} (s) = \frac {1}{(T s + 1) (s ^ {2} + 2 \zeta s + 1)}.$$

a. With $\zeta = 0.7$ , compute the step response and obtain the peak overshoot, rise time, and settling time for $T = 0$ . Repeat for increasing values of $T$ . For what values of $T$ (approximately) do the overshoot, use time, and settling time, respectively, change by more than $20\%$ from their values of $T = 0$ ?   
b. Repeat part (a) for $\zeta = .4$ and $\zeta = .1$ . Describe the influence of the pole at $-1/T$ as a function of $\zeta$ .

6.4 Repeat Problem 6.3 for $H_{d}(s) = (Ts + 1) / (s^{2} + 2\zeta s + 1)$ .

6.5 Quarter-cycle damping is defined as the case where the overshoot of each peak of the step response is $1/4$ that of the previous peak. Calculate the value of $\zeta$ that will lead to this.

6.6 Prove Equation 6.18.

6.7 Servo with flexible shaft The dc servo of Problem 2.5 (Chapter 2) (or, equivalently, of Problem 3.14 in Chapter 3) has two pairs of complex, underdamped poles. One way of controlling such poles is by placing LHP complex zeros relatively near; since closed-loop poles migrate to zeros as the gain is increased, zeros “attract” the underdamped poles away from the j-axis.

Consider the compensator

$$F (s) = k \frac {(s + 1 0 0 \pm j 1 0 0) (s + 5 \pm j 5)}{(s + 2 0 0) ^ {4}}.$$

a. Obtain the Root Locus.   
b. Calculate the range of $k$ for stability.

c. Calculate (roughly) the value of $k$ for which the lowest of the damping factors associated with any pair of complex poles is maximized; i.e., maximize the smallest damping factor.

d. For $k$ as in part (c), compute the closed-loop step response.
