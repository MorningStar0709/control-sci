# 3.4.1 Infinite-Time Linear Quadratic Regulator: Time-Varying Case: Summary

Consider a linear, time-varying plant

$$\dot {\mathbf {x}} (t) = \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t), \tag {3.4.8}$$

and a quadratic performance index

$$J = \frac {1}{2} \int_ {t _ {0}} ^ {\infty} \left[ \mathbf {x} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {x} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) \right] d t, \tag {3.4.9}$$

where, $\mathbf{u}(t)$ is not constrained and $\mathbf{x}(t_f), t_f \to \infty$ is not specified. Also, $\mathbf{Q}(t)$ is $n \times n$ symmetric, positive semidefinite matrix, and $\mathbf{R}(t)$ is $r \times r$ symmetric, positive definite matrix. Then, the optimal control is given by

$$\mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \hat {\mathbf {P}} (t) \mathbf {x} ^ {*} (t) \tag {3.4.10}$$

where, $\hat{\mathbf{P}}(t)$ , the $nxn$ symmetric, positive definite matrix (for all $t \in [t_0, t_f]$ , is the solution of the matrix differential Riccati equation (DRE)

$$\frac {\dot {\hat {\mathbf {P}}} (t) = - \hat {\mathbf {P}} (t) \mathbf {A} (t) - \mathbf {A} ^ {\prime} (t) \hat {\mathbf {P}} (t) - \mathbf {Q} (t) + \hat {\mathbf {P}} (t) \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \hat {\mathbf {P}} (t)}{(3 . 4 . 1 1)}$$

satisfying the final condition

$$\hat {\mathbf {P}} (t = t _ {f} \rightarrow \infty) = 0. \tag {3.4.12}$$

Table 3.2 Procedure Summary of Infinite-Time Linear Quadratic Regulator System: Time-Varying Case
