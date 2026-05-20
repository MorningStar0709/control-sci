# 4.7 Particle Filtering

which makes the samples at k depend on current measurement $y ( k )$ as well as the past samples. We know from Bayes’s rule and the Markov property

$$
\begin{array}{l} q (x _ {i} (k) | x _ {i} (k - 1), y (k)) = p (x _ {i} (k) | x _ {i} (k - 1), y (k)) \\ = \frac {p (y (k) | x _ {i} (k) , x _ {i} (k - 1)) p (x _ {i} (k) | x _ {i} (k - 1))}{p (y (k) | x _ {i} (k - 1))} \\ \end{array}
q (x _ {i} (k) | x _ {i} (k - 1), y (k)) = \frac {p (y (k) | x _ {i} (k)) p (x _ {i} (k) | x _ {i} (k - 1))}{p (y (k) | x _ {i} (k - 1))}
$$

Using this result we have for the integral term

$$
\begin{array}{l} \int \frac {p ^ {2} (y (k) | x _ {i} (k)) p ^ {2} (x _ {i} (k) | x _ {i} (k - 1))}{q (x _ {i} (k) | x _ {i} (k - 1) , y (k))} d x _ {i} (k) \\ = p (y (k) \mid x _ {i} (k - 1)) \int p (y (k) \mid x _ {i} (k)) p (x _ {i} (k) \mid x _ {i} (k - 1)) d x _ {i} (k) \\ = p ^ {2} (y (k) | x _ {i} (k - 1)) \\ \end{array}
$$

Substituting this result into the previous equation for conditional variance gives

$$\operatorname{var} \left(w _ {i} (k) \mid x _ {i} (k - 1), \mathbf {y} (k)\right) = 0$$

Since variance is nonnegative, the choice of importance function given in (4.60) is optimal for reducing the conditional variance of the weights. This choice has the important benefit of making the samples $x _ { i } ( k )$ more responsive to the measurement $y ( k )$ , which we show in the next example is a big improvement over the simplest particle filter.
