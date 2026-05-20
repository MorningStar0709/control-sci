# EXAMPLE 6.8 Sinusoidal command signal

Consider a reference model with the transfer function

$$G _ {m} (s) = \frac {a}{s + a}$$

Assume that the process has the transfer function

$$G (s) = \frac {a b}{(s + a) (s + b)}$$

Furthermore, let the command signal be a sinusoid with unit amplitude and frequency $\omega$ . Equations (6.55) give the equilibrium values

$$\bar {\theta} _ {\mathrm{MIT}} = \frac {k _ {0}}{k} \frac {b ^ {2} + \omega^ {2}}{b ^ {2}}\bar {\theta} _ {\mathrm{SPR}} = \frac {k _ {0}}{k} \frac {a \left(b ^ {2} + \omega^ {2}\right)}{b \left(a b - \omega^ {2}\right)} \quad \omega < \sqrt {a b}$$

The stability conditions show that the MIT rule is stable for all $\omega$ , but the SPR rule is stable only if $\omega < \sqrt{ab}$ . Figure 6.10 shows the estimates of the gain for the case behavior a = 1 and b = 10 when the input signals have frequencies $\omega = 3$ and $\omega = 3.4$ . The equilibrium values predicted by the averaging theory are also shown in the figure. The SPR is unstable for $\omega = 3.4 > \sqrt{10}$ . Also notice the drastic difference in the equilibrium values between the different updating methods. The desired equilibrium value is $\theta_{0} = k_{0}/k$ .

![](image/c70d14587af3b8db745ed7efaadb8c044bf94090ab1800d69f1c7ba74724a03e.jpg)

<details>
<summary>line</summary>

| Time | θ̂ |
| --- | --- |
| 0 | 0.0 |
| 100 | 1.0 |
| 300 | 1.0 |
| 500 | 1.0 |
</details>

![](image/77883618ba9d0a2a28971bc3b5f1c98112049048eb25170e772028ea6cda0a73.jpg)

<details>
<summary>line</summary>

| Time | θ̂ |
| --- | --- |
| 0 | 0.0 |
| 100 | 1.0 |
| 300 | 1.0 |
| 500 | 1.0 |
</details>

![](image/ca0d69c7cb720ec46c120b66cc96ecbd9de6ad5a51f4c57b8f626cb1cdee2e4c.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | 0 |
| 100 | ~4 |
| 300 | ~8 |
| 500 | ~10 |
</details>

![](image/2f45ff9980f1fdcb9d6238ad4e6c33fcee942f0f71ff15078a6ca8f70824f654.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | 0 |
| 100 | 5 |
| 200 | 10 |
</details>

Figure 6.10 Estimated feedforward gains obtained by the MIT rule with sinusoidal input signals having frequencies (a) $\omega = 3$ ; (b) $\omega = 3.4$ ; and the SPR rule when (c) $\omega = 3$ ; (d) $\omega = 3.4$ , for a system with $G_{m} = 1/(s + 1)$ and $G = 10/((s + 1)(s + 10))$ . The dashed lines are the equilibrium values obtained from averaging analysis.
