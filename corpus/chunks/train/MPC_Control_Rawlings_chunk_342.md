Starting at state x at time 0, and applying the optimal control laws iteratively to the deterministic system $x ^ { + } = x + u$ (recalling that at time i the optimal control law is $\kappa _ { 3 - i } ^ { 0 } ( \cdot )$ since, at time $i , 3 - i$ is the time to go) yields

$$
\begin{array}{l} x ^ {0} (0) = x \quad u ^ {0} (0) = - (8 / 1 3) x \\ x ^ {0} (1) = (5 / 1 3) x \quad u ^ {0} (1) = - (3 / 1 3) x \\ x ^ {0} (2) = (2 / 1 3) x \quad u ^ {0} (2) = - (1 / 1 3) x \\ \end{array}
x ^ {0} (3; x) = (1 / 1 3) x
$$

so that the optimal control and state sequences are, respectively,

$$
\begin{array}{l} \mathbf {u} ^ {0} (x) = \{- (8 / 1 3) x, - (3 / 1 3) x, - (1 / 1 3) x \} \\ \mathbf {x} ^ {0} (x) = \{x, (5 / 1 3) x, (2 / 1 3) x, (1 / 1 3) x \} \\ \end{array}
$$

which are identical with the optimal open-loop values computed above.

Consider next an uncertain version of the dynamic system in which uncertainty takes the simple form of an additive disturbance w; the system is defined by

$$x ^ {+} = x + u + w$$

in which the only knowledge of $w$ is that it lies in the compact set $\mathbb { W } : = [ - 1 , 1 ]$ . Let $\phi ( i ; \boldsymbol { x } , \mathbf { u } , \mathbf { w } )$ denote the solution of this system at time i if the initial state is x at time 0, and the input and disturbance sequences are, respectively, u and $\mathbf { w } : = \{ w ( 0 ) , w ( 1 ) , w ( 2 ) \}$ . The cost now depends on the disturbance sequence — but it also depends, in contrast to the deterministic problem discussed above, on whether the control is open-loop or feedback. To discuss the latter case, we define a feedback policy µ to be a sequence of control laws

$$\boldsymbol {\mu} := \{\mu_ {0} (\cdot), \mu_ {1} (\cdot), \mu_ {2} (\cdot) \}$$

in which $\mu _ { i } : \mathbb { R } \to \mathbb { R } , i = 0 , 1 , 2 ;$ ; under policy µ, if the state at time i is x, the control is $\mu _ { i } ( x )$ . Let M denote the class of admissible policies, for
