Assumption 4.3 (Convergent disturbances). The sequence $( \boldsymbol { w } ( \boldsymbol { k } ) , \boldsymbol { \nu } ( \boldsymbol { k } ) )$ for $k \in \mathbb { I } _ { \geq 0 }$ are bounded and converge to zero as $k \to \infty$ .

Remark 4.4 (Summable disturbances). If the disturbances satisfy Assumption 4.3, then there exists a K-function $\gamma _ { w } ( \cdot )$ such that the disturbances are summable

$$\sum_ {i = 0} ^ {\infty} \gamma_ {w} \big (| (w (i), v (i)) | \big) \text { is bounded }$$

See Sontag (1998b, Proposition 7) for a statement and proof of this result.2

Given this class of disturbances, the estimator stage cost is chosen to satisfy the following property.

Assumption 4.5 (Positive definite stage cost). The initial state cost and stage costs are continuous functions and satisfy the following inequalities for all $x \in \mathbb { R } ^ { n } , w \in \mathbb { R } ^ { g }$ , and v in $\mathbb { R } ^ { p }$

$$\underline {{{{\gamma}}}} _ {x} (| x |) \leq \ell_ {x} (x) \quad \leq \gamma_ {x} (| x |) \tag {4.4}\underline {{y}} _ {w} (| (w, v) |) \leq \ell_ {i} (w, v) \leq \gamma_ {w} (| (w, v) |) \quad i \geq 0 \tag {4.5}$$

in which $\underline { { \gamma } } _ { x } , \underline { { \gamma } } _ { w } , \gamma _ { x } , \gamma _ { w } \in \mathcal { K } _ { \infty }$ and $\gamma _ { w }$ is defined in Remark 4.4.

Notice that if we change the class of disturbances affecting the system, we may also have to change the stage cost in the state estimator to satisfy $\ell _ { i } ( w , \nu ) \leq \gamma _ { w } ( | ( w , \nu ) | )$ in (4.5). The standard stage cost is the quadratic function, but slowly decaying disturbances in the data require “stronger” than quadratic stage costs to ensure summability. An interaction between anticipated disturbances affecting the system and choice of stage cost in the state estimator is hardly surprising, but Remark 4.4 and Assumption 4.5 make the requirements explicit.
