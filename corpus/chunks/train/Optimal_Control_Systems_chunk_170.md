# 3.2 Finite-Time Linear Quadratic Regulator

3. Optimal Control: From (3.2.21), we see that the optimal control $\mathbf{u}^{*}(t)$ is minimum (maximum) if the control weighted matrix $\mathbf{R}(t)$ is positive definite (negative definite).

4. Optimal State: Using the optimal control (3.2.12) in the state equation (3.2.1), we have

$$\boxed {\dot {\mathbf {x}} ^ {*} (t) = \left[ \mathbf {A} (t) - \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) \right] \mathbf {x} ^ {*} (t) = \mathbf {G} (t) \mathbf {x} ^ {*} (t)} \tag {3.2.42}$$

where

$$\mathbf {G} (t) = \mathbf {A} (t) - \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t). \tag {3.2.43}$$

The solution of this state differential equation along with the initial condition $\mathbf{x}(t_{0})$ gives the optimal state $\mathbf{x}^{*}(t)$ . Let us note that there is no condition on the closed-loop matrix $\mathbf{G}(t)$ regarding stability as long as we are considering the finite final time $(t_{f})$ system.

5. Optimal Cost: It is shown in (3.2.29) that the minimum cost $J^{*}$ is given by

$$J ^ {*} = \frac {1}{2} \mathbf {x} ^ {* \prime} (t) \mathbf {P} (t) \mathbf {x} ^ {*} (t) \quad \text { for all } \quad t \in [ t _ {0}, t _ {f} ] \tag {3.2.44}$$

where, $\mathbf{P}(t)$ is the solution of the matrix DRE (3.2.18), and $\mathbf{x}^{*}(t)$ is the solution of the closed-loop optimal system (3.2.42).

6. Definiteness of the Matrix $\mathbf{P}(t)$ : Since $\mathbf{F}(t_f)$ is positive semidefinite, and $\mathbf{P}(t_f) = \mathbf{F}(t_f)$ , we can easily say that $\mathbf{P}(t_f)$ is positive semidefinite. We can argue that $\mathbf{P}(t)$ is positive definite for all $t \in [t_0, t_f)$ . Suppose that $\mathbf{P}(t)$ is not positive definite for some $t = t_s < t_f$ , then there exists the corresponding state $\mathbf{x}^*(t_s)$ such that the cost function $\frac{1}{2}\mathbf{x}^{*\prime}(t_s)\mathbf{P}(t_s)\mathbf{x}^*(t_s) \leq 0$ , which clearly violates that fact that minimum cost has to be a positive quantity. Hence, $\mathbf{P}(t)$ is positive definite for all $t \in [t_0, t_f)$ . Since we already know that $\mathbf{P}(t)$ is symmetric, we now have that $\mathbf{P}(t)$ is positive definite, symmetric matrix.
