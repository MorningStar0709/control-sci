$$
\mathbf {z} = \left[ \begin{array}{c} u _ {1} (0) \\ x _ {1} (1) \\ \vdots \\ u _ {1} (N - 1) \\ x _ {1} (N) \end{array} \right] \quad H = \operatorname{diag} \left(\left[ \begin{array}{l l l l l} R _ {1} & Q _ {1} & \dots & R _ {1} & P _ {1 f} \end{array} \right]\right)
$$

and can express player one’s optimal control problem as

$$\min _ {\mathbf {z}} (1 / 2) \left(\mathbf {z} ^ {\prime} H \mathbf {z} + x _ {1} (0) ^ {\prime} Q _ {1} x _ {1} (0)\right)\mathrm{s.t.} D \mathbf {z} = d$$

in which

$$
D = - \left[ \begin{array}{c c c c c c c} \overline {{B}} _ {1 1} & - I & & & & \\ & A _ {1} & \overline {{B}} _ {1 1} & - I & & \\ & & & \ddots & & \\ & & & & A _ {1} & \overline {{B}} _ {1 1} & - I \end{array} \right]

d = \left[ \begin{array}{c} A _ {1} x _ {1} (0) + \overline {{B}} _ {1 2} u _ {2} (0) \\ \overline {{B}} _ {1 2} u _ {2} (1) \\ \vdots \\ \overline {{B}} _ {1 2} u _ {2} (N - 1) \end{array} \right]
$$

![](image/5cdd47ab9b78b993b458d3aaa572044ded2d7ed57ed71f5f813c4e0dd6319079.jpg)

<details>
<summary>scatter</summary>

| Player | Iteration Type | Value |
| --- | --- | --- |
| (u₁^p, u₂^p) | current iterate | w₁ |
| (u₁^p, u₂^p) | next iterate | w₂ |
| (u₁^p, u₂^p) | player one's optimization | w₁ |
| (u₁^p, u₂^p) | player one's optimization | w₂ |
</details>

Figure 6.1: Convex step from $( u _ { 1 } ^ { p } , u _ { 2 } ^ { p } )$ to $( u _ { 1 } ^ { p + 1 } , u _ { 2 } ^ { p + 1 } )$ ; the parameters $w _ { 1 } , \ w _ { 2 }$ with $w _ { 1 } + w _ { 2 } = 1$ determine location of next iterate on line joining the two players’ optimizations: $( u _ { 1 } ^ { 0 } , u _ { 2 } ^ { p } )$ ) and $( u _ { 1 } ^ { p } , u _ { 2 } ^ { 0 } )$ .

We then apply (1.58) to obtain

$$
\left[ \begin{array}{c c} H & - D ^ {\prime} \\ - D & 0 \end{array} \right] \left[ \begin{array}{l} \mathbf {z} \\ \boldsymbol {\lambda} \end{array} \right] = \left[ \begin{array}{c} 0 \\ - \widetilde {A} _ {1} \end{array} \right] x _ {1} (0) + \left[ \begin{array}{c} 0 \\ - \widetilde {B} _ {1 2} \end{array} \right] \mathbf {u} _ {2} \tag {6.12}
$$

in which we have defined

$$
\boldsymbol {\lambda} = \left[ \begin{array}{c} \lambda (1) \\ \lambda (2) \\ \vdots \\ \lambda (N) \end{array} \right] \qquad \widetilde {A} _ {1} = \left[ \begin{array}{c} A _ {1} \\ 0 \\ \vdots \\ 0 \end{array} \right] \qquad \widetilde {B} _ {1 2} = \left[ \begin{array}{c c c c} \overline {{B}} _ {1 2} & & & \\ & \overline {{B}} _ {1 2} & & \\ & & \ddots & \\ & & & \overline {{B}} _ {1 2} \end{array} \right]
$$

Solving this equation and picking out the rows of z corresponding to the elements of $\mathbf { u } _ { 1 }$ gives
