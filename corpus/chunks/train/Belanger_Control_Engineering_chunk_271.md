# Solution

Figure 5.19 shows the D-contour. The Nyquist plot of $L'(s) = 1/[s(s + 1)^{2}]$ is sketched in Figure 5.20. This plot is not to scale due to the difficulty of showing both the large semicircle and the detail near the origin.

From Figure 5.19, we see that there are no open-loop poles inside the D-contour, so P = 0 and we need N = 0 for stability. From Figure 5.20, this will be the case if 0 < k < 2.

![](image/99cab0878ce7ba88d29d6ef3d8576c74621dbf0571e1858f931ead9da29f5f59.jpg)

<details>
<summary>text_image</summary>

-1
x
je
ε
-jε
</details>

Figure 5.19 Indented Nyquist contour

![](image/1e9da225c831b0345713305b6cc0d04640fe800e156cd84a339f546ca484ff53.jpg)

<details>
<summary>text_image</summary>

-2
</details>

Figure 5.20 The Nyquist plot

Example 5.13 Sketch the Nyquist plot for $L(s) = k\frac{(s + 1)}{s^2}$ , and determine the range of $k$ for stability. Solution Figure 5.21 shows the $D$ -contour and the Nyquist plot of $L'(s) = (s + 1)/s^2$ . The phase at $\omega = \rho$ is $-180^\circ + \tan^{-1}\rho$ , so the point $s = j\rho$ maps into $0+$ , slightly below the negative real axis. As $\omega$ increases, the phase increases (because of the zero) and the magnitude decreases, with the given result. To map the small semicircle, we use the fact that, at $s = -j\rho$ , the D-contour takes a $90^{\circ}$ right turn and, because of the double pole, goes through nearly (but not quite) $360^{\circ}$ .

![](image/ae1b63c58b9468d125839a4e5166ecab1ac1e1e7aa0b8be39431795aa2917c6c.jpg)

<details>
<summary>text_image</summary>

-1
-jp
jp
O-
O+
</details>

Figure 5.21 Nyquist contour and Nyquist plot, system with a double pole at s = 0

There are no open-loop poles within the S-contour, so N = 0 for stability. This will occur if the $(-1/k, 0)$ point is located anywhere on the negative real axis—i.e., if any k > 0.
