# A.13.2 Convex Functions

Next we turn to convex functions. For an example see Figure $\mathrm { { A . 7 } } .$ .

![](image/42b506b0c4dc47f0c24302910dc39a421f312fb58c5effa405349b077f60a4ee.jpg)

<details>
<summary>text_image</summary>

f(x)
x
y
f(y)
</details>

Figure A.7: A convex function.

A function $f : \mathbb { R } ^ { n }  \mathbb { R }$ is said to be convex if for any $x ^ { \prime } , x ^ { \prime \prime } \in \mathbb { R } ^ { n }$ and $\lambda \in [ 0 , 1 ]$ ,

$$f (\lambda x ^ {\prime} + (1 - \lambda) x ^ {\prime \prime}) \leq \lambda f (x ^ {\prime}) + (1 - \lambda) f (x ^ {\prime \prime})$$

A function $f : \mathbb { R } ^ { n }  \mathbb { R }$ is said to be concave $\mathrm { i f } \ - f$ is convex.

The epigraph of a function $f : \mathbb { R } ^ { n }  \mathbb { R }$ is defined by

$$\operatorname{epi} (f) := \{(x, y) \in \mathbb {R} ^ {n} \times \mathbb {R} \mid y \geq f (x) \}$$

Theorem A.23 (Convexity implies continuity). Suppose $f : \mathbb { R } ^ { n } $ R is convex. Then f is continuous in the interior of it domain.

The following property is illustrated in Figure A.7.

Theorem A.24 (Differentiability and convexity). Suppose $f : \mathbb { R } ^ { n }  \mathbb { R }$ is differentiable. Then f is convex if and only if

$$f (y) - f (x) \geq \left\langle \nabla f (x), y - x \right\rangle \text { for all } x, y \in \mathbb {R} ^ {n} \tag {A.9}$$

Proof. ⇒ Suppose f is convex. Then for any $x , y \in \mathbb { R } ^ { n }$ , and $\lambda \in [ 0 , 1 ]$

$$f (x + \lambda (y - x)) \leq (1 - \lambda) f (x) + \lambda f (y) \tag {A.10}$$

Rearranging (A.10) we get

$$\frac {f (x + \lambda (y - x)) - f (x)}{\lambda} \leq f (y) - f (x) \text { for all } \lambda \in [ 0, 1 ]$$

Taking the limit as $\lambda  0$ we get (A.9).

⇐ Suppose (A.9) holds. Let x and y be arbitrary points in $\mathbb { R } ^ { n }$ and let λ be an arbitrary point in [0, 1]. Let $z = \lambda x + ( 1 - \lambda ) y$ . Then

$$f (x) \geq f (z) + f ^ {\prime} (z) (x - z), \text { and }f (y) \geq f (z) + f ^ {\prime} (z) (y - z)$$

Multiplying the first equation by λ and the second by (1 − λ), adding the resultant equations, and using the fact that $z = \lambda x + ( 1 - \lambda ) y$ yields

$$\lambda f (x) + (1 - \lambda) f (y) \geq f (z) = f (\lambda x + (1 - \lambda) y)$$

Since x and y in $\mathbb { R } ^ { n }$ and λ in [0, 1] are all arbitrary, the convexity of $f ( \cdot )$ is established. 
