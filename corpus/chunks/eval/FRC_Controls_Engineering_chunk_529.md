# E.3.1 Projections

Consider a two-dimensional Euclidean space $\mathbb { R } ^ { 2 }$ shown in figure E.7 (each R is a dimension whose domain is the set of real numbers, so $\mathbb { R } ^ { 2 }$ is the standard x-y plane).

![](image/76f74289b1b8c6660548d1d779f002770806800444a7ac7a0972adbf740ca0a4.jpg)

<details>
<summary>text_image</summary>

y
x
</details>

Figure E.7: Euclidean space $\mathbb { R } ^ { 2 }$

Ordinarily, we notate points in this plane by their components in the set of basis vectors $\{ \hat { i } , \hat { j } \}$ , where $\hat { i }$ (pronounced i-hat) is the unit vector in the positive x direction and $\hat { j }$ is the unit vector in the positive $y$ direction. Figure E.8 shows an example vector v in this basis.

![](image/8c2c1f5844e48b2ca49c13346fd9e60345f2f3ac8a4db1e39398122133b8b029.jpg)

<details>
<summary>text_image</summary>

y
2
v = 2î + 1.5ĵ
1.5
ˆj
ˆi
x
</details>

Figure E.8: v with basis set $\{ \hat { i } , \hat { j } \}$

How do we find the coordinates of v in this basis mathematically? As long as the basis is orthogonal (i.e., the basis vectors are at right angles to each other), we simply take the orthogonal projection of v onto $\hat { i }$ and $\hat { j }$ . Intuitively, this means finding “the amount of v that points in the direction of $\hat { i }$ or $\hat { j } ^ { \dag }$ . Note that a set of orthogonal vectors have a dot product of zero with respect to each other.

More formally, we can calculate projections with the dot product - the projection of v onto any other vector w is as follows.

$$\operatorname{proj} _ {\mathbf {w}} \mathbf {v} = \frac {\mathbf {v} \cdot \mathbf {w}}{| \mathbf {w} |}$$

Since $\hat { i }$ and $\hat { j }$ are unit vectors, their magnitudes are 1 so the coordinates of v are $\mathbf { v } \cdot \hat { i }$ and $\mathbf { v } \cdot \hat { j }$ .

We can use this same process to find the coordinates of v in any orthogonal basis. For example, imagine the basis $\{ \hat { i } + \hat { j } , \hat { i } - \hat { j } \}$ - the coordinates in this basis are given by $\frac { \mathbf { v } \cdot ( \hat { i } + \hat { j } ) } { \sqrt { 2 } }$ an d v·(ˆi−ˆj)√ . Let’s “unwrap” the formula for dot product and look a bit more $\frac { \mathbf { v } \cdot ( \hat { i } - \hat { j } ) } { \sqrt { 2 } }$ √2 closely.

$$\frac {\mathbf {v} \cdot (\hat {i} + \hat {j})}{\sqrt {2}} = \frac {1}{\sqrt {2}} \sum_ {i = 0} ^ {n} \mathbf {v} _ {i} (\hat {i} + \hat {j}) _ {i}$$
