for all $u , \nu$ in U. To prove sufficiency, suppose $u \in U$ and that the condition in (C.17) is satisfied. It then follows from (C.19) that $f ( \nu ) \geq$ $f ( u )$ for all $\nu \in U$ so that u is globally optimal. To prove necessity, suppose that u is globally optimal but that, contrary to what we wish to prove, the condition on the right-hand side of (C.17) is not satisfied so that there exists a $\nu \in U$ such that

$$d f (u; h) = \langle \nabla f (u), v - u \rangle = - \delta < 0$$

where $h : = \nu - u$ . For all $\lambda \in [ 0 , 1 ]$ , let $\nu _ { \lambda } : = \lambda \nu + ( 1 - \lambda ) u = u + \lambda h$ ; because U is convex, each $\nu _ { \lambda }$ lies in U . Since

$$d f (u; h) = \lim _ {\lambda \searrow 0} \frac {f (u + \lambda h) - f (u)}{\lambda} = \lim _ {\lambda \searrow 0} \frac {f \left(v _ {\lambda}\right) - f (u)}{\lambda} = - \delta$$

there exists a $\lambda \in \left( 0 , 1 \right]$ such that $f ( \nu _ { \lambda } ) - f ( u ) \leq - \lambda \delta / 2 < 0$ which contradicts the optimality of u. Hence the condition in (C.17) must be satisfied. That (C.17) is equivalent to (C.18) follows from Proposition C.7 (ii).

It is an interesting fact that U in Proposition C.9 may be replaced by its approximation u ⊕ $\mathcal { T } _ { U } ( u )$ at u yielding

Proposition C.10 (Optimality conditions – tangent cone). Suppose the function $f ( \cdot )$ is convex and differentiable and the set U is convex. The point u is optimal for problem P if and only $i f u \in U$ and

$$d f (u; v - u) = \langle \nabla f (u), h \rangle \geq 0 \forall h \in \mathcal {T} _ {U} (u)$$

or, equivalently

$$- \nabla f (\boldsymbol {u}) \in \hat {N} _ {U} (\boldsymbol {u}) = \mathcal {T} _ {U} ^ {*} (\boldsymbol {u}).$$

Proof. It follows from Proposition C.9 that u is optimal for problem P if and only if $u \in U$ and $- \nabla f ( u ) \in \hat { N } _ { U } ( u )$ . But, by Proposition C.7, $\hat { N } _ { U } ( u ) \ = \ \{ g \ | \ \langle g , h \rangle \ \leq \ 0 \ \forall h \in \mathcal { T } _ { U } ( u ) \}$ so that $- \nabla f ( u ) \in \hat { N } _ { U } ( u )$ is equivalent to $\langle \nabla f ( { \boldsymbol { u } } ) , { \boldsymbol { h } } \rangle \geq 0$ for all $h \in \mathcal { T } _ { U } ( u )$ .
