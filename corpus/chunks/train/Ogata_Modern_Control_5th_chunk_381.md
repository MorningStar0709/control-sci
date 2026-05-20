$$K _ {v} = \lim _ {s \rightarrow 0} s G _ {c} (s) \frac {1 0}{s (s + 4)} = \hat {K} _ {c} \beta 2. 5 = 5 0$$

Thus

$$\hat {K} _ {c} \beta = 2 0$$

Now choose $\hat { K } _ { c } = 1$ Then.

$$\beta = 2 0$$

Choose $T = 1 0 .$ . Then the lag compensator can be given by

$$G _ {c} (s) = \frac {s + 0 . 1}{s + 0 . 0 0 5}$$

The angle contribution of the lag compensator at the closed-loop pole $s = - 2 + j \sqrt { 6 }$ is

$$\left. \underline {{{G _ {c} (s)}}} \right| _ {s = - 2 + j \sqrt {6}} = \tan^ {- 1} \frac {\sqrt {6}}{- 1 . 9} - \tan^ {- 1} \frac {\sqrt {6}}{- 1 . 9 9 5}= - 1. 3 6 1 6 ^ {\circ}$$

which is small.The magnitude of $G _ { c } ( s )$ at $s = - 2 + j 6$ is 0.981. Hence the change in the location of the dominant closed-loop poles is very small.

The open-loop transfer function of the system becomes

$$G _ {c} (s) G (s) = \frac {s + 0 . 1}{s + 0 . 0 0 5} \frac {1 0}{s (s + 4)}$$

The closed-loop transfer function is

$$\frac {C (s)}{R (s)} = \frac {1 0 s + 1}{s ^ {3} + 4 . 0 0 5 s ^ {2} + 1 0 . 0 2 s + 1}$$

To compare the transient-response characteristics before and after the compensation, the unit-step and unit-ramp responses of the compensated and uncompensated systems are shown in Figures $6 { - } 8 5 ( \mathrm { a } )$ and (b), respectively. The steady-state error in the unit-ramp response is shown in Figure 6–85(c). The designed lag compensator is acceptable.

Unit-Step Responses of Compensated and Uncompensated Systems   
![](image/7f74e4caa69a8846f6ff404d49167e044d1709bc3f5fe2a472d1c1256a24d632.jpg)

<details>
<summary>line</summary>

| t Sec | Compensated system | Uncompensated system |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | 1.1 | 1.05 |
| 2 | 1.05 | 1.0 |
| 3 | 1.0 | 1.0 |
| 4 | 1.0 | 1.0 |
| 5 | 1.0 | 1.0 |
| 6 | 1.0 | 1.0 |
| 7 | 1.0 | 1.0 |
| 8 | 1.0 | 1.0 |
| 9 | 1.0 | 1.0 |
| 10 | 1.0 | 1.0 |
</details>

Unit-Ramp Responses of Compensated and Uncompensated Systems   
![](image/f847aba2f2bd43b20315daad6169ebc9daa6504a678fbdaab8bcceb39d13c6dd.jpg)

<details>
<summary>line</summary>

| t Sec | Input Ramp and Outputs (Compensated system) | Input Ramp and Outputs (Uncompensated system) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | ~1.5 | ~1.3 |
| 2 | ~2.8 | ~2.5 |
| 3 | ~4.0 | ~3.6 |
| 4 | ~5.2 | ~4.7 |
| 5 | ~6.4 | ~5.8 |
| 6 | ~7.6 | ~6.9 |
| 7 | ~8.8 | ~8.0 |
| 8 | ~9.9 | ~9.0 |
| 9 | ~10.0 | ~10.0 |
| 10 | ~10.0 | ~10.0 |
</details>

Unit-Ramp Response (35  t  40)   
![](image/eed40ac7fa1a26a41416da240234e684f8a42fe352ba7ac6efef23d14f61cf25.jpg)

<details>
<summary>line</summary>
