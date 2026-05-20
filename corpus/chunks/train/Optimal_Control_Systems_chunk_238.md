# Example 4.4

Consider a first-order system

$$\dot {x} (t) = - x (t) + u (t), \quad x (0) = 1 \tag {4.4.17}$$

and a performance measure

$$J = \frac {1}{2} \int_ {0} ^ {\infty} e ^ {2 \alpha t} [ x ^ {2} (t) + u ^ {2} (t) ] d t. \tag {4.4.18}$$

Find the optimal control law and show that the closed-loop optimal system has a degree of stability of at least $\alpha$ .

Table 4.2 Procedure Summary of Regulator System with Prescribed Degree of Stability

<table><tr><td colspan="2">A. Statement of the Problem</td></tr><tr><td colspan="2">Given the plant as $\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t),$ the performance index as $J = \frac{1}{2} \int_{t_0}^{\infty} e^{2\alpha t} [\mathbf{x}'(t)\mathbf{Q}\mathbf{x}(t) + \mathbf{u}'(t)\mathbf{R}\mathbf{u}(t)] dt,$ and the boundary conditions as $\mathbf{x}(t_0) = \mathbf{x}_0; \quad \mathbf{x}(\infty) = 0,$ find the optimal control, state and index.</td></tr><tr><td colspan="2">B. Solution of the Problem</td></tr><tr><td>Step 1</td><td>Solve the matrix algebraic Riccati equation $\bar{\mathbf{P}}(\mathbf{A} + \alpha\mathbf{I}) + (\mathbf{A}' + \alpha\mathbf{I})\bar{\mathbf{P}} + \mathbf{Q} - \bar{\mathbf{P}}\mathbf{B}\mathbf{R}^{-1}\mathbf{B}'\bar{\mathbf{P}} = 0.$ </td></tr><tr><td>Step 2</td><td>Solve the optimal state  $\mathbf{x}^*(t)$  from $\dot{\mathbf{x}}^*(t) = (\mathbf{A} - \mathbf{B}\mathbf{R}^{-1}\mathbf{B}'\bar{\mathbf{P}}) \mathbf{x}^*(t)$ with initial condition  $\mathbf{x}(t_0) = \mathbf{x}_0.$ </td></tr><tr><td>Step 3</td><td>Obtain the optimal control  $\mathbf{u}^*(t)$  from $\mathbf{u}^*(t) = -\mathbf{R}^{-1}\mathbf{B}'\bar{\mathbf{P}}\mathbf{x}^*(t).$ </td></tr><tr><td>Step 4</td><td>Obtain the optimal performance index from $J^* = \frac{1}{2}e^{2\alpha t_0}\mathbf{x}^{*\prime}(t_0)\bar{\mathbf{P}}\mathbf{x}^*(t_0).$ </td></tr></table>

Solution: Essentially, we show that the eigenvalue of this closed-loop optimal system is less than or equal to $-\alpha$ . First of all, in the above, we note that A = a = -1, B = b = 1, Q = q = 1 and R = r = 1. Then, the algebraic Riccati equation (4.4.14) becomes

$$2 \bar {p} (\alpha - 1) - \bar {p} ^ {2} + 1 = 0 \quad \longrightarrow \bar {p} ^ {2} - 2 \bar {p} (\alpha - 1) - 1. \tag {4.4.19}$$

Solving the previous for positive value of $\bar{p}$ , we have

$$\bar {p} = - 1 + \alpha + \sqrt {(\alpha - 1) ^ {2} + 1}. \tag {4.4.20}$$

The optimal control (4.4.15) becomes

$$u ^ {*} (t) = - \bar {p} x ^ {*} (t). \tag {4.4.21}$$

The optimal system (4.4.22) becomes

$$\dot {x} ^ {*} (t) = \left(- \alpha - \sqrt {(\alpha - 1) ^ {2} + 1}\right) x ^ {*} (t). \tag {4.4.22}$$
