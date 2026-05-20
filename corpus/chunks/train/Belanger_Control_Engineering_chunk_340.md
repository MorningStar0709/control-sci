# Example 6.10 (dc Servo)

The dc servo-pure-gain design of Example 5.6 (Chapter 5) ( $k = 0.657$ ) turns out to have a phase margin of $64.2^{\circ}$ and a crossover frequency of 1.030 rad/s. Design a lead compensator such that the same phase margin is obtained, but at a crossover frequency of 3 rad/s.

Solution At $\omega = 3$ rad/s, the magnitude of the loop gain is -12.6 db and the phase is $-150.0^{\circ}$ . To preserve the phase margin of $64.2^{\circ}$ with a crossover at 3 rad/s, we must have

$$\neq L (j 3) = - \left(1 8 0 ^ {\circ} - 6 4. 2 ^ {\circ}\right) = - 1 1 5. 8 ^ {\circ}.$$

Therefore, we need to add $150.0^{\circ} - 115.8^{\circ} = 34.2^{\circ}$ of phase lead at $\omega = 3$ . From Equation 6.37,

$$\sin 3 4. 2 ^ {\circ} = 0. 5 6 2 = \frac {\alpha - 1}{\alpha + 1}$$

which, solving for $\alpha$ , yields $\alpha = 3.56$ . Using Equation 6.38,

$$T = \frac {1}{3 \sqrt {3 . 5 6}} = 0. 1 7 7 \mathrm{s}.$$

Finally, the gain $k_{1}$ is given by

$$k _ {1} = - | L (j 3) | = 1 2. 6 \mathrm{db}, \text { or } 4. 2 6.$$

The lead compensator to be added is

$$
\begin{array}{l} G _ {c} (s) = \frac {4 . 2 6}{\sqrt {3 . 5 6}} \frac {(3 . 5 6) (. 1 7 7) s + 1}{0 . 1 7 7 s + 1} \\ = 2. 2 5 8 \frac {0 . 6 3 0 s + 1}{0 . 1 7 7 s + 1}. \\ \end{array}
$$

This compensator is cascaded with the pure-gain controller (k = 0.657). The complete controller is

$$G _ {c} (s) = 1. 4 8 3 \frac {0 . 6 3 0 s + 1}{0 . 1 7 7 s + 1}.$$

Figure 6.25 shows the Bode plots with and without lead compensation.   
![](image/23584e95040a7978c68b79e22962555056864550622eb6780f70effe9755b664.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | With Lead | No Lead |
| --- | --- | --- |
| 0.1 | 25 | 20 |
| 1 | 0 | -10 |
| 10 | -30 | -50 |
| 100 | -80 | -90 |
</details>

![](image/fa35b18d84be3e7b82f6704cf3e37ee35ffbb7fae14a13d243e853d3a38a6b55.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Phase (deg) - No Lead | Phase (deg) - With Lead |
| --- | --- | --- |
| 0.1 | -95 | -90 |
| 1 | -120 | -110 |
| 10 | -180 | -170 |
| 100 | -260 | -250 |
</details>

Figure 6.25 Bode plots with and without lead compensation, dc servo
