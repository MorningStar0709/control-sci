# The Model

Consider the discrete-time, single-input, single-output system

$$y (t) + a _ {1} (t) y (t - 1) + \dots + a _ {n} (t) y (t - n) =b _ {0} (t) u (t - 1) + \dots + b _ {n - 1} (t) u (t - n) + e (t) \tag {7.1}$$

where y, u, and e are output, input, and disturbance, respectively. The noise sequence $\{e(t)\}$ is assumed to be Gaussian with zero mean and variance $R_{2}$ . Further, it is assumed that $e(t)$ is independent of $y(t-1)$ , $y(t-2)$ , $\ldots$ , $u(t-1)$ , $u(t-2)$ , $\ldots$ , $a_{i}(t)$ , $a_{i}(t-1)$ , $\ldots$ , and $b_{i}(t)$ , $b_{i}(t-1)$ , $\ldots$ . It is further assumed that $b_{0}(t) \neq 0$ and that the system is minimum-phase for all t. The time-varying parameters

$$
x (t) = \left( \begin{array}{c c c c c} b _ {0} (t) & \dots & b _ {n - 1} (t) & a _ {1} (t) & \dots & a _ {n} (t) \end{array} \right) ^ {T} \tag {7.2}
$$

are modeled by a Gauss-Markov process, which satisfies the stochastic difference equation

$$x (t + 1) = \Phi x (t) + v (t) \tag {7.3}$$

where $\Phi$ is a known constant matrix and $\{v(t)\}$ is a sequence of independent, equally distributed normal vectors with zero mean value and known covariance

$R_{1}$ . The initial state of the system in Eq. (7.3) is assumed to be normally distributed with mean value

$$E x (0) = m \tag {7.4}$$

and covariance

$$\operatorname{cov} \left\{x (0), x (0) \right\} = R _ {0} \tag {7.5}$$

It is assumed that $e(t)$ is independent of $v(t)$ and of $x(0)$ .

The input-output relation of the system of Eq. (7.1) can be written in the compact form

$$y (t) = \varphi^ {T} (t - 1) x (t) + e (t) \tag {7.6}$$

where

$$
\varphi^ {T} (t - 1) = \left( \begin{array}{c c c c c} u (t - 1) & \dots & u (t - n) & - y (t - 1) & \dots & - y (t - n) \end{array} \right) \tag {7.7}
$$

The model is thus defined by Eqs. (7.3) and (7.6).
