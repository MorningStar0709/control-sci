# Exercise 1.34: Calculating mean and variance from data

We are sampling a real-valued scalar random variable $x ( k ) \in \mathbb { R }$ at time k. Assume the random variable comes from a distribution with mean x and variance P, and the samples at different times are statistically independent.

A colleague has suggested the following formulas for estimating the mean and variance from N samples

$$\hat {x} _ {N} = \frac {1}{N} \sum_ {j = 1} ^ {N} x (j) \quad \hat {P} _ {N} = \frac {1}{N} \sum_ {j = 1} ^ {N} (x (j) - \hat {x} _ {N}) ^ {2}$$

(a) Prove that the estimate of the mean is unbiased for all N, i.e., show that for all N

$$\mathcal {E} (\hat {x} _ {N}) = \overline {{x}}$$

(b) Prove that the estimate of the variance is not unbiased for any N, i.e., show that for all N

$$\mathcal {E} (\hat {P} _ {N}) \neq P$$

(c) Using the result above, provide an alternative formula for the variance estimate that is unbiased for all N. How large does N have to be before these two estimates of P are within 1%?
