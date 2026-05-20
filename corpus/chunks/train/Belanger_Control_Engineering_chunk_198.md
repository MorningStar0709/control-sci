# Example 4.3

The plant (and hence $H_{d}$ ) has a real RHP zero at $s = x_{0}$ . The function $W(j\omega)$ is to have the form shown in Figure 4.13. $^{1}$ Derive, and discuss, the relationship enforced by Equation 4.24 between A, B, and $\omega_{b}$ .

![](image/4f036a8e7e237f2e69540a967e06e47e97b3c4877db01dd4aec34a8ed9cb0642.jpg)

<details>
<summary>line</summary>

| ω - y₀ | Value of f (x₀ = 5) | Value of f (x₀ = 1) | Value of f (x₀ = 2) |
| --- | --- | --- | --- |
| -5 | ~0.0 | ~0.0 | ~0.0 |
| -4 | ~0.0 | ~0.0 | ~0.0 |
| -3 | ~0.0 | ~0.0 | ~0.0 |
| -2 | ~0.0 | ~0.0 | ~0.0 |
| -1 | ~0.4 | ~0.6 | ~0.3 |
| 0 | 2.0 | 1.0 | 0.5 |
| 1 | ~0.4 | ~0.6 | ~0.3 |
| 2 | ~0.0 | ~0.0 | ~0.0 |
| 3 | ~0.0 | ~0.0 | ~0.0 |
| 4 | ~0.0 | ~0.0 | ~0.0 |
| 5 | ~0.0 | ~0.0 | ~0.0 |
</details>

Figure 4.12 Frequency weighting function

![](image/c040bc15e37c2e92349580f65ae62963a6a0c37732ad599aa29d5beacc3dfede.jpg)

<details>
<summary>line</summary>

| w | w(jw) |
| --- | --- |
| -w_b | 1 |
| w_b | 1 |
</details>

Figure 4.13 Frequency response function used to illustrate frequency-domain tradeoffs

Solution First, note that

$$f (z _ {0}, \omega) = \frac {x _ {0}}{x _ {0} ^ {2} + (y _ {0} - \omega) ^ {2}} = \frac {- d}{d \omega} \tan^ {- 1} \frac {y _ {0} - \omega}{x _ {0}}$$

so that Equation 4.24 becomes

$$
\begin{array}{l} \frac {2}{\pi} \left[ - \int_ {0} ^ {\omega_ {b}} \log B \frac {- d}{d \omega} \tan^ {- 1} \left(\frac {y _ {0} - \omega}{x _ {0}}\right) d \omega \right. \\ \left. - \int_ {\omega_ {b}} ^ {\infty} \log A \frac {d}{d \omega} \tan^ {- 1} \left(\frac {y _ {0} - \omega}{x _ {0}}\right) d \omega \right] = 0 \\ \end{array}
$$

where the fact that both $\log |W(j\omega)|$ and $f(z_0, \omega)$ are even has been used. Using also the fact that $y_0 = 0$ yields

$$\log B \tan^ {- 1} \frac {\omega_ {b}}{x _ {0}} + \log A \left(\frac {\pi}{2} - \tan^ {- 1} \frac {\omega_ {b}}{x _ {0}}\right) = 0$$

or

$$\log A = \frac {\tan^ {- 1} \omega_ {b} / x _ {0}}{\pi / 2 - \tan^ {- 1} \omega_ {b} / x _ {0}} (- \log B)$$

which is the required expression. Note that $B < 1$ , so that $-\log B$ is positive. Making $B$ smaller ( $-\log B$ larger) forces $\log A$ to increase; a small $|W(j\omega)|$ in the passband must be compensated by a large value outside the passband.
