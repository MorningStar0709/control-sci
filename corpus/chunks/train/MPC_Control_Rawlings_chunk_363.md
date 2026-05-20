Assumption 3.4 is satisfied, as shown in Proposition 7.13, if $f ( \cdot )$ is affine, $\ell ( \cdot )$ and $V _ { f } ( \cdot )$ are quadratic and positive definite, X is polyhedral, and $\mathbb { X } _ { f }$ and U are polytopic. Assumption 3.4 is also satisfied, as shown in Theorem C.29, if $V _ { N } ( \cdot )$ is Lipschitz continuous on bounded sets, U is compact, and there are no state constraints, i.e., if $\mathbb { X } = \mathbb { X } _ { f } = \mathbb { R } ^ { n }$ . It follows from (3.11) and (3.12) that for the nominal system under MPC, the origin is exponentially stable, with a region of attraction $x _ { N }$ ; the nominal system under MPC satisfies

$$x ^ {+} = \bar {f} (x, \kappa_ {N} (x)) \tag {3.13}$$

It also follows that there exists a $ { \boldsymbol { \gamma } } \in ( 0 , 1 )$ such that

$$V _ {N} ^ {0} (\bar {f} (x, \kappa_ {N} (x))) \leq \gamma V _ {N} ^ {0} (x)$$

for all $\boldsymbol { x } \in \mathcal { X } _ { N }$ so that $V _ { N } ^ { 0 } ( x ( i ) )$ decays exponentially to zero as $i  \infty$ , where $x ( i )$ is the state of the controlled system at time i when there is no disturbance. In fact, $V _ { N } ^ { 0 } ( x ( i ) ) \le \gamma ^ { i } V _ { N } ^ { 0 } ( x ( 0 ) )$ ) for all $i \in \mathbb { I } _ { \geq 0 }$ .

We now examine the consequences of applying the nominal model predictive controller $\kappa _ { N } ( \cdot )$ to the uncertain system (3.7). The controlled uncertain system satisfies the difference equation

$$x ^ {+} = f (x, \kappa_ {N} (x), w) \tag {3.14}$$

in which w can take any value in W. It is obvious that the state $x ( i )$ of the controlled system (3.14) cannot tend to the origin as $i  \infty$ ; the best that can be hoped for is that $x ( i )$ tends to and remains in some neighborhood of the origin. We shall establish this, if the disturbance w is sufficiently small, using the value function $V _ { N } ^ { 0 } ( \cdot )$ of the nominal optimal control problem as an input-to-state stable (ISS) Lyapunov function for the controlled uncertain system (3.14). As before, $V _ { N } ^ { 0 } ( \cdot )$ satisfies (3.11) and (3.12). Let

$$R _ {c} := \operatorname{lev} _ {c} V _ {N} ^ {0} = \{x \mid V _ {N} ^ {0} (x) \leq c \}$$
