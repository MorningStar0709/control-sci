# EXAMPLE 2.9 Frequency domain characterization

Consider a quasi-stationary signal $u(t)$ with spectrum $\Phi_{u}(\omega)$ . It follows from Parseval's theorem that

$$\lim _ {t \rightarrow \infty} \frac {1}{t} \sum_ {k = 1} ^ {t} (A (q) u (k)) ^ {2} = \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} | A \left(e ^ {i \omega}\right) | ^ {2} \Phi_ {u} (\omega) d \omega \tag {2.46}$$

This equation gives considerable insight into the notion of persistent excitation. A polynomial of degree n-1 can at most vanish in n-1 points. The right-hand side of Eq. (2.46) will thus be positive if $\Phi_{u}(\omega) \neq 0$ for at least n points in the interval $-\pi \leq \omega \leq \pi$ . A signal whose spectrum is different from zero in an interval is thus persistently exciting of any order.

A sinusoid has a point spectrum that differs from zero at two points. It is thus persistently exciting of second order. A signal that is a sum of k sinusoids is persistently exciting of order 2k. The frequency domain characterization also makes it possible to derive the following result.
