# EXAMPLE 6.15 Local instability of a minimum-variance STR

Consider a process described by

$$
\begin{array}{l} y (t) - 1. 6 y (t - 1) - 0. 7 5 y (t - 2) \\ = u (t - 1) + u (t - 2) + 0. 9 u (t - 3) + e (t) + 1. 5 e (t - 1) + 0. 7 5 e (t - 2) \\ \end{array}
$$

The B polynomial has zeros at

$$z _ {1, 2} = - 0. 5 0 \pm 0. 8 1 i$$

Furthermore,

$$C \left(z _ {1, 2}\right) = - 0. 4 0 \pm 0. 4 0 i$$

The real part of C is thus negative at the zeros of B. This implies that the parameters corresponding to minimum-variance control make an unstable equilibrium for the ODEs. Furthermore, it follows from Theorem 4.2 that these parameter values are the only possible equilibrium point for the parameters. The following heuristic argument indicates that the estimates are bounded:

![](image/32e2ad4111f8afe8fc17f9f6a822fcbc539d5d2c75a719d7d2c301317ef02342.jpg)

<details>
<summary>line</summary>

| Time | ŝ₀ (Upper) | r̂₁ (Lower) | r̂₂ (Lower) | ŝ₁ (Lower) |
| --- | --- | --- | --- | --- |
| 0 | ~2.0 | ~1.0 | ~1.0 | ~-0.5 |
| 500 | ~3.0 | ~1.0 | ~1.0 | ~-0.5 |
| 1000 | ~2.8 | ~1.0 | ~1.0 | ~-0.5 |
| 1500 | ~3.0 | ~1.0 | ~1.0 | ~-0.5 |
| 2000 | ~2.8 | ~1.0 | ~1.0 | ~-0.5 |
</details>

Figure 6.20 The parameter estimates when a self-tuning controller is used on the process in Example 6.15. The dashed lines correspond to the optimal minimum-variance controller.

If the parameters are such that the closed-loop system is unstable, the inputs and the outputs will be so large that they will dominate the stochastic terms in the model. The estimates will then quickly approach values that correspond to a deadbeat controller for the system, which gives a stable closed-loop system. This argument can be made rigorous (see Johansson (1988)). The estimates will thus vary in a bounded area without converging to any point. Figure 6.20 shows the parameter estimates when a direct self-tuning regulator with the controller structure

$$u (t) = - \frac {\hat {s} _ {0} + \hat {s} _ {1} q ^ {- 1}}{1 + \hat {r} _ {1} q ^ {- 1} + \hat {r} _ {2} q ^ {- 2}} y (t)$$
