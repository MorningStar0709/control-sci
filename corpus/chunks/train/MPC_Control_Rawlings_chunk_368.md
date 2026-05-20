in which $\pmb { \mu } = \{ u ( 0 ) , \mu _ { 1 } ( \cdot ) , \dots , \mu _ { N - 1 } ( \cdot ) \} , x ( i ) = \phi ( i ; x , \pmb { \mu } , \mathbf { w } )$ , and $u ( i ) =$ $\mu _ { i } ( x ( i ) )$ . Let ${ \mathcal { M } } ( x )$ denote the set of feedback policies $\pmb { \mu }$ that for a given initial state x satisfy: the state and control constraints, and the terminal constraint for every admissible disturbance sequence $\mathbf { w } \in \mathcal { W }$ . The first element $u ( 0 )$ in $\pmb { \mu }$ is a control action rather than a control law because the initial state $_ x$ is known, whereas future states are uncertain. Thus ${ \mathcal { M } } ( x )$ is defined by

$$\mathcal {M} (x) := \{\boldsymbol {\mu} \mid u (0) \in \mathbb {U}\phi (i; x, \boldsymbol {\mu}, \mathbf {w}) \in \mathbb {X}, \mu_ {i} (\phi (i; x, \boldsymbol {\mu}, \mathbf {w})) \in \mathbb {U} \quad \forall i \in \mathbb {I} _ {0: N - 1}\phi (N; x, \boldsymbol {\mu}, \mathbf {w}) \in \mathbb {X} _ {f} \forall \mathbf {w} \in \mathcal {W} \}$$

The robust optimal control problem is

$$\mathbb {P} _ {N} (x): \quad \inf _ {\boldsymbol {\mu}} \{V _ {N} (x, \boldsymbol {\mu}) \mid \boldsymbol {\mu} \in \mathcal {M} (x) \} \tag {3.19}$$

The solution to $\mathbb { P } _ { \mathbb { N } } ( x )$ , if it exists, is the policy $\pmb { \mu } ^ { 0 } ( x )$

$$\pmb {\mu} ^ {0} (x) = \{u ^ {0} (0; x), \mu_ {1} ^ {0} (\cdot ; x), \ldots , \mu_ {N - 1} ^ {0} (\cdot , x) \}$$

and the value function is $V _ { N } ^ { 0 } ( x ) = V _ { N } ( x , { \pmb \mu } ^ { 0 } ( x ) )$ . As in conventional MPC, the control applied to the system if the state is x is $u ^ { 0 } ( 0 ; x )$ , the first element in $\pmb { \mu } ^ { 0 } ( x )$ ; the implicit model predictive feedback control law is $\kappa _ { N } ( \cdot )$ defined by

$$\kappa_ {N} (x) := u ^ {0} (0; x)$$
