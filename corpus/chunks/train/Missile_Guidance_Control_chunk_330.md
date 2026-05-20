$$
P (t) = E \{(\mathbf {x} (t) - \hat {\mathbf {x}} (t)) (\mathbf {x} (t) - \hat {\mathbf {x}} (t)) ^ {T} \} = \left[ \begin{array}{c c c} P _ {1 1} & P _ {1 2} & P _ {1 3} \\ P _ {2 1} & P _ {2 2} & P _ {2 3} \\ P _ {3 1} & P _ {3 2} & P _ {3 3} \end{array} \right]
$$

In order to compute the solution for the matrix $P ( t )$ , initial conditions must be specified for $P _ { 1 1 } ( 0 ) , P _ { 1 2 } ( 0 ) , P _ { 1 3 } ( 0 ) , P _ { 2 2 } ( 0 ) , P _ { 2 3 } ( 0 )$ , and $P _ { 3 3 } ( 0 )$ . One of the assumptions of the Kalman–Bucy filter theory is that the filter output at $t = 0$ is zero. Since the matrix $P ( t )$ is the error covariance matrix, the diagonal elements have the following significance:

$$
\begin{array}{l} P _ {1 1} (t) = E \{y _ {T} (t) - y _ {M} (t) \} ^ {2}, \\ P _ {2 2} (t) = E \{v _ {T} (t) - \hat {x} _ {2} (t) \} ^ {2}, \\ P _ {3 3} (t) = E \{a _ {T} (t) - \hat {x} _ {3} (t) \} ^ {2}. \\ \end{array}
$$

The mean-square miss distance is given by $P _ { 1 1 } ( T )$ , where $T$ is the final or intercept time $( t _ { g o } = T - t )$ . At this point it should be pointed out, in general, that the variances of the separate components of x are along the diagonal:

$$P _ {i i} \triangleq E \{(x _ {i} - m _ {i}) ^ {2} \},$$

where $m _ { i }$ is the mean value and is given by $m _ { i } = E \{ x _ { i } \}$ . Therefore, the square root of a variance $P _ { i i }$ is termed the standard deviation of $\mathbf { x } _ { i }$ , and is denoted by $\sigma _ { i }$ . Thus, the diagonal terms can be expressed as

$$P _ {i i} \triangleq \sigma_ {i} ^ {2}.$$
