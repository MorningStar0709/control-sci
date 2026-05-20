# Exercise B.7: A Lipschitz continuous converse theorem for exponential stability

Consider the system $x ^ { + } = f ( x ) , f ( 0 ) = 0$ , with function $f : D \to \mathbb { R } ^ { n }$ Lipschitz continuous on compact set $D \subset \mathbb { R } ^ { n }$ containing the origin in its interior. Choose $R > 0$ such that $B _ { R } \subseteq D$ . Assume that there exist scalars $c > 0$ and $\lambda \in ( 0 , 1 )$ such that

$$\left| \phi (k; x) \right| \leq c | x | \lambda^ {k} \quad \text { for all } | x | \leq r, \quad k \geq 0$$

with $r : = R / c$ .

Show that there exists a Lipschitz continuous Lyapunov function $V ( \cdot )$ satisfying for all $\boldsymbol { x } \in B _ { r }$

$$a _ {1} | x | ^ {2} \leq V (x) \leq a _ {2} | x | ^ {2}V (f (x)) - V (x) \leq - a _ {3} | x | ^ {2}$$

with $a _ { 1 } , a _ { 2 } , a _ { 3 } > 0$

Hint: Use the proposed Lyapunov function of Exercise B.3 with $\sigma = 2$ . See also (Khalil, 2002, Exercise 4.68).
