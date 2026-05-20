# Example 3.2

Given a second order plant

$$\dot {x} _ {1} (t) = x _ {2} (t), \quad x _ {1} (0) = 2\dot {x} _ {2} (t) = - 2 x _ {1} (t) + x _ {2} (t) + u (t), \quad x _ {2} (0) = - 3 \tag {3.5.18}$$

and the performance index

$$J = \frac {1}{2} \int_ {0} ^ {\infty} \left[ 2 x _ {1} ^ {2} (t) + 6 x _ {1} (t) x _ {2} (t) + 5 x _ {2} ^ {2} (t) + 0. 2 5 u ^ {2} (t) \right] d t, \tag {3.5.19}$$

obtain the feedback optimal control law.

Solution: Comparing the plant (3.5.18) and PI (3.5.19) of the present system with the corresponding general formulation of plant (3.5.12) and PI (3.5.13), respectively, let us first identify the various

Table 3.3 Procedure Summary of Infinite-Interval Linear Quadratic Regulator System: Time-Invariant Case

<table><tr><td colspan="2">A. Statement of the Problem</td></tr><tr><td colspan="2">Given the plant as $\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t),$ the performance index as $J = \frac{1}{2} \int_{0}^{\infty} [\mathbf{x}'(t)\mathbf{Q}\mathbf{x}(t) + \mathbf{u}'(t)\mathbf{R}\mathbf{u}(t)] dt,$ and the boundary conditions as $\mathbf{x}(t_0) = \mathbf{x}_0; \quad \mathbf{x}(\infty) = 0,$ find the optimal control, state and index.</td></tr><tr><td colspan="2">B. Solution of the Problem</td></tr><tr><td>Step 1</td><td>Solve the matrix algebraic Riccati equation (ARE) $-\bar{\mathbf{P}}\mathbf{A} - \mathbf{A}'\bar{\mathbf{P}} - \mathbf{Q} + \bar{\mathbf{P}}\mathbf{B}\mathbf{R}^{-1}\mathbf{B}'\bar{\mathbf{P}} = 0..$ </td></tr><tr><td>Step 2</td><td>Solve the optimal state  $\mathbf{x}^{*}(t)$  from $\dot{\mathbf{x}}^{*}(t) = [\mathbf{A} - \mathbf{B}\mathbf{R}^{-1}\mathbf{B}'\bar{\mathbf{P}}] \mathbf{x}^{*}(t)$ with initial condition  $\mathbf{x}(t_0) = \mathbf{x}_0.$ </td></tr><tr><td>Step 3</td><td>Obtain the optimal control  $\mathbf{u}^{*}(t)$  from $\mathbf{u}^{*}(t) = -\mathbf{R}^{-1}\mathbf{B}'\bar{\mathbf{P}}\mathbf{x}^{*}(t).$ </td></tr><tr><td>Step 4</td><td>Obtain the optimal performance index from $J^{*} = \frac{1}{2}\mathbf{x}^{*\prime}(t)\bar{\mathbf{P}}\mathbf{x}^{*}(t).$ </td></tr></table>

matrices as

$$
\mathbf {A} = \left[ \begin{array}{l l} 0 & 1 \\ - 2 & 1 \end{array} \right]; \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right]; \tag {3.5.20}
