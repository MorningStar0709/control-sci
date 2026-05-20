# Exercise B.4: A converse theorem for asymptotic stability

Show that if the origin is globally asymptotically stable (GAS) for the system

$$x ^ {+} = f (x)$$

Then there exists a Lyapunov function $V ( \cdot )$ for the system satisfying for all $\boldsymbol { x } \in \mathbb { R } ^ { n }$

$$\alpha_ {1} (| x |) \leq V (x) \leq \alpha_ {2} (| x |)V (f (x)) - V (x) \leq - \alpha_ {3} (| x |)$$

in which $\alpha _ { 1 } ( \cdot ) , \alpha _ { 2 } ( \cdot ) , \alpha _ { 3 } ( \cdot ) \in \mathcal { K } _ { \infty }$

Hint: use the following result due to Sontag (1998b, Proposition 7) and the approach of Exercise B.3.

Proposition B.50 (Improving convergence (Sontag (1998b))). Assume that $\beta ( \cdot ) \in \mathcal { K L }$ Then there exists $\theta _ { 1 } ( \cdot ) , \theta _ { 2 } ( \cdot ) \in \mathcal { K } _ { \infty }$ so that

$$\beta (s, t) \leq \theta_ {1} (\theta_ {2} (s) e ^ {- t}) \quad \forall s \geq 0, \quad \forall t \geq 0 \tag {B.18}$$
