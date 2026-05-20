$$
\begin{array}{l} \mathbf {E} v = \mathbf {E} e = 0 \\ \operatorname{var} v = 1 \\ \text { var } e = r _ {2} \\ \operatorname{Ev} (k) e (j) = r _ {1 2} \quad \text { when } k = j \text { and } 0 \text { otherwise } \\ \end{array}
$$

Show that $y(k)$ can be represented as the output of a linear filter

$$y (k) = \lambda \frac {q - c}{q - a} \varepsilon (k) \quad | c | \leq 1$$

where $\varepsilon(k)$ is white noise with zero mean and unit variance. Determine $\lambda$ and c.

10.8 Determine the covariance function, $r_{y}(\tau)$ , and the spectrum, $\phi_{y}(\omega)$ , of the process $y(k)$ when

$$y (k) - 0. 7 y (k - 1) = e (k) - 0. 5 e (k - 1)$$

where $e(k)$ is white noise with unit variance.

10.9 Determine the variance of the stochastic process $y(k)$ defined by

$$y (k) - 1. 5 y (k - 1) + 0. 7 y (k - 2) = e (k) + 0. 2 e (k - 1)$$

where e is white noise with unit variance.

10.10 Calculate the stationary covariance function $r_{y}(\tau), \tau = 0, 1, 2, \ldots$ , for the system

$$y (k) = e (k) - 2 e (k - 1) + 3 e (k - 2) - 4 e (k - 3)$$

when e is zero-mean white noise with unit variance.

10.11 Assume that we want to generate a signal $y(k)$ with the spectral density

$$\phi_ {y} (\omega) = \frac {1}{1 . 3 6 + 1 . 2 \cos \omega}$$

(a) Determine a stable filter $H(q)$ that gives the desired signal $y(k) = H(q)e(t)$ , where $e$ is white noise such that $e \in N(0,1)$ .

(b) What is the variance of y?

10.12 Consider the discrete-time system

$$
x (k + 1) = \left( \begin{array}{l l} 0. 3 & 0. 2 \\ 0 & 0. 5 \end{array} \right) x (k) + \left( \begin{array}{l} 0 \\ 1 \end{array} \right) u (k) + v (k)

y (k) = \left( \begin{array}{l l} 1 & 0 \end{array} \right) x (k) + e (k)
$$

Assume that v and e are white-noise processes that are uncorrelated and with the covariances

$$
R _ {1} = \left( \begin{array}{c c} 1 & 0 \\ 0 & 0. 5 \end{array} \right) \quad \text { and } \quad R _ {2} = 0. 2
$$

respectively. Assume that the initial value has the zero-mean value and the covariances

$$\operatorname{cov} \left(x (0), x (0) ^ {T}\right) = I$$

Compute the stationary value of the covariance of the state vector.

10.13 Assume that a white-noise generator is available that gives a zero mean output with unit variance. Determine a filter that can be used to generate a stochastic signal with the spectral density

$$\phi (\omega) - \frac {3}{2 \pi (5 . 4 3 - 5 . 4 0 \cos (\omega))}$$
