![](image/2b8fcd957d3cd65b72bfbfee9c936381b4805124cdbe267f71047736cfa99a34.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Magnitude, dB (ζ = 0.1) | Magnitude, dB (ζ = 0.3) | Magnitude, dB (ζ = 0.5) | Magnitude, dB (ζ = 0.7) | Magnitude, dB (ζ = 0.9) |
| --- | --- | --- | --- | --- | --- |
| 10^0 | ~0 | ~0 | ~0 | ~0 | ~0 |
| 10^1 | ~15 | ~5 | ~2 | ~1 | ~0.5 |
| 10^2 | ~-40 | ~-20 | ~-10 | ~-5 | ~-2 |
</details>

![](image/9b52f5dfea13261a12d2efddb454cc567e3ab2ae6d64c17dbb373b33cce0032a.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Phase, deg (ζ = 0.1) | Phase, deg (Increasing ζ) |
| --- | --- | --- |
| 10^0 | 0 | 0 |
| 10^1 | -90 | -90 |
| 10^2 | -180 | -180 |
</details>

Figure 9.25 Bode diagram of second-order system 100 $/ ( s ^ { 2 } + 2 0 \zeta s + 1 0 0 )$ ).

4. The peak magnitude increases as damping ratio $\zeta$ is decreased.   
5. The phase angle $\phi$ starts at $0 ^ { \circ }$ for low frequencies and asymptotically approaches $- 1 8 0 ^ { \circ }$ at high frequencies.   
6. The phase angle shows a sharper transition from $0 ^ { \circ }$ to $- 1 8 0 ^ { \circ }$ as damping ratio $\zeta$ is decreased.   
7. The phase angle $\phi = - 9 0 ^ { \circ }$ when the input frequency is the corner frequency $\omega _ { c }$

The above summary tells us that the Bode diagram of a second-order system is essentially the “double” of the Bode diagram of a first-order system; that is, the high-frequency asymptote slope is doubled and the total phase shift is doubled. A key difference, however, between first- and second-order Bode diagrams is that the shapes of the magnitude and phase plots for a second-order system are greatly affected by the damping ratio $\zeta .$ . Lightly damped systems exhibit a peak magnitude or resonant peak at a particular input frequency that is less than the corner frequency $\omega _ { n }$ . The frequency at which the maximum magnitude occurs is called the resonant frequency and is

$$\omega_ {r} = \omega_ {n} \sqrt {1 - 2 \zeta^ {2}} \tag {9.52}$$

The derivation of Eq. (9.52) can be found in Reference 1. As damping ratio $\zeta  0 .$ , Eq. (9.52) tells us that the resonant frequency $\omega _ { r }  \omega _ { n }$ , which can be observed in Fig. 9.25. Because the radicand in Eq. (9.52) is less than or equal to one, the resonant frequency will always be less than the corner frequency $\omega _ { n } .$ . Finally, note that if damping ratio $\zeta > 0 . 7 0 7 1$ a resonant peak does not exist and there is no resonant frequency.
