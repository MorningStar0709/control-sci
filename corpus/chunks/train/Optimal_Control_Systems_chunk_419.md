relation (7.5.27) can be conveniently written as

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} - q _ {j} ^ {*} (t) & \text { if } \quad | q _ {j} ^ {*} (t) | \leq 1 \\ - s g n \left\{q _ {j} ^ {*} (t) \right\} & \text { if } \quad | q _ {j} ^ {*} (t) | > 1, \end{array} \right. \tag {7.5.29}
$$

or more compactly component-wise as

$$u _ {j} ^ {*} (t) = - s a t \left\{q _ {j} ^ {*} (t) \right\}, \tag {7.5.30}$$

or in vector form as

$$\boxed {\mathbf {u} ^ {*} (t) = - S A T \left\{\mathbf {q} ^ {*} (t) \right\} = - S A T \left\{\mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t) \right\}} \tag {7.5.31}$$

shown in Figure 7.37.

The following notes are in order.

1. The constrained minimum-energy control law (7.5.31) is valid only if $\mathbf{R}(t)$ is positive definite.   
2. The energy-optimal control law (7.5.31), described by saturation (SAT) function, which is different from the signum (SGN) function for time-optimal control and dead-zone (DEZ)

![](image/b47468c7f12bd923d83af9f3f184ae691c732e666d8e99bca68ecde0f37c2f93.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -1 | -1 |
| 0 | 0 |
| +1 | +1 |
| u*(t) | +1 |
</details>

Figure 7.37 Energy-Optimal Control

function for fuel-optimal control functions, is a well-defined (determinate) function. Hence, the minimum-energy system has no option to be singular.

3. In view of the above, it also follows that the optimal control $\mathbf{u}^{*}(t)$ is a continuous function of time which again is different from the piece-wise constant functions of time for time-optimal and fuel-optimal control systems discussed earlier in this chapter.   
4. If the minimum-energy system described by the system (7.5.2) and the PI (7.5.3) has no constraint (7.5.4) on the control, then by the results of Chapter 3, we obtain the optimal control $\mathbf{u}^{*}(t)$ by using the Hamiltonian (7.5.6) and the condition

$$\frac {\partial \mathcal {H}}{\partial \mathbf {u}} = 0 \longrightarrow \mathbf {R} (t) \mathbf {u} _ {n} ^ {*} (t) + \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t) = 0 \longrightarrow\mathbf {u} _ {n} ^ {*} (t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t) = - \mathbf {q} ^ {*} (t), \tag {7.5.32}$$

where, $\mathbf{u}_{n}^{*}(t)$ refers to unconstraint control. Comparing the relation (7.5.32) with (7.5.29), we see that
