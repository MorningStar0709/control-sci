# Predictive First-Order Hold

A drawback of the zero- and first-order hold is that the output is discontinuous.

![](image/a198e98c6a2dbc27e30b0477c07ebca3f847ea30f6d44ce5633652006b1cb29a.jpg)

<details>
<summary>line</summary>

| Time | Series 1 | Series 2 |
| --- | --- | --- |
| t₀ | ● | ● |
| t₁ | ● | ● |
| t₂ | ● | ● |
| t₃ | ● | ● |
| t₄ | ● | ● |
| t₅ | ● | ● |
| t₆ | ● | ● |
</details>

Figure 7.5 Sampling and first-order-hold reconstruction of a continuous-time signal.

![](image/c2378d80742a25e6eb0ae091cba423e75bd0c90163ba5b72b22ab378155c2f09.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| t₀ | 0.8 |
| t₁ | 0.6 |
| t₂ | 0.7 |
| t₃ | 1.2 |
| t₄ | 0.9 |
| t₅ | 1.1 |
| t₆ | 1.5 |
</details>

Figure 7.6 Sampling and predictive first-order hold reconstruction of a continuous-time signal.

A way to avoid this problem is to use a predictive first-order-hold. The inter-sample behavior with this hold circuit is a linear interpolation of the sampled values; see Figure 7.6. Mathematically the reconstruction can be described by

$$f (t) = f (t _ {k}) + \frac {t - t _ {k}}{t _ {k + 1} - t _ {k}} \left(f (t _ {k + 1}) - f (t _ {k})\right) \quad t _ {k} \leq t < t _ {k + 1} \tag {7.9}$$

Notice that this requires that $f(t_{k+1})$ is available at time $t_{k}$ . For general applications the predictive first-order hold is not realizable. The value $f(t_{k+1})$ can be replaced by a prediction. This can be done very conveniently in a feedback loop, as will be discussed in Section 7.5.
