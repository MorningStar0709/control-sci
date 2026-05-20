$$\langle m ^ {j}, u \rangle - \langle n ^ {j}, x \rangle - p ^ {j} > 0, \forall j \in I ^ {0} (x, u)$$

Since $x \in { \mathcal { X } }$ , there exists a ${ \bar { u } } \in { \mathcal { U } } ( x )$ so that

$$\langle m ^ {j}, \bar {u} \rangle - \langle n ^ {j}, x \rangle - p ^ {j} \leq 0, \forall j \in I ^ {0} (x, u)$$

Subtracting these two inequalities yields

$$\langle m ^ {j}, u - \bar {u} \rangle > 0, \forall j \in I ^ {0} (x, u)$$

But then, for all $\lambda \in \Lambda _ { I ^ { 0 } ( x , u ) }$ , it follows that $\begin{array} { r } { \big | \sum _ { j \in I ^ { 0 } ( x , u ) } \lambda ^ { j } m ^ { j } ( u - \bar { u } ) \big | > } \end{array}$ 0, so that

$$\sum_ {j \in I ^ {0} (x, u)} \lambda^ {j} m ^ {j} \neq 0$$

It follows that $I ^ { 0 } ( x , u ) \in \mathcal { D }$ . Hence

$$\left| \sum_ {j \in I ^ {0} (x, u)} \lambda^ {j} m ^ {j} \right| > \delta , \forall \lambda \in \Lambda_ {I ^ {0} (x, u)}$$

Now take any $g \in \partial _ { u } f ( x , u ) = \mathrm { c o } \{ m ^ { j } \mid j \in I ^ { 0 } ( x , u ) \}$ (co denotes “convex hull”). There exists a $\lambda \in \Lambda _ { I ^ { 0 } ( x , u ) }$ such that $\begin{array} { r } { g = \sum _ { j \in I ^ { 0 } ( x , u ) } \lambda ^ { j } m _ { j } } \end{array}$ . But then $| g | > \delta$ by the inequality above. This proves the claim and, hence, completes the proof of the Corollary.

Continuity of the value function when $U ( x ) ~ = ~ \{ u ~ \mid ~ ( x , u ) ~ \in ~ \mathcal { Z } \}$ . In this section we investigate continuity of the value function for the constrained linear quadratic optimal control problem $\mathbb { P } ( x )$ ; in fact we establish continuity of the value function for the more general problem where the cost is continuous rather than quadratic. We showed in Chapter 2 that the optimal control problem of interest takes the form

$$V ^ {0} (x) = \min _ {u} \{V (x, u) \mid (x, u) \in \mathcal {Z} \}$$

where $\mathcal { Z }$ is a polyhedron in $\mathbb { R } ^ { n } \times \mathbb { U }$ where $\mathbb { U } \subset \mathbb { R } ^ { m }$ is a polytope and, hence, is compact and convex; in MPC problems we replace the control u by the sequence of controls u and m by Nm. Let $u ^ { 0 } : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ be defined by

$$u ^ {0} (x) := \arg \min _ {u} \{V (x, u) \mid (x, u) \in \mathcal {Z} \}$$

and let X be defined by

$$\mathcal {X} := \{x \mid \exists u \text { such that } (x, u) \in \mathcal {Z} \}$$

so that X is the projection of $\mathcal { Z } \subset \mathbb { R } ^ { n } \times \mathbb { R } ^ { m }$ onto $\mathbb { R } ^ { n }$ . Let the set-valued function $U : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ be defined by

$$U (x) := \{u \in \mathbb {R} ^ {m} \mid (x, u) \in Z \}$$
