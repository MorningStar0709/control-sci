# Example 2: Difference between asymptotic stability definitions (Teel)

Consider the discontinuous nonlinear scalar example $x ^ { + } = f ( x )$ with

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{2} x & | x | \in [ 0, 1 ] \\ \frac {2 x}{2 - | x |} & | x | \in (1, 2) \\ 0 & | x | \in [ 2, \infty) \end{array} \right.
$$

The origin is attractive for all $x ( 0 ) \in \mathbb { R }$ , which can be demonstrated as follows. For $| x ( 0 ) | \in [ 0 , 1 ] , | x ( k ) | \le ( 1 / 2 ) ^ { k } | x ( 0 ) |$ . For $| x ( 0 ) | \in ( 1 , 2 ) , | x ( 1 ) | \geq 2$ which implies that $| x ( 2 ) | = 0 ;$ and for | $x ( 0 ) | \in [ 2 , \infty ) , | x ( 1 ) | = 0$ . The origin is Lyapunov stable, because if $\delta \leq 1$ , then $| x ( 0 ) | \leq \delta$ implies $| x ( k ) | \leq \delta$ for all k. Therefore, the origin is asymptotically stable according to the classical definition.

But there is no KL function $\beta ( \cdot )$ such that the system meets the bound for all $x ( 0 ) \in \mathbb { R }$

$$| x (k) | \leq \beta (| x (0) |, k) \quad \forall k \in \mathbb {I} _ {\geq 0}$$

Indeed, for initial conditions $\left| x ( 0 ) \right|$ slightly less than 2, the trajectory $x ( k )$ becomes arbitrarily large (at $k = 1 )$ before converging to the origin. Therefore, the origin is not asymptotically stable according to the KL definition. -

Remark 10. Note that because of Proposition B.8, the function $f ( \cdot )$ must be chosen to be discontinuous in this example to demonstrate this difference.

Proposition 11 (Extending local upper bounding function). Suppose the function V (·) is defined on X, a closed subset $o f \mathbb { R } ^ { n }$ , and that $V ( x ) \leq \alpha ( | x | _ { \mathcal { A } } )$ for all $x \in \mathbb { X } _ { f }$ where $\mathbb { X } _ { f } \ \subseteq \ X$ and contains the set A in its interior. A necessary and sufficient condition for the existence of a ${ \mathcal K } _ { \infty }$ function $\beta ( \cdot )$ satisfying $V ( x ) \leq \beta ( | x | _ { \mathcal { A } } )$ for all $x \in X$ is that $V ( \cdot )$ is locally bounded on X, i.e., V (·) is bounded on every compact subset of X.
