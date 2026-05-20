Figure 10.53 shows the Bode diagram of G(s) with P-gain $K _ { P } = 2$ . The Bode diagram shows that the closed-loop system is stable because the 0-dB and $- 1 8 0 ^ { \circ }$ phase condition do not occur simultaneously at a common frequency. If we compare Bode diagrams in Figs. 10.52 and 10.53, we see that the magnitude plot in Fig. 10.53 has been shifted down because the gain $K _ { P }$ has decreased from 30 to 2 (the phase plot does not change with gain). We now define the first of the two important relative stability margins: the gain margin is the maximum factor by which the current gain setting can be multiplied by until the closed-loop system is driven unstable. For the system described by Eqs. (10.54) and (10.55) with a P-controller, we have shown that the closed-loop system becomes marginally stable for $K _ { P } = 3 0$ . Therefore, if the current gain is $K _ { P } = 2 ,$ , then the gain margin is 15. We can easily read the gain margin from the Bode diagram using the following steps. First, we locate the “phase-crossing frequency” $\omega _ { \mathrm { g m } }$ where the phase angle is $- 1 8 0 ^ { \circ }$ (the critical point of the phase plot). Next, we project up to the magnitude plot along frequency $\omega _ { \mathrm { g m } }$ and read the associated magnitude. This magnitude must be less than unity (i.e., negative decibel value) for a stable closed-loop system. The gain margin $( G M _ { \mathrm { d B } }$ , in decibels) is shown in Fig. 10.53 and it is the difference between the magnitude at the phase-crossing frequency $\omega _ { \mathrm { g m } }$ and the 0-dB critical point. Because gain margin is defined as a multiplicative factor, we must convert the gain margin in decibels to an absolute value

![](image/b54807b97a41fd2548690e79084a3187b53d5151408bce739c2e25f4d90bdcea.jpg)

<details>
<summary>line</summary>

| Frequency (ω, rad/s) | Magnitude (dB) | Phase Angle (deg) |
| --- | --- | --- |
| 0.01 | ~30 | -90 |
| 0.1 | ~0 | -135 |
| 1 | ~-50 | -180 |
| 10 | ~-100 | -225 |
| 100 | ~-150 | -270 |
</details>

Figure 10.53 Bode diagram of open-loop transfer function $2 / ( s ^ { 3 } + 5 s ^ { 2 } + 6 s )$ showing gain and phase margins with $K _ { P } = 2$ .

$$\text { Gain margin } = 1 0 ^ {G M _ {\mathrm{dB}} / 2 0} \tag {10.56}$$
