# Theorem C.2.1 — Steady-state feedforward.

Continuous:

$$
\left[ \begin{array}{l} \mathbf {N} _ {x} \\ \mathbf {N} _ {u} \end{array} \right] = \left[ \begin{array}{l l} \mathbf {A} & \mathbf {B} \\ \mathbf {C} & \mathbf {D} \end{array} \right] ^ {+} \left[ \begin{array}{l} \mathbf {0} \\ \mathbf {1} \end{array} \right] \tag {C.3}
\mathbf {u} _ {f f} = \mathbf {N} _ {u} \mathbf {N} _ {x} ^ {+} \mathbf {r} \tag {C.4}$$

Discrete:

$$
\left[ \begin{array}{c} \mathbf {N} _ {x} \\ \mathbf {N} _ {u} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} - \mathbf {I} & \mathbf {B} \\ \mathbf {C} & \mathbf {D} \end{array} \right] ^ {+} \left[ \begin{array}{c} \mathbf {0} \\ \mathbf {1} \end{array} \right] \tag {C.5}
\mathbf {u} _ {f f, k} = \mathbf {N} _ {u} \mathbf {N} _ {x} ^ {+} \mathbf {r} _ {k} \tag {C.6}$$

In the augmented matrix, B should contain one column corresponding to an actuator and C should contain one row whose output will be driven by that actuator. More than one actuator or output can be included in the computation at once, but the result won’t be the same as if they were computed independently and summed afterward.

After computing the feedforward for each actuator-output pair, the respective collections of ${ \bf N } _ { x }$ and $\mathbf { N } _ { u }$ matrices can summed to produce the combined feedforward.

If the augmented matrix in theorem C.2.1 is square (number of inputs = number of outputs), the normal matrix inverse can be used instead.
