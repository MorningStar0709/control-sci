# 2.4.5 Further Properties of the Value Function $V _ { N } ^ { 0 } ( \cdot )$

Lemma 2.14 shows that the value function $V _ { N } ^ { 0 } ( \cdot )$ has a descent property that makes it a suitable candidate for a Lyapunov function that may be used to establish stability of the origin for a wide variety of MPC systems. To proceed, we postulate two alternative conditions on the stage cost $\ell ( \cdot )$ and terminal cost $V _ { f } ( \cdot )$ required to show that $V _ { N } ^ { 0 } ( \cdot )$ has the properties given in Appendix B, which are sufficient to establish stability of the origin. Our additional assumption is:

Assumption 2.16 (Bounds on stage and terminal costs).

(a) The stage cost $\ell ( \cdot )$ and the terminal cost $V _ { f } ( \cdot )$ satisfy

$$\ell (x, u) \geq \alpha_ {1} (| x |) \quad \forall x \in \mathcal {X} _ {N}, \forall u \in \mathbb {U}V _ {f} (x) \leq \alpha_ {2} (| x |) \quad \forall x \in \mathbb {X} _ {f}$$

in which $\alpha _ { 1 } ( \cdot )$ and $\alpha _ { 2 } ( \cdot )$ are $\mathcal { K } _ { \infty }$ functions, or

(b) The stage cost $\ell ( \cdot )$ and the terminal cost $V _ { f } ( \cdot )$ satisfy

$$\ell (x, u) \geq c _ {1} | x | ^ {a} \quad \forall x \in \mathcal {X} _ {N}, \forall u \in \mathbb {U}V _ {f} (x) \leq c _ {2} | x | ^ {a} \quad \forall x \in \mathbb {X} _ {f}$$

for some $c _ { 1 } > 0 , c _ { 2 } > 0$ , and $\alpha > 0$ .

Note that Assumption 2.16(b) implies 2.16(a) and that both Assumptions 2.16(a) and 2.16(b) are satisfied with $a = 2 \operatorname { i f } \ell ( x , u ) = ( 1 / 2 ) ( x ^ { \prime } Q x$ $+ u ^ { \prime } R u )$ and Q and R are positive definite. With this extra assumption, $V _ { N } ^ { 0 } ( \cdot )$ has the properties summarized in the following result.

Proposition 2.17 (Optimal value function properties).

(a) Suppose that Assumptions 2.2, 2.3, 2.12, 2.13, and $2 . 1 6 ( a )$ are satisfied. Then there exist ${ \mathcal K } _ { \infty }$ functions $\alpha _ { 1 } ( \cdot )$ and $\alpha _ { 2 } ( \cdot )$ such that $V _ { N } ^ { 0 } ( \cdot )$ has
