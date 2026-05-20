$$\sup _ {\omega} | W (j \omega) | | H _ {w d} (j \omega) | | 1 - F (j \omega) P (j \omega) |$$

for $\omega_0 = 4$ rad/s.

b. For $\omega_0 = 4$ , 10, and $50\mathrm{rad / s}$ , compute the magnitude Bode plot of $y / y_R$ .

4.22 Assume $P(s)$ has no $j$ -axis poles or zeros, and let $B_{p}(s)$ and $B_{z}(s)$ be the Blaschke products corresponding, respectively, to the open RHP poles and zeros of $P$ . Show that the optimum sensitivity, in the $H^{\infty}$ sense, for a weighting function $W(s)$ is the same for $P(s)$ and for the plant $P'(s) = B_{z}(s) / B_{p}(s)$ .

![](image/43bc2c3703472be4d4fe3e58a577c7af64a722d7a72f28b5fad5d68f6e139172.jpg)

4.23 As a consequence of Problem 4.22, the effect of RHP poles and zeros on the optimum sensitivity can be studied for the transfer function $B_{z}(s) / B_{p}(s)$ , rather than for $P(s)$ .

Given $W(s) = (.1Ts + 1) / (Ts + 1)$ , obtain the minimum sensitivity for a stable plant with a single RHP zero, at $s = 1$ . Plot $|S(j\omega)|$ for $Ts = 5, 1$ , and 0.1. What can you conclude about the effect of bandwidth on performance?

![](image/2d0d019af972e8142800b0cd0b8c8d54b50ee461f84d56bbfc4d21f15d712f16.jpg)

4.24 Repeat Problem 4.23 for $T = 1$ and a stable plant with RHP zeros at $s = 1$ and $s = 1 + a$ . Plot $|S(j\omega)|$ for $a = 0.1, 1,$ and 2. What can you conclude about the effect on performance of the separation between zeros?

![](image/050afd61b9eacca9bed3300a9f299fa3cfb4ad4090da16712e7126d2c9d20bc0.jpg)

4.25 Repeat Problem 4.23 for $T = 1$ and a stable plant with RHP zeros at $s = \zeta \pm j\sqrt{1 - \zeta^2}$ . Plot $|S(j\omega)|$ for $\zeta = .1, .5, .9$ . What effect does the damping factor of the zeros have on performance?

![](image/d45934b13e049d04bc5a7621add9a1c49ce8ab4480a3f6e214ec026a073607d7.jpg)

4.26 Repeat Problem 4.23 for $T = 1$ and a plant with an RHP pole at $s = 1$ and an RHP zero at $s = 1 + a$ , for $a = -.5, .1, .5$ , and 2. What effect does the separation between RHP poles and zeros have on performance?

4.27 For the plant of Problem 4.14, show that the $H^{\infty}$ norm of the weighted sensitivity may be as small as we like, for any proper minimum-phase weighting function.

4.28 Calculate the optimal sensitivity for the plant of Problem 4.15, with $W(s) = (0.1Ts + 1) / (Ts + 1)$ and $T = 0.1, 1,$ and 10.

4.29 Repeat Problem 4.28 for the plant of Problem 4.16.
