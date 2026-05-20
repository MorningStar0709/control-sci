# Definitions

Continuous-time stochastic processes can be defined in the same way as discrete-time processes. The only difference is that the index set T is the set of real variables instead of a discrete set. Covariance functions and stationary processes are defined as for discrete-time processes using the finite-dimensional distribution functions. A spectral density can also be introduced as the Fourier transform of the covariance function. Equation (10.5) is then replaced by

$$\phi_ {x y} (\omega) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} e ^ {- i \omega t} r _ {x y} (t) d t \tag {10.24}$$

The inverse transform is given by

$$r _ {x y} (t) = \int_ {- \infty} ^ {\infty} e ^ {i \omega t} \phi_ {x y} (\omega) d \omega \tag {10.25}$$

which replaces (10.6). The spectral density has the same interpretation as for discrete-time systems.
