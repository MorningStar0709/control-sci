# 4.1.2 Salient Features of Tracking System

1. Riccati Coefficient Matrix $\mathbf{P}(t)$ : We note that the desired output $\mathbf{z}(t)$ has no influence on the matrix differential Riccati equation (4.1.32) and its boundary condition (4.1.33). This means that once the problem is specified in terms of the final time $t_{f}$ , the plant matrices $\mathbf{A}(t)$ , $\mathbf{B}(t)$ , and $\mathbf{C}(t)$ , and the cost functional matrices $\mathbf{F}(t_{f})$ , $\mathbf{Q}(t)$ , and $\mathbf{R}(t)$ , the matrix function $\mathbf{P}(t)$ is completely determined.

Table 4.1 Procedure Summary of Linear Quadratic Tracking System

<table><tr><td colspan="2">A.
Statement of the Problem</td></tr><tr><td colspan="2">Given the plant as $\dot{\mathbf{x}}(t) = \mathbf{A}(t)\mathbf{x}(t) + \mathbf{B}(t)\mathbf{u}(t), \quad \mathbf{y}(t) = \mathbf{C}(t)\mathbf{x}(t), \quad \mathbf{e}(t) = \mathbf{z}(t) - \mathbf{y}(t),$ the performance index as $J = \frac{1}{2}\mathbf{e}'(t_f)\mathbf{F}(t_f)\mathbf{e}(t_f) + \frac{1}{2} \int_{t_0}^{t_f} [\mathbf{e}'(t)\mathbf{Q}(t)\mathbf{e}(t) + \mathbf{u}'(t)\mathbf{R}(t)\mathbf{u}(t)] dt,$ and the boundary conditions as $\mathbf{x}(t_0) = \mathbf{x}_0, \quad \mathbf{x}(t_f)$  is free,find the optimal control, state and performance index.</td></tr><tr><td colspan="2">B.
