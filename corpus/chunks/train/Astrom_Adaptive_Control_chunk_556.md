# Comparison with the Describing Function

Having obtained the exact formula of Eq. (8.11) for T, it is possible to investigate the precision of the describing function approximation. Consider the symmetric case and introduce h = T/2. The pulse transfer function obtained in sampling the system of Eqs. (8.9) with period h is given by

$$H _ {h} (e ^ {s h}) = \frac {1}{h} \sum_ {n = - \infty} ^ {\infty} \frac {1}{s + i n \omega_ {s}} \left(1 - e ^ {- h (s + i n \omega_ {s})}\right) G (s + i n \omega_ {s})$$

where $\omega_{s} = 2\pi / h$ . Put $sh = i\pi$ :

$$
\begin{array}{l} H _ {h} (1) = \sum_ {- \infty} ^ {\infty} \frac {2}{i (\pi + 2 n \pi)} G \left(i \frac {\pi + 2 n \pi}{h}\right) \\ = \sum_ {0} ^ {\infty} \frac {4}{\pi (1 + 2 n)} \operatorname{Im} \left(G \left(i \frac {\pi + 2 n \pi}{h}\right)\right) = 0 \\ \end{array}
$$

The first term of the series gives

$$H _ {h} (- 1) \approx \frac {4}{\pi} \operatorname{Im} \left(G \left(i \frac {\pi}{h}\right)\right) = \frac {4}{\pi} \operatorname{Im} \left(G \left(i \frac {2 \pi}{T}\right)\right) = 0$$

which is the same result for calculation of T obtained from the describing function analysis. This implies that the describing function approximation is accurate only if $G(s)$ has low-pass character. An example illustrates determination of the period of oscillation.
