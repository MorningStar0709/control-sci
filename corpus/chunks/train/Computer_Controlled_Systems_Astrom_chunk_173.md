# Example 3.4 A second-order system

Consider a system with sampling period h = 1 and the pulse-transfer function

$$H (z) = \frac {0 . 2 5 K}{(z - 1) (z - 0 . 5)}$$

then

$$H \left(e ^ {i \omega}\right) = 0. 2 5 K \frac {1 . 5 (1 - \cos \omega) - 2 \sin^ {2} \omega - i \sin \omega (2 \cos \omega - 1 . 5)}{(2 - 2 \cos \omega) (1 . 2 5 + \cos \omega)}$$

The map of $\Gamma_{c}$ is shown in Fig. 3.7. The solid line is the Nyquist curve, that is, the map of $H(e^{i\omega})$ for $\omega = 0$ to $\pi$ . Notice that the sampled-data system has a phase shift that is larger than $180^{\circ}$ for some frequencies. From the figure it can be found that the Nyquist curve crosses the negative real axis at $-0.5$ . The closed-loop system is thus stable if $K < 2$ .
