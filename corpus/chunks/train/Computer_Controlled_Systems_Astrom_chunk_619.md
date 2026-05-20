# Discrete-Time White Noise

A simple and useful random process is now introduced. Let time be the set of integers. Consider a stationary discrete-time stochastic process x such that $x(t)$ and $x(s)$ are independent if $t \neq s$ . The stochastic process can thus be considered as a sequence $\{x(t, \omega), t = \ldots, -1, 0, 1, \ldots\}$ of independent, equally distributed random variables. The covariance function is given by

$$
r (\tau) = \left\{ \begin{array}{l l} \sigma^ {2} & \quad \tau = 0 \\ 0 & \quad \tau = \pm 1, \pm 2, \dots \end{array} \right.
$$

![](image/65217f023402177e1d17a92b45dafadfbfc56af7853dd87e13b5a2983c4e95b8.jpg)  
Figure 10.4 Covariance functions, spectral densities, and sample functions for some stationary random processes. All processes have unit variance.

A process with this covariance function is called discrete-time white noise. It follows from (10.5) that the spectral density is given by

$$\phi (\omega) = \frac {\sigma^ {2}}{2 \pi}$$

The spectral density is thus constant for all frequencies. The analogy with the spectral properties of white light explains the name given to the process. White noise plays an important role in stochastic control theory. All stochastic processes that are needed will be generated simply by filtering white noise. This also implies that only a white-noise generator is needed when simulating stochastic processes. White noise is thus the equivalent of pulses for deterministic systems.
