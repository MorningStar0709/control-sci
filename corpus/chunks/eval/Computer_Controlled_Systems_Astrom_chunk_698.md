Assume that there are low-frequency disturbances (friction) that are modeled as

$$z _ {1} (k h + h) = z _ {1} (k h) + w _ {1} (k h)$$

Also assume that it is desirable to filter out disturbances because of a mechanical resonance at the frequency $\omega$ . This signal is modeled as the signal obtained by driving a system with the transfer function

$$G (s) = \frac {\omega^ {2}}{s ^ {2} + 2 \zeta \omega s + \omega^ {2}}$$

with white noise. Determine the Bode diagrams for the Kalman filter for $\zeta = 0.05$ , $\omega = 0.1$ , and $\omega = 2$ . Let the sampling period be 0.05 s. Also investigate the influence of different relative intensities of the low-frequency and the band-limited disturbance.

11.20 Consider the system

$$
x (k + 1) = \left( \begin{array}{c c} 1. 4 5 & - 0. 4 5 \\ 1 & 0 \end{array} \right) x (k) + \binom {1} {0} u (k)

y (k) = \left( \begin{array}{l l} 0. 5 & 0. 3 8 \end{array} \right) x (k)
$$

Determine the stationary controller $u(k) = -Lx(k)$ that minimizes the loss function

$$J = \sum_ {k = 1} ^ {\infty} x ^ {T} (k) C ^ {T} C x (k)$$

11.21 A computer is used to control the velocity of a motor. Let the process be described by

$$x (k + 1) = 0. 5 x (k) + u (k)y (k) = x (k) + e (k)$$

where x is the velocity, u is the input voltage, and y is the tachometer measurement of the velocity. The measurement noise is white noise with the variance $\sigma^{2}$ . Assume that the initial speed is a stochastic variable with zero mean and unit variance. Construct a controller that minimizes the loss function

$$\mathrm{E} \left(x (2) ^ {2} + \sum_ {k = 0} ^ {1} \rho u ^ {2} (k)\right)$$

The parameter $\rho$ is used to control the amplitude of the control signal. It is further desired that the velocity be as small as possible after two sampling intervals.

(a) Determine the optimal controller when $\sigma = 0$ and the regulator parameters when $\rho = 1, \rho = 0.1$ , and when $\rho \to 0$ .

(b) Determine the optimal controller when the measurement noise has the variance $\sigma^{2}=1$ .

11.22 Given the system

$$x (k + 1) = x (k) + v (k)y _ {1} (k) = x (k) + e _ {1} (k)y _ {2} (k) = x (k) + e _ {2} (k)$$

where $v \in N(0,0.1)$ , $e_{1} \in N(0,\sigma_{1})$ , and $e_{2} \in N(0,\sigma_{2})$ ; and v, $e_{1}$ , and $e_{2}$ are mutually uncorrelated.

(a) Determine the Kalman filter that gives $\hat{x}(k \mid k - 1)$ for the system.   
(h) Compute the stationary variance when $\sigma_{1} = 1$ and $\sigma_{2} = 2$ .   
(c) Compute the stationary gain when $\sigma_{1} = 1$ and $\sigma_{2} = 2$ .
