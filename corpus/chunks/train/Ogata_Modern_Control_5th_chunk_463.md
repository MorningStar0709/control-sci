# 7–6 STABILITY ANALYSIS

In this section, we shall present several illustrative examples of the stability analysis of control systems using the Nyquist stability criterion.

If the Nyquist path in the s plane encircles Z zeros and P poles of $1 + G ( s ) H ( s )$ and does not pass through any poles or zeros of $1 + G ( s ) H ( s )$ as a representative point s moves in the clockwise direction along the Nyquist path, then the corresponding contour in the $G ( s ) H ( s )$ plane encircles the $- 1 + j 0$ point $N = Z - P$ times in the clockwise direction. (Negative values of N imply counterclockwise encirclements.)

In examining the stability of linear control systems using the Nyquist stability criterion, we see that three possibilities can occur:

1. There is no encirclement of the $- 1 + j 0$ point. This implies that the system is stable if there are no poles of $G ( s ) H ( s )$ in the right-half s plane; otherwise, the system is unstable.   
2. There are one or more counterclockwise encirclements of the $- 1 + j 0$ point. In this case the system is stable if the number of counterclockwise encirclements is the same as the number of poles of $G ( s ) H ( s )$ in the right-half s plane; otherwise, the system is unstable.   
3. There are one or more clockwise encirclements of the $- 1 + j 0$ point. In this case the system is unstable.

In the following examples, we assume that the values of the gain K and the time constants (such as $T , T _ { 1 }$ and, $T _ { 2 } )$ are all positive.

EXAMPLE 7–14 Consider a closed-loop system whose open-loop transfer function is given by

$$G (s) H (s) = \frac {K}{(T _ {1} s + 1) (T _ {2} s + 1)}$$

Examine the stability of the system.

A plot of $G ( j \omega ) H ( j \omega )$ is shown in Figure 7–53. Since $G ( s ) H ( s )$ does not have any poles in the right-half s plane and the $- 1 + j 0$ point is not encircled by the $G ( j \omega ) H ( j \omega )$ locus, this system is stable for any positive values of $K , T _ { 1 }$ and, $T _ { 2 }$ .

![](image/a6392a81b344e8117d800344a8dfe9ba5f6d830e8044d9b93ab56efb87d327fd.jpg)

<details>
<summary>text_image</summary>

Im
GH Plane
ω = -∞
ω = 0
ω = ∞
Re
-1
G(jω) H(jω)
</details>

Figure 7–53   
Polar plot of $G ( j \omega ) H ( j \omega )$ considered in Example 7–14.

EXAMPLE 7–15 Consider the system with the following open-loop transfer function:

$$G (s) H (s) = \frac {K}{s \left(T _ {1} s + 1\right) \left(T _ {2} s + 1\right)}$$

Determine the stability of the system for two cases: (1) the gain K is small and (2) K is large.
