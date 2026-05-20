Peano’s existence theorem states that if f is continuous on D, then, for all $( x _ { 0 } , t _ { 0 } ) \in D$ there exists at least one solution of (A.12)) passing through $( x _ { 0 } , t _ { 0 } )$ . The solution is not necessarily unique - a counter example being ${ \dot { x } } = { \sqrt { x } }$ for $x \ge 0$ . To proceed we need to be able to deal with systems for which $f ( \cdot )$ is not necessarily continuous for the following reason. If the system is described by ${ \dot { x } } = f ( x , u , t )$ where $f : \mathbb { R } ^ { n } \times \mathbb { R } ^ { m } \to \mathbb { R } ^ { n }$ is continuous, and the control $u : \mathbb { R }  \mathbb { R } ^ { m }$ is continuous, then, for given u(·), the function $f ^ { u } : \mathbb { R } ^ { n } \times \mathbb { R } \to \mathbb { R } ^ { n }$ defined by:

$$f ^ {u} (x, t) := f (x, u (t), t)$$

is continuous in t. We often encounter controls that are not continuous, however, in which case $f ^ { u } ( \cdot )$ is also not continuous. We need a richer class of controls. A suitable class is the class of measurable functions which, for the purpose of this book, we may take to be a class rich enough to include all controls, such as those that are merely piecewise continuous, that we may encounter. If the control $u ( \cdot )$ is measurable and $f ( \cdot )$ is continuous, then $f ^ { u } ( \cdot )$ , defined above, is continuous in x but measurable in t, so we are forced to study such functions. Suppose, as above, D is an open set in $\mathbb { R } ^ { n } \times \mathbb { R }$ . The function $f : D  \mathbb { R } ^ { n }$ is said to satisfy the Caratheodory conditions in D if:

(a) f is measurable in t for each fixed x,

(b) f is continuous in x for each fixed t,

(c) for each compact set F in D there exists a measurable function $t \mapsto m _ { F } ( t )$ such that

$$\left| f (x, t) \right| \leq m _ {F} (t)$$
