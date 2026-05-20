# A.13.1 Convex Sets

Definition A.12 (Convex set). A set $S \in \mathbb { R } ^ { n }$ is said to be convex if, for any $x ^ { \prime } , x ^ { \prime \prime } \in S$ and $\lambda \in [ 0 , 1 ] , ( \lambda x ^ { \prime } + ( 1 - \lambda ) x ^ { \prime \prime } ) \in S$ .

Let S be a subset of Rn. We say that co(S) is the convex hull of S if it is the smallest7 convex set containing S.

Theorem A.13 (Caratheodory). Let S be a subset of $\mathbb { R } ^ { n } . ~ I f { \bar { x } } \in c o ( S )$ , then it may be expressed as a convex combination of no more than $n + 1$ points in $S , i . e .$ , there exist $m \leq n + 1$ distinct points, $\{ x _ { i } \} _ { i = 1 } ^ { m }$ , in S such that ${ \bar { x } } = \sum _ { i = 1 } ^ { m } \mu ^ { i } x _ { i } , \mu ^ { i } > 0 , \sum _ { i = 1 } ^ { m } \mu ^ { i } = 1$ .

Proof. Consider the set

$$C _ {s} := \{x \mid x = \sum_ {i = 1} ^ {k _ {x}} \mu^ {i} x _ {i}, x _ {i} \in S, \mu^ {i} \geq 0, \sum_ {i = 1} ^ {k _ {x}} \mu^ {i} = 1, k _ {x} \in \mathbb {I} _ {\geq 0} \}$$

First, it is clear that $S \subset C _ { s }$ . Next, since for any $x ^ { \prime } , x ^ { \prime \prime } \in C _ { s } , \lambda x ^ { \prime } +$ $( 1 - \lambda x ^ { \prime \prime } ) \in C _ { s }$ , for $\lambda \in \ [ 0 , 1 ]$ , it follows that $C _ { s }$ is convex. Hence we must have that co $( S ) \subset C _ { s } $ . Because $C _ { s }$ consists of all the convex combinations of points in S, however, we must also have that $C _ { s } \subset$ co(S). Hence $C _ { s } = \mathtt { c o } ( S )$ . Now suppose that

$$\bar {x} = \sum_ {i = 1} ^ {\bar {k}} \bar {\mu} ^ {i} x _ {i}$$

with $\bar { \mu } ^ { i } \geq 0 , i = 1 , 2 , \ldots , \bar { k } , \sum _ { i = 1 } ^ { \bar { k } } \bar { \mu } ^ { i } = 1$ . Then the following system of equations is satisfied

$$
\sum_ {i = 1} ^ {\bar {k}} \bar {\mu} ^ {i} \left[ \begin{array}{c} x _ {i} \\ 1 \end{array} \right] = \left[ \begin{array}{c} \bar {x} \\ 1 \end{array} \right] \tag {A.3}
$$

with $\bar { \mu } ^ { i } \geq 0$ . Suppose that $\bar { k } > n + 1$ . Then there exist coefficients $\alpha ^ { j } , ~ j = 1 , 2 , \ldots , \bar { k }$ , not all zero, such that

$$
\sum_ {i = 1} ^ {\bar {k}} \alpha^ {i} \left[ \begin{array}{c} x _ {i} \\ 1 \end{array} \right] = 0 \tag {A.4}
$$

Adding (A.4) multiplied by θ to (A.3) we get

$$
\sum_ {i = 1} ^ {\bar {k}} (\bar {\mu} ^ {i} + \theta \alpha^ {i}) \left[ \begin{array}{c} x _ {i} \\ 1 \end{array} \right] = \left[ \begin{array}{c} \bar {x} \\ 1 \end{array} \right]
$$
