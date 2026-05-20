# 7.1.2 Problem Formulation and Statement

Let us now present a typical time-optimal control (TOC) system. Consider a linear, time-invariant dynamical system

$$\dot {\mathbf {x}} (t) = \mathbf {A} \mathbf {x} (t) + \mathbf {B} \mathbf {u} (t) \tag {7.1.10}$$

where, $\mathbf{x}(t)$ is nth state vector; $\mathbf{u}(t)$ is rth control vector, and the matrices A and B are constant matrices of nxn and nxr dimensions, respectively. We are also given that

1. the system (7.1.10) is completely controllable, that is, the matrix

$$
\mathbf {G} = \left[ \begin{array}{c c c c c c c} \mathbf {B} & \vdots & \mathbf {A B} & \vdots & \mathbf {A} ^ {2} \mathbf {B} & \vdots & \dots & \vdots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right] \tag {7.1.11}
$$

is of rank $n$ or the matrix $\mathbf{G}$ is nonsingular, and

2. the magnitude of the control $\mathbf{u}(t)$ is constrained as

$$U ^ {-} \leq \mathbf {u} (t) \leq U ^ {+} \quad \longrightarrow \quad | \mathbf {u} (t) | \leq \mathbf {U} \tag {7.1.12}$$

or component wise

$$\left| u _ {j} (t) \right| \leq U _ {j}, \quad j = 1, 2, \dots , r. \tag {7.1.13}$$

Here, $U^{+}$ and $U^{-}$ are the upper and lower bounds of U. But, the constraint relation (7.1.12) can also be written more conveniently (by absorbing the magnitude U into the matrix B) as

$$- 1 \leq \mathbf {u} (t) \leq + 1 \quad \longrightarrow \quad | \mathbf {u} (t) | \leq 1 \tag {7.1.14}$$

or component wise,

$$\left| u _ {j} (t) \right| \leq 1, \tag {7.1.15}$$

3. the initial state is $\mathbf{x}(t_{0})$ and the final (target) state is 0.

The problem statement is: Find the (optimal) control $\mathbf{u}^{*}(t)$ which satisfies the constraint (7.1.15) and drives the system (7.1.10) from the initial state $\mathbf{x}(t_{0})$ to the origin 0 in minimum time.
