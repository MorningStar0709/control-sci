# 7.7.1 Preliminaries

The parametric linear program $\mathbb { P } ( x )$ is

$$V ^ {0} (x) = \min _ {u} \{V (x, u) \mid (x, u) \in \mathbb {Z} \}$$

where $x \in { \mathcal { X } } \subset \mathbb { R } ^ { n }$ and $u \in \mathbb { R } ^ { m }$ , the cost function V (·) is defined by

$$V (x, u) = q ^ {\prime} x + r ^ {\prime} u$$

and the constraint set Z is defined by

$$\mathbb {Z} := \{(x, u) \mid M u \leq N x + p \}$$

Let $u ^ { 0 } ( x )$ denote the solution of $\mathbb { P } ( x )$ , i.e.,

$$u ^ {0} (x) = \arg \min _ {u} \{V (x, u) \mid (x, u) \in \mathbb {Z} \}$$

The solution $u ^ { 0 } ( x )$ may be set valued. The parametric linear program may also be expressed as

$$V ^ {0} (x) = \min _ {u} \{V (x, u) \mid u \in \mathcal {U} (x) \}$$

where, as before, the parametric constraint set $\mathcal { U } ( x )$ is defined by

$$\mathcal {U} (x) := \{u \mid (x, u) \in \mathbb {Z} \} = \{u \mid M u \leq N x + p \}$$

Also, as before, the domain of $V ^ { 0 } ( \cdot )$ and $u ^ { 0 } ( \cdot )$ , i.e., the set of points x for which a feasible solution of $\mathbb { P } ( x )$ exists, is the set X defined by

$$\mathcal {X} := \{x \mid \exists u \text { such that } (x, u) \in \mathbb {Z} \} = \{x \mid \mathcal {U} (x) \neq \emptyset \}$$

The set X is the projection of $\mathbb { Z }$ (which is a set in $( x , u ) – \mathbf { s p a c e } )$ onto x-space; see Figure 7.1. We assume in the sequel that the problem is well posed, i.e., for each $x \in \mathcal { X } , V ^ { 0 } ( x ) > - \infty$ . This excludes problems like $V ^ { 0 } ( x ) = \operatorname* { i n f } _ { u } \{ x + u \mid - x \leq 1 , x \leq 1 \}$ for which $V ^ { 0 } ( x ) = - \infty$ for all $x \in \mathcal { X } = [ - 1 , 1 ]$ .

Let $\mathbb { I } _ { 1 : p }$ denote, as usual, the index set $\{ 1 , 2 , \ldots , p \}$ . For all $( x , u ) \in$ $\mathbb { Z } ,$ let $I ( x , u )$ denote the set of active constraints at $( x , u ) , \mathrm { i . e . }$ ,

$$I (x, u) := \{i \in \mathbb {I} _ {1: p} \mid M _ {i} u = N _ {i} x + p _ {i} \}$$

where $A _ { i }$ denotes the ith row of any matrix (or vector) A. Similarly, for any matrix A and any index set $I , A _ { I }$ denotes the matrix with rows $A _ { i } ,$ , $i \in I$ . If, for any $x \in \mathcal { X } , u ^ { 0 } ( x )$ is unique, the set $I ^ { 0 } ( x )$ of constraints active at $( x , u ^ { 0 } ( x ) )$ is defined by

$$I ^ {0} (x) := I (x, u ^ {0} (x))$$

When $u ^ { 0 } ( x )$ is unique, it is a vertex (a face of dimension zero) of the polyhedron $\mathcal { U } ( x )$ and is the unique solution of

$$M _ {x} ^ {0} u = N _ {x} ^ {0} x + p _ {x} ^ {0}$$

where

$$M _ {x} ^ {0} := M _ {I ^ {0} (x)}, N _ {x} ^ {0} := N _ {I ^ {0} (x)}, p _ {x} ^ {0} := p _ {I ^ {0} (x)}$$

In this case, the matrix $M _ { x } ^ { 0 }$ has rank m.
