# 5.5 Discrete-Time Linear Quadratic Tracking System

In this section, we address linear quadratic tracking (LQT) problem for a discrete-time system and are interested in obtaining a closed-loop control scheme that enables a given system track (or follow) a desired trajectory over the given interval of time. We essentially deal with linear, time-invariant systems in order to get some elegant results although the method can as well be applied to nonlinear, time-varying case [89].

![](image/bb52b3b0632116f8a1b5d6daa35d2ef2447bce9c51161719ffb32c38cfba6f0b.jpg)

<details>
<summary>line</summary>

| k | Optimal Control |
| --- | --- |
| 0 | -4.0 |
| 1 | -1.0 |
| 2 | 0.0 |
| 3 | 0.1 |
| 4 | 0.05 |
| 5 | 0.0 |
| 6 | 0.0 |
| 7 | 0.0 |
| 8 | 0.0 |
| 9 | 0.0 |
| 10 | 0.0 |
</details>

Figure 5.11 Optimal Control for Example 5.5

Let us consider a linear, time-invariant system described by the state equation

$$\mathbf {x} (k + 1) = \mathbf {A x} (k) + \mathbf {B u} (k) \tag {5.5.1}$$

and the output relation

$$\mathbf {y} (k) = \mathbf {C x} (k). \tag {5.5.2}$$

The performance index to be minimized is

$$
\begin{array}{l} J = \frac {1}{2} \left[ \mathbf {C x} (k _ {f}) - \mathbf {z} (k _ {f}) \right] ^ {\prime} \mathbf {F} \left[ \mathbf {C x} (k _ {f}) - \mathbf {z} (k _ {f}) \right] \\ + \frac {1}{2} \sum_ {k = k _ {0}} ^ {k _ {f} - 1} \left\{\left[ \mathbf {C x} (k) - \mathbf {z} (k) \right] ^ {\prime} \mathbf {Q} \left[ \mathbf {C x} (k) - \mathbf {z} (k) \right] + \mathbf {u} ^ {\prime} (k) \mathbf {R u} (k) \right\} \tag {5.5.3} \\ \end{array}
$$

where, $\mathbf{x}(k)$ , $\mathbf{u}(k)$ , and $\mathbf{y}(k)$ are n, r, and n order state, control, and output vectors, respectively. Also, we assume that F and Q are each nxn dimensional positive semidefinite symmetric matrices, and R is an rxr positive definite symmetric matrix. The initial condition is given as $\mathbf{x}(k_{0})$ and the final condition $\mathbf{x}(k_{f})$ is free with $k_{f}$ fixed. We want the error $\mathbf{e}(k)=\mathbf{y}(k)-\mathbf{z}(k)$ as small as possible with minimum control effort, where $\mathbf{z}(k)$ is n dimensional reference vector. The methodology to obtain the solution for the optimal tracking system is carried out using the following steps.

- Step 1: Hamiltonian   
- Step 2: State and Costate System   
- Step 3: Open-Loop Optimal Control   
- Step 4: Riccati and Vector Equations   
- Step 5: Closed-Loop Optimal Control

Now the details follow.
