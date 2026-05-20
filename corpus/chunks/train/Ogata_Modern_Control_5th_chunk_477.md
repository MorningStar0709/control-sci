Proper phase and gain margins ensure us against variations in the system components and are specified for definite positive values.The two values bound the behavior of the closed-loop system near the resonant frequency. For satisfactory performance, the phase margin should be between $3 0 ^ { \circ }$ and $6 0 ^ { \circ } .$ , and the gain margin should be greater than 6 dB. With these values, a minimum-phase system has guaranteed stability, even if the openloop gain and time constants of the components vary to a certain extent. Although the phase and gain margins give only rough estimates of the effective damping ratio of the closed-loop system, they do offer a convenient means for designing control systems or adjusting the gain constants of systems.

Figure 7–68 Polar plots showing more than two phase or gain crossover frequencies.   
![](image/e389e800f5bbe653bc685226c2e6bcf7712200c8fd2c6fc9d54ff3ccac3dfc71.jpg)

<details>
<summary>text_image</summary>

Phase crossover
frequencies
(ω₁, ω₂, ω₃)
ω = ∞
ω₃ ω₂ ω₁
Re
ω = ∞
ω₁ ω₂ ω₃
Gain crossover
frequencies
(ω₁, ω₂, ω₃)
ω
0
Im
Im
Re
</details>

For minimum-phase systems, the magnitude and phase characteristics of the openloop transfer function are definitely related.The requirement that the phase margin be between $3 0 ^ { \circ }$ and $6 0 ^ { \circ }$ means that in a Bode diagram the slope of the log-magnitude curve at the gain crossover frequency should be more gradual than –40 dBdecade. In most practical cases, a slope of –20 dBdecade is desirable at the gain crossover frequency for stability. If it is –40 dBdecade, the system could be either stable or unstable. (Even if the system is stable, however, the phase margin is small.) If the slope at the gain crossover frequency is –60 dBdecade or steeper, the system is most likely unstable.

For nonminimum-phase systems, the correct interpretation of stability margins requires careful study.The best way to determine the stability of nonminimum-phase systems is to use the Nyquist diagram approach rather than Bode diagram approach.
