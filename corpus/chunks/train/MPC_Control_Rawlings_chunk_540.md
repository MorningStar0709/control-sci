$$w _ {i} (k + 1) = \frac {p (y (k + 1) | x _ {i} (k + 1)) p (x _ {i} (k + 1) | x _ {i} (k))}{q (x _ {i} (k + 1) | x _ {i} (k) , y (k + 1))} \frac {h (\mathbf {x} _ {i} (k) | \mathbf {y} (k))}{q (\mathbf {x} _ {i} (k) | \mathbf {y} (k))}w _ {i} (k + 1) = \frac {p (y (k + 1) | x _ {i} (k + 1)) p (x _ {i} (k + 1) | x _ {i} (k))}{q (x _ {i} (k + 1) | x _ {i} (k) , y (k + 1))} w _ {i} (k) \tag {4.59}\overline {{w}} _ {i} (k + 1) = \frac {w _ {i} (k + 1)}{\sum_ {j} w _ {j} (k + 1)}$$

Notice we obtain a convenient recursion for the weights that depends only on the values of the samples $x _ { i } ( k + 1 )$ and $x _ { i } ( k )$ and not the rest of the trajectory contained in the samples $\mathbf { x } _ { i } ( k )$ . The trajectory’s sampled density is given by

$$p (x (k + 1), \mathbf {x} (k) | \mathbf {y} (k + 1)) =\sum_ {i = 1} ^ {s} \overline {{w}} _ {i} (k + 1) \delta (x (k + 1) - x _ {i} (k + 1)) \delta (\mathbf {x} (k) - \mathbf {x} _ {i} (k))$$

Integrating both sides over the $\mathbf { x } ( k )$ variables gives the final result

$$p (x (k + 1) | \mathbf {y} (k + 1)) = \sum_ {i = 1} ^ {s} \overline {{w}} _ {i} (k + 1) \delta (x (k + 1) - x _ {i} (k + 1))$$

Since we generate $x _ { i } ( k + 1 )$ from sampling $q ( x ( k + 1 ) | x _ { i } ( k ) , y ( k + 1 ) )$ , the trajectory samples, $\mathbf { x } _ { i } ( k )$ , and measurement trajectory, $\mathbf { y } ( k )$ , are not required at all, and the particle filter storage requirements do not grow with time. Notice also that if we choose the importance function

$$q \left(x _ {i} (k + 1) \mid x _ {i} (k), y (k + 1)\right) = p \left(x _ {i} (k + 1) \mid x _ {i} (k)\right)$$

which ignores the current measurement when sampling, we obtain for the weights

$$w _ {i} (k + 1) = w _ {i} (k) p (y (k + 1) | x _ {i} (k + 1))$$

This choice of importance function reduces to the simplest particle filter of the previous section, with its concomitant drawbacks.

Summary. We select an importance function $q ( x ( k + 1 ) | x ( k ) , y ( k +$ 1)). We start with s samples of $p ( x ( 0 ) )$ . We assume that we can evaluate $p ( y ( k ) | x ( k ) )$ using the measurement equation and $p ( x ( k +$

$1 ) | x ( k ) )$ using the model equation. The importance function particle filter is summarized by the following recursion
