# 6.4 The Hamilton-Jacobi-Bellman Equation

2. Zero-Order Hold: Alternatively, using sampler and zero-order hold [83], the continuous-time state model (6.3.32) becomes

$$\mathbf {x} (k + 1) = \mathbf {A} _ {d} \mathbf {x} (k) + \mathbf {B} _ {d} \mathbf {u} (k)\mathbf {A} _ {d} = e ^ {\mathbf {A} T}, \text {and} \mathbf {B} _ {d} = \int_ {0} ^ {T} e ^ {\mathbf {A} \tau} \mathbf {B} d \tau . \tag {6.3.37}$$

Thus, we have the discrete-time state model (6.3.35) or (6.3.37) and the corresponding discrete-time cost function (6.3.36) for which we can now apply the DP method explained in the previous sections.
