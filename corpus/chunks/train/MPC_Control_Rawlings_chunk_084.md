then the conditional density of x given y is also normal

$$p _ {x \mid y} (x \mid y) = n (x, m, P) \tag {1.23}$$

in which the mean is

$$m = m _ {x} + P _ {x y} P _ {y} ^ {- 1} (y - m _ {y})$$

and the covariance is

$$P = P _ {x} - P _ {x y} P _ {y} ^ {- 1} P _ {y x}$$

Note that the conditional mean m is itself a random variable because it depends on the random variable y.

To derive the optimal estimator, we actually require these three main results conditioned on additional random variables. The analogous results are the following.

Joint independent normals. If $p _ { x | z } ( x | z )$ is normal, and y is statistically independent of x and z and normally distributed

$$p _ {x \mid z} (x \mid z) = n (x, m _ {x}, P _ {x})y \sim N (m _ {y}, P _ {y}) \quad y \text { independent of } x \text { and } z$$

then the conditional joint density of $( x , y )$ given z is

$$
p _ {x, y \mid z} (x, y \mid z) = n (x, m _ {x}, P _ {x}) n (y, m _ {y}, P _ {y})
p _ {x, y \mid z} \left(\left[ \begin{array}{l} x \\ y \end{array} \right] \mid z\right) = n \left(\left[ \begin{array}{l} x \\ y \end{array} \right], \left[ \begin{array}{l} m _ {x} \\ m _ {y} \end{array} \right], \left[ \begin{array}{c c} P _ {x} & 0 \\ 0 & P _ {y} \end{array} \right]\right) \tag {1.24}
$$

Linear transformation of a normal.

$$p _ {x \mid z} (x \mid z) = n (x, m, P) \quad y = A xp _ {y \mid z} (y \mid z) = n (y, A m, A P A ^ {\prime}) \tag {1.25}$$

Conditional of a joint normal. If x and y are jointly normally distributed as

$$
p _ {x, y \mid z} \left(\left[ \begin{array}{c} x \\ y \end{array} \right] \bigg |   z\right) = n \left(\left[ \begin{array}{c} x \\ y \end{array} \right], \left[ \begin{array}{c} m _ {x} \\ m _ {y} \end{array} \right], \left[ \begin{array}{c c} P _ {x} & P _ {x y} \\ P _ {y x} & P _ {y} \end{array} \right]\right)
$$

then the conditional density of x given $y , z$ is also normal

$$p _ {x \mid y, z} (x \mid y, z) = n (x, m, P) \tag {1.26}$$

in which

$$m = m _ {x} + P _ {x y} P _ {y} ^ {- 1} (y - m _ {y})P = P _ {x} - P _ {x y} P _ {y} ^ {- 1} P _ {y x}$$
