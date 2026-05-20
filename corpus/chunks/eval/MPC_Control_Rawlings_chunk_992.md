# C.2.4 Nonconvex Problems

We first obtain a necessary condition of optimality for the problem min $\{ f ( u ) \mid u \in U \}$ where $f ( \cdot )$ is differentiable but not necessarily convex and $U \subset \mathbb { R } ^ { m }$ is not necessarily convex; this result generalizes the necessary condition of optimality in Proposition C.9.

Proposition C.14 (Necessary condition for nonconvex problem). A necessary condition for u to be locally optimal for the problem of minimizing a differentiable function f (·) over the set U is

$$d f (u; h) = \langle \nabla f (u), h \rangle \geq 0, \forall h \in \mathcal {T} _ {U} (u)$$

which is equivalent to the condition

$$- \nabla f (\boldsymbol {u}) \in \hat {N} _ {U} (\boldsymbol {u})$$

Proof. Suppose, contrary to what we wish to prove, that there exists a $h \in \mathcal { T } _ { U } ( u )$ and a $\delta > 0$ such that $\langle \nabla f ( u ) , h \rangle = - \delta < 0$ . Because $h \in \mathcal { T } _ { U } ( u )$ , there exist sequences $h { \xrightarrow [ { U } ] { \nu } } h$ and $\lambda ^ { \nu } \searrow 0$ such that $u ^ { \nu } : =$ $u + \lambda ^ { \nu } h ^ { \nu }$ converges to u and satisfies $u ^ { \nu } \in U$ for all $\nu \in \mathbb { I } _ { \geq 0 }$ . Then

$$f (u ^ {\nu}) - f (u) = \langle \nabla f (u), \lambda^ {\nu} h ^ {\nu} \rangle + o (\lambda^ {\nu} | h ^ {\nu} |)$$

Hence

$$[ f (u ^ {\nu}) - f (u) ] / \lambda^ {\nu} = \langle \nabla f (u), h ^ {\nu} \rangle + o (\lambda^ {\nu}) / \lambda^ {\nu}$$

where we make use of the fact that $| h ^ { \nu } |$ is bounded for ν sufficiently large. It follows that

$$[ f (u ^ {\nu}) - f (u) ] / \lambda^ {\nu} \rightarrow \langle \nabla f (u), h \rangle = - \delta$$

so that there exists a finite integer j such that $f ( u ^ { j } ) - f ( u ) \leq - \lambda ^ { j } \delta / 2 <$ < 0 which contradicts the local optimality of u. Hence $\langle \nabla f ( { \boldsymbol { u } } ) , h \rangle \geq 0$ for all $h \in \mathcal { T } _ { U } ( u )$ . That $- \nabla f ( u ) \in \hat { N } _ { U } ( u )$ follows from Proposition C.7.

A more concise proof proceeds as follows Rockafellar and Wets (1998). Since $f ( \nu ) - f ( u ) = \langle \nabla f ( u ) , \nu - u \rangle + o ( | \nu - u | )$ it follows that $\langle - \nabla f ( u ) , \nu - u \rangle = o ( | \nu - u | ) - ( f ( \nu ) - f ( u ) )$ . Because u is locally optimal, $f ( \nu ) - f ( u ) \geq 0$ for all v in the neighborhood of u so that $\left. - \nabla f ( u ) , \nu - u \right. \leq o ( | \nu - u | )$ which, by (C.15), is the definition of a normal vector. Hence $- \nabla f ( u ) \in \hat { N } _ { U } ( u )$ .
