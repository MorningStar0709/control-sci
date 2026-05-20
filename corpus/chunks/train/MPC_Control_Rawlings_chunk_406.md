in which the disturbance6 $w = w ( x , u , p )$ is defined by

$$w := (A - \bar {A}) x + (B - \bar {B}) u$$

Hence, the disturbance w lies in the set W defined by

$$\mathbb {W} := \{(A - \bar {A}) x + (B - \bar {B}) u \mid (A, B) \in \mathcal {P}, (x, u) \in \mathbb {X} \times \mathbb {U} \}$$

Clearly W is polytopic. The state and control constraint sets, Z and V for the nominal optimal control problem, defined in Section 3.4, whose solution yields implicitly the nominal control law $\bar { \kappa } _ { N } ( \cdot )$ are chosen to satisfy

$$\mathbb {Z} \oplus S _ {K} (\infty) \subset \mathbb {X} \qquad \mathbb {V} \oplus K S _ {K} (\infty) \subset \mathbb {U}$$

in which, as before,

$$S _ {K} (\infty) := \sum_ {i = 0} ^ {\infty} (\bar {A} _ {K}) ^ {i} \mathbb {W}$$

The origin is exponentially stable for the nominal system $z ^ { + } = \bar { A } z +$ $\bar { B } \bar { \kappa } _ { N } ( z )$ with a region of attraction $\mathcal { Z } _ { N }$ . We know from Section 3.4 that the control law $\kappa _ { N } ( x , z ) = \bar { \kappa } _ { N } ( z ) + K ( x - z )$ results in satisfaction of the state and control constraints $x \in \mathbb { X }$ and $u \in \mathbb { U }$ for all admissible disturbance sequences provided that the initial state $( x ( 0 ) , z ( 0 ) )$ of the composite satisfies $( x ( 0 ) , z ( 0 ) ) \in \mathcal { M } _ { N } : = \{ ( x , z ) ~ | ~ x \in \{ z \} \oplus S _ { K } ( \infty ) , z \in$ ${ \mathcal { Z } } _ { N } \} \subseteq \mathbb { X } \times { \mathcal { Z } } _ { N }$ . The set $S _ { K } ( \infty ) \times \{ 0 \}$ is robustly exponentially stable for the composite controlled system with a region of attraction $\mathcal { M } _ { N }$ .
