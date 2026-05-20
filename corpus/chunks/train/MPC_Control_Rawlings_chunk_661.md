Lemma 6.4 (Exponential stability of suboptimal MPC). The origin is exponentially stable for the closed-loop system under suboptimal MPC with region of attraction $x _ { N }$ if either of the following assumptions holds

(a) U is compact. In this case, $x _ { N }$ may be unbounded.

(b) $x _ { N }$ is compact. In this case U may be unbounded.

Exercises 6.7 and 6.8 explore what to conclude about exponential stability when both U and $x _ { N }$ are unbounded.

Proof. First we show that the origin of the extended state $( x , \mathbf { u } )$ is exponentially stable for $x ( 0 ) \in \mathcal { X } _ { N }$ .

(a) For the case U compact, we use the same argument used to prove Proposition 2.18 of Chapter 2. We have $\left| \mathbf { u } \right| \leq d \left| x \right| , x \in r { \mathcal { B } }$ . Consider the optimization

$$\max _ {\mathbf {u} \in \mathbb {U} ^ {N}} | \mathbf {u} | = s > 0$$

The solution exists by the Weierstrass theorem since U is compact, which implies $\mathbb { U } ^ { N }$ is compact. Then we have $\vert \mathbf { u } \vert ~ \le ~ ( s / r ) \left. x \right.$ for $_ x \in$ $\mathcal { X } _ { N } \backslash r \mathcal { B } ,$ so we have $| \mathbf { u } | \leq d ^ { \prime } \left| x \right|$ for $\boldsymbol { x } \in \mathcal { X } _ { N }$ in which $d ^ { \prime } = \operatorname* { m a x } ( d , s / r )$ .

(b) For the case $x _ { N }$ compact, consider the optimization

$$\max _ {x \in \mathcal {X} _ {N}} V (x, \mathbf {h} (x)) = \bar {V} > 0$$

The solution exists because $x _ { N }$ is compact and $\mathbf { h } ( \cdot )$ and $V ( \cdot )$ are continuous. Define the compact set U¯ by

$$\bar {\mathbb {U}} = \{\mathbf {u} \mid V (x, \mathbf {u}) \leq \bar {V}, x \in \mathcal {X} _ {N} \}$$

The set is bounded because $V ( x , \mathbf { u } ) \geq a \left| ( x , \mathbf { u } ) \right| ^ { 2 } \geq a \left| \mathbf { u } \right| ^ { 2 }$ . The set is closed because V is continuous. The significance of this set is that for all $k \geq 0$ and all $x \in \mathcal { X } _ { N } , { \mathbf { u } ( k ) } \in \bar { \mathbb { U } }$ . Therefore we have established that $x _ { N }$ compact implies u(k) evolves in a compact set as in the previous case when U is assumed compact. Using the same argument as in that case, we have established that there exists $d ^ { \prime } > 0$ such that $| \mathbf { u } | \leq d ^ { \prime } \left| x \right|$ for all $\boldsymbol { x } \in \mathcal { X } _ { N }$ .

For the two cases, we therefore have established for all $x \in \mathcal { X } _ { N }$ , $\mathbf { u } \in \mathbb { U } ^ { N }$ (case (a)) or $\mathbf { u } \in \bar { \mathbb { U } }$ (case (b))
