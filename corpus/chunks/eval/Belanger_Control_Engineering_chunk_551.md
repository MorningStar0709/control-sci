# 9.6.3 The Nyquist Criterion

The principle of the argument applies to the z-plane as well as to the s-plane. This time, however, the D-contour is replaced by the unit circle, and we require all closed-loop poles to be inside, for stability. As before, infinitesimal indentations are made to avoid poles on the unit circle, and these map into circles or semicircles of infinite radii.

![](image/53af5a80d7b0d192e0408e17117e6edb15b9c09eabfb30e4fe9f09ae09e1aad0.jpg)

<details>
<summary>scatter</summary>

| Real Axis | Imaginary Axis |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.0 |
</details>

Figure 9.10a Root locus for Example 9.10, positive gain

The map of the unit circle is $P(e^{j\omega})$ , $0 \leq \omega \leq 2\pi$ . Since $e^{j(2\pi - \omega)} = e^{-j\omega}$ , the lower half of the unit circle ( $2\pi - 0$ to $2\pi - \pi$ ) maps into $P(e^{-j\omega}) = P^{*}(e^{j\omega})$ , just as the lower half of the $D$ -contour in the $s$ -plane maps into the complex conjugate of the map of the top half. Since $e^{j\omega}$ is periodic with a period of $2\pi$ , $P(e^{j\omega})$ is also periodic. This represents a major difference from the situation in continuous time, since the notion of roll-off is no longer meaningful. It is possible—in fact, usual—to use $z = e^{j\omega T_s}$ , where $T_s$ is the sampling period, and to plot $P(e^{j\omega T_s})$ , $0 \leq \omega \leq 2\pi / T_s$ . This also maps the unit circle, but $\omega$ is now related to the time base of sampled plant. The frequency $2\pi / T_s$ is half the Nyquist frequency (MATLAB dynquist).

Discrete-time Bode diagrams may also be plotted, for $0 \leq \omega \leq \pi / T_{s}$ (MATLAB dbode). There is no equivalent here of the low- and high-frequency asymptotic straight lines of the continuous-time plots; the Bode plot must be computed point by point.

![](image/b804d4265244c1e3eef7aaa81f523f63c1dc30cce2fc69c1e16bcbc4f7d67d2b.jpg)

<details>
<summary>scatter</summary>

| Real Axis | Imaginary Axis |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.0 |
</details>

Figure 9.10b Root locus for Example 9.10, negative gain
