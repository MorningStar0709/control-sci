# Proof.

(a) First we show that $f ( X )$ is closed. Thus, let $\{ f ( x _ { i } ) \mid i \in \mathbb { I } _ { \geq 0 } \}$ , with $x _ { i } \in X$ , be any sequence in $f ( X )$ such that $f ( x _ { i } )  y$ as $i  \infty$ . Since $\{ x _ { i } \}$ is in a compact set X, there exists a subsequence $\{ x _ { i } \mid i \in K \}$ such that $x _ { i } \stackrel { K } { \to } x ^ { * } \in X$ as $i  \infty$ . Since $f ( \cdot )$ is continuous, $f ( x _ { i } ) \stackrel { K } {  } f ( x ^ { * } )$ as $i  \infty$ . But y is the limit of $\{ f ( x _ { i } ) \mid i \in \mathbb { I } _ { \geq 0 } \}$ and hence it is the limit of any subsequence of $\{ f ( x _ { i } ) \}$ . We conclude that $y = f ( x ^ { * } )$ and hence that $y \in f ( X ) , \operatorname { i . e . , } f ( X )$ is closed.

(b) Next, we prove that f (X) is bounded. Suppose $f ( X )$ is not bounded. Then there exists a sequence $\{ x _ { i } \}$ such that $| f ( x _ { i } ) | \geq i$ for all $i \in \mathbb { I } _ { \geq 0 }$ . Now, since $\{ x _ { i } \}$ is in a compact set, there exists a subsequence $\{ x _ { i } \mid i \in$ $K \}$ such that $x _ { i } \stackrel { K } {  } x ^ { * }$ with $x ^ { * } \in X$ , and $f ( x _ { i } ) \stackrel { K } {  } f ( x ^ { * } )$ by continuity of $f ( \cdot )$ . Hence there exists an $i _ { 0 }$ such that for any $j > i > i _ { 0 } , j , i \in { \cal K }$

$$\left| f \left(x _ {j}\right) - f \left(x _ {i}\right) \right| \leq \left| f \left(x _ {j}\right) - f \left(x ^ {*}\right) \right| + \left| f \left(x _ {i}\right) - f \left(x ^ {*}\right) \right| < 1 / 2 \tag {A.2}$$

Let $i \geq i _ { 0 }$ be given. By hypothesis there exists a $j \in K , j \ge i$ such that $| f ( x _ { j } ) | \geq j \geq | f ( x _ { i } ) | + 1$ . Hence

$$\left| f (x _ {j}) - f (x _ {i}) \right| \geq \left| \left| f (x _ {j}) \right| - \left| f (x _ {i}) \right| \right| \geq 1$$

which contradicts (A.2). Thus $f ( X )$ must be bounded, which completes the proof.

Let $Y \subset \mathbb { R }$ . Then inf(Y ), the infimum of Y , is defined to be the greatest lower bound6 of Y . If inf $( Y ) \in Y$ , then min $( Y ) : = \operatorname* { m i n } \{ y \mid$ $y \in Y \}$ , the minimum of the set Y , exists and is equal to inf(Y ). The infimum of a set Y always exists if Y is not empty and is bounded from below, in which case there always exist sequences $\{ y _ { i } \} \in Y$ such that $\qquad y _ { i } \setminus \beta : = \operatorname { i n f } ( Y )$ as $i  \infty$ . Note that $\beta : = \operatorname { i n f } ( Y )$ does not necessarily lie in the set Y .

Proposition A.7 (Weierstrass). Suppose that $f : \mathbb { R } ^ { n }  \mathbb { R }$ is continuous and that $X \subset \mathbb { R } ^ { n }$ is compact. Then there exists an ${ \hat { x } } \in X$ such that
