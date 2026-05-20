# Lead Compensation in the Frequency Domain

Lead compensation is used to increase the bandwidth of the closed-loop system. This is done by raising the crossover frequency, which (as the reader will recall) is roughly equal to the bandwidth.

To understand the principle, refer to Figure 6.15. It is easy to see that, for a phase margin of $45^{\circ}$ , the crossover frequency must be set at $\omega = 1.0$ rad/s; the reason is that $\neq L(j\omega) = -135^{\circ}$ at $\omega = 1.0$ . Suppose that the crossover frequency is to be doubled, to 2.0 rad/s while the $45^{\circ}$ phase margin is maintained. Since the phase at $\omega = 2.0$ must be $-135^{\circ}$ , it will be necessary to boost the phase of $L(j2)$ from $-190.3^{\circ}$ to $-135^{\circ}$ , a difference of $55.3^{\circ}$ . The purpose of lead compensation is to provide this phase boost, i.e., to provide phase lead near crossover.

A lead compensator has a transfer function

$$G _ {c} (s) = k \frac {\alpha T s + 1}{T s + 1}, \quad \alpha > 1. \tag {6.36}$$

As shown in Figure 6.24, (for $\alpha = 10$ ), $G_{c}$ provides phase lead in the midfrequency range. In that range, the compensator adds roughly 20 db/decade to the slope of the magnitude plot of the plant. This is consistent with Bode's theorem, insofar as it raises the slope in a region where it would normally be too negative to allow placement of the crossover frequency.

To calculate the maximum phase lead and the frequency where it occurs, we write

$$\phi = \not \prec G _ {c} (j \omega) = \tan^ {- 1} \alpha \omega T - \tan^ {- 1} \omega T$$

and differentiate with respect to $\omega$ . This yields

$$\frac {d}{d \omega} \phi = \frac {\alpha T}{1 + (\alpha \omega T) ^ {2}} - \frac {T}{1 + (\omega T) ^ {2}}.$$

To maximize, set the RHS to zero. This yields $\omega T = 1 / \sqrt{\alpha}$ . To calculate the maximum phase, we compute $\neq G_c(j\omega)$ with $\omega T = 1 / \sqrt{\alpha}$ . After some trigonometric manipulations, this turns out to be $\neq G_c = \sin^{-1}(\alpha - 1) / (\alpha + 1)$ .

![](image/1d21c319993a9eeced6b0f0aacb3db6e1147b19217b7be2868a48b6992d066a5.jpg)

<details>
<summary>line</summary>

| ωT | db |
| --- | --- |
| 10^-2 | 0 |
| 10^-1 | 5 |
| 10^0 | 15 |
| 10^1 | 20 |
</details>

![](image/84d6e812e91753578821e5bb7af67d8153011964186d5aaf0df4033c39769a88.jpg)

<details>
<summary>line</summary>

| ωT | Deg |
| --- | --- |
| 10^-2 | ~5 |
| 10^-1 | ~40 |
| 10^0 | ~55 |
| 10^1 | ~5 |
</details>
