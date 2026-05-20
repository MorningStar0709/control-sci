In Figure 8–12, notice that, in the case where the system has gain $K = 3 0 . 3 2 2$ , the closed-loop poles at $s = - 2 . 3 5 \pm j 4 . 8 2$ act as dominant poles.Two additional closed-loop poles are very near the double zero at $s = - 0 . 6 5$ , with the result that these closed-loop poles and the double zero almost cancel each other.The dominant pair of closed-loop poles indeed determines the nature of the response. On the other hand, when the system has $K = 1 3 . 8 4 6 .$ , the closed-loop poles at $s = - 2 . 3 5 \pm j 2 . 6 2$ are not quite dominant because the two other closed-loop poles near the double zero at $s = - 0 . 6 5$ have considerable effect on the response.The maximum overshoot in the step response in this case (18%) is much larger than the case where the system is of second order and having only dominant closed-loop poles. (In the latter case the maximum overshoot in the step response would be approximately 6%.)

It is possible to make a third, a fourth, and still further trials to obtain a better response. But this will take a lot of computations and time. If more trials are desired, it is desirable to use the computational approach presented in Section 10–3. Problem A–8–12 solves this problem with the computational approach with MATLAB. It finds sets of parameter values that will yield the maximum overshoot of 10% or less and the settling time of 3 sec or less. A solution to the present problem obtained in Problem A–8–12 is that for the PID controller defined by

$$G _ {c} (s) = K \frac {(s + a) ^ {2}}{s}$$

Figure 8–12

Root-locus diagram of system when PID controller has double zero at s=–0.65. K=13.846 corresponds to  G (s) given by Equation (8–1) and K=30.322 corresponds to  Gc(s) given by Equation (8–2).

![](image/7b448eae32825da9556468619e26b1b7fecbe47c69a78cb12ba9957e1edf39ce.jpg)

<details>
<summary>line</summary>

| k | Value |
| --- | --- |
| K | 30.322 |
| ζ | 0.358 |
| ζ | 0.67 |
</details>

the values of K and a are

$$K = 2 9, \quad a = 0. 2 5$$

with the maximum overshoot equal to 9.52% and settling time equal to 1.78 sec.Another possible solution obtained there is that

$$K = 2 7, \quad a = 0. 2$$

with the 5.5% maximum overshoot and 2.89 sec of settling time. See Problem A–8–12 for details.
