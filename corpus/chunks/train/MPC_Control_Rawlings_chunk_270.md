# 2.6.1 Replacing the Terminal Constraint by a Terminal Cost

A reasonably simple procedure is to replace the terminal constraint $x ( N ) \in \mathbb { X } _ { f }$ by a terminal cost that is sufficiently large to ensure automatic satisfaction of the terminal constraint.

We assume, as in the examples of MPC discussed in Section 2.5, that the terminal cost function $V _ { f } ( \cdot )$ , the constraint set $\mathbb { X } _ { f }$ , and the stage cost $\ell ( \cdot )$ for the optimal control problem $\mathbb { P } _ { N } ( x )$ are chosen to satisfy Assumptions 2.12, 2.13 and 2.16 so that there exists a local control law $\kappa _ { f } : \mathbb { X } _ { f } \to \mathbb { U }$ such that $\mathbb { X } _ { f } \subseteq \{ x \in \mathbb { X } \mid \kappa _ { f } ( x ) \in \mathbb { U } \}$ is positive invariant for $x ^ { + } = f ( x , \kappa _ { f } ( x ) )$ and $V _ { f } ( f ( x , \kappa _ { f } ( x ) ) ) { + } \ell ( x , \kappa _ { f } ( x ) ) \leq V _ { f } ( x )$ for all $\boldsymbol { x } \in \mathbb { X } _ { f }$ . We assume that the function $V _ { f } ( \cdot )$ is defined on X even though it possesses the property $V _ { f } ( f ( x , \kappa _ { f } ( x ) ) ) + \ell ( x , \kappa _ { f } ( x ) ) \leq V _ { f } ( x )$ only in $\mathbb { X } _ { f }$ . In many cases, even if the system being controlled is nonlinear, $V _ { f } ( \cdot )$ is quadratic and positive definite, and $\kappa _ { f } ( \cdot )$ is linear. The set $\mathbb { X } _ { f }$ may be chosen to be a sublevel set of $V _ { f } ( \cdot )$ so that $\mathbb { X } _ { f } = W ( a ) : = \{ x \mid$ $V _ { f } ( x ) \leq a \}$ for some $\alpha > 0$ . We discuss in the sequel a modified form of the optimal control problem $\mathbb { P } _ { N } ( x )$ in which the terminal cost $V _ { f } ( \cdot )$ is replaced by $\beta V _ { f } ( \cdot )$ and the terminal constraint $\mathbb { X } _ { f }$ is omitted, and show that if $\beta$ is sufficiently large the solution of the modified optimal control problem is such that the optimal terminal state nevertheless lies in $\mathbb { X } _ { f }$ so that terminal constraint is implicitly satisfied.

For all $\beta \geq 1$ , let $\mathbb { P } _ { N } ^ { \beta } ( x )$ denote the modified optimal control problem defined by

$$\hat {V} _ {N} ^ {\beta} (x) = \min _ {\mathbf {u}} \{V _ {N} ^ {\beta} (x, \mathbf {u}) \mid \mathbf {u} \in \hat {\mathcal {U}} _ {N} (x) \}$$

in which the cost function to be minimized is now

$$V _ {N} ^ {\beta} (x, \mathbf {u}) := \sum_ {i = 0} ^ {N - 1} \ell (x (i), u (i)) + \beta V _ {f} (x (N))$$
