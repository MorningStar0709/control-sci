be the largest sublevel set of $V _ { N } ^ { 0 } ( \cdot )$ contained in $\chi _ { N } ;$ ; the set $R _ { c }$ is compact. Hence there exists a finite Lipschitz constant d for $V _ { N } ^ { 0 } ( \cdot )$ in $R _ { c } \times \mathbb { W }$ . Since $R _ { c } \subset \mathcal { X } _ { N }$ , the state constraint $x \in \mathbb { X }$ is satisfied everywhere in $R _ { c }$ . Because the uncertain system satisfies (3.14) rather than (3.13), the value function evolves along trajectories of the uncertain system according to

$$V _ {N} ^ {0} (f (x, \kappa_ {N} (x), w)) - V _ {N} ^ {0} (x) \leq V _ {N} ^ {0} (\bar {f} (x, \kappa_ {N} (x))) - V _ {N} ^ {0} (x) + d | w |$$

for all $w \in \mathbb { W } , \operatorname { i . e . }$ , according to

$$V _ {N} ^ {0} (f (x, \kappa_ {N} (x), w)) \leq \gamma V _ {N} ^ {0} (x) + d | w | \tag {3.15}$$

where $ { \boldsymbol { \gamma } } \in ( 0 , 1 )$ . In contrast to the nominal case, the value function does not necessarily decrease along trajectories of the uncertain system; indeed, at the origin $( x ~ = ~ 0 )$ , the value function increases unless $w = 0$ . The origin is not asymptotically stable for the uncertain system. If W is sufficiently small, however, a sublevel set $R _ { b } \ = \ \{ { \boldsymbol { x } } \ |$ $V _ { N } ^ { 0 } ( x ) \le b \} \subset R _ { c }$ of $V _ { N } ^ { 0 } ( \cdot )$ satisfying $b < c$ is robust positive invariant for $x ^ { + } \ = \ f ( x , \kappa _ { N } ( x ) , w ) , w \in \mathbb { W }$ , which we show next. We assume, therefore,

Assumption 3.5 (Restricted disturbances). Let $e : = \operatorname* { m a x } _ { w } \{ | w | \ | \ w \in$ $\mathbb { W } \} ; e \le ( \rho - \gamma ) b / d$ for some $\rho \in ( \gamma , 1 )$ .

The first consequence of this assumption is that $R _ { b }$ is robust positive invariant for $x ^ { + } = f ( x , \kappa _ { N } ( x ) , w ) , w \in \mathbb { W }$ . Suppose $x \in R _ { b }$ so that $V _ { N } ^ { 0 } ( x ) \le b$ . Then

$$V _ {N} ^ {0} (f (x, \kappa_ {N} (x), w)) \leq \gamma V _ {N} ^ {0} (x) + d | w | \leq \gamma b + (\rho - \gamma) b \leq \rho b$$

so that $x ^ { + } ~ \in ~ R _ { b }$ for all $w ~ \in ~ \mathbb { W }$ . A second consequence is that $R _ { c }$ is robust positive invariant and that any $x \in R _ { c } \ \backslash \ R _ { b }$ is steered by the controller into $R _ { b }$ in finite time since Assumption 3.5 implies $V _ { N } ^ { 0 } ( x ^ { + } ) \leq$ $\rho V _ { N } ^ { 0 } ( x )$ for all $x ^ { + } = f ( x , \kappa _ { N } ( x ) , w )$ , all $x \in R _ { c } \ \backslash \ R _ { b }$ , all $w \in \mathbb { W }$ . Any trajectory with an initial state x in $R _ { c }$ remains in $R _ { c }$ and enters, in finite time, the set $R _ { b }$ where it then remains.
