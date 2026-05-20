# Example 11.2 Time-varying controller

Consider the integrator process

$$x (k + 1) = x (k) + u (k)$$

Let the loss function be

$$\sum_ {k = 0} ^ {4} \left(x ^ {2} (k) + 1 0 u ^ {2} (k)\right) + q _ {0} x ^ {2} (5)$$

![](image/0ffe9a6019dc01ada9db232973f464da4497c83ec56546569c8c6404a5e3a1b2.jpg)

<details>
<summary>line</summary>

| Control weighting ρ | Gains l_t (solid) | Gains l_t (dashed) |
| --- | --- | --- |
| 10^-5 | 2.0 | 2.0 |
| 10^0 | ~0.5 | ~1.0 |
| 10^5 | ~0.1 | ~0.2 |
</details>

Figure 11.3 Linear quadratic controller for the double integrator. The stationary gains $l_{1}$ (solid) and $l_{2}$ (dashed) of the feedback vector $L = [l_{1}, l_{2}]$ for different values of $\rho$ .

That is, the time horizon is only five steps. The Riccati equation and the controller gain become

$$s (k) = s (k + 1) + 1 - \frac {s ^ {2} (k + 1)}{s (k + 1) + 1 0} \quad s (5) = q _ {0}l (k) = \frac {s (k + 1)}{s (k + 1) + 1 0}$$

Figure 11.4 shows $s(k), l(k)$ , and the trajectory of the state when $x(0) = 1$ for different values of $q_0$ . The value $q_0 = 3.70$ corresponds to the stationary solution of the Riccati equation. When $q_0$ is increasing $x(5)$ approaches zero.
