# EXAMPLE 3.4 Indirect self-tuner with cancellation of process zero

Let the process be the same as in Example 3.1 and assume that the process zero is canceled. The specifications are the same as in Example 3.1, that is, to obtain a closed-loop characteristic polynomial $A_{m}$ . The parameters of the model

$$y (t) + a _ {1} y (t - 1) + a _ {2} y (t - 2) = b _ {0} u (t - 1) + b _ {1} u (t - 2)$$

![](image/465ac721109d44465511a8ad4f6cb74c41c884ff1a629a5eee4454da53e25517.jpg)

<details>
<summary>line</summary>

| Time | u_c | y |
| --- | --- | --- |
| 0 | 1 | 1 |
| 20 | 1 | 1 |
| 30 | -1 | -1 |
| 50 | -1 | 1 |
| 60 | 1 | 1 |
| 75 | 1 | -1 |
| 80 | -1 | -1 |
| 90 | -1 | -1 |
| 100 | -1 | -1 |
</details>

![](image/12b57b9471da6ec7147f8afa78144063d4588ba9131f7170b55dcca720136fbd.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | ~3.0 |
| 5 | ~-4.0 |
| 10 | ~0.0 |
| 15 | ~0.0 |
| 20 | ~0.0 |
| 25 | ~-3.0 |
| 30 | ~0.0 |
| 35 | ~0.0 |
| 40 | ~0.0 |
| 45 | ~0.0 |
| 50 | ~2.0 |
| 55 | ~-1.0 |
| 60 | ~0.0 |
| 65 | ~0.0 |
| 70 | ~0.0 |
| 75 | ~-3.0 |
| 80 | ~0.0 |
| 85 | ~0.0 |
| 90 | ~0.0 |
| 95 | ~0.0 |
| 100 | ~0.0 |
</details>

Figure 3.4 Output and input in using an indirect self-tuning regulator to control the system in Example 3.1. Notice the "ringing" in the control signal due to cancellation of the zero at -0.84.

![](image/7c8ba9943325991e3e2e9cf38a2e82dae36389549300be288b9b8fa376caedbd.jpg)

<details>
<summary>line</summary>

| Time | a₂ | a₁ | b̂₁ | b̂₀ |
| --- | --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.2 | 0.0 |
| 1 | -0.5 | -0.5 | 0.2 | 0.0 |
| 2 | -1.0 | -1.0 | 0.1 | 0.0 |
| 3 | -1.5 | -1.5 | 0.1 | 0.0 |
| 4 | -1.8 | -1.8 | 0.1 | 0.0 |
| 5 | -1.9 | -1.9 | 0.1 | 0.0 |
| 6 | -1.95 | -1.95 | 0.1 | 0.0 |
| 7 | -1.98 | -1.98 | 0.1 | 0.0 |
| 8 | -1.99 | -1.99 | 0.1 | 0.0 |
| 9 | -1.995 | -1.995 | 0.1 | 0.0 |
| 10 | -1.998 | -1.998 | 0.1 | 0.0 |
| 11 | -1.999 | -1.999 | 0.1 | 0.0 |
| 12 | -1.9995 | -1.9995 | 0.1 | 0.0 |
| 13 | -1.9998 | -1.9998 | 0.1 | 0.0 |
| 14 | -1.9999 | -1.9999 | 0.1 | 0.0 |
| 15 | -1.99995 | -1.99995 | 0.1 | 0.0 |
| 16 | -1.99998 | -1.99998 | 0.1 | 0.0 |
| 17 | -1.99999 | -1.99999 | 0.1 | 0.0 |
| 18 | -1.999995 | -1.999995 | 0.1 | 0.0 |
| 19 | -1.999998 | -1.999998 | 0.1 | 0.0 |
| 20 | -2.0 | -2.0 | 0.1 | 0.0 |
</details>

Figure 3.5 Parameter estimates corresponding to the simulation in Fig. 3.4. The true parameters are shown by dashed lines.

which has the same structure as Eq. (3.17), are estimated by using the least-squares algorithm. Algorithm 3.2 is used for the self-tuning regulator. The calculations, which were done in Example 3.1, give the control law
