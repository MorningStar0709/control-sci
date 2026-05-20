# Example 6.11 (dc Servo)

Design a lead-lag compensator for a dc servo that satisfies the crossover-frequency and phase-margin specifications of Example 6.10 and the dc specifications of Example 6.8.

Solution The first part of the design is exactly as in Example 6.10. The resulting compensator is

$$G _ {c 1} (s) = 1. 4 8 3 \frac {0 . 6 3 0 s + 1}{0 . 1 7 7 s + 1}.$$

In Example 6.8, it was determined that the dc gain of the compensator had to be at least 2.28. The dc gain of $G_{c1}(s)$ is 1.483, so the lag compensator must contribute

$$k _ {0} = G _ {c 2} (j 0) = \frac {2 . 2 8}{1 . 4 8 3} = 1. 5 3 7.$$

From Equation 6.29,

$$k _ {1} = 1. 5 3 7 - 1 = 0. 5 3 7.$$

Note that the process of increasing the crossover frequency has increased the gain at all frequencies, as Figure 6.25 shows. This means that the lag is not called upon to deliver as much additional gain as in Example 6.5.

From Equation 6.30, with $a = 0.1$ and $\omega_{c} = 3$ rad/s,

$$T = \frac {1}{3} \sqrt {\frac {. 5 3 7 ^ {2}}{. 1 ^ {2}} - 1}= 1. 7 6 \mathrm{s}.$$

Because this time constant is much smaller than that in Example 6.8, it should avoid the long, slow tail in the transients. The lag portion is

$$G _ {c 2} (s) = 1. 5 3 7 \frac {1 . 1 4 s + 1}{1 . 7 6 s + 1}.$$

The complete compensator is

$$
\begin{array}{l} G _ {c} (s) = G _ {c 2} (s) G _ {c 1} (s) \\ = 2. 2 8 \frac {(1 . 1 4 s + 1)}{(1 . 7 6 s + 1)} \frac {(. 6 3 0 s + 1)}{(. 1 7 7 s + 1)}. \\ \end{array}
$$

Figures 6.26 and 6.27 show, respectively, the responses to a unit step in the set-point $\theta_{d}$ and to a step load torque of -0.01 Nm. These should be compared to the responses of Figures 6.19 and 6.20.

![](image/0188deb907f615b4723c92ef821dd688221315207b95143f828c1fc2172e6014.jpg)

<details>
<summary>line</summary>

| Time (s) | Theta (rad) |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.8 |
| 1.0 | 1.1 |
| 1.5 | 1.0 |
| 2.0 | 1.0 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
| 3.5 | 1.0 |
| 4.0 | 1.0 |
| 4.5 | 1.0 |
| 5.0 | 1.0 |
</details>

Figure 6.26 Step response, dc servo with lead-lag compensation

![](image/c5dcb3de218848906743c30bb547fd5a1b059e38db16d1778e077f33c403beb4.jpg)

<details>
<summary>line</summary>

| Time (s) | Theta (rad) |
| --- | --- |
| 0.0 | 0.0000 |
| 0.5 | 0.0060 |
| 1.0 | 0.0095 |
| 1.5 | 0.0100 |
| 2.0 | 0.0100 |
| 2.5 | 0.0098 |
| 3.0 | 0.0095 |
| 3.5 | 0.0092 |
| 4.0 | 0.0090 |
| 4.5 | 0.0088 |
| 5.0 | 0.0085 |
</details>

Figure 6.27 Load torque response, dc servo with lead-lag compensation
