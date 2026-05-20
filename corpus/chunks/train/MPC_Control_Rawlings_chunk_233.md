Proposition 2.18 (Extension of upper bound to compact set). Suppose that Assumptions 2.2, 2.3, 2.12, and 2.13 hold, that $\mathbb { X } _ { f }$ contains the origin in its interior, and that $\complement _ { f } \subseteq X$ where X is a compact set in $\mathbb { R } ^ { n }$ . If there exists a $\mathcal { K } _ { \infty }$ function $\alpha ( \cdot )$ such that $V _ { N } ^ { 0 } ( x ) \leq \alpha ( | x | )$ for all $\boldsymbol { x } \in \mathbb { X } _ { f }$ , then there exists another $\mathcal { K } _ { \infty }$ function $\beta ( \cdot )$ such that $V _ { N } ^ { 0 } ( x ) \le \beta ( | x | )$ for all $x \in X$ .

Proof. Because the origin lies in the interior of $\mathbb { X } _ { f }$ , there exists a $d > 0$ such that $\{ x \mid | x | \leq d \} \subset \mathbb { X } _ { f }$ . Let $e \ = \ \operatorname* { m a x } \{ \alpha ( | x | ) \ | \ | x | \ \leq \ d \} \ > \ 0 ;$ then $\alpha ( | x | ) \geq e$ for all $x \in X \backslash \mathbb { X } _ { f }$ . Since X is compact by assumption, U is compact by Assumption 2.3, and $V _ { N } ( \cdot )$ continuous by Proposition 2.4, there exists an upper bound $c > e$ for $V _ { N } ( \cdot )$ on $X \times \mathbb { U } ^ { N }$ and, hence, for $V _ { N } ^ { 0 } ( \cdot )$ on X. Thus $\beta ( \cdot ) : = ( c / e ) \alpha ( \cdot )$ is a $\mathcal { K } _ { \infty }$ function satisfying $\beta ( | x | ) \geq \alpha ( | x | )$ for all x in X and $\beta ( | x | ) \geq c$ for all $x \in X \backslash \mathbb { X } _ { f }$ . Hence $\beta ( \cdot )$ is a $\mathcal { K } _ { \infty }$ function satisfying $V _ { N } ^ { 0 } ( x ) \le \beta ( | x | )$ for all $x \in X$ . 

An immediate consequence of Propositions 2.17 and 2.18 is the following result.

Proposition 2.19 (Lyapunov function on $x _ { N } )$ . Suppose Assumptions 2.2, $2 . 3 , 2 . I 2 , 2 . I 3 ,$ and 2.16 are satisfied, that $\mathbb { X } _ { f }$ has an interior containing the origin, and that $x _ { N }$ is bounded. Then, for all $\boldsymbol { x } \in \mathcal { X } _ { N }$

$$V _ {N} ^ {0} (x) \geq \alpha_ {1} (| x |) \tag {2.20}V _ {N} ^ {0} (x) \leq \alpha_ {2} (| x |) \tag {2.21}V _ {N} ^ {0} (f (x, \kappa_ {N} (x))) \leq V _ {N} ^ {0} (x) - \alpha_ {1} (| x |) \tag {2.22}$$

in which $\alpha _ { 1 } ( \cdot )$ and $\alpha _ { 2 } ( \cdot )$ are $\mathcal { K } _ { \infty }$ functions.

Proof. The result follows directly from Proposition 2.18 since the assumption that the set $x _ { N }$ is bounded, coupled with the fact that it is closed, as shown in Proposition 2.11, implies that it is compact. 
