If we include poles and zeros at infinity, the number of open-loop poles is equal to that of open-loop zeros. Hence we can always state that the root loci start at the poles of $G ( s ) H ( s )$ and end at the zeros of $G ( s ) H ( s )$ , as K increases from zero to infinity, where the poles and zeros include both those in the finite s plane and those at infinity.

2. Determine the root loci on the real axis. Root loci on the real axis are determined by open-loop poles and zeros lying on it. The complex-conjugate poles and complexconjugate zeros of the open-loop transfer function have no effect on the location of the root loci on the real axis because the angle contribution of a pair of complex-conjugate poles or complex-conjugate zeros is $3 6 0 ^ { \circ }$ on the real axis. Each portion of the root locus on the real axis extends over a range from a pole or zero to another pole or zero. In constructing the root loci on the real axis, choose a test point on it. If the total number of real poles and real zeros to the right of this test point is odd, then this point lies on a root locus. If the open-loop poles and open-loop zeros are simple poles and simple zeros, then the root locus and its complement form alternate segments along the real axis.

3. Determine the asymptotes of root loci. If the test point s is located far from the origin, then the angle of each complex quantity may be considered the same. One open-loop zero and one open-loop pole then cancel the effects of the other. Therefore, the root loci for very large values of s must be asymptotic to straight lines whose angles (slopes) are given by

$$\text { Angles of asymptotes } = \frac {\pm 1 8 0 ^ {\circ} (2 k + 1)}{n - m} \quad (k = 0, 1, 2, \dots)$$

where number of finite poles of n = $G ( s ) H ( s )$

$$m = \text { number of finite zeros of } G (s) H (s)$$

Here, $k = 0$ corresponds to the asymptotes with the smallest angle with the real axis.Although k assumes an infinite number of values, as k is increased the angle repeats itself, and the number of distinct asymptotes is $n \mathrm { ~ - ~ } m$ .

All the asymptotes intersect at a point on the real axis. The point at which they do so is obtained as follows: If both the numerator and denominator of the open-loop transfer function are expanded, the result is

$$G (s) H (s) = \frac {K \left[ s ^ {m} + \left(z _ {1} + z _ {2} + \cdots + z _ {m}\right) s ^ {m - 1} + \cdots + z _ {1} z _ {2} \cdots z _ {m} \right]}{s ^ {n} + \left(p _ {1} + p _ {2} + \cdots + p _ {n}\right) s ^ {n - 1} + \cdots + p _ {1} p _ {2} \cdots p _ {n}}$$
