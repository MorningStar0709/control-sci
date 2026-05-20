# Solution

Figure 5.22 shows the pole-zero plot and the $D$ -contour. For $0 < \omega < 1$ , the phase of $L'(s) = (s^2 + 1) / (s - 1)^3$ is

$$- 9 0 ^ {\circ} + 9 0 ^ {\circ} - 3 (1 8 0 ^ {\circ} - \theta) = - 1 8 0 ^ {\circ} + 3 \theta .$$

As $\omega$ approaches 1 from below, the magnitude approaches zero and the phase $-45^{\circ}$ ( $\theta \to 45^{\circ}$ ). The Nyquist locus crosses the origin (odd multiplicity); the magnitude grows, then tends to zero with a phase of $90^{\circ}$ as $\omega \to \infty$ (Fig. 5.22).

The real-axis crossing at $-1$ is for $\omega = 0$ . The other crossing clearly occurs for $\omega > 1$ , where the phase is equal to $3\theta$ . Therefore, the crossing occurs for $\theta = 60^{\circ}$ ,

![](image/aa29cc08c02609c1bcfeb57e569fc16656c9410247464407c4b2e3f24508f790.jpg)

<details>
<summary>text_image</summary>

j
180° - θ
θ
x
-j
-1
</details>

Figure 5.22 Nyquist contour and Nyquist plot, system with zeros on the imaginary axis

or $\omega = \sqrt{3}$ . At that frequency,

$$\left| L ^ {\prime} (j \sqrt {3}) \right| = \frac {| - 3 + 1 |}{(3 + 1) ^ {3 / 2}} = \frac {1}{4}.$$

Since $P = 3$ , we require $N = -3$ for stability. That will take place if $\frac{1}{4} < -\frac{1}{k} < -0$ , or $4 < k < \infty$ .
