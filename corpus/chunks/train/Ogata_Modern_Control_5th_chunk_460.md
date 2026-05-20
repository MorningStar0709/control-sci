Special Case when $G ( s ) H ( s )$ Involves Poles and/or Zeros on the jV Axis. In the previous discussion, we assumed that the open-loop transfer function $G ( s ) H ( s )$ ) has neither poles nor zeros at the origin.We now consider the case where $G ( s ) H ( s )$ involves poles and/or zeros on the $j \omega$ axis.

Since the Nyquist path must not pass through poles or zeros of $G ( s ) H ( s )$ , if the function $G ( s ) H ( s )$ has poles or zeros at the origin (or on the jv axis at points other than the origin), the contour in the s plane must be modified. The usual way of modifying the contour near the origin is to use a semicircle with the infinitesimal radius e, as shown in Figure 7–50. [Note that this semicircle may lie in the right-half s plane or in the left-half s plane. Here we take the semicircle in the right-half s plane.] A representative point s moves along the negative jv axis from $- j \infty$ to $j 0 -$ . From $s = j 0 - \tan s = j 0 +$ , the point moves along the semicircle of radius e (where $\varepsilon \ll 1 )$ and then moves along the positive $j \omega$ axis from $j 0 + \mathrm { t o } j \infty .$ . From $s = j \infty ,$ the contour follows a semicircle with infinite radius, and the representative point moves back to the starting point, $s = - j \infty$ .The area that the modified closed contour avoids is very small and approaches zero as the radius e approaches zero. Therefore, all the poles and zeros, if any, in the right-half s plane are enclosed by this contour.

Consider, for example, a closed-loop system whose open-loop transfer function is given by

$$G (s) H (s) = \frac {K}{s (T s + 1)}$$

The points corresponding to $s = j 0 +$ and $s = j 0 -$ on the locus of $G ( s ) H ( s )$ in the $G ( s ) H ( s )$ plane are $- j \infty$ and $j \infty .$ , respectively. On the semicircular path with radius e (where $\varepsilon \ll 1 )$ ), the complex variable s can be written

$$s = \varepsilon e ^ {j \theta}$$

where u varies from $- 9 0 ^ { \circ } ~ \mathrm { t o }  9 0 ^ { \circ }$ . Then $G ( s ) H ( s )$ becomes

$$G \left(\varepsilon e ^ {j \theta}\right) H \left(\varepsilon e ^ {j \theta}\right) = \frac {K}{\varepsilon e ^ {j \theta}} = \frac {K}{\varepsilon} e ^ {- j \theta}$$

![](image/4eea4c6ff4b68d17c0b33c2ecc2c0a1b7688dd0b162cbce318e76712d738999c.jpg)

<details>
<summary>text_image</summary>

jω
s Plane
j0+
ε
0
σ
j0-
jω
s Plane
∞
s = ε e^{jθ}
σ
</details>

Figure 7–50 Contour near the origin of the s plane and closed contour in the s plane avoiding poles and zeros at the origin.
