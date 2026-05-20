The graph of a set-valued functions is often a useful tool. The graph of $U : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is defined to be the set $Z : = \{ ( x , u ) \in \mathbb { R } ^ { n } \times \mathbb { R } ^ { m } \mid u \in$ $U ( x ) \}$ ; the domain of the set-valued function U is the set $\mathcal { X } : = \{ x \in $ $\mathbb { R } ^ { n } \mid U ( x ) \neq \emptyset \} = \{ x \in \mathbb { R } ^ { n } \mid \exists u \in \mathbb { R } ^ { m }$ such that $( x , u ) \in Z \}$ ; clearly $\boldsymbol { x } \subset \mathbb { R } ^ { n }$ . Also X is the projection of the set $Z \subset \mathbb { R } ^ { n } \times \mathbb { R } ^ { m }$ onto $\mathbb { R } ^ { n } , \mathbf { i . e . }$ , $( x , u ) \in Z$ implies $x \in { \mathcal { X } }$ . An example is shown in Figure C.9. In this example, U(x) varies continuously with x. Examples in which U(·) is discontinuous are shown in Figure C.10. In Figure C.10(a), the set $U ( x )$ varies continuously if x increases from its initial value of $x _ { 1 }$ , but jumps to a much larger set if x decreases an infinitesimal amount (from its initial value of $x _ { 1 } )$ ; this is an example of a set-valued function that is inner semicontinuous at $x _ { 1 }$ . In Figure C.10(b), the set $U ( x )$ varies continuously if x decreases from its initial value of $x _ { 1 }$ , but jumps to a much smaller set if x increases an infinitesimal amount (from its initial value of $x _ { 1 } )$ ; this is an example of a set-valued function that is outer semicontinuous at $x _ { 1 }$ . The set-valued function is continuous at $x _ { 2 }$ where it is both outer and inner semicontinuous.

![](image/c82342ec6a3877e0c8c10f20225f1fa1e30bde4fecb903ab32dbbaaa6e5b13ca.jpg)

<details>
<summary>text_image</summary>

U(x)
S₁
U(x₁)
S₂
x₁	x₂	x
</details>

(a) Inner semicontinuous set-valued function.

![](image/7b68714d5dcbc36db16372965c21995de619bb0aab7d782b36eaa801ace59a96.jpg)

<details>
<summary>text_image</summary>

U(x)
S₃
S₁
U(x₁)
x₁	x₂	x
</details>

(b) Outer semicontinuous set-valued function.   
Figure C.10: Graphs of discontinuous set-valued functions.

We can now give precise definitions of inner and outer semicontinuity.
