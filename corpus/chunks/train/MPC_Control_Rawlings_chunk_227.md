# 2.4.3 Stabilizing Conditions: Constrained Problems

In this section we consider the case when state and control constraints (2.2) are present. MPC is stabilizing if a global CLF is employed as the terminal cost. A global CLF is seldom available, however, either because the system is nonlinear or because constraints are present. Hence, we must set our sights lower and employ as our terminal cost function $V _ { f } ( \cdot )$ , a local CLF, one that is defined only on a neighborhood $\mathbb { X } _ { f }$ of the origin where $\mathbb { X } _ { f } \subseteq \mathbb { X }$ . A consequent requirement is that the terminal state must be constrained, explicitly or implicitly, to lie in $\mathbb { X } _ { f }$ . Our stabilizing condition now takes the form:

Assumption 2.12 (Basic stability assumption).

$$\min _ {u \in \mathbb {U}} \left\{V _ {f} (f (x, u)) + \ell (x, u) \mid f (x, u) \in \mathbb {X} _ {f} \right\} \leq V _ {f} (x), \forall x \in \mathbb {X} _ {f}$$

This assumption implicitly requires that for each $x \in \mathbb { X } _ { f }$ , there exists a $u \in \mathbb { V }$ such that $f ( x , u ) \in \mathbb { X } _ { f }$ , i.e., Assumption 2.12 implies the following assumption.

Assumption 2.13 (Implied invariance assumption). The set $\mathbb { X } _ { f }$ is control invariant for the system $x ^ { + } = f ( x , u )$ .

Assumptions 2.12 and 2.13 specify properties which, if possessed by the terminal cost function and terminal constraint set, enable us to employ the value function $V _ { N } ^ { 0 } ( \cdot )$ for the optimal control problem $\mathbb { P } _ { N }$ as a Lyapunov function. The important descent and monotonicity properties of $V _ { N } ^ { 0 } ( \cdot )$ are established in Lemmas 2.14 and 2.15.

Lemma 2.14 (Optimal cost decrease). Suppose, as usual, that Assumptions 2.2 and 2.3 hold, and that Assumptions 2.12 (and 2.13) hold. Then

$$V _ {N} ^ {0} (f (x, \kappa_ {N} (x))) \leq V _ {N} ^ {0} (x) - \ell (x, \kappa_ {N} (x))$$

for all $\boldsymbol { x } \in \mathcal { X } _ { N }$ .

Proof. Let x be any point in $x _ { N }$ . Then $V _ { N } ^ { 0 } ( x ) = V _ { N } ( x , { \bf u } ^ { 0 } ( x ) )$ where

$$\mathbf {u} ^ {0} (x) = \{u ^ {0} (0; x), u ^ {0} (1; x), \dots , u ^ {0} (N - 1; x) \}$$

and $u ^ { 0 } ( 0 ; x ) = \kappa _ { N } ( x )$ ; the control sequence is feasible for $\mathbb { P } _ { N } ( x )$ because it satisfies all control, state, and terminal constraints. The corresponding state sequence is

$$\mathbf {x} ^ {0} (x) = \{x ^ {0} (0; x), x ^ {0} (1; x), \dots , x ^ {0} (N; x) \}$$
