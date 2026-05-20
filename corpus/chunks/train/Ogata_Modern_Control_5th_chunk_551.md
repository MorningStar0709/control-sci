A–7–18. A Bode diagram of the open-loop transfer function $G ( s )$ of a unity-feedback control system is shown in Figure 7–135. It is known that the open-loop transfer function is minimum phase. From the diagram, it can be seen that there is a pair of complex-conjugate poles at $\omega = 2 \mathrm { r a d } / \mathrm { s e c }$ . Determine the damping ratio of the quadratic term involving these complex-conjugate poles. Also, determine the transfer function G(s).

Solution. Referring to Figure 7–9 and examining the Bode diagram of Figure 7–135, we find the damping ratio $\zeta$ and undamped natural frequency $\omega _ { n }$ of the quadratic term to be

$$\zeta = 0. 1, \quad \omega_ {n} = 2 \mathrm{rad/sec}$$

![](image/b559085392b13ee0c8402c0d451f0b265d1d437729bdb55d05335c39e7623731.jpg)

<details>
<summary>line</summary>

| ω in rad/sec | dB | Angle (°) |
| --- | --- | --- |
| 0.1 | 40.0 | -180 |
| 0.2 | 30.0 | -175 |
| 0.4 | 20.0 | -170 |
| 0.6 | 10.0 | -165 |
| 1.0 | 5.0 | -160 |
| 2.0 | 15.0 | -155 |
| 4.0 | -20.0 | -180 |
| 6.0 | -40.0 | -190 |
| 10.0 | -60.0 | -200 |
| 20.0 | -80.0 | -210 |
| 40.0 | -90.0 | -220 |
| 60.0 | -95.0 | -230 |
| 100.0 | -100.0 | -240 |
</details>

Figure 7–135 Bode diagram of the open-loop transfer function of a unityfeedback control system.

Noting that there is another corner frequency at $\omega = 0 . 5$ radsec and the slope of the magnitude curve in the low-frequency region is –40 dBdecade, $G ( j \omega )$ can be tentatively determined as follows:

$$G (j \omega) = \frac {K \left(\frac {j \omega}{0 . 5} + 1\right)}{(j \omega) ^ {2} \left[ \left(\frac {j \omega}{2}\right) ^ {2} + 0 . 1 (j \omega) + 1 \right]}$$

Since, from Figure 7–135 we find $\left| G ( j 0 . 1 ) \right| = 4 0 ~ \mathrm { d B } .$ , the gain value K can be determined to be unity.Also, the calculated phase curve, $\underline { { \ d / G ( j \omega ) } }$ versus v, agrees with the given phase curve. Hence, the transfer function $G ( s )$ can be determined to be

$$G (s) = \frac {4 (2 s + 1)}{s ^ {2} \left(s ^ {2} + 0 . 4 s + 4\right)}$$

A–7–19. A closed-loop control system may include an unstable element within the loop.When the Nyquist stability criterion is to be applied to such a system, the frequency-response curves for the unstable element must be obtained.

How can we obtain experimentally the frequency-response curves for such an unstable element? Suggest a possible approach to the experimental determination of the frequency response of an unstable linear element.
