# Suboptimal control algorithm.

Data: Integer $N _ { \mathrm { i t e r } }$ .

Input: Current state x, previous state sequence $\mathbf { w } = \{ w ( 0 ) , w ( 1 ) , \ldots ,$ $w \left( N \right) \}$ , previous control sequence $\mathbf { v } = \{ \nu ( 0 ) , \nu ( 1 ) , \ldots , \nu ( N - 1 ) \}$ .

Step 1: If $x \notin \mathbb { X } _ { f } .$ , use $\left\{ \nu ( 1 ) , \nu ( 2 ) , \ldots , \nu ( N - 1 ) , \kappa _ { f } ( w ( N ) ) \right\}$ as a warm start for an optimization algorithm. Perform $N _ { \mathrm { i t e r } }$ iterations of the algorithm to obtain an improved control sequence $\mathbf { u } \in \mathcal { U } _ { N } ( x )$ . Apply control $u = u ( 0 )$ to the system being controlled.

Step 2: If $x \in \mathbb { X } _ { f }$ , set $u \ = \ \kappa _ { f } ( x )$ and apply u to the system being controlled; or perform $N _ { \mathrm { i t e r } }$ steps of an optimization algorithm using u $\mathbf { \Omega } _ { 1 } ( x , \kappa _ { f } )$ , defined previously, as a warm start to obtain an improved control sequence $\mathbf { u } \in \mathcal { U } _ { N } ( x )$ satisfying (2.43) and associated state sequence w.

A nominally stabilizing controller with very low online computational demands may be obtained by merely using the warm starts defined in the algorithm. Improved performance is obtained by using $N _ { \mathrm { i t e r } }$ iterations of an optimization algorithm to improve the warm start. It is more important to employ optimization in Step 1 when $x \notin \mathbb { X } _ { f }$ since the warm start when $\boldsymbol { x } \in \mathbb { X } _ { f }$ has good performance if $\kappa _ { f } ( \cdot )$ is designed properly.
