# 4.7 Particle Filtering

Taking $w _ { i } ( k - 1 )$ outside the integral and performing the integral over $x _ { i } ( k )$ and then $y ( k )$ gives

$$E (w _ {i} (k) | x _ {i} (k - 1), \mathbf {y} (k - 1)) = w _ {i} (k - 1) \int p (y (k) | x _ {i} (k - 1)) d y (k)E (w _ {i} (k) | x _ {i} (k - 1), \mathbf {y} (k - 1)) = w _ {i} (k - 1)$$

Taking the variance of both sides and using the conditional variance formula (4.54) gives

$$\operatorname{var} \left(E \left(w _ {i} (k) \mid x _ {i} (k - 1), \mathbf {y} (k - 1)\right)\right) = \operatorname{var} \left(w _ {i} (k - 1)\right)\operatorname{var} \left(w _ {i} (k)\right) - E \left(\operatorname{var} \left(w _ {i} (k) \mid x _ {i} (k - 1), \mathbf {y} (k - 1)\right)\right) = \operatorname{var} \left(w _ {i} (k - 1)\right)$$

Again, noting that variance is nonnegative gives the inequality

$$\operatorname{var} (w _ {i} (k)) \geq \operatorname{var} (w _ {i} (k - 1))$$

and we see that the variance for the unbiased weights of the simplest particle filter increases with time.

Next we present two examples that show the serious practical limitations of the simplest particle filter and the simplest particle filter with resampling.
