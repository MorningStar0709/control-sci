# 7.8.3 Do feedforwards affect stability?

Feedforwards have no effect on stability because they don’t use the system state. We’ll demonstrate this for a plant inversion feedforward.

Let $\mathbf { u } _ { k } = \mathbf { K } ( \mathbf { r } _ { k } - \mathbf { x } _ { k } )$ be a feedback controller for the discrete model $\mathbf { x } _ { k + 1 } = \mathbf { A } \mathbf { x } _ { k } +$ $\mathbf { B } \mathbf { u } _ { k }$ .

$$
\begin{array}{l} \mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B u} _ {k} \\ \mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B} (\mathbf {K} (\mathbf {r} _ {k} - \mathbf {x} _ {k})) \\ \mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B K} (\mathbf {r} _ {k} - \mathbf {x} _ {k}) \\ \mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B K r} _ {k} - \mathbf {B K x} _ {k} \\ \mathbf {x} _ {k + 1} = (\mathbf {A} - \mathbf {B K}) \mathbf {x} _ {k} + \mathbf {B K r} _ {k} \\ \end{array}
$$

The system is stable if the eigenvalues of A − BK are within the unit circle. Now add the plant inversion feedforward controller $\mathbf { B } ^ { + } ( \mathbf { r } _ { k + 1 } - \mathbf { A r } _ { k } )$ to $\mathbf { u } _ { k }$ .

$$
\begin{array}{l} \mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B u} _ {k} \\ \mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B} (\mathbf {K} (\mathbf {r} _ {k} - \mathbf {x} _ {k}) + \mathbf {B} ^ {+} (\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k})) \\ \mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B K} (\mathbf {r} _ {k} - \mathbf {x} _ {k}) + \mathbf {r} _ {k + 1} - \mathbf {A r} _ {k} \\ \mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B K r} _ {k} - \mathbf {B K x} _ {k} + \mathbf {r} _ {k + 1} - \mathbf {A r} _ {k} \\ \mathbf {x} _ {k + 1} = (\mathbf {A} - \mathbf {B K}) \mathbf {x} _ {k} + \mathbf {r} _ {k + 1} + (\mathbf {B K} - \mathbf {A}) \mathbf {r} _ {k} \\ \mathbf {x} _ {k + 1} = (\mathbf {A} - \mathbf {B K}) \mathbf {x} _ {k} + \mathbf {r} _ {k + 1} - (\mathbf {A} - \mathbf {B K}) \mathbf {r} _ {k} \\ \end{array}
$$

The multiplicative term on $\mathbf { x } _ { k }$ is still A−BK, so the feedforward didn’t affect stability. It still affects the system response and steady-state error though.
