# Example 9.9

Figure 9.28 presents the spool-valve dynamics from Example 9.4, where force $f _ { \mathrm { e m } }$ (from the solenoid) is the input and valve position y is the output. Show the resonant frequency (if applicable) and bandwidth on the Bode diagram and present these frequencies in hertz.

The spool-valve transfer function is

$$G _ {2} (s) = \frac {1}{0 . 0 4 s ^ {2} + 1 6 s + 7 0 0 0} = \frac {Y (s)}{F _ {\mathrm{em}} (s)}$$

Figure 9.29 shows the Bode diagram of the second-order spool-valve system. The DC gain of $G _ { 2 } ( s )$ is $1 / 7 0 0 0 =$ $1 . 4 2 9 ( 1 0 ^ { - 4 } ) ( \mathrm { o r } , - 7 7 \mathrm { d B } )$ and the corner frequency is $\omega _ { c } = \sqrt { 7 0 0 0 / 0 . 0 4 } = 4 1 8 . 3$ rad/s. From Fig. 9.29 we see that the magnitude drops 3 dB from its DC gain at a cutoff frequency of about $\omega _ { B } = 5 4 2$ rad/s (86.3 Hz), hence the bandwidth is greater than the corner frequency. Because the undamped natural frequency and damping ratio of the spool valve are $\omega _ { n } = 4 1 8 . 3$ rad/s and $\zeta = 0 . 4 7 8$ , respectively, the resonant frequency of the spool valve is $\omega _ { r } = \omega _ { n } \sqrt { 1 - 2 \zeta ^ { 2 } } = 3 0 8 . 2$ rad/s or 49.1 Hz. The magnitude of the resonant peak is fairly small (due to the moderate amount of damping) as demonstrated by the magnitude plot in Fig. 9.29.

![](image/2080f1a5ea4e78e50b740d1ecc4dc471806834b7f280e04fddaa6d560e5d9e83.jpg)

<details>
<summary>text_image</summary>

Electromagnetic
force, f_em (N) → [1 / (0.04s^2 + 16s + 7000)] → Valve position, y (m)
</details>

Spool-valve dynamics, $G _ { 2 } ( s )$   
Figure 9.28 Spool valve for Example 9.9.

![](image/f890f82b48275f71d4bedd437e7cc80d154a73ecb8fe576f0de6087774240e82.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Magnitude, dB | Phase, deg |
| --- | --- | --- |
| 10^0 | -80 | 0 |
| 10^1 | -80 | -30 |
| 10^2 | -80 | -60 |
| 10^3 | -120 | -150 |
| 10^4 | -140 | -180 |
</details>

Figure 9.29 Bode diagram of spool valve $G _ { 2 } ( s )$ (Example 9.9).
