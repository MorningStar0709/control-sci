![](image/e8b4998a71f7357bfe9b76e812bca8c2ebe0c5b796a619bba67a328d1f19aaf9.jpg)

<details>
<summary>line</summary>

| k | x |
| --- | --- |
| 0 | 0 |
| 1 | -1 |
| 2 | -1.5 |
| 3 | -2 |
</details>

(b) Uncertain case.   
Figure 3.3: State trajectory and state tube.

$$X (i + 1) = F (X (i), \mu_ {i} (\cdot)) \qquad X (0) = \{x \}$$

in which $F ( X , \mu _ { i } ( \cdot ) ) : = \{ f ( x , \mu _ { i } ( x ) , w ) ~ | ~ x \in X , w \in \mathbb { W } \}$ .

If we define $V _ { N } ( \cdot )$ and $J _ { N } ( \cdot )$ as in (3.17) and (3.18), respectively, then the MPC problem $\mathbb { P } _ { N } ( x )$ at state x is, as before

$$\mathbb {P} _ {N} (x): \quad \inf _ {\boldsymbol {\mu}} \{V _ {N} (x, \boldsymbol {\mu}) \mid \boldsymbol {\mu} \in \mathcal {M} (x) \}$$

in which ${ \mathcal { M } } ( x )$ is the set of feedback policies $\pmb { \mu } = \{ u ( 0 ) , \mu _ { 1 } ( \cdot ) , \ldots ,$ $\mu _ { N - 1 } ( \cdot ) \big \}$ that, for a given initial state x, satisfy the state and control constraints $u ( 0 ) \in \mathbb { U } , \phi ( i ; x , \pmb { \mu } , \mathbf { w } ) \in \mathbb { X } , \phi ( N ; x , \pmb { \mu } , \mathbf { w } ) \in \mathbb { X } _ { f } ,$ , and $\mu _ { i } ( \phi ( i ; x , \pmb { \mu } , \mathbf { w } ) ) \in \mathbb { U }$ , for all $i \in \{ 1 , \ldots , N - 1 \}$ and every admissible disturbance sequence $\mathbf { w } \in \mathcal { W }$ . This is precisely the problem solved by DP in Section 3.3. So the solution obtained by solving $\mathbb { P } _ { N } ( x )$ for the given state x, rather than for every state $\boldsymbol { x } \in \mathcal { X } _ { N }$ as provided by DP, is indeed the DP solution restricted to the sets $X ^ { 0 } ( i ; x ) : = \{ \phi ( i ; x , \pmb \mu ^ { 0 } ( x ) , \mathbf w )$ | $\mathbf { w } \in \mathcal { W } \} , i \in \{ 0 , 1 , \dots , N \}$ . More precisely, the DP solution yields, for each $i \in \{ 0 , 1 , \ldots , N \}$ , the value function $V _ { i } ^ { 0 } ( z )$ and optimal control law $\kappa _ { i } ( z )$ for each $z \in \mathcal X _ { i }$ , whereas the solution to the MPC problem $\mathbb { P } _ { N } ( x )$ yields, for each $i \in \{ 0 , 1 , \ldots , N \}$ , the value function $V _ { i } ^ { 0 } ( z )$ and optimal control law $\kappa _ { i } ( z )$ for each $z \in X ^ { 0 } ( i ; x )$ .
