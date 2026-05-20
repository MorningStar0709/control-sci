# 4.7.6 Optimal Importance Function

In this section we develop the so-called “optimal” importance function $q ( x ( k ) | x _ { i } ( k - 1 ) , y ( k ) )$ ). We start with the weight recursion for the importance function particle filter given in (4.59), repeated here with k replacing $k + 1$

$$w _ {i} (k) = w _ {i} (k - 1) \frac {p (y (k) | x _ {i} (k)) p (x _ {i} (k) | x _ {i} (k - 1))}{q (x _ {i} (k) | x _ {i} (k - 1) , y (k))}$$

We consider the $w _ { i } ( k )$ conditioned on the random variables $x _ { i } ( k \textrm { -- }$ $1 ) , \mathbf { y } ( k )$ . The weight $w _ { i } ( k )$ is then a function of the random variable $x _ { i } ( k )$ , which is sampled from the importance function $q ( x ( k ) | x _ { i } ( k -$

1), $y ( k ) )$ . Taking the expectation gives

$$
\begin{array}{l} \mathcal {E} \left(w _ {i} (k) | x _ {i} (k - 1), \mathbf {y} (k)\right) \\ = \int w _ {i} (k) q \left(x _ {i} (k) \mid x _ {i} (k - 1), y (k)\right) d x _ {i} (k) \\ = \int \frac {p (y (k) | x _ {i} (k)) p (x _ {i} (k) | x _ {i} (k - 1))}{q (x _ {i} (k) | x _ {i} (k - 1) , y (k))} \\ w _ {i} (k - 1) q (x _ {i} (k) | x _ {i} (k - 1), y (k)) d x _ {i} (k) \\ = \int p (y (k) | x _ {i} (k)) p (x _ {i} (k) | x _ {i} (k - 1)) w _ {i} (k - 1) d x _ {i} (k) \\ = w _ {i} (k - 1) p (y (k) | x _ {i} (k - 1)) \\ \end{array}
$$

Next we compute the conditional variance of the weights

$$
\begin{array}{l} \operatorname{var} (w _ {i} (k) | x _ {i} (k - 1), \mathbf {y} (k)) \\ = \mathcal {E} (w _ {i} ^ {2} (k) | x _ {i} (k - 1), \mathbf {y} (k)) - \mathcal {E} ^ {2} (w _ {i} | x _ {i} (k - 1), \mathbf {y} (k)) \\ \end{array}
$$

Using the recursion in the first term and the expectation just derived in the second term gives

$$
\begin{array}{l} \operatorname{var} \left(w _ {i} (k) \mid x _ {i} (k - 1), \mathbf {y} (k)\right) = \\ \int w _ {i} ^ {2} (k) q (x _ {i} (k) | x _ {i} (k - 1), y (k)) d x _ {i} (k) \\ - \left(w _ {i} (k - 1) p (y (k) | x _ {i} (k - 1))\right) ^ {2} \\ \end{array}

\begin{array}{l} \operatorname{var} \left(w _ {i} (k) \mid x _ {i} (k - 1), \mathbf {y} (k)\right) \\ = \int w _ {i} ^ {2} (k - 1) \frac {\left(p (y (k) | x _ {i} (k)) p (x _ {i} (k) | x _ {i} (k - 1))\right) ^ {2}}{q ^ {2} (x _ {i} (k) | x _ {i} (k - 1) , y (k))} \\ q (x _ {i} (k) | x _ {i} (k - 1), y (k)) d x _ {i} (k) - \left(w _ {i} (k - 1) p (y (k) | x _ {i} (k - 1))\right) ^ {2} \\ = w _ {i} ^ {2} (k - 1) \bigg [ \int \frac {p ^ {2} (y (k) | x _ {i} (k)) p ^ {2} (x _ {i} (k) | x _ {i} (k - 1))}{q (x _ {i} (k) | x _ {i} (k - 1) , y (k))} d x _ {i} (k) \\ - \left. p ^ {2} (y (k) | x _ {i} (k - 1)) \right] \\ \end{array}
$$

We can now optimize the choice of $q ( x _ { i } ( k ) | x _ { i } ( k { - } 1 ) , y ( k ) )$ to minimize this conditional variance. Consider the choice

$$\boxed {q \left(x _ {i} (k) \mid x _ {i} (k - 1), y (k)\right) = p \left(x _ {i} (k) \mid x _ {i} (k - 1), y (k)\right)} \tag {4.60}$$
