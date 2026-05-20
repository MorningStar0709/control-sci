Definition 7.1 (Polytopic (polyhedral) partition). A set ${ \mathcal { P } } = \{ \mathbb { Z } _ { i } \mid i \in { \mathcal { I } } \}$ , for some index set I, is called a polytopic (polyhedral) partition of the polytopic (polyhedral) set Z if $\mathbb { Z } = \cup _ { i \in { 2 } } \mathbb { Z } _ { i }$ and the sets $\mathbb { Z } _ { i } , ~ i \in \mathrm { ~ \mathcal { I } ~ }$ , are polytopes (polyhedrons) with nonempty interiors (relative to $\mathbb { Z } ) ^ { 1 }$ that are nonintersecting: int $( \mathbb { Z } _ { i } ) \cap \operatorname { i n t } ( \mathbb { Z } _ { j } ) = \emptyset \operatorname { i f } i \neq j$ .

Definition 7.2 (Piecewise affine function). A function $f : \mathbb { Z } \to \mathbb { R } ^ { m }$ is said to be piecewise affine on a polytopic (polyhedral) partition $\mathcal { P } =$ $\{ \mathbb { Z } _ { i } \mid i \in \mathcal { I } \}$ if it satisfies, for some $K _ { i } , k _ { i } , i \in \mathcal { I } , f ( x ) = K _ { i } x + k _ { i }$ for all $x \in \mathbb { Z } _ { i }$ , all $i \in { \mathcal { I } }$ . Similarly, a function $f : \mathbb { Z } \to \mathbb { R }$ is said to be piecewise quadratic on a polytopic (polyhedral) partition ${ \mathcal { P } } = \{ \mathbb { Z } _ { i } \mid i \in \mathcal { I } \}$ if it satisfies, for some $Q _ { i } , r _ { i } .$ , and $s _ { i } , i \in \mathcal { I } , f ( x ) = ( 1 / 2 ) x ^ { \prime } Q _ { i } x + r _ { i } ^ { \prime } x + s _ { i }$ for all $x \in \mathbb { Z } _ { i }$ , all $i \in { \mathcal { I } }$ .

Note the piecewise affine and piecewise quadratic functions defined this way are not necessarily continuous and may, therefore, be set valued at the intersection of the defining polyhedrons. An example is the piecewise affine function $f ( \cdot )$ defined by

$$
\begin{array}{l} f (x) := - x - 1 \quad x \in (- \infty , 0 ] \\ := x + 1 \quad x \in [ 0, \infty) \\ \end{array}
$$

This function is set valued at $x \ = \ 0$ where it has the value $f ( 0 ) =$ $\{ - 1 , 1 \}$ . We shall mainly be concerned with continuous piecewise affine and piecewise quadratic functions.

We now generalize the points illustrated by our example above and consider, in turn, parametric quadratic programming and parametric linear programming and their application to optimal control problems. We deal with parametric quadratic programming first because it is more widely used and because, with reasonable assumptions, the minimizer is unique making the underlying ideas somewhat simpler to follow.
