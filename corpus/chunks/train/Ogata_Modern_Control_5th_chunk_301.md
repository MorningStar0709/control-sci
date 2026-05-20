If a test point is located very far from the origin, then by dividing the denominator by the numerator, it is possible to write G(s)H(s) as

$$G (s) H (s) = \frac {K}{s ^ {n - m} + \left[ \left(p _ {1} + p _ {2} + \cdots + p _ {n}\right) - \left(z _ {1} + z _ {2} + \cdots + z _ {m}\right) \right] s ^ {n - m - 1} + \cdots}$$

or

$$G (s) H (s) = \frac {K}{\left[ s + \frac {\left(p _ {1} + p _ {2} + \cdots + p _ {n}\right) - \left(z _ {1} + z _ {2} + \cdots + z _ {m}\right)}{n - m} \right] ^ {n - m}} \tag {6-12}$$

The abscissa of the intersection of the asymptotes and the real axis is then obtained by setting the denominator of the right-hand side of Equation (6–12) equal to zero and solving for s, or

$$s = - \frac {\left(p _ {1} + p _ {2} + \cdots + p _ {n}\right) - \left(z _ {1} + z _ {2} + \cdots + z _ {m}\right)}{n - m} \tag {6-13}$$

[Example 6–1 shows why Equation (6–13) gives the intersection.] Once this intersection is determined, the asymptotes can be readily drawn in the complex plane.

It is important to note that the asymptotes show the behavior of the root loci for A root-locus branch may lie on one side of the corresponding asymptote or may∑s∑  1. cross the corresponding asymptote from one side to the other side.

4. Find the breakaway and break-in points. Because of the conjugate symmetry of the root loci, the breakaway points and break-in points either lie on the real axis or occur in complex-conjugate pairs.

If a root locus lies between two adjacent open-loop poles on the real axis, then there exists at least one breakaway point between the two poles. Similarly, if the root locus lies between two adjacent zeros (one zero may be located at –q) on the real axis, then there always exists at least one break-in point between the two zeros. If the root locus lies between an open-loop pole and a zero (finite or infinite) on the real axis, then there may exist no breakaway or break-in points or there may exist both breakaway and break-in points.

Suppose that the characteristic equation is given by

$$B (s) + K A (s) = 0$$

The breakaway points and break-in points correspond to multiple roots of the characteristic equation. Hence, as discussed in Example 6–1, the breakaway and break-in points can be determined from the roots of

$$\frac {d K}{d s} = - \frac {B ^ {\prime} (s) A (s) - B (s) A ^ {\prime} (s)}{A ^ {2} (s)} = 0 \tag {6-14}$$
