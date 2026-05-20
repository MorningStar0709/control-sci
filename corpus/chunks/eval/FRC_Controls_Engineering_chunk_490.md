# Theorem B.4.1 — Implicit model following.

$$
\mathbf {u} _ {k} ^ {*} = \underset {\mathbf {u} _ {k}} {\arg \min} \sum_ {k = 0} ^ {\infty} \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\mathsf {T}} \left[ \begin{array}{c c} \mathbf {Q} _ {i m f} & \mathbf {N} _ {i m f} \\ \mathbf {N} _ {i m f} ^ {\mathsf {T}} & \mathbf {R} _ {i m f} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right]
\text { subject to } \mathbf {x} _ {k + 1} = \mathbf {A} \mathbf {x} _ {k} + \mathbf {B} \mathbf {u} _ {k} \tag {B.6}$$

where

$$\mathbf {Q} _ {i m f} = (\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C}) ^ {\top} \mathbf {Q} (\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C})\mathbf {N} _ {i m f} = (\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C}) ^ {\top} \mathbf {Q} (\mathbf {C B})\mathbf {R} _ {i m f} = (\mathbf {C B}) ^ {\top} \mathbf {Q} (\mathbf {C B}) + \mathbf {R}$$

The optimal control policy $\mathbf { u } _ { k } ^ { * }$ is $- \mathbf { K } \mathbf { x } _ { k }$ . K can be computed via the typical LQR equations based on the algebraic Riccati equation.

The control law $\mathbf { u } _ { i m f , k } = - \mathbf { K } \mathbf { x } _ { k }$ makes $\mathbf { x } _ { k + 1 } = \mathbf { A } \mathbf { x } _ { k } + \mathbf { B } \mathbf { u } _ { i m f , k }$ match the openloop response of $\mathbf { z } _ { k + 1 } = \mathbf { A } _ { r e f } \mathbf { z } _ { k }$ .

If the original and desired system have the same states, then C = I and the cost func-

tional simplifies to

$$
J = \sum_ {k = 0} ^ {\infty} \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\mathsf {T}} \left[ \begin{array}{c c} \underbrace {(\mathbf {A} - \mathbf {A} _ {r e f}) ^ {\mathsf {T}} \mathbf {Q} (\mathbf {A} - \mathbf {A} _ {r e f})} _ {\mathbf {Q}} & \underbrace {(\mathbf {A} - \mathbf {A} _ {r e f}) ^ {\mathsf {T}} \mathbf {Q B}} _ {\mathbf {N}} \\ \underbrace {\mathbf {B} ^ {\mathsf {T}} \mathbf {Q} (\mathbf {A} - \mathbf {A} _ {r e f})} _ {\mathbf {N} ^ {\mathsf {T}}} & \underbrace {\mathbf {B} ^ {\mathsf {T}} \mathbf {Q B} + \mathbf {R}} _ {\mathbf {R}} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] (B. 7)
$$
