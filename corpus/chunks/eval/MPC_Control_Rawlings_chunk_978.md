# C.1.2 Dynamic Programming

One way to approach DP for discrete time control problems is the simple observation that for all $( x , i )$

$$
\begin{array}{l} V ^ {0} (x, i) = \min _ {\mathbf {u} ^ {i}} \left\{V (x, i, \mathbf {u} ^ {i}) \mid \mathbf {u} ^ {i} \in \mathcal {U} (x, i) \right\} \\ = \min _ {u} \left\{\ell (x, u) + \min _ {\mathbf {u} ^ {i + 1}} V (f (x, u), i + 1, \mathbf {u} ^ {i + 1}) \right| \\ \{u, \mathbf {u} ^ {i + 1} \} \in \mathcal {U} (x, i) \} \tag {C.8} \\ \end{array}
$$

where $\mathbf u ^ { i } = \{ u , u ( i + 1 ) , \ldots , u ( N - 1 ) \} = \{ u , \mathbf u ^ { i + 1 } \}$ . We now make use of the fact that $\{ u , \mathbf u ^ { i + 1 } \} \in \mathcal { U } ( x , i )$ if and only if $( x , u ) \in \mathbb { Z } , f ( x , u ) \in$ $X ( i + 1 )$ , and ${ \mathbf { u } } ^ { i + 1 } \in \mathcal { U } ( f ( x , u ) , i + 1 )$ ) since $f ( x , u ) = x ( i + 1 )$ . Hence we may rewrite (C.8) as

$$V ^ {0} (x, i) = \min _ {u} \{\ell (x, u) + V ^ {0} (f (x, u), i + 1) \mid(x, u) \in \mathbb {Z}, f (x, u) \in X (i + 1) \} \tag {C.9}$$

for all $x \in X ( i )$ where

$$X (i) = \{x \in \mathbb {R} ^ {n} \mid \exists u \text { such that } (x, u) \in \mathbb {Z} \text { and } f (x, u) \in X (i + 1) \} \tag {C.10}$$

Equations (C.9) and (C.10), together with the boundary condition

$$V ^ {0} (x, N) = V _ {f} (x) \forall x \in X (N), \quad X (N) = \mathbb {X} _ {f}$$

constitute the DP recursion for constrained discrete time optimal control problems. If there are no state constraints, i.e., if $\mathbb { Z } = \mathbb { R } ^ { n } \times \mathbb { U }$ where $\mathbb { U } \subset \mathbb { R } ^ { m }$ is compact, then $\ b X ( i ) = \mathbb R ^ { n }$ for all $i \in \{ 0 , 1 , \ldots , N \}$ and the DP equations revert to the familiar DP recursion:

$$V ^ {0} (x, i) = \min _ {u} \{\ell (x, u) + V ^ {0} (f (x, u), i + 1) \} \forall x \in \mathbb {R} ^ {n}$$

with boundary condition

$$V ^ {0} (x, N) = V _ {f} \forall x \in \mathbb {R} ^ {n}$$

We now prove some basic facts; the first is the well known principle of optimality.

Lemma C.1 (Principle of optimality). Let $x \in X _ { N }$ be arbitrary, let $\textbf { u } : =$ $\{ u ( 0 ) , u ( 1 ) , \ldots , u ( N - 1 ) \} \in \mathcal { U } ( x , 0 )$ denote the solution of $\mathbb { P } ( x , 0 )$ and $l e t \left\{ x , x ( 1 ) , x ( 2 ) , \ldots , x ( N ) \right\}$ denote the corresponding optimal state trajectory so that for each i, $x ( i ) \ = \ \phi ( i ; ( x , 0 ) , { \bf u } )$ . Then, for any $i \in$ $\{ 0 , 1 , \ldots , N { - } 1 \}$ , the control sequence $\mathbf { u } ^ { i } : = \{ u ( i ) , u ( i { + } 1 ) , \ldots , u ( N { - } 1 ) \}$ is optimal for $\mathbb { P } ( x ( i ) , i )$ (any portion of an optimal trajectory is optimal).
