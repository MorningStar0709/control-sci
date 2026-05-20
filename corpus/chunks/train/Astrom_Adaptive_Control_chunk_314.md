# EXAMPLE 5.8 Linear systems with signals in $L_{2e}$

Let the signal space be $L_{2e}$ . Consider a linear system with the transfer function $G(s)$ . Assume that $G(s)$ has no poles in the closed right half-plane and that the system is initially at rest. Let u be the input and y the output, and let U and Y be the corresponding Laplace transforms. It follows from Parseval's theorem, Theorem 2.8, that

$$
\begin{array}{l} \left\| y \right\| ^ {2} = \int_ {0} ^ {\infty} y ^ {2} (t) d t = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} Y (i \omega) Y (- i \omega) d \omega \\ = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} G (i \omega) U (i \omega) G (- i \omega) U (- i \omega) d \omega \\ \leq \max _ {\omega} | G (i \omega) | ^ {2} \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} U (i \omega) U (- i \omega) d \omega \\ = \max _ {\omega} | G (i \omega) | ^ {2} \int_ {0} ^ {\infty} u ^ {2} (t) d t = \max _ {\omega} | G (i \omega) | ^ {2} \cdot \| u \| ^ {2} \\ \end{array}
$$

Hence

$$\| y \| \leq \max _ {\omega} | G (i \omega) | \cdot \| u \|$$

The gain is thus less than $\max|G(i\omega)|$ . We get equality in the above equation if u is a sinusoid with the frequency that maximizes $|G(i\omega)|$ . However, such a signal is not in $L_{2e}$ . The value of $\|y\|$ can be made arbitrarily close to $\max|G(i\omega)|$ with a truncated sinusoid in $L_{2e}$ by making T sufficiently large. The gain of the system is thus

$$\gamma (G) = \max _ {\omega} | G (i \omega) | \tag {5.41}$$
