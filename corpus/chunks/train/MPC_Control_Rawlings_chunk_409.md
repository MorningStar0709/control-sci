$$
\left[ \begin{array}{c} e \\ z \end{array} \right] = T \left[ \begin{array}{c} x \\ z \end{array} \right], \quad T := \left[ \begin{array}{c c} I & - I \\ 0 & I \end{array} \right]
$$

since $e : = x - z$ . Since T is invertible, the two composite systems are equivalent and stability for one system implies stability for the other. We assume that the value function $\bar { V } _ { N } ^ { 0 } ( \cdot )$ for the nominal optimal control problem has the usual properties:

$$\bar {V} _ {N} ^ {0} (z) \geq c _ {1} | z | ^ {2} + c _ {1} | \bar {\kappa} _ {N} (z) | ^ {2}\bar {V} _ {N} ^ {0} (f (z, \bar {\kappa} _ {N} (z))) \leq \bar {V} _ {N} ^ {0} (z) - c _ {1} | z | ^ {2}\bar {V} _ {N} ^ {0} (z) \leq c _ {2} | z | ^ {2}$$

for all $z \in \mathcal { Z } _ { N }$ ; these properties arise when the stage cost is quadratic and positive definite, $\mathcal { Z } _ { N }$ is bounded, and an appropriate terminal cost and constraint set are employed. The first inequality, which is a minor extension of the inequality normally employed, follows from the definition of $\bar { V } _ { N } ^ { 0 } ( \cdot )$ and of $\ell ( \cdot )$ . It follows from these conditions that there exists a $c > 0$ such that

$$| \bar {\kappa} _ {N} (z) | \leq c | z |$$

for all $z \in \mathcal { Z } _ { N }$ . For all $\alpha \geq 0$ , let $\operatorname { l e v } _ { \alpha } V$ denote the sublevel set of $\bar { V } _ { N } ^ { 0 } ( \cdot )$ defined by

$$\operatorname{lev} _ {\alpha} V := \left\{z \in \mathcal {Z} _ {N} \mid \bar {V} _ {N} ^ {0} (z) \leq \alpha \right\}$$

and let $S : = S _ { K } ( \infty )$ ; S is robust positive invariant for $e ^ { + } = A _ { K } e + w$ , $w \in \mathbb { W }$ and, from Assumption $3 . 1 9 , S \subset ( 1 / 4 ) \mathbb { X }$ and $K S \subset ( 1 / 4 ) \mathbb { U }$ .

We show below that, for all $\epsilon \in ( 0 , 3 / 4 ]$ , there exists a $\delta > 0$ such that $( z ( 0 ) , e ( 0 ) ) \ \leq \ \delta$ implies $z ( i ) \in \epsilon ( 3 / 4 ) \mathbb { X }$ and $e ( i ) ~ \in ~ \epsilon S$ for all $i \in \mathbb { I } _ { \geq 0 }$ thereby establishing robust stability of the origin for the composite system. The upper limit of $3 / 4$ on  is not a limitation since the analysis shows that, for every $\epsilon \geq 3 / 4$ , there exists a $\delta > 0$ such that $( z ( 0 ) , e ( 0 ) ) \leq \delta$ implies $z ( i ) \in \epsilon ^ { * } \mathbb { X }$ and $e ( i ) \in \epsilon ^ { * } S$ for all $i \in \mathbb { I } _ { \geq 0 }$ where $\epsilon ^ { * } = 3 / 4 \leq \epsilon$ .
