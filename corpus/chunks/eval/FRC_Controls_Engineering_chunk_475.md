J = \sum_ {k = 0} ^ {\infty} \left[ \begin{array}{c c} \mathbf {x} _ {k} ^ {\mathsf {T}} & \mathbf {u} _ {k} ^ {\mathsf {T}} \end{array} \right] \left[ \begin{array}{c} \mathbf {Q x} _ {k} + \mathbf {N u} _ {k} \\ \mathbf {N} ^ {\mathsf {T}} \mathbf {x} _ {k} + \mathbf {R u} _ {k} \end{array} \right]
J = \sum_ {k = 0} ^ {\infty} (\mathbf {x} _ {k} ^ {\top} (\mathbf {Q x} _ {k} + \mathbf {N u} _ {k}) + \mathbf {u} _ {k} ^ {\top} (\mathbf {N} ^ {\top} \mathbf {x} _ {k} + \mathbf {R u} _ {k}))J = \sum_ {k = 0} ^ {\infty} (\mathbf {x} _ {k} ^ {\mathsf {T}} \mathbf {Q} \mathbf {x} _ {k} + \mathbf {x} _ {k} ^ {\mathsf {T}} \mathbf {N} \mathbf {u} _ {k} + \mathbf {u} _ {k} ^ {\mathsf {T}} \mathbf {N} ^ {\mathsf {T}} \mathbf {x} _ {k} + \mathbf {u} _ {k} ^ {\mathsf {T}} \mathbf {R} \mathbf {u} _ {k})J = \sum_ {k = 0} ^ {\infty} (\mathbf {x} _ {k} ^ {\top} \mathbf {Q} \mathbf {x} _ {k} + \mathbf {x} _ {k} ^ {\top} \mathbf {N} \mathbf {u} _ {k} + \mathbf {x} _ {k} ^ {\top} \mathbf {N} \mathbf {u} _ {k} ^ {\top} + \mathbf {u} _ {\mathbf {k}} ^ {\top} \mathbf {R} \mathbf {u} _ {k})J = \sum_ {k = 0} ^ {\infty} (\mathbf {x} _ {k} ^ {\mathsf {T}} \mathbf {Q} \mathbf {x} _ {k} + 2 \mathbf {x} _ {k} ^ {\mathsf {T}} \mathbf {N} \mathbf {u} _ {k} + \mathbf {u} _ {k} ^ {\mathsf {T}} \mathbf {R} \mathbf {u} _ {k})J = \sum_ {k = 0} ^ {\infty} (\mathbf {x} _ {k} ^ {\mathsf {T}} \mathbf {Q} \mathbf {x} _ {k} + \mathbf {u} _ {k} ^ {\mathsf {T}} \mathbf {R} \mathbf {u} _ {k} + 2 \mathbf {x} _ {k} ^ {\mathsf {T}} \mathbf {N} \mathbf {u} _ {k})$$

The feedback control law which minimizes J subject to the constraint $\mathbf { x } _ { k + 1 } = \mathbf { A } \mathbf { x } _ { k } +$ $\mathbf { B } \mathbf { u } _ { k }$ is

$$\mathbf {u} _ {k} = - \mathbf {K x} _ {k}$$

where K is given by

$$\mathbf {K} = (\mathbf {R} + \mathbf {B} ^ {\mathsf {T}} \mathbf {P B}) ^ {- 1} (\mathbf {B} ^ {\mathsf {T}} \mathbf {P A} + \mathbf {N} ^ {\mathsf {T}})$$

and P is found by solving the discrete time algebraic Riccati equation defined as

$$\mathbf {A} ^ {\top} \mathbf {P A} - \mathbf {P} - (\mathbf {A} ^ {\top} \mathbf {P B} + \mathbf {N}) (\mathbf {R} + \mathbf {B} ^ {\top} \mathbf {P B}) ^ {- 1} (\mathbf {B} ^ {\top} \mathbf {P A} + \mathbf {N} ^ {\top}) + \mathbf {Q} = 0$$

or alternatively

$$\mathcal {A} ^ {\mathsf {T}} \mathbf {P} \mathcal {A} - \mathbf {P} - \mathcal {A} ^ {\mathsf {T}} \mathbf {P} \mathbf {B} (\mathbf {R} + \mathbf {B} ^ {\mathsf {T}} \mathbf {P} \mathbf {B}) ^ {- 1} \mathbf {B} ^ {\mathsf {T}} \mathbf {P} \mathcal {A} + \mathbf {Q} = 0$$

with
