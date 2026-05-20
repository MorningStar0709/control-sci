where the subscript i denotes which component of each vector and n is the total number of components. To change coordinates, we expanded both v and $\hat { i } + \hat { j }$ in a basis, multiplied their components, and added them up. Here’s a more concrete example. Let ${ \bf v } = 2 \hat { i } + 1 . 5 \hat { j }$ from figure E.8. First, we’ll project v onto the $\hat { i } + \hat { j }$ basis vector.

$$
\begin{array}{l} \frac {\mathbf {v} \cdot (\hat {i} + \hat {j})}{\sqrt {2}} = \frac {1}{\sqrt {2}} (2 \hat {i} \cdot \hat {i} + 1. 5 \hat {j} \cdot \hat {j}) \\ \frac {\mathbf {v} \cdot (\hat {i} + \hat {j})}{\sqrt {2}} = \frac {1}{\sqrt {2}} (2 + 1. 5) \\ \frac {\mathbf {v} \cdot (\hat {i} + \hat {j})}{\sqrt {2}} = \frac {3 . 5}{\sqrt {2}} \\ {\frac {\mathbf {v} \cdot (\hat {i} + \hat {j})}{\sqrt {2}}} = {\frac {3 . 5 \sqrt {2}}{2}} \\ \frac {\mathbf {v} \cdot (\hat {i} + \hat {j})}{\sqrt {2}} = 1. 7 5 \sqrt {2} \\ \end{array}
$$

Next, we’ll project v onto the $\hat { i } - \hat { j }$ basis vector.

$$
\begin{array}{l} \frac {\mathbf {v} \cdot (\hat {i} - \hat {j})}{\sqrt {2}} = \frac {1}{\sqrt {2}} (2 \hat {i} \cdot \hat {i} - 1. 5 \hat {j} \cdot \hat {j}) \\ \frac {\mathbf {v} \cdot (\hat {i} - \hat {j})}{\sqrt {2}} = \frac {1}{\sqrt {2}} (2 - 1. 5) \\ \frac {\mathbf {v} \cdot (\hat {i} - \hat {j})}{\sqrt {2}} = \frac {0 . 5}{\sqrt {2}} \\ \frac {\mathbf {v} \cdot (\hat {i} - \hat {j})}{\sqrt {2}} = \frac {0 . 5 \sqrt {2}}{2} \\ \frac {\mathbf {v} \cdot (\hat {i} - \hat {j})}{\sqrt {2}} = 0. 2 5 \sqrt {2} \\ \end{array}
$$

Figure E.9 shows this result geometrically with respect to the basis $\{ \hat { i } + \hat { j } , \hat { i } - \hat { j } \}$ .

The previous example was only a change of coordinates in a finite-dimensional vector space. However, as we will see, the core idea does not change much when we move to more complicated structures. Observe the formula for the Fourier transform.

$$\hat {f} (\xi) = \int_ {- \infty} ^ {\infty} f (x) e ^ {- 2 \pi i x \xi} d x \text { where } \xi \in \mathbb {R}$$

![](image/6d1b79a98174830fafb59329e719e265974c32bcde92d1a0c8dd00c838a3c2d8.jpg)

<details>
<summary>text_image</summary>

y
0.25√2
v
î - ĵ
1.75√2
x
î - ĵ
</details>

Figure E.9: v with basis $\{ \hat { i } + \hat { j } , \hat { i } - \hat { j } \}$
