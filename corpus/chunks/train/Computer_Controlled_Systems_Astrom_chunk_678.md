# The Kalman Filter

Let the process be described by (11.3) with h = 1. Postulate an one-step-ahead estimator of the form

$$\hat {x} (k + 1 \mid k) = \Phi \hat {x} (k \mid k - 1) + \Gamma u (k) + K (k) \left(y (k) - C \hat {x} (k \mid k - 1)\right) \tag {11.43}$$

The reconstruction error $\tilde{x} = x - \hat{x}$ is governed by

$$
\begin{array}{l} \tilde {x} (k + 1) = \Phi \tilde {x} (k) + v (k) - K (k) (y (k) - C \hat {x} (k \mid k - 1)) \\ = (\Phi - K (k) C) \tilde {x} (k) + v (k) - K (k) e (k) \tag {11.44} \\ = \left( \begin{array}{l l} I & - K (k) \end{array} \right) \left(\left( \begin{array}{l} \Phi \\ C \end{array} \right) \tilde {x} (k) + \left( \begin{array}{l} v (k) \\ e (k) \end{array} \right)\right) \\ \end{array}
$$

In Sec. 4.4 K is used to give the system of (11.44) desired eigenvalues. The problem is approached differently here: The properties of the noise are taken into account and the criterion is to minimize the variance of the estimation error, which is denoted by $P(k)$ .

$$P (k) = \mathbf {E} (\tilde {x} (k) - \mathbf {E} \tilde {x} (k)) (\tilde {x} (k) - \mathbf {E} \tilde {x} (k)) ^ {T}$$

The mean value of $\tilde{x}$ is obtained from (11.44)

$$\mathbf {E} \tilde {x} (k + 1) = (\Phi - K (k) C) \mathbf {E} \tilde {x} (k)$$

Because $E x(0) = m_{0}$ , the mean value of the reconstruction error is zero for all times $k \geq 0$ independent of K if $\hat{x}(0) = m_{0}$ . Because $\bar{x}(k)$ is independent of $v(k)$ and $e(k)$ Eq. (11.44) now gives

$$
\begin{array}{l} P (k + 1) = \mathrm{E} \bar {x} (k + 1) \tilde {x} (k + 1) ^ {T} \\ = \left( \begin{array}{c c} I & - K (k) \end{array} \right) \left(\left( \begin{array}{l} \Phi \\ C \end{array} \right) P (k) \binom{\Phi}{C} ^ {T} + \left( \begin{array}{c c} R _ {1} & R _ {1 2} \\ R _ {1 2} ^ {T} & R _ {2} \end{array} \right)\right) \binom{I}{- K ^ {T} (k)} \\ = \left( \begin{array}{l l} I & - K (k) \end{array} \right) \left( \begin{array}{c c} \Phi P (k) \Phi^ {T} + R _ {1} & \Phi P (k) C ^ {T} + R _ {1 2} \\ C P (k) \Phi^ {T} + R _ {1 2} ^ {T} & C P (k) C ^ {T} + R _ {2} \end{array} \right) \left( \begin{array}{c} I \\ - K ^ {T} (k) \end{array} \right) \tag {11.45} \\ \end{array}
$$

Further, $P(0) = R_0$ . From (11.45) it follows that if $P(k)$ is positive semidefinite, then $P(k + 1)$ is also positive semidefinite. Equation(11.45) has the same form as (11.11) and should be minimized with respect to $K(k)$ . By using the idea of completion of squares, it follows that $\alpha^T P(k + 1)\alpha$ is minimized by $K(k)$ satisfying
