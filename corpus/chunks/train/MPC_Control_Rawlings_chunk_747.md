# Exercise 6.25: Partitioned optimality conditions with constraints

Consider a partitioned version of the constrained optimization problem of Exercise 6.24 with uncoupled constraints

$$\min _ {u _ {1}, u _ {2}} V (u _ {1}, u _ {2}) \quad \text { subject to } \quad u _ {1} \in \mathbb {U} _ {1} \quad u _ {2} \in \mathbb {U} _ {2}$$

in which V is a quadratic function and $\mathbb { U } _ { 1 }$ and $\mathbb { U } _ { 2 }$ are convex and nonempty.

![](image/867833cdaaedc02cf7f8804ee1e6d6d3703e3d0bf2f0d097ae1a4360f104c3ee.jpg)

<details>
<summary>text_image</summary>

-∇V
θ
u*
V = c₂ < c₁
V = c₁
z
U
/
</details>

(a)

![](image/ccfedcf30af617b66e7bb5233e2cb95eadc26cb82c4b2d3df0405b9727a09b36.jpg)

<details>
<summary>text_image</summary>

-\n\nu*\nN(\u03b1,\u03b1*)\n(b)
</details>

(D)   
Figure 6.9: (a) Optimality of $u ^ { * }$ means the angle between $- \nabla V$ and any point $_ { z }$ in the feasible region must be greater than $9 0 ^ { \circ }$ and less than $2 7 0 ^ { \circ }$ . (b) The same result restated: $u ^ { * }$ is optimal if and only if the negative gradient is in the normal cone to the feasible region at $u ^ { * } , - \nabla V | _ { u ^ { * } } \in$ $N ( \mathbb { U } , u ^ { * } )$ .

(a) Show that $( u _ { 1 } ^ { * } , u _ { 2 } ^ { * } )$ is an optimal solution if and only if

$$\langle z _ {1} - u _ {1} ^ {*}, - \nabla_ {u _ {1}} V | _ {(u _ {1} ^ {*}, u _ {2} ^ {*})} \rangle \leq 0 \quad \forall z _ {1} \in \mathbb {U} _ {1}\langle z _ {2} - u _ {2} ^ {*}, - \nabla_ {u _ {2}} V | _ {(u _ {1} ^ {*}, u _ {2} ^ {*})} \rangle \leq 0 \quad \forall z _ {2} \in \mathbb {U} _ {2} \tag {6.33}$$

(b) Extend the optimality conditions to cover the case

$$\min _ {u _ {1}, \dots , u _ {M}} V (u _ {1}, \dots , u _ {M}) \quad \text { subject to } \quad u _ {j} \in \mathbb {U} _ {j} \quad j = 1, \dots , M$$

in which V is a quadratic function and the $\mathbb { U } _ { j }$ are convex and nonempty.
