# 5.4.4 Control of the Nominal System

Since $x ( i ) \in \{ z ( i ) \} \oplus \mathbb { T } ( i )$ and $u ( i ) \in \{ \nu ( i ) \} \oplus K \mathbb { S } ( i )$ for all i, we can use MPC to control the sequences $\{ z ( i ) \}$ and $\{ \upsilon ( i ) \}$ so that $x ( i ) \in \mathbb { X }$ and $u ( i ) \in \mathbb { U }$ for all i. The constraints on x and u are satisfied if $z$ and v are required to satisfy the tighter time-varying constraints

$$z (i) \in \mathbb {Z} _ {i} := \mathbb {X} \ominus \mathbb {\Gamma} (i) \quad v (i) \in \mathbb {V} _ {i} := \mathbb {U} \ominus K \mathbb {S} (i)$$

for all i; $\mathbb { Z } _ { i }$ and $\mathbb { V } _ { i }$ may be replaced by outer approximating sets. For this to be possible, we assume

Assumption 5.9 (Constraint bounds; time-varying case). $\mathbb { T } ( 0 ) \subset \mathbb { X }$ and $K \mathbb { S } ( 0 ) \subset \mathbb { U }$ .

Since both $\{ \mathbb { T } ( i ) \}$ and $\{ \mathbb { S } ( i ) \}$ are nonincreasing sequences, $\{ \mathbb { Z } _ { i } \}$ and $\{ \mathbb { S } _ { i } \}$ are nondecreasing sequences so that satisfaction of Assumption 5.9 ensures that $\mathbb { Z } _ { i }$ and $\mathbb { V } _ { i }$ are not empty for all $i \in \mathbb { I } _ { \geq 0 }$ . The constraints are time varying, so the nominal MPC problem at time $k ,$ , state z is $\mathbb { P } _ { N } ( z , k )$ defined by

$$\mathbb {P} _ {N} (z, k): \quad \bar {V} _ {N} ^ {0} (z, k) = \min _ {\mathbf {v}} \{\bar {V} _ {N} (z, \mathbf {v}) \mid \mathbf {v} \in \mathcal {V} _ {N} (z, k) \}$$

where the cost function $\bar { V } _ { N } ( \cdot )$ is defined by

$$\bar {V} _ {N} (z, \mathbf {v}) := \sum_ {k = 0} ^ {N - 1} \ell (z (k), v (k)) + V _ {f} (z (N))$$

and the constraint set $\mathcal { V } _ { N } ( z , k )$ by

$$
\begin{array}{l} \mathcal {V} _ {N} (z, k) := \left\{\mathbf {v} \mid v (i) \in \mathbb {V} _ {k + i}, z (i) \in \mathbb {Z} _ {k + i}, \forall i \in \{0, 1, \dots , N \}, \right. \\ \left. z (N) \in \mathbb {Z} _ {f} \right\} \tag {5.28} \\ \end{array}
$$
