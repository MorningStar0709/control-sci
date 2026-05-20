<table><tr><td colspan="2">A. Statement of the Problem</td></tr><tr><td colspan="2">Given the plant as $\dot{\mathbf{x}}(t) = \mathbf{A}(t)\mathbf{x}(t) + \mathbf{B}(t)\mathbf{u}(t),$ the performance index as $J = \frac{1}{2} \int_{t_0}^{\infty} [\mathbf{x}'(t)\mathbf{Q}(t)\mathbf{x}(t) + \mathbf{u}'(t)\mathbf{R}(t)\mathbf{u}(t)] dt,$ and the boundary conditions as $\mathbf{x}(t_0) = \mathbf{x}_0; \quad \mathbf{x}(\infty)$  is free,find the optimal control, state and performance index.</td></tr><tr><td colspan="2">B. Solution of the Problem</td></tr><tr><td>Step 1</td><td>Solve the matrix differential Riccati equation (DRE) $\dot{\hat{\mathbf{P}}} (t) = -\hat{\mathbf{P}}(t)\mathbf{A}(t) - \mathbf{A}'(t)\hat{\mathbf{P}}(t) - \mathbf{Q}(t) + \hat{\mathbf{P}}(t)\mathbf{B}(t)\mathbf{R}^{-1}(t)\mathbf{B}'(t)\hat{\mathbf{P}}(t)$ with final condition  $\hat{\mathbf{P}}(t = t_f) = 0$ .</td></tr><tr><td>Step 2</td><td>Solve the optimal state  $\mathbf{x}^{*}(t)$  from $\mathbf{x}^{*}(t) = \left[ \mathbf{A}(t) - \mathbf{B}(t)\mathbf{R}^{-1}(t)\mathbf{B}'(t)\hat{\mathbf{P}}(t) \right] \mathbf{x}^{*}(t)$ with initial condition  $\mathbf{x}(t_0) = \mathbf{x}_0$ .</td></tr><tr><td>Step 3</td><td>Obtain the optimal control  $\mathbf{u}^{*}(t)$  from $\mathbf{u}^{*}(t) = -\mathbf{R}^{-1}(t)\mathbf{B}'(t)\hat{\mathbf{P}}(t)\mathbf{x}^{*}(t)$ .</td></tr><tr><td>Step 4</td><td>Obtain the optimal performance index from $J^{*} = \frac{1}{2}\mathbf{x}^{*\prime}(t)\hat{\mathbf{P}}(t)\mathbf{x}^{*}(t)$ .</td></tr></table>

The optimal state is the solution of

$$\boxed {\dot {\mathbf {x}} ^ {*} (t) = \left[ \mathbf {A} (t) - \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \hat {\mathbf {P}} (t) \right] \mathbf {x} ^ {*} (t)} \tag {3.4.13}$$

and the optimal cost is

$$\boxed {J ^ {*} = \frac {1}{2} \mathbf {x} ^ {* \prime} (t) \hat {\mathbf {P}} (t) \mathbf {x} ^ {*} (t).} \tag {3.4.14}$$

The optimal control $\mathbf{u}^{*}(t)$ given by (3.4.10) is linear in the optimal state $\mathbf{x}^{*}(t)$ . The entire procedure is now summarized in Table 3.2.
