Note that

$$\frac {1}{\sqrt {\alpha}} = \frac {1}{\sqrt {0 . 2 4}} = \frac {1}{0 . 4 9} = 6. 2 \mathrm{dB}$$

and $\left| G _ { 1 } ( j \omega ) \right| = - 6 . 2 \ : \mathrm { d B }$ corresponds to $\omega = 9 \mathrm { r a d / s e c }$ .We shall select this frequency to be the new gain crossover frequency $\omega _ { c }$ . Noting that this frequency corresponds to $1 / { \left( \sqrt { \alpha } T \right) }$ o r, $\bar { \omega } _ { c } = 1 / \big ( \sqrt { \alpha } T \big )$ we obtain,

$$\frac {1}{T} = \sqrt {\alpha} \omega_ {c} = 4. 4 1$$

and

$$\frac {1}{\alpha T} = \frac {\omega_ {c}}{\sqrt {\alpha}} = 1 8. 4$$

The lead compensator thus determined is

$$G _ {c} (s) = K _ {c} \frac {s + 4 . 4 1}{s + 1 8 . 4} = K _ {c} \alpha \frac {0 . 2 2 7 s + 1}{0 . 0 5 4 s + 1}$$

where the value of $K _ { c }$ is determined as

$$K _ {c} = \frac {K}{\alpha} = \frac {1 0}{0 . 2 4} = 4 1. 7$$

Thus, the transfer function of the compensator becomes

$$G _ {c} (s) = 4 1. 7 \frac {s + 4 . 4 1}{s + 1 8 . 4} = 1 0 \frac {0 . 2 2 7 s + 1}{0 . 0 5 4 s + 1}$$

Note that

$$\frac {G _ {c} (s)}{K} G _ {1} (s) = \frac {G _ {c} (s)}{1 0} 1 0 G (s) = G _ {c} (s) G (s)$$

The magnitude curve and phase-angle curve for $G _ { c } ( j \omega ) / 1 0$ are shown in Figure 7–96. The compensated system has the following open-loop transfer function:

$$G _ {c} (s) G (s) = 4 1. 7 \frac {s + 4 . 4 1}{s + 1 8 . 4} \frac {4}{s (s + 2)}$$

![](image/70a49e3d823efbf7d2bb8d1afdd718d8707551d9fbbe08c4c3ba11caa8a49ca0.jpg)

<details>
<summary>line</summary>

| ω in rad/sec | Gc/10 dB (Gc/G) | Kv dB (Gc/G) | Gc/G dB (Gc/G) |
| --- | --- | --- | --- |
| 1 | 25 | 20 | -90 |
| 2 | 20 | 15 | -95 |
| 4 | 10 | 5 | -100 |
| 6 | 0 | 0 | -105 |
| 10 | -10 | -10 | -110 |
| 20 | -20 | -20 | -120 |
| 40 | -30 | -30 | -130 |
| 60 | -40 | -40 | -140 |
| 100 | -50 | -50 | -150 |
</details>

Figure 7–96 Bode diagram for the compensated system.

The solid curves in Figure 7–96 show the magnitude curve and phase-angle curve for the compensated system. Note that the bandwidth is approximately equal to the gain crossover frequency. The lead compensator causes the gain crossover frequency to increase from 6.3 to 9 radsec. The increase in this frequency means an increase in bandwidth. This implies an increase in the speed of response.The phase and gain margins are seen to be approximately $5 0 ^ { \circ }$ and ±q dB, respectively. The compensated system shown in Figure 7–97 therefore meets both the steady-state and the relative-stability requirements.
