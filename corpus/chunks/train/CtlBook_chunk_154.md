# 5.4.7 Bode Asymptotic Phase Plot

We will derive the Bode Asymptotic Phase Plot the same way as the magnitude: by considering three values of ω relative to the pole or zero.

Single Pole Again, we start by looking at a simple transfer function consisting of one pole:

$$G (s) = \frac {1}{(s + a)}$$

In all frequency response analysis we assume that $R e ( p ) < 0 .$ . For now we assume $I m ( p ) = 0$ . We consider $s = j \omega$ and there are three values of ω which are relevant. The Bode phase plot uses a linear vertical axis for the phase angle (but uses the same $\log ( \omega )$ horizontal axis).

$1 . \ \omega < < | a |$   
$2 , \ \omega = | a |$   
$3 . \ \omega > > \ | a |$

For each region of the three regions, as we plug $s = j \omega$ into $\frac { 1 } { ( s + a ) }$ , we approximate $| G ( j \omega ) |$ as

1. $\angle G ( j \omega ) \approx 0$

![](image/6736c059833024c81611654d18367473bf80c92aafb6893a18ea4a6c9899925d.jpg)

<details>
<summary>line</summary>

| log(w) | G(jω) |
| --- | --- |
| 0 | 0 |
| 10 | -45 |
| 100 | -90 |
</details>

Figure 5.6: Bode Phase Plot of a single pole. Three approximations of increasing accuracy are given. 1) Straight line (step) asymptotes. 2) linear approximation between 0.1a $< \omega < 1 0 a ,$ 3) Smooth curve passing through −45◦ at ω = a.

$\begin{array} { r } { 2 . \angle G ( j \omega ) = \angle \frac { 1 } { a + j a } = - 4 5 ^ { \circ } } \end{array}$   
$3 . \ \angle G ( j \omega ) \approx \angle \frac { 1 } { j \omega } = - 9 0 ^ { \circ }$

If we plot this we get Figure 5.6. The gure shows three increasingly accurate approximations to the true phase curve. Based on the asymptotic approximations above, we get asymptotes which look like a step function which changes from 0◦ to −90◦ as ω increases past a. A better approximation is a linear relationship passing through the points

$$\{\omega = 0. 1 a, \phi = 0 ^ {\circ} \}, \{\omega = a, \phi = - 4 5 ^ {\circ} \}, \{\omega = 1 0 a, \phi = - 9 0 ^ {\circ} \}$$

Finally, by making a smooth curve rst above, and then below the linear approximation we can get quite close to a numerically accurate phase curve. In manual plotting, the intent is not high numerical accuracy, just quick insight. For precise phase curves, the computer is better.

Single Zero By very similar arguments, you can show that a zero such as

$$G (s) = (s + a)$$

Contributes the same type of phase curve except ipped above the $0 ^ { \circ }$ horizontal axis.

Combining Phase Curves Just as we can add the Bode Asymptotic Magnitude plots of several poles and zeros (due to the log() nature of dB), we can add asymptotic phase curves from the dierent poles and zeros of a transfer function because the angles of two complex numbers add together when you multiply them.
