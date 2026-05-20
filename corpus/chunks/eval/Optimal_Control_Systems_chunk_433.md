# 7.6.2 Slack Variable Method

The slack variable approach [68, 137], often known as Valentine's method, transforms the given inequality state (path) constraint into an equality state (path) constraint by introducing a slack variable. For the sake of completeness, let us restate the state constraint problem.

Consider the optimal control system

$$\dot {\mathbf {x}} (t) = \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t), \quad \mathbf {x} (t = t _ {o}) = \mathbf {x} _ {o} \tag {7.6.32}$$

which minimizes the performance index

$$\mathbf {J} = F (\mathbf {x} (t _ {f}), t _ {f}) + \int_ {t _ {o}} ^ {t _ {f}} V (\mathbf {x} (t), \mathbf {u} (t), t) d t \tag {7.6.33}$$

subject to the state-variable inequality constraint

$$S (\mathbf {x} (t), t) \leq 0. \tag {7.6.34}$$

Here, $\mathbf{x}(t)$ is an n-dimensional order state vector, $\mathbf{u}(t)$ is an r-dimensional control vector and the constraint S is of pth order in the sense that the pth derivative of S contains the control $\mathbf{u}(t)$ explicitly.

The state-constrained, optimal control problem is solved by converting the given inequality constrained problem into an equality constrained one by introducing a “slack variable,” as [68, 137]

$$S (\mathbf {x} (t), t) + \frac {1}{2} \alpha^ {2} (t) = 0. \tag {7.6.35}$$

Differentiating (7.6.35) $p$ times with respect to time $t$ , we obtain

$$
\begin{array}{l} S _ {1} (\mathbf {x} (t), t) + \alpha \alpha_ {1} = 0 \\ S _ {2} (\mathbf {x} (t), t) + \alpha_ {1} ^ {2} + \alpha \alpha_ {2} = 0 \\ \dots \\ S _ {p} (\mathbf {x} (t), \underline {{\mathrm{u}}} (t), t) + \{\text { terms   involving } \alpha (t), \alpha_ {1}) (t), \dots , \alpha_ {p} (t) \} = 0 \tag {7.6.36} \\ \end{array}
$$

where, the subscripts on S and $\alpha$ denote the time derivatives, that is,

$$S _ {1} = \frac {d S}{d t} = \left(\frac {\partial S}{\partial \mathbf {x}}\right) \left(\frac {d \mathbf {x}}{d t}\right) + \frac {\partial S}{\partial t} \text { and } \alpha_ {1} = \frac {d \alpha}{d t}. \tag {7.6.37}$$

Since the control $\mathbf{u}(t)$ is explicitly present in the $p$ th derivative equation, we can solve for the control to obtain

$$\mathbf {u} (t) = g (\mathbf {x} (t), \alpha (t), \alpha_ {1}) (t),..., \alpha_ {p} (t), t). \tag {7.6.38}$$

Substituting the control (7.6.38) in the plant (7.6.32) and treating the various $\alpha,\ldots,\alpha_{p-1}$ as additional state variables, the new unconstrained control becomes $\alpha_{p}$ . Thus,
