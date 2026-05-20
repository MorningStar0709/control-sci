$$
\left\{\left[ \begin{array}{l l} A & 0 \\ C & 0 \end{array} \right] - \left[ \begin{array}{l} B \\ 0 \end{array} \right] \left[ K _ {x} \quad K _ {z} \right] \right\} \left[ \begin{array}{l} \mathbf {x} ^ {*} \\ \mathbf {z} ^ {*} \end{array} \right] = - \left[ \begin{array}{l} B \\ 0 \end{array} \right] \mathbf {u} _ {f} ^ {*} - \left[ \begin{array}{l} \Gamma \\ 0 \end{array} \right] \mathbf {w} ^ {*} + \left[ \begin{array}{l} 0 \\ I \end{array} \right] \mathbf {y} _ {d} ^ {*}. \tag {7.53}
$$

The matrix on the LHS has only stable eigenvalues and is therefore nonsingular (no eigenvalues at $s = 0$ ). Thus, there is a unique solution for $\mathbf{x}^*, \mathbf{z}^*$ . Furthermore, from Equation 7.53, that solution satisfies $C\mathbf{x}^* = \mathbf{y}_d^*$ ; i.e., $\mathbf{y}^* = \mathbf{y}_d^*$ . The practical meaning of this fact is that, with any feedforward control $\mathbf{u}_f$ (including $\mathbf{u}_f = 0$ ), the system will find an equilibrium such that $\mathbf{y} = \mathbf{y}_d$ . The use of a feedforward term becomes optional—it may help speed up the transient to a new steady state, but it is not necessary. Any inaccuracy in the value of $\mathbf{u}_f$ will be compensated by the integral control. This, in fact, is a generalization of the Type 1 system to the multivariable case, presented in a state-space context.

The design procedure can be summarized as follows:

1. Append m integrators, driven by the error signals $y - y_{d}$ , to the state equations.   
2. Design a stabilizing state feedback controller, using any method. If the LQ regulator method is used, all integrator outputs z must figure in the performance index. It is necessary that these zero-frequency modes be observable from an output $Q^{1/2}x$ ; otherwise, the detectability condition fails.   
3. If desired, design a feedforward control.
