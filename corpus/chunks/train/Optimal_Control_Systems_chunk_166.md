# 3.2.4 Finite-Time Linear Quadratic Regulator: Time-Varying Case: Summary

Given a linear, time-varying plant

$$\dot {\mathbf {x}} (t) = \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t) \tag {3.2.31}$$

and a quadratic performance index

$$
\begin{array}{l} J = \frac {1}{2} \mathbf {x} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {x} (t _ {f}) \\ + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ \mathbf {x} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {x} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) \right] d t \tag {3.2.32} \\ \end{array}
$$

where, $\mathbf{u}(t)$ is not constrained, $t_{f}$ is specified, and $\mathbf{x}(t_{f})$ is not specified, $\mathbf{F}(t_{f})$ and $\mathbf{Q}(t)$ are nxn symmetric, positive semidefinite matrices, and $\mathbf{R}(t)$ is rxr symmetric, positive definite matrix, the optimal control is given by

$$\mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) \mathbf {x} ^ {*} (t) = - \mathbf {K} (t) \mathbf {x} ^ {*} (t) \tag {3.2.33}$$

where $\mathbf{K}(t)=\mathbf{R}^{-1}(t)\mathbf{B}^{\prime}(t)\mathbf{P}(t)$ is called Kalman gain and $\mathbf{P}(t)$ , the nxn symmetric, positive definite matrix (for all $t\in[t_{0},t_{f}]$ ), is the solution of the matrix differential Riccati equation (DRE)

$$\dot {\mathbf {P}} (t) = - \mathbf {P} (t) \mathbf {A} (t) - \mathbf {A} ^ {\prime} (t) \mathbf {P} (t) - \mathbf {Q} (t) + \mathbf {P} (t) \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) \tag {3.2.34}$$

satisfying the final condition

$$\mathbf {P} (t = t _ {f}) = \mathbf {F} (t _ {f}) \tag {3.2.35}$$

Table 3.1 Procedure Summary of Finite-Time Linear Quadratic Regulator System: Time-Varying Case
