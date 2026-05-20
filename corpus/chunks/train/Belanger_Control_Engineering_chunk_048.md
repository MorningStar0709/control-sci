$$\Delta \dot {\mathbf {x}} = \left. \frac {\partial \mathbf {f}}{\partial \mathbf {x}} \right| _ {*} \Delta \mathbf {x} + \left. \frac {\partial \mathbf {f}}{\partial \mathbf {u}} \right| _ {*} \Delta \mathbf {u} + \left. \frac {\partial \mathbf {f}}{\partial \mathbf {w}} \right| _ {*} \Delta \mathbf {w} \tag {2.50}\Delta \mathbf {y} = \left. \frac {\partial \mathbf {h}}{\partial \mathbf {x}} \right| _ {*} \Delta \mathbf {x} + \left. \frac {\partial \mathbf {h}}{\partial \mathbf {u}} \right| _ {*} \Delta \mathbf {u} + \left. \frac {\partial \mathbf {h}}{\partial \overline {{\mathbf {w}}}} \right| _ {*} \Delta \mathbf {w} \tag {2.51}$$

where w is the vector of disturbance inputs.

If the original system is linear and time-invariant, it is represented by equations of the form

$$\dot {\mathbf {x}} = A \mathbf {x} + B \mathbf {u} + F \mathbf {w}\mathbf {y} = C \mathbf {x} + D \mathbf {u} + G \mathbf {w}. \tag {2.52}$$

The equilibrium point satisfies

$$\mathbf {0} = A \mathbf {x} ^ {*} + B \mathbf {u} ^ {*} + F \mathbf {w} ^ {*}\mathbf {y} ^ {*} = C \mathbf {x} ^ {*} + D \mathbf {u} ^ {*} + G \mathbf {w} ^ {*}. \tag {2.53}$$

If $u^{*}$ and $w^{*}$ are given, a unique solution $x^{*}$ (hence $y^{*}$ ) always exists if A is nonsingular. If A is singular, there are multiple solutions if the vector $Bu^{*} + Fw^{*}$ is in the range space of A, i.e., can be constructed by a linear combination of the columns of A; if that is not the case, there is no solution.

If $\mathbf{y}^*$ and $\mathbf{w}^*$ are given and we wish to solve for $\mathbf{x}^*$ and $\mathbf{u}^*$ , it is useful to write Equation 2.53 as

$$
\left[ \begin{array}{l l} A & B \\ C & D \end{array} \right] \left[ \begin{array}{l} \mathbf {x} ^ {*} \\ \mathbf {u} ^ {*} \end{array} \right] = \left[ \begin{array}{l} 0 \\ \mathbf {y} ^ {*} \end{array} \right] - \left[ \begin{array}{l} F \\ G \end{array} \right] \mathbf {w} ^ {*}. \tag {2.54}
$$
