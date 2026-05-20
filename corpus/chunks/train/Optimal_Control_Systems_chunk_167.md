<table><tr><td colspan="2">A. Statement of the Problem</td></tr><tr><td colspan="2">Given the plant as $\dot{\mathbf{x}}(t) = \mathbf{A}(t)\mathbf{x}(t) + \mathbf{B}(t)\mathbf{u}(t),$ the performance index as $J = \frac{1}{2}\mathbf{x}'(t_f)\mathbf{F}(t_f)\mathbf{x}(t_f) + \frac{1}{2} \int_{t_0}^{t_f} [\mathbf{x}'(t)\mathbf{Q}(t)\mathbf{x}(t) + \mathbf{u}'(t)\mathbf{R}(t)\mathbf{u}(t)] dt,$ and the boundary conditions as $\mathbf{x}(t_0) = \mathbf{x}_0, \quad t_f$  is fixed, and  $\mathbf{x}(t_f)$  is free,find the optimal control, state and performance index.</td></tr><tr><td colspan="2">B. Solution of the Problem</td></tr><tr><td>Step 1</td><td>Solve the matrix differential Riccati equation $\dot{\mathbf{P}}(t) = -\mathbf{P}(t)\mathbf{A}(t) - \mathbf{A}'(t)\mathbf{P}(t) - \mathbf{Q}(t) + \mathbf{P}(t)\mathbf{B}(t)\mathbf{R}^{-1}(t)\mathbf{B}'(t)\mathbf{P}(t)$ with final condition  $\mathbf{P}(t = t_f) = \mathbf{F}(t_f).$ </td></tr><tr><td>Step 2</td><td>Solve the optimal state  $\mathbf{x}^*(t)$  from $\dot{\mathbf{x}}^*(t) = [\mathbf{A}(t) - \mathbf{B}(t)\mathbf{R}^{-1}(t)\mathbf{B}'(t)\mathbf{P}(t)] \mathbf{x}^*(t)$ with initial condition  $\mathbf{x}(t_0) = \mathbf{x}_0.$ </td></tr><tr><td>Step 3</td><td>Obtain the optimal control  $\mathbf{u}^*(t)$  as $\mathbf{u}^*(t) = -\mathbf{K}(t)\mathbf{x}^*(t)$  where,  $\mathbf{K}(t) = \mathbf{R}^{-1}(t)\mathbf{B}'(t)\mathbf{P}(t).$ </td></tr><tr><td>Step 4</td><td>Obtain the optimal performance index from $J^* = \frac{1}{2}\mathbf{x}^{*\prime}(t)\mathbf{P}(t)\mathbf{x}^*(t).$ </td></tr></table>

the optimal state is the solution of

$$\boxed {\dot {\mathbf {x}} ^ {*} (t) = \left[ \mathbf {A} (t) - \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) \right] \mathbf {x} ^ {*} (t)} \tag {3.2.36}$$

and the optimal cost is

$$\boxed {J ^ {*} = \frac {1}{2} \mathbf {x} ^ {* \prime} (t) \mathbf {P} (t) \mathbf {x} ^ {*} (t).} \tag {3.2.37}$$

The optimal control $\mathbf{u}^{*}(t)$ , given by (3.2.33), is linear in the optimal state $\mathbf{x}^{*}(t)$ . The entire procedure is now summarized in Table 3.1.

Note: It is simple to see that one can absorb the $\frac{1}{2}$ that is associated with J by redefining a performance measure as
