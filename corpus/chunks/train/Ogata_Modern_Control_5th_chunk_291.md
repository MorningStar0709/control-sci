$$\underline {{\sigma + j \omega + 1}} = \pm 6 0 ^ {\circ} (2 k + 1)$$

or

$$\tan^ {- 1} \frac {\omega}{\sigma + 1} = 6 0 ^ {\circ}, \quad - 6 0 ^ {\circ}, \quad 0 ^ {\circ}$$

Taking the tangent of both sides of this last equation,

$$\frac {\omega}{\sigma + 1} = \sqrt {3}, \qquad - \sqrt {3}, \qquad 0$$

which can be written as

$$\sigma + 1 - \frac {\omega}{\sqrt {3}} = 0, \quad \sigma + 1 + \frac {\omega}{\sqrt {3}} = 0, \quad \omega = 0$$

These three equations represent three straight lines, as shown in Figure 6–4.The three straight lines shown are the asymptotes. They meet at point s=–1. Thus, the abscissa of the intersection of the asymptotes and the real axis is obtained by setting the denominator of the right-hand side of Equation (6–5) equal to zero and solving for s. The asymptotes are almost parts of the root loci in regions very far from the origin.

3. Determine the breakaway point. To plot root loci accurately, we must find the breakaway point, where the root-locus branches originating from the poles at 0 and –1 break away (as K is increased) from the real axis and move into the complex plane.The breakaway point corresponds to a point in the s plane where multiple roots of the characteristic equation occur.

A simple method for finding the breakaway point is available. We shall present this method in the following: Let us write the characteristic equation as

$$f (s) = B (s) + K A (s) = 0 \tag {6-6}$$

![](image/bfe8ea504583e492750e213d0d13825684609eb1dcb6b1bd5793b1d1faf2323d.jpg)

<details>
<summary>text_image</summary>

jω
-j√3
σ + 1 - ω/√3 = 0
ω = 0
-1
0
σ
σ + 1 + ω/√3 = 0
-j√3
</details>

Figure 6–4 Three asymptotes.

where A(s) and $B ( s )$ do not contain K. Note that $f ( s ) = 0$ has multiple roots at points where

$$\frac {d f (s)}{d s} = 0$$

This can be seen as follows: Suppose that $f ( s )$ has multiple roots of order r, where $r \geq 2 .$ .Then $f ( s )$ may be written as

$$f (s) = \bigl (s - s _ {1} \bigr) ^ {r} \bigl (s - s _ {2} \bigr) \dots \bigl (s - s _ {n} \bigr)$$

Now we differentiate this equation with respect to s and evaluate ${ d f ( s ) } / { d s } \mathrm { a t } s = s _ { 1 }$ . Then we get

$$\left. \frac {d f (s)}{d s} \right| _ {s = s _ {1}} = 0 \tag {6-7}$$

This means that multiple roots of $f ( s )$ will satisfy Equation (6–7). From Equation (6–6), we obtain

$$\frac {d f (s)}{d s} = B ^ {\prime} (s) + K A ^ {\prime} (s) = 0 \tag {6-8}$$

where

$$A ^ {\prime} (s) = \frac {d A (s)}{d s}, \quad B ^ {\prime} (s) = \frac {d B (s)}{d s}$$
