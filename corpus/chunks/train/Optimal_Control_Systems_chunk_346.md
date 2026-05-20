# 6.3.3 Optimal Control of Discrete-Time Systems

Here, we try to derive the optimal feedback control of a discrete-time system using the principle of optimality of dynamic programming $[79, 89]$ . Consider a linear, time-invariant, discrete-time plant,

$$\mathbf {x} (k + 1) = \mathbf {A x} (k) + \mathbf {B u} (k) \tag {6.3.15}$$

and the associated performance index

$$
\begin{array}{l} J _ {i} = \frac {1}{2} \mathbf {x} ^ {\prime} (k _ {f}) \mathbf {F x} (k _ {f}) \\ + \frac {1}{2} \sum_ {i} ^ {k _ {f} - 1} \left[ \mathbf {x} ^ {\prime} (k) \mathbf {Q x} (k) + \mathbf {u} ^ {\prime} (k) \mathbf {R u} (k) \right] \tag {6.3.16} \\ \end{array}
$$

where, $\mathbf{x}(k)$ and $\mathbf{u}(k)$ are n and r dimensional state and control vectors, and $\mathbf{A}(\mathbf{k})$ and $\mathbf{B}(\mathbf{k})$ are matrices of nxn and nxr dimensions, respectively. Further, F and Q are each nxn order symmetric, positive semidefinite matrices, and R is rxr symmetric, positive definite matrix. For our present discussion, let us assume that there are no constraints on the state or control.

The problem is to find the optimal control $\mathbf{u}^{*}(k)$ for $i \leq k \leq k_{f}$ that minimizes the performance index $J_{k}$ using the principle of optimality. Let us assume further that the initial state $\mathbf{x}(k_{0})$ is fixed and the final state $\mathbf{x}(k_{f})$ is free. In using dynamic programming, we start with the final stage $\mathbf{x}(k_{f})$ and work backwards. At each stage, we find the optimal control and state. Let us start with last stage $k = k_{f}$ .

Last Stage: $k = k_{f}$

Let us first note that at $i = k_{f}$ ,
