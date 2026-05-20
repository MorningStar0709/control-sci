# 6.3 Constrained Two-Player Game

Now that we have introduced most of the notation and the fundamental ideas, we consider more general cases. Because we are interested in establishing stability properties of the controlled systems, we focus exclusively on cooperative distributed MPC from this point forward. In this section we consider convex input constraints on the two players. We assume output constraints have been softened with exact soft constraints and added to the objective function, so do not consider output constraints explicitly. The input constraints break into two significant categories: coupled and uncoupled constraints. We treat each of these in turn.

We also allow unstable systems and replace Assumption 6.7 with the following more general restrictions on the systems and controller parameters.

Assumption 6.12 (Constrained two-player game).

(a) The systems $( \underline { { A } } _ { i } , \underline { { B } } _ { i } ) , i = 1 , 2$ are stabilizable, in which $\underline { { A } } _ { i } = \mathrm { d i a g } ( A _ { 1 i } , A _ { 2 i } )$ and Bi = h B1iB2i i. $\underline { { { B } } } _ { i } = \left[ \begin{array} { l } { B _ { 1 i } } \\ { B _ { 2 i } } \end{array} \right]$   
(b) The systems $( A _ { i } , C _ { i } ) , i = 1 , 2$ are detectable.   
(c) The input penalties $R _ { 1 } , R _ { 2 }$ are positive definite, and the state penalties $Q _ { 1 } , Q _ { 2 }$ are semidefinite.   
(d) The systems $( A _ { 1 } , Q _ { 1 } )$ and $( A _ { 2 } , Q _ { 2 } )$ are detectable.   
(e) The horizon is chosen sufficiently long to zero the unstable modes, $N \geq \operatorname* { m a x } _ { i \in \mathbb { I } _ { 1 : 2 } } \underline { n } _ { i } ^ { u }$ , in which $\underline { n } _ { i } ^ { u }$ is the number of unstable modes of $\underline { { A } } _ { i }$ , i.e., number of $\lambda \in \mathrm { e i g } ( \underline { { A } } _ { i } )$ such that $| \lambda | \ge 1$ .

Assumption (b) implies that we have $L _ { i }$ such that $( A _ { i } - L _ { i } C _ { i } ) , i = 1 ,$ , 2 is stable. Note that the stabilizable and detectable conditions of Assumption 6.12 are automatically satisfied if we obtain the state space models from a minimal realization of the input/output models for $( u _ { i } , y _ { j } ) , i , j = 1 , 2$ .

Unstable modes. To handle unstable systems, we add constraints to zero the unstable modes at the end of the horizon. To set up this constraint, consider the real Schur decomposition of $A _ { i j }$ for $i , j \in \mathbb { I } _ { 1 : 2 }$
