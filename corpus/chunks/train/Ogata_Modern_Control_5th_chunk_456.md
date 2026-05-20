Application of the Mapping Theorem to the Stability Analysis of Closed-Loop Systems. For analyzing the stability of linear control systems, we let the closed contour in the s plane enclose the entire right-half s plane. The contour consists of the entire jv axis from $\omega = - \infty$ to ± q and a semicircular path of infinite radius in the right-half s plane. Such a contour is called the Nyquist path. (The direction of the path is clockwise.) The Nyquist path encloses the entire right-half s plane and encloses all the zeros and poles of $1 + G ( s ) H ( s )$ that have positive real parts. [If there are no zeros of $1 + G ( s ) H ( s )$ in the right-half s plane, then there are no closed-loop poles there, and the system is stable.] It is necessary that the closed contour, or the Nyquist path, not pass through any zeros and poles of $1 + G ( s ) H ( s )$ . If $G ( s ) H ( s )$ has a pole or poles at the origin of the s plane, mapping of the point $s = 0$ becomes indeterminate. In such cases, the origin is avoided by taking a detour around it. (A detailed discussion of this special case is given later.)

If the mapping theorem is applied to the special case in which $F ( s )$ is equal to $1 + G ( s ) H ( s )$ , then we can make the following statement: If the closed contour in the s plane encloses the entire right-half s plane, as shown in Figure 7–47, then the number of right-half plane zeros of the function $F ( s ) = 1 + G ( s ) H ( s )$ ) is equal to the number of poles of the function $F ( s ) = 1 + G ( s ) H ( s )$ in the right-half s plane plus the number of clockwise encirclements of the origin of the $1 + G ( s ) H ( s )$ plane by the corresponding closed curve in this latter plane.

Because of the assumed condition that

$$\lim _ {s \rightarrow \infty} [ 1 + G (s) H (s) ] = \text { constant }$$

the function of $1 + G ( s ) H ( s )$ remains constant as s traverses the semicircle of infinite radius. Because of this, whether the locus of $1 + G ( s ) H ( s )$ encircles the origin of the $1 + G ( s ) H ( s )$ plane can be determined by considering only a part of the closed contour in the s plane—that is, the jv axis. Encirclements of the origin, if there are any, occur only while a representative point moves from –jq to ±jq along the jv axis, provided that no zeros or poles lie on the jv axis.

![](image/9cea41453f605a6ccd2f04467385d2be5d32e7a7a8447b98d70852131f9102fa.jpg)

<details>
<summary>text_image</summary>

jω
s Plane
∞
0
σ
</details>

Figure 7–47 Closed contour in the s plane.
