which is a linear inequality in w. Similarly, since $\nabla _ { u } V ( w , u ) = R u +$ $S w + r$ and since $C ^ { * } ( x , u ^ { 0 } ( x ) ) = \{ g \mid L _ { x } ^ { 0 } g \leq 0 \}$ where $L _ { x } ^ { 0 } = L _ { ( x , u ^ { 0 } ( x ) ) }$ , the constraint $- \nabla _ { u } V ( x , u _ { x } ^ { 0 } ( w ) ) \in C ( x , u ^ { 0 } ( x ) )$ may be expressed as

$$- L _ {x} ^ {0} (R (K _ {x} w + k _ {x}) + S w + r) \leq 0$$

which is also an affine inequality in the variable w. Thus, for each x, there exists a matrix $F _ { x }$ and vector $f _ { x }$ such that

$$R _ {x} ^ {0} = \{w \mid F _ {x} w \leq f _ {x} \}$$

so that $R _ { x } ^ { 0 }$ is polyhedral. Since $u _ { x } ^ { 0 } ( x ) = u ^ { 0 } ( x )$ , it follows that $u _ { x } ^ { 0 } ( x ) \in$ $\mathcal { U } ( x )$ and $- \nabla _ { u } V ( x , u _ { x } ^ { 0 } ( x ) ) \in C ^ { * } ( x , u ^ { 0 } ( x ) )$ so that $x \in R _ { x } ^ { 0 }$ .

Our next task is to bound the number of distinct regions $R _ { x } ^ { 0 }$ that exist as we permit x to range over X. We note, from its definition, that $R _ { x } ^ { 0 }$ is determined, through the constraint $M _ { x } ^ { 0 } u \ = \ N _ { x } ^ { 0 } w \ + \ p _ { x } ^ { 0 }$ in $\mathbb { P } _ { x } ( \boldsymbol { w } )$ , through $u _ { x } ^ { 0 } ( \cdot )$ and through $C ^ { * } ( x , u ^ { 0 } ( x ) )$ , by $I ^ { 0 } ( x )$ so that $R _ { x _ { 1 } } ^ { 0 } \ \neq \ R _ { x _ { 2 } } ^ { 0 }$ implies that $I ^ { 0 } ( x _ { 1 } ) \neq I ^ { 0 } ( x _ { 2 } )$ . Since the number of subsets of $\{ 1 , 2 , \ldots , p \}$ is finite, the number of distinct regions $R _ { x } ^ { 0 }$ as x ranges over X is finite. Because each $x \in { \mathcal { X } }$ lies in the set $R _ { x } ^ { 0 }$ , there exists a discrete set of points $X \subset { \mathcal { X } }$ such that ${ \mathcal { X } } = \cup \{ R _ { x } ^ { 0 } \mid x \in X \}$ . We have proved:

Proposition 7.10 (Piecewise quadratic (affine) cost (solution)).

(a) There exists a set X of a finite number of points in X such that $x =$ $\cup \{ R _ { x } ^ { 0 } \mid x \in X \}$ and $\{ R _ { x } ^ { 0 } \ | \ x \in X \}$ is a polyhedral partition of X.

(b) The value function $V ^ { 0 } ( \cdot )$ of the parametric piecewise quadratic program P is piecewise quadratic in X, being quadratic and equal to $V _ { x } ^ { 0 } ( \cdot )$ , defined in (7.3) in each polyhedron $R _ { x } , x \in X$ . Similarly, the minimizer $u ^ { 0 } ( \cdot )$ is piecewise affine in X, being affine and equal to $u _ { x } ^ { 0 } ( \cdot )$ defined in (7.4) in each polyhedron $R _ { x } ^ { 0 } , x \in X$ .
