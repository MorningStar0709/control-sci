The terminal equality constraint is chosen for simplicity. Because of the terminal equality constraint, there is no terminal cost. The terminal constraint $\hat { x } ( N ) = z ^ { * } ( N ; z )$ induces the implicit constraint ${ \textbf { u } } \in$ $\mathcal { U } _ { N } ( \hat { x } , z )$ on the control sequence u. For each $z \in { \mathcal { Z } } _ { N }$ , the domain of the value function $\bar { V } _ { N } ^ { 0 } ( \cdot , z )$ , and of the minimizer $\boldsymbol { \mathbf { u } } ^ { 0 } ( \cdot , z )$ , is the set $\hat { X } _ { N } ( z )$ defined by

$$\hat {X} _ {N} (z) := \{\hat {x} \mid \mathcal {U} _ {N} (\hat {x}, z) \neq \emptyset \}$$

The minimizing control sequence is

$$\mathbf {u} ^ {0} (\hat {x}, z) = \{u ^ {0} (0; \hat {x}, z), u ^ {0} (1; \hat {x}, z), \dots , u ^ {0} (N - 1; \hat {x}, z) \}$$

and the control applied to the estimator system (when the estimator state is xˆ and the state of the nominal system is z) is $u ^ { 0 } ( 0 ; \hat { x } , z )$ , the first element in this sequence. The corresponding optimal state sequence is

$$\hat {\mathbf {x}} ^ {0} (\hat {x}, z) = \{\hat {x} ^ {0} (0; \hat {x}, z), \hat {x} ^ {0} (1; \hat {x}, z), \dots , \hat {x} ^ {0} (N; \hat {x}, z) \}$$

The implicit ancillary control law is, therefore, $\kappa _ { N } ( \cdot )$ defined by

$$\kappa_ {N} (\hat {x}, z) := u ^ {0} (0; \hat {x}, z)$$

The controlled composite system satisfies

$$
\begin{array}{l} \hat {x} ^ {+} = f (\hat {x}, \kappa_ {N} (\hat {x}, z)) + \delta \\ z ^ {+} = f (z, \bar {k} _ {N} (z)) \\ \end{array}
$$

For each $c > 0$ , each $z \in { \mathcal { Z } } _ { N }$ , let $S _ { c } ( z ) : = \{ \hat { x } | \bar { V } _ { N } ^ { 0 } ( \hat { x } , z ) \leq c \}$ . With appropriate assumptions, there exists a $c \in ( 0 , \infty )$ such that if ${ \hat { x } } ( 0 ) \in$ $S _ { c } ( z ( 0 ) )$ , then $\hat { x } ( i ) \in S _ { c } ( z ^ { 0 } ( i ; z ( 0 ) ) )$ ) for all $i \in \mathbb { I } _ { \geq 0 }$ and all admissible disturbance and measurement noise sequences, w and ν. In other words, c is such that $S _ { c } ( \cdot )$ is xˆ-robust positive invariant for the controlled composite system. It follows from the discussion previously that the solutions $\hat { x } ( i )$ and $z ( i )$ of the controlled composite system satisfy

$$
\begin{array}{l} z (i) \rightarrow 0 \text { as } i \rightarrow \infty \\ \hat {x} (i) \in S _ {c} (z (i)) \quad \forall i \in \mathbb {I} _ {\geq 0} \\ x (i) \in S _ {c} (z (i)) \oplus \mathbb {Z} _ {x} \quad \forall i \in \mathbb {I} _ {\geq 0} \\ \end{array}
$$
