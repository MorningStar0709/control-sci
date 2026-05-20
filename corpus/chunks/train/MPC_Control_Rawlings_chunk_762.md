We assume that $\boldsymbol { x } \in \mathbb { R } ^ { n }$ and $u \in \mathbb { R } ^ { m }$ . Let $\boldsymbol { x } \subset \mathbb { R } ^ { n }$ be defined by

$$\mathcal {X} := \{x \mid \exists u \text { such that } (x, u) \in \mathbb {Z} \} = \{x \mid \mathcal {U} (x) \neq \emptyset \}$$

The set X is the domain of $V ^ { 0 } ( \cdot )$ and $u ^ { 0 } ( \cdot )$ and is thus the set of points x for which a feasible solution of $\mathbb { P } ( x )$ exists; it is the projection of Z (which is a set in (x, u)-space) onto x-space. See Figure 7.1, which illustrates Z and $\mathcal { U } ( x )$ for the case when $\mathcal { U } ( x ) = \{ u \ | \ M u \leq N x + p \}$ ; the set Z is thus defined by $\mathbb { Z } : = \{ ( x , u ) \mid M u \leq N x + p \}$ . In this case, both Z and $\mathcal { U } ( x )$ are polyhedral.

Before proceeding to consider parametric linear and quadratic programming, some simple examples may help the reader to appreciate the underlying ideas. Consider first a very simple parametric linear program m $\mathsf { i n } _ { u } \{ V ( x , u ) \mid ( x , u ) \in \mathbb { Z } \}$ where $V ( x , u ) \ : = \ x + u$ and $\mathbb { Z } : = \{ ( x , u ) \mid u + x \geq 0 , u - x \geq 0 \}$ so that $\mathcal { U } ( x ) = \{ u \geq - x , u \geq x \}$ . The problem is illustrated in Figure 7.2. The set Z is the region lying above the two solid lines $u \ = \ - x$ and $u \ = \ x$ , and is convex. The gradient $\nabla _ { u } V ( x , u ) ~ = ~ 1$ everywhere, so the solution, at each x, to the parametric program is the smallest u in U(x), i.e., the smallest u lying above the two lines $u = - x$ and $u \ : = \ : x$ . Hence $u ^ { 0 } ( x ) = - x$ if $x ~ \le ~ 0$ and $u ^ { 0 } ( x ) \ = \ x$ if $x ~ \geq ~ 0$ , i.e., $u ^ { 0 } ( x ) \ = \ | x | ;$ the graph of $u ^ { 0 } ( \cdot )$ is the dashed line in Figure 7.2. Both $u ^ { 0 } ( \cdot )$ and $V ^ { 0 } ( \cdot )$ , where $V ^ { 0 } ( x ) = x + u ^ { 0 } ( x )$ , are piecewise affine, being affine in each of the two regions $X _ { 1 } : = \{ x \mid x \leq 0 \}$ and $X _ { 2 } : = \{ x \mid x \geq 0 \}$ .

![](image/716a86304fd635e52f682af2a970f1288e42c83f62f7256d4171792ae284503b.jpg)

<details>
<summary>text_image</summary>

u
U(x)
Z
x
x
</details>

Figure 7.1: The sets Z, X and $\mathcal { U } ( x )$ .   
![](image/a06c1898b7a6d9ad32f0f37a06117e0477d320925d5c2566b184b7850bc11e70.jpg)

<details>
<summary>text_image</summary>

u
u⁰(x)
Z
constraint
0
x
</details>

Figure 7.2: Parametric linear program.
