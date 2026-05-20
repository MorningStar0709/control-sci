Theorem A.25 (Second derivative and convexity). Suppose that $f :$ $\mathbb { R } ^ { n } \to \mathbb { R }$ is twice continuously differentiable. Then f is convex if and only if the Hessian (second derivative) matrix $\partial ^ { 2 } f ( x ) / \partial x ^ { 2 }$ is positive semidefinite for all $x \in \mathbb { R } ^ { n } , i . e . , \left. y , \partial ^ { 2 } f ( x ) / \partial x ^ { 2 } y \right. \geq 0$ for all $x , y \in \mathbb { R } ^ { n }$ .

Proof. ⇒ Suppose f is convex. Then for any $x , y \in \mathbb { R } ^ { n }$ , because of Theorem A.24 and Proposition A.11

$$
\begin{array}{l} 0 \leq f (y) - f (x) - \left\langle \nabla f (x), y - x \right\rangle \\ = \int_ {0} ^ {1} (1 - s) \left\langle y - x, \frac {\partial^ {2} f (x + s (y - x))}{\partial x ^ {2}} (y - x) \right\rangle d s \tag {A.11} \\ \end{array}
$$

Hence, dividing by $\vert y - x \vert ^ { 2 }$ and letting $y  x$ , we obtain that $\partial ^ { 2 } f ( x ) / \partial x ^ { 2 }$ is positive semidefinite.

⇐ Suppose that $\partial ^ { 2 } f ( x ) / \partial x ^ { 2 }$ is positive semidefinite for all $x \in \mathbb { R }$ . Then it follows directly from the equality in (A.11) and Theorem A.24 that $f$ is convex.

Definition A.26 (Level set). Suppose $f : \mathbb { R } ^ { n }  \mathbb { R }$ . A level set of f is a set of the form $\{ x \mid f ( x ) = \alpha \} , \alpha \in \mathbb { R }$ .

Definition A.27 (Sublevel set). Suppose $f : \mathbb { R } ^ { n }  \mathbb { R }$ . A sublevel set X of f is a set of the form $\mathbb { X } = \{ x \mid f ( x ) \leq \alpha \} , \alpha \in \mathbb { R }$ . We also write the sublevel set as ${ \mathbb X } = \mathrm { l e v } _ { \alpha } f$ .

Definition A.28 (Support function). Suppose $Q \subset \mathbb { R } ^ { n }$ . The support function $\sigma _ { Q } : \mathbb { R } ^ { n }  \mathbb { R } _ { e } = \mathbb { R } \cup \{ + \infty \}$ is defined by:

$$\sigma_ {Q} (p) = \sup _ {x} \{\langle p, x \rangle \mid x \in Q \}$$

$\sigma _ { Q } ( \boldsymbol { p } )$ measures how far Q extends in direction $p .$ .

Proposition A.29 (Set membership and support function). Suppose $Q \subset$ $\mathbb { R } ^ { n }$ is a closed and convex set. Then $x \in Q$ if and only if $\ ' \sigma _ { Q } ( p ) \geq \left. p , x \right.$ for all $\boldsymbol { p } \in \mathbb { R } ^ { n }$

Proposition A.30 (Lipschitz continuity of support function). Suppose $Q \subset \mathbb { R } ^ { n }$ is bounded. Then $\sigma _ { Q }$ is bounded and Lipschitz continuous $| \sigma _ { Q } ( p ) - \sigma _ { Q } ( q ) | \leq K | p - q |$ for all p, $q \in \mathbb { R } ^ { n }$ , where $K : = \operatorname* { s u p } \{ | x | | x \in$ $Q \} < \infty$ .
