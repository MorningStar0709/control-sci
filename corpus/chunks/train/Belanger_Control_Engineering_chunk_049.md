If $m = r$ (equal number of inputs and outputs), then the matrix on the left-hand side (LHS) of Equation 2.54 is square, and a unique solution exists if that matrix is nonsingular. If $r > m$ (more inputs than outputs), and if the matrix has maximal rank $n + m$ , there exist multiple solutions to Equation 2.54. Finally, if $r < m$ (fewer inputs than outputs) and the matrix has maximal rank $n + r$ , there is a (unique) solution only in the special case where $\mathbf{y}^*$ and $\mathbf{w}^*$ are such that the RHS of Equation 2.54 in the range space of the matrix $[A_{C}B_{D}]$ .

As for the incremental system, with

$$\mathbf {x} = \mathbf {x} ^ {*} + \Delta \mathbf {x}, \quad \mathbf {u} = \mathbf {u} ^ {*} + \Delta \mathbf {u}, \quad \mathbf {y} = \mathbf {y} ^ {*} + \Delta \mathbf {y}, \quad \mathbf {w} = \mathbf {w} ^ {*} + \Delta \mathbf {w}$$

Equations 2.52 become

$$\Delta \dot {\mathbf {x}} = A \mathbf {x} ^ {*} + B \mathbf {u} ^ {*} + F \mathbf {w} ^ {*} + A \Delta \mathbf {x} + B \Delta \mathbf {u} + F \Delta \mathbf {w}\mathbf {y} ^ {*} + \Delta \mathbf {y} = C \mathbf {x} ^ {*} + D \mathbf {u} ^ {*} + G \mathbf {w} ^ {*} + C \Delta \mathbf {x} + D \Delta \mathbf {u} + G \Delta \mathbf {w}$$

which, in view of Equation 2.53, yields .

$$\Delta \dot {\mathbf {x}} = A \Delta \mathbf {x} + B \Delta \mathbf {u} + F \Delta \mathbf {w}\Delta \mathbf {y} = C \Delta \mathbf {x} + D \Delta \mathbf {u} + G \Delta \mathbf {w}. \tag {2.55}$$

Equation 2.55 expresses the fact that a linear system is its own incremental system, and therefore no extra work is needed to obtain the incremental system in that case.
