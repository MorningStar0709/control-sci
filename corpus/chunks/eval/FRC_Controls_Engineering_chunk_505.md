# C.2.1 Continuous case

To find the control input required at steady-state, set equation (6.3) to zero.

$$\dot {\mathbf {x}} = \mathbf {A x} + \mathbf {B u}\mathbf {y} = \mathbf {C x} + \mathbf {D u}\mathbf {0} = \mathbf {A x} _ {s s} + \mathbf {B u} _ {s s}\mathbf {y} _ {s s} = \mathbf {C x} _ {s s} + \mathbf {D u} _ {s s}\mathbf {0} = \mathbf {A N} _ {x} \mathbf {y} _ {s s} + \mathbf {B N} _ {u} \mathbf {y} _ {s s}\mathbf {y} _ {s s} = \mathbf {C N} _ {x} \mathbf {y} _ {s s} + \mathbf {D N} _ {u} \mathbf {y} _ {s s}
\left[ \begin{array}{c} \mathbf {0} \\ \mathbf {y} _ {s s} \end{array} \right] = \left[ \begin{array}{c} \mathbf {A N} _ {x} + \mathbf {B N} _ {u} \\ \mathbf {C N} _ {x} + \mathbf {D N} _ {u} \end{array} \right] \mathbf {y} _ {s s}

\left[ \begin{array}{c} \mathbf {0} \\ \mathbf {1} \end{array} \right] = \left[ \begin{array}{c} \mathbf {A N} _ {x} + \mathbf {B N} _ {u} \\ \mathbf {C N} _ {x} + \mathbf {D N} _ {u} \end{array} \right]

\left[ \begin{array}{c} \mathbf {0} \\ \mathbf {1} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ \mathbf {C} & \mathbf {D} \end{array} \right] \left[ \begin{array}{c} \mathbf {N} _ {x} \\ \mathbf {N} _ {u} \end{array} \right]

\left[ \begin{array}{c} \mathbf {N} _ {x} \\ \mathbf {N} _ {u} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ \mathbf {C} & \mathbf {D} \end{array} \right] ^ {+} \left[ \begin{array}{c} \mathbf {0} \\ \mathbf {1} \end{array} \right]
$$

where + denotes the Moore-Penrose pseudoinverse.
