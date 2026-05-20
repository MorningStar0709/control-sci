Figure 4.23 shows, for $p_0 = 1$ and no RHP zeros, two complementary sensitivity magnitude curves that satisfy Equation 4.54. For demonstration purposes, the form $T(s) = (T_1s + 1) / (T_2s + 1)^2$ has been selected, with $T_2 = 2$ and 5, and $T_1$ calculated to satisfy the constraint $T(p_0) = 1$ . In contrast with the case of $S(j\omega)$ , we would ideally like to have $|T(j\omega)| = 1[\log |T(j\omega)| = 0]$ at low frequencies, with rolloff at frequencies beyond the bandwidth supported by the sensors and actuators. Clearly, it is necessary to accumulate some positive area at low frequencies, to compensate for the negative area generated at higher frequencies. If $\log |T(j\omega)|$ starts rolling off at some frequency that is appreciably less than $p_0 (= 1$ here), the negative area is given appreciable weight, and $\log |T(j\omega)|$ must be significantly greater than 0 over part of the passband. Conversely, if $\log |T(j\omega)|$ is to be near zero in the passband (thus accumulating a small positive area), then the rolloff must start at a frequency sufficiently high for the weight placed on the negative contribution to be small. The conclusion is that the control of an unstable system requires a bandwidth at least equal to the magnitude of the largest unstable pole.

Thus, whereas RHP zeros impose an upper limit on the bandwidth that can be achieved, RHP poles impose a lower limit on the bandwidth that must be achieved. The implication for actuators and sensors is that it is useless for the bandwidths of these components to extend much beyond the limit imposed by the RHP zeros, but that they must have enough bandwidth to control the unstable poles.

![](image/43239008c0f3e3e99deabab71b329b3211a13e18442bef521de43dc0123ba88f.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | T₂ = 2 | T₂ = 5 |
| --- | --- | --- |
| 0 | 1.0 | 1.0 |
| 2 | 0.3 | -0.5 |
| 4 | 0.1 | -1.0 |
| 6 | 0.0 | -1.5 |
| 8 | -0.1 | -1.8 |
| 10 | -0.2 | -2.0 |
| 12 | -0.3 | -2.2 |
| 14 | -0.4 | -2.4 |
| 16 | -0.5 | -2.5 |
</details>

Figure 4.23 Admissible complementary sensitivity functions
