For simplicity, we will assume unity feedback, H(s) = 1. Therefore, the closed-loop transfer function using P-control is

$$T (s) = \frac {K _ {P} G (s)}{1 + K _ {P} G (s)} = \frac {K _ {P}}{s (s + 2) (s + 3) + K _ {P}} \tag {10.55}$$

Using Eq. (10.55), we see that the characteristic equation is $1 + K _ { P } G ( s ) = 0 , { \mathrm { o r } } s ^ { 3 } + 5 s ^ { 2 } + 6 s + K _ { P } = 0 .$ . If the P-gain is $K _ { P } = 3 0$ , the characteristic equation is

$$K _ {P} = 3 0: \quad s ^ {3} + 5 s ^ {2} + 6 s + 3 0 = 0$$

The corresponding closed-loop roots are $r _ { 1 } = - 5$ and $r _ { 2 , 3 } = \pm j 2 . 4 5$ . Because two roots are on the imaginary axis, the closed-loop system is marginally stable for $K _ { P } = 3 0$ . For gain $K _ { P } > 3 0$ , the closed-loop system is unstable. Figure 10.52 shows the Bode diagram of the open-loop transfer function $K _ { P } G ( s ) H ( s )$ ) with gain $K _ { P } = 3 0$ . The critical condition for marginal stability can be seen on the Bode diagram: when the control gain is $K _ { P } = 3 0$ , the critical condition of unity magnitude (0 dB) and $- 1 8 0 ^ { \circ }$ phase occurs simultaneously at the frequency $\omega = 2 . 4 5$ rad/s. Hence, the Bode diagram in Fig. 10.52 shows a marginally stable system that oscillates at a frequency of 2.45 rad/s. This frequency matches the two marginally stable roots that lie on the imaginary axis, $r _ { 2 , 3 } = \pm j 2 . 4 5$ , when the P-gain is $K _ { P } = 3 0$ .

![](image/78a2f03d3ff968dedce514b89ee675cccbc72f97c6e71f8c909732532608041a.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Magnitude, dB (Kp=30) | Phase, deg (-180°) |
| --- | --- | --- |
| 10⁻² | ~50 | -90 |
| 10⁻¹ | ~30 | -135 |
| 10⁰ | ~0 | -180 |
| 10¹ | ~-30 | -225 |
| 10² | ~-90 | -270 |
</details>

Figure 10.52 Bode diagram of open-loop transfer function $3 0 / ( s ^ { 3 } + 5 s ^ { 2 } + 6 s )$ showing a marginally stable closed-loop system with $K _ { P } = 3 0$ .
