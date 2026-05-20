and $x ( i ) : = \phi ( i ; ( x , 0 ) , { \bf u } )$ . Thus $\mathcal { U } ( x , 0 )$ is the set of admissible control sequences1 if the initial state is x at time 0. It follows from the continuity of $f ( \cdot )$ that for all $i \in \{ 0 , 1 , \ldots , N - 1 \}$ and all $x \in \mathbb { R } ^ { n }$ , $\mathbf { u } \ \mapsto \ \phi ( i ; ( x , 0 ) , \mathbf { u } )$ is continuous, $\mathbf { u } \ \mapsto \ V ( x , 0 , \mathbf { u } )$ is continuous and $\mathcal { U } ( x , 0 )$ is compact. Hence the minimum in (C.4) exists at all $x \in \{ x \in$ $\mathbb { R } ^ { n } \mid \mathcal { U } ( x , 0 ) \neq \emptyset \}$ .

DP embeds problem $\mathbb { P } ( x , 0 )$ for a given state x in a whole family of problems $P ( x , i )$ where, for each $( x , i )$ , problem $\mathbb { P } ( x , i )$ is defined by

$$V ^ {0} (x, i) = \min _ {\mathbf {u} ^ {i}} \left\{V (x, i, \mathbf {u} ^ {i}) \mid \mathbf {u} ^ {i} \in \mathcal {U} (x, i) \right\}$$

where

$$\mathbf {u} ^ {i} := \{u (i), u (i + 1), \dots , u (N - 1) \}V (x, i, \mathbf {u} ^ {i}) := V _ {f} (x (N)) + \sum_ {j = i} ^ {N - 1} \ell (x (j), u (j)) \tag {C.5}$$

and

$$
\begin{array}{l} \mathcal {U} (x, i) := \left\{\mathbf {u} ^ {i} \in \mathbb {R} ^ {(N - i) m} \mid (x (j), u (j)) \in \mathbb {Z}, j = i, i + 1, \dots , N - 1 \right. \\ x (N) \in \mathbb {X} _ {f} \} \quad (\mathrm{C.6}) \\ \end{array}
$$

In (C.5) and $( \mathrm { C . 6 } ) , x ( j ) = \phi ( j ; ( x , i ) , \mathbf { u } ^ { i } )$ , the solution at time j of (C.1) if the initial state is x at time i and the control sequence is $\mathbf { u } ^ { i }$ . For each i, X(i) denotes the domain of $V ^ { 0 } ( \cdot , i )$ and $\mathcal { U } ( \cdot , i )$ so that

$$X (i) = \{x \in \mathbb {R} ^ {n} \mid \mathcal {U} (x, i) \neq \emptyset \}. \tag {C.7}$$
