# Robust control algorithm (offset-free MPC).

Initialization: At time 0, set $i = 0$ , set $\hat { \phi } = \hat { \phi } ( 0 )$ in which $\hat { \phi } = ( \hat { x } , \hat { d } )$ and set $z = { \hat { x } }$ .

Step 1 (Compute control): At time i, solve the “nominal” optimal control problem $\bar { \mathbb { P } } _ { N } ( z , \hat { d } , \bar { r } )$ to obtain the current “nominal” control action $\nu = \bar { \kappa } _ { N } ( z , \hat { d } , \bar { r } )$ and the control action $u = \nu + K ( \hat { x } - z )$ .

Step 2 (Check): If $\bar { \mathbb { P } } _ { N } ( z , \hat { d } , \bar { r } )$ is infeasible, adopt safety/recovery procedure.

Step 3 (Apply control): Apply the control u to the system being controlled.

Step 4 (Update): (a) Compute the successor state estimate $\hat { \phi } ^ { + } = \stackrel { \sim } { A } \hat { x } +$ $\tilde { B } u + L ( y - \tilde { C } \hat { \phi } )$ . (b) Compute the successor state $z ^ { + } = A z + B _ { d } \hat { d } +$ Bv of the nominal system.

Step 5: Set $( \hat { \phi } , z ) = ( \hat { \phi } ^ { + } , z ^ { + } )$ , set $i = i + 1$ , and go to Step 1.

In normal operation, Step 2 is not activated; Propositions 5.2 and 5.3 ensure that the constraints ${ \hat { x } } \in \{ z \} \oplus \mathbb { S }$ and $u \in \{ \nu \} \oplus K \mathbb { S }$ are satisfied. If an unanticipated event occurs and Step 2 is activated, the controller can be reinitialized by setting $\nu = \bar { \kappa } _ { N } ( \hat { x } , \hat { d } , \bar { r } )$ , setting $u = \nu$ and relaxing constraints if necessary.
