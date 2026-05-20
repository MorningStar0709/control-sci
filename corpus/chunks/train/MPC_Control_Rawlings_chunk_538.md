$$p (\mathbf {x} (k + 1) | \mathbf {y} (k + 1)) = \frac {p (y (k + 1) | \mathbf {x} (k + 1)) p (\mathbf {x} (k + 1) | \mathbf {y} (k))}{p (y (k + 1) | \mathbf {y} (k))} \tag {4.55}$$

in which we have used the second identity in Exercise 1.47 and the Markov property, which implies

$$p (y (k + 1) | \mathbf {x} (k + 1), y (k)) = p (y (k + 1) | \mathbf {x} (k + 1))$$

Again, because the process is Markov $p ( y ( k + 1 ) | \mathbf { x } ( k + 1 ) ) = p ( y ( k +$ $1 ) | x ( k { + } 1 ) )$ . We next use the identity $p _ { A , B | C } ( a , b | c ) = p _ { A | B , C } ( a | b , c ) p _ { B | C } ( b | c )$ (see Exercise 1.46) and obtain

$$p (\mathbf {x} (k + 1) | \mathbf {y} (k)) = p (x (k + 1) | \mathbf {x} (k), \mathbf {y} (k)) p (\mathbf {x} (k) | \mathbf {y} (k))$$

Again using the Markov property in this equation, we know $p ( x ( k { \mathrm { ~ + ~ } }$ $1 ) | \mathbf { x } ( k ) , \mathbf { y } ( k ) ) = p ( x ( k + 1 ) | x ( k ) )$ and therefore

$$p (\mathbf {x} (k + 1) | \mathbf {y} (k)) = p (x (k + 1) | x (k)) p (\mathbf {x} (k) | \mathbf {y} (k))$$

Substituting these relations into (4.55) gives

$$p (\mathbf {x} (k + 1) | \mathbf {y} (k + 1)) =\frac {p (y (k + 1) \mid x (k + 1)) p (x (k + 1) \mid x (k))}{p (y (k + 1) \mid \mathbf {y} (k))} p (\mathbf {x} (k) \mid \mathbf {y} (k)) \tag {4.56}$$

We use importance sampling to sample this density. Notice the denominator does not depend on $\mathbf { x } ( k + 1 )$ and is therefore not required when using importance sampling. We use instead

$$p (\mathbf {x} (k + 1) | \mathbf {y} (k + 1)) = \frac {h (\mathbf {x} (k + 1))}{\int h (\mathbf {x} (k + 1)) d \mathbf {x} (k + 1)}h (\mathbf {x} (k + 1)) =p (y (k + 1) \mid x (k + 1)) p (x (k + 1) \mid x (k)) p (\mathbf {x} (k) \mid \mathbf {y} (k)) \tag {4.57}$$

Note also that using importance sampling here when we do not wish to evaluate the normalizing constant introduces bias for finite sample size
