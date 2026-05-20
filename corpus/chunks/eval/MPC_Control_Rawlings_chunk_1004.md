# C.3 Set-Valued Functions and Continuity of Value Function

A set-valued function $U ( \cdot )$ is one for which, for each value of $x , U ( x )$ is a set; these functions are encountered in parametric programming. For example, in the problem $\mathbb { P } ( x ) : \operatorname* { i n f } _ { u } \{ f ( x , u ) \mid u \in U ( x ) \}$ (which has the same form as an optimal control problem in which x is the state and u is a control sequence), the constraint set U is a set-valued function of the state. The solution to the problem $\mathbb { P } ( x )$ (the value of u that achieves the minimum) can also be set-valued. It is important to know how smoothly these set-valued functions vary with the parameter x. In particular, we are interested in the continuity properties of the value function $x \mapsto f ^ { 0 } ( x ) = \operatorname* { i n f } _ { u } \{ f ( x , u ) \mid u \in U ( x ) \}$ since, in optimal control problems we employ the value function as a Lyapunov function and robustness depends, as we have discussed earlier, on the continuity of the Lyapunov function. Continuity of the value function depends, in turn, on continuity of the set-valued constraint set $U ( \cdot )$ . We use the notation $U : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ to denote the fact that $U ( \cdot )$ maps points in $\mathbb { R } ^ { n }$ into subsets of $\mathbb { R } ^ { m }$ .

![](image/739271710eb1990b7f34c32f14e5156fe8a6cf825c69c00624b2e7548d48e8ef.jpg)

<details>
<summary>text_image</summary>

u
U(x₁)
Z
x₁
x
X
</details>

Figure C.9: Graph of set-valued function $U ( \cdot )$ .
