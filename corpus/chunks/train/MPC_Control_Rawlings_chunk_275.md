in which $x ^ { f } ( j ; x , i )$ is the solution of $x ^ { + } = f ( x , \kappa _ { f } ( x ) )$ at time j if the initial state is x at time i, $u ^ { f } ( j ; x , i ) = \kappa _ { f } ( x ^ { f } ( j ; x , i ) )$ , and $\kappa _ { f } ( \cdot )$ is the local control law that satisfies the stability assumptions. The second inequality follows from the fact that the control sequence $\{ u ^ { f } ( j ; x , i ) \mid$ | $i \in \mathbb { I } _ { i : N - 1 } \}$ is feasible for $\mathbb { P } _ { N } ^ { \beta } ( x ) { \mathrm { ~ i f ~ } } x \in \mathbb { X } _ { f }$ . Suppose contrary to what is to be proved, that there exists a $i \in \mathbb { I } _ { 0 : N - 1 }$ such that $\boldsymbol { x } ^ { \beta } ( i ; \boldsymbol { x } ) \in \mathbb { X } _ { f } ,$ . By the principle of optimality, the control sequence $\{ u ^ { \beta } ( i ; x ) , u ^ { \beta } ( i \stackrel { . } { + }$ $1 ; x ) , \ldots , u ^ { \beta } ( N - 1 ; x ) .$ } is optimal for $\mathbb { P } _ { N - i } ^ { \beta } ( x ^ { \beta } ( i ; x ) )$ . Hence

$$\beta V _ {f} (x ^ {\beta} (i; x)) \geq \hat {V} _ {N - i} ^ {\beta} (x ^ {\beta} (i; x)) \geq \beta V _ {f} (x ^ {\beta} (N; x)) > \beta a$$

since $x ^ { \beta } ( N ; x ) \notin \mathbb { X } _ { f }$ contradicting the fact that $\boldsymbol { x } ^ { \beta } ( i ; \boldsymbol { x } ) \in \mathbb { X } _ { f }$ . This proves the lemma.

For all $\beta \geq 1$ , let the set $\Gamma _ { N } ^ { \beta }$ be defined by

$$\Gamma_ {N} ^ {\beta} := \{x \mid \hat {V} _ {N} ^ {\beta} (x) \leq N d + \beta a \}$$

We assume in the sequel that there exists a $d > 0$ such $\ell ( x , u ) \geq d$ for all $x \in \mathbb { X } \backslash \mathbb { X } _ { f }$ and all $u \in \mathbb { U }$ . The following result is due to Limon et al. (2006).

Theorem 2.39 (MPC stability; no terminal constraint). The origin is asymptotically or exponentially stable for the closed-loop system $x ^ { + } =$ $f ( x , \dot { \kappa } _ { N } ^ { \beta } ( x ) )$ with a region of attraction $\Gamma _ { N } ^ { \beta }$ . The set $\Gamma _ { N } ^ { \beta }$ is positive invariant for $x ^ { + } = f ( x , \kappa _ { N } ^ { \beta } ( x ) )$ .

Proof. From the Lemma, $x ^ { \beta } ( N ; x ) \notin \mathbb { X } _ { f }$ implies ${ x ^ { \beta } } ( i ; x ) \notin \mathbb { X } _ { f }$ for all $i \in \mathbb { I } _ { 0 : N }$ . This, in turn, implies

$$\hat {V} _ {N} ^ {\beta} (x) > N d + \beta a$$
