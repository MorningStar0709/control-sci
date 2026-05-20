# 5.4.5 Control of the State Estimator

The implicit control law for the state estimator is $\kappa _ { N } ( \cdot )$ defined by

$$\kappa_ {N} (\hat {x}, z, k) := \bar {\kappa} _ {N} (z, k) + K (\hat {x} - z)$$

Hence, the composite system with state $( \hat { x } , z )$ satisfies

$$\hat {x} ^ {+} = A \hat {x} + B \kappa_ {N} (\hat {x}, z, k) + \delta (k) \tag {5.29}z ^ {+} = A z + B \bar {\kappa} _ {N} (z, k) \tag {5.30}k ^ {+} = k + 1 \tag {5.31}$$

with initial state $( \hat { x } ( 0 ) , z ( 0 ) )$ satisfying $\hat { x } ( 0 ) \in \{ z ( 0 ) \} \oplus \mathbb { S } ( 0 ) , z ( 0 ) \in$ $\mathcal { Z } _ { N } ( 0 )$ ; these constraints are satisfied if $z ( 0 ) = \hat { x } ( 0 ) \in \mathcal { Z } _ { N } ( 0 )$ .

Also, from Proposition 5.8, the sequences $\{ \Phi ( k ) \} , \{ \Gamma ( k ) \}$ and $\{ \mathbb { S } ( k ) \}$ converge exponentially fast to Φ, Γ and S, respectively. We have the following result for robust time-varying output MPC:

Proposition 5.10 (Exponential convergence of output MPC: time-varying case). There exists a $c > 0$ and a $ { \boldsymbol { \gamma } } \in \left( 0 , 1 \right)$ such that $| z ( k ) | \ \leq$ $c | z ( 0 ) | \gamma ^ { k }$ and d $( x ( k ) , \Gamma ) \le c ( | z ( 0 ) | + 1 )  { \gamma } ^ { k }$ for all $k \in \mathbb { I } _ { \geq 0 } , a l l \boldsymbol { x } ( 0 )$ , ${ \hat { x } } ( 0 ) , z ( 0 )$ such that $( x ( 0 ) - \hat { x } ( 0 ) , \hat { x } ( 0 ) - z ( 0 ) ) \in \Phi ( 0 ) , z ( 0 ) \in \mathcal { Z } _ { N } ( 0 )$ .

Proof. $\mathrm { I f } ~ z ( 0 ) \in \mathcal { Z } _ { N } ( 0 )$ , we have $x ( k ) \in \{ z ( k ) \} \oplus \mathbb { T } ( k )$ for all $k \in \mathbb { I } _ { \geq 0 }$ . From Proposition 5.8, there exists a $c > 0$ and a $ { \boldsymbol { \gamma } } \in ( 0 , 1 )$ such that $d _ { H } ( \mathbb { T } ( k ) , \mathbb { T } ) \leq c y ^ { k } \mathrm { ~ a n d ~ } | z ( k ) | \leq c | z ( 0 ) | y ^ { k } , z ( 0 ) \in \mathcal { Z } _ { N } ( 0 )$ , for all $k \in$ $ { \mathbb { I } } _ { \geq 0 }$ . Hence

$$
\begin{array}{l} d (x (k), \mathbb {T}) \leq d _ {H} (\{z (k) \} \oplus \mathbb {T} (k), \mathbb {T}) \\ \leq | z (k) | + d _ {H} (\mathbb {T} (k), \mathbb {T}) \\ \leq c (| z (0) | + 1) \gamma^ {k} \tag {5.32} \\ \end{array}
$$

for all $k \in \mathbb { I } _ { \geq 0 }$ , all $( x ( 0 ) , { \hat { x } } ( 0 ) )$ such that $\phi ( 0 ) = ( x ( 0 ) - \hat { x } ( 0 ) , \hat { x } ( 0 ) -$ $z ( 0 ) ) \in \Phi ( 0 )$

Similarly it can be shown that there exist a possibly different $c > 0$ and $ { \boldsymbol { \gamma } } \in ( 0 , 1 )$ such that

$$d (\hat {x} (k), \mathbb {S}) \leq c (| z (0) | + 1) \gamma^ {k}$$

for all $k \in  { \mathbb { I } } _ { \geq 0 }$ . This result is not as strong as the corresponding result in Proposition 5.5 where exponential stability of $\mathbb { S } \times \{ 0 \}$ with a region of attraction $( \mathcal { Z } _ { N } \oplus \mathbb { S } ) \times \mathcal { Z } _ { N }$ is established for the composite system (5.25) and (5.26); the time-varying nature of the problem appears to preclude a stronger result.
