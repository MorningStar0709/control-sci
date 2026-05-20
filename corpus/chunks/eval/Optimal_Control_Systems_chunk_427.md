# 7.6.1 Penalty Function Method

Let us consider the system as

$$\dot {\mathbf {x}} (t) = \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t) \tag {7.6.1}$$

and the performance index as

$$J = \int_ {t _ {0}} ^ {t _ {f}} V (\mathbf {x} (t), \mathbf {u} (t), t) \tag {7.6.2}$$

where, $\mathbf{x}(t)$ and $\mathbf{u}(t)$ are n and r dimensional state and control vectors, respectively. Let the inequality constraints on the states be expressed as

$$\mathbf {g} (\mathbf {x} (t), t) \geq \mathbf {0} \tag {7.6.3}$$

or

$$g _ {1} (x _ {1} (t), x _ {2} (t), \dots , x _ {n} (t), t) \geq 0g _ {2} \left(x _ {1} (t), x _ {2} (t), \dots , x _ {n} (t), t\right) \geq 0$$

• • • • • • • • • • • • • • • • •

$$g _ {p} (x _ {1} (t), x _ {2} (t), \dots , x _ {n} (t), t) \geq 0 \tag {7.6.4}$$

where, g is a $p \leq n$ vector function of the states and assumed to have continuous first and second partial derivatives with respect to state $\mathbf{x}(t)$ . There are several methods of solving this system where the inequality constraints (7.6.3) are converted to equality constraints. One such methodology is described below. Let us define a new variable $x_{n+1}(t)$ by

$$
\begin{array}{l} \dot {x} _ {n + 1} (t) \cong f _ {n + 1} (\mathbf {x} (t), t), \\ = \left[ g _ {1} (\mathbf {x} (t), t) \right] ^ {2} H \left(g _ {1}\right) + \left[ g _ {2} (\mathbf {x} (t), t) \right] ^ {2} H \left(g _ {2}\right) + \dots \\ + \left[ g _ {p} (\mathbf {x} (t), t) \right] H \left(g _ {p}\right), \tag {7.6.5} \\ \end{array}
$$

where, $H(g_{i})$ is a unit Heaviside step function defined by

$$
H (g _ {i}) = \left\{ \begin{array}{l l} 0, & \text { if } g _ {i} (\mathbf {x} (t), t) \geq 0, \\ 1, & \text { if } g _ {i} (\mathbf {x} (t), t) <   0, \end{array} \right. \tag {7.6.6}
$$

for $i = 1,2,\ldots ,p$ . The relations (7.6.6) and (7.6.5) mean that $\dot{x}_{n + 1}(t) = 0$ for all $t$ when the constraint relation (7.6.3) is satisfied and $\dot{x}_{n + 1}(t)\geq 0$ for all $t$ due to the square terms in (7.6.5). Further, let us require that the new variable $x_{n + 1}(t)$ has the boundary conditions

$$x _ {n + 1} (t _ {0}) = 0, \quad \text { and } \quad x _ {n + 1} (t _ {f}) = 0 \tag {7.6.7}$$

such that

$$
\begin{array}{l} x _ {n + 1} (t) = \int_ {t _ {0}} ^ {t} \dot {x} _ {n + 1} (t) d t \\ = \int_ {t _ {0}} ^ {t} \left\{\left[ g _ {1} (\mathbf {x} (t), t ] ^ {2} H (g _ {1}) + \left[ g _ {2} (\mathbf {x} (t), t) \right] ^ {2} H (g _ {2}) + \dots \right. \right. \\ \left. + \left[ g _ {p} (\mathbf {x} (t), t) \right] ^ {2} H \left(g _ {p}\right) \right\} d t. \tag {7.6.8} \\ \end{array}
$$
