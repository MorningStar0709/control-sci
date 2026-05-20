which is the set of control sequences such that the nominal system satisfies the control, state, and terminal constraints when the initial state at time 0 is x. Thus, $\mathcal { U } _ { N } ( x )$ is the set of feasible controls for the nominal optimal control problem $\mathbb { P } _ { N } ( x )$ . The set $\mathcal { X } _ { N } \subset \mathbb { R } ^ { n }$ , defined by

$$\mathcal {X} _ {N} := \{x \in \mathbb {X} \mid \mathcal {U} _ {N} (x) \neq \emptyset \}$$

is the domain of the value function $V _ { N } ^ { 0 } ( \cdot ) , \mathrm { i . e . }$ , the set of $x \in \mathbb { X }$ for which $\mathbb { P } _ { N } ( x )$ has a solution; $x _ { N }$ is also the domain of the minimizer $\mathbf { u } ^ { 0 } ( x )$ . The value of the nominal model predictive control at state x is $u ^ { 0 } ( 0 ; x )$ , the first control in the sequence $\mathbf { u } ^ { 0 } ( x )$ . Hence the implicit nominal MPC control law is $\kappa _ { N } : \mathcal { X } _ { N }  \mathbb { U }$ defined by

$$\kappa_ {N} (x) = u ^ {0} (0; x)$$

We assume, as before, that $\ell ( \cdot )$ and $V _ { f } ( \cdot )$ are defined by

$$\ell (x, u) := (1 / 2) \left(x ^ {\prime} Q x + u ^ {\prime} R u\right) \quad V _ {f} (x) := (1 / 2) x ^ {\prime} P _ {f} x$$

in which $Q , R ,$ , and $P _ { f }$ are all positive definite. We also assume that $V _ { f } ( \cdot )$ and $\mathbb { X } _ { f }$ satisfy the standard assumption that, for $x \in \mathbb { X } _ { f }$ , there exists a $u \in \mathbb { U }$ such that $V _ { f } ( \bar { f } ( x , u ) ) \le V _ { f } ( x ) - \ell ( x , u )$ and that $x _ { N }$ is compact. Under these assumptions, as shown in Chapter 2, there exist positive constants $c _ { 1 }$ and $c _ { 2 } , c _ { 2 } > c _ { 1 }$ , satisfying

$$c _ {1} | x | ^ {2} \leq V _ {N} ^ {0} (x) \leq c _ {2} | x | ^ {2} \tag {3.11}V _ {N} ^ {0} (\bar {f} (x, \kappa_ {N} (x))) \leq V _ {N} ^ {0} (x) - c _ {1} | x | ^ {2} \tag {3.12}$$

for all $\boldsymbol { x } \in \mathcal { X } _ { N }$ . We also assume:

Assumption 3.4 (Lipschitz continuity of value function). The value function $V _ { N } ^ { 0 } ( \cdot )$ is Lipschitz continuous on bounded sets.
