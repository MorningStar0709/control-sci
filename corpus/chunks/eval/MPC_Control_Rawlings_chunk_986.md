# C.2.2 Convex Optimization Problems

The optimization problem P is convex if the function $f : \mathbb { R } ^ { m }  \mathbb { R }$ and the set $U \subset \mathbb { R } ^ { m }$ are convex. In convex optimization problems, U often takes the form $\{ u \ | \ g _ { j } ( u ) \ \leq \ 0 , j \in \mathcal { I } \}$ where $\mathcal { I } : = \{ 1 , 2 , \dots , J \}$ and each function $g _ { j } ( \cdot )$ is convex. A useful feature of convex optimization problems is the following result:

Proposition C.8 (Global optimality for convex problems). Suppose the function $f ( \cdot )$ is convex and differentiable and the set U is convex. Any locally optimal point of the convex optimization problem $\operatorname* { i n f } _ { u } \{ f ( u ) \mid$ $u \in U \}$ is globally optimal.

Proof. Suppose u is locally optimal so that there exists an $\varepsilon > 0$ such that $f ( \nu ) \geq f ( u )$ for all $\nu \in ( u \oplus \varepsilon { \mathcal { B } } ) \cap U$ . If, contrary to what we wish to prove, u is not globally optimal, there exists a $w \in U$ such that $f ( w ) < f ( u )$ . For any $\lambda \in [ 0 , 1 ]$ , the point $w _ { \lambda } : = \lambda w + ( 1 - \lambda ) u$ lies in $[ u , w ]$ (the line joining u and w). Then $w _ { \lambda } \in U$ (because U is convex) and $f ( w _ { \lambda } ) \leq \lambda f ( w ) + ( 1 - \lambda ) f ( u ) < f ( u )$ for all $\lambda \in \left( 0 , 1 \right]$ (because $f ( \cdot )$ is convex and $f ( w ) < f ( u ) )$ . We can choose $\lambda > 0$ so that $w _ { \lambda } \in ( u \oplus \varepsilon { \mathcal { B } } ) \cap U$ and $f ( w _ { \lambda } ) < f ( u )$ . This contradicts the local optimality of u. Hence u is globally optimal. 

On the assumption that $f ( \cdot )$ is differentiable, we can obtain a simple necessary and sufficient condition for the (global) optimality of a point u.

Proposition C.9 (Optimality conditions – normal cone). Suppose the function $f ( \cdot )$ is convex and differentiable and the set U is convex. The point u is optimal for problem P if and only $i f u \in U$ and

$$d f (u; v - u) = \langle \nabla f (u), v - u \rangle \geq 0 \forall v \in U \tag {C.17}$$

or, equivalently

$$- \nabla f (\boldsymbol {u}) \in \hat {N} _ {U} (\boldsymbol {u}) \tag {C.18}$$

Proof. Because $f ( \cdot )$ is convex, it follows from Theorem 7 in Appendix A1 that

$$f (\nu) \geq f (u) + \langle \nabla f (u), \nu - u \rangle \tag {C.19}$$
