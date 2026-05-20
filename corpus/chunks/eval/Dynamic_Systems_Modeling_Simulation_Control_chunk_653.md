Figure 11.8 shows the Bode diagram of the vibration isolation system. For low-frequency inputs (1–2 rad/s or 0.16–0.32 Hz), the magnitude is 0 dB and the phase is nearly zero. Recall that a magnitude of 0 dB is equal to an amplitude ratio of unity, so for low-frequency inputs the steady-state driver position $z _ { 2 } ( t )$ essentially matches the input sinusoid $z _ { 0 } ( t )$ . Figure 11.6a demonstrates how the output $z _ { 2 } ( t )$ matches the input $z _ { 0 } ( t )$ when input frequency is 0.25 Hz. The Bode diagram in Fig. 11.8 also shows that the maximum amplitude ratio (resonance) is about 6 dB, which occurs at an input frequency of about 10 rad/s. An exact value of the frequency response for a desired input frequency can be obtained using the MATLAB commands:

$$
\begin{array}{l} > > \mathrm{w} = 1 0; \\ \% \text { input frequency,} \omega , \text { rad / s } \\ > > [ \text { mag }, \text { phase } ] = \text { bode(sys,w) } \\ \% \text {compute magnitude and phase} \\ \end{array}
$$

Magnitude is returned as the output/input amplitude ratio, and phase angle is in degrees. Using these MATLAB commands, we find that the peak amplitude ratio is about 2.0643 at the corresponding resonant frequency of 10.07 rad/s (or, 1.60 Hz). The peak magnitude in decibels is 20 $\log _ { 1 0 } ( 2 . 0 6 4 3 ) = 6 . 3 \ : \mathrm { d B }$ . The Bode diagram also shows that the amplitude ratio drops off at a rate of about 40 dB/decade for frequencies higher than the resonant frequency of 10 rad/s.

The constant low-frequency magnitude, followed by a single peak at a resonant frequency, and a −40 dB/decade magnitude drop for high-frequency inputs all indicate that we can develop an approximate, second-order transfer function relating the driver displacement $z _ { 2 }$ and input $z _ { 0 } .$ . Because the low-frequency magnitude is unity (or, 0 dB), an approximate transfer function must have a unity DC gain. Therefore, an approximate transfer function $\overline { { G } } ( s )$ would have the standard second-order form

$$\overline {{G}} (s) = \frac {\omega_ {n} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}} = \frac {Z _ {2} (s)}{Z _ {0} (s)} \tag {11.7}$$

![](image/5625ea9f1ded11456d9757e5826fa61232ccbcd6c27a7db512a604326c53808a.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Magnitude, dB |
| --- | --- |
| 1 | 0 |
| 10 | 5 |
| 100 | -30 |
| 1000 | -75 |
</details>

![](image/66678229e12eaa971a64972d046d84b7808c4c731144fab53f939cf3b40e0086.jpg)
