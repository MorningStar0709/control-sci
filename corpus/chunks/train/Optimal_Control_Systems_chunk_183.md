Figure 3.4 Closed-Loop Optimal Control System for Example 3.1

Using results similar to the previous case of finite final time $t_{f}$ (see Table 3.1), the optimal control for the infinite-horizon linear regulator system is obtained as

$$\mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \hat {\mathbf {P}} (t) \mathbf {x} ^ {*} (t), \tag {3.4.3}$$

where,

$$\hat {\mathbf {P}} (t) = \lim _ {t _ {f} \rightarrow \infty} \left\{\mathbf {P} (t) \right\}, \tag {3.4.4}$$

the nxn symmetric, positive definite matrix (for all $t \in [t_{0}, t_{f}]$ ) is the solution of the matrix differential Riccati equation (DRE)

$$\dot {\hat {\mathbf {P}}} (t) = - \hat {\mathbf {P}} (t) \mathbf {A} (t) - \mathbf {A} ^ {\prime} (t) \hat {\mathbf {P}} (t) - \mathbf {Q} (t) + \hat {\mathbf {P}} (t) \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \hat {\mathbf {P}} (t), \tag {3.4.5}$$

![](image/75b433413c6dccd7cf76159b8bf6fda785161f61d33e62cd9aade708f551bfa8.jpg)

<details>
<summary>line</summary>

| t | x₁(t) | x₂(t) |
| --- | --- | --- |
| 0.0 | 2.0 | -3.0 |
| 0.5 | 1.0 | -1.0 |
| 1.0 | 0.5 | -0.5 |
| 1.5 | 0.3 | -0.2 |
| 2.0 | 0.2 | -0.1 |
| 2.5 | 0.1 | -0.05 |
| 3.0 | 0.05 | -0.02 |
| 3.5 | 0.02 | -0.01 |
| 4.0 | 0.01 | -0.005 |
| 4.5 | 0.005 | -0.002 |
| 5.0 | 0.002 | -0.001 |
</details>

Figure 3.5 Optimal States for Example 3.1

![](image/b01b2a7bdab9e8d2c0393e333b21e2e327298bd20ea6617c3d93afcb3a8604eb.jpg)

<details>
<summary>line</summary>

| t | Optimal Control |
| --- | --- |
| 0.0 | 14.0 |
| 0.5 | 6.0 |
| 1.0 | 3.0 |
| 1.5 | 2.0 |
| 2.0 | 1.5 |
| 2.5 | 1.0 |
| 3.0 | 0.8 |
| 3.5 | 0.6 |
| 4.0 | 0.4 |
| 4.5 | 0.2 |
| 5.0 | 0.1 |
</details>

Figure 3.6 Optimal Control for Example 3.1

satisfying the final condition

$$\lim _ {t _ {f} \to \infty} \hat {\mathbf {P}} (t _ {f}) = 0. \tag {3.4.6}$$

The optimal cost is given by

$$J ^ {*} = \frac {1}{2} \mathbf {x} ^ {* \prime} (t) \hat {\mathbf {P}} (t) \mathbf {x} ^ {*} (t). \tag {3.4.7}$$

The proofs for the previous results are found in optimal control text specializing in quadratic methods [3]. Example 3.1 can be easily solved for $t_f \to \infty$ and $\mathbf{F} = 0$ .
