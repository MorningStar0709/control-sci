# 4.7 Particle Filtering

as follows

$$
\begin{array}{l} \mathcal {E} (\mathcal {E} (g (A) | B)) = \int p _ {B} (b) \int p _ {A | B} (a | b) g (a) d a d b \\ = \int p _ {B} (b) \int \frac {p _ {A , B} (a , b)}{p _ {B} (b)} g (a) d a d b \\ = \iint p _ {A, B} (a, b) g (a) d a d b \\ = \int p _ {A} (a) g (a) d a \\ = \mathcal {E} (g (A)) \\ \end{array}
$$

We require a second identity

$$\operatorname{var} (A) = \mathcal {E} (\operatorname{var} (A | B)) + \operatorname{var} (\mathcal {E} (A | B)) \tag {4.54}$$

which is known as the conditional variance formula or the law of total variance. We establish this identity as follows. Starting with the definition of variance

$$\operatorname{var} (A) = \mathcal {E} (A ^ {2}) - \mathcal {E} ^ {2} (A)$$

we use (4.53) to obtain

$$\operatorname{var} (A) = \mathcal {E} (\mathcal {E} (A ^ {2} | B)) - \mathcal {E} ^ {2} (\mathcal {E} (A | B))$$

Using the definition of variance on the first term on the right-hand side gives

$$
\begin{array}{l} \operatorname{var} (A) = \mathcal {E} (\operatorname{var} (A | B) + \mathcal {E} ^ {2} (A | B)) - \mathcal {E} ^ {2} (\mathcal {E} (A | B)) \\ = \mathcal {E} (\operatorname{var} (A | B)) + \mathcal {E} \left(\mathcal {E} ^ {2} (A | B)\right) - \mathcal {E} ^ {2} (\mathcal {E} (A | B)) \\ \end{array}
$$

and using the definition of variance again on the last two terms on the right-hand side gives

$$\operatorname{var} (A) = \mathcal {E} (\operatorname{var} (A | B)) + \operatorname{var} (\mathcal {E} (A | B))$$

which establishes the result. Notice that since variance is nonnegative, this result also implies the inequality

$$\operatorname{var} (\mathcal {E} (A | B)) \leq \operatorname{var} (A)$$

which shows that the conditional expectation of random variable A has less variance than A itself.

We proceed to analyze the simplest particle filter. Actually we analyze the behavior of the weights for the idealized, unbiased case given by (4.51)

$$w _ {i} (k) = w _ {i} (k - 1) \frac {p (y (k) | x _ {i} (k))}{p (y (k) | \mathbf {y} (k - 1))}$$

in which we consider the random variable $w _ { i } ( k )$ to be a function of the random variables $y ( k ) , x _ { i } ( k )$ . We next consider the conditional density of the random variables $y ( k ) , x _ { i } ( k )$ relative to the previous samples $x _ { i } ( k - 1 )$ , and the data $\mathbf { y } ( k - 1 )$ . We have
