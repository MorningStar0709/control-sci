# Solution

The sampled signal is

$$y ^ {*} (t) = \sum_ {k = 0} ^ {\infty} \cos k T _ {s} u _ {0} (t - k T _ {s}).$$

For $T_{s}=2\pi$ ,

$$y ^ {*} (t) = \sum_ {k = 0} ^ {\infty} \cos k 2 \pi u _ {0} (t - k 2 \pi) = \sum_ {k = 0} ^ {\infty} u _ {0} (t - k 2 \pi).$$

For $T_{s} = \pi / 2$ ,

$$
\begin{array}{l} y ^ {*} (t) = \sum_ {k = 0} ^ {\infty} \cos k \frac {\pi}{2} u _ {0} \left(t - k \frac {\pi}{2}\right) \\ = u _ {0} (t) - u _ {0} (t - \pi) + u _ {0} (t - 2 \pi) \dots \\ \end{array}
$$

Figures 9.7a and b show plots of the impulse area versus k. Clearly, Figure 9.7a could have been obtained by sampling a constant or, indeed, any harmonic of cos t.

Since $\cos t = \frac{1}{2}(e^{jt} + e^{-jt})$ , its spectrum consists of impulses of area $\frac{1}{2}$ at $\omega = \pm1$ rad/s. For $\omega_{0} = 1$ rad/s, Figure 9.7c shows the sum of $(1/2\pi)Y(j\omega)$ and the aliases centered at $\pm1$ rad/s and $\pm2$ rad/s. It is not difficult to see that the final result is a train of impulses of equal areas, $1/2\pi$ , in the frequency domain. The result for $\omega_{0} = 4$ rad/s is shown in Figure 9.7d.

![](image/3d16401967db0722ac95c64a49a0062e7b2680f0956bfdfdb214a5249fb440b2.jpg)

<details>
<summary>text_image</summary>

π
2π
3π
4π
</details>

Figure 9.7a $y = \cos t$ samples with $\omega_0 = 1$ rads/s

![](image/00d2715b7bb30b693c5930f95c00115c3d74ad5a605b986070af7dd6608e4bb5.jpg)

<details>
<summary>text_image</summary>

π
2π
3π
4π
</details>

Figure 9.7b y   
![](image/18d68fbca46ef6d6e9bfe5bb95e591dd94806a499077e2b4c88cea4471585ccd.jpg)

<details>
<summary>line</summary>

| ω | Value |
| --- | --- |
| -3 | ↑ |
| -2 | ↑ |
| -1 | ↑ |
| 0 | 1/2 π |
| 1 | ↑ |
| 2 | ↑ |
| 3 | 1/4 π |
| (Note: The values for the rightmost points are not explicitly labeled in the chart as they are estimated based on the arrowheads). The x-axis is labeled ω) and the y-axis is unlabeled but represents the magnitude of the wave function. )
</details>

Figure 9.7c Construction of the spectrum of the sampled waveform

![](image/5ecf9b46c92d58533657b4a66fa6eb7d2de072ef5cc783ebb73c679645a7b534.jpg)

<details>
<summary>bar</summary>

| Frequency (ω) | Amplitude |
| --- | --- |
| -5 | ↑ |
| -4 | 1 |
| -3 | ↑ |
| -2 | 0 |
| -1 | ↑ |
| 0 | 1 |
| 1 | ↑ (1/π) |
| 2 | 0 |
| 3 | ↑ |
| 4 | 1 |
| 5 | ↑ |
</details>

Figure 9.7d The spectrum for the sampled waveform of Figure 9.7b

If the sampled signal is sent through an ideal low-pass filter with a bandwidth of $\omega_{0}/2$ , the result for $\omega_{0}=1$ rad/s is a single spectral line at $\omega=0$ ; the signal is constant. For $\omega_{0}=4$ rad/s, this operation recovers the original spectrum.
