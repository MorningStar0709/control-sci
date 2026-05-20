# 5.5 Sensitivity to Modeling Errors

A process model is a key element in control-system design. It is interesting to investigate how sensitive the closed-loop system is to modeling errors and also to determine how accurate the model needs to be for a successful control design. These problems can be approached very naturally in polynomial design. We refer to the discussion of sensitivity and robustness in Sec. 3.3.

![](image/bacbf2be223d8607769495c850c33bac6459f852f89c5ba0215c01b04e80fece.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 1 |
| 5 | 1 | 0 |
| 10 | 1 | 0 |
</details>

![](image/809a1c7af0692fe448725b1be6dfa3b16dae5fcde18c11f28f802852c42e5658.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 1 |
| 5 | 1 | 0 |
| 10 | 1 | 0 |
</details>

Figure 5.5 Step response of a motor with pole-placement control. The specifications are $\omega = 1$ and $\zeta = 0.7$ . The sampling periods are (a) $h = 0.25$ and (b) $h = 1.0$ . The process zero is not canceled.
