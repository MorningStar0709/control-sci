# B.3 State feedback with output cost

LQR is normally used for state feedback on

$$\mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B u} _ {k}\mathbf {y} _ {k} = \mathbf {C x} _ {k} + \mathbf {D u} _ {k}$$

with the cost functional

$$J = \sum_ {k = 0} ^ {\infty} (\mathbf {x} _ {k} ^ {\mathsf {T}} \mathbf {Q} \mathbf {x} _ {k} + \mathbf {u} _ {k} ^ {\mathsf {T}} \mathbf {R} \mathbf {u} _ {k})$$

However, we may not know how to select costs for some of the states, or we don’t care what certain internal states are doing. We can address this by writing the cost functional in terms of the output vector instead of the state vector. Not only can we make our output contain a subset of states, but we can use any other cost metric we can think of as long as it’s representable as a linear combination of the states and inputs.[3]

For state feedback with an output cost, we want to minimize the following cost functional.

$$J = \sum_ {k = 0} ^ {\infty} (\mathbf {y} _ {k} ^ {\mathsf {T}} \mathbf {Q} \mathbf {y} _ {k} + \mathbf {u} _ {k} ^ {\mathsf {T}} \mathbf {R} \mathbf {u} _ {k})$$

Substitute in the expression for $\mathbf { y } _ { k }$ .

$$J = \sum_ {k = 0} ^ {\infty} ((\mathbf {C x} _ {k} + \mathbf {D u} _ {k}) ^ {\top} \mathbf {Q} (\mathbf {C x} _ {k} + \mathbf {D u} _ {k}) + \mathbf {u} _ {k} ^ {\top} \mathbf {R u} _ {k})$$

Apply the transpose to the left-hand side of the $\mathbf { Q }$ term.

$$J = \sum_ {k = 0} ^ {\infty} ((\mathbf {x} _ {k} ^ {\mathsf {T}} \mathbf {C} ^ {\mathsf {T}} + \mathbf {u} _ {k} ^ {\mathsf {T}} \mathbf {D} ^ {\mathsf {T}}) \mathbf {Q} (\mathbf {C x} _ {k} + \mathbf {D u} _ {k}) + \mathbf {u} _ {k} ^ {\mathsf {T}} \mathbf {R u} _ {k})$$

Factor out $\begin{array} { r } { \left[ \mathbf { x } _ { k } \right] ^ { \top } } \\ { \left[ \mathbf { u } _ { k } \right] ^ { \top } } \end{array}$ from the left side and $\left[ { \bf { x } } _ { k } \right]$ from the right side of each term.
