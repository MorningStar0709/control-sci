# White Noise

White noise is defined as a stationary process with constant spectral density. If

$$\phi (\omega) = \frac {r _ {0}}{2 \pi}$$

it follows formally from (10.25) that the corresponding covariance is a delta function, that is,

$$r (t) = r _ {0} \delta (t)$$

Continuous-time white noise thus has the property that values of the signal at different times are uncorrelated as for discrete-time white noise. Continuous-time white noise has, however, infinite variance. This will cause some mathematical difficulties. Intuitively, continuous-time white noise is analogous to delta functions in the theory of linear systems.

Some of the difficulties with continuous-time white noise can be avoided by introducing a stochastic process that formally is the time integral

$$w (t) = \int_ {0} ^ {t} e (s) d s$$

of white noise e. The stochastic process w has zero mean value. Its increments over disjoint intervals are uncorrelated. If the covariance function of e is

$$\operatorname{cov} \left(e (t), e (s)\right) = r _ {0} \delta (t - s)$$

then the variances of the increments of w are given by

$$\mathbf {E} \Big (w (t) - w (s) \Big) ^ {2} = | t - s | \cdot r _ {0}$$

The stochastic process $\{w(t), t \in T\}$ is called a Wiener process if it also is Gaussian. The Wiener process is a model for random walk. The infinitesimal increment

$$d w = w (t + d t) - w (t)$$

has the variance

$$\mathbf {E} (d w) ^ {2} = r _ {0} d t$$

The increment dw thus has the magnitude $\sqrt{r_{0}dt}$ in the mean-square sense. The number $r_{0}dt$ is called the incremental covariance of the Wiener process.
