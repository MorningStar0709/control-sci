Given T (and S), the second phase of a 2-DOF design is carried out by choosing a stable $H_{d}(s)$ with zeros at the closed RHP zeros of P, and such that $H_{d}(j\omega) \approx 1$ in the desired passband for the set-point signal. Once $H_{d} = RPS$ is known, R can be calculated since P and S are given. Note that the problem of selecting a stable $H_{d}$ with given RHP zeros is basically the open-loop design problem. Also note that the unstable poles of P do not matter. Although such poles (in the presence of RHP zeros) have a deleterious effect on the sensitivity, they do not restrict our freedom to choose the set-point transmission.

To complete the discussion of 2-DOF design, we note that

$$
\begin{array}{l} u = \frac {1}{P} (y - d) \\ = \frac {H _ {d}}{P} y _ {d} - \frac {T}{P} (d + v) \tag {4.72} \\ \end{array}
$$

so that the control effort tends to be large if $|T(j\omega)|$ or $|H_{d}(j\omega)|$ is large over a bandwidth greatly exceeding that of $P(j\omega)$ . Thus, T should be rolled off outside the disturbance-stop bandwidth, and $H_{d}$ should attenuate outside the set-point passband.
