# 4.7.4 The Simplest Particle Filter

Next we implement these sampling ideas for state estimation. This first version follows the approach given by Gordon, Salmond, and Smith (1993). In state estimation, the density $p ( x ( k ) | \mathbf { y } ( k ) )$ contains the information of most interest. The model is of the form

$$x (k + 1) = f (x (k), n (k))y (k) = h (x (k), m (k))$$

in which f is a possibly nonlinear function of the state and process noise, n, and h is a possibly nonlinear function of the state and measurement noise, m. We assume that the densities of m, n and x(0) are available. To start things off, first assume the conditional density $p ( x ( k ) | \mathbf { y } ( k ) )$ is available as a sampled density

$$p (x (k) | \mathbf {y} (k)) = \sum_ {i = 1} ^ {s} w _ {i} (k) \delta (x (k) - x _ {i} (k))$$

and we wish to find samples for $p ( x ( k + 1 ) | \mathbf { y } ( k ) )$ . The state evolution can be considered a noninvertible transformation from $x ( k ) , n ( k )$ to $x ( k { + } 1 )$ , in which $n ( k )$ is statistically independent of $x ( k )$ and ${ \bf y } ( k )$ . We generate s samples of $n ( k )$ , call these $n _ { i } ( k )$ , and we have s samples of the conditional density $p ( x ( k ) , n ( k ) | \mathbf { y } ( k ) )$ given by $\{ x _ { i } ( k ) , n _ { i } ( k ) \} , i =$ $1 , \ldots , s .$ . As shown in Section 4.7.1, the sampled density of $p ( x ( k { \mathrm { ~ + ~ } }$ $1 ) | \mathbf { y } ( k ) )$ is given by

$$p (x (k + 1) | \mathbf {y} (k)) = \left\{x _ {i} (k + 1), w _ {i} ^ {-} (k + 1) \right\}x _ {i} (k + 1) = f \left(x _ {i} (k), n _ {i} (k)\right) \quad w _ {i} ^ {-} (k + 1) = w _ {i} (k)$$

Next, given the sampled density for the conditional density $p ( x ( k ) |$ | $\mathbf { y } ( k - 1 ) )$

$$p (x (k) | \mathbf {y} (k - 1)) = \sum_ {i = 1} ^ {s} w _ {i} ^ {-} (k) \delta (x (k) - x _ {i} (k))$$

we add the measurement $y ( k )$ to obtain the sampled density $p ( x ( k ) |$ $\mathbf { y } ( k ) )$ . Notice that $\mathbf { y } ( k ) = ( y ( k ) , \mathbf { y } ( k - 1 ) )$ and use the relationship (see Exercise 1.47)

$$p _ {A | B, C} (a | b, c) = p _ {C | A, B} (c | a, b) \frac {p _ {A | B} (a | b)}{p _ {C | B} (c | b)}$$

to obtain

$$p (x (k) | \mathbf {y} (k)) = \frac {p (y (k) | x (k) , \mathbf {y} (k - 1)) p (x (k) | \mathbf {y} (k - 1))}{p (y (k) | \mathbf {y} (k - 1))}$$

Because the process is Markov, $p ( y ( k ) | x ( k ) , \mathbf { y } ( k - 1 ) ) = p ( y ( k ) | x ( k ) )$ , and we have

$$p (x (k) | \mathbf {y} (k)) = \frac {p (y (k) | x (k)) p (x (k) | \mathbf {y} (k - 1))}{p (y (k) | \mathbf {y} (k - 1))}$$

The density of interest is in the form
