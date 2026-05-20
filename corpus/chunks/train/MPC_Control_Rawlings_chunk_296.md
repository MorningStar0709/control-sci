$$\mathcal {U} _ {N} (x) := \{\mathbf {u} \mid u (i) \in \mathbb {U}, i = 0, 1, \dots , N - 1, \phi (N; x, \mathbf {u}) = x _ {s} \}$$

The domain of $V _ { N } ^ { 0 } ( \cdot )$ , i.e., the set of feasible initial states for $\mathbb { P } _ { N } ( x )$ , is $x _ { N }$ defined by

$$\mathcal {X} _ {N} := \{x \mid \mathcal {U} _ {N} (x) \neq \emptyset \}$$

For all $x \in \mathcal { X } _ { N }$ , the constraint set $\mathcal { U } _ { N } ( x )$ is compact. The set $x _ { N }$ is thus the set of states that can be steered to $x _ { s }$ in N steps by a control sequence u that satisfies the control constraint. It follows from its definition that $x _ { N }$ is closed and is compact if A is invertible. Because $V _ { N } ( \cdot )$ is continuous, and $\mathcal { U } _ { N } ( x )$ is compact for each $\boldsymbol { x } \in \mathcal { X } _ { N }$ , it follows that for each $x \ \in \ \mathcal { X } _ { N }$ , u $\begin{array} { r l } { \mapsto } & { { } V _ { N } ( x , \mathbf { u } ) } \end{array}$ achieves its minimum, $V _ { N } ^ { 0 } ( x )$ , in $\mathcal { U } _ { N } ( x )$ . Let $\mathbf { u } ^ { 0 } ( x ) \ = \ \{ u ^ { 0 } ( 0 ; x ) , u ^ { 0 } ( 1 ; x ) , \ldots , u ^ { 0 } ( N - 1 ; x ) \}$ denote the solution of $\mathbb { P } _ { N } ( x )$ . Following usual practice, the model predictive control at state x is $\kappa _ { N } ( x ) : = u ^ { 0 } ( 0 ; x )$ , the first element of the optimal control sequence $\mathbf { u } ^ { 0 } ( x )$ .

The optimal steady state $( x _ { s } , u _ { s } )$ is defined to be the solution of the optimization problem $\mathbb { P } _ { \mathrm { s } }$

$$\left(x _ {s}, u _ {s}\right) := \arg \min _ {x, u} \{\ell (x, u) \mid x = A x + B u, u \in \mathbb {U} \}$$

This problem has a solution if $0 ~ \in ~ \mathbb { U }$ since then (0, 0) satisfies the constraints. Since $Q , R > 0$ , the minimizer $( x _ { s } , u _ { s } )$ is unique. Clearly $\ell ( x _ { s } , u _ { s } ) > 0$ unless the setpoint $( x _ { \mathrm { s p } } , u _ { \mathrm { s p } } )$ is feasible for $\mathbb { P } _ { \mathrm { s } } ;$ it is this fact that requires a nonstandard method for establishing asymptotic stability of $( x _ { s } , u _ { s } )$ . The following theorem is proved in (Rawlings, Bonn´e, Jørgensen, Venkat, and Jørgensen, 2008)

Theorem 2.42 (MPC stability with unreachable setpoint). The optimal steady state $x _ { s }$ is asymptotically stable with a region of attraction $x _ { N }$ for the closed-loop system $x ^ { + } = A x + B \kappa _ { N } ( x )$ using setpoint MPC.

This paper also discusses relaxing the terminal constraint and using instead a terminal penalty based on a terminal controller.
