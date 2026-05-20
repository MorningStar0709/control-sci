# 4.3.3 Performance Limitations

As we saw in Section 4.3.1, open-loop control neither attenuates disturbances nor reduces sensitivity. The stability theorem just derived shows that open-loop control cannot stabilize an unstable plant, since $P(s)$ is required to be stable at the outset. It appears, then, that open-loop control is suitable only in cases where the plant is stable, well modeled, and not very perturbed, and where the objective is to adjust the set-point response.

Even then, there are limitations on the achievable transmission $H_{d}(j\omega)$ . The first is due to the actuators. From Figure 4.10, with $d = 0$ ,

$$u (s) = \frac {y (s)}{P (s)} = \frac {H _ {d} (s)}{P (s)} y _ {d} (s)$$

and

$$u (j \omega) = \frac {H _ {d} (j \omega)}{P (j \omega)} y _ {d} (j \omega). \tag {4.19}$$

Typically, $P$ is low-pass, so that, for $\omega$ greater than some $\omega_1$ , $|P(j\omega)|$ is less than 1 and becomes smaller as $\omega$ increases. Loosely speaking, $\omega_1$ is the natural bandwidth of the plant. If the set-point signal $y_d(t)$ has significant spectral content up to $\omega_b > \omega_1$ , it is desirable to make $H_d(j\omega) \approx 1$ for frequencies up to $\omega_b$ , in order to transmit $y_d$ faithfully. But this makes the ratio $|H_d(j\omega)/P(j\omega)|$ large for frequencies between $\omega_1$ and $\omega_b$ , and hence $|u(j\omega)|$ is relatively large at those frequencies. The actuator is then called upon to compensate for the low high-frequency gain of the plant and deliver considerable power at high frequencies; in most cases, this leads to higher costs. To summarize: pushing bandwidth beyond its natural plant level requires high-performance (and expensive)

The other limitation is more subtle and in

It appears when $P(s)$ has one or more RHP zeros. It is possible to make $H_{d}(s)$ equal 1 by choosing $F(s) = P^{-1}(s)$ . If $P(s)$ has no zeros in the closed RHP, such an $F(s)$ is stable and therefore satisfies the condition of internal stability. That condition is violated if $P(s)$ has an RHP zero, because that zero becomes an RHP pole of $F(s) = P^{-1}(s)$ . Therefore, it is not possible to have both $H_{d}(s)$ equal to 1 and internal stability if $P(s)$ has one or more zeros in the closed RHP.
