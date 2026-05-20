# C.2.1 Tangent and Normal Cones

In determining conditions of optimality, it is often convenient to employ approximations to the cost function $f ( \cdot )$ and the constraint set U. Thus the cost function $f ( \cdot )$ may be approximated, in the neighborhood of a point u¯, by the first order expansion $f ( \bar { u } ) + \langle \nabla f ( \bar { u } ) , ( u - \bar { u } ) \rangle$ or by the second order expansion $f ( \bar { u } ) + \langle \nabla f ( \bar { u } ) , ( u - \bar { u } ) \rangle + ( 1 / 2 ) ( ( u -$ $\bar { u } ) ^ { \prime } \nabla ^ { 2 } f ( \bar { x } ) ( u - \bar { u } ) ;$ ) if the necessary derivatives exist. Thus we see that in the unconstrained case, a necessary condition for the optimality of u¯ is $\nabla f ( { \bar { u } } ) = 0$ . To obtain necessary conditions of optimality for constrained optimization problems, we need to approximate the constraint set as well; this is more difficult. An example of U and its approximation is shown in Figure C.2; here the set $U = \{ u \in \mathbb { R } ^ { 2 } \ | \ g ( u ) \ = \ 0 \}$ where $g : \mathbb { R }  \mathbb { R }$ is approximated in the neighborhood of a point u¯ satisfying $g ( \bar { u } ) ~ = ~ 0$ by the set u¯ ⊕ $\mathcal { T } _ { U } ( \bar { u } )$ where2 the tangent cone $\mathcal T _ { U } ( \bar { u } ) : = \{ h \in \mathbb { R } ^ { 2 } \ | \ \nabla g ( \bar { u } ) , u - \bar { u } \} = 0 \}$ . In general, a set U is approximated, near a point u¯, by u¯ ⊕ $\mathcal { T } _ { U } ( \bar { u } )$ where its tangent cone $\mathcal { T } _ { U } ( \bar { u } )$ is defined below. Following Rockafellar and Wets (1998), we use $u { \xrightarrow [ { U } ] { \nu } } \nu$ to denote that the sequence $\{ u ^ { \nu } \mid \nu \in \mathbb { I } _ { \geq 0 } \}$ converges to v as $\nu \to \infty$ while satisfying $u ^ { \nu } \in U$ for all $\nu \in \mathbb { I } _ { \geq 0 }$ .

![](image/8e27a5465ee4cb9d2e3af94d0666300c66464ce0a0d606c45f4344883fd24282.jpg)

<details>
<summary>text_image</summary>

u₂
∇f(ū)
ū ⊕ Tₐ(ū)
ū₂
U
ū₁
u₁
</details>

Figure C.2: Approximation of the set U.   
![](image/8d5ecd8567c2baeed073c828c9c68167e1f8afd4cdad73fa307061dbd44e9067.jpg)

<details>
<summary>text_image</summary>

N̂(u)
u
U
T_U(v)
v
T_U(u)
N̂(v)
</details>

Figure C.3: Tangent cones.

![](image/afa8fa72efd98770dc24a6b85b9374710ce4270479581494c4714e261005c969.jpg)

<details>
<summary>text_image</summary>

ˆN_U(u)
u
U
</details>

Figure C.4: Normal at u.
