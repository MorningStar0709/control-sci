The subgradient at a point x is, unlike the ordinary gradient, a set. For our max example $( f ( x ) = \psi ( x ) = \mathrm { m a x } _ { i } \{ f _ { i } ( x ) \ | \ i \in I \} )$ we have $d \psi ( x ; h ) \ = \ \operatorname * { m a x } _ { i } \{ \langle \nabla f ^ { i } ( x ) , h \rangle \ | \ i \ \in \ I ^ { 0 } ( x ) \}$ . In this case, it can be shown that

$$\partial \psi (x) = \operatorname{co} \{\nabla f ^ {i} (x) \mid i \in I ^ {0} (x) \}$$

If the directional derivative $h \mapsto d f ( x ; h )$ is convex, then the subgradient $\partial f ( x )$ is nonempty and the directional derivative $d f ( x ; h )$ may be expressed as

$$d f (x; h) = \max _ {g} \{\langle g, h \rangle \mid g \in \partial f (x) \}$$

Figure A.4 illustrates this for the case when $\psi ( x ) : = \mathrm { m a x } \{ f _ { 1 } ( x ) , f _ { 2 } ( x ) \}$ and $I ^ { 0 } ( x ) = \{ 1 , 2 \}$ .

![](image/88fa286bbe080f06cfa4090b6b0771765ef8335aefa77ac6c052d045dcb4705d.jpg)

<details>
<summary>text_image</summary>

∇f₁(x)
∂ψ(x)
x
∇f₂(x)
f₁(x) = ψ(x)
f₂(x) = ψ(x)
</details>

Figure A.4: Subgradient.
