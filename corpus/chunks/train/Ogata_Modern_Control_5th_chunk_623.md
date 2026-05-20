$$\left| K \frac {(s + 1) (s + 0 . 5 7 1 4)}{s} \frac {1}{s ^ {2} + 1} \right| _ {s = - 1 + j \sqrt {3}} = 1$$

or

$$K = 2. 3 3 3 3$$

Then the compensator can be written as follows:

$$G _ {c} (s) = 2. 3 3 3 3 \frac {(s + 1) (s + 0 . 5 7 1 4)}{s}$$

The open-loop transfer function becomes

$$G _ {c} (s) G (s) = \frac {2 . 3 3 3 3 (s + 1) (s + 0 . 5 7 1 4)}{s} \frac {1}{s ^ {2} + 1}$$

From this equation a root-locus plot for the compensated system can be drawn. Figure 8–50 is a root-locus plot.

![](image/aac7769b2910cf6bfcda75505141db0c1c2e3a7cf0e15bdd42ea195c82f02c64.jpg)

<details>
<summary>other</summary>

| Point Type | Real Axis | Imag Axis |
| --- | --- | --- |
| Circle | -1.0 | 0.0 |
| Circle | -0.8 | 0.0 |
| Circle | -0.6 | 0.0 |
| Circle | -0.4 | 0.0 |
| Circle | -0.2 | 0.0 |
| Circle | 0.0 | 0.0 |
| Cross | 0.0 | 1.0 |
| Cross | 0.0 | -1.0 |
</details>

Figure 8–50 Root-locus plot of the compensated system.

Figure 8–51 Unit-step response of the compensated system.   
![](image/d42fe8a2d4a6cac4641acbd3c30867f2cca83f493326e62b2d8f8ed7def6c732.jpg)

<details>
<summary>line</summary>

| Time (sec) | Amplitude |
| --- | --- |
| 0 | 0.0 |
| 1 | 1.1 |
| 2 | 0.8 |
| 3 | 0.8 |
| 4 | 0.9 |
| 5 | 0.95 |
| 6 | 0.97 |
| 7 | 0.98 |
| 8 | 0.99 |
| 9 | 0.995 |
| 10 | 0.998 |
| 11 | 0.999 |
| 12 | 1.0 |
</details>

The closed-loop transfer function is given by

$$\frac {C (s)}{R (s)} = \frac {2 . 3 3 3 3 (s + 1) (s + 0 . 5 7 1 4)}{s ^ {3} + s + 2 . 3 3 3 3 (s + 1) (s + 0 . 5 7 1 4)}$$

The closed-loop poles are located at $s = - 1 \pm j \sqrt { 3 }$ and $\begin{array} { r } { s = - 0 . 3 3 3 3 . } \end{array}$ A unit-step response curve is shown in Figure 8–51. The closed-loop pole at $s = - 0 . 3 3 3 3$ and a zero at $s = - 0 . 5 7 1 4$ produce a long tail of small amplitude.

A–8–7. Consider the system shown in Figure 8–52. Design a compensator such that the static velocity error constant is $4 \sec ^ { - 1 }$ , phase margin is $5 0 ^ { \circ }$ , and gain margin is 10 dB or more. Plot unit-step and unit-ramp response curves of the compensated system with MATLAB.Also, draw a Nyquist plot of the compensated system with MATLAB. Using the Nyquist stability criterion, verify that the designed system is stable.

Solution. Since the plant does not have an integrator, it is necessary to have an integrator in the compensator. Let us choose the compensator to be

$$G _ {c} (s) = \frac {K}{s} \hat {G} _ {c} (s), \quad \lim _ {s \rightarrow 0} \hat {G} _ {c} (s) = 1$$
