We shall assume for the moment that $P(s)$ may have poles in the open RHP but not on the j-axis (those will be handled separately). Therefore, let $p_{i}, i = 1, 2, \ldots, N$ , be poles of $p(s)$ in the open RHP. To satisfy the interpolation constraints,

$$S (p _ {i}) = k \frac {B (p _ {i})}{W (p _ {i})} = 0, \quad i = 1, 2, \dots , N. \tag {4.57}$$

Since $W(s)$ has no RHP poles, $W(p_i) \neq \infty$ and therefore we must have $B(p_i) = 0, i = 1, 2, \ldots, N$ . This forces $B(s)$ to have the form

$$B (s) = B _ {p} (s) B ^ {\prime} (s) \tag {4.58}$$

where $B_{p}(s) = [(-s + p_{1}) / (s + p_{1})] \cdots [(-s + p_{N}) / (s + p_{N})]$ . In Equation 4.58, $B'$ is a Blaschke product, to be determined presently.

Note that, in the absence of RHP zeros, the term $B'$ is not required, since all interpolation constraints are satisfied with $B_{p}(s)$ . In that case, k may be any real nonzero constant, as small as desired.

Given RHP zeros, $B'$ is found by using the interpolation conditions at the RHP zeros of p. If these zeros are $z_{1}, z_{2}, \ldots, z_{M}$ , stability forces $S(z_{1}) = S(z_{2}) = \cdots = S(z_{M}) = 1$ . From Equations 4.57 and 4.58,

$$S (z _ {i}) W (z _ {i}) = W (z _ {i}) = k B ^ {\prime} (z _ {i}) B _ {p} (z _ {i}), \quad i = 1, 2, \dots , M$$

or

$$k B ^ {\prime} (z _ {i}) = \frac {W (z _ {i})}{B _ {p} (z _ {i})}, \quad i = 1, 2, \dots , M. \tag {4.59}$$

Equation 4.59 represents M equations; it is to be expected that M free parameters will be needed to satisfy them. The gain k is one parameter; $B'$ must have the remaining $M - 1$ . Indeed, it can be shown that $B'$ has the form

$$
B ^ {\prime} (s) = \left\{ \begin{array}{c c} \left(\frac {- s + a _ {1}}{s + a _ {1}}\right) \cdot \left(\frac {- s + a _ {2}}{s + a _ {2}}\right) \dots \left(\frac {- s + a _ {M - 1}}{s + a _ {M - 1}}\right) & \text { if } M > 1 \\ 1 & \text { if } M = 1 \end{array} \right. \tag {4.60}
$$

where the $a_{i}$ are complex numbers with the positive real part chosen, together with $k$ , to satisfy Equation 4.59.

Once $k$ and the $a_i$ have been determined, $S$ is calculated as

$$S (s) = \frac {k B ^ {\prime} (s) B _ {p} (s)}{W (s)} \tag {4.61}$$

which is stable, since $B'$ and $B_p$ are stable and $W$ has no RHP zeros. The compensator design then proceeds as before.

Note that, since $|B(j\omega)| = 1$ ,

$$| S (j \omega) | = \frac {| k |}{| W (j \omega) |}. \tag {4.62}$$

This equation reveals that the shape of the sensitivity magnitude curve is just the inverse of that of W. If $|W(j\omega)|$ is relatively high at low frequencies, $|S(j\omega)|$ will be relatively low. Thus, the shape of the optimal $|S(j\omega)|$ is independent of P; the influence of the plant dynamics is exerted entirely through the gain k.
