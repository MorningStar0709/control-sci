Proposition C.20 (Quasiregular set). Suppose $U : = \{ u \mid g _ { i } ( u ) \leq 0 \ \forall i \in$ I} where, for each $i \in \textit { I }$ , the function $g _ { i } : \mathbb { R } ^ { m }  \mathbb { R }$ is differentiable. Suppose also that $u \in U$ and that there exists a vector $\bar { h } \in \mathcal { F } _ { U } ( u )$ such that

$$\langle \nabla g _ {i} (u), \bar {h} \rangle < 0, \forall i \in \mathcal {I} ^ {0} (u) \tag {C.24}$$

![](image/4bf3310b5e1b7443b69fbda0455ee25cd3112d12069fb5fd71b2d4d9e94e16b7.jpg)

<details>
<summary>text_image</summary>

∇g₁(u)
0
Fᵤ(u)
Tᵤ(u)
∇g₂(u)
</details>

Figure C.8: $\mathcal { F } _ { U } ( u ) \neq \mathcal { T } _ { U } ( u )$ .

Then

$$\mathcal {T} _ {U} (u) = \mathcal {F} _ {U} (u)$$

i.e., U is quasiregular at u.

Equation (C.24) is the constraint qualification; it can be seen that it precludes the situation shown in Figure C.8.

Proof. It follows from the definition (C.23) of $\mathcal { F } _ { U } ( u )$ and the constraint qualification (C.24) that:

$$\langle \nabla g _ {i} (u), h + \alpha (\bar {h} - h) \rangle < 0, \forall h \in \mathcal {F} _ {U} (u), \alpha \in (0, 1 ], i \in \mathcal {I} ^ {0} (u)$$

Hence, for all $h \in { \mathcal { F } } _ { U } ( u )$ , all $\alpha \in \left( 0 , 1 \right]$ , there exists a vector $h _ { \alpha } : =$ $h + \alpha ( \bar { h } - h )$ , in $\mathcal { F } _ { U } ( u )$ satisfying $ { \langle \nabla g _ { i } ( u ) , h _ { \alpha } \rangle } < 0$ for all $i \in \mathcal { I } ^ { 0 } ( u )$ . Assuming for the moment that $h _ { \alpha } \in \mathcal { T } _ { U } ( u )$ for all $\alpha \in ( 0 , 1 ]$ , it follows, since $h _ { \alpha } \to h { \mathrm { ~ a s ~ } } \alpha \to 0$ and $\mathcal { T } _ { U } ( u )$ is closed, that $h \in \mathcal { T } _ { U } ( u )$ , thus proving ${ \mathcal { F } } _ { U } ( u ) \subset { \mathcal { T } } _ { U } ( u )$ . It remains to show that $h _ { \alpha }$ is tangent to U at u. Consider the sequences $h ^ { \nu }$ and $\lambda ^ { \nu } ~ \searrow ~ 0$ where $h ^ { \nu } : = h _ { \alpha }$ for all $\nu \in \mathbb { I } _ { \geq 0 }$ . There exists a $\delta > 0$ such that $\langle \nabla g _ { i } ( u ) , h _ { \alpha } \rangle \leq - \delta$ for all $i \in \mathcal { I } ^ { 0 } ( u )$ and $g _ { i } ( u ) \leq - \delta$ for all $i \in \mathcal { I } \setminus \mathcal { I } ^ { 0 } ( u )$ . Since

$$g _ {i} (u + \lambda^ {\nu} h ^ {\nu}) = g _ {i} (u) + \lambda^ {\nu} \langle \nabla g _ {i} (u), h _ {\alpha} \rangle + o (\lambda^ {\nu}) \leq - \lambda^ {\nu} \delta + o (\lambda^ {\nu})$$
