# 3.5.1 Meaningful Interpretation of Riccati Coefficient

Consider the matrix differential Riccati equation (3.2.34) with final condition $\mathbf{P}(t_{f}) = 0$ . Now consider a simple time transformation $\tau = t_{f} - t$ . Then, in $\tau$ scale we can think of the final time $t_{f}$ as the “starting time,” $\mathbf{P}(t_{f})$ as the “initial condition,” and $\bar{P}$ as the “steady-state solution” of the matrix DRE. As the time $t_{f} \to \infty$ , the “transient solution” is pushed to near $t_{f}$ which is at infinity. Then for most of the practical time interval the matrix $\mathbf{P}(t)$ becomes a steady state, i.e., a constant matrix $\bar{P}$ , as shown in Figure 3.7 [6]. Then the optimal control is given by

$$\mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {x} ^ {*} (t) = - \bar {\mathbf {K}} \mathbf {x} ^ {*} (t), \tag {3.5.7}$$

![](image/a0feeffa2997ba205d0c71613796614cc688c252ef15421d58c61afa018f8c35.jpg)

<details>
<summary>line</summary>

| Time Point | Value |
| --- | --- |
| t_f | steady-state interval (P(t)) |
| t_f | transient interval (P(t)) |
| t_f | 0 |
| t | P(t_f)=0 |
</details>

Figure 3.7 Interpretation of the Constant Matrix $\bar{P}$

where, $\bar{K} = R^{-1}B'\bar{P}$ is called the Kalman gain. Alternatively, we can write

$$\mathbf {u} ^ {*} (t) = - \bar {\mathbf {K}} _ {a} ^ {\prime} \mathbf {x} ^ {*} (t) \tag {3.5.8}$$

where, $\bar{K}_{a} = \bar{PBR}^{-1}$ . The optimal state is the solution of the system obtained by using the control (3.5.8) in the plant (3.5.1)

$$\dot {\mathbf {x}} ^ {*} (t) = \left[ \mathbf {A} - \mathbf {B} \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \right] \mathbf {x} ^ {*} (t) = \mathbf {G} \mathbf {x} ^ {*} (t), \tag {3.5.9}$$

where, the matrix $G = A - BR^{-1}B' \bar{P}$ must have stable eigenvalues so that the closed-loop optimal system (3.5.9) is stable. This is required since any unstable states with infinite time interval would lead to an infinite cost functional $J^{*}$ . Let us note that we have no constraint on the stability of the original system (3.5.1). This means that although the original system may be unstable, the optimal system must be definitely stable.

Finally, the minimum cost (3.2.29) is given by

$$J ^ {*} = \frac {1}{2} \mathbf {x} ^ {* \prime} (t) \bar {\mathbf {P}} \mathbf {x} ^ {*} (t). \tag {3.5.10}$$
