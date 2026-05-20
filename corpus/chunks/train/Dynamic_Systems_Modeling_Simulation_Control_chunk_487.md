# Example 9.5

Figure 9.16 shows the block diagram of an LTI system where the input is a sine wave. Use the Bode diagram in Fig. 9.15 to compute the frequency response of this system.

We can use the Bode diagram in Fig. 9.15 because this diagram corresponds to the system transfer function in Fig. 9.16. Reading Fig. 9.15 with input frequency ?? = 7 rad/s, we obtain the following magnitude and phase:

$$\left| G (j 7) \right| _ {\mathrm{dB}} = - 2. 5 \mathrm{dB}\phi = \angle G (j 7) = - 6 0 ^ {\circ}$$

![](image/6a45fecf435ca55373544a1b53bcdda734fabf81526d6f7a0f42ad2a57b2b102.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Input, u(t) = 4.5sin7t"] --> B["6/(s + 4)"]
    B --> C["Output, y"]
    style B fill:#f9f,stroke:#333
```
</details>

Figure 9.16 LTI system for Example 9.5.

Therefore, the absolute-value magnitude is

$$| G (j 7) | = 1 0 ^ {- 2. 5 / 2 0} = 0. 7 5$$

and the phase angle is $\phi = - 1 . 0 4 7 2$ rad. Finally, using the input amplitude $U _ { 0 } = 4 . 5$ and Eq. (9.17) the frequency response is

$$
\begin{array}{l} y _ {\mathrm{ss}} (t) = | G (j \omega) | U _ {0} \sin (\omega t + \phi) \\ = (0. 7 5) (4. 5) \sin (7 t - 1. 0 4 7 2) \\ = 3. 3 7 5 \sin (7 t - 1. 0 4 7 2) \\ \end{array}
$$

In summary, the frequency response has an amplitude of 3.375, frequency of 7 rad/s (same as the input), and phase angle of −1.0472 rad (−60∘) relative to the input sinusoid.
