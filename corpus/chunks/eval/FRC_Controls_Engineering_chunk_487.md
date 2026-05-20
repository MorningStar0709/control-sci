# B.4.1 Following reference system matrix

Let the original system dynamics be

$$\mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B u} _ {k}\mathbf {y} _ {k} = \mathbf {C x} _ {k}$$

and the desired system dynamics be $\mathbf { z } _ { k + 1 } = \mathbf { A } _ { r e f } \mathbf { z } _ { k }$ .

$$\mathbf {y} _ {k + 1} = \mathbf {C x} _ {k + 1}\mathbf {y} _ {k + 1} = \mathbf {C} (\mathbf {A x} _ {k} + \mathbf {B u} _ {k})\mathbf {y} _ {k + 1} = \mathbf {C A x} _ {k} + \mathbf {C B u} _ {k}$$

We want to minimize the following cost functional.

$$J = \sum_ {k = 0} ^ {\infty} \left((\mathbf {y} _ {k + 1} - \mathbf {z} _ {k + 1}) ^ {\top} \mathbf {Q} (\mathbf {y} _ {k + 1} - \mathbf {z} _ {k + 1}) + \mathbf {u} _ {k} ^ {\top} \mathbf {R u} _ {k}\right)$$

We’ll be measuring the desired system’s state, so let $\mathbf y = \mathbf z$

$$\mathbf {z} _ {k + 1} = \mathbf {A} _ {r e f} \mathbf {y} _ {k}\mathbf {z} _ {k + 1} = \mathbf {A} _ {r e f} \mathbf {C x} _ {k}$$

Therefore,

$$\mathbf {y} _ {k + 1} - \mathbf {z} _ {k + 1} = \mathbf {C A x} _ {k} + \mathbf {C B u} _ {k} - (\mathbf {A} _ {r e f} \mathbf {C x} _ {k})\mathbf {y} _ {k + 1} - \mathbf {z} _ {k + 1} = (\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C}) \mathbf {x} _ {k} + \mathbf {C B u} _ {k}$$

Substitute this into the cost functional.

$$J = \sum_ {k = 0} ^ {\infty} \left(\left(\mathbf {y} _ {k + 1} - \mathbf {z} _ {k + 1}\right) ^ {\top} \mathbf {Q} \left(\mathbf {y} _ {k + 1} - \mathbf {z} _ {k + 1}\right) + \mathbf {u} _ {k} ^ {\top} \mathbf {R u} _ {k}\right)
\begin{array}{l} J = \sum_ {k = 0} ^ {\infty} \left(\left(\left(\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C}\right) \mathbf {x} _ {k} + \mathbf {C B u} _ {k}\right) ^ {\top} \mathbf {Q} \left(\left(\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C}\right) \mathbf {x} _ {k} + \mathbf {C B u} _ {k}\right) \right. \\ \left. + \mathbf {u} _ {k} ^ {\top} \mathbf {R u} _ {k}\right) \\ \end{array}
$$

Apply the transpose to the left-hand side of the $\mathbf { Q }$ term.

$$
\begin{array}{l} J = \sum_ {k = 0} ^ {\infty} \big ((\mathbf {x} _ {k} ^ {\mathsf {T}} (\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C}) ^ {\mathsf {T}} + \mathbf {u} _ {k} ^ {\mathsf {T}} (\mathbf {C B}) ^ {\mathsf {T}}) \mathbf {Q} ((\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C}) \mathbf {x} _ {k} + \mathbf {C B u} _ {k}) \\ \left. + \mathbf {u} _ {k} ^ {\top} \mathbf {R u} _ {k}\right) \\ \end{array}
$$
