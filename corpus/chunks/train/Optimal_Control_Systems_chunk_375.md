# 7.1 Constrained Optimal Control

\- Step 1: Performance Index: For the minimum-time system formulation specified by (7.1.10) and by the control constraint relation (7.1.14), the performance index (PI) becomes

$$J (\mathbf {u} (t)) = \int_ {t _ {0}} ^ {t _ {f}} V [ \mathbf {x} (t), \mathbf {u} (t), t ] d t = \int_ {t _ {0}} ^ {t _ {f}} 1 d t = t _ {f} - t _ {0} \tag {7.1.16}$$

where, $t_{0}$ is fixed and $t_{f}$ is free. If the final time $t_{f}$ is fixed, trying to minimize a fixed quantity makes no sense.

\- Step 2: Hamiltonian: We form the Hamiltonian $\mathcal{H}$ for the problem described by the system (7.1.10) and the PI (7.1.16) as

$$
\begin{array}{l} \mathcal {H} (\mathbf {x} (t), \boldsymbol {\lambda} (t), \mathbf {u} (t)) = 1 + \boldsymbol {\lambda} ^ {\prime} (t) [ \mathbf {A x} (t) + \mathbf {B u} (t) ], \\ = 1 + \left[ \mathbf {A} \mathbf {x} (t) \right] ^ {\prime} \boldsymbol {\lambda} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {B} ^ {\prime} \boldsymbol {\lambda} (t) \tag {7.1.17} \\ \end{array}
$$

where, $\lambda(t)$ is the costate variable.

\- Step 3: State and Costate Equations: Let us assume the optimal values $\mathbf{u}^{*}(t)$ , $\mathbf{x}^{*}(t)$ , and $\boldsymbol{\lambda}^{*}(t)$ . Then, the state $\mathbf{x}^{*}(t)$ and the costate $\boldsymbol{\lambda}^{*}(t)$ are given by

$$\dot {\mathbf {x}} ^ {*} (t) = + \left(\frac {\partial \mathcal {H}}{\partial \boldsymbol {\lambda}}\right) _ {*} = \mathbf {A} \mathbf {x} ^ {*} (t) + \mathbf {B} \mathbf {u} ^ {*} (t), \tag {7.1.18}\dot {\boldsymbol {\lambda}} ^ {*} (t) = - \left(\frac {\partial \mathcal {H}}{\partial \mathbf {x}}\right) _ {*} = - \mathbf {A} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) \tag {7.1.19}$$

with the boundary conditions

$$\mathbf {x} ^ {*} (t _ {0}) = \mathbf {x} (t _ {0}); \quad \mathbf {x} ^ {*} (t _ {f}) = \mathbf {0} \tag {7.1.20}$$

where, we again note that $t_f$ is free.

\- Step 4: Optimal Condition: Now using Pontryagin Principle, we invoke the condition (7.1.6) for optimal control in terms of the Hamiltonian. Using (7.1.17) in (7.1.6), we have
