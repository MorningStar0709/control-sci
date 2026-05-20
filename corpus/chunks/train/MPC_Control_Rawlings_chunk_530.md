$$
\begin{array}{l} p (y (k), x _ {i} (k) | \mathbf {y} (k - 1), x _ {i} (k - 1)) \\ = p (y (k) | \mathbf {y} (k - 1), x _ {i} (k - 1)) p (x _ {i} (k) | \mathbf {y} (k - 1), x _ {i} (k - 1)) \\ = p (y (k) | \mathbf {y} (k - 1)) p (x _ {i} (k) | x _ {i} (k - 1)) \\ \end{array}
$$

The first equation results from the statistical independence of $y ( k )$ and $x _ { i } ( k )$ , and the second results from the sampling procedure used to generate $x _ { i } ( k )$ given $x _ { i } ( k - 1 )$ . Note that in the next section, we use a different sampling procedure in which $x _ { i } ( k )$ depends on both the new data $y ( k )$ as well as the $x _ { i } ( k - 1 )$ . Now we take the expectation of the weights at time k conditional on the previous samples and previous measurement trajectory

$$
\begin{array}{l} E (w _ {i} (k) | x _ {i} (k - 1), \mathbf {y} (k - 1)) \\ = \iint w _ {i} (k) p (y (k), x _ {i} (k) | x _ {i} (k - 1), \mathbf {y} (k - 1)) d x _ {i} (k) d y (k) \\ = \iint w _ {i} (k) p (y (k) | \mathbf {y} (k - 1)) p (x _ {i} (k) | x _ {i} (k - 1)) d x _ {i} (k) d y (k) \\ \end{array}
$$

Substituting the weight recursion and simplifying yields

$$
\begin{array}{l} E (w _ {i} (k) | x _ {i} (k - 1), \mathbf {y} (k - 1)) \\ = \iint w _ {i} (k - 1) \frac {p (y (k) | x _ {i} (k))}{p (y (k) | \mathbf {y} (k - 1))} \\ p (y (k) | \mathbf {y} (k - 1)) p (x _ {i} (k) | x _ {i} (k - 1)) d x _ {i} (k) d y (k) \\ \end{array}

\begin{array}{l} E (w _ {i} (k) | x _ {i} (k - 1), \mathbf {y} (k - 1)) \\ = \iint w _ {i} (k - 1) p (y (k) | x _ {i} (k)) p (x _ {i} (k) | x _ {i} (k - 1)) d x _ {i} (k) d y (k) \\ \end{array}
$$
