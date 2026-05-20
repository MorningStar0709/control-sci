# 6.5 LQR System Using H-J-B Equation

We employ the H-J-B equation to obtain the closed-loop optimal control of linear quadratic regulator system. Consider the plant described by

$$\dot {\mathbf {x}} (t) = \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t) \tag {6.5.1}$$

where, $\mathbf{x}(t)$ and $\mathbf{u}(t)$ are n and r dimensional state and control vectors respectively, and the performance index to be minimized as

$$
\begin{array}{l} J = \frac {1}{2} \mathbf {x} ^ {\prime} (t _ {f}) \mathbf {F x} (t _ {f}) \\ + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ \mathbf {x} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {x} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) \right] d t, \tag {6.5.2} \\ \end{array}
$$

where, as defined earlier, F, and $\mathbf{Q}(t)$ are real, symmetric, positive semidefinite matrices respectively, and $\mathbf{R}(t)$ is a real, symmetric, positive definite matrix. We will use the procedure given in Table 6.4.

\- Step 1: As a first step in optimization, let us form the Hamiltonian as

$$
\begin{array}{l} \mathcal {H} (\mathbf {x} (t), \mathbf {u} (t), J _ {\mathbf {x}} ^ {*}, t) = \frac {1}{2} \mathbf {x} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {x} (t) + \frac {1}{2} \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) \\ + J _ {\mathbf {x}} ^ {* \prime} (\mathbf {x} (t), t) [ \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t) ]. \tag {6.5.3} \\ \end{array}
$$

\- Step 2: A necessary condition for optimization of $\mathcal{H}$ w.r.t. $\mathbf{u}(t)$ is that

$$\frac {\partial \mathcal {H}}{\partial \mathbf {u}} = 0 \longrightarrow \mathbf {R} (t) \mathbf {u} (t) + \mathbf {B} ^ {\prime} (t) J _ {\mathbf {x}} ^ {* \prime} (\mathbf {x} (t), t) = 0, \tag {6.5.4}$$

which leads to

$$\mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) J _ {\mathbf {x}} ^ {*} (\mathbf {x} (t), t). \tag {6.5.5}$$

Let us note that for the minimum control, the sufficient condition that

$$\frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {u} ^ {2}} = \mathbf {R} (t) \tag {6.5.6}$$

is positive definite, is satisfied due to our assumption that $\mathbf{R}(t)$ is symmetric positive definite.

\- Step 3: With optimal control (6.5.5) in the Hamiltonian (6.5.3)
