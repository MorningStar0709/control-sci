# Theorem B.3.1 — Linear-quadratic regulator with output cost.

$$
\mathbf {u} _ {k} ^ {*} = \underset {\mathbf {u} _ {k}} {\arg \min} \sum_ {k = 0} ^ {\infty} \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\top} \left[ \begin{array}{c c} \underbrace {\mathbf {C} ^ {\top} \mathbf {Q C}} _ {\mathbf {Q}} & \underbrace {\mathbf {C} ^ {\top} \mathbf {Q D}} _ {\mathbf {N}} \\ \underbrace {\mathbf {D} ^ {\top} \mathbf {Q C}} _ {\mathbf {N} ^ {\top}} & \underbrace {\mathbf {D} ^ {\top} \mathbf {Q D} + \mathbf {R}} _ {\mathbf {R}} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right]
\text { subject to } \mathbf {x} _ {k + 1} = \mathbf {A} \mathbf {x} _ {k} + \mathbf {B} \mathbf {u} _ {k} \tag {B.4}$$

The optimal control policy $\mathbf { u } _ { k } ^ { * }$ is ${ \bf K } ( { \bf r } _ { k } - { \bf x } _ { k } )$ where $\mathbf { r } _ { k }$ is the desired state. Note that the Q in $\mathbf { C } ^ { \top } \mathbf { Q C }$ is outputs × outputs instead of states × states. K can be computed via the typical LQR equations based on the algebraic Riccati equation.

If the output is just the state vector, then ${ \bf C } = { \bf I } , { \bf D } = { \bf 0 }$ , and the cost functional simplifies to that of LQR with a state cost.

$$
J = \sum_ {k = 0} ^ {\infty} \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\mathsf {T}} \left[ \begin{array}{c c} \mathbf {Q} & \mathbf {0} \\ \mathbf {0} & \mathbf {R} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right]
$$
