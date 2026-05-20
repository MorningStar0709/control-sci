# C.2.3 Deriving steady-state input

Now, we’ll find an expression that uses ${ \bf N } _ { x }$ and $\mathbf { N } _ { u }$ to convert the reference r to a control input feedforward $\mathbf { u } _ { f f }$ . Let’s start with equation (C.1).

$$\mathbf {x} _ {s s} = \mathbf {N} _ {x} \mathbf {y} _ {s s}\mathbf {N} _ {x} ^ {+} \mathbf {x} _ {s s} = \mathbf {y} _ {s s}$$

Now substitute this into equation (C.2).

$$\mathbf {u} _ {s s} = \mathbf {N} _ {u} \mathbf {y} _ {s s}\mathbf {u} _ {s s} = \mathbf {N} _ {u} (\mathbf {N} _ {x} ^ {+} \mathbf {x} _ {s s})\mathbf {u} _ {s s} = \mathbf {N} _ {u} \mathbf {N} _ {x} ^ {+} \mathbf {x} _ {s s}$$

$\mathbf { u } _ { s s }$ and $\mathbf { x } _ { s s }$ are also known as $\mathbf { u } _ { f f }$ and r respectively.

$$\mathbf {u} _ {f f} = \mathbf {N} _ {u} \mathbf {N} _ {x} ^ {+} \mathbf {r}$$

So all together, we get theorem C.2.1.
