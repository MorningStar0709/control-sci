For a minimum-phase system, the phase angle at $\omega = \infty$ becomes $- 9 0 ^ { \circ } ( q \mathrm { ~ - ~ } p )$ , where $p$ and q are the degrees of the numerator and denominator polynomials of the transfer function, respectively. For a nonminimum-phase system, the phase angle at $\omega = \infty$ differs from $- 9 0 ^ { \circ } ( q - p )$ . In either system, the slope of the log-magnitude curve at $\omega = \infty$ is equal $\mathrm { t o } - 2 0 ( q - p )$ dBdecade. It is therefore possible to detect whether the system is minimum phase by examining both the slope of the high-frequency asymptote of the log-magnitude curve and the phase angle at $\omega = \infty .$ . If the slope of the log-magnitude curve as v approaches infinity is $- 2 0 ( q - p )$ dBdecade and the phase angle at $\omega = \infty$ is equal to $- 9 0 ^ { \circ } ( q \mathrm { ~ - ~ } p )$ , then the system is minimum phase.

![](image/6d6395afd1fafebc437ae3ed37bc7150f9270e6d2a1faa6d627e562d277f3b87.jpg)

<details>
<summary>line</summary>

| ω | G₁(jω) | G₂(jω) |
| --- | --- | --- |
| 0° | 0° | 0° |
| -90° | ~-20° | ~-70° |
| -180° | ~-30° | ~-180° |
</details>

Figure 7–13 Phase-angle characteristics of the systems $G _ { 1 } ( s )$ and $G _ { 2 } ( s )$ shown in Figure 7–12.

Nonminimum-phase systems are slow in responding because of their faulty behavior at the start of a response. In most practical control systems, excessive phase lag should be carefully avoided. In designing a system, if fast speed of response is of primary importance, we should not use nonminimum-phase components. (A common example of nonminimum-phase elements that may be present in control systems is transport lag or dead time.)

It is noted that the techniques of frequency-response analysis and design to be presented in this and the next chapter are valid for both minimum-phase and nonminimum-phase systems.

Transport Lag. Transport lag, which is also called dead time, is of nonminimumphase behavior and has an excessive phase lag with no attenuation at high frequencies. Such transport lags normally exist in thermal, hydraulic, and pneumatic systems.

Consider the transport lag given by

$$G (j \omega) = e ^ {- j \omega T}$$

The magnitude is always equal to unity, since

$$\left| G (j \omega) \right| = | \cos \omega T - j \sin \omega T | = 1$$

Therefore, the log magnitude of the transport lag $e ^ { - j { \boldsymbol { \omega } } T }$ is equal to 0 dB. The phase angle of the transport lag is
