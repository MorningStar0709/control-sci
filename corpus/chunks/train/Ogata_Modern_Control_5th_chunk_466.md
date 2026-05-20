# EXAMPLE 7–17

Consider the closed-loop system having the following open-loop transfer function:

$$G (s) H (s) = \frac {K}{s (T s - 1)}$$

Determine the stability of the system.

![](image/0eb7bd0c7c72fe37cc78257920b7c5d8e38c182154fcdd3aafa51d27efa9070e.jpg)

<details>
<summary>text_image</summary>

Im
GH Plane
ω = 0+
ω = ∞
ω = -∞
-1
Re
ω = 0-
ω = 0-
</details>

Figure 7–56 Polar plot of the system considered in Example 7–17.

The function $G ( s ) H ( s )$ has one pole $( s = 1 / T )$ in the right-half s plane.Therefore, $P = 1$ . The Nyquist plot shown in Figure $7 - 5 6$ indicates that the $G ( s ) H ( s )$ plot encircles the $- 1 + j 0$ point once clockwise. Thus, $N = 1$ . Since $Z = N + P $ , we find that $Z = 2 .$ . This means that the closedloop system has two closed-loop poles in the right-half s plane and is unstable.

EXAMPLE 7–18 Investigate the stability of a closed-loop system with the following open-loop transfer function:

$$G (s) H (s) = \frac {K (s + 3)}{s (s - 1)} \quad (K > 1)$$

The open-loop transfer function has one pole $( s = 1 )$ in the right-half s plane, or $P = 1$ . The open-loop system is unstable. The Nyquist plot shown in Figure 7–57 indicates that the $- 1 + j 0$ point is encircled by the $G ( s ) H ( s )$ locus once in the counterclockwise direction. Therefore, $N = - 1$ . Thus, Z is found from $Z = N + P$ to be zero, which indicates that there is no zero of $1 + G ( s ) H ( s )$ in the right-half s plane, and the closed-loop system is stable. This is one of the examples for which an unstable open-loop system becomes stable when the loop is closed.

![](image/4144f49e538562df456b68081d2ede3622c7484d235fcdd98af5ccecbbd43c7b.jpg)

<details>
<summary>text_image</summary>

Im
GH Plane
ω = 0+
ω = -∞
ω = -1
ω = ∞
Re
-1
ω = 0-
</details>

Figure 7–57 Polar plot of the system considered in Example 7–18.

Figure 7–58 Polar plot of a conditionally stable system.   
![](image/600ad8f9cd7192e0431c82b24b40e82af11fb221bff854cb531fbf5915d12827.jpg)

<details>
<summary>text_image</summary>

Im
GH Plane
ω = ∞
C B A 0 Re
ω
0
</details>
