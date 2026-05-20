$$G (j \omega) = \frac {1}{1 + 2 \zeta \left(j \frac {\omega}{\omega_ {n}}\right) + \left(j \frac {\omega}{\omega_ {n}}\right) ^ {2}}, \quad \text { for } \zeta > 0$$

are given, respectively, by

$$\lim _ {\omega \rightarrow 0} G (j \omega) = 1 \underline {{{/ 0 ^ {\circ}}}} \quad \text { and } \quad \lim _ {\omega \rightarrow \infty} G (j \omega) = 0 \underline {{{/ - 1 8 0 ^ {\circ}}}}$$

The polar plot of this sinusoidal transfer function starts at $1 / 0 ^ { \circ }$ and ends at $0 / { - } 1 8 0 ^ { \circ }$ as v increases from zero to infinity. Thus, the high-frequency portion of $G ( j \omega )$ is tangent to the negative real axis.

Figure 7–28 Polar plots of $\frac { 1 } { 1 + 2 \zeta \left( j \frac { \omega } { \omega _ { n } } \right) + \left( j \frac { \omega } { \omega _ { n } } \right) ^ { 2 } } \mathrm { f o r } \zeta > 0 .$ v 1 v   
![](image/9a076b058d8190eb5e19f4cd0e82d8ed99ab755fac6c6f8e8be57c695104a22f.jpg)

<details>
<summary>text_image</summary>

Im
ω = ∞
0
1
Re
ω = 0
ωₙ
(ζ: Large)
ωₙ
ωₙ
(ζ: Small)
</details>

Examples of polar plots of the transfer function just considered are shown in Figure 7–28. The exact shape of a polar plot depends on the value of the damping ratio $\zeta ,$ , but the general shape of the plot is the same for both the underdamped case $( 1 > \zeta > 0 )$ and overdamped case $( \zeta > 1 )$ .

For the underdamped case at $\omega = \omega _ { n }$ , we have $G ( j \omega _ { n } ) = 1 / ( j 2 \zeta )$ , and the phase angle at $\omega = \omega _ { n } \mathrm { i s } - 9 0 ^ { \circ }$ . Therefore, it can be seen that the frequency at which the $G ( j \omega )$ locus intersects the imaginary axis is the undamped natural frequency $\omega _ { n }$ . In the polar plot, the frequency point whose distance from the origin is maximum corresponds to the resonant frequency $\omega _ { r }$ . The peak value of $G ( j \omega )$ is obtained as the ratio of the magnitude of the vector at the resonant frequency $\omega _ { r }$ to the magnitude of the vector at $\omega = 0$ . The resonant frequency $\omega _ { r }$ is indicated in the polar plot shown in Figure 7–29.

For the overdamped case, as $\zeta$ increases well beyond unity, the $G ( j \omega )$ locus approaches a semicircle. This may be seen from the fact that, for a heavily damped system, the characteristic roots are real, and one is much smaller than the other. Since, for sufficiently large $\zeta ,$ , the effect of the larger root (larger in the absolute value) on the response becomes very small, the system behaves like a first-order one.
