# Zero-Order Hold (ZOH)

In previous chapters zero-order-hold sampling has been used. This causal reconstruction is given by

$$f (t) = f \left(t _ {k}\right) \quad t _ {k} \leq t < t _ {k + 1} \tag {7.8}$$

This means that the reconstructed signal is piecewise constant, continuous from the right, and equal to the sampled signal at the sampling instants. Because of its simplicity, the zero-order hold is very common in computer-controlled systems. The standard D-A converters are often designed in such a way that the old value is held constant until a new conversion is ordered. The zero-order hold also has the advantage that it can be used for nonperiodic sampling. Notice, however, that the reconstruction in (7.8) gives an exact inverse of the sampling operation only for signals that are right continuous and piecewise constant over the sampling intervals. For all other signals, the reconstruction of (7.8) gives an error (see Fig. 7.4).

![](image/fbb2c1977c43a5d02a358fc52fd9172c5269cfb724760e8162fae2f47e44128c.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| t₀ | 0.5 |
| t₁ | 0.3 |
| t₂ | 0.4 |
| t₃ | 0.8 |
| t₄ | 0.6 |
| t₅ | 0.7 |
| t₆ | 1.0 |
</details>

Figure 7.4 Sampling and zero-order-hold reconstruction of a continuous-time signal.
