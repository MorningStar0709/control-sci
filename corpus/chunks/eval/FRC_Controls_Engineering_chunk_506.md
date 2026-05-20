# C.2.2 Discrete case

Now, we’ll do the same thing for the discrete system. To find the control input required at steady-state, set $\mathbf { x } _ { k + 1 } = \mathbf { A } \mathbf { x } _ { k } + \mathbf { B } \mathbf { u } _ { k }$ to zero.

$$\mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B u} _ {k}\mathbf {y} _ {k} = \mathbf {C x} _ {k} + \mathbf {D u} _ {k}\mathbf {x} _ {s s} = \mathbf {A x} _ {s s} + \mathbf {B u} _ {s s}\mathbf {y} _ {s s} = \mathbf {C x} _ {s s} + \mathbf {D u} _ {s s}\mathbf {0} = (\mathbf {A} - \mathbf {I}) \mathbf {x} _ {s s} + \mathbf {B u} _ {s s}\mathbf {y} _ {s s} = \mathbf {C x} _ {s s} + \mathbf {D u} _ {s s}\mathbf {0} = (\mathbf {A} - \mathbf {I}) \mathbf {N} _ {x} \mathbf {y} _ {s s} + \mathbf {B N} _ {u} \mathbf {y} _ {s s}\mathbf {y} _ {s s} = \mathbf {C N} _ {x} \mathbf {y} _ {s s} + \mathbf {D N} _ {u} \mathbf {y} _ {s s}
\left[ \begin{array}{c} \mathbf {0} \\ \mathbf {y} _ {s s} \end{array} \right] = \left[ \begin{array}{c} (\mathbf {A} - \mathbf {I}) \mathbf {N} _ {x} + \mathbf {B N} _ {u} \\ \mathbf {C N} _ {x} + \mathbf {D N} _ {u} \end{array} \right] \mathbf {y} _ {s s}

\left[ \begin{array}{c} \mathbf {0} \\ \mathbf {1} \end{array} \right] = \left[ \begin{array}{c} (\mathbf {A} - \mathbf {I}) \mathbf {N} _ {x} + \mathbf {B N} _ {u} \\ \mathbf {C N} _ {x} + \mathbf {D N} _ {u} \end{array} \right]

\left[ \begin{array}{c} \mathbf {0} \\ \mathbf {1} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} - \mathbf {I} & \mathbf {B} \\ \mathbf {C} & \mathbf {D} \end{array} \right] \left[ \begin{array}{c} \mathbf {N} _ {x} \\ \mathbf {N} _ {u} \end{array} \right]

\left[ \begin{array}{c} \mathbf {N} _ {x} \\ \mathbf {N} _ {u} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} - \mathbf {I} & \mathbf {B} \\ \mathbf {C} & \mathbf {D} \end{array} \right] ^ {+} \left[ \begin{array}{c} \mathbf {0} \\ \mathbf {1} \end{array} \right]
$$

where + denotes the Moore-Penrose pseudoinverse.
