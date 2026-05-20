# Remarks on the Nyquist Stability Criterion

1. This criterion can be expressed as

$$Z = N + P$$

where number of zeros of Z = $1 + G ( s ) H ( s )$ in the right-half s plane

number of clockwise encirclements of the –1+j0 point N =

number of poles of G(s)H(s) in the right-half s plane P =

If P is not zero, for a stable control system, we must have $Z = 0 , \mathrm { o r } N = - P$ , which means that we must have P counterclockwise encirclements of the $- 1 + j 0$ point.

If $G ( s ) H ( s )$ does not have any poles in the right-half s plane, then $Z = N$ . Thus, for stability there must be no encirclement of the $- 1 + j 0$ point by the $G ( j \omega ) H ( j \omega )$ locus. In this case it is not necessary to consider the locus for the entire jv axis, only for the positive-frequency portion. The stability of such a system can be determined by seeing if the $- 1 + j 0$ point is enclosed by the Nyquist plot of $G ( j \omega ) H ( j \omega )$ . The region enclosed by the Nyquist plot is shown in Figure 7–49. For stability, th $\div - 1 + j 0$ point must lie outside the shaded region.

2. We must be careful when testing the stability of multiple-loop systems since they may include poles in the right-half s plane. (Note that although an inner loop may be unstable, the entire closed-loop system can be made stable by proper design.) Simple inspection of encirclements of the $- 1 + j 0$ point by the $G ( j \omega ) H ( j \omega )$ locus is not sufficient to detect instability in multiple-loop systems. In such cases, however, whether any pole of $1 + G ( s ) H ( s )$ is in the right-half s plane can be determined easily by applying the Routh stability criterion to the denominator of $G ( s ) H ( s )$ .

If transcendental functions, such as transport lag $e ^ { - T s }$ , are included in $G ( s ) H ( s )$ they must be approximated by a series expansion before the Routh stability criterion can be applied.

3. If the locus of $G ( j \omega ) H ( j \omega )$ passes through the $- 1 + j 0$ point, then zeros of the characteristic equation, or closed-loop poles, are located on the jv axis. This is not desirable for practical control systems. For a well-designed closed-loop system, none of the roots of the characteristic equation should lie on the jv axis.

![](image/06a825e44bd39208c1131208b82adf4f7baa79d03dac8bee662aeae36a086daa.jpg)

<details>
<summary>text_image</summary>

Im
GH Plane
-1 0 Re
</details>

Figure 7–49 Region enclosed by a Nyquist plot.
