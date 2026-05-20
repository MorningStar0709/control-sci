# Exercise 4.23: Unbiased particle filter with importance sampling

Show that an unbiased particle filter using importance sampling is given by

$$\overline {{p}} _ {s} (x (k) | \mathbf {y} (k)) = \{x _ {i} (k), \tilde {w} _ {i} (k) \}\tilde {w} _ {i} (k + 1) = \tilde {w} _ {i} (k) \frac {p (y (k + 1) | x _ {i} (k + 1)) p (x _ {i} (k + 1) | x _ {i} (k))}{p (y (k + 1) | \mathbf {y} (k)) q (x _ {i} (k + 1) | x _ {i} (k) , y (k + 1))}$$

in which $x _ { i } ( k )$ are samples of the importance function $q ( x ( k ) | x _ { i } ( k - 1 ) , y ( k ) )$ . Note that normalization of $\tilde { \boldsymbol { w } } _ { i }$ is not required in this form of a particle filter, but evaluation of $p ( y ( k + 1 ) | \mathbf { y } ( k ) )$ ) is required.
