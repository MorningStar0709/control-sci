# 3.3 Analytical Solution to the Matrix Differential Riccati Equation

In this section, we explore an analytical solution for the matric differential Riccati equation (DRE). This material is based on $[138, 89]$ . Let us rewrite the Hamiltonian system $(3.2.8)$ of the state and costate equations for the time-invariant case as (omitting \* for the sake of simplicity)

$$
\left[ \begin{array}{c} \dot {\mathbf {x}} (t) \\ \dot {\boldsymbol {\lambda}} (t) \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} & - \mathbf {E} \\ - \mathbf {Q} & - \mathbf {A} ^ {\prime} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} (t) \\ \boldsymbol {\lambda} (t) \end{array} \right] \tag {3.3.1}
$$

where, $\mathbf{E} = \mathbf{B}\mathbf{R}^{-1}\mathbf{B}'$ . Let

$$
\Delta = \left[ \begin{array}{c c} {\mathbf {A}} & {- \mathbf {E}} \\ {- \mathbf {Q}} & {- \mathbf {A} ^ {\prime}} \end{array} \right]. \tag {3.3.2}
$$

Let us also recall that by the transformation $\boldsymbol{\lambda}(t)=\mathbf{P}(t)\mathbf{x}(t)$ , we get the differential matrix Riccati equation (3.2.18), rewritten for (time-invariant matrices A, B, Q and R) as

$$\dot {\mathbf {P}} (t) = - \mathbf {P} (t) \mathbf {A} - \mathbf {A} ^ {\prime} \mathbf {P} (t) - \mathbf {Q} + \mathbf {P} (t) \mathbf {B} \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \mathbf {P} (t), \tag {3.3.3}$$

with the final condition

$$\mathbf {P} (t _ {f}) = \mathbf {F} (t _ {f}). \tag {3.3.4}$$

The solution $\mathbf{P}(t)$ can be obtained analytically (in contrast to numerical integration) in terms of the eigenvalues and eigenvectors of the Hamiltonian matrix $\Delta$ . In order to find analytical solution to the differential Riccati equation (3.3.3), it is necessary to show that if $\mu$ is an eigenvalue of the Hamiltonian matrix $\Delta$ in (3.3.2), then it implies that $-\mu$ is also the eigenvalue of $\Delta$ [89, 3]. For this, let us define

$$
\Gamma = \left[ \begin{array}{c c} \mathbf {0} & \mathbf {I} \\ - \mathbf {I} & \mathbf {0} \end{array} \right] \tag {3.3.5}
$$

so that $\Gamma^{-1} = -\Gamma$ . Then by a simple pre- and post-multiplication with $\Gamma$ we get

$$\Delta = \Gamma \Delta^ {\prime} \Gamma = - \Gamma \Delta^ {\prime} \Gamma^ {- 1}. \tag {3.3.6}$$

Now, if $\mu$ is an eigenvalue of $\Delta$ with corresponding eigenvector $\mathbf{v}$ ,

$$\Delta \mathbf {v} = \mu \mathbf {v} \tag {3.3.7}$$

then
