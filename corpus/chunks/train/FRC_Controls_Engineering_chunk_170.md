# 6.11.4 Simulation

Python Control will be used to discretize the model and simulate it. One of the frccontrol examples[14] creates and tests a controller for it. Figure 6.9 shows the closed-loop system response.

![](image/19a60c9fc4aafd6f8ce07ccfa35571bdeedefc86e42537078d555a302e5ca99e.jpg)

<details>
<summary>line</summary>

| Time (s) | Reference (rad/s) | State (rad/s) | Reference (V) | State (V) |
| --- | --- | --- | --- | --- |
| 0.0 | 0.0 | 0.0 | 10.0 | 0.0 |
| 0.5 | 0.0 | 0.4 | 10.0 | 0.4 |
| 1.0 | 0.0 | 0.6 | 10.0 | 0.6 |
| 1.5 | 0.0 | 0.8 | 10.0 | 0.8 |
| 2.0 | 0.0 | 1.0 | 10.0 | 1.0 |
| 2.5 | 0.0 | 1.0 | 10.0 | 0.0 |
</details>

Figure 6.9: Single-jointed arm response
