so that $x \notin \Gamma _ { N } ^ { \beta }$ . Hence $x \in \Gamma _ { N } ^ { \beta }$ implies ${ x ^ { \beta } } ( N ; x ) \in \mathbb { X } _ { f }$ . It then follows, since $\beta V _ { f } ( \cdot )$ and $\mathbb { X } _ { f }$ satisfy Assumptions 2.12 and 2.13, that the origin is asymptotically or exponentially stable for $x ^ { + } = f ( x , \kappa _ { N } ^ { \beta } ( x ) )$ with a region of attraction $\Gamma _ { N } ^ { \beta }$ . It also follows that $x \in \Gamma _ { N } ^ { \beta } ( x )$ implies

$$\hat {V} _ {N} ^ {\beta} (x ^ {\beta} (1; x)) \leq \hat {V} _ {N} ^ {\beta} (x) - \ell (x, \kappa_ {N} ^ {\beta} (x)) \leq \hat {V} _ {N} ^ {\beta} (x) \leq N d + \beta a$$

so that $x ^ { \beta } ( 1 ; x ) = f ( x , \kappa _ { N } ^ { \beta } ( x ) ) \in \Gamma _ { N } ^ { \beta }$ . Hence $\Gamma _ { N } ^ { \beta }$ is positive invariant for $x ^ { + } = f ( x , \kappa _ { N } ^ { \beta } ( x ) )$ .

Limon et al. (2006) then proceed to show that $\Gamma _ { N } ^ { \beta }$ increases with $\beta$ or, more precisely, that $\beta _ { 1 } \leq \beta _ { 2 }$ implies that $\Gamma _ { N } ^ { \beta _ { 1 } } \subseteq \Gamma _ { N } ^ { \beta _ { 2 } }$ . They also show that for any x steerable to the interior of $\mathbb { X } _ { f }$ by a feasible control, there exists $\mathtt { a } \beta$ such that $\boldsymbol { x } \in \Gamma _ { N } ^ { \beta }$ .

An attractive alternative is described by Hu and Linnemann (2002) who merely require that the state and control constraint sets, X and U respectively, are closed. Their approach uses, as usual, a terminal cost function $V _ { f } : \mathbb { X } _ { f } \to \mathbb { R }$ , a terminal constraint set $\mathbb { X } _ { f }$ , and a stage cost $\ell ( \cdot )$ that satisfy Assumptions 2.12, 2.13, and 2.16. Let $\mathbb { X } _ { f }$ be a sublevel set of $V _ { f } ( \cdot )$ defined by

$$\mathbb {X} _ {f} := \{x \in \mathbb {X} \mid V _ {f} (x) \leq a \}$$

for some $\alpha > 0$ . Then the extended function $V _ { f } ^ { e } : \mathbb { R } ^ { n }  \mathbb { R }$ is defined by

$$
V _ {f} ^ {e} (x) := \left\{ \begin{array}{l l} V _ {f} (x) & x \in \mathbb {X} _ {f} \\ a & x \notin \mathbb {X} _ {f} \end{array} \right.
$$

The function $V _ { f } ^ { e } ( \cdot )$ is continuous but not continuously differentiable; we show later how the definition may be modified to ensure continuous differentiability, a desirable property for optimization algorithms. The optimization problem $\mathbb { P } _ { N } ^ { e } ( x )$ solved online is defined by

$$\hat {V} _ {N} ^ {e} (x) := \min _ {\mathbf {u}} \{V _ {N} ^ {e} (x, \mathbf {u}) \mid \mathbf {u} \in \hat {\mathcal {U}} _ {N} (x) \}$$
