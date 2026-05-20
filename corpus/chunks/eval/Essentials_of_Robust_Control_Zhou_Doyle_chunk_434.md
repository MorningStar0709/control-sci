# 16.4 Further Guidelines for Loop Shaping

Let $P = N M ^ { - 1 }$ be a normalized right coprime factorization. It was shown in Georgiou and Smith [1990] that

$$
b _ {\mathrm{opt}} (P) \leq \lambda (P) := \inf _ {\operatorname{Res} > 0} \underline {{\sigma}} \left(\left[ \begin{array}{c} M (s) \\ N (s) \end{array} \right]\right).
$$

Hence a small $\lambda ( P )$ would necessarily imply a small $b _ { \mathrm { o p t } } ( P )$ . We shall now discuss the performance limitations implied by this relationship for a scalar system. The following argument is based on Vinnicombe [1993b], to which the reader is referred for further discussions. Let $z _ { 1 } , z _ { 2 } , \ldots , z _ { m }$ and $p _ { 1 } , p _ { 2 } , \ldots , p _ { k }$ be the open right-half plane zeros and poles of the plant P . Define

$$N _ {z} (s) = \frac {z _ {1} - s}{z _ {1} + s} \frac {z _ {2} - s}{z _ {2} + s} \dots \frac {z _ {m} - s}{z _ {m} + s}, N _ {p} (s) = \frac {p _ {1} - s}{p _ {1} + s} \frac {p _ {2} - s}{p _ {2} + s} \dots \frac {p _ {k} - s}{p _ {k} + s}.$$

Then P can be written as

$$P (s) = P _ {0} (s) N _ {z} (s) / N _ {p} (s)$$

where $P _ { 0 } ( s )$ has no open right-half plane poles or zeros. Let $N _ { 0 } ( s )$ and $M _ { 0 } ( s )$ be stable and minimum phase spectral factors:

$$N _ {0} (s) N _ {0} ^ {\sim} (s) = \left(1 + \frac {1}{P (s) P ^ {\sim} (s)}\right) ^ {- 1}, M _ {0} (s) M _ {0} ^ {\sim} (s) = \left(1 + P (s) P ^ {\sim} (s)\right) ^ {- 1}.$$

Then $P _ { 0 } = N _ { 0 } / M _ { 0 }$ is a normalized coprime factorization and $( N _ { 0 } N _ { z } )$ and $( M _ { 0 } N _ { p } )$ form a pair of normalized coprime factorizations of P . Thus

$$b _ {\mathrm{opt}} (P) \leq \sqrt {| N _ {0} (s) N _ {z} (s) | ^ {2} + | M _ {0} (s) N _ {p} (s) | ^ {2}}, \forall \mathrm{Re} (s) > 0. \tag {16.19}$$

Since $N _ { 0 }$ and $M _ { 0 }$ are both stable and have no zeros in the open right-half plane, ln $( N _ { 0 } ( s ) )$ and $\ln ( M _ { 0 } ( s ) )$ are both analytic in $\operatorname { R e } ( s ) > 0$ and so can be determined from their boundary values on $\operatorname { R e } ( s ) = 0$ via Poisson integrals (see also Problem 16.15):

$$\ln | N _ {0} (r e ^ {j \theta}) | = \int_ {- \infty} ^ {\infty} \ln \left(\frac {1}{\sqrt {1 + 1 / | P (j \omega) | ^ {2}}}\right) K _ {\theta} (\omega / r) d (\ln \omega)\ln | M _ {0} (r e ^ {j \theta}) | = \int_ {- \infty} ^ {\infty} \ln \left(\frac {1}{\sqrt {1 + | P (j \omega) | ^ {2}}}\right) K _ {\theta} (\omega / r) d (\ln \omega)$$

where $r > 0 , - \pi / 2 < \theta < \pi / 2$ , and
