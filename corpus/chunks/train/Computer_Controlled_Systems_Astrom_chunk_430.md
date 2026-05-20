Higher-order filters are obtained by cascading first- and second-order systems. Examples of filters are given in Table 7.1. The table gives filters with bandwidth $\omega_{B}=1$ . The filters get bandwidth $\omega_{B}$ by changing the factors (7.11) to

$$\frac {\omega^ {2}}{(s / \omega_ {B}) ^ {2} + 2 \zeta \omega (s / \omega_ {B}) + \omega^ {2}} \tag {7.12}$$

where $\omega$ and $\zeta$ are given by Table 7.1. The Bessel filter has a linear phase curve, which means that the shape of the signal is not distorted much. The Bessel filters are therefore common in high-performance systems.

The filter must be taken into account in the design of the regulator if the desired crossover frequency is larger than about $\omega_{B}/10$ , where $\omega_{B}$ is the bandwidth of the filter. The Bessel filter can, however, be approximated with a time delay, because the filter has linear phase for low frequencies. Table 7.2 shows the delay for different orders of the filter. Figure 7.12 shows the Bode plot of a sixth-order Bessel filter and a time delay of $2.7/\omega_{B}$ . This property implies that the sampled-data model including the antialiasing filter can be assumed to contain an additional time delay compared to the process. Assume that the bandwidth of the filter is chosen as

$$\left| G _ {a a} (i \omega_ {N}) \right| = \beta$$

![](image/c959f0ec6b6cd4a649a9be6f434ea1be42a5b271194897c73cae95575cdf3474.jpg)

<details>
<summary>line</summary>

| x | Gain |
| --- | --- |
| 0.1 | 1.0 |
| 1 | 1.0 |
| 10 | 0.01 |
</details>

![](image/23e654d04f61a559a7dfc246fad05597f03587ee93b12c50888ee3b08b421ff1.jpg)

<details>
<summary>line</summary>

| Frequency, rad/s | Phase |
| --- | --- |
| 0.1 | 0 |
| 1 | -180 |
| 10 | -360 |
</details>

Figure 7.12 Bode plot of a sixth-order Bessel filter (solid) when $\omega_{B} = 1$ and a time delay $T_{d} = 2.7$ (dashed).

where $\omega_{N}$ is the Nyquist frequency, and $G_{aa}(s)$ is the transfer function of the antialiasing filter. Table 7.3 gives some values of $T_{d}$ , as a function of $\beta$ . First, the attenuation $\beta$ is chosen. The table then gives the bandwidth of the filter in relation to the Nyquist frequency. The delay measured in the units of the sampling period is also obtained, that is, if a small value of $\beta$ is desired, then the bandwidth of the filter must be low and the corresponding delay is long.
