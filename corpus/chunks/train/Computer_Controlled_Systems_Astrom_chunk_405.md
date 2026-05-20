# Simple Criteria

A simple way to specify regulation performance is to give allowable errors for typical disturbances. For example, it can be required that a step disturbance give no steady-state error, and that the error due to a ramp disturbance be a fraction of the ramp velocity. These specifications are typically expressed in terms of the steady-state behavior, as discussed in Sec. 3.5. The error coefficients give requirements only on the low-frequency behavior. The bandwidth of the system should therefore be specified, in addition to the error coefficients.

Another more complete way to specify regulation performance is to give conditions on the transfer function from the disturbances to the process output.

![](image/ed7b7b37d1d6ab9b5dc4836db49c271dc3d9373ffd54b7400258ec6a3dc7a7cb.jpg)

<details>
<summary>line</summary>

| Process output | Probability density (Test limit) | Probability density (Set point for regulator with low variance) | Probability density (Set point for regulator with high variance) |
| --- | --- | --- | --- |
| -2 | 0.0 | 0.0 | 0.0 |
| 0 | 0.5 | 0.0 | 0.1 |
| 2 | 0.0 | 0.5 | 0.3 |
| 4 | 0.0 | 0.0 | 0.1 |
| 6 | 0.0 | 0.0 | 0.0 |
</details>

Figure 6.7 Expressing regulation performance in terms of variation in quality variables.
