# 4.7 Particle Filtering

as well as evaluating $P ^ { - 1 } ( x )$ , which generally requires solving nonlinear equations. Importance sampling is a method for sampling $p ( x )$ without performing integration or solving nonlinear equations.

The following idea motivates importance sampling. Consider the random variable $\xi$ to be distributed with density $p$ . Consider a new random variable $\eta$ to be distributed with density $q$

$$\xi \sim p (x) \quad \eta \sim q (x)$$

The density $q ( x )$ , known as the importance function, is any density that can be readily sampled according to (4.38) and has the same support as $p$ . Examples of such $q$ are uniforms for bounded intervals, lognormals and exponentials for semi-infinite intervals, and normals for infinite intervals. For any function $g ( x )$ , we have

$$
\begin{array}{l} \mathcal {E} _ {p} (g (\xi)) = \int g (x) p (x) d x \\ = \int \left[ g (x) \frac {p (x)}{q (x)} \right] q (x) d x \\ \mathcal {E} _ {p} (g (\xi)) = \mathcal {E} _ {q} \left(g (\eta) \frac {p (\eta)}{q (\eta)}\right) \quad \text {   for   all   } g (\cdot) \\ \end{array}
$$

When we can sample p directly, we use for the sampled density

$$p _ {s} = \left\{x _ {i}, \quad w _ {i} = \frac {1}{s} \right\} \quad p _ {s a} (x _ {i}) = p (x _ {i})$$

So when we cannot conveniently sample $p$ but can sample $q ,$ we use instead

$$\overline {{p}} _ {s} = \left\{x _ {i}, \quad w _ {i} = \frac {1}{s} \frac {p (x _ {i})}{q (x _ {i})} \right\} \quad p _ {i s} (x _ {i}) = q (x _ {i})$$

Given s samples $x _ { i }$ from $q ( x )$ , denote the sampled density of $q$ as $q _ { s }$ , and we have defined the importance-sampled density $\overline { { p } } _ { s } ( x )$ as

$$\overline {{{p}}} _ {s} (x) = q _ {s} (x) \frac {p (x)}{q (x)}$$

We next show that $\overline { { p } } _ { s } ( x )$ converges to $p ( x )$ as sample size increases (Smith and Gelfand, 1992). Using the fact that $q _ { s }$ converges to $q$ gives

$$\lim _ {s \rightarrow \infty} \overline {{p}} _ {s} (x) = \lim _ {s \rightarrow \infty} q _ {s} (x) \frac {p (x)}{q (x)} = p (x)$$

![](image/f598e4a12d63a3cf25a9940964753caa19b27f3a27c12ac253e51aec7b605dbd.jpg)

<details>
<summary>line</summary>

| x | P(x) | p(x) |
| --- | --- | --- |
| -2 | 0.0 | 0.0 |
| 0 | 0.0 | 0.0 |
| 2 | 0.2 | 0.3 |
| 4 | 0.8 | 0.4 |
| 6 | 0.95 | 0.1 |
| 8 | 1.0 | 0.0 |
</details>

Figure 4.15: Probability density $p ( x )$ to be sampled and the corresponding cumulative distribution P (x).

![](image/bcc777800b57c46ed5f23e5ca47f929851988a5c25b339541f228cde37bd4e1e.jpg)
