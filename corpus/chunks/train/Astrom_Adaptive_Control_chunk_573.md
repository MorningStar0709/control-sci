# EXAMPLE 9.5 Nonlinear transformation of a second-order system

Consider the system

$$\frac {d x _ {1}}{d t} = f _ {1} (x _ {1}, x _ {2})\frac {d x _ {2}}{d t} = f _ {2} (x _ {1}, x _ {2}, u)y = x _ {1}$$

Assume that the state variables can be measured and that we want to find a feedback such that the response of the variable $x_{1}$ to the command signal is given by the transfer function

$$G (s) = \frac {\omega^ {2}}{s ^ {2} + 2 \zeta \omega s + \omega^ {2}} \tag {9.5}$$

Introduce new coordinates $z_{1}$ and $z_{2}$ , defined by

$$
\begin{array}{l} z _ {1} = x _ {1} \\ z _ {2} = \frac {d x _ {1}}{d t} = f _ {1} (x _ {1}, x _ {2}) \\ \end{array}
$$

and the new control signal v, defined by

$$v = F (x _ {1}, x _ {2}, u) = \frac {\partial f _ {1}}{\partial x _ {1}} f _ {1} + \frac {\partial f _ {1}}{\partial x _ {2}} f _ {2} \tag {9.6}$$

These transformations result in the linear system

$$\frac {d z _ {1}}{d t} = z _ {2} \tag {9.7}\frac {d z _ {2}}{d t} = v$$

It is easily seen that the linear feedback

$$v = \omega^ {2} (u _ {c} \dots z _ {1}) - 2 \zeta \omega z _ {2} \tag {9.8}$$

gives the desired closed-loop transfer function of Eq. (9.5) from $u_{c}$ to $z_{1} = x_{1}$ for the linear system of Eqs. (9.7). It remains to transform back to the original variables. It follows from Eqs. (9.6) and (9.8) that

$$F (x _ {1}, x _ {2}, u) = \frac {\partial f _ {1}}{\partial x _ {1}} f _ {1} + \frac {\partial f _ {1}}{\partial x _ {2}} f _ {2} = \omega^ {2} (u _ {c} - x _ {1}) - 2 \zeta \omega f _ {1} (x _ {1}, x _ {2})$$

Solving this equation for u gives the desired feedback. It follows from the implicit function theorem that a condition for local solvability is that the partial derivative $\partial F/\partial u$ is different from zero. □

The generalization of Example 9.5 requires a solution to the general problem of transforming a nonlinear system into a linear system by nonlinear feedback. Conditions and examples are given in the references at the end of this chapter. Figure 9.7 shows the general case when the full state is measured. There is a nonlinear transformation

$$u = g _ {1} (x, v)z = g _ {2} (x)$$

that makes the relation between v and z linear. A state feedback controller from z is then computed that gives v. The control signal v is then transformed into the original control signal u. Feedback linearization requires good knowledge about the nonlinearities of the process. Uncertainties will give a transformed system that is not linear, although it may be easier to control than the original system.
