# 7.4 Constrained Linear Quadratic Control

We now show how parametric quadratic programming may be used to solve the optimal receding horizon control problem when the system is linear, the constraints polyhedral, and the cost is quadratic. The system is described, as before, by

$$x ^ {+} = A x + B u \tag {7.6}$$

and the constraints are, as before,

$$x \in \mathbb {X}, \quad u \in \mathbb {U} \tag {7.7}$$

where X is a polyhedron containing the origin in its interior and U is a polytope also containing the origin in its interior. There may be a terminal constraint of the form

$$x (N) \in \mathbb {X} _ {f} \tag {7.8}$$

where $\mathbb { X } _ { f }$ is a polyhedron containing the origin in its interior. The cost is

$$V _ {N} (x, \mathbf {u}) = \left[ \sum_ {i = 0} ^ {N - 1} \ell (x (i), u (i)) \right] + V _ {f} (x (N)) \tag {7.9}$$

in which, for all i, $x ( i ) ~ = ~ \phi ( i ; x , { \bf u } )$ , the solution of (7.6) at time i if the initial state at time 0 is x and the control sequence is $\textbf { u } : =$ $\{ u ( 0 ) , u ( 1 ) , \ldots , u ( N - 1 ) \}$ . The functions $\ell ( \cdot )$ and $V _ { f } ( \cdot )$ are quadratic

$$\ell (x, u) := (1 / 2) x ^ {\prime} Q x + (1 / 2) u ^ {\prime} R u, \quad V _ {f} (x) := (1 / 2) x ^ {\prime} Q _ {f} x \tag {7.10}$$

The state and control constraints (7.7) induce, via the difference equation (7.6), an implicit constraint $( x , \mathbf { u } ) \in \mathcal { Z }$ where

$$\mathbb {Z} := \{(x, \mathbf {u}) \mid x (i) \in \mathbb {X}, u (i) \in \mathbb {U}, i \in \mathbb {I} _ {0: N - 1}, x (N) \in \mathbb {X} _ {f} \} \tag {7.11}$$

![](image/21e45567e26425656b73f2f3dc4404e53fdd74636813cc6bc52300ecc7abb08e.jpg)

<details>
<summary>surface_3d</summary>

| x | y |
| --- | --- |
| -3.0 | 1.8 |
| -2.5 | 1.5 |
| -2.0 | 1.2 |
| -1.5 | 0.9 |
| -1.0 | 0.6 |
| -0.5 | 0.3 |
| 0.0 | 0.0 |
| 0.5 | -0.3 |
| 1.0 | -0.6 |
| 1.5 | -0.9 |
| 2.0 | -1.2 |
| 2.5 | -1.5 |
| 3.0 | -1.8 |
</details>

Figure 7.6: Regions Rx, $x \in X$ for a second-order example.

where, for all $i , x ( i ) = \phi ( i ; x , { \bf { u } } )$ . It is easily seen that Z is polyhedral since, for each $i , x ( i ) = A ^ { i } x + M _ { i } \mathbf { u }$ for some matrix $M _ { i }$ in $\mathbb { R } ^ { n \times N m }$ ; here u is regarded as the column vector $\left[ u ( 0 ) ^ { \prime } \quad u ( 1 ) ^ { \prime } \quad \cdot \cdot \cdot \quad u ( N - 1 ) ^ { \prime } \right] ^ { \prime }$ . Clearly $x ( i ) = \phi ( i ; x , { \bf u } )$ is linear in $\mathbf { \bar { \rho } } ( x , \mathbf { u } )$ . The constrained linear optimal control problem may now be defined by
