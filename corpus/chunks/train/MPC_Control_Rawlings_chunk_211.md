i.e., $\kappa _ { N } ( x ) = - { \sf s a t } ( ( 3 / 5 ) x )$ which is the saturating control law depicted in Figure 2.1(a). The control law is piecewise affine and the value function piecewise quadratic. The structure of the solution to constrained linear quadratic optimal control problems is explored more fully in Chapter 7. -

As we show in Chapter 3, continuity of the value function is desirable. Unfortunately, this is not true in general; the major difficulty is in establishing that the set-valued function $x \mapsto \mathcal { U } _ { N } ( x )$ has certain continuity properties. Continuity of the value function $V _ { N } ^ { 0 } ( \cdot )$ and of the implicit control law $\kappa _ { N } ( \cdot )$ may be established for a few important cases, however, as is shown by the next result, which assumes satisfaction of our standing assumptions: 2.2 and 2.3 so that the cost function $V _ { N } ( \cdot )$ is continuous in (x, u).

Theorem 2.7 (Continuity of value function and control law). Suppose that Assumptions 2.2 and 2.3 hold.

(a) Suppose that there are no state constraints so that ${ \mathbb X } = { \mathbb X } _ { f } = { \mathbb R } ^ { n }$ . Then the value function $V _ { N } ^ { 0 } : \mathcal { X } _ { N }  \mathbb { R }$ is continuous and $\mathcal { X } _ { N } = \mathbb { R } ^ { n }$ .   
(b) Suppose f (·) is linear $( x ^ { + } = A x + B u )$ and that the state and control constraints sets X and U are polyhedral.3 Then the value function $V _ { N } ^ { 0 }$ : $\mathcal { X } _ { N }  \mathbb { R }$ is continuous.   
(c) If, in addition, the solution $\mathbf { u } ^ { 0 } ( x )$ of $\mathbb { P } _ { N } ( x )$ is unique at each $\boldsymbol { x } \in \mathcal { X } _ { N }$ , then the implicit MPC control law $\kappa _ { N } ( \cdot )$ is continuous.

The proof of this theorem is given in Section C.3 of Appendix C. The following example, due to Meadows, Henson, Eaton, and Rawlings (1995), shows that there exist nonlinear examples where the value function and implicit control law are not continuous.
