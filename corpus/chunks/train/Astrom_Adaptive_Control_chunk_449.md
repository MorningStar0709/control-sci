# EXAMPLE 6.10 Unmodeled dynamics

Assume that the nominal transfer function (6.56) has $a = 1$ and $b = 2$ but that the actual transfer function is

$$G (s) = \frac {4 5 8}{(s + 1) (s ^ {2} + 3 0 s + 2 2 9)} \tag {6.63}$$

The dynamics correspond to the nominal plant $2/(s+1)$ cascaded with $229/(s^{2}+30s+229)$ . The process thus has two poles $s = -15 \pm 2i$ , which were neglected in the model used to design the adaptive controller. Figure 6.13 shows the behavior of the controller parameters when the command signal is a step and there is a sinusoidal measurement error. Figure 6.14 shows the behavior of the parameters when the command signal is sinusoidal with different frequencies.

![](image/122c507a004deebf856671347c352c7d1a40f013187cd67e30ec0ac73adfef84.jpg)

<details>
<summary>line</summary>

| Time | θ̂₁ (no noise) | θ̂₂ (no noise) | θ̂₂ (no noise) |
| --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 |
| 10 | ~0.4 | ~-0.1 | ~-0.15 |
| 20 | ~0.45 | ~-0.1 | ~-0.15 |
| 30 | ~0.5 | ~-0.1 | ~-0.15 |
| 40 | ~0.6 | ~-0.1 | ~-0.15 |
</details>

Figure 6.18 Controller parameters $\hat{\theta}_1$ and $\hat{\theta}_2$ when the adaptive control law of Eqs. (6.57) is applied to the process of Eq. (6.63). The command signal is a step, and there is sinusoidal measurement noise. The smooth curves show the behavior when there is no measurement noise.

Example 6.10 shows that the presence of unmodeled dynamics will drastically change the behavior of the adaptive system. Figure 6.14 shows that the equilibrium depends on the frequency of the command signal and that it may be unstable for certain frequencies. We now attempt to understand the mechanisms that change the behavior of the system so drastically and to find suitable remedies.
