# Robust control algorithm (linear constrained systems).

Initialization: At time 0, set i = 0, set $\hat { x } = \hat { x } ( 0 )$ and set $z = { \hat { x } }$ .

Step 1: At time i, solve the nominal optimal control problem $\bar { \mathbb { P } } _ { N } ( z )$ to obtain the current nominal control action $\nu = \bar { \kappa } _ { N } ( z )$ and the control $u = \nu + K ( \hat { x } - z )$ .

Step 2: If ${ \hat { x } } \notin \{ z \} \oplus \mathbb { S }$ or $u \not \in \{ \nu \} \oplus K \mathbb { S }$ , set $z = { \hat { x } }$ and re-solve $\bar { \mathbb { P } } _ { N } ( z )$ to obtain $\upsilon = \bar { \kappa } _ { N } ( z )$ and $u = \nu$ .

Step 3: Apply the control u to the system being controlled.

Step 4: (a) Compute the successor state estimate $\hat { x } ^ { + } = A \hat { x } + B u + L ( y -$ Cx)ˆ . (b) Compute the successor state $z ^ { + } = f ( z , \nu )$ of the nominal system.

Step 5: Set $( \hat { x } , z ) = ( \hat { x } ^ { + } , z ^ { + } )$ , set i = i + 1 and go to Step 1.

In normal operation, Step 2 is not activated; Propositions 5.2 and 5.3 ensure that the constraints are satisfied. In the event of an unanticipated event, Step 2 is activated, the controller is reinitialized and normal operation resumed. If Step 2 is activated, $\nu = \bar { \kappa } _ { N } ( \hat { x } )$ and $u = \nu$ . Hence nominal MPC would ensue if Step 2 were activated at each sample.

If the terminal cost $V _ { f } ( \cdot )$ and terminal constraint set $\mathbb { Z } _ { f }$ satisfy the stability Assumptions 2.12 and 2.13 of Chapter 2, and if Assumption 5.4 is satisfied, the value function $\bar { V } _ { N } ^ { 0 } ( \cdot )$ satisfies

$$\bar {V} _ {N} ^ {0} (z) \geq \ell (z, \bar {\kappa} _ {N} (z)) \quad \forall z \in \mathcal {Z} _ {N}\Delta \bar {V} _ {N} ^ {0} (z) \leq - \ell (z, \bar {\kappa} _ {N} (z)) \quad \forall z \in \mathcal {Z} _ {N}\bar {V} _ {N} ^ {0} (z) \leq V _ {f} (z) \quad \forall z \in \mathbb {Z} _ {f}$$

in which $\Delta \bar { V } _ { N } ^ { 0 } ( z ) : = \bar { V } _ { N } ^ { 0 } ( f ( z , \bar { \kappa } _ { N } ( z ) ) ) - \bar { V } _ { N } ^ { 0 } ( z )$

As shown in Section 3.4.3, if, in addition to Assumption 5.4, (i) the stability Assumptions 2.12 and 2.13 are satisfied, (ii) $\ell ( z , \nu ) \ =$ $( 1 / 2 ) ( | z | _ { Q } ^ { 2 } + | \nu | _ { R } ^ { 2 } )$ where Q and R are positive definite, (iii) $V _ { f } ( z ) =$ $( 1 / 2 ) | Z | _ { P _ { f } } ^ { 2 }$ where $P _ { f }$ is positive definite, and $( \mathrm { i v } ) ~ { \cal Z } _ { N }$ is a C-set, then there exist positive constants $c _ { 1 }$ and $c _ { 2 }$ such that
