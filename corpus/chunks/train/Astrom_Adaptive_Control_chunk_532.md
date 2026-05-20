![](image/e53d39897c49b69e863ddf74eded409f0066ac4f9b111df3cb1c7f3ee92c0af2.jpg)

<details>
<summary>scatter</summary>

| p | Loss/step (a) | Loss/step (b) | Loss/step (c) |
| --- | --- | --- | --- |
| 0.003 | 2.5 | 1.5 | 1.0 |
| 0.1 | 3.5 | 2.0 | 1.5 |
| 0.2 | 4.5 | 2.5 | 2.0 |
| 0.3 | 6.0 | 4.0 | 3.0 |
| 0.4 | 7.5 | 5.5 | 4.0 |
| 0.5 | 9.5 | 7.0 | 4.5 |
</details>

Figure 7.8 The mean values and standard deviations of the losses for Monte Carlo runs with different values of $\sqrt{R_{1}}$ for the system in Example 7.6. (a) Cautious controller. (b) Suboptimal dual controller from Wittenmark and Elcvitch (1985). (c) Numerically computed optimal dual controller from Åström and Helmersson (1982).

For $\sqrt{R_{1}} = 0.003$ there is good agreement between the suboptimal controller and the optimal dual controller that was derived under the assumption that $R_{1} = 0$ . The optimal dual controller from Example 7.4 corresponds to $R_{1} = 0$ . The controller obtained has been used also for $\sqrt{R_{1}} = 0.003$ .

In Eq. (7.20), $R_{2}/p_{b_{0}}(t+1)$ is used as a normalization factor in the term added to the loss function. The reason is an attempt to preserve a property of the dual optimal controller. In Example 7.4 the loss $V_{N}$ was a function of the normalized variables $\eta$ and $\beta$ . The loss function of Eq. (7.19) with Eq. (7.20) will also have this property for the integrator example. Simulations indicate that the normalization in Eq. (7.20) also makes the choice of $\rho$ less crucial. ☐
