$$
\begin{array}{l} r _ {y u} (\tau) = \mathrm{E} y (k + \tau) u ^ {T} (k) = \mathrm{E} \sum_ {n = 0} ^ {\infty} h (n) u (k + \tau - n) u ^ {T} (k) \\ = \sum_ {n = 0} ^ {\infty} h (n) \mathrm{E} \left(u (k + \tau - n) u ^ {T} (k)\right) = \sum_ {n = 0} ^ {\infty} h (n) r _ {u} (\tau - n) \tag {10.15} \\ \end{array}
$$

Notice that it has been assumed that all infinite sums exist and that the operations of infinite summation and mathematical expectation have been freely exchanged in these calculations. This must of course he justified; it is easy to do in the sense of mean-square convergence, if it is assumed that the fourth moment of the input signal is finite.

The relations expressed by Eqs. (10.14) and (10.15) can be expressed in a simpler form if spectral densities are introduced. The definition of spectral density in (10.5) gives

$$\phi_ {y} (\omega) = \phi_ {y y} (\omega) = \frac {1}{2 \pi} \sum_ {n = - \infty} ^ {\infty} e ^ {- i n \omega} r _ {y} (n)$$

Introducing $r_y$ from (10.14) gives

$$
\begin{array}{l} \phi_ {y} (\omega) = \frac {1}{2 \pi} \sum_ {n = - \infty} ^ {\infty} e ^ {- i n \omega} \sum_ {k = 0} ^ {\infty} \sum_ {l = 0} ^ {\infty} h (k) r _ {u} (n + l - k) h ^ {T} (l) \\ = \frac {1}{2 \pi} \sum_ {k = 0} ^ {\infty} \sum_ {n = - \infty} ^ {\infty} \sum_ {l = 0} ^ {\infty} e ^ {- i k \omega} h (k) e ^ {- i (n + l - k) \omega} r _ {u} (n + l - k) e ^ {i l \omega} h ^ {T} (l) \\ = \frac {1}{2 \pi} \sum_ {k = 0} ^ {\infty} e ^ {- i k \omega} h (k) \sum_ {n = - \infty} ^ {\infty} e ^ {- i n \omega} r _ {u} (n) \sum_ {l = 0} ^ {\infty} e ^ {i l \omega} h ^ {T} (l) \\ \end{array}
$$

Introduce the pulse-transfer function $H(z)$ of the system. This is related to the impulse response $h(k)$ by

$$H (z) = \sum_ {k = 0} ^ {\infty} z ^ {- k} h (k)$$

The equation for the spectral density can then be written as

$$\phi_ {y} (\omega) = H (e ^ {i \omega}) \phi_ {u} (\omega) H ^ {T} (e ^ {- i \omega})$$

Similarly,

$$
\begin{array}{l} \phi_ {y u} (\omega) = \frac {1}{2 \pi} \sum_ {n = - \infty} ^ {\infty} e ^ {- i n \omega} r _ {y u} (n) = \frac {1}{2 \pi} \sum_ {n = - \infty} ^ {\infty} e ^ {- i n \omega} \sum_ {k = 0} ^ {\infty} h (k) r _ {u} (n - k) \\ = \frac {1}{2 \pi} \sum_ {k = 0} ^ {\infty} e ^ {- i k \omega} h (k) \sum_ {n = - \infty} ^ {\infty} e ^ {- i n \omega} r _ {u} (n) = H (e ^ {i \omega}) \phi_ {u} (\omega) \\ \end{array}
$$

Main result. To obtain the general result, the propagation of the mean value through the system must also be investigated.
