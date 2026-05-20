# 4.7 Particle Filtering

as stated in (4.49). We now state the two properties of $q$ that provide a convenient importance function

$$q (x (k + 1) | \mathbf {x} (k), \mathbf {y} (k + 1)) = q (x (k + 1) | x (k), y (k + 1))q (\mathbf {x} (k + 1) | \mathbf {y} (k + 1)) =q (x (k + 1) | x (k), y (k + 1)) q (\mathbf {x} (k) | \mathbf {y} (k)) \tag {4.58}$$

The first property of $q$ is satisfied also by the density $p ,$ so it is not unusual to pick an importance function to share this behavior. The second property is not satisfied by the density, however, and it is chosen strictly for convenience; it allows a recursive evaluation of $q$ at time $k + 1$ from the value at time k. See Exercise 4.18 for further discussion of this point.

Next we need to generate the samples of $q ( \mathbf { x } ( k + 1 ) | \mathbf { y } ( k + 1 ) )$ . Given the second property in (4.58), we have

$$
\begin{array}{l} q (\mathbf {x} (k + 1) | \mathbf {y} (k + 1)) = q (x (k + 1), x (k), \mathbf {x} (k - 1) | y (k + 1), \mathbf {y} (k)) \\ = q (x (k + 1) | x (k), y (k + 1)) q (x (k), \mathbf {x} (k - 1) | \mathbf {y} (k)) \\ \end{array}
$$

which is of the form studied in Example 4.32 with the substitution

$$a = x (k + 1) \quad b = x (k) \quad c = \mathbf {x} (k - 1) \quad d = y (k + 1) \quad e = \mathbf {y} (k)$$

Using the results of that example, our sampling procedure is as follows. We have available samples of $q ( { \bf x } ( k ) , { \bf y } ( k ) ) = q ( x ( k ) , { \bf x } ( k - 1 ) | { \bf y } ( k ) )$ . Denote these samples by $( x _ { i } ( k ) , \mathbf { x } _ { i } ( k - 1 ) ) , i = 1 , \ldots , s .$ . Then we draw one sample from $q ( x ( k + 1 ) | x _ { i } ( k ) , y ( k + 1 ) )$ ) for each $i = 1 , \dots , s .$ . Denote these samples as $x _ { i } ( k + 1 )$ . Then the samples of $q ( \mathbf { x } ( k + 1 ) | \mathbf { y } ( k +$ 1)) are given by $( x _ { i } ( k + 1 ) , x _ { i } ( k ) , \mathbf { x } _ { i } ( k - 1 ) ) = ( x _ { i } ( k + 1 ) , \mathbf { x } _ { i } ( k ) )$ . So we have

$$\mathbf {x} _ {i} (k + 1) = \left(x _ {i} (k + 1), \mathbf {x} _ {i} (k)\right) \quad i = 1, \dots , s$$

Next we evaluate the weights for these samples

$$w _ {i} (k + 1) = \frac {h (\mathbf {x} _ {i} (k + 1) | \mathbf {y} (k + 1))}{q (\mathbf {x} _ {i} (k + 1) | \mathbf {y} (k + 1))}$$

Using (4.57) to evaluate h and the second property of the importance

function to evaluate q gives
