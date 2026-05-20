# Exercise 6.5: Recursively summing quadratic functions

Consider generalizing Example 1.1 to an N-term sum. Let the N-term sum of quadratic functions be defined as

$$V (N, x) = \frac {1}{2} \sum_ {i = 1} ^ {N} (x - x (i)) ^ {\prime} X _ {i} (x - x (i))$$

in which $x , x ( i ) \in \mathbb { R } ^ { n }$ are real n-vectors and $X _ { i } \in \mathbb { R } ^ { n \times n }$ are positive definite matrices.

(a) Show that $V ( N , x )$ can be found recursively

$$V (N, x) = (1 / 2) (x - \nu (N)) ^ {\prime} H (N) (x - \nu (N)) + \text { constant }$$

in which v(i) and H(i) satisfy the recursion

$$H (i + 1) = H _ {i} + X _ {i + 1} \quad v (i + 1) = H ^ {- 1} (i + 1) \left(H _ {i} v _ {i} + X _ {i + 1} x (i + 1)\right)H _ {1} = X _ {1} \quad v _ {1} = x _ {1}$$

Notice the recursively defined $\nu ( m )$ and $H ( m )$ provide the solutions and the Hessian matrices of the sequence of optimization problems

$$\min _ {x} V (m, x) \quad 1 \leq m \leq N$$

(b) Check your answer by solving the equivalent, but larger dimensional, constrained least squares problem (see Exercise 1.16)

$$\min _ {z} (z - z _ {0}) ^ {\prime} \tilde {H} (z - z _ {0})$$

subject to

$$D z = 0$$

in which $z , z _ { 0 } \in \mathbb { R } ^ { n N } , \tilde { H } \in \mathbb { R } ^ { n N \times n N }$ is a block diagonal matrix, $D \in \mathbb { R } ^ { n ( N - 1 ) \times n N }$

$$
z _ {0} = \left[ \begin{array}{c} x (1) \\ \vdots \\ x (N - 1) \\ x (N) \end{array} \right] \qquad \tilde {\widetilde {H}} = \left[ \begin{array}{c c c c} X _ {1} & & & \\ & \ddots & & \\ & & X _ {N - 1} & \\ & & & X _ {N} \end{array} \right] \qquad D = \left[ \begin{array}{c c c c} I & - I & & \\ & \ddots & \ddots & \\ & & I & - I \end{array} \right]
$$

(c) Compare the size and number of matrix inverses required for the two approaches.
