where $x ^ { 0 } ( 0 ; x ) = x , x ^ { 0 } ( 1 ; x ) = f ( x , \kappa _ { N } ( x ) )$ and $x ^ { 0 } ( N ; x ) \in \mathbb { X } _ { f }$ . At the successor state $x ^ { + } = x ^ { 0 } ( 1 ; x )$ , we choose, as before, the nonoptimal control sequence u defined by

$$\tilde {\mathbf {u}} := \{u ^ {0} (1; x), \dots , u ^ {0} (N - 1; x), u \}$$

where u is still to be chosen. The resultant state sequence is

$$\widetilde {\mathbf {x}} = \{x ^ {0} (1; x), \dots , x ^ {0} (N; x), f (x ^ {0} (N; x), u) \}$$

The control sequence $\tilde { u } ( \cdot )$ is feasible, but not necessarily optimal, for $\mathbb { P } _ { N } ( x ^ { 0 } ( 1 ; x ) )$ ) provided that $f ( x ^ { 0 } ( N ; x ) , u ) \in \mathbb { X } _ { f }$ . We obtain as before

$$V _ {N} ^ {0} (f (x, \kappa_ {N} (x))) \leq V _ {N} ^ {0} (x) - \ell (x, \kappa_ {N} (x))$$

provided now that for all $\boldsymbol { x } \in \mathbb { X } _ { f }$ , there exists a $u \in \mathbb { U }$ such that

$$V _ {f} (f (x, u)) \leq V _ {f} (x) - \ell (x, u), \mathrm{and} f (x, u) \in \mathbb {X} _ {f}$$

which is true by Assumptions 2.12 and 2.13.

Lemma 2.14 holds if U is closed but not necessarily bounded and can be used, with suitable assumptions on $\ell ( \cdot )$ , to establish asymptotic stability of the origin. The descent property established in Lemma 2.14 may be established also using a monotonicity property of the value function.
