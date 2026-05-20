# 7.6 DP Solution of the Constrained LQ Control Problem

A disadvantage in the procedure described in Section 7.4 for determining the piecewise affine receding horizon control law is the dimension Nm of the decision variable u. It seems natural to inquire whether or not DP, which replaces a multistage decision problem by a sequence of relatively simple single-stage problems, provides a simpler solution. We answer this question by showing how DP may be used to solve the constrained linear quadratic (LQ) problem discussed in Section 7.4. For all $j \in \mathbb { I } _ { 1 : N }$ , let $V _ { j } ^ { 0 } ( \cdot )$ , the optimal value function at time-to-go j, be defined by

$$V _ {j} ^ {0} (x) := \min _ {u} \left\{V _ {j} (x, u) \mid (x, \mathbf {u}) \in \mathbb {Z} _ {j} \right\}V _ {j} (x, \mathbf {u}) := \sum_ {i = 0} ^ {j - 1} \ell (x (i), u (i)) + V _ {f} (x (j))\mathbb {Z} _ {j} := \{(x, \mathbf {u}) \mid x (i) \in \mathbb {X}, u (i) \in \mathbb {U}, i \in \mathbb {I} _ {0: j - 1}, x (j) \in \mathbb {X} _ {f} \}$$

with $x ( i ) : = \phi ( i ; x , { \bf u } ) ; V _ { j } ^ { 0 } ( \cdot )$ is the value function for $\mathbb { P } _ { j } ( x )$ . As shown in Chapter 2, the constrained DP recursion is

$$V _ {j + 1} ^ {0} (x) = \min _ {u} \left\{\ell (x, u) + V _ {j} ^ {0} (f (x, u)) \mid u \in \mathbb {U}, f (x, u) \in \mathcal {X} _ {j} \right\} \tag {7.18}\mathcal {X} _ {j + 1} = \{x \in \mathbb {X} \mid \exists u \in \mathbb {U} \text {such that} f (x, u) \in \mathcal {X} _ {j} \} \tag {7.19}$$

where $f ( x , u ) : = A x + B u$ with boundary condition

$$V _ {0} ^ {0} (\cdot) = V _ {f} (\cdot), \quad \mathcal {X} _ {0} = \mathbb {X} _ {f}$$

The minimizer of (7.18) is $\kappa _ { j + 1 } ( x )$ . In the equations, the subscript j denotes time to go, so that current time $i = N - j$ . For each $j , x _ { j }$ is the domain of the value function $V _ { j } ^ { 0 } ( \cdot )$ and of the control law $\kappa _ { j } ( \cdot )$ , and is the set of states that can be steered to the terminal set $\mathbb { X } _ { f }$ in j steps or less by an admissible control that satisfies the state and control constraints. The time-invariant receding horizon control law for horizon j is $\kappa _ { j } ( \cdot )$ whereas the optimal policy for problem $\mathbb { P } _ { j } ( x )$ is $\{ \kappa _ { j } ( \cdot ) , \kappa _ { j - 1 } ( \cdot ) , \ldots , \kappa _ { 1 } ( \cdot ) \}$ . The data of the problem are identical to the data in Section 7.4.
