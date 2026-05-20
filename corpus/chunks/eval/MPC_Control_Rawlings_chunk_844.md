Theorem A.15 can be used to prove the following special case of Theorem A.14:

Corollary A.16 (Existence of separating hyperplane). Let $S _ { 1 } , S _ { 2 }$ be two compact convex sets in $\mathbb { R } ^ { n }$ such that $S _ { 1 } \cap S _ { 2 } = \emptyset$ . Then there exists a hyperplane which separates $S _ { 1 }$ and $S _ { 2 }$ .

Proof. Let $C = S _ { 1 } - S _ { 2 } : = \{ x _ { 1 } - x _ { 2 } \mid x _ { 1 } \in S _ { 1 } , x _ { 2 } \in S _ { 2 } \}$ . Then C is convex and compact and 0 6∈ C. Let ${ \hat { x } } = ( { \hat { x } } _ { 1 } - { \hat { x } } _ { 2 } ) = \arg \operatorname* { m i n } \{ | x | ^ { 2 } | x \in C \}$ , where $\hat { x } _ { 1 } \in S _ { 1 }$ and $\hat { x } _ { 2 } \in S _ { 2 }$ . Then, by Theorem A.15

$$\langle x - \hat {x}, \hat {x} \rangle \geq 0, \text { for all } x \in C \tag {A.5}$$

Let $x = x _ { 1 } - \hat { x } _ { 2 }$ , with $x _ { 1 } \in S _ { 1 }$ . Then (A.5) leads to

$$\langle x _ {1} - \hat {x} _ {2}, \hat {x} \rangle \geq | \hat {x} | ^ {2} \tag {A.6}$$

for all $x _ { 1 } \in S _ { 1 }$ . Similarly, letting $x = \hat { x } _ { 1 } - x _ { 2 }$ , in (A.5) yields

$$\langle \hat {x} _ {1} - x _ {2}, \hat {x} \rangle \geq | \hat {x} | ^ {2} \tag {A.7}$$

for all $x _ { 2 } \in S _ { 2 }$ . The inequality in (A.7) implies that

$$\langle \hat {x} _ {1} - \hat {x} _ {2} + \hat {x} _ {2} - x _ {2}, \hat {x} \rangle \geq | \hat {x} | ^ {2}$$

Since $\hat { x } _ { 1 } - \hat { x } _ { 2 } = \hat { x }$ , we obtain

$$\langle x _ {2} - \hat {x} _ {2}, \hat {x} \rangle \leq 0 \tag {A.8}$$

for all $x _ { 2 } ~ \in ~ S _ { 2 }$ . The desired result follows from (A.6) and (A.8), the separating hyperplane H being $\{ x \in \mathbb { R } ^ { n } \mid \langle \hat { x } , x - \hat { x } _ { 2 } \rangle = 0 \}$ .

Definition A.17 (Support hyperplane). Suppose $S \subset \mathbb { R } ^ { n }$ is convex. We say that $H = \{ x \mid \langle x - { \bar { x } } , \nu \rangle = 0 \}$ is a support hyperplane to S through x¯ with inward (outward) normal v if $\bar { x } \in \top S )$ and

$$\langle x - \bar {x}, v \rangle \geq 0 (\leq 0) \text { for all } x \in S$$

Theorem A.18 (Convex set and halfspaces). A closed convex set is equal to the intersection of the halfspaces which contain it.

Proof. Let C be a closed convex set and A the intersection of halfspaces containing C. Then clearly $C \subset A$ . Now suppose ${ \bar { x } } \notin C .$ . Then there exists a support hyperplane H which separates strictly x¯ and C so that x¯ does not belong to one halfspace containing C. It follows that ${ \bar { x } } \notin A .$ . Hence $C ^ { c } \subset A ^ { c }$ which leads to the conclusion that $A \subset C$ .

An important example of a convex set is a convex cone.
