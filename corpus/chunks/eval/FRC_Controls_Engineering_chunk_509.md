# Case study: second-order CIM motor model

Each feedforward implementation has advantages. The steady-state feedforward allows using specific actuators to maintain the reference at steady-state. Plant inversion doesn’t support this, but can be used for reference tracking as well with the same tuning parameters as LQR design. Figure C.2 shows both types of feedforwards applied to a second-order CIM motor model.

Plant inversion isn’t as effective in figure C.2 because the R matrix penalized control effort. If the R cost matrix is removed from the plant inversion calculation, the reference tracking is much better (see figure C.3).

![](image/2f48b4fc4ccb7cecd41837bf4973ce32a472d8fc23696e9756da445520b7e670.jpg)

<details>
<summary>line</summary>

| Time (s) | Reference (rad/s) | No FF (rad/s) | Steady-state FF (rad/s) | Plant inversion (Q and R cost) (rad/s) | Current (A) | Input (V) |
|----------|-------------------|---------------|--------------------------|----------------------------------------|-------------|-----------|
| 0.000    | 200               | 100           | 100                      | 10                                     | 0           | 10        |
| 0.005    | 200               | 100           | 100                      | 10                                     | 10          | 5         |
| 0.010    | 200               | 50            | 50                       | 5                                      | 5           | 5         |
| 0.015    | 200               | 25            | 25                       | 2.5                                    | 5           | 5         |
| 0.020    | 200               | 25            | 25                       | 2.5                                    | 5           | 5         |
| 0.025    | 200               | 25            | 25                       | 2.5                                    | 5           | 5         |
</details>

![](image/9f9aafc964e31188817e69585067a2c8165fd8c69c00edfa0659e6b2103990eb.jpg)

<details>
<summary>line</summary>
