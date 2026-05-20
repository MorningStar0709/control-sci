A stochastic process is called stationary if the finite-dimensional distribution of $x(t_{1}), x(t_{2}), \ldots, x(t_{n})$ is identical to the distribution of $x(t_{1} + \tau), x(t_{2} + \tau), \ldots, x(t_{n} + \tau)$ for all $\tau, n, t_{1}, \ldots, t_{n}$ . The process is called weakly stationary if the first two moments of the distributions are the same for all $\tau$ . The mean-value function of a (weakly) stationary process is constant. The cross-covariance function of weakly stationary processes is a function of the difference s - t of the arguments only. With some abuse of function notation, write

$$r _ {x y} (s, t) = r _ {x y} (s - t)$$

The cross-covariance function of (weakly) stationary processes is a function of one argument only. Hence

$$r _ {x v} (\tau) = \operatorname{cov} (x (t + \tau), y (t))$$

When $x$ is scalar the function

$$r _ {x} (\tau) = r _ {x x} (\tau) = \operatorname{cov} (x (t + \tau), x (t))$$

called the autocovariance function.

The cross-spectral density of (weakly) stationary processes is the Fourier transform of its covariance function. Hence,

$$\phi_ {x y} (\omega) = \frac {1}{2 \pi} \sum_ {k = - \infty} ^ {\infty} r _ {x y} (k) e ^ {- i k \omega} \tag {10.5}$$

and

$$r _ {x y} (k) = \int_ {- \pi} ^ {\pi} e ^ {i k \omega} \phi_ {x y} (\omega) d \omega \tag {10.6}$$

It is also customary to refer to $\phi_{xx}$ and $\phi_{xy}$ as the autospectral density and the cross-spectral density, respectively. The autospectral density is also called spectral density for simplicity.

Interpretation of covariances and spectra. Stationary Gaussian processes are completely characterized by their mean-value functions and their covariance functions. In applications, it is useful to have a good intuitive understanding of how the properties of a stochastic process are reflected by these functions.

The mean-value function is almost self-explanatory. The value $r_{x}(0)$ of the covariance function at the origin is the variance of the process. It tells how large the fluctuations of the process are. The standard deviation of the variations is equal to the square root of $r_{x}(0)$ . If the covariance function is normalized by $r_{x}(0)$ , the correlation function, which is defined by

$$\rho_ {x} (\tau) = \frac {r _ {x} (\tau)}{r _ {x} (0)}$$

is obtained. It follows from Schwartz's inequality that

$$\left| r _ {x} (\tau) \right| \leq r _ {x} (0)$$
