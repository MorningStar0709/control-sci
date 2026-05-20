$$> > \text { sysGH } = t f (1, [ 0. 5 4 2 3 3 4 ])\% \text { create } G (s) H (s)> > \text { rlocus(sysGH) }\% \text{ create and draw the root locus}$$

Figure 10.36 shows MATLAB’s construction of the root locus for the closed-loop control system in Fig. 10.35 (the plot has been enhanced by adding the asymptotes and text labels). The three open-loop poles are clearly identified by the “×” markers. One closed-loop root begins at the open-loop pole $p _ { 1 } = - 2$ (for $K _ { P } = 0 )$ ) and moves left along the negative real axis as the gain is increased. No closed-loop roots lie on the real axis to the right of $p _ { 1 } = - 2$ as expected. The other two closed-loop roots begin at the open-loop complex conjugate pairs $p _ { 2 , 3 } = - 3 \pm j 5$ (again with $K _ { P } = 0 )$ and move to the right as the gain is increased. Eventually, these two complex closed-loop poles follow the $\pm 6 0 ^ { \circ }$ asymptotes.

Once we have the root locus (either by sketch or from MATLAB), we can interpret the effect that varying the proportional gain $K _ { P }$ has on the closed-loop transient response and closed-loop stability. Figure 10.36 shows that as the gain is increased, the two complex roots move to the right, cross the imaginary axis, and eventually follow the $\pm 6 0 ^ { \circ }$ asymptotes. Because the real part of these two roots is approaching zero, the associated settling time is increasing, which means that the closed-loop response is becoming slower as the gain increases. Furthermore, the closed-loop damping ratio $\zeta$ associated with the two complex roots decreases (as gain increases) as the complex roots approach the imaginary axis. By contrast, the closed-loop pole emanating from $p _ { 1 } = - 2$ moves to the left as gain increases and hence its contribution to the transient response exhibits a decreasing (shorter) settling time. As an example, we can use MATLAB to compute the closed-loop roots for the gain $K _ { P } = 3 0 :$ :

![](image/9c0b95f237fc0fb8a098b27c86acf4f7337c99d787d13e57c48f5cafda785e0f.jpg)

<details>
<summary>line</summary>

| Real Axis | Imaginary Axis | Trajectory Type |
| --- | --- | --- |
| -3 | 5 | Curve |
| -2 | 0 | Curve |
| -3 | -5 | Curve |
| 2 | -10 | Curve |
| 0 | 0 | Asymptote |
| 0 | 0 | Right-half plane |
| -3 | 0 | Left-half plane |
</details>

Figure 10.36 Root-locus plot for Example 10.10.

$$K _ {P} = 3 0: \text { closed - loop roots are } s _ {1} = - 4. 2 5 7 3, s _ {2, 3} = - 1. 8 7 1 4 \pm j 5. 1 5 4 0$$
