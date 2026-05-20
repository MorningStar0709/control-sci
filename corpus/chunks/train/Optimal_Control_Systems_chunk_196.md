# 3.5.4 Stability Issues of Time-Invariant Regulator

Let us consider the previous result for linear time-invariant system with infinite-time horizon from relations $(3.5.12)$ to $(3.5.17)$ and Table 3.3. We address briefly some stability remarks of the infinite-time regulator system $[3, 89]$ .

![](image/22899fd78e1c8f6baceeec4b9a72b27ebcc5794cf49beb677cda77b5e5d5c62e.jpg)

<details>
<summary>line</summary>

| t | x₁(t) | x₂(t) |
| --- | --- | --- |
| 0 | 2.0 | -3.0 |
| 1 | 0.5 | -1.0 |
| 2 | 0.2 | -0.5 |
| 3 | 0.1 | -0.2 |
| 4 | 0.05 | -0.1 |
| 5 | 0.02 | -0.05 |
| 6 | 0.01 | -0.02 |
| 7 | 0.005 | -0.01 |
| 8 | 0.002 | -0.005 |
| 9 | 0.001 | -0.002 |
| 10 | 0.0005 | -0.001 |
</details>

Figure 3.10 Optimal States for Example 3.2

1. The closed-loop optimal system (3.5.16) is not always stable especially when the original plant is unstable and these unstable states are not weighted in the PI (3.5.13). In order to prevent such a situation, we need the assumption that the pair $[A, C]$ is detectable, where C is any matrix such that $C'C = Q$ , which guarantees the stability of closed-loop optimal system. This assumption essentially ensures that all the potentially unstable states will show up in the $\mathbf{x}'(t)\mathbf{Q}\mathbf{x}(t)$ part of the performance measure.   
2. The Riccati coefficient matrix $\bar{P}$ is positive definite if and only if $[A,C]$ is completely observable.   
3. The detectability condition is necessary for stability of the closed-loop optimal system.   
4. Thus both detectability and stabilizability conditions are necessary for the existence of a stable closed-loop system.

![](image/8ae967455ad625076a94b6f028a8cb3f498309d512184792e001ab51dbb6636e.jpg)

<details>
<summary>line</summary>

| t | u(t) |
| --- | --- |
| 0 | 15.0 |
| 1 | 5.0 |
| 2 | 2.5 |
| 3 | 1.0 |
| 4 | 0.5 |
| 5 | 0.25 |
| 6 | 0.1 |
| 7 | 0.05 |
| 8 | 0.025 |
| 9 | 0.01 |
| 10 | 0.005 |
</details>

Figure 3.11 Optimal Control for Example 3.2
