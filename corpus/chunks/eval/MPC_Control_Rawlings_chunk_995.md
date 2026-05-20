Proposition C.17 (Set of regular tangents is closed convex cone). At any $u \in U$ , the set $\hat { \mathcal { T } } _ { U } ( u )$ of regular tangents to U at u is a closed convex cone with $\hat { \mathcal { T } } _ { U } ( u ) \subset \mathcal { T } _ { U } ( u )$ . Moreover, if U is locally closed at u, then $\hat { \mathcal { T } } _ { U } ( u ) = N _ { U } ( u ) ^ { * }$ .

Figure C.7 illustrates some of these results. In Figure C.7, the constant cost contour $\{ \nu \mid f ( \nu ) = f ( u ) \}$ of a nondifferentiable cost function $f ( \cdot )$ is shown together with a sublevel set D passing through the point u: $f ( \nu ) \leq f ( u )$ for all $\nu \in D$ . For this example, $d f ( u ; h ) =$ max $\{ \langle g _ { 1 } , h \rangle , \langle g _ { 2 } , h \rangle \}$ where $g _ { 1 }$ and $g _ { 2 }$ are normals to the level set of $f ( \cdot )$ at u so that $d f ( u ; h ) \ge 0$ for all $h \in \hat { \mathcal { T } } _ { U } ( u )$ , a necessary condition of optimality; on the other hand, there exist $h \in \mathcal { T } _ { U } ( u )$ such that $d f ( u ; h ) < 0$ . The situation is simpler if the constraint set U is regular at u.

![](image/4036366b9517813bee94eff6bd40dfbb290d668ab218c374d50a189ca90bc569.jpg)

<details>
<summary>text_image</summary>

T̂_U(u)
U
g₁
u
g₂
D
T̂_U(u)
</details>

Figure C.7: Condition of optimality.

Definition C.18 (Regular set). A set U is regular at a point $u \in U$ in the sense of Clarke if it is locally closed at u and if ${ \cal { N } } _ { U } ( u ) = \hat { \cal { N } } _ { U } ( u )$ (all normal vectors at u are regular).

The following consequences of Clarke regularity are established in Rockafellar and Wets (1998), Corollary 6.29:

Proposition C.19 (Conditions for regular set). Suppose U is locally closed at $u \in U$ . Then U is regular at u is equivalent to each of the following.

(a) ${ \cal { N } } _ { U } ( u ) = \hat { \cal { N } } _ { U } ( u )$ (all normal vectors at u are regular).   
(b) $\mathcal { T } _ { U } ( u ) = \hat { \mathcal { T } } _ { U } ( u )$ (all tangent vectors at u are regular).   
(c) $N _ { U } ( u ) = \mathcal { T } _ { U } ( u ) ^ { * }$ .   
(d) $\mathcal { T } _ { U } ( u ) = N _ { U } ( u ) ^ { * }$ .   
(e) $\langle g , h \rangle \leq 0 f o r a l l h \in \mathcal { T } _ { U } ( u ) , a l l g \in N _ { U } ( u )$ .

It is shown in Rockafellar and Wets (1998) that if U is regular at u and a constraint qualification is satisfied, then a necessary condition of optimality, similar to (C.21), may be obtained. To obtain this result, we pursue a slightly different route in Sections C.2.6 and C.2.7.
