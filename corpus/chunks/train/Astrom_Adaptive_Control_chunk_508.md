# THEOREM 7.1 Conditional distribution of the states

Consider the model of Eq. (7.3) with the output defined by Eq. (7.6), where $e(t)$ and $v(t)$ are independent zero mean Gaussian variables with covariances

$R_{2}$ and $R_{1}$ , respectively. The initial state of the system is given by Eqs. (7.4) and (7.5).

The conditional distribution of $x(t)$ , given $Y_{t-1}$ , is Gaussian with mean $\hat{x}(t)$ and covariance $P(t)$ satisfying the difference equations

$$\hat {x} (t + 1) = \Phi \hat {x} (t) + K (t) \left(y (t) - \varphi^ {T} (t - 1) \hat {x} (t)\right)P (t + 1) = \left(\Phi - K (t) \varphi^ {T} (t - 1)\right) P (t) \Phi^ {T} + R _ {1} \tag {7.9}K (t) = \Phi P (t) \varphi (t - 1) \left(R _ {2} + \varphi^ {T} (t - 1) P (t) \varphi (t - 1)\right) ^ {- 1}$$

with the initial conditions

$$\hat {x} (0) = mP (0) = R _ {0}$$

Furthermore, the conditional distribution of $y(t)$ , given $\mathcal{Y}_t$ is Gaussian with mean value

$$m _ {y} (t) = \varphi^ {T} (t - 1) \hat {x} (t)$$

and covariance

$$\sigma_ {y} ^ {2} (t) = R _ {2} + \varphi^ {T} (t - 1) P (t) \varphi (t - 1)$$

Proof: If $\varphi(t-1)$ is a known time-varying vector, then the theorem is identical to the Kalman filtering theorem, which can be found in standard textbooks on stochastic control. Going through the details of the proof of the Kalman filtering theorem, we find that it is still valid, since $\varphi(t-1)$ is a function of $\mathcal{Y}_{t-1}$ . In other words, the vector $\varphi(t-1)$ is not known in advance, but it is known when it is needed in the computations.

Remark. Notice that the conditional distribution of $y(t)$ , given $\mathcal{Y}_{t-1}$ , is Gaussian even if $y(t)$ is not Gaussian.

The estimation problem is thus easily solved for the model structure chosen. The conditional distribution of the state of the system is called the hyperstate. The distribution is Gaussian in the problem under consideration. It is then sufficient to consider the mean and covariance of $x(t)$ . Further, some of the old inputs and outputs must be stored to compute the distribution defined in Eqs. (7.9). In the problem under consideration the hyperstate is finite-dimensional and can be characterized by the triple

$$
\xi (t) = \left( \begin{array}{c c c} \tilde {\varphi} (t - 1) & \hat {x} (t) & P (t) \end{array} \right) \tag {7.10}
$$

where

$$\tilde {\varphi} ^ {T} (t - 1) = \left(0 u (t 2) \dots u (t - n) - y (t - 1) \dots - y (t - n)\right) \tag {7.11}$$

The vector $\bar{\varphi}^{T}(t-1)$ is the same as $\varphi^{T}(t-1)$ , except that $u(t-1)$ is replaced by a zero. The updating of the hyperstate is given by Theorem 7.1 and the definition of $\bar{\varphi}^{T}(t-1)$ . In the general case the conditional probability distribution is not Gaussian. This will considerably increase the computational difficulties and the storage requirements.
