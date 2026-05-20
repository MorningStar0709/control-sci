6. Find the points where the root loci may cross the imaginary axis. The points where the root loci intersect the jv axis can be found easily by (a) use of Routh’s stability criterion or (b) letting $s = j \omega$ in the characteristic equation, equating both the real part and the imaginary part to zero, and solving for v and K.The values of v thus found give the frequencies at which root loci cross the imaginary axis. The K value corresponding to each crossing frequency gives the gain at the crossing point.   
7. Taking a series of test points in the broad neighborhood of the origin of the s plane, sketch the root loci. Determine the root loci in the broad neighborhood of the jv axis and the origin. The most important part of the root loci is on neither the real axis nor the asymptotes but is in the broad neighborhood of the jv axis and the origin.The shape

![](image/f4dc7f420ffd3305623a090189d64c1eed08283fbeafdf65da400ed4ac4ac204.jpg)

<details>
<summary>text_image</summary>

jω
Angle of departure
φ
θ₁
0
σ
θ₂
</details>

Figure 6–12 Construction of the root locus. [Angle of departure $= 1 8 0 ^ { \circ } -$ $\left( \theta _ { 1 } + \theta _ { 2 } \right) + \phi . ]$

of the root loci in this important region in the s plane must be obtained with reasonable accuracy. (If accurate shape of the root loci is needed, MATLAB may be used rather than hand calculations of the exact shape of the root loci.)

8. Determine closed-loop poles. A particular point on each root-locus branch will be a closed-loop pole if the value of K at that point satisfies the magnitude condition. Conversely, the magnitude condition enables us to determine the value of the gain K at any specific root location on the locus. (If necessary, the root loci may be graduated in terms of K. The root loci are continuous with K.)

The value of K corresponding to any point s on a root locus can be obtained using the magnitude condition, or

$$K = \frac {\text { product of lengths between point } s \text { to poles }}{\text { product of lengths between point } s \text { to zeros }}$$

This value can be evaluated either graphically or analytically. (MATLAB can be used for graduating the root loci with K. See Section 6–3.)
