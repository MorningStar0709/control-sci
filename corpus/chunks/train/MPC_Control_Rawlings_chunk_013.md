# Proof.

Sufficiency. We assume that $V ( \cdot )$ is locally bounded and construct the function $\beta ( \cdot )$ . Because A lies in the interior of $\mathbb { X } _ { f }$ , there exists an $\alpha > 0$ such that $| x | _ { \mathcal { A } } \leq a$ implies $x \in \mathbb { X } _ { f }$ . For each $i \in \mathbb { I } _ { \geq 1 }$ , let $S _ { i } \stackrel {  } { = } \{ x \ | \ | x | _ { \mathcal { A } } \leq i a \}$ . We define a sequence of numbers $\{ \alpha _ { i } \}$ as follows

$$\alpha_ {i} := \sup _ {S _ {i} \cap X} V (x) + \alpha (a) + i$$

Since $S _ { i }$ is compact for each i and X is closed, their intersection is a compact subset of X and the values $\alpha _ { i }$ exist for all $i \in \mathbb { I } _ { \geq 1 }$ because $V ( \cdot )$ is bounded on every compact subset of X. The sequence $\{ \alpha _ { i } \}$ is strictly increasing. For each $i \in \mathbb { I } _ { \geq 1 }$ , let the interpolating function $\phi _ { i } ( \cdot )$ be defined by

$$\phi_ {i} (s) := (s - i a) / a \quad s \in [ i a, (i + 1) a ]$$

Note that $\phi _ { i } ( i a ) = 0 , \phi _ { i } ( ( i + 1 ) a ) = 1$ , and that $\phi ( \cdot )$ is affine in [ia, $( i + 1 ) a ]$ . We can now define the function $\beta ( \cdot )$ as follows

$$
\beta (s) := \left\{ \begin{array}{l l} (\alpha_ {2} / \alpha (a)) \alpha (s) & s \in [ 0, a ] \\ \alpha_ {i + 1} + \phi_ {i} (s) (\alpha_ {i + 2} - \alpha_ {i + 1}) & s \in [ i a, (i + 1) a ] \text {   for   all   } i \in \mathbb {I} _ {\geq 1} \end{array} \right.
$$

It can be seen that $\beta ( 0 ) = 0 , \beta ( s ) \geq \alpha ( s )$ for $s \in [ 0 , a ]$ , that $\beta ( \cdot )$ is continuous, strictly increasing, and unbounded, and that $V ( x ) \leq \beta ( | x | _ { \mathcal { A } } )$ for all $x \in X$ . Hence we have established the existence of a $\mathcal { K } _ { \infty }$ function $\beta ( \cdot )$ such that $V ( x ) \leq \beta ( | x | _ { \mathcal { A } } )$ for all $x \in X$ .

Necessity. If we assume that $V ( \cdot )$ is not locally bounded, i.e., not bounded on some compact set $C \subseteq X ,$ , it follows immediately that there is no (continuous and, hence, locally bounded) ${ \mathcal K } _ { \infty }$ function $\beta ( \cdot )$ such that such that $V ( x ) \leq \beta ( x )$ for all $x \in C$ .

Note, however, that most of the Lyapunov function theorems appearing in $\mathrm { A p \cdot }$ pendix B also hold under the stronger KL definition of GAS. As an example, we provide a modified proof required for establishing Theorem B.11.
