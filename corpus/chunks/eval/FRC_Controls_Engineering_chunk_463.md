# 17.3.5 Differential drive

Here’s a problem formulation for differential drive MPC with a circular keep-out region.

$$\min _ {\mathbf {x} _ {0: N}, \mathbf {u} _ {0: N - 1}} \sum_ {k = 0} ^ {N - 1} (\mathbf {r} - \mathbf {x} _ {k}) ^ {\top} \mathbf {Q} (\mathbf {r} - \mathbf {x} _ {k})$$

subject to x0 = current state

$$\mathbf {x} _ {k + 1} = \operatorname{RK4} (f, \mathbf {x} _ {k}, \mathbf {u} _ {k}, \Delta T)\mathbf {u} _ {\text { min }} \leq \mathbf {u} _ {k} \leq \mathbf {u} _ {\text { max }}(x _ {k} - c _ {x}) ^ {2} + (y _ {k} - c _ {y}) ^ {2} \geq r ^ {2}$$

where $\mathbf { x } _ { k } = \left[ x \quad y \quad \theta \quad v _ { l } \quad v _ { r } \right] ^ { \mathsf { T } } , \mathbf { u } _ { k } = \left[ V _ { l } \quad V _ { r } \right] ^ { \mathsf { T } }$ , r is the reference, $( c _ { x } , c _ { y } )$ is the circle’s center, and r is the circle’s radius. Figures 17.5 and 17.6 show the closed-loop response.

![](image/35c7493297b120aab080bd4736c2a7c03d794a08ab8002d0daf9ce448eb65dfb.jpg)

<details>
<summary>line</summary>

| x (m) | y (m) - Reference | y (m) - State | y (m) - Keep-out region |
|-------|-------------------|---------------|--------------------------|
| 2     | 13.5              | 13.5          | 13.5                     |
| 4     | 14.5              | 15.0          | 14.5                     |
| 6     | 15.5              | 16.0          | 15.5                     |
| 8     | 16.5              | 17.0          | 16.5                     |
| 10    | 17.5              | 18.0          | 17.5                     |
</details>

Figure 17.5: Differential drive MPC x-y plot

![](image/914179795c2f3903617049d37e86f7425cbce8e561486a2735f2a3b20bb2667d.jpg)

<details>
<summary>line</summary>
