# Example 2.9 Solution of the difference equation

Consider the discrete-time system

$$
x (k + 1) = \left( \begin{array}{c c} \lambda_ {1} & 0 \\ 1 & \lambda_ {2} \end{array} \right) x (k)
$$

with $x(0) = \left( \begin{array}{ll} 1 & 1 \end{array} \right)^T$ . It is easily verified that

$$
\Phi^ {k} = \left( \begin{array}{c c} \lambda_ {1} ^ {k} & 0 \\ \sum_ {j = 1} ^ {k} \lambda_ {1} ^ {k - j} \lambda_ {2} ^ {j - 1} & \lambda_ {2} ^ {k} \end{array} \right)
$$

and

$$x (k) = \binom {\lambda_ {1} ^ {k}} {\sum_ {j = 1} ^ {k} \lambda_ {1} ^ {k - j} \lambda_ {2} ^ {j - 1} + \lambda_ {2} ^ {k}}$$

If $|\lambda_i| < 1, j = 1, 2$ , then $x(k)$ will converge to the origin. If one of the eigenvalues of $\Phi$ has an absolute value larger than 1, then one or both of the states will diverge.
