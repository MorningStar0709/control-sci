where $v(k)$ is a random variable with zero mean and covariance $R_{1}$ that is independent of $x(k)$ and independent of all past values of x. This implies that $v(k)$ also is independent of all past v's. The sequence $\{v(k), k = \ldots, -1, 0, 1, \ldots\}$ is a sequence of independent equally distributed random variables. The stochastic process $\{v(k)\}$ is thus discrete-time white noise. Equation (10.7) is called a linear stochastic-difference equation. To define the random process $\{x(k)\}$ completely, it is necessary to specify the initial conditions. It is assumed that initial state has the mean $m_{0}$ , and the covariance matrix $R_{0}$ .

Properties of linear stochastic-difference equations. The character of the random process defined by the linear stochastic-difference equation of (10.7) will now be investigated and the first and second moments of the process will be calculated. To obtain the mean-value function

$$m (k) = \operatorname{Ex} (k)$$

simply take the mean values of both sides of (10.7). Because v has zero mean, the following difference equation is obtained:

$$m (k + 1) = \Phi m (k) \tag {10.8}$$

The initial condition is

$$m (0) = m _ {0}$$

The mean value will thus propagate in the same way as the unperturbed system. To calculate the covariance function, we introduce

$$P (k) = \operatorname{cov} \Bigl (x (k), x (k) \Bigr) = \operatorname{E} \tilde {x} (k) \tilde {x} ^ {T} (k)$$

where

$$\tilde {x} = x - m$$

It follows from Eqs. (10.7) and (10.8) that $\tilde{x}$ satisfies Eq. (10.7) with the mean of the initial condition equal zero. The mean value can thus be treated separately. To calculate the covariance, form the expression

$$
\begin{array}{l} \tilde {x} (k + 1) \tilde {x} ^ {T} (k + 1) = (\Phi \tilde {x} (k) + v (k)) (\Phi \tilde {x} (k) + v (k)) ^ {T} \\ = \Phi \tilde {x} (k) \tilde {x} ^ {T} (k) \Phi^ {T} + \Phi \tilde {x} (k) v ^ {T} (k) + v (k) \tilde {x} ^ {T} (k) \Phi^ {T} + v (k) v ^ {T} (k) \\ \end{array}
$$

Taking mean values gives

$$P (k + 1) = \Phi P (k) \Phi^ {T} + R _ {1}$$

because $v(k)$ and $\bar{x}(k)$ are independent. The initial conditions are

$$P (0) = R _ {0}$$

The recursive equation for $P$ tells how the covariance propagates. To calculate the covariance function of the state, observe that

$$\tilde {x} (k + 1) \tilde {x} ^ {T} (k) = \Big (\Phi \tilde {x} (k) + v (k) \Big) \tilde {x} ^ {T} (k)$$

Because $v(k)$ and $\tilde{x}(k)$ are independent and $v(k)$ has zero mean,
