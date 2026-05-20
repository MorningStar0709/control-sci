# Example A.39: Nonlinear transformation

Show that

$$p _ {\eta} (y) = \frac {1}{3 \sqrt {2 \pi} \sigma y ^ {2 / 3}} \exp \left[ - \frac {1}{2} \left(\frac {y ^ {1 / 3} - m}{\sigma}\right) ^ {2} \right]$$

is the density function of the random variable η under the transformation

$$\eta = \xi^ {3}$$

for $\xi \sim N ( m , \sigma ^ { 2 } )$ . Notice that the density $p _ { \eta }$ is singular at $y = 0$ .

Noninvertible transformations. Given n random variables $\xi = ( \xi _ { 1 } , \xi _ { 2 }$ , $\ldots , \xi _ { n } )$ with joint density $p _ { \xi }$ and k random variables $\eta = ( \eta _ { 1 } , \eta _ { 2 } , \dots , \eta _ { k } )$ defined by the transformation $\eta = f ( \xi )$

$$\eta_ {1} = f _ {1} (\xi) \quad \eta_ {2} = f _ {2} (\xi) \quad \dots \quad \eta_ {k} = f _ {k} (\xi)$$

We wish to find $p _ { \eta }$ in terms of $p _ { \xi }$ . Consider the region generated in $\mathbb { R } ^ { n }$ by the vector inequality

$$f (x) \leq c$$

![](image/2ecea1ffe19e72527866c5f4d57e668e47cb1dbc171dcb22ef6dee24eefb39e5.jpg)

<details>
<summary>text_image</summary>

x₂
X(c)
c
c
x₁
</details>

Figure A.12: The region $\mathbb { X } ( c )$ for $y = \operatorname* { m a x } ( x _ { 1 } , x _ { 2 } ) \leq c$ .

Call this region $\mathbb { X } ( c )$ , which is by definition

$$\mathbb {X} (c) = \{x | f (x) \leq c \}$$

Note X is not necessarily simply connected. The probability distribution (not density) for η then satisfies

$$P _ {\eta} (y) = \int_ {\mathbb {X} (y)} p _ {\xi} (x) d x \tag {A.31}$$

If the density $p _ { \eta }$ is of interest, it can be obtained by differentiating $P _ { \eta }$
