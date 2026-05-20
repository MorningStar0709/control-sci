$$p (x (k) | \mathbf {y} (k)) = g (x (k)) p (x (k) | \mathbf {y} (k - 1))g (x (k)) = \frac {p (y (k) | x (k))}{p (y (k) | \mathbf {y} (k - 1))}$$

and we have a sampled density for $p ( x ( k ) | \mathbf { y } ( k - 1 ) )$ . If we could conveniently evaluate $^ { g , }$ , then we could obtain a sampled density using the product rule given in (4.36)

$$p (x (k) | \mathbf {y} (k)) = \{x _ {i} (k), \tilde {w} _ {i} (k) \}$$

in which

$$\tilde {w} _ {i} (k) = w _ {i} ^ {-} (k) \frac {p (y (k) | x _ {i} (k))}{p (y (k) | \mathbf {y} (k - 1))} \tag {4.51}$$

This method would provide an unbiased sampled density, but it is inconvenient to evaluate the term $p ( y ( k ) | \mathbf { y } ( k - 1 ) )$ . So we consider an alternative in which the available sampled density is used as a weighted importance function for the conditional density of interest. If we define the importance function $q ( x ( k ) ) \ = \ p ( x ( k ) | \mathbf { y } ( k - 1 ) )$ , then the conditional density is of the form

$$p (x (k) | \mathbf {y} (k)) = \frac {h (x (k))}{\int h (x (k)) d x (k)}h (x (k)) = p (y (k) | x (k)) p (x (k) | \mathbf {y} (k - 1))$$

We then use weighted importance sampling and (4.50) to obtain

$$p (x (k) | \mathbf {y} (k)) = \left\{x _ {i} (k), \overline {{w}} _ {i} (k) \right\} \quad w _ {i} (k) = w _ {i} ^ {-} (k) p (y (k) | x _ {i} (k))\overline {{w}} _ {i} (k) = \frac {w _ {i} (k)}{\sum_ {j} w _ {j} (k)}$$

By using this form of importance sampling, the sampled density is biased for all finite sample sizes, but converges to $p ( x ( k ) | \mathbf { y } ( k ) )$ as the sample size increases.

Summary. Starting with s samples of $p ( n ( k ) )$ and s samples of $p ( x ( 0 ) )$ , we assume that we can evaluate $p ( y ( k ) | x ( k ) )$ ) using the measurement equation. The iteration for the simple particle filter is summarized by the following recursion.

$$
\begin{array}{l} p (x (0)) = \left\{x _ {i} (0), w _ {i} (0) = 1 / s \right\} \\ p (x (k) | \mathbf {y} (k)) = \left\{x _ {i} (k), \overline {{w}} _ {i} (k) \right\} \\ w _ {i} (k) = \overline {{w}} _ {i} (k - 1) p (y (k) | x _ {i} (k)) \\ \overline {{w}} _ {i} (k) = \frac {w _ {i} (k)}{\sum_ {j} w _ {j} (k)} \\ p (x (k + 1) | \mathbf {y} (k)) = \left\{x _ {i} (k + 1), \overline {{w}} _ {i} (k) \right\} \\ x _ {i} (k + 1) = f \left(x _ {i} (k), n _ {i} (k)\right) \\ \end{array}
$$

The sampled density of the simplest particle filter converges to the conditional density $p ( x ( k ) | \mathbf { y } ( k ) )$ in the limit of large sample size. The sampled density is biased for all finite sample sizes.
