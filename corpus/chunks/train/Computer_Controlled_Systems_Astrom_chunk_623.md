$$r _ {x x} (k + 1, k) = \operatorname{cov} \left(x (k + 1), x (k)\right) = \Phi P (k)$$

Repeating this discussion,

$$r _ {x x} (k + \tau , k) = \Phi^ {\tau} P (k) \quad \tau \geq 0$$

The covariance function is thus obtained by propagating the variance function through a system with the dynamics given by $\Phi$ . The results obtained are so important that they deserve to be summarized.

THEOREM 10.1 FILTERED DISCRETE-TIME WHITE NOISE Consider a random process defined by the linear stochastic-difference equation (10.7), where $\{v(k)\}$ is a white-noise process with zero mean and covariance $R_{1}$ . Let the initial state have mean $m_{0}$ and covariance $R_{0}$ . The mean-value function of the process is then given by

$$m (k + 1) = \Phi m (k) \quad m (0) = m _ {0} \tag {10.9}$$

and the covariance function by

$$r (k + \tau , k) = \Phi^ {\prime} P (k) \quad \tau \geq 0 \tag {10.10}$$

where $P(k) = \operatorname{cov}\left(x(k), x(k)\right)$ is given by

$$P (k + 1) = \Phi P (k) \Phi^ {T} + R _ {1} \quad P (0) = R _ {0} \tag {10.11}$$

Remark 1. If the random variables are Gaussian, then the stochastic process is uniquely characterized by its mean-value function m and its covariance function r.

Remark 2. If the system has an output y = Cx, then the mean-value function of y is given by

$$m _ {y} = C m$$

and its covariance is given by

$$r _ {y y} = C r _ {x x} C ^ {T}$$

The cross-covariance between $y$ and $x$ is given by

$$r _ {y x} = C r _ {x x}$$

Remark 3. Notice that the steady-state solution of (10.11) for the matrix P is closely related to Eq. (3.9), which was used to calculate Lyapunov functions in Chapter 3.

Remark 4. The different terms of (10.11) have good physical interpretations. The covariance P may represent the uncertainty in the state, the term $\Phi P(k)\Phi^{T}$ tells how the uncertainty at time k propagates due to the system dynamics, and the term $R_{1}$ describes the increase of uncertainty due to the disturbance v.
