# Complete State Information

Assume that $v(k) \equiv 0$ in (11.3) but that the initial state is uncertain. Theorem 11.2 gives

$$
\begin{array}{l} J = \mathbf {E} \left(\sum_ {k = 0} ^ {N - 1} \left(x ^ {T} (k) Q _ {1} x (k) + u ^ {T} (k) Q _ {2} u (k) + 2 x ^ {T} (k) Q _ {1 2} u (k)\right) + x ^ {T} (N) Q _ {0} x (N)\right) \\ = \mathbf {E} (x ^ {T} (0) S (0) x (0)) \\ + \mathrm{E} \left(\sum_ {k = 0} ^ {N - 1} (u (k) + L (k) x (k)) ^ {T} (\Gamma^ {T} S (k + 1) \Gamma + Q _ {2}) (u (k) + L (k) x (k))\right) \\ \end{array}
$$

Because $S(k)$ is positive semidefinite, the second term is nonnegative. Further, $S(k)$ is independent of $u(k)$ , and it follows that

$$J _ {\text { complete }} \geq \mathbf {E} x ^ {T} (0) S (0) x (0) = m _ {0} ^ {T} S (0) m _ {0} + \operatorname{tr} S (0) R _ {0} \tag {11.29}$$

where (11.28) has been used. Equality is obtained for the control law of (11.18). Theorem 11.2 and (11.29) give an alternative way to prove Theorem 11.1.

Now assume that there are stochastic disturbances acting on the system and that the full state is still measurable. Using Theorem 11.2, (11.22), and that $v(k)$ is independent of $u(k)$ and $x(k)$ gives

$$
\begin{array}{l} J = \mathrm{E} \left(x ^ {T} (0) S (0) x (0) + \sum_ {k = 0} ^ {N - 1} v ^ {T} (k) S (k + 1) v (k) \right. \\ \left. + \sum_ {k = 0} ^ {N - 1} (u (k) + L (k) x (k)) ^ {T} (\Gamma^ {T} S (k + 1) \Gamma + Q _ {2}) (u (k) + L (k) x (k))\right) \tag {11.30} \\ \end{array}
$$

Using (11.28) gives the relationship

$$J _ {\text { noise }} \geq m _ {0} ^ {T} S (0) m _ {0} + \operatorname{tr} S (0) R _ {0} + \sum_ {k = 0} ^ {N - 1} \operatorname{tr} S (k + 1) R _ {1} \tag {11.31}$$

Equality is obtained for the control law of (11.18), which is an admissible control law. The difference in the optimal costs of (11.29) and (11.31) is due to the disturbance $v(k)$ . The control law of (11.18) thus minimizes the loss for the complete state information case.

Assume on the other hand that $v(k)$ is known when determining $u(k)$ . From (11.23) it follows that the loss function is minimized for

$$u (k) = - L (k) x (k) - L _ {v} (k) v (k) \tag {11.32}$$

where $L_{\nu}$ is given by (11.24) and the minimum loss is

$$
\begin{array}{l} J = m _ {0} ^ {T} S (0) m _ {0} + \operatorname{tr} S (0) R _ {0} + \sum_ {k = 0} ^ {N - 1} \operatorname{tr} S (k + 1) R _ {1} \\ - \sum_ {k = 0} ^ {N - 1} \operatorname{tr} L _ {v} (k) R _ {1} L _ {v} ^ {T} (k) \left(\Gamma^ {T} S (k + 1) \Gamma + Q _ {2}\right) \\ \end{array}
$$

This loss is less than (11.31) and shows the improved performance if $v(k)$ could be used.
