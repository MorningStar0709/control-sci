# EXAMPLE 3.10 Load disturbances: Modified estimator and controller

We now show that the difficulties found in Example 3.9 can be avoided by modifying the estimator and the controller. We first introduce a controller that has integral action by applying the design procedure that we have just described. To do this, we consider the same system as in Example 3.5 where the controller was defined by

![](image/cf7858f5b6e5f20f56c8bbce191869a0e87c81ce89a4f3e6a5721b33a9b3cd20.jpg)

<details>
<summary>line</summary>

| Time | u_c | y |
| --- | --- | --- |
| 0 | 0 | 1.0 |
| 25 | -1 | -1.0 |
| 50 | 1 | -1.0 |
| 75 | -1 | -1.0 |
| 100 | -1 | -1.0 |
</details>

Figure 3.16 Output and control signal with an indirect self-tuner with integral action and a modified estimator.

$$R ^ {0} = q + r _ {1} \quad S ^ {0} = s _ {0} q + s _ {1}$$

The closed-loop characteristic polynomial $A_{c}$ has degree three. To obtain a controller with integral action, the order of the closed-loop system is increased by introducing an extra closed-loop pole at $q = -x_{0} = 0$ . It then follows from Eq. (3.41) that

$$y _ {0} = - \frac {\mathbf {1} + r _ {1}}{b _ {0} + b _ {1}}$$

Hence $X = q$ and $Y = y_0$ , and Eqs. (3.39) now give

$$
\begin{array}{l} R = q (q + r _ {1}) + y _ {0} (b _ {0} q + b _ {1}) = (q - 1) (q - b _ {1} y _ {0}) \\ S = q \left(s _ {0} q + s _ {1}\right) - y _ {0} \left(q ^ {2} + a _ {1} q + a _ {2}\right) = \left(s _ {0} - y _ {0}\right) q ^ {2} + \left(s _ {1} - a _ {1} y _ {0}\right) q - a _ {2} y _ {0} \\ \end{array}
$$

The estimates are based on the model (3.42) with $A_{d} = q - 1$ to reduce the effects of the disturbances. Figure 3.16 shows a simulation corresponding to Fig. 3.14 with the modified self-tuning regulator. A comparison with Fig. 3.14 shows a significant improvement. The load disturbance is reduced quickly. Because of the integral action the control will decrease with a magnitude corresponding to the load disturbance shortly after t = 40. The parameter estimates are shown in Fig. 3.17, which indicates the advantages in using the modified estimator. Notice in particular that there is a very small change in the estimates when the load disturbance occurs.

![](image/64813a6c2c197efe5cd90d1289110ba59e904d59046198825927ae725de68361.jpg)

<details>
<summary>line</summary>

| Time | â₂ | â₁ |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 10 | 0.0 | -1.5 |
| 20 | 0.0 | -1.5 |
| 30 | 0.0 | -1.5 |
| 40 | 0.0 | -1.5 |
| 50 | 0.0 | -1.5 |
| 60 | 0.0 | -1.5 |
| 70 | 0.0 | -1.5 |
| 80 | 0.0 | -1.5 |
| 90 | 0.0 | -1.5 |
| 100 | 0.0 | -1.5 |
</details>

![](image/71b636000cc6a270f2841a75a9c9caf2458534e5808340902d1e9a260b88eb77.jpg)

<details>
<summary>line</summary>

| Time | b̂₁ | b̂₀ |
| --- | --- | --- |
| 0 | 0.2 | 0.0 |
| 10 | 0.1 | 0.05 |
| 20 | 0.1 | 0.1 |
| 30 | 0.1 | 0.1 |
| 40 | 0.1 | 0.1 |
| 50 | 0.1 | 0.1 |
| 60 | 0.1 | 0.1 |
| 70 | 0.1 | 0.1 |
| 80 | 0.1 | 0.1 |
| 90 | 0.1 | 0.1 |
| 100 | 0.1 | 0.1 |
</details>

Figure 3.17 Parameter estimates corresponding to Fig. 3.16.
