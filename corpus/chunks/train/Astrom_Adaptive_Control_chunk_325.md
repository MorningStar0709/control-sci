# EXAMPLE 5.12 Linear time-invariant systems

Consider a linear time-invariant system with the transfer function $G(s)$ . Assume that $G(s)$ has no poles in the closed right half-plane. It follows from

Parseval's theorem that

$$
\begin{array}{l} \langle y \mid u \rangle = \int_ {0} ^ {\infty} y (t) u (t) d t = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} Y (i \omega) U (- i \omega) d \omega \\ = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} G (i \omega) U (i \omega) U (- i \omega) d \omega \\ = \frac {1}{\pi} \int_ {0} ^ {\infty} \operatorname{Re} \left\{G (i \omega) \right\} U (i \omega) U (- i \omega) d \omega \tag {5.47} \\ \end{array}
$$

where Y and U are the Laplace transforms of y and u, respectively. If $G(i\omega)$ is positive real (see Definition 5.5), we have $\operatorname{Re} G(i\omega) \geq 0$ , and we get

$$\langle y | u \rangle \geq 0$$

which shows that the system is passive. It follows from Definition 5.9 that a positive real transfer function is input strictly passive if

$$\operatorname{Re} G (i \omega) \geq \varepsilon > 0$$

and output strictly passive if

$$\operatorname{Re} G (i \omega) \geq \varepsilon | G (i \omega) | ^ {2}$$

The transfer function $G(s) = s + 1$ is thus SPR and ISP but not OSP. The transfer function $G(s) = 1/(s + 1)$ is SPR and OSP but not ISP. The transfer function

$$G (s) = \frac {s ^ {2} + 1}{(s + 1) ^ {2}}$$

is OSP and ISP but not SPR.

In control systems applications it is common for transfer functions to be proper or strictly proper. The output strict passivity is therefore the concept that is normally used in these applications.
