# Example 10.3 A first order system

Consider the first-order system

$$x (k + 1) = a x (k) + v (k)$$

where v is a sequence of uncorrelated random variables with zero mean values and covariances $r_{1}$ . Let the state at time $k_{0}$ , have the mean $m_{0}$ and the covariance $r_{0}$ . It follows from (10.9) that the mean value

$$m (k) = \operatorname{Ex} (k)$$

is given by

$$m (k + 1) = a m (k) \quad m (k _ {0}) = m _ {0}$$

Hence

$$m (k) = a ^ {k - k _ {0}} m _ {0}$$

Equation (10.11) gives

$$P (k + 1) = a ^ {2} P (k) + r _ {1} \quad P (k _ {0}) = r _ {0}$$

Solving this difference equation we get

$$P (k) = a ^ {2 (k - k _ {0})} r _ {0} + \frac {1 - a ^ {2 (k - k _ {0})}}{1 - a ^ {2}} r _ {1}$$

Furthermore,

$$r _ {x} (l, k) = a ^ {l - k} P (k) \quad l \geq k$$

and

$$r _ {x} (l, k) = a ^ {k - l} P (l) \quad l < k$$

If $|a| < 1$ and $k_0 \to -\infty$ , it follows that

$$
\begin{array}{l} m (k) \rightarrow 0 \\ P (k) \rightarrow \frac {r _ {1}}{1 - a ^ {2}} \\ r _ {x} (k + \tau , k) \rightarrow \frac {r _ {1} a ^ {| \tau |}}{1 - a ^ {2}} \\ \end{array}
$$

The process then becomes stationary because m is constant and the covariance function is a function of $\tau$ only. If an output

$$y (k) = x (k) + e (k)$$

is introduced, where e is a sequence of uncorrelated random variables with zero mean and covariance $r_{2}$ , it follows that the covariance function of y becomes

$$
r _ {y} (\tau) = \left\{ \begin{array}{l l} r _ {2} + \frac {r _ {1}}{1 - a ^ {2}} & \quad \tau = 0 \\ \frac {r _ {1} a ^ {| \tau |}}{1 - a ^ {2}} & \quad \tau \neq 0 \end{array} \right.
$$

The spectral density is obtained from (10.5). Hence

$$
\begin{array}{l} \phi_ {y} (\omega) = \frac {1}{2 \pi} \left(r _ {2} + \frac {r _ {1}}{(e ^ {i \omega} - a) (e ^ {- i \omega} - a)}\right) \\ = \frac {1}{2 \pi} \left(r _ {2} + \frac {r _ {1}}{1 + a ^ {2} - 2 a \cos \omega}\right) \\ \end{array}
$$

![](image/af3ab58d4db666ad64c3f577442db8d305cf2247d34be78db1006321d71d5b46.jpg)  
Figure 10.5 Generation of disturbances by driving dynamic systems with white noise.
