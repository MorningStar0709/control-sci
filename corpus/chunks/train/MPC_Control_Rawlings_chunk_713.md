$$
\begin{array}{l} V (x ^ {+}, \mathbf {u} ^ {+}) \leq V (x, \mathbf {u}) - \sum_ {j \in \mathbb {I} _ {1: M}} \rho_ {j} \ell_ {j} (x _ {j}, u _ {j}) \\ | \mathbf {u} | \leq d | x | \quad x \in r \mathcal {B} \\ \end{array}
$$

For the M-player game, we generalize Assumption 6.12 of the twoplayer game to the following.

Assumption 6.16 (Constrained M-player game).

(a) The systems $( \underline { { A } } _ { i } , \underline { { B } } _ { i } ) , i \in \mathbb { I } _ { 1 : M }$ are stabilizable, in which $\underline { { A } } _ { i } = \mathrm { d i a g } ( A _ { 1 i } , A _ { 2 i } , \cdot \cdot \cdot , A _ { M }$

(b) The systems $( A _ { i } , C _ { i } ) , i \in \mathbb { I } _ { 1 : M }$ are detectable.

(c) The input penalties $R _ { i } , i \in \mathbb { I } _ { 1 : M }$ are positive definite, and $Q _ { i } , i \in \mathbb { I } _ { 1 : M }$ are semidefinite.

(d) The systems $( A _ { i } , Q _ { i } ) , i \in \mathbb { I } _ { 1 : M }$ are detectable.

(e) The horizon is chosen sufficiently long to zero the unstable modes; $N \geq \operatorname* { m a x } _ { i \in \mathbb { I } _ { 1 : M } } ( \underline { { n } } _ { i } ^ { u } )$ , in which $\underline { n } _ { i } ^ { u }$ is the number of unstable modes of $\underline { { A } } _ { i }$ .

(f) Zero offset. For achieving zero offset, we augment the models with integrating disturbances such that

$$
\operatorname{rank} \left[ \begin{array}{c c} I - A _ {i} & - B _ {d i} \\ C _ {i} & C _ {d i} \end{array} \right] = n _ {i} + p _ {i} \qquad i \in \mathbb {I} _ {1: M}
$$

Applying Theorem 6.4 then establishes exponential stability of the solution $x ( k ) = 0$ for all k. The region of attraction is the set of states for which the unstable modes of each subsystem can be brought to zero in N moves while satisfying the respective input constraints. These conclusions apply regardless of how many iterations of the players’ optimizations are used in the control calculation. Although the closedloop system is exponentially stable for both coupled and uncoupled constraints, the converged distributed controller is equal to the centralized controller only for the case of uncoupled constraints.

The exponential stability of the regulator implies that the states and inputs of the constrained M-player system converge to the steady-state target. The steady-state target can be calculated as a centralized or distributed problem. We assume the centralized target has a feasible, zero offset solution for the true plant disturbance. The initial state of the plant and the estimate error must be small enough that feasibility of the target is maintained under the nonzero estimate error.
