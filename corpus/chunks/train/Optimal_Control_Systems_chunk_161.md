# 3.2.2 Optimal Control

Is the optimal control $\mathbf{u}^{*}(t)$ a minimum? This can be answered by considering the second partials of the Hamiltonian (3.2.3). Let us recall from Chapter 2 that this is done by examining the second variation of the cost functional. Thus, the condition (2.7.41) (reproduced here for convenience) for examining the nature of optimal control is that the matrix

$$
\Pi = \left[ \begin{array}{c c} \frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {x} ^ {2}} & \frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {x} \partial \mathbf {u}} \\ \frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {u} \partial \mathbf {x}} & \frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {u} ^ {2}} \end{array} \right] _ {*} \tag {3.2.20}
$$

must be positive definite (negative definite) for minimum (maximum). In most of the cases this reduces to the condition that

$$\left(\frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {u} ^ {2}}\right) _ {*} \tag {3.2.21}$$

must be positive definite (negative definite) for minimum (maximum). Now using the Hamiltonian (3.2.3) and calculating the various partials,

$$\left(\frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {x} ^ {2}}\right) _ {*} = \mathbf {Q} (t), \quad \left(\frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {x} \partial \mathbf {u}}\right) _ {*} = 0,\left(\frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {u} \partial \mathbf {x}}\right) _ {*} = 0, \quad \left(\frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {u} ^ {2}}\right) _ {*} = \mathbf {R} (t). \tag {3.2.22}$$

Substituting the previous partials in the condition (3.2.20), we have

$$
\Pi = \left[ \begin{array}{c c} \mathbf {Q} (t) & 0 \\ 0 & \mathbf {R} (t) \end{array} \right]. \tag {3.2.23}
$$

Since $\mathbf{R}(t)$ is positive definite, and $\mathbf{Q}(t)$ is positive semidefinite, it follows that the preceding matrix (3.2.23) is only positive semidefinite. However, the condition that the second partial of H w.r.t. $\mathbf{u}^{*}(t)$ , which is $\mathbf{R}(t)$ , is positive definite, is enough to guarantee that the control $\mathbf{u}^{*}(t)$ is minimum.
