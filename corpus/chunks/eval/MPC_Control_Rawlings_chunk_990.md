Corollary C.13 (Optimality conditions — linear inequalities). Suppose the function $f ( \cdot )$ is convex and differentiable and $U = \{ u \mid A u \leq b \}$ . Then u is optimal for $\mathbb { P } : \operatorname* { m i n } _ { u } \left\{ f ( u ) \mid u \in U \right\}$ if and only if $A u \leq b$ and there exist multipliers $\mu _ { i } \geq 0 , i \in \mathcal { I } ^ { 0 } ( u )$ satisfying

$$\nabla f (u) + \sum_ {i \in \mathcal {I} ^ {0} (u)} \mu_ {i} \nabla g _ {i} (u) = 0 \tag {C.20}$$

where, for each i, $g _ { i } ( u ) : = \langle a _ { i } , u \rangle - b _ { i }$ so that $g _ { i } ( u ) \leq 0$ is the constraint $\langle a _ { i } , u \rangle \leq b _ { i }$ and $\nabla g _ { i } ( u ) = a _ { i }$ .

Proof. Since any point $g \in \mathrm { c o n e } \{ a _ { i } \ | \ i \in \mathcal { I } ^ { 0 } ( u ) \}$ may be expressed as $\begin{array} { r } { g = \sum _ { i \in \ b { \mathcal { I } } ^ { 0 } ( u ) } \mu _ { i } a _ { i } } \end{array}$ where, for each i, $\mu _ { i } \geq 0$ , the condition $- \nabla f ( u ) \in$ cone $\{ a _ { i } \ | \ i \in \mathcal { I } ^ { 0 } ( u ) \}$ is equivalent to the existence of multipliers $\mu _ { i } \geq$ $0 , i \in \mathcal { I } ^ { 0 } ( u )$ satisfying (C.20). 

The above results are easily extended if U is defined by linear equality and inequality constraints, i.e., if

$$U := \{\langle a _ {i}, u \rangle \leq b _ {i}, i \in \mathcal {I}, \langle c _ {i}, u \rangle = d _ {i}, i \in \mathcal {E} \}$$

In this case, at any point $u \in U$ , the tangent cone is

$$\mathcal {T} _ {U} (u) = \{h \mid \langle a _ {i}, h \rangle \leq 0, i \in \mathcal {I} ^ {0} (u), \langle c _ {i}, h \rangle = 0, i \in \mathcal {E} \}$$

and the normal cone is

$$\hat {N} _ {U} (u) = \{\sum_ {i \in \mathcal {I} ^ {0} (u)} \lambda_ {i} a _ {i} + \sum_ {i \in \mathcal {E}} \mu_ {i} c _ {i} \mid \lambda_ {i} \geq 0 \forall i \in \mathcal {I} ^ {0} (u), \mu_ {i} \in \mathbb {R} \forall i \in \mathcal {E} \}$$

![](image/a8f644c690f9c47ccadae1932f132ab5bd1d71c0f745418041285eb4b7982f35.jpg)

<details>
<summary>text_image</summary>

U
u
a1
-∇f(u)
F*(u)
a2
F(u)
</details>

Figure C.5: Condition of optimality.

With U defined this way, u is optimal for min $\iota _ { u } \{ f ( u ) \mid u \in U \}$ where $f ( \cdot )$ is convex and differentiable if and only if

$$- \nabla f (\boldsymbol {u}) \in \hat {N} _ {U} (\boldsymbol {u})$$
