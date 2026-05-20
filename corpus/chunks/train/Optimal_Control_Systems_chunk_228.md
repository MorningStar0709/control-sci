# 4.3 Fixed-End-Point Regulator System

\- Step 3: State and Costate System: Obtain the state and costate equations as

$$\dot {\mathbf {x}} ^ {*} (t) = + \frac {\partial \mathcal {H}}{\partial \boldsymbol {\lambda}} \longrightarrow \dot {\mathbf {x}} ^ {*} (t) = \mathbf {A} (t) \mathbf {x} ^ {*} (t) + \mathbf {B} (t) \mathbf {u} ^ {*} (t), \tag {4.3.9}\dot {\pmb {\lambda}} ^ {*} (t) = - \frac {\partial \mathcal {H}}{\partial \mathbf {x}} \longrightarrow \dot {\pmb {\lambda}} ^ {*} (t) = - \mathbf {Q} (t) \mathbf {x} ^ {*} (t) - \mathbf {A} ^ {\prime} (t) \pmb {\lambda} ^ {*} (t). \quad (4. 3. 1 0)$$

Eliminating control $\mathbf{u}^{*}(t)$ from (4.3.8) and (4.3.9) to obtain the canonical system of equations

$$
\left[ \begin{array}{c} \dot {\mathbf {x}} ^ {*} (t) \\ \dot {\boldsymbol {\lambda}} ^ {*} (t) \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} (t) & - \mathbf {E} (t) \\ - \mathbf {Q} (t) & - \mathbf {A} ^ {\prime} (t) \end{array} \right] \left[ \begin{array}{c} \mathbf {x} ^ {*} (t) \\ \boldsymbol {\lambda} ^ {*} (t) \end{array} \right] \tag {4.3.11}
$$

where, $\mathbf{E}(t) = \mathbf{B}(t)\mathbf{R}^{-1}(t)\mathbf{B}'(t)$ . This state and costate system, along with the given boundary conditions (4.3.5), constitutes a two-point boundary value problem (TPBVP), which when solved gives optimal state $\mathbf{x}^{*}(t)$ and costate $\boldsymbol{\lambda}^{*}(t)$ functions. This optimal costate function $\boldsymbol{\lambda}^{*}(t)$ substituted in (4.3.8) gives optimal control $\mathbf{u}^{*}(t)$ . This leads us to open-loop optimal control as discussed in Chapter 2. But our interest here is to obtain closed-loop optimal control for the fixed-end-point regulator system.

\- Step 4: Closed-Loop Optimal Control: Now if this were a free-end-point system $(\mathbf{x}(t_f)$ free), using transversality conditions, we would be able to obtain a final condition on the costate $\lambda(t_f)$ , which lets us assume a Riccati transformation between the state and costate function as

$$\boldsymbol {\lambda} ^ {*} (t) = \mathbf {P} (t) \mathbf {x} ^ {*} (t). \tag {4.3.12}$$

In the absence of any knowledge on the final condition of the costate function $\boldsymbol{\lambda}^{*}(t)$ , we are led to assume a kind of inverse Riccati transformation as [104, 113]

$$\mathbf {x} ^ {*} (t) = \mathbf {M} (t) \boldsymbol {\lambda} ^ {*} (t) \tag {4.3.13}$$
