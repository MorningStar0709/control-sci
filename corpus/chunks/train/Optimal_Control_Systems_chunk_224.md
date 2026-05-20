# 4.2 LQT System: Infinite-Time Case

In Chapter 3, in the case of linear quadratic regulator system, we extended the results of finite-time case to infinite-time (limiting or steady-state) case. Similarly, we now extend the results of finite-time case of the linear quadratic tracking system to the case of infinite time [3]. Thus, we restrict our treatment to time-invariant matrices in the plant and the performance index. Consider a linear time-invariant plant as

$$\dot {\mathbf {x}} (t) = \mathbf {A} \mathbf {x} (t) + \mathbf {B} \mathbf {u} (t) \tag {4.2.1}\mathbf {y} (t) = \mathbf {C x} (t). \tag {4.2.2}$$

The error is

$$\mathbf {e} (t) = \mathbf {z} (t) - \mathbf {y} (t), \tag {4.2.3}$$

and choose the performance index as

$$\lim _ {t _ {f} \rightarrow \infty} J = \lim _ {t _ {f} \rightarrow \infty} \frac {1}{2} \int_ {0} ^ {\infty} \left[ \mathbf {e} ^ {\prime} (t) \mathbf {Q e} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R u} (t) \right] d t \tag {4.2.4}$$

![](image/92b7c726812814e26fe82e9a1862859f11af9a68b861898d0e2728f2ff369f16.jpg)

<details>
<summary>line</summary>

| t | p₁₁(t) | p₁₂(t) | p₂₂(t) |
| --- | --- | --- | --- |
| 0 | 1.0 | 0.2 | 0.0 |
| 2 | 1.0 | 0.2 | 0.0 |
| 4 | 1.0 | 0.2 | 0.0 |
| 6 | 1.0 | 0.2 | 0.0 |
| 8 | 1.0 | 0.2 | 0.0 |
| 10 | 1.0 | 0.2 | 0.0 |
| 12 | 1.0 | 0.2 | 0.0 |
| 14 | 1.0 | 0.2 | 0.0 |
| 16 | 1.0 | 0.2 | 0.0 |
| 18 | 1.0 | 0.2 | 0.0 |
| 20 | 0.5 | 0.2 | 0.0 |
</details>

Figure 4.6 Riccati Coefficients for Example 4.2

to track the desired signal $\mathbf{z}(t)$ . Also, we assume that Q is an nxn symmetric, positive semidefinite matrix, and R is a rxr symmetric, positive definite matrix. Note that there is no terminal cost function in the PI (4.2.4) and hence F = 0.

An obvious way of getting results for infinite-time (steady-state) case is to write down the results of finite-time case and then simply let $t_{f} \to \infty$ . Thus, as $t_{f} \to \infty$ , the matrix function $\mathbf{P}(t)$ in (4.1.19) tends to the steady-state value $\bar{P}$ as the solution of

$$\boxed {- \bar {\mathbf {P}} \mathbf {A} - \mathbf {A} ^ {\prime} \bar {\mathbf {P}} + \bar {\mathbf {P}} \mathbf {B R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} - \mathbf {C} ^ {\prime} \mathbf {Q C} = 0.} \tag {4.2.5}$$

Also, the vector function $\mathbf{g}(t)$ in (4.1.20) tends to a finite function $\bar{\mathbf{g}}(t)$ as the solution of
