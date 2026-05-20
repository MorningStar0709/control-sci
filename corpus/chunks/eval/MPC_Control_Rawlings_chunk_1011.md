We now specialize to the case where $U ( x ) = \{ u \in \mathbb { R } ^ { m } \mid ( x , u ) \in \mathcal { Z } \}$ where $\mathcal { Z }$ is a polyhedron in $\mathbb { R } ^ { n } \times \mathbb { R } ^ { m }$ ; for each $x , U ( x )$ is a polytope. This type of constraint arises in constrained optimal control problems when the system is linear and the state and control constraints are polyhedral. What we show in the sequel is that, in this special case, $U ( \cdot )$ is continuous and so, therefore, is $V ^ { 0 } ( \cdot )$ . An alternative proof, which many readers may prefer, is given in Chapter $7$ where we exploit the fact that if $V ( \cdot )$ is strictly convex and quadratic and $\mathcal { Z }$ polyhedral, then $V ^ { 0 } ( \cdot )$ is piecewise quadratic and continuous. Our first concern is to obtain a bound on $d ( u , U ( x ^ { \prime } ) )$ , the distance of any $u \in U ( x )$ from the constraint set $U ( x ^ { \prime } )$ .

A bound on $d ( u , U ( x ^ { \prime } ) ) , u \in U ( x )$ . The bound we require is given by a special case of a theorem due to Clarke, Ledyaev, Stern, and Wolenski (1998, Theorem 3.1, page 126). To motivate this result, consider a differentiable convex function $f : \mathbb { R } \to \mathbb { R }$ so that $f ( u ) \geq f ( \nu ) +$ $\langle \nabla f ( \nu ) , u - \nu \rangle$ for any two points u and v in R. Suppose also that there exists a nonempty interval $U = [ a , b ] \subset \mathbb { R }$ such that $f ( u ) \leq 0$ for all $u \in U$ and that there exists a $\delta > 0$ such that $\Delta f ( u ) > \delta$ for all $u \in \mathbb { R }$ . Let $u > b$ and let $\nu = b$ be the closest point in U to u. Then $f ( u ) \ge f ( \nu ) + \langle \nabla f ( \nu ) , u - \nu \rangle \ge \delta | \nu - u |$ so that d $( u , U ) \le f ( u ) / \delta$ . The theorem of Clarke et al. (1998) extends this result to the case when $f ( \cdot )$ is not necessarily differentiable but requires the concept of a subgradient of a convex function

![](image/7c9a8a2b1e775a92d4f3d99a03b2938c75574199b61f138b2cf93b59b0b2b2d4.jpg)

<details>
<summary>text_image</summary>

f
(u,f(u)
(g,-1)
1
g
</details>

Figure C.12: Subgradient of $f ( \cdot )$ .

Definition C.30 (Subgradient of convex function). Suppose $f : \mathbb { R } ^ { m } $ R is convex. Then the subgradient $\delta f ( u )$ of $f ( \cdot )$ at u is defined by

$$\delta f (u) := \{g \mid f (v) \geq f (u) + \langle g, v - u \rangle \forall v \in \mathbb {R} ^ {m} \}$$
