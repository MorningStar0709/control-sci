# 2.5.1.3 Nonlinear Systems

Generally, when the system is nonlinear, albeit unconstrained, it is difficult to obtain a global CLF. We next present two forms of MPC. In the first, which is the simplest, the target set is the origin $\mathbb { X } _ { f } ~ = ~ \{ 0 \}$ . In the second, $\mathbb { X } _ { f }$ is a positive invariant ellipsoidal set for the system with linear control based on the linearization of the nonlinear system at the origin. The system to be controlled is

$$x ^ {+} = f (x, u)$$

in which $f ( \cdot )$ is continuous. The cost function $V _ { N } ( \cdot )$ is defined as before by

$$V _ {N} (x, \mathbf {u}) = \sum_ {i = 0} ^ {N - 1} \ell (x (i), u (i)) + V _ {f} (x (N))$$

where, for each $i , x ( i ) : = \phi ( i ; x , { \bf u } )$ , the solution of $x ^ { + } = f ( x , u )$ at time i if the initial state is x at time 0 and the control is u. Unless $V _ { f } ( \cdot )$ is a global CLF, a terminal constraint set $\mathbb { X } _ { f }$ is required, so the optimal control problem solved online is

$$\mathbb {P} _ {N} (x): \quad V _ {N} ^ {0} (x) = \min _ {\mathbf {u}} \left\{V _ {N} (x, \mathbf {u}) \mid \mathbf {u} \in \mathcal {U} _ {N} (x) \right\}$$

in which, in the absence of state and control constraints,

$$\mathcal {U} _ {N} (x) := \{\mathbf {u} \mid \phi (N; x, \mathbf {u}) \in \mathbb {X} _ {f} \}$$

Problem $\mathbb { P } _ { N } ( x )$ is an unconstrained nonlinear parametric program so that global solutions are not usually possible. We ignore this difficulty here and assume in this section that the global solution for any x may be computed online. We address the problem when this is not possible in Section 2.8.

Case 1. $\mathbb { X } _ { f } = \{ 0 \} , V _ { f } ( 0 ) = 0$ . This is the simplest case. As before, we note that Assumptions 2.12 and 2.13 hold if the origin is an equilibrium point, i.e., if $f ( 0 , 0 ) = 0$ . If, in addition, we assume that $\ell ( \cdot )$ satisfies Assumption 2.16(a), namely that there exists a $\mathcal { K } _ { \infty }$ function $\alpha _ { 1 } ( \cdot )$ such that $\ell ( \cdot )$ satisfies $\ell ( x , u ) \geq \alpha _ { 1 } ( | x | )$ for all $( x , u ) \in \mathbb { R } ^ { n } \times \mathbb { R } ^ { m }$ , then, for all $\boldsymbol { x } \in \mathcal { X } _ { N }$

$$
\begin{array}{l} V _ {N} ^ {0} (x) \geq \ell (x, \kappa_ {N} (x)) \geq \alpha_ {1} (| x |) \\ V _ {N} ^ {0} (f (x, \kappa_ {N} (x))) - V _ {N} ^ {0} (x) \leq - \ell (x, \kappa_ {N} (x)) \leq - \alpha_ {1} (| x |) \\ \end{array}
$$

where the latter inequality is a consequence of Lemma 2.14. If we also assume the controllability Assumption 2.23 is satisfied, then
