# 8.4.2 Affine system discretization

We’re going to discretize the following continuous time state-space model with a zeroorder hold.

$$\dot {\mathbf {x}} = \mathbf {A} _ {c} \mathbf {x} + \mathbf {B} _ {c} \mathbf {u} + \mathbf {c}$$

Since u and c are held constant between updates, we can treat them as the aggregated input of the linear model $\dot { \mathbf { x } } = \mathbf { A } _ { c } \mathbf { x } + \mathbf { B } _ { c } \mathbf { u }$ and use the zero-order hold from theorem 7.3.1.

$$\dot {\mathbf {x}} = \mathbf {A} _ {c} \mathbf {x} + \mathbf {B} _ {c} (\mathbf {u} + \mathbf {B} _ {c} ^ {+} \mathbf {c})\mathbf {x} _ {k + 1} = \mathbf {A} _ {d} \mathbf {x} _ {k} + \mathbf {B} _ {d} (\mathbf {u} _ {k} + \mathbf {B} _ {c} ^ {+} \mathbf {c} _ {k})\mathbf {x} _ {k + 1} = \mathbf {A} _ {d} \mathbf {x} _ {k} + \mathbf {B} _ {d} \mathbf {u} _ {k} + \mathbf {B} _ {d} \mathbf {B} _ {c} ^ {+} \mathbf {c} _ {k} \tag {8.4}$$

See theorem 7.3.1 for how to compute $\mathbf { A } _ { d }$ and $\mathbf { B } _ { d } .$
