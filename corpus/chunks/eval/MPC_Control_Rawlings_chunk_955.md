Definition B.32 (CLF (disturbances, constrained)). Suppose the sets X and ${ \mathcal { A } } , X \supset { \mathcal { A } }$ , are control invariant for $x ^ { + } = f ( x , u , w ) , u \in \mathbb { U } , w \in \mathbb { W }$ . A function $V : X \to \mathbb { R } _ { \geq 0 }$ is said to be a control-Lyapunov function in X for the system $x ^ { + } = f ( x , u , w ) , u \in \mathbb { U } , w \in \mathbb { W }$ and set A if there exist functions $\alpha _ { i } \in \mathcal { K } _ { \infty } , i = 1 , 2$ and $\alpha _ { 3 } \in \mathcal { P D }$ , defined on X, such that for any $x \in X$ ,

$$
\begin{array}{l} V (x) \geq \alpha_ {1} (| x | _ {\mathcal {A}}) \\ V (x) \leq \alpha_ {2} (| x | _ {\mathcal {A}}) \\ \inf _ {u \in \mathbb {U}} \sup _ {z \in F (x, u)} \{V (z) \mid F (x, u) \subseteq X \} \leq V (x) - \alpha_ {3} (| x | _ {\mathcal {A}}) \\ \end{array}
$$

Suppose now that the state x is required to lie in the closed set $\mathbb { X } \subset \mathbb { R } ^ { n }$ . Again, in order to show that there exists a condition similar to (B.11), we assume that there exists a control invariant set $X \subseteq \mathbb { X }$ for $x ^ { + } = f ( x , u , w ) , u \in \mathbb { U } , w \in \mathbb { W }$ . This enables us to obtain a control law that keeps the state in X and, hence, in X, and, under suitable conditions, to satisfy a variant of (B.11).
