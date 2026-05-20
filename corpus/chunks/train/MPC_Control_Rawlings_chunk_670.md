$$\mathbf {u} _ {1} ^ {0} = K _ {1} x _ {1} (0) + L _ {1} \mathbf {u} _ {2}$$

and we see player one’s optimal decision depends linearly on his initial state, but also on player two’s decision. This is the key difference between decentralized control and noncooperative control. In noncooperative control, player two’s decisions are communicated to player one and player one accounts for them in optimizing the local objective.

Convex step. Let $p \in \mathbb { I } _ { \geq 0 }$ denote the integer-valued iteration in the optimization problem. Looking ahead to the M-player game, we do not take the full step, but a convex combination of the the current optimal solution, ${ \bf u } _ { 1 } ^ { 0 }$ , and the current iterate, $\mathbf { u } _ { 1 } ^ { p }$

$$\mathbf {u} _ {1} ^ {p + 1} = w _ {1} \mathbf {u} _ {1} ^ {0} + (1 - w _ {1}) \mathbf {u} _ {1} ^ {p} \quad 0 < w _ {1} < 1$$

This iteration is displayed in Figure 6.1. Notice we have chosen a distributed optimization of the Gauss-Jacobi type (see Bertsekas and Tsitsiklis, 1997, pp.219–223).

We place restrictions on the systems under consideration before analyzing stability of the controller.

Assumption 6.7 (Unconstrained two-player game).

(a) All subsystems, $A _ { i j } , i = 1 , 2 , j = 1 , 2$ , are stable.   
(b) The controller penalties $Q _ { 1 } , Q _ { 2 } , R _ { 1 } , R _ { 2 }$ are positive definite.

The assumption of stable models is purely for convenience of exposition. We treat unstable, stabilizable systems in Section 6.3.

Convergence of the players’ iteration. To understand the convergence of the two players’ iterations, we express both players’ moves as follows

$$
\begin{array}{l} \mathbf {u} _ {1} ^ {p + 1} = w _ {1} \mathbf {u} _ {1} ^ {0} + (1 - w _ {1}) \mathbf {u} _ {1} ^ {p} \\ \mathbf {u} _ {2} ^ {p + 1} = w _ {2} \mathbf {u} _ {2} ^ {0} + (1 - w _ {2}) \mathbf {u} _ {2} ^ {p} \\ 1 = w _ {1} + w _ {2} \quad 0 <   w _ {1}, w _ {2} <   1 \\ \end{array}
$$

or

$$
\left[ \begin{array}{c} \mathbf {u} _ {1} \\ \mathbf {u} _ {2} \end{array} \right] ^ {p + 1} = \left[ \begin{array}{c c} w _ {1} I & 0 \\ 0 & w _ {2} I \end{array} \right] \left[ \begin{array}{c} \mathbf {u} _ {1} ^ {0} \\ \mathbf {u} _ {2} ^ {0} \end{array} \right] + \left[ \begin{array}{c c} (1 - w _ {1}) I & 0 \\ 0 & (1 - w _ {2}) I \end{array} \right] \left[ \begin{array}{c} \mathbf {u} _ {1} \\ \mathbf {u} _ {2} \end{array} \right] ^ {p}
$$

The optimal control for each player is
