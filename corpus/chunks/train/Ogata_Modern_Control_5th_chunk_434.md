# 7–3 POLAR PLOTS

The polar plot of a sinusoidal transfer function $G ( j \omega )$ is a plot of the magnitude of $G ( j \omega )$ versus the phase angle of $G ( j \omega )$ on polar coordinates as v is varied from zero to infinity. Thus, the polar plot is the locus of vectors $\left| G ( j \omega ) \right| / \left| G ( j \omega ) \right.$ as v is varied from zero to infinity. Note that in polar plots a positive (negative) phase angle is measured counterclockwise (clockwise) from the positive real axis.The polar plot is often called the Nyquist plot.An example of such a plot is shown in Figure 7–25. Each point on the polar plot of $G ( j \omega )$ represents the terminal point of a vector at a particular value of v. In the polar plot, it is important to show the frequency graduation of the locus. The projections of $G ( j \omega )$ on the real and imaginary axes are its real and imaginary components.

![](image/6c2318b2efa7880c150c3ef95dc15bb88b5e1be973fa7bb341c7eacb14b30a7b.jpg)

<details>
<summary>text_image</summary>

Im
Re[G(jω)]
ω = ∞
G(jω)
Im[G(jω)]
ω₁
ω₂
ω₃
G(jω)
Re
ω = 0
</details>

Figure 7–25 Polar plot.

MATLAB may be used to obtain a polar plot $G ( j \omega )$ or to obtain $\left| G ( j \omega ) \right|$ and @ $/ G ( j \omega )$ accurately for various values of v in the frequency range of interest.

An advantage in using a polar plot is that it depicts the frequency-response characteristics of a system over the entire frequency range in a single plot. One disadvantage is that the plot does not clearly indicate the contributions of each individual factor of the open-loop transfer function.

Integral and Derivative Factors $( j \omega ) ^ { \mp 1 }$ . The polar plot of $G ( j \omega ) = 1 / j \omega$ is the negative imaginary axis, since

$$G (j \omega) = \frac {1}{j \omega} = - j \frac {1}{\omega} = \frac {1}{\omega} \angle - 9 0 ^ {\circ}$$

The polar plot of $G ( j \omega ) = j \omega$ is the positive imaginary axis.

First-Order Factors $( 1 + j \omega T ) ^ { \mp 1 }$ . For the sinusoidal transfer function

$$G (j \omega) = \frac {1}{1 + j \omega T} = \frac {1}{\sqrt {1 + \omega^ {2} T ^ {2}}} \left\lfloor - \tan^ {- 1} \omega T \right.$$

the values of $G ( j \omega )$ at v=0 and $\omega = 1 / T$ are, respectively,

$$G (j 0) = 1 \underline {{\left/ 0 ^ {\circ} \left. \right.}} \quad \text { and } \quad G \left(j \frac {1}{T}\right) = \frac {1}{\sqrt {2}} \underline {{\left/ - 4 5 ^ {\circ} \left. \right.}}$$
