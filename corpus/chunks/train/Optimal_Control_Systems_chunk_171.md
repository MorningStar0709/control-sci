7. Computation of Matrix DRE: Under some conditions we can get analytical solution for the nonlinear matrix DRE as shown later. But in general, we may try to solve the matrix DRE (3.2.18) by integrating backwards from its known final condition (3.2.19).

8. Independence of the Riccati Coefficient Matrix $\mathbf{P}(t)$ : The matrix $\mathbf{P}(t)$ is independent of the optimal state $\mathbf{x}^{*}(t)$ , so that once the system and the cost are specified, that is, once we are given the system/plant matrices $\mathbf{A}(t)$ and $\mathbf{B}(t)$ , and the performance index matrices $\mathbf{F}(t_{f})$ , $\mathbf{Q}(t)$ , and $\mathbf{R}(t)$ , we can independently compute the matrix $\mathbf{P}(t)$ before the optimal system operates in the forward direction from its initial condition. Typically, we compute (offline) the matrix $\mathbf{P}(t)$ backward in the interval $t \in [t_{f}, t_{0}]$ and store them separately, and feed these stored values when the system is operating in the forward direction in the interval $t \in [t_{0}, t_{f}]$ .

9. Implementation of the Optimal Control: The block diagram implementing the closed-loop optimal controller (CLOC) is shown in Figure 3.2. The figure shows clearly that the CLOC gets its values of $\mathbf{P}(t)$ externally, after solving the matrix DRE backward in time from $t = t_{f}$ to $t = t_{0}$ and hence there is no way that we can implement the closed-loop optimal control configuration on-line.

It is to be noted that the optimal control $\mathbf{u}^{*}(t)$ can be solved and implemented in open-loop configuration by using the Pontryagin procedure given in Chapter 2. In that case, the open-loop optimal controller (OLOC) is quite cumbersome compared to the equivalent closed-loop optimal controller as will be illustrated later in this chapter.

10. Linear Optimal Control: The optimal feedback control $\mathbf{u}^*(t)$ given by (3.2.12) is written as

$$\boxed {\mathbf {u} ^ {*} (t) = - \mathbf {K} (t) \mathbf {x} ^ {*} (t)} \tag {3.2.45}$$

where, the Kalman gain $\mathbf{K}(t) = \mathbf{R}^{-1}(t)\mathbf{B}'(t)\mathbf{P}(t)$ . Or alternatively, we can write

$$\mathbf {u} ^ {*} (t) = - \mathbf {K} _ {a} ^ {\prime} (t) \mathbf {x} ^ {*} (t) \tag {3.2.46}$$
