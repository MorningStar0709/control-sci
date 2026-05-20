Suppose that the state x is required to lie in the closed set $\mathbb { X } \subset \mathbb { R } ^ { n }$ . In order to show that it is possible to ensure a decrease of a Lyapunov function, as in (B.11), in the presence of the state constraint $x \in \mathbb { X } ,$ , we assume that there exists a control invariant set $X \subseteq \mathbb { X }$ for $\begin{array} { r l } { x ^ { + } } & { { } = } \end{array}$ $f ( x , u , w ) , u \in \mathbb { U } , w \in \mathbb { W }$ . This enables us to obtain a control law that keeps the state in X and, hence, in X, and, under suitable conditions, to satisfy a variant of (B.11).

Definition B.30 (CLF (constrained)). Suppose the sets X and ${ \mathcal { A } } , X \supset { \mathcal { A } }$ , are control invariant for $x ^ { + } = f ( x , u ) , u \in \mathbb { U } .$ . A function $V : X \to \mathbb { R } _ { \geq 0 }$ is said to be a control-Lyapunov function in X for the system $\begin{array} { r l } { x ^ { + } } & { { } = } \end{array}$ $f ( x , u ) , u \in \mathbb { U }$ , and set A in X if there exist functions $\alpha _ { i } \in \mathcal { K } _ { \infty } , i = 1 , 2$ and $\alpha _ { 3 } \in \mathcal { P D }$ , defined on X, such that for any $x \in X$ ,

$$
\begin{array}{l} V (x) \geq \alpha_ {1} (| x | _ {\mathcal {A}}) \\ V (x) \leq \alpha_ {2} (| x | _ {\mathcal {A}}) \\ \inf _ {u \in \mathbb {U}} \left\{V (f (x, u)) \mid f (x, u) \in X \right\} \leq V (x) - \alpha_ {3} (| x | _ {\mathcal {A}}) \\ \end{array}
$$

Finally we consider the constrained case in the presence of disturbances. First we define control invariance in the presence of disturbances.

Definition B.31 (Control invariance (disturbances, constrained)). The set A is control invariant for $x ^ { + } = f ( x , u , w ) , u \in \mathbb { U } , w \in \mathbb { W } { \mathrm { i f } } ,$ , for all $x \in { \mathcal { A } }$ , there exists a $u \in \mathbb { U }$ such that $f ( x , u , w ) \in \mathcal { A }$ for all $w \in \mathbb { W }$ (or $F ( x , u ) \subseteq { \mathcal { A } }$ where $F ( x , u ) : = \{ f ( x , u , w ) \mid w \in \mathbb { W } \}$ .

Next, we define what we mean by a control-Lyapunov function in this context.
