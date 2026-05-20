# 5.3.4 Output MPC

Model predictive controllers can now be constructed as described in Chapter 3, which dealt with robust control when the state was known. There is an obvious difference in that we are now concerned with controlling xˆ whereas, in Chapter 3, our concern was control of x. We describe here the appropriate modification of the simple model predictive controller presented in Section 3.4.2. We adopt the same procedure of defining a nominal optimal control problem with tighter constraints than in the original problem. The solution to this problem defines the center of a tube in which solutions to the original system lie, and the tighter constraints in the nominal problem ensure that the original constraints are satisfied by the actual system.

The nominal system is described by

$$z ^ {+} = A z + B v \tag {5.19}$$

The nominal optimal control problem is the minimization of the cost function $\bar { V } _ { N } ( z , { \bf v } )$ where

$$\bar {V} _ {N} (z, \mathbf {v}) := \sum_ {k = 0} ^ {N - 1} \ell (z (k), v (k)) + V _ {f} (z (N)) \tag {5.20}$$

subject to satisfaction by the state and control sequences of (5.19) and the tighter constraints

$$z (i) \in \mathbb {Z} \subseteq \mathbb {X} \ominus \mathbb {\Gamma} \quad \mathbb {\Gamma} := \mathbb {S} \oplus \mathbb {\Sigma} \tag {5.21}\nu (i) \in \mathbb {V} \subseteq \mathbb {U} \ominus K \mathbb {S} \tag {5.22}$$

as well as a terminal constraint $z ( N ) \in \mathbb { Z } _ { f } \subseteq \mathbb { Z }$ . Notice that Γ appears in (5.21) whereas $\mathbb { S } ,$ the set in which $e = { \hat { x } } - z \operatorname { l i e s }$ , appears in (5.22); this differs from the case studied in Chapter 3 where the same set appears in both equations. The sets W and N are assumed to be sufficiently small to ensure the following condition.

Assumption 5.4 (Constraint bounds). $\mathbb { T } = \mathbb { S } \oplus \mathbb { Z } \subseteq \mathbb { X }$ and $K \mathbb { S } \subseteq \mathbb { U }$ .

If Assumption 5.4 holds, the sets on the right-hand side of (5.21) and (5.22) are not empty; it can be seen from their definitions that the sets Σ and $\mathbb { S }$ tend to the set {0} as W and N tend to the set {0} in the sense that $d _ { H } ( \mathbb { W } , \{ 0 \} ) \to 0$ and $d _ { H } ( \mathbb { N } , \{ 0 \} ) \to 0$ .
