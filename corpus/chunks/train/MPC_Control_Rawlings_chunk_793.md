The optimization problem (7.20) motivates us, as in parametric quadratic programming, to consider, for any parameter w “close” to x, the simpler equality constrained problem $\mathbb { P } _ { x } ( \boldsymbol { w } )$ defined by

$$
\begin{array}{l} V _ {x} ^ {0} (w) = \min _ {u} \{V (w, u) \mid M _ {x} ^ {0} u = N _ {x} ^ {0} w + p _ {x} ^ {0} \} \\ u _ {x} ^ {0} (w) = \arg \min _ {u} \{V (w, u) \mid M _ {x} ^ {0} u = N _ {x} ^ {0} w + p _ {x} ^ {0} \} \\ \end{array}
$$

Let $u _ { x } ^ { 0 } ( w )$ denote the solution of $\mathbb { P } _ { x } ( \boldsymbol { w } )$ . Because, for each $x \in \mathcal { X }$ , the matrix $M _ { x } ^ { 0 }$ has full rank m, there exists an index set $I _ { x }$ such that $M _ { I _ { x } } \in \mathbb { R } ^ { m \times m }$ is invertible. Hence, for each w, $u _ { x } ^ { 0 } ( w )$ is the unique solution of

$$M _ {I _ {x}} \boldsymbol {u} = N _ {I _ {x}} \boldsymbol {w} + p _ {I _ {x}}$$

so that for all $x \in { \mathcal { X } }$ , all $\boldsymbol { w } \in \mathbb { R } ^ { m }$

$$u _ {x} ^ {0} (w) = K _ {x} w + k _ {x} \tag {7.21}$$

where $K _ { x } : = ( M _ { I _ { x } } ) ^ { - 1 } N _ { I _ { x } }$ and $k _ { x } : = ( M _ { I _ { x } } ) ^ { - 1 } p _ { I _ { x } }$ . In particular, $u ^ { 0 } ( x ) =$ $u _ { x } ^ { 0 } ( x ) = K _ { x } x + k _ { x }$ . Since $V _ { x } ^ { 0 } ( x ) = V _ { x } ( x , u _ { x } ^ { 0 } ( w ) ) = q ^ { \prime } x + r ^ { \prime } u _ { x } ^ { 0 } ( w )$ , it follows that

$$V _ {x} ^ {0} (x) = \left(q ^ {\prime} + r ^ {\prime} K _ {x}\right) x + r ^ {\prime} k _ {x}$$

for all $x \in { \mathcal { X } }$ , all $\boldsymbol { w } \in \mathbb { R } ^ { m }$ . Both $V _ { x } ^ { 0 } ( \cdot )$ and $u _ { x } ^ { 0 } ( \cdot )$ are affine in x.

It follows from Proposition $7 . 1 9 \mathrm { t h a t } - r \in C ^ { * } ( x , u ^ { 0 } ( x ) ) = \mathrm { c o n e } \{ M _ { i } ^ { \prime } \mid $ $i \in I ^ { 0 } ( x ) = I ( x , u ^ { 0 } ( x ) ) \} = \mathrm { c o n e } \{ M _ { i } ^ { \prime } \ | \ i \in I _ { x } \}$ . Since $\mathbb { P } _ { x } ( \boldsymbol { w } )$ satisfies the conditions of Proposition 7.8, we may proceed as in Section 7.3.4 and define, for each $x \in { \mathcal { X } }$ , the set $R _ { x } ^ { 0 }$ as in (7.5)

$$
R _ {x} ^ {0} := \left\{w \in \mathbb {R} ^ {n}   \Big | \begin{array}{c} u _ {x} ^ {0} (w) \in \mathcal {U} (w) \\ - \nabla_ {u} V (w, u _ {x} ^ {0} (w)) \in C ^ {*} (x, u ^ {0} (x)) \end{array} \right\}
$$
