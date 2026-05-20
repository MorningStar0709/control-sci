# 2.9.1 No Uncertainty

We assume initially that there is no model error and no disturbance. The target state and associated steady-state control are obtained by minimizing $| \bar { u } | ^ { 2 }$ with respect to $( x , u )$ subject to the equality constraints

$$x = f (x, u)r = h (x)$$

and the inequality constraints $x \in \mathbb { X }$ and $u \in \mathbb { V }$ . We assume that a solution exists and denote the solution by $( \bar { x } ( r ) , \bar { u } ( r ) )$ ; this notation indicates the dependence of the target state and its associated control on the reference variable r . We require the dimension of r to be less than or equal to m, the dimension of u.

MPC may then be achieved by solving online the optimal control problem $\mathbb { P } _ { N } ( x , r )$ defined by

$$V _ {N} ^ {0} (x, r) = \min _ {\mathbf {u}} \left\{V _ {N} (x, r, \mathbf {u}) \mid \mathbf {u} \in \mathcal {U} _ {N} (x, r) \right\}$$

in which the cost function $V _ { N } ( \cdot )$ and the constraint set are defined by

$$V _ {N} (x, r, \mathbf {u}) := \sum_ {i = 0} ^ {N - 1} \ell (x (i) - \bar {x} (r), u (i) - \bar {u} (r)) + V _ {f} (x, r)\mathcal {U} _ {N} (x, r) := \{\mathbf {u} \mid x (i) \in \mathbb {X}, u (i) \in \mathbb {U}, \forall i \in \mathbb {I} _ {0: N - 1}; x (N) \in \mathbb {X} _ {f} (r) \}$$

In these definitions, $x ( i ) = \phi ( i ; x , { \bf u } )$ , the solution at time i of $x ^ { + } =$ $f ( x , u )$ if the initial state is x and the control sequence is u. Let ${ \bf u } ^ { 0 } ( x , r )$ denote the solution of $\mathbb { P } _ { N } ( x , r )$ . The MPC control law is $\kappa _ { N } ( x , r )$ , the first control in the sequence ${ \bf u } ^ { 0 } ( x , r )$ . The terminal cost function $V _ { f } ( \cdot , r )$ and constraint set $\mathbb { X } _ { f } ( r )$ must be chosen to satisfy suitably modified stabilizing conditions. Since both depend on r , the simplest option is to choose a terminal equality constraint so that

$$V _ {f} (\bar {x} (r), r) = 0 \quad \mathbb {X} _ {f} (r) = \{\bar {x} (r) \} \subset \mathbb {X}$$

If the system is linear, i.e., if $x ^ { + } = A x + B u$ , an alternative choice is

$$V _ {f} (x, r) = V _ {f} ^ {\prime} (x - \bar {x} (r)) \quad \mathbb {X} _ {f} (r) = \{\bar {x} (r) \} \oplus \mathbb {X} _ {f} ^ {\prime} \subset \mathbb {X}$$
