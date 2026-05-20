# 9.2.3 The Zero-Order Hold

As shown in Figure 9.2, the sampled signal is converted to analog form by “holding” the most recent value. This process is entirely equivalent to passing an impulse-sampled waveform through the linear system whose impulse response is shown in Figure 9.3b, known as a zero-order hold (ZOH). The transfer function corresponding to that impulse response is

$$H _ {Z O H} (s) = \frac {1 - e ^ {- s T _ {s}}}{s} \tag {9.7}$$

or

$$
\begin{array}{l} H _ {Z O H} (j \omega) = e ^ {- j \omega (T _ {s} / 2)} \frac {e ^ {j \omega (T _ {s} / 2)} - e ^ {- j \omega (T s / 2)}}{j \omega} \\ = 2 \sin \left(\omega \frac {T _ {s}}{2}\right) \frac {e ^ {- j \omega (T _ {s} / 2)}}{\omega}. \tag {9.8} \\ \end{array}
$$

Thus,

$$\left| H _ {Z O H} (j \omega) \right| = \frac {2}{\omega} \sin \omega \frac {T _ {s}}{2}\neq H _ {Z O H} (j \omega) = - \omega \frac {T _ {s}}{2}. \tag {9.9}$$

Figure 9.8 shows the magnitude; it is seen to be low-pass in character. The phase is the same as that of a pure delay, $T_{s}/2$ .   
![](image/62c56647609f83b1d19b9bb113972a5aaca9aa0407a0d2c0b117ff891e68c973.jpg)

<details>
<summary>line</summary>

| ω·Ts/2 | Mag. H(j·ω)/Ts |
| --- | --- |
| 0 | 1.0 |
| 2 | 0.5 |
| 4 | 0.2 |
| 6 | 0.0 |
| 8 | 0.1 |
| 10 | 0.0 |
| 12 | 0.1 |
| 14 | 0.0 |
| 16 | 0.1 |
| 18 | 0.0 |
| 20 | 0.1 |
</details>

Figure 9.8 Magnitude of the spectrum of the zero-order hold

If aliasing effects are to be minimized, it is necessary that (i) the sampling frequency be at least twice as high as the highest frequency of significance in the signal and (ii) the impulse-sampled signal be low-pass filtered to attenuate the aliases. The ZOH is seen to have the desired low-pass characteristics. Other hold devices may be closer to an ideal low-pass filter (unity in the passband, zero outside) than the ZOH (see Problems 9.3 and 9.4).
