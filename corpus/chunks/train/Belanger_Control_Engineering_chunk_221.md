<details>
<summary>line</summary>

| Frequency (rad/s) | f for log S (T=5) | f for log S (T=0.2) |
| --- | --- | --- |
| 0 | 1.0 | -1.5 |
| 2 | 0.5 | -0.5 |
| 4 | 0.0 | 0.0 |
| 6 | -0.5 | 0.5 |
| 8 | -0.5 | 0.75 |
| 10 | -0.5 | 0.8 |
| 12 | -0.5 | 0.85 |
| 14 | -0.5 | 0.9 |
| 16 | -0.5 | 0.95 |
</details>

Figure 4.22 Admissible sensitivity frequency responses

Figure 4.22 shows, for $z_0 = 1$ and no RHP poles, the weighting function $f(z_0, \omega)$ and two admissible sensitivity log magnitude curves. For purposes of demonstration, the form $S(s) = k[(T_s + 1) / (.1T_s + 1)]$ is chosen, with $T_s = .2$ and $5$ , and $k$ calculated to meet the condition $S(z_0) = 1$ . The net weighted area under each sensitivity log magnitude curve must be zero, because we accumulate negative area when $|S(j\omega)| < 1 (\log |S(j\omega)| < 0)$ and compensate with positive area where $|S(j\omega)| > 1$ . We accumulate net negative area at low frequencies, and the positive contribution comes at higher frequencies. The larger the bandwidth, the greater the negative area and, furthermore, the smaller the weight given to the positive contribution. It follows that a large bandwidth is obtained at the cost of large $|S(j\omega)|$ at higher frequencies. As a rule of thumb, for real zeros, the achievable bandwidth in radians per second is roughly equal to the real RHP zero closest to the origin.

If there are RHP poles as well as RHP zeros, the situation is worse. Suppose there is one RHP pole, $p_{0}$ , and an RHP zero, $z_{0}$ . Then

$$B _ {p} (z _ {0}) = \frac {- z _ {0} + p _ {0}}{z _ {0} + p _ {0}}.$$

Since $z_0$ and $p_0$ are positive, $|B_p(z_0)| < 1$ and $\log 1 / |B_p(z_0)| > 0$ . The net area represented by the LHS of Equation 4.53 must be positive, which means that the curves $\log |S(j\omega)|$ must be generally more positive than in the absence of RHP poles. The situation is particularly bad if $p_0$ and $z_0$ are close, because $|B_p(z_0)|$ is small and $1 / |B_p(z_0)|$ is large.

By a process entirely analogous to that which led to Equation 4.53, an equation is written for the complementary sensitivity:

$$\frac {1}{\pi} \int_ {- \infty} ^ {\infty} \log | T (j \omega) | f (p _ {0}, \omega) d \omega = \log \frac {1}{| B _ {z} (p _ {0}) |} \tag {4.54}$$

where $B_{z}$ is the Blaschke product associated with the zeros of P in the open RHP, and $p_{0}$ is a pole of P in the open RHP. In the absence of RHP zeros, $B_{z}(s)=1$ .
