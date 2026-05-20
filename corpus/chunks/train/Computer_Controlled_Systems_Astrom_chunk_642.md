# Filtering Continuous-Time Processes

The analysis of linear systems with continuous-time stochastic processes as inputs is analogous to the corresponding analysis for discrete-time systems. Consider a time-invariant stable system with impulse response g. The input-output relationship is

$$y (t) = \int_ {- \infty} ^ {t} g (t - s) u (s) d s = \int_ {0} ^ {t} g (s) u (t - s) d s \tag {10.31}$$

[compare with Eq. (10.12)]. Let the input signal u be a stochastic process with mean-value function $m_{u}$ and covariance function $r_{u}$ .

The following result is analogous to Theorem 10.2 for discrete-time systems.

THEOREM 10.6 FILTERING STATIONARY PROCESSES Consider a stationary linear system with the transfer function G. Let the input signal be a stationary continuous-time stochastic process with mean value $m_{u}$ and spectral density $\phi_{u}$ . If the system is stable, then the output is also a stationary process with the mean value

$$m _ {y} = G (0) m _ {u}$$

and the spectral density

$$\phi_ {y} (\omega) = G (i \omega) \phi_ {u} (\omega) G ^ {T} (- i \omega) \tag {10.32}$$

The cross-spectral density between the input and the output is given by

$$\phi_ {y u} (\omega) = G (i \omega) \phi_ {u} (\omega)$$

The result may be interpreted in the same way as the corresponding result for discrete-time systems. Compare with Remarks 1 and 2 of Theorem 10.2.
