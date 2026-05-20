Consider now the problem $\mathbb { P } _ { N } ^ { \mathrm { u c } } ( x )$ defined in the same way as $\mathbb { P } _ { N } ( x )$ except that all constraints are omitted so that $\mathcal { U } _ { N } ( x ) = \mathbb { R } ^ { N m }$

$$\mathbb {P} _ {N} ^ {\mathrm{uc}} (x): \quad V _ {N} ^ {\mathrm{uc}} (x) = \min _ {\mathbf {u}} V _ {N} (x, \mathbf {u})$$

in which $V _ { N } ( \cdot )$ is defined as previously by

$$V _ {N} (x, \mathbf {u}) := \sum_ {i = 0} ^ {N - 1} \ell (x (i), u (i)) + V _ {f} (x (N))$$

with $V _ { f } ( \cdot )$ the value function for the infinite horizon unconstrained optimal control problem, i.e., $V _ { f } ( x ) \ : = \ V _ { \infty } ^ { \mathrm { u c } } ( x ) \ = \ ( 1 / 2 ) x ^ { \prime } P x$ . With these definitions, it follows that

$$
\begin{array}{l} V _ {N} ^ {\mathrm{uc}} (x) = V _ {\infty} ^ {\mathrm{uc}} (x) = V _ {f} (x) = (1 / 2) x ^ {\prime} P x \\ \kappa_ {N} ^ {\mathrm{uc}} (x) = K x, \quad K = - (B ^ {\prime} P B + R) ^ {- 1} B ^ {\prime} P A \\ \end{array}
$$

for all $x \in \mathbb { R } ^ { n } ; u = K x$ is the optimal controller for the unconstrained infinite horizon problem. But $\mathbb { X } _ { f }$ is positive invariant for $x ^ { + } = A _ { K } x$ .

We now claim that with $V _ { f } ( \cdot )$ chosen to equal to $V _ { \infty } ^ { \mathrm { { u c } } } ( \cdot )$ , the terminal constraint set $\mathbb { X } _ { f }$ is positive invariant for $x ^ { + } = A x + B \kappa _ { N } ( x )$ . We do this by showing that $V _ { N } ^ { 0 } ( x ) = V _ { N } ^ { \mathrm { u c } } ( x ) = V _ { \infty } ^ { \mathrm { u c } } ( x )$ for all $x \in \mathbb { X } _ { f }$ , so that the associated control laws are the same, i.e., $\begin{array} { r } { \kappa _ { N } ( x ) = K x } \end{array}$ . First, because $\mathbb { P } _ { N } ^ { \mathrm { u c } } ( x )$ is identical with $\mathbb { P } _ { N } ( x )$ except for the absence of all constraints, we have

$$V _ {N} ^ {\mathrm{uc}} (x) = V _ {f} (x) \leq V _ {N} ^ {0} (x) \quad \forall x \in \mathcal {X} _ {N} \supseteq \mathbb {X} _ {f}$$

Second, from Lemma 2.15,

$$V _ {N} ^ {0} (x) \leq V _ {f} (x) \quad \forall x \in \mathbb {X} _ {f}$$

Hence $V _ { N } ^ { 0 } ( x ) = V _ { N } ^ { \mathrm { u c } } ( x ) = V _ { f } ( x )$ for all $\boldsymbol { x } \in \mathbb { X } _ { f }$ . That $\begin{array} { r } { \kappa _ { N } ( x ) = K x } \end{array}$ for all $x \in \mathbb { X } _ { f }$ follows from the uniqueness of the solutions to the problems $\mathbb { P } _ { N } ( x )$ and $\mathbb { P } _ { N } ^ { \mathrm { u c } } ( x )$ . Summarizing, we have:

If $V _ { f } ( \cdot )$ is chosen to be the value function for the unconstrained infinite horizon optimal control problem, if $u \ =$ $K x$ is the associated controller, and if $\mathbb { X } _ { f }$ is invariant for $x ^ { + } = A _ { K } x$ , then $\mathbb { X } _ { f }$ is also positive invariant for the controlled system $x ^ { + } = A x + B \kappa _ { N } ( x )$ . Also $\begin{array} { r } { \kappa _ { N } ( x ) = K x } \end{array}$ for all $\boldsymbol { x } \in \mathbb { X } _ { f }$ .
