$$e ^ {+} = A _ {K} e + \delta \quad A _ {K} := A + B K \tag {5.18}$$

The feedforward component v of the control u generates the trajectory $\{ z ( i ) \}$ , which is the center of the tube in which the state estimator trajectory {x(i) ˆ } lies. Because $\mathbb { \Delta }$ is a C-set and $\rho ( A _ { K } ) < 1$ , there exists a robust positive invariant C-set S satisfying

$$A _ {K} \mathbb {S} \oplus \mathbb {\Delta} = \mathbb {S}$$

An immediate consequence is the following.

Proposition 5.3 (Proximity of state estimate and nominal state). If the initial states of the estimator and nominal system, $\hat { x } ( 0 )$ and $z ( 0 )$ respectively, satisfy $\mathbf { \partial } \cdot \hat { x } ( 0 ) \in \{ z ( 0 ) \} \oplus \mathbb { S }$ , then $\hat { x } ( i ) \in \{ z ( i ) \}$ ⊕ S and $u ( i ) \in$ $\{ \nu ( i ) \} \oplus K \mathbb { S }$ for all $i \in \mathbb { I } _ { \geq 0 }$ , and all admissible disturbance sequences w and ν.

It follows from Proposition 5.3 that the state estimator trajectory $\hat { \mathbf { x } }$ remains in the tube $\hat { \mathbf { X } } ( z ( 0 ) , \mathbf { v } ) : = \{ \{ z ( i ) \} \oplus \mathbb { S } | i \in \mathbb { I } _ { \ge 0 } \}$ and the control trajectory v remains in the tube $\hat { \mathbf { V } } ( \mathbf { v } ) : = \{ \{ \nu ( i ) \} \oplus K \mathbb { S } | i \in \mathbb { I } _ { \geq 0 } \}$ provided that $e ( 0 ) \in \mathbb { S }$ . Hence, from Propositions 5.2 and 5.3, the state trajectory x lies in the tube $\mathbf { X } ( z ( 0 ) , \mathbf { v } ) : = \{ \{ z ( i ) \} \oplus \mathbb { \Gamma } | \ i \in \mathbb { I } _ { \ge 0 } \}$ where $\mathbb { T } : = \mathbb { S } \oplus \mathbb { Z }$ provided that $ { \widetilde { { x } } } ( 0 ) = x ( 0 ) -  { \hat { { x } } } ( 0 ) \in \mathbb { { Z } }$ and $e ( 0 ) \in \mathbb { S }$ . This information may be used to construct a robust output feedback model predictive controller using the procedures outlined in Chapter 3 for robust state feedback MPC of systems; the major difference is that we now control the estimator state $\hat { x }$ and use the fact that the actual state x lies in $\{ { \hat { x } } \} \oplus { \mathbb { \Sigma } }$ .
