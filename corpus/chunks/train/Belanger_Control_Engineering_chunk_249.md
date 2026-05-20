$$\neq G (s ^ {*}) = 1 8 0 ^ {\circ} \pm k 3 6 0 ^ {\circ} \tag {5.13}$$

where $k$ is an integer. Let $s^*$ be a point on the real axis.

From Figure 5.2 we observe that: (i) the net contribution of the complex conjugate poles and zeros to $\neq G(s^{*})$ is zero; (ii) real poles and zeros to the left of $s^{*}$ contribute $0^{\circ}$ ; (iii) each zero to the right of $s^{*}$ contributes $180^{\circ}$ , and each pole $-180^{\circ}$ . Since $+180^{\circ}$ and $-180^{\circ}$ are the same,

$$
\begin{array}{l} \neq G (s ^ {*}) = \text { contributions   of   complex   poles   and   zeros } \\ + \text {   contributions   of   real   poles   and   zeros   left   of   } s ^ {*} \\ + \text {   contributions   of   real   poles   and   zeros   right   of   } s ^ {*} \\ = 1 8 0 ^ {\circ} [ \text { number   (N.)   of   real   poles   right   of } s ^ {*} \\ + \mathrm{N.of~real~zeros~right~of} s ^ {*} ]. \\ \end{array}
$$

![](image/27d03f9af6c1b307349470d79b95724abdf06fcf97577dc0c2d481720d71a49f.jpg)

<details>
<summary>text_image</summary>

0°
s*
θ₁
-θ₁
180° 180°
x
θ₁
</details>

Figure 5.2 Pertaining to the angle of a transfer function at a point on the real axis

To satisfy Equation 5.13, the total of the number of real poles plus the number of real zeros to the right of $s^*$ must be odd.

For $k < 0$ , it can be shown that a real-axis point belongs to the Root Locus in the total number of poles and zeros to its right is even (including zero).

Rule 3 As $k \to \infty$ , the branches tend to straight-line asymptotes radiating from a common point, or centroid, on the real axis. The location of the centroid is given by

$$\sigma = \frac {\Sigma \text { poles of } G - \Sigma \text { zeros of } G}{\mathrm{N.ofpoles-N.ofzeros}} \tag {5.14}$$

and the asymptote angles are

$$\neq s = \frac {1 8 0 ^ {\circ} \pm k 3 6 0 ^ {\circ}}{\mathrm{N.ofzeros-N.ofpoles}} \tag {5.15}$$

where $k$ is an integer. If the number of poles equals the number of zeros, there are no asymptotes.

For the proof of the result on the centroid, we refer the reader to Shinners [3]. The result on angles is established from Equation 5.7. From Figure 5.3, if $s^*$ is a Root Locus point far from the origin, the angles of the vectors from the poles and zeros to $s^*$ are all approximately equal to $\neq s^*$ . Using Equation 5.13,

$$\neq G (s ^ {*}) = (\mathrm{N.ofzeros-N.ofpoles}) \neq s ^ {*} = 1 8 0 ^ {\circ} \pm k 3 6 0 ^ {\circ}$$

and the result follows.

For $k < 0$ , the centroid result also holds, and $180^{\circ}$ in the numerator of Equation 5.15 is removed.
