# Proof.

(a)–(c) Suppose, for some $i , x _ { i }$ is robust control invariant so that any point $x \in \mathcal X _ { i }$ can be robustly steered into $x _ { i }$ . By construction, $\boldsymbol { \mathcal { X } } _ { i + 1 }$ is the set of all points x that can be robustly steered into $x _ { i }$ . Hence $\mathcal { X } _ { i + 1 } \supseteq \mathcal { X } _ { i }$ and $\boldsymbol { \mathcal { X } } _ { i + 1 }$ is robust control invariant. But $\boldsymbol { \mathcal { X } } _ { 0 } = \mathbb { X } _ { f }$ is robust control invariant. Both (a) and (b) follow by induction. Part (c) follows from (b).

(d) Assume $V _ { i } ^ { 0 } ( x ) \leq V _ { i - 1 } ^ { 0 } ( x )$ for all $x \in \mathcal { X } _ { i - 1 }$ . Then from (3.20) we have

$$
\begin{array}{l} \left[ V _ {i + 1} ^ {0} - V _ {i} ^ {0} \right] (x) = \max _ {w \in \mathbb {W}} \left\{\ell \left(x, \kappa_ {i + 1} (x), w\right) + V _ {i} ^ {0} \left(f \left(x, \kappa_ {i + 1} (x), w\right)\right) \right\} \\ - \max _ {w \in \mathbb {W}} \{\ell (x, \kappa_ {i} (x), w) + V _ {i - 1} ^ {0} (f (x, \kappa_ {i} (x), w)) \} \\ \leq \max _ {w \in \mathbb {W}} \left\{\ell \left(x, \kappa_ {i} (x), w\right) + V _ {i} ^ {0} \left(f \left(x, \kappa_ {i} (x), w\right)\right) \right\} \\ - \max _ {w \in \mathbb {W}} \{\ell (x, \kappa_ {i} (x), w) + V _ {i - 1} ^ {0} (f (x, \kappa_ {i} (x), w)) \} \\ \end{array}
$$

for all $x \in { \mathcal { X } } _ { i }$ since $\kappa _ { i } ( \cdot )$ may not be optimal for problem $\mathbb { P } _ { i + 1 } ( x )$ . We now use the fact that max $\begin{array} { r } { _ w \{ a ( w ) \} - \operatorname* { m a x } _ { w } { \{ b ( w ) \} } \ \leq \ \operatorname* { m a x } _ { w } { \{ a ( w ) \ - } \quad }  \end{array}$ $b ( w ) \}$ }, which is discussed in Exercise 3.2, to obtain

$$[ V _ {i + 1} ^ {0} - V _ {i} ^ {0} ] (x) \leq \max _ {w \in \mathbb {W}} \{[ V _ {i} ^ {0} - V _ {i - 1} ^ {0} ] (f (x, \kappa_ {i} (x), w)) \}$$

for all $( x , w ) \in X _ { i } \times \mathbb { W }$ . Also, for all $x \in \mathcal { X } _ { 0 } = \mathbb { X } _ { f }$ ,

$$
\begin{array}{l} [ V _ {1} ^ {0} - V _ {0} ^ {0} ] (x) = \min _ {u \in \mathbb {U}} \max _ {w \in \mathbb {W}} \{\ell (x, u, w) + V _ {f} (f (x, u, w)) - V _ {f} (x) \} \\ = \min _ {u \in \mathbb {U}} \max _ {w \in \mathbb {W}} [ \Delta V _ {f} + \ell ] (x, u, w) \\ \leq 0 \\ \end{array}
$$

in which the last inequality follows from Assumption 3.8. By induction, $V _ { i } ^ { 0 } ( x ) \le V _ { i - 1 } ^ { 0 } ( x ) \ \forall x \in \mathcal { X } _ { i - 1 } , \ \forall i \in \{ 1 , \ldots , N \}$ ; this is the monotonicity property of the value function for a constrained min-max optimal control problem.

(e) This result is a direct consequence of (a) and (d).
