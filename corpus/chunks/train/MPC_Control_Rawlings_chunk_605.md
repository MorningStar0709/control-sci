$$\bar {V} _ {N} ^ {0} (z) \geq c _ {1} | z | ^ {2} \quad \forall z \in \mathcal {Z} _ {N}\Delta \bar {V} _ {N} ^ {0} (z) \leq - c _ {1} | z | ^ {2} \quad \forall z \in \mathcal {Z} _ {N}\bar {V} _ {N} ^ {0} (z) \leq c _ {2} | z | ^ {2} \quad \forall z \in \mathcal {Z} _ {N}$$

It follows from Chapter 2 that the origin is exponentially stable for the nominal system $z ^ { + } = A z + B \bar { \kappa } _ { N } ( z )$ with a region of attraction $\mathcal { Z } _ { N }$ so that there exists a $c > 0$ and a $ { \boldsymbol { \gamma } } \in ( 0 , 1 )$ such that

$$| z (i) | \leq c | z (0) | \gamma^ {i}$$

for all $z ( 0 ) \in \mathcal { Z } _ { N }$ , all $i \in \mathbb { I } _ { \geq 0 }$ . Also $z ( i ) \in \mathcal { Z } _ { N }$ for all $i \in \mathbb { I } _ { \ge 0 } \mathrm { i f } z ( 0 ) \in \mathcal { Z } _ { N }$ so that problem $\mathbb { P } _ { N } \big ( z ( i ) \big )$ is always feasible. Because the state $\hat { x } ( i )$ of the state estimator always lies in $\{ z ( i ) \} \oplus \mathbb { S }$ , and the state $x ( i )$ of the system being controlled always lies in $\{ z ( i ) \} \oplus \mathbb { T }$ , it follows that $\hat { x } ( i )$ converges robustly and exponentially fast to $\mathbb { S } ,$ , and $x ( i )$ converges robustly and exponentially fast to Γ. We are now in a position to establish exponential stability of $\mathcal { A } : = \mathbb { S } \times \{ 0 \}$ with a region of attraction $( \mathcal { Z } _ { N } \oplus \mathbb { S } ) \times \mathcal { Z } _ { N }$ for the composite system (5.25) and (5.26).

Proposition 5.5 (Exponential stability of output MPC). The set $\mathcal { A } : =$ $\mathbb { S } \times \{ 0 \}$ is exponentially stable with a region of attraction $( \mathcal { Z } _ { N } \oplus \mathbb { S } ) \times \mathcal { Z } _ { N }$ for the composite system (5.25) and (5.26).

Proof. Let $\phi : = ( \hat { x } , z )$ denote the state of the composite system. Then $| \phi | _ { \mathcal { A } }$ is defined by

$$| \phi | _ {\mathcal {A}} = | \hat {x} | _ {\mathbb {S}} + | z |$$

where $| \hat { x } | _ { \mathbb { S } } : = d ( \hat { x } , \mathbb { S } )$ . But ${ \hat { x } } \in \{ z \} \oplus \mathbb { S }$ implies

$$| \hat {x} | _ {\mathbb {S}} = d (\hat {x}, \mathbb {S}) = d (z + e, \mathbb {S}) \leq d (z + e, e) = | z |$$

since $e \in \mathbb { S }$ . Hence $| \phi | _ { \mathcal { A } } \leq 2 | z |$ so that

$$| \phi (i) | _ {\mathcal {A}} \leq 2 | z (i) | \leq 2 c | z (0) | \gamma^ {i} \leq 2 c | \phi (0) | \gamma^ {i}$$
