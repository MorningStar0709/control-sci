The Nyquist plots of the open-loop transfer function with a small value of K and a large value of K are shown in Figure 7–54.The number of poles of $G ( s ) H ( s )$ in the right-half s plane is zero.

![](image/fc176a60d7f27da8736325d8deb39d5e93cb75c2150aef141d9cb5e71022d242.jpg)

<details>
<summary>text_image</summary>

Im
ω = 0-
GH Plane
P = 0
N = 0
Z = 0
ω = ∞
-1
ω = -∞
(Stable)
ω = 0+
Re
</details>

Small K

![](image/d4696f3d366b225d4286f04803beea74e097567283a1f847c4a84836962ca073.jpg)

<details>
<summary>text_image</summary>

Im
ω = 0 -
GH Plane
P = 0
N = 2
Z = 2
ω = ∞
-1
ω = -∞
Re
(Unstable)
ω = 0+
ω = 0+
</details>

Large K   
Figure 7–54   
Polar plots of the system considered in Example 7–15.

Therefore, for this system to be stable, it is necessary that $N = Z = 0$ or that the $G ( s ) H ( s )$ locus not encircle the $- 1 + j 0$ point.

For small values of K, there is no encirclement of the $- 1 + j 0$ point. Hence, the system is stable for small values of K. For large values of K, the locus of $G ( s ) H ( s )$ encircles the $- 1 + j 0$ point twice in the clockwise direction, indicating two closed-loop poles in the right-half s plane, and the system is unstable. (For good accuracy, K should be large. From the stability viewpoint, however, a large value of K causes poor stability or even instability.To compromise between accuracy and stability, it is necessary to insert a compensation network into the system. Compensating techniques in the frequency domain are discussed in Sections 7–11 through 7–13.)
