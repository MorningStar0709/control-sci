# 5.5.5 The Nyquist Contour for the Case of $j$ -Axis Poles and Zeros

There are practical instances where $L(s)$ has poles or zeros on the imaginary axis, with a pole at the origin being particularly frequent. Some modification must be made, because the principle of the argument does not allow poles or zeros on the s-plane contour.

The D-contour is modified so as to skirt around the j-axis poles and zeros. As shown in Figure 5.18, the contour avoids these poles with detours along semicircles of small radii. The mapping of the D-contour in the L-plane is the frequency response, interrupted by the mappings of the small semicircles.

Semicircles of infinitesimal radii centered on poles map into circular arcs of large radii in the L-plane. Consider a pole of multiplicity m, at s = jy, and write

$$L (s) = \frac {1}{(s - j y) ^ {m}} L _ {1} (s)$$

where $L_{1}(s)$ has no pole or zero at $s = jy$ .

Along the semicircle of radius $\rho$ about $s = jy$ , we have $s = jy + \rho e^{j\theta}$ and

$$L (s) = \frac {1}{\rho^ {m} e ^ {j m \theta}} L _ {1} (j y + \rho e ^ {j \theta}).$$

For very small $\rho, |L_1(jy + \rho e^{j\theta})| \approx |L_1(jy)|$ and

$$| L (s) | \approx \frac {| L _ {1} (j y) |}{\rho^ {m}} \tag {5.21}$$

which is a constant tending to infinity as $\rho \to 0$ . Thus, the mapping is a circular arc of large radius.

As for the phase, we see that $\theta$ in Figure 5.18 increases from $-90^{\circ}$ to $+90^{\circ}$ . This causes $e^{-jm\theta}$ to decrease by $180^{\circ}m$ degrees, causing the semicircle to be traversed in the counterclockwise direction. (The indentation can also be made to the left of the pole, in which case the direction is clockwise.) It is helpful to remember that the mapping is conformal, so that a $90^{\circ}$ right turn in the $D$ contour maps into a $90^{\circ}$ right turn in the $L$ -plane.

To summarize, the infinitesimal semicircle around a pole maps into a circular arc of large radius. The arc runs counterclockwise and goes through an angle of

$$\pi m + \not \prec L _ {1} (j y +) - \not \prec L _ {1} (j y -). \tag {5.22}$$

![](image/e80144abefbe43737de971b6d60ab170ae1d9117b853d842515c949b5b3729a0.jpg)

<details>
<summary>natural_image</summary>

Pure geometric diagram with curved lines and arrows, no text or symbols present
</details>

Figure 5.18 Indented Nyquist contour for the case of imaginary axis poles and zeros
