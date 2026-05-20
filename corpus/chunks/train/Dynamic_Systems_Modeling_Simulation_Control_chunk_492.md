| Frequency, ω, rad/s | Phase, deg (τ = 0.05 s, ωc = 20 rad/s) | Phase, deg (τ = 1 s, ωc = 1 rad/s) | Phase, deg (τ = 0.2 s, ωc = 5 rad/s) |
| --- | --- | --- | --- |
| 0.01 | 0 | 0 | 0 |
| 0.1 | -15 | -20 | -30 |
| 1 | -45 | -60 | -75 |
| 10 | -75 | -90 | -90 |
| 100 | -90 | -90 | -90 |
| 1000 | -90 | -90 | -90 |
</details>

Figure 9.18 Bode diagrams of first-order system $1 / ( \tau s + 1 )$ .

$$\tau = 0. 0 5 \mathrm{s}: \quad \omega_ {c} = 2 0 \mathrm{rad/s}\tau = 0. 2 \mathrm{s}: \quad \omega_ {c} = 5 \mathrm{rad/s}\tau = 1 \mathrm{s:} \qquad \omega_ {c} = 1 \mathrm{rad/s}$$

It is also clear from Fig. 9.18 that the phase plot is shifted left or right as the time constant (or corner frequency) is varied. In all cases, the phase angle starts at $0 ^ { \circ }$ at low frequencies and asymptotically approaches $- 9 0 ^ { \circ }$ at high frequencies. The reader should note that the phase angle is $- 4 5 ^ { \circ }$ at the respective corner frequency. In other words, half of the total possible phase lag has occurred when the input frequency matches the corner frequency.

As a final note, we observe that the slope of the high-frequency asymptote remains unchanged despite variations in the DC gain K or time constant ??. Both magnitude plots in Figs. 9.17 and 9.18 show that the high-frequency asymptote drops 20 dB when the input frequency changes by a factor of 10 (a 10-fold factor in frequency is a “decade”). For example, consider the magnitude plot in Fig. 9.18 with $\tau = 1$ s: when ?? = 10 rad/s, the magnitude is −20 dB and when ?? = 100 rad/s, the magnitude has dropped to −40 dB. This characteristic of the high-frequency asymptote for first-order systems is proven in Problem 9.9 at the end of the chapter.

On the basis of the noted observations of Figs. 9.17 and 9.18, we can summarize the basic characteristics of the Bode diagram for a first-order transfer function in the standard form $G ( s ) = K / ( \tau s + 1 )$ :

1. A flat low-frequency asymptote exists with a magnitude of $2 0 \mathrm { l o g } _ { 1 0 } ( K ) \mathrm { d } \mathrm { B }$   
2. A high-frequency asymptote exists with a slope of −20 dB/decade.   
3. The low- and high-frequency asymptotes intersect at the corner frequency $\omega _ { c } = 1 / \tau \mathrm { r a d / s }$   
4. The phase angle $\phi$ starts at $0 ^ { \circ }$ for low frequencies and asymptotically approaches $- 9 0 ^ { \circ }$ at high frequencies.   
5. The phase angle $\phi = - 4 5 ^ { \circ }$ when the input frequency is the corner frequency $\omega _ { c }$

The reader should be able to quickly compute the corner frequency and low-frequency asymptote from the first-order transfer function. For example, given the first-order system

$$G (s) = \frac {4}{s + 8} = \frac {K}{\tau s + 1}$$

we see that the time constant is $\tau = 1 / 8 = 0 . 1 2 5 \mathrm { ~ s ~ }$ and the DC gain is $K = 4 / 8 = 0 . 5$ . Hence, the lowfrequency asymptote is $2 0 \mathrm { l o g } _ { 1 0 } ( 0 . 5 ) = - 6 . 0 2$ dB and the corner frequency is $\omega _ { c } = 1 / \tau = 8$ rad/s.
