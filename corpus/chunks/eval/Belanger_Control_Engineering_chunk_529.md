# 9.2.2 Aliasing

The sampled signal is $y^{*}(t) = y(t)p(t)$ . Using the real multiplication theorem,

$$
\begin{array}{l} Y ^ {*} (j \omega) = \int_ {- \infty} ^ {\infty} Y (j \Omega) P (j \omega - j \Omega) d \Omega \\ = \frac {1}{T _ {s}} \int_ {- \infty} ^ {\infty} Y (j \Omega) \sum_ {n = - \infty} ^ {\infty} u _ {0} (j \omega - j \Omega - j n \omega_ {0}) d \Omega \\ = \frac {1}{T _ {s}} \sum_ {n = - \infty} ^ {\infty} Y (j \omega - j n \omega_ {0}). \tag {9.6} \\ \end{array}
$$

Equation 9.6 is illustrated in Figure 9.6. The spectrum of the sampled waveform reproduces $Y(j\omega)$ (for $n = 0$ ) but adds to it replicas displaced in frequency by $n\omega_0$ , $n = \pm 1, \pm 2, \ldots$ . These replicas are known as aliases.

If the spectrum $Y(j\omega)$ is band-limited to $\omega_{0}/2$ —i.e., is zero for $|\omega| > \omega_{0}/2$ —we see from Figure 9.6 that the aliases do not overlap. In that case, an ideal low-pass filter (or, practically, one that approaches it) will recover $Y(j\omega)$ without error. This result is due to Nyquist; if $Y(j\omega)$ is band-limited to $\Omega_{0}$ , then $\omega_{0} = 2\Omega_{0}$ is called the Nyquist rate, corresponding to the signal $y(t)$ .

![](image/ca57018c0d4a53b86f595c597435f3d8dd0efb0e0a46732c99218e780863bc02.jpg)

<details>
<summary>text_image</summary>

Y(jω)
-ω₀/2
ω₀/2 ω
</details>

![](image/c29f82026a4cab6b5292d54d508b9e1069a98888bcf606e7cdd6aab5febd93bc.jpg)

<details>
<summary>text_image</summary>

1/Ts Y(jω + jω0)
-ω0
1/Ts Y(jω)
Y*(jω)
1/Ts Y(jω - jω0)
ω0
</details>

Figure 9.6 The spectrum of a signal and of the signal multiplied by a periodic string of unit impulses

If, on the other hand, the aliases do overlap, it will not be possible to recover $y(t)$ unless more than spectral information is given about the signal. The practical lesson is that we should ensure that the signal being sampled has negligible content at frequencies greater than half the sampling frequency, even if it proves necessary to filter away some of the spectrum before sampling.

![](image/b1daa106f2504159706c81d8350aa4ee1292e35e42b87566d0ae3e356a4eaa7f.jpg)
