Stability. Because $\mathbb { X } _ { f }$ contains the origin in its interior, there exists a $\delta _ { 1 } > 0$ such that $\delta _ { 1 } { \mathcal { B } } \subset \mathbb { X } _ { f } ;$ here B denotes the closed unit ball in Rn. Let $\delta \in ( 0 , \delta _ { 1 } ] > 0$ be arbitrary. Let $\phi ( i ; x )$ denote the solution of $x ^ { + } = f ( x )$ at time i if the initial state is x. Suppose that $| x | \le \delta$ so that $x \in \mathbb { X } _ { f }$ . It follows from (2.24) that $V ( x ) \ \leq \ \alpha _ { 2 } ( \delta )$ and from (2.25) that $V ( \dot { \phi } ( i ; x ) ) \le V ( x ) \le \alpha _ { 2 } ( \delta )$ for all $i \in \mathbb { I } _ { \geq 0 }$ . From (2.23), $\vert \phi ( i ; x ) \vert \le \alpha _ { 1 } ^ { - 1 } ( V ( x ( i ) ) ) \le ( \alpha _ { 1 } ^ { - 1 } \circ \alpha _ { 2 } ) ( \delta )$ for all $i \in \mathbb { I } _ { \geq 0 }$ . Hence for all $\varepsilon > 0$ , there exists a $\delta > 0 , \delta : = \operatorname* { m i n } \{ \delta _ { 1 } , ( \alpha _ { 1 } ^ { - 1 } \circ \alpha _ { 2 } ) ^ { - 1 } ( \varepsilon ) \}$ , such that $| x | \le \delta$ implies that $| \phi ( i ; x ) | \leq \varepsilon$ for all $i \in \mathbb { I } _ { \geq 0 }$ . Stability of the origin is established.

Attractivity. The proof of attractivity is similar to the proof of attractivity in Theorem B.11 of Appendix B.

Hence, if we add to the hypotheses of Proposition 2.17 the assumption that $\mathbb { X } _ { f }$ contains the origin in its interior, we can use Theorem 2.22 to establish the asymptotic stability of the origin with a region of attraction $x _ { N }$ for the system $x ^ { + } = f ( x , \kappa _ { N } ( x ) )$ .

In situations where $\mathbb { X } _ { f }$ does not have an interior, such as when $\mathbb { X } _ { f } =$ {0}, we cannot establish an upper bound for $V _ { N } ^ { 0 } ( \cdot )$ from Assumptions 2.12 and 2.13, and resort to the following assumption.

Assumption 2.23 (Weak controllability). There exists a $\mathcal { K } _ { \infty }$ function $\alpha ( \cdot )$ such that

$$V _ {N} ^ {0} (x) \leq \alpha (| x |) \forall x \in \mathcal {X} _ {N}$$

Assumption 2.23 is weaker than a controllability assumption though it bounds the cost of steering an initial state x to $\mathbb { X } _ { f }$ . It confines attention to those initial states that can be steered to $\mathbb { X } _ { f }$ in N steps while satisfying the control and state constraints, and merely requires that the cost of doing so is not excessive.
