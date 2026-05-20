# 4.7.1 The Sampled Density of a Transformed Random Variable

Given the random variable $\xi ,$ , assume we have a sampled density for its density $p _ { \xi } ( x )$

$$p _ {\xi} (x) = \sum_ {i = 1} ^ {s} w _ {i} \delta (x - x _ {i})$$

Define a new random variable η by an invertible, possibly nonlinear transformation

$$\eta = f (\xi) \quad \xi = f ^ {- 1} (\eta)$$

We wish to find a sampled density for the random variable η, $p _ { \eta } ( y )$ . Denote the sampled density for η as

$$p _ {\eta} (y) = \sum_ {i = 1} ^ {s} \overline {{w}} _ {i} \delta (y - y _ {i})$$

We wish to find formulas for $\overline { { { w _ { i } } } }$ and $y _ { i }$ in terms of $w _ { i } , x _ { i }$ and $f .$ . We proceed as in the development of equation (A.30) in Appendix A. We wish to have an equivalence for every function $g ( x )$

$$
\begin{array}{l} \mathcal {E} _ {p _ {\xi}} (g (\xi)) = \mathcal {E} _ {p _ {\eta}} (g (f ^ {- 1} (\eta))) \\ \int p _ {\xi} (x) g (x) d x = \int p _ {\eta} (y) g (f ^ {- 1} (y)) d y \quad \text { for   all } g (\cdot) \\ \end{array}
$$

Using the sampled densities on both sides of the equation

$$\sum_ {i} w _ {i} g (x _ {i}) = \sum_ {i} \overline {{w}} _ {i} g (f ^ {- 1} (y _ {i}))$$

One solution to this equation that holds for every $^ g$ is the simple choice

$$y _ {i} = f (x _ {i}) \quad \overline {{{w}}} _ {i} = w _ {i} \tag {4.37}$$

We see that for the transformed sampled density, we transform the samples and use the weights of the original density.
