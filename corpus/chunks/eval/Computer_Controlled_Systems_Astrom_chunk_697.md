(b) Simulate the covariance and gain equations and determine the speed of convergence and the steady-state values.

11.14 Given the system

$$
x (k + 1) = \left( \begin{array}{l l} 1 & 1 \\ 0 & 1 \end{array} \right) x (k) + \binom {0} {1} v (k) + \binom {0. 5} {1}

y (k) = \left( \begin{array}{c c} 1 & 0 \end{array} \right) x (k)
$$

where $v(k)$ is zero-mean white noise with standard deviation 0.1. Assume the $x(0)$ is known exactly. Determine the estimate of $x(k+3)$ , given $y(k)$ that minimizes the prediction error. Use that to determine the best estimate of $y(3)$ and its variance.

11.15 The signal $x(k)$ is defined as

$$x (k + 1) = a x (k) + v (k)y (k) = x (k) + e (k)$$

where v and e are independent white-noise processes with zero mean. The variances are 1 and $\sigma$ , respectively. The signal x is estimated using exponential smoothing as

$$\hat {x} (k \mid k) = \alpha \hat {x} (k - 1) \mid k - 1) + (1 - \alpha) y (k)$$

Determine an expression for how the variance of the estimation error depends on the parameters $\alpha$ and $\sigma$ . Compare with the steady-state optimal Kalman filter.

11.16 Show that Theorem 11.5 can be generalized to the situation when the disturbances $e(k)$ and $v(k)$ have constant but unknown mean values. (Compare with Sec. 4.5.)

11.17 A constant variable x is measured through two different sensors. The measurements are noisy and have different accuracy. Let the system be described by

$$
\begin{array}{l} x (k + 1) = x (k) \\ y (k) = C x (k) + e (k) \\ \end{array}
$$

where $C^{T} = [1\ 1]$ and $e(k)$ is a zero-mean white-noise vector with the covariance matrix

$$
R _ {2} = \left( \begin{array}{l l} 1 & 0 \\ 0 & 9 \end{array} \right)
$$

Estimate x as

$$\hat {x} (k) = a _ {1} y _ {1} (k) + a _ {2} y _ {2} (k)$$

Determine the constants $a_{1}$ and $a_{2}$ such that the mean value of the prediction error is zero and such that the variance of the prediction error is as low as possible. Compare the minimum variance with the cases when only one of the measurements is used. Compare the solution with the Kalman filter.

11.18 Prove that the filter estimate given by (11.50) to (11.54) is the optimal filter in the sense that the variance of the estimation error is minimized.

11.19 Consider the design of a Kalman filter for estimating the velocity in a motor drive based on angle measurements. The basic dynamics of the motor, which relate the angle to the current, is given by

$$G (s) = \frac {1}{s (s + 1)}$$
