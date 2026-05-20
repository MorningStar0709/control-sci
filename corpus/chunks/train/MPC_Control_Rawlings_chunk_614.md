where, for all $i , z ( i ) : = \bar { \phi } ( i ; z , \mathbf { v } )$ , the solution of $z ^ { + } = A x + B \nu$ at time i if the initial state at time 0 is z and the nominal control sequence is $\mathbf { v } = \{ \nu ( 0 ) , \nu ( 1 ) , \ldots , \nu ( N - 1 ) \}$ . In (5.28), $\mathbb { Z } _ { f } \ \subseteq \ \mathbb { Z } _ { N }$ is the terminal constraint set and $z ( i )$ is the predicted state at time $k + i$ which is why $z ( i )$ is required to lie in the set $\mathbb { Z } _ { k + i }$ and $\nu ( i )$ to lie in $\mathbb { V } _ { k + i } ;$ clearly $\mathbb { Z } _ { f } \subseteq \mathbb { Z } _ { i }$ for all $i \geq N$ so there is no need to make the terminal constraint set time varying. Let $\mathbf { v } ^ { 0 } ( z , k ) = \{ \nu ^ { 0 } ( 0 ; z , k ) , \nu ^ { 0 } ( 1 ; z , k ) , \ldots , \nu ^ { 0 } ( N ; z , k ) \}$ denote the minimizing control sequence; the stage cost $\ell ( \cdot )$ is chosen to ensure uniqueness of $\mathbf { v } ^ { 0 } ( z , k )$ . The implicit MPC control law for the nominal system is $\bar { \kappa } _ { N } ( \cdot )$ defined by

$$\bar {\kappa} _ {N} (z, k) := \nu^ {0} (0; z, k)$$

where $\nu ^ { 0 } ( 0 ; z , k )$ is the first element in the sequence $\mathbf { v } ^ { 0 } ( z , k )$ . The domain of $\bar { V } _ { N } ^ { 0 } ( \cdot , k )$ and $\mathbf { v } ( \cdot , k )$ and, hence, of $\bar { \kappa } _ { N } ( \cdot , k )$ , is $\mathcal { Z } _ { N } ( k )$ defined by

$$\mathcal {Z} _ {N} (k) := \{z \in \mathbb {Z} _ {k} \mid \mathcal {V} _ {N} (z, k) \neq \emptyset \}$$

${ \mathcal { Z } } _ { N } ( k )$ is the set of states z at time k that can be robustly steered to $\mathbb { Z } _ { f }$ in N steps by an admissible control v. Because the constraints become weaker with time, the domain $\mathcal { Z } _ { N } ( k + 1 )$ of $\bar { V } _ { N } ^ { 0 } ( \cdot , k + 1 )$ is larger than the domain $\mathcal { Z } _ { N } ( k )$ of $\bar { V } _ { N } ^ { 0 } ( \cdot , k )$ for all $k > 0 ;$ ; the sequence $\{ \mathcal { Z } _ { N } ( k ) \}$ is monotonically nondecreasing.

If the terminal cost $V _ { f } ( \cdot )$ and terminal constraint set $\mathbb { Z } _ { f }$ satisfy the stability Assumptions 2.12 and 2.13 of Chapter 2, and if Assumption 5.9 is satisfied, the value function $\bar { V } _ { N } ^ { 0 } ( \cdot )$ satisfies, for all $k \in \mathbb { I } _ { \geq 0 }$

$$
\begin{array}{l} \bar {V} _ {N} ^ {0} (z, k) \geq \ell (z, \bar {\kappa} _ {N} (z, k)) \quad \forall z \in \mathcal {Z} _ {N} (k) \\ \Delta \bar {V} _ {N} ^ {0} (z, k) \leq - \ell (z, \bar {\kappa} _ {N} (z, k)) \quad \forall z \in \mathcal {Z} _ {N} (k) \\ \bar {V} _ {N} ^ {0} (z, k) \leq V _ {f} (z) \quad \forall z \in \mathbb {Z} _ {f} \\ \end{array}
$$
