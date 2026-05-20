# Example 9.1 Double integrator with antireset windup

A controller with integral action for the double integrator was designed in Sec. 5.7. In this example we use the same design procedure with parameters $\omega = 0.4$ and $\omega h = 0.2$ . The result when using the antireset windup procedure in Fig. 9.7 with $A_{\text{out}} = (q - 0.5)^2$ is shown in Fig. 9.8. The antireset windup gives less overshoot and the control signal is only saturating at the maximum value. The response with the antireset windup is similar but somewhat slower than for the unsaturated case.

A generalization of the antireset windup in Fig. 9.7 is given in Fig. 9.9. An extra degree of freedom is introduced through the polynomial $A_{n}$ . This polynomial, as well as $A_{ww}$ , should be monic and stable. The case in Fig. 9.7 is obtained for $A_{n} = 1$ . The polynomial $A_{n}$ can be used to shape the response from errors due to the saturation.

![](image/7783b2ea235af73eec7a5f73f05a382a11fe78865c590b813817433ca6279234.jpg)

<details>
<summary>line</summary>

| Time | Output (Solid) | Output (Dashed) | Input (Solid) | Input (Dashed) |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0.05 | 0.05 |
| 25 | 1.0 | 1.0 | -0.1 | -0.1 |
</details>

![](image/a73f79680844eb9bdce1d22dcd115b995da3a88dbe809fe62047ec3c0799f098.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 0.1 |
| 25 | 1 | -0.1 |
</details>

Figure 9.8 Output and input when the double integrator is controlled with a controller (a) without and (b) with antirest windup given by (9.12). The dashed lines show the behavior when there is no saturation.
