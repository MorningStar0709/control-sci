11.8 Consider the ship-steering problem characterized by the model of (11.41) and the loss function in (11.42). Use the numbers $a_{11} = -0.454$ , $a_{12} = -0.433$ , $a_{21} = -4.005$ , $a_{22} = -0.807$ , $b_{1} = 0.097$ , $b_{2} = -0.807$ , $\alpha = 0.014$ , and $\rho = 0.08$ . Determine the optimal state feedback when h = 5 s.

11.9 The ship-steering problem is sometimes approximated further by using the second-order model

$$
\frac {d}{d t} \binom{\Psi}{r} = \left( \begin{array}{c c} 0 & 1 \\ 0 & - \alpha \end{array} \right) \binom{\Psi}{r} + \binom{0}{k} \delta
$$

and the following approximation of the loss function:

$$J = \lim _ {T \rightarrow \infty} \frac {1}{T} \int_ {0} ^ {T} (\Psi^ {2} + \rho \delta^ {2}) d t$$

Determine the optimal feedback for a sampled regulator. Use the parameters $\alpha = 0.001$ , k = 0.0005, and $\rho = 0.08$ , and the sampling period h = 5 s.

11.10 Consider the LQ-controller determined in Problem 11.5 for the inventory model. Use (11.39) to determine the gain margin.

11.11 A stochastic process is generated as

$$x (k + 1) = 0. 5 x (k) + v (k)y (k) = x (k) + e (k)$$

where v and e are uncorrelated white-noise processes with the covariances $r_{1}$ and $r_{2}$ , respectively. Further, $x(0)$ is normally distributed with zero mean and variance $r_{0}$ . Determine the Kalman filter for the system. What is the gain in steady state? Compute the pole of the steady-state filter and compare with the pole of the system.

11.12 The double integrator with process noise can be described by

$$
x (k + 1) = \left( \begin{array}{l l} 1 & 1 \\ 0 & 1 \end{array} \right) x (k) + \binom {0. 5} {1} u (k) + \binom {0} {1} v (k)

y (k) = \left( \begin{array}{c c} 1 & 0 \end{array} \right) x (k)
$$

where $v(k)$ is a sequence of independent, normal, zero-mean, random variables with unit variance. Assume that $x(0)$ is normal with mean $\mathbf{Ex}(0) = [1 \cdot 1]^{T}$ and the covariance matrix $R_{0} = 3 \cdot I$ .

(a) Determine the equations for the covariance matrix of the reconstruction error and the gain vector in the Kalman filter.

(b) Simulate the covariance and gain equations and determine the speed of convergence and the steady-state values.

11.13 Consider the double integrator in Problem 11.12, but let the output be

$$
y (k) = \left( \begin{array}{l l} 1 & 0 \end{array} \right) x (k) + v (k)
$$

(a) Determine the equations for the covariance matrix of the reconstruction error and the gain vector in the Kalman filter.
