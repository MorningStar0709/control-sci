Rather than plot the imaginary part versus the real part, a gain-phase plot displays the gain (in decibels) versus the phase (in degrees). This was convenient in the precomputer era, because the gain and phase information could be read directly from Bode plots. Gain-phase plots do offer some advantages over Nyquist plots.

![](image/2b851c6e1822505aa3867eb311a07b6fb9bb216583e614ab8e425393f931e986.jpg)

<details>
<summary>contour</summary>

| Real Range | Imaginary Range | M |
| --- | --- | --- |
| -3 to -0.5 | -1.5 to 1.5 | 1.5 |
| -3 to -0.5 | -1 to 0.5 | 2 |
| -3 to -0.5 | -0.5 to 0.5 | 2.5 |
</details>

Figure 6.9 Constant-M circles

The logarithmic scales make it easier to display widely differing magnitudes; the plot for $kL(j\omega)$ is simply that for $L(j\omega)$ raised by $|k|$ db, because $20|kL(j\omega)| \geqslant 20\log |k| + 20\log |L(j\omega)|$ .

Constant-M contours can also be plotted on the gain-phase plane, since Y and X are expressible in terms of log magnitude and phase. The contours are no longer circles, of course, but are the mapping of circles through a particular nonlinear transformation. Such constant-M contours, together with loci of constant phase of $T(j\omega)$ , constitute a Nichols chart. From a Nichols chart and a gain-phase plot of the loop gain $L(j\omega)$ , we may, for any frequency point, read the magnitude and phase of the closed-loop transmission $T(j\omega)$ . In particular, we can easily ascertain the peak value of $|T(j\omega)|$ in decibels as the M-value of the contour of highest magnitude touched by the locus $L(j\omega)$ .

Since $S = 1 / (1 + L) = L^{-1} / (1 + L^{-1})$ , the behavior of $S$ can be studied on the Nichols chart by plotting the locus of $L^{-1}(j\omega)$ rather than $L(j\omega)$ .
