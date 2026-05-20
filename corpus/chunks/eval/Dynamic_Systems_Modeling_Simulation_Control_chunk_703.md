Another way to illustrate the benefit of adding the lead controller is to observe the Bode diagrams of the respective closed-loop transfer functions. Figure 11.48 shows the Bode diagram of the EHA closed-loop transfer function T(s) for the P-controller [i.e., Eq. (11.62)] with gain $K _ { P } = 5 0 0 \mathrm { V / m }$ and the lead controller (with gain $K _ { \mathrm { L F } } = 2 0 0 0 )$ . Both controllers show the ability to closely track low-frequency input signals as the closed-loop magnitude is 0 dB (unity output/input ratio) and the phase angle is small. However, for input frequencies greater than 4 rad/s (about 0.6 Hz), the phase angle of the lead-controller system is greater than the phase of the P-control system. Therefore, the closed-loop EHA system with a lead controller can track a sinusoidal input with smaller phase (or time) lag when compared to the closed-loop P-control system. Note that we can read the magnitude and phase for ?? = 12.57 rad/s (2 Hz) from the Bode diagram and estimate the closed-loop frequency responses shown in Figs. 11.46 and 11.47.

![](image/528f6784ccdc9208adfead5593bcd1f44e91a2eb294af6c242303ab11b68c682.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | P-controller | Lead controller |
| --- | --- | --- |
| 0.1 | 0 | 0 |
| 1 | -5 | -2 |
| 10 | -15 | -8 |
| 100 | -30 | -20 |
| 1000 | -60 | -45 |
</details>

![](image/56ab81cd2d7d7a67ef2109c5573f518172ac61239d119a66f9ae555e79675063.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Phase of T(jω), deg (Solid Line) | Phase of T(jω), deg (Dashed Line) |
| --- | --- | --- |
| 0.1 | 0 | 0 |
| 1 | ~-20 | ~-30 |
| 10 | ~-60 | ~-40 |
| 100 | ~-120 | ~-90 |
| 1000 | ~-270 | ~-250 |
</details>

Figure 11.48 Bode diagram of the closed-loop EHA systems using proportional and lead controllers.
