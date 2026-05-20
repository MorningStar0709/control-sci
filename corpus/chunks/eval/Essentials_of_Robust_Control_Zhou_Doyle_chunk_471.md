# 17.3 Geometric Interpretation of ν-Gap Metric

The most salient feature of the ν-gap metric is that it can be computed pointwise in frequency domain:

$$\delta_ {\nu} (P _ {1}, P _ {2}) = \sup _ {\omega} \psi (P _ {1} (j \omega), P _ {2} (j \omega))$$

provided the winding number condition is satisfied. (For a more extensive coverage of material presented in this section and the next two sections, readers are encouraged to consult the original references by Vinnicombe [1992a, 1992b, 1993a, 1993b].)

In particular, for a single-input single-output system,

$$\psi (P _ {1} (j \omega), P _ {2} (j \omega)) = \frac {| P _ {1} (j \omega) - P _ {2} (j \omega) |}{\sqrt {1 + | P _ {1} (j \omega) | ^ {2}} \sqrt {1 + | P _ {2} (j \omega) | ^ {2}}}. \tag {17.2}$$

This function has the interpretation of being the chordal distance between $P _ { 1 } ( j \omega )$ and $P _ { 2 } ( j \omega )$ . To illustrate this, consider the Riemann sphere, which is a unit sphere tangent at its “south pole” to the complex plant at its origin shown in Figure 17.7.

![](image/d0216d51c99b46f86979cbdf837855f3392347eff1909a128933d03116390387.jpg)

<details>
<summary>text_image</summary>

projection of s₁=1-j
projection of s₂=1
ψ(s₁, s₂)
real axis
0.5
0
-0.5
-1
-1
0
imaginary axis
</details>

Figure 17.7: Projection onto the Riemann sphere

A point $s _ { 1 } \left( \mathrm { e . g . } , s _ { 1 } = 1 - j \right)$ in the complex plane is stereographically projected on the Riemann sphere by connecting the “north pole” to $s _ { 1 }$ and determining the intersection of this straight line with the Riemann sphere, resulting in the projection, $q _ { 1 } , \mathrm { o f } s _ { 1 }$ . The

coordinates of $q _ { 1 }$ are

$$x _ {1} = \frac {\mathrm{Res} _ {1}}{1 + | s _ {1} | ^ {2}}, y _ {1} = \frac {\Im s _ {1}}{1 + | s _ {1} | ^ {2}}, z _ {1} = \frac {| s _ {1} | ^ {2}}{1 + | s _ {1} | ^ {2}}.$$

Thus, the north pole represents the point at infinity and the unit circle is projected onto the “equator.” The chordal distance between two points, $s _ { 1 }$ and $s _ { 2 } .$ , is the Euclidean distance between their stereographical projections, $q _ { 1 }$ and $q _ { 2 } \colon$

$$d (s _ {1}, s _ {2}) = \sqrt {(x _ {1} - x _ {2}) ^ {2} + (y _ {1} - y _ {2}) ^ {2} + (z _ {1} - z _ {2}) ^ {2}} = \frac {| s _ {1} - s _ {2} |}{\sqrt {1 + | s _ {1} | ^ {2}} \sqrt {1 + | s _ {2} | ^ {2}}}.$$

![](image/48213d7def6fb25a4537ed96255354a213b6e5f587c8061d16ddf6a1d30e7cd7.jpg)

<details>
<summary>natural_image</summary>
