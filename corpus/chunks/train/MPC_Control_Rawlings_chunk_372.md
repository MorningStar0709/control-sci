Since Assumptions 3.8 and 3.9 appear to be similar to Assumptions 2.12 and 2.13, we would expect to obtain stability results analogous to those obtained in Chapter 2. We do obtain preliminary results that are similar, but the stability properties of the closed-loop system are quite different. Before stating the preliminary results, we note that Assumptions 3.8 and 3.9 imply the existence of a terminal control law $\kappa _ { f } : \mathbb { X } _ { f } \to \mathbb { U }$ with the following four properties: (i)

$[ \Delta V _ { f } + \ell ] ( x , \kappa _ { f } ( x ) , w ) \leq 0$ for all $x \in \mathbb { X } _ { f }$ , all $w \in \mathbb { W }$ , (ii) $\mathbb { X } _ { f }$ is robust positive invariant for $x ^ { + } = f ( x , \kappa _ { f } ( x ) , w )$ , (iii) $\mathbb { X } _ { f } \subseteq \mathbb { X }$ , and (iv) $\kappa _ { f } ( \mathbb { X } _ { f } ) \subseteq \mathbb { U }$ .

Theorem 3.10 (Recursive feasibility of control policies). Suppose Assumptions 3.8 and 3.9 hold. Then:

$( a ) \ : \mathcal { X } _ { N } \supseteq \mathcal { X } _ { N - 1 } \supseteq \ldots \supseteq \mathcal { X } _ { 1 } \supseteq \mathcal { X } _ { 0 } = \mathbb { X } _ { f } .$   
(b) $x _ { i }$ is robust control invariant for $\pmb { x } ^ { + } = f ( x , u , w ) ~ \forall i \in \{ 0 , 1 , \ldots , N \}$ .   
(c) $x _ { i }$ is robust positive invariant for $x ^ { + } = f ( x , \kappa _ { i } ( x ) , w ) \quad \forall i \in \{ 0 , 1$ , $\dots , N \}$ .

$( d ) V _ { i } ^ { 0 } ( x ) \leq V _ { i - 1 } ^ { 0 } ( x ) \quad \forall x \in \mathcal { X } _ { i - 1 } \quad \forall i \in \{ 1 , \ldots , N \} .$

$\begin{array} { r } { ( e ) V _ { N } ^ { 0 } ( x ) \leq V _ { f } ( x ) \quad \forall x \in X _ { f } . } \end{array}$

$\begin{array} { r l } & { ( f ) [ \Delta V _ { N } ^ { 0 } + \ell ] ( x , \kappa _ { N } ( x ) , w ) \leq [ V _ { N } ^ { 0 } - V _ { N - 1 } ^ { 0 } ] ( f ( x , \kappa _ { N } ( x ) , w ) ) \leq 0 } \\ & { \forall ( x , w ) \in \mathcal { X } _ { N } \times \mathbb { W } . } \end{array}$

(g) For any x $\mathbf { \xi } : \in \mathcal { X } _ { N } , \{ \kappa _ { N } ( x ) , \kappa _ { N - 1 } ( \cdot ) , \ldots , \kappa _ { 1 } ( \cdot ) , \kappa _ { f } ( \cdot ) \}$ is a feasible policy $f o r \mathbb { P } _ { N + 1 } ( x )$ , and, for any x ∈ XN−1, {κN−1(x), κN−2(·), . . . , κ1(·), κf (·)} is a feasible policy for $\mathbb { P } _ { N } ( x )$ .
